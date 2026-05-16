# Master Build Specification — 500 cm² Stacked CO2RR Electrolyzer

**Configuration**: 5 × 100 cm² AEM-MEA cells in electrical series, parallel gas/liquid feed
**Target**: ≥ 24 h continuous operation, FE(CO) ≥ 80%, SPU 10–20% per cell
**Lineage**: 5 cm² baseline (350 h validated) → 100 cm² (55 h with salt diagnosis) → 500 cm² stack

---

## 1. System Architecture (P&ID)

```
                                                                      ┌─────────────┐
                              CO2 SUPPLY                              │   GC-TCD    │
                              (>99.99%)                               │   (online)  │
                                  │                                   └──────▲──────┘
                                  ▼                                          │
                        ┌──────────────────┐                                 │
                        │  MFC #1          │  0–5000 ml/min                  │
                        │  (Bronkhorst)    │                                 │
                        └────────┬─────────┘                                 │
                                 ▼                                           │
                        ┌──────────────────┐                                 │
                        │  ACID HUMIDIFIER │  0.5 M CH3COOH @ 50°C            │
                        │  (PTFE bubbler)  │  Heated bath                    │
                        └────────┬─────────┘                                 │
                                 ▼ heated line @ 50°C                        │
                        ┌──────────────────┐                                 │
                        │ Z-TYPE GAS       │                                 │
                        │ MANIFOLD         │                                 │
                        └─┬──┬──┬──┬──┬───┘                                  │
       ┌──────────────────┼──┼──┼──┼──┼──────────────────┐                   │
       │   FM₁  FM₂  FM₃  FM₄  FM₅      (per-cell flow meters)               │
       │    ▼    ▼    ▼    ▼    ▼                                            │
       │ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐                                  │
       │ │CELL│ │CELL│ │CELL│ │CELL│ │CELL│  5-cell electrical-series stack  │
       │ │ 1  │═│ 2  │═│ 3  │═│ 4  │═│ 5  │  Each: 100 cm² active area       │
       │ │    │ │    │ │    │ │    │ │    │  Single-serpentine cathode FF    │
       │ └─┬──┘ └─┬──┘ └─┬──┘ └─┬──┘ └─┬──┘  Parallel anode FF                │
       │   ▼      ▼      ▼      ▼      ▼      All @ 50°C                     │
       │   └──────┴──────┼──────┴──────┘                                      │
       │             ┌───▼─────────┐                                          │
       │             │ Outlet hdr  │──────► H2O knockout ──► GC ──────────────┘
       │             │ (gas)       │
       │             └─────────────┘
       │
       │ Anolyte loop (parallel feed):
       │   50 L of 0.1 M KHCO3 @ 50°C
       │           │
       │           ▼
       │   ┌──────────────┐
       │   │ Pump (mag-   │  500 ml/min
       │   │ drive, 1L/min│
       │   │ rated)       │
       │   └──────┬───────┘
       │          ▼
       │   ┌──────────────┐
       │   │ Z-MANIFOLD   │
       │   └─┬──┬──┬──┬──┬─┘
       │     ▼  ▼  ▼  ▼  ▼   100 ml/min/cell (rotameter on each)
       │    [anodes of cells 1–5]
       │     │  │  │  │  │
       │     ▼  ▼  ▼  ▼  ▼
       │   ┌──────────────┐
       │   │ Return hdr   │
       │   └──────┬───────┘
       │          ▼
       │   ┌──────────────┐
       │   │ Reservoir    │  pH probe, T-couple, level
       │   │ 60 L PP/HDPE │  Heater (immersion or jacket)
       │   │ + heater     │
       │   └──────────────┘
       │
       └── Galvanostat (BioLogic VMP-300 or equivalent, 50A capability)
           ─ Stack +/− leads to end plates
           ─ Per-cell V taps to isolated DAQ (NI 9219 ×2)
```

---

## 2. Bill of Materials

### 2.1 Cell hardware (×5, identical)

