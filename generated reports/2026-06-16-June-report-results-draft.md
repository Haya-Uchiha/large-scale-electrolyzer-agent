# June monthly report — Results (draft)

Track 2 (Ag NPs / AEM / KHCO₃), 100 cm² parallel flow-field, 100 mA·cm⁻². Source of truth
for the formatted `.docx`. Estimated values from figure images are marked `[estimated]`;
unverified values are marked `[TBD]`.

---

## Results

### Effect of CO₂ flow rate on FE(CO) durability in the 100 cm² parallel flow-field

To evaluate the effect of CO₂ flow rate on operational durability, the 100 cm² parallel
flow-field MEA was operated galvanostatically at 100 mA·cm⁻² under humidified CO₂ (50 mM
CH₃COOH) supplied at 200, 400, and 800 ml·min⁻¹ (2, 4, and 8 ml·min⁻¹·cm⁻², respectively).
As shown in Figure 1, all three conditions delivered a comparable initial FE(CO) of
~90–95 % [estimated], whereas the duration of stable operation scaled monotonically with the
CO₂ flow rate: the 200 ml·min⁻¹ condition declined first (~20 h [estimated]), followed by
400 ml·min⁻¹ (~25 h [estimated]), while 800 ml·min⁻¹ sustained FE(CO) the longest (~33–36 h
[estimated], FE(CO) ~78–80 % at ~33 h). Throughout each run, the cell voltage remained stable
at ~3.2–3.3 V. The stable voltage signature indicates that failure proceeded by surface
channel water blockage rather than deep gas-diffusion-electrode pore flooding, for which a
decreasing voltage would be expected; the PTFE hydrophobicity of the GDE was therefore
retained. The improvement with increasing flow rate is attributed to the higher per-channel
gas velocity, which clears accumulated liquid water more effectively and delays channel
blockage. According to our previous results, increasing the CO₂ flow rate delays but does not
eliminate parallel-flow-field failure, since the underlying low per-channel velocity at any
individual channel remains the geometric constraint. The complementary cell-voltage and
cathode vent-pressure profiles for the 800 ml·min⁻¹ condition (Figure 1, lower panels) confirm
stable operation: the second run maintained ~3.2 V for ~40 h with pressure excursions limited
to gas-chromatography injection events, whereas the first run exhibited an abrupt voltage drop
at ~13–15 h [estimated] consistent with a short-circuit event rather than a flow-field
limitation. It is worth noting that this short-circuit behaviour is distinct from the gradual
flow-field decline and is addressed separately below.

**Figure 1.** Influence of CO₂ flow rate (200, 400, 800 ml·min⁻¹) on FE(CO) and cell voltage
of the AgNPs (50 nm, ~0.6 mg·cm⁻²) / AEM / IrO₂-TiPt 100 cm² parallel-flow-field MEA under
50 mM CH₃COOH humidified CO₂, 150 ml·min⁻¹ [TBD] 0.1 M KHCO₃ anolyte, 100 mA·cm⁻². Lower
panels: cell-voltage and cathode vent-pressure profiles for two 800 ml·min⁻¹ runs with a
PiperION AEM.

---

### Effect of membrane thickness on short-circuit susceptibility under 30° tilted operation

To ascertain the effect of membrane thickness on operational stability during gravity-assisted
drainage, the 100 cm² parallel flow-field MEA was tilted to a 30° orientation and operated at
100 mA·cm⁻² under 400 ml·min⁻¹ humidified CO₂, comparing a thin 20 µm PiperION membrane
(Figure 2) with a thicker 40 µm AEM (Figure 3); the flat 0° orientation was run in parallel as
a reference in both cases. As shown in Figure 2, the 20 µm membrane delivered a high initial
FE(CO) of ~96–98 % that remained stable to ~10 h, after which a first short-circuit event
(~10 h) reduced FE(CO) by ~20 %, followed by a second short-circuit event (~25 h) that reduced
FE(CO) by a further ~35 %. The mean cell voltage was 3.227 ± 0.072 V, remaining otherwise flat
between events with discrete downward steps coinciding with each short-circuit. This signature
— an abrupt voltage perturbation and a stepwise FE(CO) loss against an otherwise stable
baseline — identifies an electrical breach of the membrane rather than GDE flooding or kinetic
degradation. In contrast, the 40 µm membrane (Figure 3) sustained ~95 % [estimated] FE(CO)
without any short-circuit event over a markedly longer run. This comparison demonstrates that
membrane thickness governs short-circuit susceptibility under the mechanical loading of the
tilted 100 cm² assembly: the 20 µm membrane is too thin to withstand compression in the
tilted configuration, whereas the 40 µm membrane preserves electrical isolation. It is worth
noting that the 30° tilt alone is insufficient to prevent failure when the membrane is thin,
so adequate membrane thickness is a prerequisite for exploiting tilted-drainage operation.

