# May Figures — Data Registry & Analysis
Track 2 (Ag NPs / AEM / KHCO₃) unless noted. All experiments: 100 mA/cm².

---

## Figure 1 — 5 cm² repeat runs: AgNPs/AEM/IrO₂-TiPt (baseline reproducibility)

**System**: AgNPs (>100 nm, 0.6 mg/cm²) | AEM (Sustanion) | IrO₂-TiPt — 5 cm² MEA
**Conditions**: 50 mM CH₃COOH humidified CO₂ (20 ml/min) — 4 ml/min 0.1 M KHCO₃ — 100 mA/cm²

| | Run (a) — 1st | Run (b) — 2nd |
|---|---|---|
| Initial FE(CO) | ~70–75% | ~20–30% |
| Peak FE(CO) | ~80% (~100 h) | ~80–85% (scattered) |
| Duration | ~300 h (membrane damaged ~200–250 h) | ~350 h |
| Cell voltage | ~3.5 V stable | ~3.5 V stable |
| Post-mortem | AEM discolouration / physical damage observed | [TBD — inspect photos] |

**Extracted values to confirm**: exact GC-point FE values at each time point [TBD from raw data].
**Failure mechanism**: Run (a) — AEM physical degradation (confirmed by "membrane damaged" annotation and post-run photo). Run (b) — lower initial FE suggests fresh assembly variation; no catastrophic failure observed.
**Note**: voltage stable in both runs — failure not GDE flooding (which would show V decrease); no rising V (not kinetic degradation). AEM integrity is the limiting factor in Run (a).

---

## Figure 2 — Two-panel: AgNP particle size (5 cm²) + Flow-field comparison (100 cm²)

### Figure 2 (top) — 5 cm² AgNPs: 50 nm vs >100 nm

**System**: AgNPs (0.6 mg/cm²) | AEM (Sustanion) | IrO₂-TiPt — 5 cm² MEA
**Conditions**: 0.5 M CH₃COOH humidified CO₂ (20 ml/min) — 4 ml/min 0.1 M KHCO₃ — 100 mA/cm²

| | AgNPs 50 nm (blue) | AgNPs >100 nm (orange) |
|---|---|---|
| Initial FE(CO) | ~90% | ~85–90% |
| FE(CO) at ~15 h | ~90% | ~90% |
| FE(CO) at ~40 h | [TBD] | ~90% |
| Duration | ~45 h | ~45 h |
| Cell voltage | ~3.5 V stable | ~3.5 V stable |

**Key observation**: Both particle sizes sustain high FE(CO) with 0.5 M CH₃COOH acid at 5 cm² scale. Larger particles (>100 nm) show marginally better sustained FE(CO) across the run; 50 nm particles show comparable behaviour. No clear voltage divergence — neither failure mechanism (flooding nor kinetic degradation) triggered within the run window.

---

### Figure 2 (bottom) — 100 cm² flow-field comparison
### ⟵ LINKED WITH FIGURE 3 (read together — see §Fig2–Fig3 Linkage below)

**System**: AgNPs (>100 nm, 0.4–0.5 mg/cm²) | AEM (Sustanion) | IrO₂-TiPt — 100 cm² MEA
**Conditions**: 50 mM CH₃COOH humidified CO₂ (200 ml/min) — 100 ml/min 0.1 M KHCO₃ — 100 mA/cm²

| Flow-field | Initial FE(CO) | Durability | End FE(CO) | Voltage trend |
|---|---|---|---|---|
| Single-serpentine (blue) | ~93% | ~55 h (flushing at ~47–50 h) | ~60% at 55 h | Decreases with FE drop |
| Quad-serpentine (orange) | ~93% | ~43 h | ~70% at 43 h | Decreases with FE drop |
| Parallel (purple) | ~92% | ~20 h | [TBD] | **Stable** despite FE drop |

**Flushing event** (single-serpentine, ~47–50 h): FE(CO) recovers briefly after high-flow CO₂ purge; voltage partially recovers. Confirms GDE flooding (not catalyst deactivation) as dominant failure mode — flushing re-opens gas pathways temporarily.

---

## Figure 3 — Cathode inlet pressure: flow-field comparison (100 cm²)
### ⟵ LINKED WITH FIGURE 2 (bottom) — same experiment, complementary diagnostic

