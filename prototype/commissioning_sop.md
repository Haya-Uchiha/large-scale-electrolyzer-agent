# Commissioning SOP — 500 cm² Stacked CO2RR Electrolyzer

Complete this checklist in order before any electrochemical run. Each item must
be initialed and dated by the operator. Do not skip items.

---

## Stage 1 — Mechanical (BEFORE any plumbing or electrical)

- [ ] All 5 GDEs verified at 0.4–0.5 mg/cm² Ag NP loading
- [ ] All 5 AEMs hydrated in 1 M KOH ≥ 24 h, then in 0.1 M KHCO3
- [ ] Gaskets inspected (no cuts, debris, compression set)
- [ ] BPP edge tap-points drilled, tapped (M3), tap-screws inserted
- [ ] Tie-rods sleeved with PEEK/PTFE insulators
- [ ] Stack assembled in correct order (cathode FF → GDE → AEM → anode → BPP → repeat)
- [ ] Star-pattern torque sequence completed (4 passes: 25 / 50 / 75 / 100 %)
- [ ] 30 min relaxation wait, then re-torque pass at 100 %
- [ ] Fuji Prescale film verifies uniform compression on cell 1 and cell 5
- [ ] Tie-rod-to-BPP resistance > 10 MΩ at every junction (no shorts)

---

## Stage 2 — Plumbing

### Gas
- [ ] CO2 cylinder regulator set to 1.5 bar outlet, leak-checked with snoop
- [ ] MFC installed, calibration certificate on file
- [ ] Acid humidifier vessel filled with 200 ml of 0.5 M CH3COOH, frit submerged
- [ ] Heated transfer line connected, heat-trace controller set to 50 °C
- [ ] Z-type gas manifold installed, branch lengths verified equal (±5 cm)
- [ ] All 5 per-cell flow meters wired and checked
- [ ] Pressure transducer installed at stack inlet, zeroed at atmospheric
- [ ] Outlet header → water knockout → GC sample line → vent
- [ ] Pressure relief valve set to 2.0 bar gauge (verified with calibrated gauge)

### Liquid
- [ ] Reservoir filled with 50 L of 0.1 M KHCO3
- [ ] Immersion heater installed, PID tuned, 50 °C setpoint armed
- [ ] Recirculation pump primed, flow direction verified
- [ ] Z-type liquid manifold connected
- [ ] All 5 cell-anode rotameters trim-valved to read 100 ml/min ±10
- [ ] pH probe calibrated (4.01, 7.00, 10.01 buffers) within last 7 days
- [ ] Level switch installed, low-level alarm verified (manually trip)

### Pressure balance
- [ ] Differential pressure gauge between cathode and anode outlets reads
      < ±50 mbar at full flow

---

## Stage 3 — Electrical

### Power
- [ ] Galvanostat positive lead bolted to end-plate-positive bus bar (torqued)
- [ ] Galvanostat negative lead bolted to end-plate-negative bus bar (torqued)
- [ ] 50 A shunt installed in negative leg
- [ ] Continuity verified end-plate-to-end-plate (open circuit when stack dry,
      ~ kΩ when wet)

### Per-cell V taps
- [ ] M3 brass screws torqued into all 6 tap points (T₀ through T₅)
- [ ] 22 AWG PTFE wire from each tap to terminal block (≤ 3 m)
- [ ] Wire bundle routed ≥ 15 cm from any current-carrying bus bar
- [ ] Shield drained at DAQ chassis ONLY (verify with multimeter)
- [ ] NI 9219 modules installed in cDAQ chassis, USB connected
- [ ] DAQmx test panel reads 0.000 ± 0.001 V on each channel (open circuit)
- [ ] Inject 1.000 V (calibration source) at one tap pair → reads 1.000 ± 0.005 V
      on that channel, 0.000 V on all others (no crosstalk)

