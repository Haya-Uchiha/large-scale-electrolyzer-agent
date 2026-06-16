# June Figures — Data Registry & Analysis
Track 2 (Ag NPs / AEM / KHCO₃), 100 cm² parallel flow-field, 100 mA/cm² throughout.
Theme: durability engineering of the parallel flow-field — CO₂ flow rate, MEA tilt
orientation, membrane thickness, and in-situ recovery interventions.

Angle confirmed with Heng: **30°** for all June runs (the "45° position" header in the
Fig 2 bottom panel is a label typo). 45° is next month's upcoming task.

---

## Figure 1 — Influence of CO₂ flow rate on durability (200 / 400 / 800 ml/min)

**Title**: Parallel flow-field 100 cm² MEA system: Influence of CO₂ flow rate on long-term CO₂ electrolysis
**System**: AgNPs (50 nm, ~0.6 mg/cm²) | AEM (PiperION for the two bottom-panel 800 ml/min runs) | IrO₂-TiPt — 100 cm² parallel flow-field
**Conditions**: 50 mM CH₃COOH humidified CO₂ (200, 400, 800 ml/min) — 150 ml/min 0.1 M KHCO₃ [figure label; docx procedure says 100 ml/min — TBD] — 100 mA/cm²

### Top panel — FE(CO) + cell voltage vs time, three flow rates
| CO₂ flow | Colour | Early FE(CO) | Durability (stable window) | End behaviour |
|---|---|---|---|---|
| 200 ml/min (2 ml/min/cm²) | purple | ~90–95% | shortest, ~20 h [estimated] | FE declines first |
| 400 ml/min (4 ml/min/cm²) | teal | ~90–95% | ~25 h [estimated] | FE ~88% at ~20 h then declines |
| 800 ml/min (8 ml/min/cm²) | red | ~90–95% | longest, ~33–36 h [estimated] | FE ~78–80% at ~33 h |
| Cell voltage (all) | — | ~3.2–3.3 V | **stable throughout** | parallel channel-blockage fingerprint |

### Bottom panels — 800 ml/min PiperION-AEM, two runs (cell V + CA vent pressure)
| | 1st Run | 2nd Run |
|---|---|---|
| Cell voltage | ~3.2 V stable | ~3.2 V stable |
| Duration | ~17.5 h | ~40 h |
| Notable event | **short-circuit event ~13–15 h** [estimated] | none — stable to ~40 h |
| CA vent pressure | low; spikes during GC injection only | low; spikes during GC injection only |

**Failure mechanism**: stable cell voltage in all conditions → parallel flow-field channel
water blockage (no deep GDE pore flooding; PTFE hydrophobicity holds — consistent with May
Fig 5). Higher CO₂ flow rate raises per-channel velocity, clearing water plugs more
effectively and extending the stable FE(CO) window (800 > 400 > 200 ml/min). A short-circuit
event in the 1st 800 ml/min run is a separate electrical failure (membrane breach / contact),
not flow-field related — distinguished by an abrupt voltage drop rather than a gradual trend.

---

## Figure 2 — Tilt-angle test, thin 20 µm PiperION membrane (0° vs 30°)

**Title**: Parallel flow-field 100 cm² MEA system: long-term CO₂ electrolysis of MEA cell at 30° angle
**System**: AgNPs (50 nm, ~0.6 mg/cm², + 10% XC ionomer) | PiperION AEM 20 µm | IrO₂-TiPt — 100 cm² parallel flow-field
**Conditions**: 50 mM CH₃COOH humidified CO₂ (400 ml/min) — 100 ml/min 0.1 M KHCO₃ — 100 mA/cm²
**Positions compared**: 0° (orange) vs 30° (blue)

| | Value |
|---|---|
| Initial FE(CO) (both positions) | ~96–98% |
| FE(CO) stable to | ~10 h |
| 1st short-circuit event | ~10 h — **FE(CO) loss ~20%** |
| 2nd short-circuit event | ~25 h — **FE(CO) loss ~35%** |
| Cell voltage (mean) | **3.227 ± 0.072 V** — stable, stepwise dips at each short-circuit |
| Duration | ~25 h |

**Failure mechanism**: the thin 20 µm membrane is prone to **short-circuiting** under
compression in the tilted assembly. Each short-circuit event steps FE(CO) down (cumulative
~20% then ~35% loss) while cell voltage stays otherwise flat between events — an electrical
breach signature, not GDE flooding or kinetic degradation. Tilting to 30° alone does not
prevent shorting when the membrane is this thin.