**Same system and conditions as Figure 2 (bottom).**
Photos: Quad-Serp / Single-Serp / Parallel flow-field plate images (pre-experiment).

| Flow-field | Initial pressure | Pressure trend | Notable events |
|---|---|---|---|
| Single-serpentine (blue) | ~80 mbar | Rises steadily to ~120–130 mbar by 50 h; spikes throughout | Flushing (~47–50 h) causes abrupt drop, then rises again |
| Quad-serpentine (orange) | ~80 mbar | Rises steadily; ends ~43 h | Similar progressive rise as single-serp |
| Parallel (purple) | ~60–70 mbar | Brief spike to ~180–200 mbar at ~1 h; drops and stabilises ~80–90 mbar until ~20 h | Early spike then stable — consistent with rapid channel blockage then partial clearing |

**Units on pressure axis**: [TBD — confirm whether mbar or arbitrary DAQ units from raw CSV].

---

## Fig 2 (bottom) — Fig 3 Linkage: Combined Mechanistic Interpretation

These two figures report the **same experiment** from two complementary measurement channels: Fig 2 (bottom) captures the electrochemical signatures (FE(CO) + cell voltage), and Fig 3 captures the hydraulic signature (cathode CO₂ inlet pressure). Interpreted together:

**Single-serpentine and Quad-serpentine**:
- FE(CO) declines gradually (Fig 2) **and** inlet pressure rises progressively (Fig 3) — both consistent with the salt-formation cascade: K⁺-mediated carbonate/bicarbonate crystallisation accumulates at the serpentine CO₂ inlet, restricting gas flow (rising pressure) and starving the GDE of CO₂ (falling FE). As CO₂ starvation deepens, product water back-floods GDE pores, shifting the reaction to HER. The cell voltage **decreases** (Fig 2) as iR and η_conc both drop upon flooding — the "serpentine GDE flooding" voltage fingerprint.
- The flushing event in single-serpentine (green band, Fig 2; pressure dip, Fig 3) temporarily restores CO₂ pathways: FE(CO) and voltage both recover briefly before resuming decline — confirming physical GDE flooding rather than catalyst deactivation as the limiting mechanism.

**Parallel**:
- FE(CO) collapses faster (~20 h, Fig 2), yet cell voltage **remains stable** (Fig 2) — confirming channel water blockage without deep GDE pore flooding (PTFE hydrophobicity intact). The brief pressure spike at ~1 h (Fig 3) indicates rapid water accumulation in low-velocity parallel channels; the subsequent stabilisation reflects partial clearing but continued channel blockage at isolated positions. Because GDE pores are not flooded, ohmic resistance and CO₂ concentration overpotential at the remaining active area do not change, keeping voltage flat even as active area shrinks.

**Summary**: rising pressure (Fig 3) = leading indicator of salt/water blockage; voltage direction (Fig 2) = identifies whether blockage has progressed to GDE pore flooding (decreasing V) or remains in channels (stable V).

---

## Figure 4 — AgNPs (100 nm) vs 0.5Ni-SAC in AEM system (5 cm² and 100 cm²)

**Title**: Acid Humidifier CO₂ of 5 cm² AEM system: AgNPs (100 nm) vs 0.5Ni-SAC (800°C–4 h–10°C/min)

### Top panel — 5 cm² comparison

**System**: AgNPs (0.6 mg/cm², blue) and 0.5NiSAC (1.8 mg/cm², orange) | AEM (Sustanion) | IrO₂-TiPt
**Conditions**: 0.5 M CH₃COOH humidified CO₂ (200 ml/min) — 100 ml/min 0.1 M KHCO₃ — 100 mA/cm²

| | AgNPs 100 nm (blue) | 0.5NiSAC (orange) |
|---|---|---|
| Initial FE(CO) | ~96–97% | ~80–82% |
| FE(CO) at ~50 h | ~96% | ~78% |
| FE(CO) at ~150 h | ~96% | ~80% |
| FE(CO) at ~250 h | ~83–85% | ~80% |
| FE(CO) at ~290 h | ~60–62% | ~80% |
| FE(CO) at ~350 h | ~80% | ~77–78% |
| Duration | ~360 h | ~360 h |
| Initial cell voltage | ~3.0 V | ~3.5 V |
| Final cell voltage | ~3.5 V | ~4.5–5.0 V |
| Voltage trend | Gradual rise (~0.5 V over 360 h) | Steep rise after ~200 h |

