# July Figures — Data Registry & Analysis
Hybrid configuration: **Track-1 catalyst (0.5NiSAC) operated on the Track-2 durability
platform** — 100 cm² MEA, AEM 40 µm, 0.1 M KHCO₃ anolyte, acetic-acid-humidified CO₂,
tilted operation, 100 mA/cm² throughout.
Theme: long-term (~600 h) durability of the NiSAC cathode on the AEM/tilt rig — the
longest continuous 100 cm² run to date, foreshadowed in June's "Upcoming tasks".

**Discrepancies flagged with Heng (do not silently resolve):**
1. **Tilt angle** — June forecast said "30° position"; July figure title reads **15° angle**.
   Registry uses 15° (matches the data). Confirm.
2. **NiSAC synthesis** — figure reads "850 °C-4h-10 °C·min⁻¹" (4 h); June forecast said
   "850 °C-2h"; §2 boilerplate says 800 °C/2 h. Confirm the actual July synthesis.
3. **Failure mechanism — resolved with Heng** — the ~590 h V + CA-outlet rise + HER increase
   is **water-driven GDE flooding**. Post-mortem (Fig 2) shows **no precipitated salt in the
   flow-field channels**, confirming carbonate/bicarbonate salt precipitation is NOT the
   failure cause. (Earlier fingerprint caveat withdrawn per Heng's interpretation + post-mortem.)

---

## Figure 1 — Effect of flow-field configuration & 15° tilt on long-term FE(CO) durability (100 cm², ~600 h)

**Title (figure)**: Parallel flow-field 100 cm² MEA system: long-term CO₂ electrolysis of MEA cell at 15° angle
**System**: 0.5NiSAC (850 °C, 4 h, 10 °C·min⁻¹) | AEM 40 µm | IrO₂–TiPt — 100 cm²; Single-Serp (0°) or Parallel (15°)
**Conditions**: 50 mM CH₃COOH humidified CO₂ — 200 mL·min⁻¹ (0°) or 400 mL·min⁻¹ (15°) — 100 mL·min⁻¹ 0.1 M KHCO₃ — 100 mA·cm⁻²

### Top-left panel — FE(CO) + SPU vs time (0° vs 15°)
| Series | Colour | Angle | Durability (stable FE(CO)) | FE(CO) | SPU |
|---|---|---|---|---|---|
| 0° (vertical) | blue | 0° | **~20 h** (rapid failure) | ~100 % early | ~60 % [estimated] |
| 15° (tilted) | orange | 15° | **~590 h** | ~95–100 % sustained, slight droop at end | ~18–20 % [estimated] |

- **Headline (Heng's framing)**: tilting the MEA from 0° → 15° extends durability **~20 h → ~590 h**.
  Attributed to gravity-assisted water drainage mitigating water accumulation in the GDE — a
  main cause of rapid cell failure in the vertical configuration.
- **Incidental interruptions the 15° cell survived** (FE held / recovered after each): CO₂ tank replacement ~150 h; electricity shutdown ~280 h; CO₂ tank replacement ~518 h.

### Right panel — Voltage & Pressure profiles
| | Value |
|---|---|
| Cell voltage | ~3.0–3.2 V stable through most of the run; rises toward ~4 V near 590 h |
| CA-outlet pressure | low/steady; barely changed across the run |
| Segment labels | 6 h / 150 h / 288 h / 518 h / 590 h |

### Bottom-left panel — Voltage & Temperature profiles
| | Value |
|---|---|
| Cell / pre-heater / bottle temperatures | ~25–32 °C, essentially unchanged across run |
| Cell voltage | tracks the right panel — stable then rises at ~590 h |

### Bottom-right panel — Voltage & Outlet-gas profiles
| | Value |
|---|---|
| Concentration gas (SLPM) | steady baseline; rises sharply near 590 h |
| Cell voltage | stable then elevated at ~590 h |

**Figure-stated summary notes**: "Pressure and Temperature profiles are barely changed."
"Voltage and CA-Outlet profiles are substantially elevated due to an increase in parasitic
HER activity @590 h ⇒ GDE Flooding."

**Mechanism / result**: tilting from 0° → 15° extends stable ~95–100 % FE(CO) operation from
~20 h to ~590 h at 100 mA·cm⁻² — the longest 100 cm² run to date — with flat pressure,
temperature, and cell voltage, and surviving three incidental interruptions. The improvement
is attributed to gravity-assisted water drainage that mitigates GDE water accumulation.
Failure onset at ~590 h (coupled rise in cell voltage + CA-outlet signal + parasitic HER) is
**water-driven GDE flooding**; the post-mortem (Fig 2) shows no salt in the flow-field channels,
ruling out salt precipitation as the failure cause.

---

## Figure 2 — Post-mortem of the 100 cm² MEA after 600 h operation
### ⟵ LINKED WITH FIGURE 1 (same 15° / 40 µm / 0.5NiSAC run)

**Title (figure)**: 100 cm² MEA disassembly after 600 h of CO₂ electrolysis
**Photos**: top row — cathode flow-field plate, 0.5NiSAC GDE (front/back), AEM membrane, cathode housing; bottom row — anode flow-field plate and housing at several views.

| Component | Observation |
|---|---|
| Flow-field channels | **no precipitated salt** (key finding — rules out salt as failure cause) |
| 0.5NiSAC GDE (cathode) | largely intact |
| AEM membrane (40 µm) | largely intact; no obvious physical breach |

**Interpretation (per Heng)**: after ~600 h, **no precipitated salt is present in the
flow-field channels**, and the GDE and 40 µm membrane remain largely intact. The absence of
carbonate/bicarbonate salt precipitation confirms that salt formation was NOT the primary
cause of cell failure, consistent with the voltage/CA-outlet behaviour in Fig 1 and supporting
water-driven GDE flooding as the limiting mechanism. (Report keeps the Fig 2 statement simple:
no salt in the channels — do not over-describe anode staining.)

---

## Figure 3 — Revisiting 5 cm²: FE(CO)–SPU correlation & stability vs applied current density

**Title (figure)**: CO₂ electrolysis of 0.5NiSAC in AEM electrolyzer at different applied current densities
**System**: 0.5NiSAC (850 °C, 4 h, 10 °C·min⁻¹) | IrO₂-TiPt — **5 cm²** MEA
**Membrane**: **SustAEM (Sustainion)** for the 1 h screening (top); **PiperION 40 µm** for both long-term panels — membrane differs between screening and stability tests (confirm intentional).
**Conditions**: 0.5 M CH₃COOH humidified CO₂ at 20 mL·min⁻¹; 4 mL·min⁻¹ of 0.1 M KHCO₃.

### Top panel — 1 h screening (values read directly from the figure table)
| j (mA·cm⁻²) | FE(CO) % | FE(H₂) % | SPU % | Potential (V) |
|---|---|---|---|---|
| 100 | 98.35 | 1.23 | 19.02 | 2.94 |
| 200 | 98.15 | 1.74 | 37.96 | 3.19 |
| 250 | 95.46 | 4.93 | 46.14 | 3.28 |
| 300 | 86.94 | 13.50 | 48.75 | 3.40 |

- FE(CO) > 95 % from 100–250 mA·cm⁻²; max SPU 46.14 % at 250. At 300, FE(CO) falls to 86.94 % while SPU rises only to 48.75 % and FE(H₂) jumps to 13.50 % → mass-transport-limited / CO₂-depleted regime.

### Middle panel — long-term at 300 mA·cm⁻² (0.5 M CH₃COOH, PiperION 40 µm)
- FE(CO) declines rapidly: figure points ~83 % → ~70 % over ~7 h [estimated]; Heng states ~85 % → ~65 %. Competing HER dominant. SPU ~44 → ~40.

### Bottom panel — long-term at 250 mA·cm⁻² (0.5 M vs 1.0 M CH₃COOH, PiperION 40 µm)
- FE(CO) > 90 % sustained ~12 h (both 0.5 M and 1.0 M humidifier), then cell voltage climbs and FE(CO)/SPU collapse by ~21 h. Photos show (bi)carbonate salt on the flow-field channels. Raising humidifier to 1.0 M CH₃COOH did **not** prevent salt-induced failure.

**Mechanism / result**: operating in the high-SPU, CO₂-depleted zone accelerates cell failure via **both** massive (bi)carbonate salt precipitation **and** consequent GDE flooding. Future work: raise acetic-acid concentration / use a stronger-acid humidifier and increase CO₂ flow rate to relieve depletion.

---

## Figure 4 — Optimisation of 0.5NiSAC synthesis: pyrolysis temperature & hold time

**Title (figure)**: Effect of pyrolysis temperature and time on CO₂-to-CO selectivity and durability
**Panels**: FE(CO) + cell voltage vs time; (top) 2 h series, (bottom) 4 h series; ramp rate fixed 10 °C·min⁻¹.

### BET (values read directly from figure tables)
| Condition (°C/h/°C·min⁻¹) | Surface Area (m²·g⁻¹) | Pore Volume (cm³·g⁻¹) |
|---|---|---|
| 800/2/10 | 135.70 | 0.34 |
| 850/2/10 | 171.50 | 0.41 |
| 900/2/10 | 181.92 | 0.52 |
| 800/4/10 | 112.69 | 0.36 |
| 850/4/10 | 178.11 | 0.53 |
| 900/4/10 | 210.36 | 0.61 |

- **Temperature** directly raises both SA and PV (800 < 850 < 900). **Hold time** (2→4 h) has only a modest/non-monotonic effect on SA but substantially raises PV (e.g. 850: 0.41 → 0.53).
- **CO₂RR**: **850C-4h-10** gives the highest FE(CO) and longest lifetime (bottom panel, ~33 h) → optimal condition.

## Figure 5 — Optimisation of 0.5NiSAC synthesis: pyrolysis ramp rate

**Title (figure)**: Effect of pyrolysis ramp rate at each temperature on CO₂-to-CO selectivity and durability
**Panels**: (top) 800 °C/4 h — 5 vs 10 °C·min⁻¹; (middle) 850 °C/2 h — 10 vs 20 °C·min⁻¹; (bottom) 900 °C/4 h — 5 vs 10 °C·min⁻¹.

### BET (values read directly from figure tables)
| Condition (°C/h/°C·min⁻¹) | Surface Area (m²·g⁻¹) | Pore Volume (cm³·g⁻¹) |
|---|---|---|
| 800/4/5 | – (not measured) | – |
| 800/4/10 | 112.686 | 0.36 |
| 850/2/10 | 171.502 | 0.41 |
| 850/2/20 | 220.898 | 0.43 |
| 900/4/5 | 216.874 | 0.79 |
| 900/4/10 | 210.36 | 0.61 |

- **No consistent ramp-rate trend**: 850 (10→20) SA up (171.5→220.9), PV ~flat; 900 (5→10) SA & PV both down (216.9→210.4; 0.79→0.61).
- **CO₂RR**: performance is **random / no systematic trend** with ramp rate.
- **Future work (Heng)**: extend ramp-rate range (5, 10, 20 °C·min⁻¹) to resolve the effect more clearly.

---

## Values to confirm with Heng (TBD / resolved)
- [x] Tilt angle **15°** — confirmed by Heng.
- [x] NiSAC synthesis **850 °C / 4 h / 10 °C·min⁻¹** — confirmed by Heng.
- [x] Cathode loading **1.8 ± 0.1 mg·cm⁻²** on **Sigracet 39BB** — confirmed by Heng.
- [x] MEA-assembly extras (anolyte volume, humidifier/cell temperature) — Heng: no need to specify.
- [x] Failure mechanism — **water-driven GDE flooding**; salt precipitation ruled out by post-mortem (no salt in channels).
- [x] Durability — **0° ~20 h → 15° ~590 h** (confirmed by Heng).
- [ ] Fig 1: exact end-of-run FE(CO) and the timestamp/FE at the ~590 h HER onset (GC CSV) — still `[estimated]`.
- [ ] Fig 1: exact SPU value ~18–20 % (15°) (GC CSV) — still `[estimated]`.