| Item | Spec | Qty | Vendor (suggested) |
|---|---|---|---|
| Cathode flow plate | Graphite, single-serpentine, 100 cm² active area, 1×1 mm channel, 0.5 mm rib | 5 | In-house machining or Fuel Cell Technologies |
| Anode flow plate | Ti or graphite, parallel channels, 100 cm² | 5 | Same |
| Bipolar plate (BPP) | Graphite, double-sided (cathode-FF/anode-FF) for cells 2–4 | 4 | Same — these double as cathode-of-cell-N + anode-of-cell-N+1 |
| End plate (negative) | Stainless 316 or Al 6061, ≥30 mm thick, 200×200 mm | 1 | In-house |
| End plate (positive) | Same | 1 | In-house |
| Cathode GDE | AgNPs, >100 nm, 0.4–0.5 mg/cm² loading on Sigracet 39BB | 5 | In-house deposition |
| AEM | Sustanion X37-50, cut to fit | 5 | Dioxide Materials |
| Anode | IrO2 on Ti-Pt mesh, same as 100 cm² baseline | 5 | In-house |
| Gasket (cathode) | PTFE, 250 μm, laser-cut | 5 | In-house |
| Gasket (anode) | FKM/Viton, 250 μm | 5 | In-house |
| Tie-rods | M6 stainless 316, 250 mm long | 8 | McMaster |
| Belleville washers | DIN 6796 for M6 | 16 | McMaster |
| Insulating sleeves | PEEK or PTFE around tie-rods (electrical isolation from BPPs) | 8 | McMaster |
| Tap-point screws | M3 brass, threaded into BPP/end-plate edges | 6 | McMaster |

### 2.2 Gas system

| Item | Spec | Qty | Vendor |
|---|---|---|---|
| CO2 supply | Research grade, ≥99.99% | 1 cyl | Airgas / local |
| CO2 regulator | Two-stage, 0–5 bar outlet | 1 | Airgas |
| MFC (CO2) | 0–5000 ml/min, ±0.5% FS, EtherCAT/Modbus | 1 | Bronkhorst EL-FLOW Prestige |
| Acid humidifier vessel | PTFE bubbler, 250 ml fill, with PTFE frit | 1 | In-house or BOLA |
| Heated water bath | Programmable, 25–80°C, 5L | 1 | Julabo CORIO CD |
| Heated CO2 transfer line | PFA, 6 mm OD, heat-traced to 50°C | 2 m | Swagelok |
| Z-type gas manifold | 316 SS, 10 mm ID trunk, 4 mm ID branches, equal length | 1 set | In-house |
| Per-cell gas flow meter | Thermal mass flow sensor, 0–1000 ml/min, 4–20 mA out | 5 | Sensirion SFM3300 or similar |
| Pressure transducer (CO2 inlet) | 0–3 bar gauge, 4–20 mA, chemical compatible | 1 | Omega PX309 |
| Outlet water knockout | PTFE, 100 ml, with drain | 1 | In-house |
| GC sample line | Heated PFA, 6 mm OD | 1 m | Swagelok |
| GC | TCD + FID, online, automated injection | 1 | SRI 8610C or Agilent 990 micro-GC |

### 2.3 Liquid system

| Item | Spec | Qty | Vendor |
|---|---|---|---|
| Anolyte reservoir | 60 L PP/HDPE tank with lid, drain | 1 | Nalgene |
| Reservoir heater | 1 kW immersion heater, PTFE-coated, with PID | 1 | Julabo immersion or PolyScience |
| Recirculation pump | Magnetic-drive centrifugal, 1 L/min rated, PP/PVDF wetted, chemical-resistant | 1 | March Pump 0150 |
| Z-type liquid manifold | PVDF or PP, 10 mm ID trunk, 4 mm ID branches | 1 set | In-house |
| Per-cell liquid rotameter | 0–200 ml/min, glass + PTFE | 5 | King Instruments |
| Tubing | PFA, 6 mm OD throughout liquid loop | 20 m | Swagelok |
| pH probe | Lab-grade with temperature compensation, BNC out | 1 | Mettler InLab Expert |
| pH transmitter | 4–20 mA out from BNC | 1 | Mettler M300 |
| Level switch | Float switch, low-level alarm on reservoir | 1 | Madison M5000 |
| Anolyte refresh valve | Manual ball valve, drain to neutralization tank | 1 | Hayward |

### 2.4 Electrical and DAQ