---

## Figure 3 — Tilt-angle test, 40 µm AEM (0° vs 30°) + recovery interventions (~195 h)
### ⟵ LINKED WITH FIGURE 4 (same cell; Fig 4 is its post-mortem)

**Title**: Parallel flow-field 100 cm² MEA system: long-term CO₂ electrolysis of MEA cell at 30° angle
**System**: AgNPs (50 nm, ~0.6 mg/cm²) | AEM 40 µm | IrO₂-TiPt — 100 cm² parallel flow-field
**Conditions**: 50 mM CH₃COOH humidified CO₂ (400 ml/min) — 100 ml/min 0.1 M KHCO₃ — 100 mA/cm²
**Positions compared**: 0° (orange — early data only, ~25 h) vs 30° (blue — sustained to ~195–200 h)

| | 30° position (blue) |
|---|---|
| FE(CO) | ~95% sustained, scatter to ~80% around 80 / 110 / 150 h then recovers [estimated] |
| Cell voltage | ~3.2–3.3 V stable across full run |
| CA outlet pressure | ~30–40 mBar, periodic spikes (GC injection) |
| Total duration | ~195–200 h |

**Recovery-intervention timeline (bottom panel labels)**:
| Time | Intervention |
|---|---|
| After 80 h | Shut down & rerun immediately |
| After 87 h | Purge dried N₂ for 4 h and rerun |
| After 140 h | Purge dried N₂ for 8 h |
| After 160 h | Refresh 0.1 M KHCO₃ anolyte |

**Mechanism / result**: the thicker 40 µm membrane eliminates the short-circuit failure seen
with 20 µm (Fig 2). Combined with 30° tilt (gravity-assisted water drainage from the parallel
channels) and **periodic in-situ recovery** — dried-N₂ purging to clear accumulated water/salt
and anolyte refresh to restore K⁺/carbonate balance — the cell sustained ~195–200 h at ~95%
FE(CO). Stable voltage throughout confirms the channel-blockage (not GDE-flooding) regime; the
interventions reset the blockage before it deepened.

---

## Figure 4 — Post-mortem of the 100 cm² MEA after 195 h operation
### ⟵ LINKED WITH FIGURE 3 (same 40 µm / 30° run)

**Title**: Post-mortem of 100 cm² MEA after 195 h operation
**Photos**: test rig; parallel flow-field plate; AgNPs GDE cathode; AEM membrane. Two time points labelled — "After 140 h of CO2RR" and "After 195 h of CO2RR".

| Component | Observation [confirm from photos — TBD] |
|---|---|
| Parallel flow-field plate | channels relatively clean; minor residue, no gross blockage |
| AgNPs GDE cathode | grayish surface deposits (mild salt / carbonate film) |
| AEM membrane (40 µm) | intact, grayish-white; no obvious physical breach |

**Interpretation**: relatively clean flow-field channels and an intact membrane after ~195 h
are consistent with the sustained FE(CO) and stable voltage in Fig 3 — the 30° drainage plus
periodic N₂ purge / anolyte refresh kept the channels clear and the membrane sound. Mild GDE
salt deposition remains the residual degradation pathway. Direct visual confirmation of
specific salt locations is [TBD] from higher-resolution photos.

---

## Values to confirm with Heng (TBD)
- [ ] Fig 1: anolyte flow rate — figure label says 150 ml/min, docx procedure says 100 ml/min
- [ ] Fig 1: exact per-flow-rate end durations and end FE(CO) (200 / 400 / 800 ml/min) from GC CSV
- [ ] Fig 1: exact timestamp of the 1st-run short-circuit event (~13–15 h)
- [ ] Fig 2: exact short-circuit timestamps (~10 h, ~25 h) and FE(CO) before/after each from GC CSV
- [ ] Fig 2: confirm "30°" (bottom-panel header reads "45°" — typo per Heng)
- [ ] Fig 3: FE(CO) values at the scatter dips (~80 / 110 / 150 h) from GC CSV
- [ ] Fig 3: confirm whether the 0° run was stopped intentionally at ~25 h
- [ ] Fig 4: confirm post-mortem observations (salt location, membrane condition) from raw photos
