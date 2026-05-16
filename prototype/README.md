# 500 cm² Stacked CO2RR-to-CO Electrolyzer — Prototype Build Package

This directory contains everything needed to build, commission, and operate a
5-cell × 100 cm² stacked AEM-MEA electrolyzer for CO2 reduction to CO.

## Contents

| File | Purpose |
|---|---|
| `prototype_build_spec.md` | Master engineering specification: BOM, P&ID, assembly, plumbing, electrical, thermal, DAQ |
| `electrolyzer_control.py` | Runnable Python control software with simulation mode |
| `commissioning_sop.md` | Step-by-step commissioning checklist |
| `operating_sop.md` | Standard operating procedure (cold start → shutdown) |
| `requirements.txt` | Python dependencies for control software |

## Quick start

1. Read `prototype_build_spec.md` end-to-end. Confirm BOM is procurable.
2. Install Python deps: `pip install -r requirements.txt`
3. Run the controller in simulation mode (no hardware needed):
   `python electrolyzer_control.py --simulate --duration 24`
4. Verify alarm logic and data logging by triggering simulated faults.
5. Replace `SimulatedHardware` with `RealHardware` when instruments arrive.
6. Follow `commissioning_sop.md` before first electrochemical run.

## Operating target (Run #1)

- 5 × 100 cm² cells, electrical series, parallel gas/liquid feed
- Single-serpentine cathode flow-field
- 100 mA/cm² (10 A stack current)
- 3.5 ml/min/cm² CO2 = 1.75 L/min total stack flow
- 0.5 M CH3COOH humidifier @ 50 °C
- 50 L of 0.1 M KHCO3 anolyte, 500 ml/min recirculation
- Stack and anolyte at 50 °C
- Goal: ≥ 24 h with FE(CO) ≥ 80%, SPU 10–20%

Project lineage: scale-up from validated 5 cm² (350 h baseline) and
single-cell 100 cm² (55 h with single-serpentine) results.
