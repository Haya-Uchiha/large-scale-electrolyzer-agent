# August 2026 — data registry (`writing.agent/plotted graphs/August/`)

System (all three runs unless noted): **0.5NiSAC cathode + AEM (40 µm) + IrO₂-TiPt anode**
— a NiSAC-in-AEM hybrid (not classic Track 1 BPM nor Track 2 Ag NPs). All values read
from the figure images are marked `[estimated]`; verify against raw GC/DAQ logs.
Config strings are quoted verbatim from the figure labels.

Figure ↔ to-do mapping: Fig 1 → to-do #1 (tilt-angle 100 cm²); Fig 2 → to-do #2 (IrO₂-TiPt
fabrication + OER); Fig 3 → to-do #3 (5 vs 100 cm² long-term stability).

---

## Figure 1 — Long-term CO₂ electrolysis at 15° and 45° tilt, 200 mA cm⁻²

**Filename**: `Figure 1_Long-term CO2 electrolysis at 15 and 45 angle at 200mA:cm2.png`
**Config**: 100 cm², 0.5NiSAC | AEM (40 µm) | IrO₂-TiPt; 350/250 µm silicone gaskets,
8 ft·lb; parallel cathode flow-field; 50 mM CH₃COOH-humidified CO₂ at 400 mL/min;
100 mL/min 0.1 M KHCO₃ anolyte; 200 mA cm⁻²; tilted operation (15° vs 45° from vertical).
Panels: top = %FE(CO) markers + cell V vs time (both angles overlaid); bottom = per-angle
pressure profile (AN/CA inlet+outlet) and outlet-gas (SLPM) profile.

| Quantity | 15° tilt | 45° tilt | Source to verify |
|---|---|---|---|
| FE(CO), plateau | ≈ 97 % `[estimated]` | ≈ 97 % `[estimated]` | GC CSV |
| FE(CO), end-of-life | drops near end `[TBD]` | drops at flooding `[TBD]` | GC CSV |
| Durability | ≈ 72 h `[estimated]` | ≈ 60 h `[estimated]` | DAQ logger CSV |
| Cell V, initial | ≈ 3.15 V `[estimated]` | ≈ 3.25 V `[estimated]` | DAQ logger CSV |
| Cell V, final trend | gradual rise → ≈ 3.7 V | sharp oscillatory rise → ≈ 4.3 V at ≈ 58 h | DAQ logger CSV |
| AN inlet pressure | ≈ 85 mBar `[estimated]` | ≈ 85 mBar `[estimated]` | pressure channel |
| CA inlet pressure | ≈ 35 mBar `[estimated]` | ≈ 35 mBar `[estimated]` | pressure channel |
| CA outlet pressure | ≈ 22 mBar `[estimated]` | ≈ 22 mBar `[estimated]` | pressure channel |
| CA outlet gas | ≈ 0.30 SLPM `[estimated]` | ≈ 0.30 → 0.45 SLPM at flooding `[estimated]` | flow log |
| Intervention spikes | ≈ 4, 27, 67 h | ≈ 4, 16, 44 h | N₂-purge / anolyte-refresh log |

**Failure event / mechanism**: 45° panel is Heng-annotated **"Complete GDE flooding"**;
cell V shows a sharp oscillatory rise at ≈ 58 h. 15° reached ≈ 72 h with only a gradual
V rise. Observation: shallower tilt (15°) outlasted steeper tilt (45°) at 200 mA cm⁻².
Mechanism reported per Heng's own annotation (GDE flooding), not an independent claim.

---

## Figure 2 — OER performance of as-prepared IrO₂-TiPt anode (100 cm²)

**Filename**: `Figure 2_OER performance of as-prepared IrO2-TiPt anode.png`
**Config (from label)**: 39BB-GDE | BPM | IrO₂-TiPt; humidified N₂ (200 mL/min);
100 mL/min 0.1 M KHCO₃; 100 mA cm⁻²; 1 h benchmark. N₂ (not CO₂) feed → isolates the
anode/OER contribution to cell voltage.

| Sample | Cell voltage | Note |
|---|---|---|
| Old-IrO₂ (dashed) | ≈ 4.8 V, slight decline to ≈ 4.75 V `[estimated]` | prior batch |
| New-IrO₂-1 | ≈ 4.5–4.55 V, stable `[estimated]` | re-fabricated |
| New-IrO₂-2 | ≈ 4.5–4.55 V, stable `[estimated]` | re-fabricated (repeat) |

**Key result**: re-fabrication lowers cell voltage by ≈ 0.3 V vs the old anode; New-1 and
New-2 near-overlap → batch-to-batch reproducibility. Verify absolute V and Δ against DAQ log.

---

## Figure 3 — 5 vs 100 cm² long-term CO₂ stability, 100 mA cm⁻²

**Filename**: `Figure 3_Comparison of long-term CO2 stability of 5 and 100 cm2 MEA cell at 100mA:cm2.png`
**Config (from label)**: 0.5NiSAC (850 °C-4h-10 °C min⁻¹) | AEM (40 µm) | IrO₂-TiPt;
(500 mM or 50 mM) CH₃COOH-humidified CO₂ at 4 mL CO₂ min⁻¹ cm⁻²; 100 mL/min 0.1 M KHCO₃;
100 mA cm⁻². Panels: 5 cm² (top), 100 cm² (middle), overlay (bottom). rate_deg = per-segment
cell-voltage degradation between anolyte refreshes (sawtooth recoveries).

| Quantity | 5 cm² | 100 cm² | Source to verify |
|---|---|---|---|
| FE(CO), plateau | ≈ 97–98 % `[estimated]` | ≈ 97–98 % `[estimated]` | GC CSV |
| FE(CO), end-of-life | held to ≈ 595 h | drops to ≈ 70 % at ≈ 590 h `[estimated]` | GC CSV |
| Cell V, plateau | ≈ 3.2 V `[estimated]` | ≈ 3.2 V `[estimated]` | DAQ logger CSV |
| Total duration | ≈ 595 h `[estimated]` | ≈ 590 h `[estimated]` | DAQ logger CSV |
| rate_deg (mV h⁻¹) | 1.174, 0.948, 0.907, 0.450, 0.968, 0.634 | 0.768, 0.830, 0.652, **4.512** | rate_deg fit |
| Refresh interval | ≈ 100 h | ≈ 150 h | anolyte-refresh log |

**Key result**: both cells track closely through ≈ 520 h at ≈ 3.2 V / ≈ 97 % FE(CO); the
100 cm² cell then enters accelerated degradation (final rate_deg 4.512 mV h⁻¹, ≈ 5–7×
higher than its earlier segments) with a sharp V rise and FE(CO) collapse to ≈ 70 % near
590 h → scale-up durability penalty. rate_deg values are printed on the figure (transcribe
exactly); FE(CO) markers `[estimated]`.
