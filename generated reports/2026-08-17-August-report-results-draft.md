# August 2026 monthly report — Results (draft)

System: 0.5NiSAC cathode + AEM (40 µm) + IrO₂-TiPt anode (NiSAC-in-AEM hybrid).
All values read from figure images are marked `[estimated]`; unreadable values `[TBD]`.
rate_deg values in §3 are transcribed directly from the figure and are not estimates.

---

## Effect of cell tilt angle on CO₂RR durability at 100 cm² and 200 mA cm⁻²

To evaluate the effect of gravity-assisted drainage on flooding-limited durability, the
100 cm² 0.5NiSAC/AEM cell equipped with a parallel cathode flow-field was operated at
200 mA cm⁻² while tilted 15° and 45° from vertical, with 50 mM CH₃COOH-humidified CO₂
supplied at 400 mL/min and 100 mL/min of 0.1 M KHCO₃ recirculated as the anolyte. As
shown in Figure 1, FE(CO) was maintained at ≈ 97 % `[estimated]` for both tilt angles
over the majority of each run, while the cell voltage rose gradually from ≈ 3.15 V to
≈ 3.7 V `[estimated]` for the 15° configuration and reached ≈ 72 h `[estimated]` before
failure. In contrast, the 45° configuration failed earlier at ≈ 60 h `[estimated]`,
where the cell voltage underwent a sharp oscillatory excursion to ≈ 4.3 V `[estimated]`
at ≈ 58 h `[estimated]` accompanied by the "complete GDE flooding" event annotated on the
outlet-gas channel, in which the cathode outlet flow spiked from ≈ 0.30 to ≈ 0.45 SLPM
`[estimated]`. The oscillatory voltage signature and the concurrent outlet-flow surge are
consistent with accumulated liquid water breaching the gas pathway and flooding the
gas-diffusion electrode, rather than a kinetic or membrane failure. That the shallower 15°
tilt outlasted the steeper 45° tilt indicates that, at 200 mA cm⁻², the higher
water-generation rate overwhelms the incremental drainage benefit of a steeper angle, so
the deeper tilt does not translate into longer flooding-limited durability. It is worth
noting that the periodic pressure spikes at ≈ 4, 27, and 67 h (15°) and ≈ 4, 16, and 44 h
(45°) `[estimated]` correspond to the in-situ recovery interventions; the reversibility of
these excursions supports channel/GDE water management, not irreversible degradation, as
the limiting mechanism.

**Figure 1.** Long-term CO₂ electrolysis of the 100 cm² 0.5NiSAC | AEM (40 µm) | IrO₂-TiPt
MEA under 15° and 45° tilted operation at 200 mA cm⁻², with 50 mM CH₃COOH-humidified CO₂
(400 mL/min), 100 mL/min of 0.1 M KHCO₃ anolyte, 350/250 µm silicone gaskets, and 8 ft·lb
compression: (top) %FE(CO) and cell voltage versus time for both tilt angles; (bottom)
per-angle pressure profiles (anode/cathode inlet and outlet) and outlet-gas flow profiles.

---

## Reproducibility and voltage improvement of the re-fabricated IrO₂-TiPt anode

To ascertain the reproducibility of the re-fabricated anode and its effect on cell
voltage, the OER performance of the as-prepared IrO₂/TiPt-felt electrodes was benchmarked
at 100 cm² and 100 mA cm⁻² under a humidified N₂ feed (200 mL/min) with 100 mL/min of
0.1 M KHCO₃ anolyte, such that the measured cell voltage isolates the anodic contribution
in the absence of CO₂RR. As shown in Figure 2, the two re-fabricated anodes (New-IrO₂-1
and New-IrO₂-2) sustained a stable cell voltage of ≈ 4.5–4.55 V `[estimated]` and
near-overlapping traces over the 1 h test, whereas the previous batch (Old-IrO₂) operated
at ≈ 4.8 V `[estimated]`. The ≈ 0.3 V `[estimated]` reduction in cell voltage demonstrates
that the revised fabrication yields a more active anode, while the close overlap of the two
new electrodes confirms batch-to-batch reproducibility of the thermal-deposition procedure.
This improvement directly lowers the operating voltage available to the full CO₂RR cell and
provides a qualified anode for the subsequent long-term stability tests.