### Sensor wiring
- [ ] All 5 flow meter 4–20 mA loops at NI 9205, scaled correctly
- [ ] CO2 inlet pressure transducer at NI 9205, scaled
- [ ] pH transmitter at NI 9205, scaled (4 mA = pH 0, 20 mA = pH 14)
- [ ] All 6 thermocouples at NI 9211, type K selected
- [ ] Stack-current shunt (50 mV / 50 A) at NI 9219 channel, scaled

### Interlocks
- [ ] E-stop wired into hardwired NC loop, tested (button → relay opens)
- [ ] Level switch wired into same loop, tested
- [ ] H2 detector relay (NO, trips on alarm) wired in, tested with calibration gas
- [ ] CO detector relay wired in, tested
- [ ] CO2 solenoid valve closes on any interlock open (verify with N2)
- [ ] Galvanostat enable signal disabled when any interlock open

---

## Stage 4 — Pressure and leak tests (no current applied)

### Gas pressure test
- [ ] Pressurize cathode side to 0.5 bar with N2 (NOT CO2 — non-flammable)
- [ ] Bubble-test all joints with snoop solution
- [ ] Hold 15 min, pressure drop ≤ 5%
- [ ] Repeat for anode side

### Liquid leak test
- [ ] Fill anolyte loop completely
- [ ] Run pump at 500 ml/min for 30 min
- [ ] Inspect every fitting and cell gasket — zero drips
- [ ] Verify no liquid in cathode-side tubing (cross-leak through AEM = bad seal)

---

## Stage 5 — Cold flow uniformity

- [ ] Open CO2 to 1750 ml/min through stack at room temperature
- [ ] Read each per-cell flow meter
- [ ] All 5 cells within 350 ± 35 ml/min (±10%)
- [ ] If maldistributed: inspect manifold for blockage, re-trim branches
- [ ] If uniform: record values as commissioning baseline

---

## Stage 6 — DAQ and software

- [ ] Install controller software: `pip install -r requirements.txt`
- [ ] Run simulation: `python electrolyzer_control.py --simulate --duration 0.5`
      → completes without error, generates `runs/<timestamp>/samples.csv`
- [ ] Run with fault injection: `--fault cell3_fail_at_5h --time-scale 1200`
      → confirm cell 3 V deviation triggers ABORT with correct alarm code
- [ ] Verify CSV format readable by analysis tools (pandas, Excel)

---

## Stage 7 — Thermal commissioning

- [ ] Start anolyte recirculation at 500 ml/min
- [ ] Set all heaters to 50 °C
- [ ] Start CO2 flow at 200 ml/min N2 carrier (don't bubble through acid yet)
- [ ] Monitor temperatures every 5 min
- [ ] All temperatures reach 50 °C ± 2 within 60 min
- [ ] Hold at 50 °C for 30 min, verify stable
- [ ] Switch CO2 line to bubble through 0.5 M CH3COOH humidifier
- [ ] Verify outlet humidity (should see acid vapor, mild vinegar smell at vent)

---

## Stage 8 — Polarization curve (commissioning, NOT durability)

- [ ] All Stage 1–7 items checked
- [ ] System at 50 °C, full CO2 flow with acid humidification, anolyte circulating
- [ ] OCV stabilized for 10 min, all cell V within 0.05 V of each other
- [ ] Apply current sequentially: 25, 50, 75, 100 mA/cm²; hold 10 min each
- [ ] At each step: record stack V, all 5 cell V, GC measurement (FE CO + H2)
- [ ] At 100 mA/cm²: FE(CO) ≥ 90 % expected
- [ ] No single cell V > 0.1 V different from stack-mean cell V at any current

---

## Stage 9 — Sign-off

- [ ] All Stage 1–8 items completed
- [ ] Polarization curve attached to commissioning record
- [ ] Initial K⁺ and pH measurements logged
- [ ] Operator briefed on alarm codes and abort response
- [ ] Emergency procedures posted at the bench
- [ ] Run #1 scheduled

Operator signature: ________________________ Date: ________________
Reviewer signature: ________________________ Date: ________________