| Item | Spec | Qty | Vendor |
|---|---|---|---|
| Galvanostat | ≥50 A, ≥30 V, 4-quadrant, computer-controlled | 1 | BioLogic VMP-300 with 50A booster, or Gamry Reference 30k |
| Bus bars | Cu, 25×6 mm, tinned | 2 | McMaster |
| Stack-current shunt | 50 A / 50 mV, ±0.5% | 1 | Murata |
| DAQ chassis | 4-slot USB cDAQ | 1 | NI cDAQ-9174 |
| Per-cell V module | 4-channel, ±60 V differential, 250 V isolation, 24-bit | 2 | NI 9219 |
| Analog input module | 8-channel, ±10 V, for 4–20 mA loops (with 250 Ω resistors) | 1 | NI 9205 |
| Thermocouple module | 4-channel TC, K-type | 1 | NI 9211 |
| Digital output module | 4-ch relay, for galvanostat enable + valve interlocks | 1 | NI 9472 |
| K-type thermocouples | 1 m, fiberglass insulated | 6 | Omega |
| Emergency stop | Mushroom-head, latching, NC | 1 | Schneider XB7 |
| Solid-state relay | For CO2 valve cutoff on E-stop | 1 | Crydom |
| CO2 shutoff valve | Solenoid, normally closed, fail-safe | 1 | ASCO |
| Industrial PC or workstation | Win/Linux, USB, network | 1 | Any |

### 2.5 Safety and infrastructure

| Item | Spec | Qty | Notes |
|---|---|---|---|
| H2 gas detector | 0–4% in air, audible + relay | 1 | Mounted near outlet |
| CO gas detector | 0–500 ppm, audible + relay | 1 | Mounted near outlet |
| Fume hood or vented enclosure | Sized for stack + reservoir | 1 | Required for CO handling |
| Pressure relief valve | Set @ 2.0 bar gauge, on CO2 inlet line | 1 | Swagelok |
| First-aid + acid spill kit | For CH3COOH and KHCO3 | 1 | Lab supply |

---

## 3. Mechanical Assembly Procedure

### 3.1 Stack-up order (bottom to top, viewed from end-plate)

```
[End plate negative]
  PEEK insulator gasket
[Cathode flow plate of cell 1]              ← Tap point T₀
  Cathode gasket (PTFE)
  Cathode GDE (AgNPs side facing AEM)
  AEM (Sustanion)
  Anode gasket (FKM)
  Anode (IrO2-TiPt mesh)
[BPP 1: anode-side-of-cell-1 + cathode-side-of-cell-2]   ← Tap point T₁
  Cathode gasket / GDE / AEM / Anode-gasket / Anode (cell 2)
[BPP 2]                                      ← Tap point T₂
  ... cell 3 ...
[BPP 3]                                      ← Tap point T₃
  ... cell 4 ...
[BPP 4]                                      ← Tap point T₄
  ... cell 5 ...
[End plate positive]                         ← Tap point T₅
```

### 3.2 Pre-assembly checks

1. Confirm all 5 GDE samples have matching loading (0.4–0.5 mg/cm² Ag NPs).
2. Hydrate AEMs in 1 M KOH for ≥ 24 h, then rinse and store in 0.1 M KHCO3.
3. Inspect every gasket for cuts, debris, or compression set. Reject any.
4. Verify BPP edges have tap-point holes drilled and tapped (M3 ×4 mm depth).
5. Insulate tie-rods with PEEK/PTFE sleeves; verify no tie-rod can touch any BPP.

### 3.3 Compression sequence

1. Stack components in order on bottom end plate, alignment-pinned.
2. Place top end plate.
3. Insert all 8 tie-rods with PEEK sleeves.
4. Add Belleville washers under each nut (2 stacked, opposing for spring action).
5. Hand-tighten all nuts evenly.
6. **Star-pattern torque sequence**, 4 passes:
   - Pass 1: 25% torque = 2 ft·lbs (~2.7 N·m) per bolt
   - Pass 2: 50% torque = 4 ft·lbs (~5.4 N·m) per bolt
   - Pass 3: 75% torque = 6 ft·lbs (~8.1 N·m) per bolt
   - Pass 4: 100% torque = 8 ft·lbs (~11 N·m) per bolt
7. Wait 30 minutes for gasket relaxation; re-torque pass 4.
8. **Verify uniform compression** with Fuji Prescale film between cell 1 and cell 5 GDEs on first build. Imprint must be uniform color across the full active area.

### 3.4 Verify electrical isolation

Before plumbing:
- Multimeter resistance check: each tie-rod to each BPP must read > 10 MΩ.
- End plate to end plate (through stack): expect ~kΩ from MEA wet-out (depends on humidity).
- No tap point should short to another except through MEA stack-up.

---

## 4. Plumbing

### 4.1 Gas (CO2 path)