**Figure 2.** OER performance of as-prepared IrO₂/TiPt-felt anodes (Old-IrO₂, New-IrO₂-1,
New-IrO₂-2) in a 100 cm² MEA (39BB-GDE | BPM | IrO₂-TiPt) under humidified N₂ (200 mL/min)
with 100 mL/min of 0.1 M KHCO₃ anolyte at 100 mA cm⁻²: cell voltage versus time.

---

## Effect of cell active area (5 vs 100 cm²) on long-term CO₂RR stability at 100 mA cm⁻²

To evaluate the effect of cell active area on long-term durability, the 0.5NiSAC
(850 °C-4h-10 °C min⁻¹) | AEM (40 µm) | IrO₂-TiPt system was operated at 100 mA cm⁻² in
both 5 cm² and 100 cm² MEA cells under CH₃COOH-humidified CO₂ (4 mL CO₂ min⁻¹ cm⁻²) with
100 mL/min of 0.1 M KHCO₃ anolyte and periodic anolyte refreshes. As shown in Figure 3,
both cells sustained FE(CO) of ≈ 97–98 % `[estimated]` and a cell voltage of ≈ 3.2 V
`[estimated]` and tracked one another closely through ≈ 520 h `[estimated]`, with the 5 cm²
cell exhibiting low per-segment degradation rates of 0.450–1.174 mV h⁻¹ across its ≈ 595 h
`[estimated]` run. Beyond ≈ 520 h, however, the 100 cm² cell entered an accelerated
degradation regime, with the final-segment rate rising to 4.512 mV h⁻¹ — roughly five- to
seven-fold higher than its earlier segments (0.652–0.830 mV h⁻¹) — followed by a sharp
voltage rise and an FE(CO) collapse to ≈ 70 % `[estimated]` near 590 h `[estimated]`. The
sawtooth voltage recoveries after each anolyte refresh confirm that the baseline
degradation is dominated by reversible K⁺/carbonate accumulation, whereas the terminal
runaway unique to the larger cell indicates a scale-dependent onset of irreversible
GDE-level salt/water accumulation. This scale-up penalty — comparable early-life behaviour
but earlier terminal failure at 100 cm² — identifies late-stage salt/water management as
the key barrier to translating small-cell stability to the 100 cm² scale.

**Figure 3.** Comparison of long-term CO₂ electrolysis stability of 5 cm² and 100 cm²
0.5NiSAC (850 °C-4h-10 °C min⁻¹) | AEM (40 µm) | IrO₂-TiPt MEA cells at 100 mA cm⁻² under
CH₃COOH-humidified CO₂ (4 mL CO₂ min⁻¹ cm⁻²) with 100 mL/min of 0.1 M KHCO₃ anolyte:
%FE(CO) and cell voltage versus time for (top) the 5 cm² cell, (middle) the 100 cm² cell,
and (bottom) the overlaid comparison, with per-segment voltage degradation rates (rate_deg)
annotated between anolyte refreshes.

---

### Placeholders / values to verify
- FE(CO) ≈ 97–98 % on Figures 1 and 3 read from marker positions near the 100-line —
  confirm against GC CSV.
- Figure 1 durability (15° ≈ 72 h, 45° ≈ 60 h), initial/final cell voltages, pressures,
  and outlet-gas values — confirm against DAQ logger / pressure / flow channels.
- Figure 1 intervention timings (≈ 4/27/67 h and ≈ 4/16/44 h) — confirm against the
  N₂-purge / anolyte-refresh log.
- Figure 2 absolute voltages (≈ 4.8 V old, ≈ 4.5–4.55 V new) and the ≈ 0.3 V delta —
  confirm against DAQ logger.
- Figure 3 FE(CO) collapse value (≈ 70 %) and timing (≈ 590 h), plateau voltage (≈ 3.2 V),
  and total durations — confirm against GC/DAQ CSV. rate_deg values transcribed from the
  figure; confirm the fit windows.
