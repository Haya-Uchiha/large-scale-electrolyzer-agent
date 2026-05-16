# Operating SOP — 500 cm² Stacked CO2RR Electrolyzer

Standard operating procedure for Run #1 baseline durability test.

**Pre-condition**: All items in `commissioning_sop.md` are signed off.

---

## A. Cold start (~75 min)

| # | Action | Verify |
|---|---|---|
| A1 | Confirm anolyte reservoir level ≥ 90 % | Visual + level-switch normal |
| A2 | Confirm 0.5 M CH3COOH humidifier ≥ 75 % full | Visual |
| A3 | Confirm CO2 cylinder pressure > 30 bar | Regulator gauge |
| A4 | Confirm fume hood / vent active | Manometer or flow indicator |
| A5 | Confirm H2 and CO detectors armed and not in alarm | Indicator LEDs |
| A6 | Software: `python electrolyzer_control.py --hardware --duration 24` | Script connects to DAQ, MFC, galvanostat |
| A7 | Heaters set to 50 °C automatically by software (HEATING state) | Logger shows ramp |
| A8 | Anolyte pump starts at 500 ml/min automatically | Per-cell rotameters read 100 ml/min ±10 |
| A9 | Wait for thermal equilibrium (≤ 60 min real time) | All T within 50 °C ±2 |

---

## B. CO2 flow and OCV

| # | Action | Verify |
|---|---|---|
| B1 | Software auto-purges with N2 (5 min) | CO2 MFC at 0 |
| B2 | Software ramps CO2 to 1750 ml/min over 5 min | Per-cell flow meters all show 350 ml/min ±35 |
| B3 | OCV stabilization 10 min | All cell V within 0.05 V of each other; logger captures baseline |
| B4 | Operator review of OCV baselines | Sign run-log book before proceeding |

---

## C. Galvanostatic operation

| # | Action | Verify |
|---|---|---|
| C1 | Software auto-applies 10 A galvanostatic | Stack V settles in 16.5–17.5 V |
| C2 | First GC injection at 1 h | FE(CO) ≥ 90 % expected at startup |
| C3 | Hourly GC sampling continues automatically | Each result logged to `samples.csv` |
| C4 | Continuous monitoring of cell V, pressure, T, pH | Watch alarm log for WARN events |
| C5 | At 12 h: take anolyte sample for ICP-OES (off-line K⁺) | Log timestamp, sample ID |
| C6 | At 24 h: anolyte refresh (see procedure D) | Without stopping galvanostat if possible |

### Pass criteria for Run #1 (target)
- FE(CO) ≥ 80 % stack-averaged for ≥ 24 h
- SPU 10–20 % per cell
- No single-cell V deviation > 0.20 V from initial
- CO2 inlet pressure rise < 20 % over 24 h

### Abort triggers (automatic via software)
- Any cell V deviation > 0.30 V from initial
- Any cell V outside 2.5 – 4.5 V band
- Stack V > 22 V
- CO2 inlet pressure rise > 30 %
- E-stop, H2 detector, CO detector, low anolyte level

---

## D. Anolyte refresh (every 24 h)

Performed live without stopping the run:

1. Open drain valve on reservoir partially — drain ~ 10 L into neutralization tank
2. Add 10 L fresh 0.1 M KHCO3 (pre-heated to 50 °C in carboy)
3. Repeat in 10-L increments until full 50 L is replaced
4. Total time: ~ 30 min — pH should recover to 8.6 ± 0.1 within 15 min after final fill
5. Log refresh event in run log book

---

## E. Planned shutdown (after Run #1 duration target met)

| # | Action | Verify |
|---|---|---|
| E1 | Software auto-shutdown at end of duration | State → SHUTDOWN |
| E2 | Galvanostat → OCV | Cell V relaxes to OCV |
| E3 | Hold OCV under CO2 for 5 min | Allows residual species to dissipate |
| E4 | Software switches CO2 to N2 purge (10 min @ 200 ml/min) | Outlet GC reads no CO |
| E5 | Heaters off | Begin natural cool-down (~2 h to room T) |
| E6 | Anolyte pump runs additional 30 min during cool-down | Prevents hot-spots |
| E7 | When stack < 35 °C: pump off, drain anolyte to storage | |
| E8 | Final post-mortem inspection | See section F |

---

## F. Post-run inspection

1. Disassemble stack carefully; photograph each cell during teardown
2. Inspect each GDE backside (cathode side):
   - Salt crystals visible? Where? Quantify via image analysis or weighing
3. Inspect each AEM:
   - Color change? Discoloration at edges? Tears?
4. Cross-section SEM/EDX on cells 1, 3, 5 (first, middle, last in stack):
   - GDE-AEM interface integrity
   - K⁺ profile in GDE depth
   - Salt deposit composition (KHCO3 vs K2CO3 vs other)
5. Anolyte ICP-OES:
   - Final K⁺ concentration
   - Iridium dissolution markers (anode degradation)
6. Update run log book and project tracker

---

## G. Emergency response

### G1. Audible alarm + red ABORT light
1. Read alarm code on display
2. **Do not approach stack** until you know the trigger
3. If H2 or CO detector: evacuate, ventilate, call safety officer
4. If V_cell or pressure: software has already stopped current and closed CO2; safe to approach for inspection
5. Document alarm code, sample ID, timestamp

### G2. Visible leak
1. Press E-stop
2. Identify leak source (gas vs. liquid)
3. Gas leak: depressurize CO2, ventilate
4. Liquid leak: turn off pump, contain spill, neutralize per spill kit (KHCO3 is mild; CH3COOH at 0.5 M is mildly acidic but not corrosive at this concentration)
5. Do not restart until repaired

### G3. Power outage
1. Galvanostat output ceases (loss of power)
2. Solenoid valves close (fail-safe normally-closed)
3. Heaters off
4. Stack cools naturally
5. On power restoration: do not restart automatically — perform full Stage 7
   commissioning recheck before next run

### G4. Operator-initiated stop
- Press Ctrl+C in software console: graceful shutdown via state machine
- Press E-stop: hardwired immediate shutdown of CO2 + galvanostat
- Both options safe — software stop preferred for non-emergencies (logs final
  data cleanly)