**Figure 2.** Long-term CO₂ electrolysis of the AgNPs (50 nm, ~0.6 mg·cm⁻²) / PiperION 20 µm /
IrO₂-TiPt 100 cm² parallel-flow-field MEA at 0° and 30° orientation under 50 mM CH₃COOH
humidified CO₂ (400 ml·min⁻¹), 100 ml·min⁻¹ 0.1 M KHCO₃, 100 mA·cm⁻². Lower panel: cell
voltage (3.227 ± 0.072 V) and cathode outlet pressure, with two short-circuit events annotated.

---

### Recovery interventions and post-mortem analysis of extended 100 cm² operation

To evaluate whether in-situ recovery interventions can extend operation in the tilted
configuration, the 40 µm AEM cell at 30° orientation (400 ml·min⁻¹ humidified CO₂,
100 mA·cm⁻²) was operated with periodic maintenance and subsequently disassembled for
post-mortem inspection. As shown in Figure 3, the cell sustained ~95 % [estimated] FE(CO) at a
stable cell voltage of ~3.2–3.3 V for ~195–200 h, with the cathode outlet pressure held at
~30–40 mBar. Four interventions were applied over the run: an immediate shutdown-and-rerun at
80 h, a 4 h dried-N₂ purge with rerun at 87 h, an 8 h dried-N₂ purge at 140 h, and a refresh
of the 0.1 M KHCO₃ anolyte at 160 h. The transient FE(CO) excursions to ~80 % [estimated]
around 80, 110, and 150 h, each recovering after the corresponding intervention, indicate that
the dominant degradation was reversible channel water/salt accumulation rather than
irreversible catalyst or membrane failure; the stable voltage throughout confirms the
channel-blockage regime, and the dried-N₂ purge re-opened the gas pathways while the anolyte
refresh restored the K⁺/carbonate balance. Post-mortem inspection of the disassembled cell
(Figure 4) showed relatively clean parallel-flow-field channels with only minor residue, mild
grayish salt deposition on the AgNPs gas-diffusion electrode, and an intact 40 µm membrane
with no visible physical breach [TBD — confirm from photos], all consistent with the sustained
FE(CO) and stable voltage recorded during the run. These observations indicate that combining
a 40 µm membrane, 30° gravity-assisted drainage, and periodic dried-N₂ purging with anolyte
refresh extends stable 100 cm² operation to ~195–200 h, with mild GDE salt deposition
remaining the residual degradation pathway to be addressed.

**Figure 3.** Long-term CO₂ electrolysis of the AgNPs (50 nm, ~0.6 mg·cm⁻²) / AEM 40 µm /
IrO₂-TiPt 100 cm² parallel-flow-field MEA at 0° and 30° orientation under 50 mM CH₃COOH
humidified CO₂ (400 ml·min⁻¹), 100 ml·min⁻¹ 0.1 M KHCO₃, 100 mA·cm⁻², reaching ~195–200 h.
Lower panel: cell voltage and cathode outlet pressure with recovery interventions annotated
(shutdown-rerun at 80 h; dried-N₂ purge at 87 h and 140 h; anolyte refresh at 160 h).

**Figure 4.** Post-mortem photographs of the 100 cm² MEA after 195 h of CO₂RR, showing the
parallel flow-field plate, AgNPs gas-diffusion electrode, and 40 µm AEM after 140 h and 195 h
of operation.

---

## Placeholders / values Heng must verify

1. **Fig 1 anolyte flow rate** — figure label reads 150 ml·min⁻¹, docx procedure reads
   100 ml·min⁻¹. Confirm which applies to the flow-rate study.
2. **Fig 1 durations & end FE(CO)** — exact stable-window end times and end FE(CO) for 200 /
   400 / 800 ml·min⁻¹ from GC CSV (currently `[estimated]`).
3. **Fig 1 short-circuit timestamp** — exact time of the 1st-run 800 ml·min⁻¹ short-circuit
   (~13–15 h).
4. **Fig 2 short-circuit timing & FE loss** — exact event times (~10 h, ~25 h) and FE(CO)
   before/after each from GC CSV.
5. **Fig 3 FE(CO) values** — values at the scatter dips (~80 / 110 / 150 h) and whether the
   0° run was stopped intentionally at ~25 h.
6. **Fig 4 post-mortem** — confirm salt-deposit location, channel cleanliness, and membrane
   condition from raw photos (currently `[TBD]`).

## Suggested next step

Confirm the values above (especially items 1–2), then I will update the `.docx` with the
corrected numbers and commit. Next month's runs move to 45° tilt at 400 / 800 ml·min⁻¹ per
the Upcoming tasks list.