1. Wrap heat-trace cable around CO2 line from humidifier outlet to manifold.
2. Insulate with foam sleeve. Set heat-trace controller to 50 °C.
3. Connect manifold branches (4 mm ID PFA) to each cell cathode inlet — equal lengths within ±5 cm.
4. Outlet header collects gas from all 5 cells, passes through water knockout, then to GC sample line and vent.
5. Pressure relief valve: tee'd onto CO2 line between MFC and humidifier, set to 2.0 bar gauge.
6. Solenoid shutoff valve: between CO2 cylinder regulator and MFC, normally closed, opens on system enable.

### 4.2 Liquid (anolyte path)

1. Reservoir at lowest point, pump suction from bottom drain (with screen).
2. Pump discharge → manifold trunk → 5 branches → cell anode inlets.
3. Cell anode outlets → return header → back to reservoir top (with splash guard).
4. Each branch line has a rotameter and a needle valve for individual flow trim.
5. pH probe, thermocouple, and level switch in reservoir.

### 4.3 Pressure balance (critical)

- Cathode and anode outlet headers must be at matched static pressure (within ±50 mbar) to prevent AEM rupture.
- Solution: both outlet headers vent to common atmosphere through equal-impedance vents.
- Verify with differential pressure gauge before electrochemical run.

---

## 5. Electrical Wiring

### 5.1 Power circuit (high-current)

- Galvanostat (+) → bus bar → end plate positive
- End plate negative → bus bar → galvanostat (−)
- Stack-current shunt in series on negative leg
- All connections crimped, torqued, and inspected.

### 5.2 Per-cell voltage sense (low-current, isolated)

Six tap points (T₀ at end plate negative, T₁–T₄ at BPPs, T₅ at end plate positive):

- 22 AWG stranded PTFE wire, shielded twisted pairs at DAQ end ONLY
- Each wire from M3 brass tap-point screw to terminal block, then to NI 9219 channel
- Cell N voltage = differential measurement on NI 9219 channel N: V(T_N) − V(T_{N-1})
- Channel-to-channel isolation: 250 V (built into NI 9219)
- Wire bundle routed ≥ 15 cm away from bus bars to avoid inductive pickup
- Shield drained at DAQ chassis ground only

### 5.3 Sensor wiring

| Sensor | Cable | Module |
|---|---|---|
| 5× per-cell flow meters (4–20 mA) | Twisted pair, shielded | NI 9205 with 250 Ω resistors |
| CO2 inlet pressure (4–20 mA) | Same | NI 9205 |
| pH transmitter (4–20 mA) | Same | NI 9205 |
| 6× thermocouples (K-type) | TC-grade extension | NI 9211 |
| Stack-current shunt (50 mV) | Twisted pair, shielded | NI 9219 (one channel) |
| E-stop, level switch | Discrete | DAQ digital input |

### 5.4 Interlock circuit (hardwired, independent of software)

```
E-STOP button (NC) ──┬── Solid-state relay control input
                     │
Level switch (NC) ───┤
                     │
H2 detector (NO,    ─┤   Any one open → relay opens →
 trips on alarm)     │   CO2 solenoid closes, galvanostat enable disabled
                     │
CO detector (NO,    ─┤
 trips on alarm)     │
```

This loop must close before the galvanostat can be enabled. Any one open = abort.

---

## 6. Thermal Management

- Anolyte reservoir: 1 kW immersion heater with PID, target 50 °C ± 1.
- Stack body: silicone-rubber heating pads on outer end plates (×2, 200×200 mm, 200 W each), temperature controlled by thermocouple mounted on end plate, target 50 °C.
- CO2 humidifier bath: Julabo circulator, 50 °C ± 0.5.
- CO2 transfer line: heat-trace cable, controller, target 50 °C ± 2.
- Heat-up time: 60 minutes from cold start to thermal equilibrium.
- Anolyte recirculation while heating to homogenize temperature.

---

## 7. Commissioning Procedure

See `commissioning_sop.md` for the complete checklist. Summary:

