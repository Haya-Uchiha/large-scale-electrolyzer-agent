"""
500 cm² Stacked CO2RR Electrolyzer — Control Software
======================================================

Runnable prototype controller for a 5×100 cm² stacked AEM-MEA electrolyzer.
Includes simulation mode for testing the entire control loop without hardware.

Usage
-----
    # Run a 24 h simulated experiment with simulated faults:
    python electrolyzer_control.py --simulate --duration 24

    # Run for 1 hour with fast-time scaling (1 sec real = 60 sec sim):
    python electrolyzer_control.py --simulate --duration 1 --time-scale 60

    # Connect real hardware (requires --hardware flag and config):
    python electrolyzer_control.py --hardware --config hardware.yaml

Architecture
------------
    ElectrolyzerController
    ├── HardwareInterface (abstract)
    │   ├── SimulatedHardware (built-in physics-lite model + fault injection)
    │   └── RealHardware       (NI DAQmx + Modbus + serial — stubbed)
    ├── DataLogger             (CSV + event log with rotation)
    ├── AlarmManager           (thresholds → warnings + abort)
    └── SafetyInterlock        (graceful abort sequence)
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import logging
import math
import random
import signal
import sys
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from enum import Enum
from pathlib import Path
from typing import Optional


# =============================================================================
# CONSTANTS — operating setpoints (Run #1 conditions)
# =============================================================================

NUM_CELLS = 5
ACTIVE_AREA_PER_CELL = 100.0          # cm²
TARGET_CURRENT_DENSITY = 100.0        # mA/cm²
TARGET_STACK_CURRENT = (
    TARGET_CURRENT_DENSITY * ACTIVE_AREA_PER_CELL / 1000.0
)                                      # A → 10 A
TARGET_PER_CELL_CO2_FLOW = 350.0      # ml/min (3.5 ml/min/cm²)
TARGET_TOTAL_CO2_FLOW = TARGET_PER_CELL_CO2_FLOW * NUM_CELLS  # 1750 ml/min
TARGET_ANOLYTE_FLOW_TOTAL = 500.0     # ml/min
TARGET_TEMPERATURE = 50.0             # °C
TARGET_ACID_CONC_M = 0.5              # M CH3COOH

# Alarm thresholds (per spec section 9)
V_CELL_ABS_MIN = 2.5                   # V — abort below this
V_CELL_ABS_MAX = 4.5                   # V — abort above this
V_STACK_MAX = 22.0                     # V
V_CELL_DEVIATION_ABORT = 0.30          # V from initial steady-state
V_CELL_DEVIATION_WARN = 0.15           # V from 1h moving avg
PRESSURE_RISE_ABORT_FRAC = 0.30        # 30% above initial
PRESSURE_RISE_WARN_FRAC = 0.20
PH_REFRESH_RECOMMEND = 7.0
FE_CO_TARGET_MIN = 80.0                # %

# Galvanic Faraday for CO2RR→CO at 2 e⁻/mol
FARADAY = 96485.0  # C/mol


# =============================================================================
# DATA STRUCTURES
# =============================================================================

class RunState(Enum):
    IDLE = "idle"
    HEATING = "heating"
    PURGING = "purging"
    CO2_RAMP = "co2_ramp"
    OCV = "ocv"
    GALVANOSTATIC = "galvanostatic"
    SHUTDOWN = "shutdown"
    ABORTED = "aborted"


@dataclass
class Sample:
    """One time-step measurement of the entire system."""
    t_iso: str
    t_seconds: float
    state: str
    stack_V: float
    stack_I: float
    cell_V: list[float]                  # 5 values
    flow_cell: list[float]               # 5 values, ml/min
    pressure_CO2_inlet_bar: float
    T_endplate_neg: float
    T_endplate_pos: float
    T_anolyte: float
    T_humidifier: float
    anolyte_pH: float
    anolyte_level_pct: float
    fe_co_pct: Optional[float] = None    # GC, every 1 h
    fe_h2_pct: Optional[float] = None
    spu_pct: Optional[float] = None
    alarm_state: str = "OK"
    abort_flag: bool = False


@dataclass
class AlarmEvent:
    t_iso: str
    severity: str       # WARN or ABORT
    code: str
    message: str
    sample: Optional[Sample] = None


# =============================================================================
# HARDWARE INTERFACE (abstract)
# =============================================================================

class HardwareInterface(ABC):
    @abstractmethod
    def read_cell_voltages(self) -> list[float]: ...
    @abstractmethod
    def read_stack_current(self) -> float: ...
    @abstractmethod
    def read_per_cell_flows(self) -> list[float]: ...
    @abstractmethod
    def read_pressure_CO2_inlet(self) -> float: ...
    @abstractmethod
    def read_temperatures(self) -> dict[str, float]: ...
    @abstractmethod
    def read_anolyte_pH(self) -> float: ...
    @abstractmethod
    def read_anolyte_level(self) -> float: ...

    @abstractmethod
    def set_galvanostat_current(self, amps: float) -> None: ...
    @abstractmethod
    def galvanostat_to_OCV(self) -> None: ...
    @abstractmethod
    def set_co2_flow(self, ml_per_min: float) -> None: ...
    @abstractmethod
    def close_co2_solenoid(self) -> None: ...
    @abstractmethod
    def set_anolyte_pump(self, ml_per_min: float) -> None: ...
    @abstractmethod
    def set_heater_setpoint(self, channel: str, celsius: float) -> None: ...

    @abstractmethod
    def trigger_GC_injection(self) -> tuple[float, float, float]:
        """Return (FE_CO_pct, FE_H2_pct, SPU_pct)."""

    @abstractmethod
    def is_safe_to_run(self) -> bool:
        """Hardware E-stop, gas detectors, level switch — all OK."""


# =============================================================================
# SIMULATED HARDWARE — physics-lite model with fault injection
# =============================================================================

class SimulatedHardware(HardwareInterface):
    """
    Simple time-stepping model that mimics the salt-formation failure cascade.

    Failure model:
      - K+ accumulates at AEM/cathode interface at a rate proportional to
        current, attenuated by temperature (Biemolt) and by acid vapor flux.
      - When K+ exceeds threshold in any cell, that cell's CO2 inlet starts
        clogging (modeled as gradual flow restriction).
      - Once flow drops below a threshold, GDE flooding begins — cell V drops,
        FE(CO) drops.
      - Without intervention, failure is irreversible.

    Fault injection: an optional fault scenario can be activated via CLI flag
    to force a specific cell to fail at a specific time (for alarm testing).
    """

    def __init__(self, time_scale: float = 1.0, fault_scenario: str | None = None):
        self.time_scale = time_scale
        self.fault_scenario = fault_scenario

        self.t0 = time.monotonic()
        self.galv_current = 0.0
        self.co2_setpoint = 0.0
        self.anolyte_pump_setpoint = 0.0
        self.heater_setpoints = {
            "anolyte": 25.0, "humidifier": 25.0, "endplate": 25.0
        }

        # Per-cell state
        self.cell_K_accum = [0.0] * NUM_CELLS         # μmol/cm² at AEM interface
        self.cell_blockage_frac = [0.0] * NUM_CELLS   # 0–1, fraction blocked
        self.cell_flow_actual = [TARGET_PER_CELL_CO2_FLOW] * NUM_CELLS
        self.cell_initial_V = [3.45] * NUM_CELLS
        self.cell_V = [3.45] * NUM_CELLS

        # System state
        self.T_endplate_neg = 25.0
        self.T_endplate_pos = 25.0
        self.T_anolyte = 25.0
        self.T_humidifier = 25.0
        self.anolyte_pH = 8.6
        self.anolyte_level_pct = 95.0
        self.pressure_CO2_initial = 1.20  # bar gauge
        self.pressure_CO2_now = 1.20

        self.galvanostat_enabled = False
        self.co2_solenoid_open = True
        self.estop_pressed = False

        self.last_step_t = self.t0

    # ---- internal sim step ----
    def _advance(self):
        now = time.monotonic()
        dt_real = now - self.last_step_t
        dt_sim = dt_real * self.time_scale  # seconds of simulated time
        self.last_step_t = now

        # Heater dynamics (1st-order, tau ~ 600 s real)
        for ch, key in [("anolyte", "T_anolyte"),
                        ("humidifier", "T_humidifier"),
                        ("endplate", "T_endplate_neg")]:
            target = self.heater_setpoints[ch]
            current = getattr(self, key)
            tau = 600.0
            new = current + (target - current) * (1 - math.exp(-dt_sim / tau))
            setattr(self, key, new)
        self.T_endplate_pos = self.T_endplate_neg + random.uniform(-0.5, 0.5)

        # Acid vapor flux: scales with humidifier T and acid conc setpoint
        # Effective acid flux index (1.0 = the proven 5cm² baseline)
        # Baseline: 0.5 M @ 4 ml/min/cm² → 2.0 normalized
        # Now:      0.5 M @ 3.5 ml/min/cm² → 1.75 normalized at 50°C
        # At 25°C with 0.05 M @ 2 ml/min/cm² → 0.10 (the 100 cm² failure case)
        # We'll fix this at the Run #1 setpoint values.
        acid_flux = 1.75 if self.T_humidifier > 45 else 0.10

        # K+ accumulation rate per cell:
        # base_rate proportional to local current density
        # Temperature attenuation: 50°C → 50× lower than 25°C (Biemolt)
        # Acid vapor attenuation: dissolves K+ as KAc, scales linearly with flux
        if self.galvanostat_enabled and self.galv_current > 0.1:
            base_rate = 0.035  # μmol/cm²/s at 25°C, dry, per A
            T_factor = math.exp(-(self.T_anolyte - 25.0) * math.log(50) / 25.0)
            acid_factor = max(0.05, 1.0 - 0.95 * acid_flux / 2.0)
            for i in range(NUM_CELLS):
                # Cell-to-cell variation in K+ (simulates manifold non-uniformity)
                cell_var = 1.0 + 0.05 * (i - 2)
                rate = (base_rate
                        * (self.galv_current / NUM_CELLS) / 10.0
                        * T_factor * acid_factor * cell_var)
                self.cell_K_accum[i] += rate * dt_sim

        # Fault injection
        if self.fault_scenario == "cell3_fail_at_5h":
            sim_elapsed = (now - self.t0) * self.time_scale
            if sim_elapsed > 5 * 3600:
                self.cell_K_accum[2] += 0.2 * dt_sim  # accelerate cell 3

        # Salt blockage: when K_accum exceeds threshold, flow restricts
        K_threshold = 80.0  # μmol/cm² before crystals start blocking
        for i in range(NUM_CELLS):
            if self.cell_K_accum[i] > K_threshold:
                excess = self.cell_K_accum[i] - K_threshold
                self.cell_blockage_frac[i] = min(0.95, excess / 200.0)

        # Per-cell CO2 flow: nominal minus blockage
        for i in range(NUM_CELLS):
            target = self.co2_setpoint / NUM_CELLS
            self.cell_flow_actual[i] = target * (1 - self.cell_blockage_frac[i])

        # CO2 inlet pressure rises with total blockage
        avg_block = sum(self.cell_blockage_frac) / NUM_CELLS
        self.pressure_CO2_now = self.pressure_CO2_initial * (1 + 0.6 * avg_block)

        # Cell voltages: drop as blockage worsens (the serpentine fingerprint)
        for i in range(NUM_CELLS):
            base = self.cell_initial_V[i]
            block = self.cell_blockage_frac[i]
            # Salt-blockage-induced voltage drop (per voltage_fingerprint_analysis):
            #   E_rev shift: -0.11 V × block
            #   iR drop:     -0.15 V × block (flooding lowers ohmic)
            #   net:         up to -0.26 V at full blockage
            v_drop = -0.26 * block
            noise = random.gauss(0, 0.005)
            if self.galvanostat_enabled:
                self.cell_V[i] = base + v_drop + noise
            else:
                self.cell_V[i] = 0.0

        # Anolyte pH drift: drops over time as carbonate accumulates
        if self.galvanostat_enabled:
            pH_drift_rate = 0.04 / 3600.0  # pH units per second of sim time
            self.anolyte_pH = max(6.5, self.anolyte_pH - pH_drift_rate * dt_sim)

    # ---- read methods ----
    def read_cell_voltages(self) -> list[float]:
        self._advance()
        return list(self.cell_V)

    def read_stack_current(self) -> float:
        return self.galv_current if self.galvanostat_enabled else 0.0

    def read_per_cell_flows(self) -> list[float]:
        return list(self.cell_flow_actual)

    def read_pressure_CO2_inlet(self) -> float:
        return self.pressure_CO2_now

    def read_temperatures(self) -> dict[str, float]:
        return {
            "endplate_neg": self.T_endplate_neg,
            "endplate_pos": self.T_endplate_pos,
            "anolyte": self.T_anolyte,
            "humidifier": self.T_humidifier,
        }

    def read_anolyte_pH(self) -> float:
        return self.anolyte_pH

    def read_anolyte_level(self) -> float:
        return self.anolyte_level_pct

    # ---- write methods ----
    def set_galvanostat_current(self, amps: float) -> None:
        self.galv_current = amps
        self.galvanostat_enabled = amps > 0.05

    def galvanostat_to_OCV(self) -> None:
        self.galv_current = 0.0
        self.galvanostat_enabled = False

    def set_co2_flow(self, ml_per_min: float) -> None:
        if self.co2_solenoid_open:
            self.co2_setpoint = ml_per_min

    def close_co2_solenoid(self) -> None:
        self.co2_solenoid_open = False
        self.co2_setpoint = 0.0

    def set_anolyte_pump(self, ml_per_min: float) -> None:
        self.anolyte_pump_setpoint = ml_per_min

    def set_heater_setpoint(self, channel: str, celsius: float) -> None:
        self.heater_setpoints[channel] = celsius

    def trigger_GC_injection(self) -> tuple[float, float, float]:
        """Estimate FE(CO), FE(H2), SPU from current sim state."""
        if not self.galvanostat_enabled:
            return (0.0, 0.0, 0.0)
        avg_block = sum(self.cell_blockage_frac) / NUM_CELLS
        # Initial FE(CO) ~92%, drops as blockage rises
        fe_co = max(20.0, 92.0 - 75.0 * avg_block) + random.uniform(-1, 1)
        fe_h2 = max(0.0, 100.0 - fe_co - 5.0)
        # SPU: at 350 ml/min/cell and 10 A stack:
        # CO2 stoich = 10A × 60s × 22400ml/mol / (2 × 96485 C/mol) = 69.7 ml/min
        # SPU = consumed/total * 100. Consumed = stoich × FE(CO)/100
        co2_stoich_total = TARGET_STACK_CURRENT * 60 * 22400 / (2 * FARADAY)
        co2_in_total = self.co2_setpoint
        spu = (co2_stoich_total * fe_co / 100.0) / max(1.0, co2_in_total) * 100
        return (fe_co, fe_h2, spu)

    def is_safe_to_run(self) -> bool:
        return not self.estop_pressed


# =============================================================================
# REAL HARDWARE — stub for NI DAQmx + Modbus integration
# =============================================================================

class RealHardware(HardwareInterface):
    """
    Stub. Fill in with NI-DAQmx (nidaqmx package), Modbus (pymodbus), and
    serial drivers for the actual instruments listed in the BOM.
    """
    def __init__(self, config_path: str):
        raise NotImplementedError(
            "RealHardware integration is a stub. Implement using nidaqmx "
            "(per-cell V via NI 9219, sensors via NI 9205, T via NI 9211), "
            "pymodbus for Bronkhorst MFC, and pyserial for galvanostat."
        )

    def read_cell_voltages(self): raise NotImplementedError
    def read_stack_current(self): raise NotImplementedError
    def read_per_cell_flows(self): raise NotImplementedError
    def read_pressure_CO2_inlet(self): raise NotImplementedError
    def read_temperatures(self): raise NotImplementedError
    def read_anolyte_pH(self): raise NotImplementedError
    def read_anolyte_level(self): raise NotImplementedError
    def set_galvanostat_current(self, amps): raise NotImplementedError
    def galvanostat_to_OCV(self): raise NotImplementedError
    def set_co2_flow(self, ml_per_min): raise NotImplementedError
    def close_co2_solenoid(self): raise NotImplementedError
    def set_anolyte_pump(self, ml_per_min): raise NotImplementedError
    def set_heater_setpoint(self, ch, c): raise NotImplementedError
    def trigger_GC_injection(self): raise NotImplementedError
    def is_safe_to_run(self): raise NotImplementedError


# =============================================================================
# DATA LOGGER
# =============================================================================

class DataLogger:
    def __init__(self, run_dir: Path):
        self.run_dir = run_dir
        self.run_dir.mkdir(parents=True, exist_ok=True)
        self.csv_path = run_dir / "samples.csv"
        self.events_path = run_dir / "events.log"
        self._csv_file = open(self.csv_path, "w", newline="")
        self._writer = csv.writer(self._csv_file)
        self._wrote_header = False

    def log_sample(self, s: Sample):
        if not self._wrote_header:
            header = ["t_iso", "t_seconds", "state",
                      "stack_V", "stack_I"] + \
                     [f"V_cell_{i+1}" for i in range(NUM_CELLS)] + \
                     [f"flow_cell_{i+1}" for i in range(NUM_CELLS)] + \
                     ["pressure_CO2_inlet_bar",
                      "T_endplate_neg", "T_endplate_pos",
                      "T_anolyte", "T_humidifier",
                      "anolyte_pH", "anolyte_level_pct",
                      "fe_co_pct", "fe_h2_pct", "spu_pct",
                      "alarm_state", "abort_flag"]
            self._writer.writerow(header)
            self._wrote_header = True
        row = [s.t_iso, f"{s.t_seconds:.2f}", s.state,
               f"{s.stack_V:.4f}", f"{s.stack_I:.4f}"] + \
              [f"{v:.4f}" for v in s.cell_V] + \
              [f"{f:.2f}" for f in s.flow_cell] + \
              [f"{s.pressure_CO2_inlet_bar:.4f}",
               f"{s.T_endplate_neg:.2f}", f"{s.T_endplate_pos:.2f}",
               f"{s.T_anolyte:.2f}", f"{s.T_humidifier:.2f}",
               f"{s.anolyte_pH:.3f}", f"{s.anolyte_level_pct:.1f}",
               "" if s.fe_co_pct is None else f"{s.fe_co_pct:.2f}",
               "" if s.fe_h2_pct is None else f"{s.fe_h2_pct:.2f}",
               "" if s.spu_pct is None else f"{s.spu_pct:.2f}",
               s.alarm_state, "1" if s.abort_flag else "0"]
        self._writer.writerow(row)
        self._csv_file.flush()

    def log_event(self, event: AlarmEvent):
        with open(self.events_path, "a") as f:
            f.write(f"{event.t_iso} [{event.severity}] {event.code}: "
                    f"{event.message}\n")

    def close(self):
        self._csv_file.close()


# =============================================================================
# ALARM MANAGER
# =============================================================================

class AlarmManager:
    """
    Evaluates each sample against alarm thresholds. Maintains a 1-h moving
    average of cell voltages for soft warnings.
    """
    def __init__(self):
        self.cell_V_history: list[list[float]] = [[] for _ in range(NUM_CELLS)]
        self.cell_V_initial: Optional[list[float]] = None
        self.pressure_initial: Optional[float] = None
        self.warn_count = 0
        self.abort_triggered = False
        self.abort_reason: Optional[str] = None

    def set_baselines(self, cell_V: list[float], pressure: float):
        """Call once after current is applied and steady-state reached."""
        self.cell_V_initial = list(cell_V)
        self.pressure_initial = pressure

    def evaluate(self, s: Sample) -> tuple[str, list[AlarmEvent]]:
        events: list[AlarmEvent] = []
        state = "OK"

        # Alarms only meaningful during galvanostatic operation
        if s.state != RunState.GALVANOSTATIC.value:
            return state, events

        # Update moving averages (last 3600 samples assuming 1 Hz)
        for i, v in enumerate(s.cell_V):
            self.cell_V_history[i].append(v)
            if len(self.cell_V_history[i]) > 3600:
                self.cell_V_history[i].pop(0)

        # Hard limits — abort
        for i, v in enumerate(s.cell_V):
            if v < V_CELL_ABS_MIN:
                events.append(self._abort(s, "V_CELL_LOW",
                    f"Cell {i+1} V = {v:.3f} below {V_CELL_ABS_MIN}"))
                state = "ABORT"
            elif v > V_CELL_ABS_MAX:
                events.append(self._abort(s, "V_CELL_HIGH",
                    f"Cell {i+1} V = {v:.3f} above {V_CELL_ABS_MAX}"))
                state = "ABORT"

        if s.stack_V > V_STACK_MAX:
            events.append(self._abort(s, "V_STACK_HIGH",
                f"Stack V = {s.stack_V:.2f} above {V_STACK_MAX}"))
            state = "ABORT"

        if self.cell_V_initial is not None:
            for i, (v, v0) in enumerate(zip(s.cell_V, self.cell_V_initial)):
                dev = abs(v - v0)
                if dev > V_CELL_DEVIATION_ABORT:
                    events.append(self._abort(s, "V_CELL_DEVIATION",
                        f"Cell {i+1} V = {v:.3f} deviates {dev:.3f} V from "
                        f"initial {v0:.3f}"))
                    state = "ABORT"

        if self.pressure_initial is not None:
            rise_frac = ((s.pressure_CO2_inlet_bar - self.pressure_initial)
                         / self.pressure_initial)
            if rise_frac > PRESSURE_RISE_ABORT_FRAC:
                events.append(self._abort(s, "PRESSURE_RISE",
                    f"CO2 inlet pressure rose {rise_frac*100:.1f}% (threshold "
                    f"{PRESSURE_RISE_ABORT_FRAC*100:.0f}%)"))
                state = "ABORT"
            elif rise_frac > PRESSURE_RISE_WARN_FRAC and state == "OK":
                events.append(self._warn(s, "PRESSURE_RISE_WARN",
                    f"CO2 inlet pressure rose {rise_frac*100:.1f}%"))
                state = "WARN"

        # Soft limits — warn
        if state == "OK":
            if s.anolyte_pH < PH_REFRESH_RECOMMEND:
                events.append(self._warn(s, "PH_LOW",
                    f"Anolyte pH = {s.anolyte_pH:.2f}, refresh recommended"))
                state = "WARN"

            for i, v in enumerate(s.cell_V):
                hist = self.cell_V_history[i]
                if len(hist) >= 60:
                    avg = sum(hist[-3600:]) / len(hist[-3600:])
                    if abs(v - avg) > V_CELL_DEVIATION_WARN:
                        events.append(self._warn(s, "V_CELL_DRIFT",
                            f"Cell {i+1} V = {v:.3f} drifts "
                            f"{abs(v-avg):.3f} from 1h avg {avg:.3f}"))
                        state = "WARN"

            if (s.fe_co_pct is not None
                    and s.fe_co_pct < FE_CO_TARGET_MIN
                    and s.state == RunState.GALVANOSTATIC.value):
                events.append(self._warn(s, "FE_CO_LOW",
                    f"FE(CO) = {s.fe_co_pct:.1f}% below "
                    f"target {FE_CO_TARGET_MIN}%"))
                state = "WARN"

        return state, events

    def _abort(self, s: Sample, code: str, msg: str) -> AlarmEvent:
        if not self.abort_triggered:
            self.abort_triggered = True
            self.abort_reason = msg
        return AlarmEvent(t_iso=s.t_iso, severity="ABORT", code=code,
                          message=msg, sample=s)

    def _warn(self, s: Sample, code: str, msg: str) -> AlarmEvent:
        self.warn_count += 1
        return AlarmEvent(t_iso=s.t_iso, severity="WARN", code=code,
                          message=msg, sample=s)


# =============================================================================
# ELECTROLYZER CONTROLLER (state machine)
# =============================================================================

class ElectrolyzerController:
    def __init__(self, hw: HardwareInterface, logger: DataLogger,
                 alarms: AlarmManager, time_scale: float = 1.0):
        self.hw = hw
        self.logger = logger
        self.alarms = alarms
        self.time_scale = time_scale
        self.state = RunState.IDLE
        self.t_start = time.monotonic()
        self.last_GC = -math.inf
        self.GC_interval = 3600.0  # 1 h of simulated time
        self._stop_requested = False

    def request_stop(self):
        self._stop_requested = True

    def run(self, duration_hours: float):
        try:
            self._heat_to_setpoint()
            self._purge_with_N2()
            self._co2_ramp()
            self._stabilize_OCV()
            self._galvanostatic_run(duration_hours)
        except KeyboardInterrupt:
            log.info("Operator interrupt")
        finally:
            self._shutdown()

    # ---- phases ----
    def _heat_to_setpoint(self):
        self._set_state(RunState.HEATING)
        log.info("Starting heat-up to %.0f °C (≤60 min real time)",
                 TARGET_TEMPERATURE)
        self.hw.set_heater_setpoint("anolyte", TARGET_TEMPERATURE)
        self.hw.set_heater_setpoint("humidifier", TARGET_TEMPERATURE)
        self.hw.set_heater_setpoint("endplate", TARGET_TEMPERATURE)
        self.hw.set_anolyte_pump(TARGET_ANOLYTE_FLOW_TOTAL)
        # Wait until all temperatures within ±2 °C
        while not self._stop_requested:
            T = self.hw.read_temperatures()
            self._sample_and_log(fe_co=None)
            if all(abs(T[k] - TARGET_TEMPERATURE) < 2.0
                   for k in ("anolyte", "humidifier", "endplate_neg")):
                log.info("Thermal equilibrium reached")
                return
            self._tick()

    def _purge_with_N2(self):
        # In simulated mode, we just set CO2 flow to 0 and wait
        self._set_state(RunState.PURGING)
        log.info("N2 purge (5 min sim time)")
        self.hw.set_co2_flow(0.0)
        end = self._sim_now() + 300
        while self._sim_now() < end and not self._stop_requested:
            self._sample_and_log(fe_co=None)
            self._tick()

    def _co2_ramp(self):
        self._set_state(RunState.CO2_RAMP)
        log.info("Ramping CO2 to %.0f ml/min over 5 min", TARGET_TOTAL_CO2_FLOW)
        end = self._sim_now() + 300
        while self._sim_now() < end and not self._stop_requested:
            elapsed = self._sim_now() - (end - 300)
            self.hw.set_co2_flow(TARGET_TOTAL_CO2_FLOW * elapsed / 300.0)
            self._sample_and_log(fe_co=None)
            self._tick()
        self.hw.set_co2_flow(TARGET_TOTAL_CO2_FLOW)

    def _stabilize_OCV(self):
        self._set_state(RunState.OCV)
        log.info("OCV stabilization (10 min sim time)")
        end = self._sim_now() + 600
        while self._sim_now() < end and not self._stop_requested:
            self._sample_and_log(fe_co=None)
            self._tick()
        # Note: baselines for V_cell deviation are captured AFTER current is
        # applied and the stack reaches steady-state — not at OCV (where V≈0).
        # Pressure baseline is captured here at OCV under full CO2 flow.
        pressure = self.hw.read_pressure_CO2_inlet()
        self.alarms.pressure_initial = pressure
        log.info("Pressure baseline: %.3f bar (V_cell baseline pending)",
                 pressure)

    def _galvanostatic_run(self, duration_hours: float):
        self._set_state(RunState.GALVANOSTATIC)
        log.info("Applying %.1f A for up to %.1f h",
                 TARGET_STACK_CURRENT, duration_hours)
        self.hw.set_galvanostat_current(TARGET_STACK_CURRENT)
        # Wait 5 min sim time for steady-state, then snapshot V baseline
        steady_state_end = self._sim_now() + 300
        while self._sim_now() < steady_state_end and not self._stop_requested:
            self._sample_and_log(fe_co=None)
            self._tick()
        cell_V = self.hw.read_cell_voltages()
        self.alarms.cell_V_initial = list(cell_V)
        log.info("V_cell baseline locked: %s",
                 [f"{v:.3f}" for v in cell_V])
        end = self._sim_now() + duration_hours * 3600.0

        while self._sim_now() < end and not self._stop_requested:
            # Periodic GC injection
            fe_co = fe_h2 = spu = None
            if self._sim_now() - self.last_GC >= self.GC_interval:
                fe_co, fe_h2, spu = self.hw.trigger_GC_injection()
                self.last_GC = self._sim_now()
                log.info("GC: FE(CO)=%.1f%%, FE(H2)=%.1f%%, SPU=%.1f%%",
                         fe_co, fe_h2, spu)

            sample = self._sample_and_log(fe_co=fe_co, fe_h2=fe_h2, spu=spu)
            if self.alarms.abort_triggered:
                log.error("ABORT triggered: %s", self.alarms.abort_reason)
                self._set_state(RunState.ABORTED)
                return
            self._tick()

        log.info("Galvanostatic phase complete")

    def _shutdown(self):
        if self.state != RunState.ABORTED:
            self._set_state(RunState.SHUTDOWN)
        log.info("Shutdown sequence")
        self.hw.galvanostat_to_OCV()
        # Brief OCV under CO2 then close
        time.sleep(0.5 / max(self.time_scale, 1))
        self.hw.close_co2_solenoid()
        self.hw.set_heater_setpoint("anolyte", 25.0)
        self.hw.set_heater_setpoint("humidifier", 25.0)
        self.hw.set_heater_setpoint("endplate", 25.0)
        self.hw.set_anolyte_pump(0.0)
        self._sample_and_log(fe_co=None)
        self.logger.close()
        log.info("Run complete. Data: %s", self.logger.run_dir)

    # ---- helpers ----
    def _set_state(self, st: RunState):
        log.info("State: %s → %s", self.state.value, st.value)
        self.state = st

    def _sim_now(self) -> float:
        return (time.monotonic() - self.t_start) * self.time_scale

    def _tick(self):
        # Sleep ~1 s of simulated time, scaled to real time
        time.sleep(max(0.001, 1.0 / self.time_scale))

    def _sample_and_log(self, fe_co=None, fe_h2=None, spu=None) -> Sample:
        cell_V = self.hw.read_cell_voltages()
        T = self.hw.read_temperatures()
        s = Sample(
            t_iso=dt.datetime.now().isoformat(timespec="seconds"),
            t_seconds=self._sim_now(),
            state=self.state.value,
            stack_V=sum(cell_V),
            stack_I=self.hw.read_stack_current(),
            cell_V=cell_V,
            flow_cell=self.hw.read_per_cell_flows(),
            pressure_CO2_inlet_bar=self.hw.read_pressure_CO2_inlet(),
            T_endplate_neg=T["endplate_neg"],
            T_endplate_pos=T["endplate_pos"],
            T_anolyte=T["anolyte"],
            T_humidifier=T["humidifier"],
            anolyte_pH=self.hw.read_anolyte_pH(),
            anolyte_level_pct=self.hw.read_anolyte_level(),
            fe_co_pct=fe_co, fe_h2_pct=fe_h2, spu_pct=spu,
        )
        alarm_state, events = self.alarms.evaluate(s)
        s.alarm_state = alarm_state
        s.abort_flag = self.alarms.abort_triggered
        self.logger.log_sample(s)
        for e in events:
            self.logger.log_event(e)
            log.warning("[%s] %s — %s", e.severity, e.code, e.message)
        return s


# =============================================================================
# MAIN
# =============================================================================

log = logging.getLogger("electrolyzer")


def main():
    p = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--simulate", action="store_true",
                   help="Run with built-in simulated hardware")
    g.add_argument("--hardware", action="store_true",
                   help="Run with real hardware (stub — implement first)")

    p.add_argument("--duration", type=float, default=24.0,
                   help="Galvanostatic run duration in (simulated) hours")
    p.add_argument("--time-scale", type=float, default=600.0,
                   help="Sim seconds per real second (default 600 = 10 min/s)")
    p.add_argument("--config", type=str, default=None,
                   help="Hardware config YAML (only with --hardware)")
    p.add_argument("--fault", type=str, default=None,
                   choices=[None, "cell3_fail_at_5h"],
                   help="Inject a simulated fault scenario")
    p.add_argument("--run-dir", type=str, default=None,
                   help="Output directory (default: ./runs/<timestamp>)")
    p.add_argument("--quiet", action="store_true")

    args = p.parse_args()

    logging.basicConfig(
        level=logging.WARNING if args.quiet else logging.INFO,
        format="%(asctime)s %(levelname)-7s %(message)s",
        datefmt="%H:%M:%S")

    run_dir = Path(args.run_dir or
                   f"runs/{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}")

    if args.simulate:
        hw = SimulatedHardware(time_scale=args.time_scale,
                               fault_scenario=args.fault)
    else:
        hw = RealHardware(args.config)

    logger = DataLogger(run_dir)
    alarms = AlarmManager()
    ctrl = ElectrolyzerController(hw, logger, alarms,
                                   time_scale=args.time_scale)

    # Graceful Ctrl+C
    signal.signal(signal.SIGINT, lambda *_: ctrl.request_stop())

    log.info("Starting run — output: %s", run_dir)
    log.info("Mode: %s, time-scale: %.0fx, duration: %.1f h sim",
             "SIMULATE" if args.simulate else "HARDWARE",
             args.time_scale, args.duration)

    ctrl.run(args.duration)

    if alarms.abort_triggered:
        log.error("RUN ABORTED — %s", alarms.abort_reason)
        sys.exit(2)
    else:
        log.info("RUN COMPLETED — %d warnings", alarms.warn_count)
        sys.exit(0)


if __name__ == "__main__":
    main()