**Failure mechanism**:
- **0.5NiSAC (orange)**: steep voltage rise after ~200 h with declining FE(CO) → **kinetic degradation** fingerprint (Ni-SAC site deactivation). Consistent with BPM-system NiSAC behaviour but here in AEM/KHCO₃ — the rising V confirms catalyst failure, not flooding.
- **AgNPs (blue)**: gradual voltage rise (~3.0 → 3.5 V) with maintained high FE(CO) to ~250 h → partial kinetic penalty from Ag catalyst aging and/or progressive mild flooding not fully suppressed by 0.5 M acid at 5 cm². The eventual FE(CO) drop at ~290 h may indicate onset of salt accumulation despite acid humidification.

### Bottom panel — 100 cm² 0.5NiSAC only (first scale-up test in AEM system)

**System**: 0.5NiSAC (1.8 mg/cm²) | AEM (Sustanion) | IrO₂-TiPt — 100 cm²
**Conditions**: 50 mM CH₃COOH humidified CO₂ (200 ml/min) — 100 ml/min 0.1 M KHCO₃ — 100 mA/cm²

| | Value |
|---|---|
| Duration | ~20 h (short initial test) |
| FE(CO) data | Not available (no GC measurements recorded) |
| Initial voltage | ~3.0 V |
| Voltage at 20 h | ~3.5 V |
| Voltage trend | Rising — consistent with kinetic degradation fingerprint |

**Note**: No FE(CO) data collected in this run (GC not yet connected or sampling not initiated). Voltage rise alone is consistent with NiSAC kinetic degradation but insufficient to confirm mechanism without GC data — further testing required.

---

## Figure 5 — CO₂ flow rate effect on 100 cm² parallel flow-field durability

**System**: AgNPs (50 nm, ~0.6 mg/cm²) | AEM (Sustanion) | IrO₂-TiPt — 100 cm² MEA, parallel flow-field
**Conditions**: 50 mM CH₃COOH humidified CO₂ (200 or 400 ml/min) — 100 ml/min 0.1 M KHCO₃ — 100 mA/cm²

| | 200 ml/min CO₂ (purple) | 400 ml/min CO₂ (teal) |
|---|---|---|
| Initial FE(CO) | ~93% | ~90% |
| FE(CO) at ~3 h | ~98% | ~98% |
| FE(CO) at ~8 h | ~95% | ~90% |
| FE(CO) at ~13 h | [TBD] | ~93% |
| FE(CO) at ~20 h | ~50% | ~85–88% |
| FE(CO) at ~24 h | ~73% | ~85% |
| Duration | ~24 h | ~24 h |
| Cell voltage | ~3.4 V stable throughout | ~3.45 V stable throughout |

**Failure mechanism**: Both conditions show **stable voltage** — parallel flow-field channel blockage fingerprint (no GDE pore flooding). Higher CO₂ flow rate (400 ml/min, 4 ml/min/cm²) substantially improves FE(CO) stability vs 200 ml/min (2 ml/min/cm²): higher per-channel velocity clears water plugs more effectively, extending stable operation. However, voltage is stable in both cases, confirming that the root cause is surface channel blockage (not deep GDE flooding) regardless of flow rate.

**Implication**: increasing CO₂ flow rate is a Tier-1 intervention that delays but does not eliminate parallel flow-field failure, as the underlying low per-channel velocity at any given channel remains the geometric constraint. This is consistent with the de-risking troubleshooting hierarchy (Tier 1: increase CO₂ flow to 3.5 → 5 ml/min/cm²).

---

## Values to confirm with Heng (TBD)

- [ ] Fig 1: exact GC FE(CO) values at each time point from raw CSV
- [ ] Fig 1: exact time of membrane damage event (appears ~200–250 h)
- [ ] Fig 2 (top): AgNPs 50 nm FE(CO) at 40 h
- [ ] Fig 2 (bottom): Parallel flow-field end FE(CO) at failure (~20 h)
- [ ] Fig 3: pressure axis units (mbar, mmH₂O, or arbitrary DAQ units)
- [ ] Fig 4 (bottom): why no GC data at 100 cm² NiSAC run — was GC not connected?
- [ ] Fig 4: confirm voltage values at key time points from raw data
- [ ] Fig 5: FE(CO) at ~13 h for 200 ml/min condition