1. **Mechanical**: stack-up, torque, compression verification with Fuji Prescale.
2. **Electrical isolation**: tie-rods, tap points, no shorts.
3. **Pressure test (gas)**: pressurize cathode side to 0.5 bar with N2; bubble test all joints. Hold 15 min, max 5% pressure drop.
4. **Leak test (liquid)**: fill anolyte loop, run pump at 500 ml/min, check for drips at all fittings and cell gaskets.
5. **Cold gas flow uniformity**: 1.75 L/min CO2 through stack at room temperature, verify each cell sees 350 ± 35 ml/min on its flow meter. If not, redesign manifold.
6. **DAQ verification**: simulate 1.000 V on each tap-point pair; confirm correct cell V reads on each NI 9219 channel; confirm no crosstalk.
7. **Alarm test**: trigger each alarm (over-V, under-V, ΔV, pressure rise, pH drop, E-stop, H2 detector). Confirm each trips abort and logs the event.
8. **Thermal equilibration**: heat to 50 °C with N2 flow; monitor temperature uniformity across end plates and per-cell positions.
9. **Polarization curve**: 25 → 100 mA/cm² in steps under N2, then under CO2. Confirm V-I behavior matches expectation. FE(CO) ≥ 90% at 100 mA/cm² before durability run.

---

## 8. Standard Operating Procedure

See `operating_sop.md` for the full procedure. Summary:

1. **Cold start**: pre-flow check, anolyte fill, heat-up to 50 °C (60 min).
2. **N2 purge**: 5 min at 500 ml/min.
3. **CO2 ramp**: switch from N2 to CO2, ramp to 1.75 L/min over 5 min.
4. **OCV stabilization**: hold 10 min, log baseline cell voltages.
5. **Apply current**: galvanostatic 100 mA/cm² (10 A), record initial stack and per-cell V.
6. **Steady-state monitoring**: GC every 1 h, V continuous, alarms armed.
7. **Anolyte refresh**: every 24 h, full 50 L swap.
8. **Shutdown**: stop current, hold OCV under CO2 for 5 min, switch to N2, cool to room T, drain.

---

## 9. Alarm and Interlock Logic (Software)

Implemented in `electrolyzer_control.py`. Summary:

| Condition | Action | Threshold |
|---|---|---|
| Any V_cell deviates >0.30 V from initial | Abort | Hard limit |
| Any V_cell <2.5 V or >4.5 V | Abort | Hard limit |
| Stack V >22 V | Abort | Hard limit |
| CO2 inlet pressure >+30% from initial | Abort | Hard limit |
| Anolyte pH <7.0 | Warn (refresh recommended) | Soft limit |
| Any V_cell deviates >0.15 V from 1h moving avg | Warn | Soft limit |
| H2 detector trip | Abort + close CO2 valve (hardwired) | — |
| CO detector trip | Abort + close CO2 valve (hardwired) | — |
| E-stop pressed | Abort + close CO2 valve (hardwired) | — |

Abort sequence:
1. Galvanostat → OCV
2. CO2 solenoid → close
3. Anolyte pump → off (after 30 s drain time)
4. Heaters → off
5. Log final state, notify operator (email/SMS)

---

## 10. Data Logging

All data written to a single CSV per run, timestamped at 1 Hz:

```
timestamp_iso, run_id, stack_V, stack_I,
V_cell_1, V_cell_2, V_cell_3, V_cell_4, V_cell_5,
T_endplate_neg, T_endplate_pos, T_anolyte, T_humidifier,
flow_cell_1, flow_cell_2, flow_cell_3, flow_cell_4, flow_cell_5,
pressure_CO2_inlet, anolyte_pH, anolyte_level,
GC_FE_CO, GC_FE_H2, GC_SPU,
alarm_state, abort_flag
```

Plus a separate event log for state changes, GC injections, refreshes, and alarms.

---

## 11. Maintenance

| Task | Frequency |
|---|---|
| Anolyte refresh | Every 24 h during operation |
| Acid humidifier refill | Every 72 h or when level <50% |
| Visual inspection (leaks, salt) | Daily |
| Per-cell flow meter calibration | Monthly |
| pH probe calibration | Weekly |
| MFC zero/span | Quarterly |
| Galvanostat current calibration | Quarterly |
| Full system disassembly + GDE inspection | After each long-duration run |
| AEM replacement | Every ~500 h or at sign of degradation |

---

## 12. References

- Hao et al., *Nat. Energy* 2025 — salt mechanism, K⁺ crossover
- Hao et al., *Science* 2025 + SM — acid humidification, multi-serpentine
- Biemolt et al., *ACS Energy Lett.* 2025 — cation accumulation, T effects
- Li et al., *EES Catalysis* 2025 — SPCE, elevated T/P
- Internal documents: `500cm2_stack_operating_conditions.txt`, `derisking_and_voltage_tap_spec.txt`, `voltage_fingerprint_analysis.txt`
