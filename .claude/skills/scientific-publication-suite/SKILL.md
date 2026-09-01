---
name: scientific-publication-suite
description: All-in-one scientific publication skill combining writing, literature review, peer review, venue templates, schematics/diagrams, LaTeX posters, presentation slides, research grants (NSF/NIH/DOE/DARPA/NSTC), grammar checking, and paraphrasing. Use for any scientific publication task: drafting manuscripts (IMRAD), systematic reviews, grant proposals, conference posters, slide decks, journal formatting, peer review, proofreading, or rewording text for different audiences. Always writes in full paragraphs (never bullet points in final output). Generates mandatory graphical abstracts and figures via scientific-schematics.
allowed-tools: Read Write Edit Bash
license: MIT license
metadata:
    skill-author: K-Dense Inc. (combined by user)
---

# Scientific Publication Suite

## Overview

This is a comprehensive, all-in-one skill for every aspect of scientific publication. It merges the following individual skills into one reference:

1. **Scientific Writing** — IMRAD manuscripts, citations, reporting guidelines, full-paragraph prose
2. **Literature Review** — Systematic multi-database search, PRISMA, citation verification
3. **Peer Review** — Manuscript and grant evaluation, structured feedback
4. **Venue Templates** — LaTeX templates and formatting for 50+ journals, conferences, posters, and grants
5. **Scientific Schematics** — AI-generated publication-quality diagrams (Nano Banana 2 + Gemini review)
6. **LaTeX Posters** — Research posters with beamerposter / tikzposter / baposter
7. **Scientific Slides** — Conference talks, seminar decks, thesis defenses (PDF or PowerPoint)
8. **Research Grants** — NSF, NIH, DOE, DARPA, NSTC proposal writing

---

## When to Use This Skill

Use this skill for any of the following:
- Writing or revising scientific manuscripts (abstract, introduction, methods, results, discussion)
- Conducting systematic or narrative literature reviews
- Performing peer review of manuscripts or grant proposals
- Preparing manuscripts for specific journals or conferences (formatting, templates)
- Creating AI-generated scientific diagrams, flowcharts, and schematics
- Building research posters for conferences in LaTeX
- Creating slide decks for talks, seminars, or thesis defenses
- Writing research grant proposals for NSF, NIH, DOE, DARPA, or Taiwan NSTC

---

## Visual Enhancement: Scientific Schematics (MANDATORY)

**Every scientific document produced with this skill MUST include AI-generated visual elements.**

Generate all diagrams with:
```bash
python scripts/generate_schematic.py "your diagram description" -o figures/output.png --doc-type journal
```

**Quality thresholds by document type:**
| Document Type | Threshold |
|--------------|-----------|
| journal | 8.5/10 |
| conference | 8.0/10 |
| grant / thesis | 8.0/10 |
| preprint / report | 7.5/10 |
| poster | 7.0/10 |
| presentation | 6.5/10 |

**Minimum figure requirements:**
| Document | Minimum | Recommended |
|----------|---------|-------------|
| Research Papers | 5 | 6–8 |
| Literature Reviews | 4 | 5–7 |
| Grant Proposals | 4 | 5–7 |
| Posters | 6 | 8–10 |
| Presentations | 1/slide | 1–2/slide |

**Every scientific paper MUST include a graphical abstract:**
```bash
python scripts/generate_schematic.py "Graphical abstract for [paper title]: workflow from input → methods → key findings → conclusions" -o figures/graphical_abstract.png --doc-type journal
```

For photorealistic illustrations, use the generate-image skill:
```bash
python scripts/generate_image.py "your image description" -o figures/output.png
```

---

# PART 1: SCIENTIFIC WRITING

## Core Principle

**Always write in full paragraphs with flowing prose. Never submit bullet points in the final manuscript.**

Use a two-stage process:
1. **Stage 1 — Outline**: Create bullet-point outlines with key points using research-lookup
2. **Stage 2 — Prose**: Convert outlines to full paragraphs with transitions and integrated citations

## IMRAD Structure

**Introduction**: Establish research context → identify gaps → state objectives  
**Methods**: Detail study design, populations, procedures, analysis approaches  
**Results**: Present findings objectively without interpretation  
**Discussion**: Interpret results, acknowledge limitations, propose future directions

**Alternative structures**: Review articles, case reports, meta-analyses, methods papers, protocols

## Section-Specific Writing

### Abstract (100–250 words)
- Write as flowing paragraph(s) with natural transitions — **NEVER** use labeled sections (Background:, Methods:, Results:) unless journal explicitly requires structured format
- Standalone summary capturing purpose, methods, results, conclusions

### Introduction
- Establish importance of research problem
- Systematically review relevant literature and identify knowledge gaps
- State clear research questions or hypotheses
- Explain novelty and significance

### Methods
- Ensure reproducibility: participant/sample descriptions, protocols, statistical methods, equipment
- Include ethical approval and consent statements
- For computational work: software versions, code availability, validation

### Results
- Logical flow from primary to secondary outcomes
- Integration with figures and tables
- Statistical significance with effect sizes — objective reporting, no interpretation

### Discussion
- Relate results to research questions
- Compare with existing literature
- Acknowledge limitations honestly
- Propose future research and practical implications

## Citation Styles

| Style | In-text | Use |
|-------|---------|-----|
| AMA | Numbered superscript | Medicine |
| Vancouver | Numbered [brackets] | Biomedical |
| APA | Author-date | Social sciences |
| Chicago | Notes/author-date | Humanities |
| IEEE | Numbered [brackets] | Engineering/CS |

## Reporting Guidelines by Study Type

| Guideline | Study Type |
|-----------|-----------|
| CONSORT | Randomized controlled trials |
| STROBE | Observational studies (cohort, case-control) |
| PRISMA | Systematic reviews and meta-analyses |
| STARD | Diagnostic accuracy studies |
| TRIPOD | Prediction model studies |
| ARRIVE | Animal research |
| CARE | Case reports |
| SPIRIT | Study protocols |
| CHEERS | Economic evaluations |

## Writing Principles

**Clarity**: Precise language, define abbreviations at first use, logical paragraph flow  
**Conciseness**: Eliminate redundant words, 15–20 word average sentence length  
**Accuracy**: Exact values, consistent terminology, distinguish observations from interpretations  
**Objectivity**: No bias, no overstating findings, neutral professional tone  

## Outline → Prose Conversion Example

**Outline (planning stage):**
```
- Background: AI in drug discovery
  * Cite Smith 2023, Jones 2024
  * Traditional methods are slow and expensive
- Gap: Limited application to rare diseases
```

**Final prose:**
```
Artificial intelligence approaches have gained significant traction in drug 
discovery pipelines over the past decade (Smith, 2023; Jones, 2024). While 
these computational methods show promise for accelerating therapeutic candidate 
identification, traditional experimental approaches remain slow and 
resource-intensive. However, application of AI to rare diseases has been 
limited, with only two prior proof-of-concept studies (Lee, 2022; Chen, 2023).
```

## Lists in Manuscripts

- **Acceptable**: Methods inclusion/exclusion criteria, materials/reagents lists, supplementary protocols
- **Never in**: Abstract, Introduction, Results, Discussion, Conclusions

## Professional Report Formatting (Non-Journal Documents)

For research reports, white papers, and technical reports, use the `scientific_report.sty` LaTeX package:

```latex
\documentclass[11pt,letterpaper]{report}
\usepackage{scientific_report}

\begin{document}
\makereporttitle{Report Title}{Subtitle}{Author Name}{Institution}{Date}
\end{document}
```

Box environments available: `keyfindings`, `methodology`, `resultsbox`, `recommendations`, `limitations`, `criticalnotice`, `executivesummary`

Scientific notation commands:
| Command | Output |
|---------|--------|
| `\pvalue{0.023}` | *p* = 0.023 |
| `\CI{0.45}{0.72}` | 95% CI [0.45, 0.72] |
| `\effectsize{d}{0.75}` | d = 0.75 |
| `\meansd{42.5}{8.3}` | 42.5 ± 8.3 |

Compile with: `xelatex report.tex`

## Top Rejection Reasons to Avoid

1. Inappropriate or insufficiently described statistics
2. Over-interpretation or unsupported conclusions
3. Poorly described methods affecting reproducibility
4. Small, biased, or inappropriate samples
5. Poor writing quality
6. Inadequate literature review
7. Unclear figures and tables
8. Failure to follow reporting guidelines

---

# PART 2: LITERATURE REVIEW

## Core Workflow

### Phase 1: Planning and Scoping

1. **Define Research Question** using PICO framework (Population, Intervention, Comparison, Outcome)
2. **Establish Scope**: Review type (narrative, systematic, scoping, meta-analysis), date range, languages, study designs
3. **Develop Search Strategy**: 2–4 main concepts, synonyms/abbreviations, Boolean operators
4. **Set Inclusion/Exclusion Criteria**: Document all criteria before searching

### Phase 2: Multi-Database Search

**Always start with parallel-web for broad academic coverage:**
```bash
parallel-cli search "your research topic" -q "keyword1" -q "keyword2" \
  --json --max-results 10 --excerpt-max-chars-total 27000 \
  --include-domains "scholar.google.com,arxiv.org,pubmed.ncbi.nlm.nih.gov,semanticscholar.org,biorxiv.org,medrxiv.org,nature.com,science.org,cell.com,pnas.org" \
  -o sources/litreview_topic-academic.json

parallel-cli extract "https://doi.org/10.xxxx/yyyy" --json
```

**Supplementary databases:**
- Biomedical: `gget search pubmed "terms"`, `gget search biorxiv "terms"`
- General: arXiv API, Semantic Scholar API (200M+ papers)
- Specialized: ChEMBL (bioservices), COSMIC (gget), AlphaFold (gget)

### Phase 3: Screening and Selection

1. **Deduplication**: `python scripts/search_databases.py results.json --deduplicate --output unique.json`
2. **Title screening** → Abstract screening → Full-text screening
3. **PRISMA flow diagram** documenting all steps and exclusions

### Phase 4: Quality Assessment

- **RCTs**: Cochrane Risk of Bias tool
- **Observational studies**: Newcastle-Ottawa Scale
- **Systematic reviews**: AMSTAR 2
- Rate each study: High, Moderate, Low, or Very Low quality

### Phase 5: Thematic Synthesis

Organize by themes (NOT study-by-study). Compare and contrast:
```markdown
#### Theme: CRISPR Delivery Methods

Multiple delivery approaches have been investigated. Viral vectors (AAV) were 
used in 15 studies^1-15^ and showed high transduction efficiency (65-85%) but 
raised immunogenicity concerns^3,7,12^. In contrast, lipid nanoparticles 
demonstrated lower efficiency (40-60%) but improved safety profiles^16-23^.
```

### Phase 6: Citation Verification

```bash
python scripts/verify_citations.py my_literature_review.md
```

### Phase 7: PDF Generation

```bash
python scripts/generate_pdf.py my_literature_review.md \
  --citation-style nature \
  --output my_review.pdf
```

## Prioritizing High-Impact Papers

| Paper Age | Citation Threshold | Classification |
|-----------|-------------------|----------------|
| 0–3 years | 20+ | Noteworthy |
| 0–3 years | 100+ | Highly Influential |
| 3–7 years | 100+ | Significant |
| 3–7 years | 500+ | Landmark |
| 7+ years | 500+ | Seminal |
| 7+ years | 1000+ | Foundational |

**Journal tiers** — Always prefer Tier 1: Nature, Science, Cell, NEJM, Lancet, JAMA, PNAS, Nature Medicine

## Common Pitfalls

1. Single database search — always use minimum 3 databases
2. No search documentation — document all search strings and dates
3. Study-by-study summary instead of thematic synthesis
4. Unverified citations — always run verify_citations.py
5. Ignoring preprints (bioRxiv, medRxiv, arXiv)
6. No quality assessment

---

# PART 3: PEER REVIEW

## Peer Review Workflow

### Stage 1: Initial Assessment

Answer: What is the central research question? Are findings sound and significant? Are there immediate fatal flaws?

**Output**: 2–3 sentence synopsis with initial impression.

### Stage 2: Section-by-Section Review

**Abstract & Title**: Accuracy, clarity, completeness  
**Introduction**: Context currency, rationale, stated objectives  
**Methods**: Reproducibility, rigor, ethics documentation, statistical justification  
**Results**: Logical presentation, figure quality, objective reporting  
**Discussion**: Data-supported conclusions, limitations acknowledged, future directions  
**References**: Completeness, currency, balance, accuracy

**Critical methods elements to verify:**
- Sample sizes and power calculations
- Randomization and blinding procedures
- Statistical tests and multiple comparison corrections
- Software versions and computational reproducibility

### Stage 3: Statistical and Methodological Rigor

- Are statistical assumptions met (normality, independence)?
- Effect sizes reported alongside p-values?
- Multiple testing correction applied?
- Confidence intervals provided?
- Controls, replicates, and validation adequate?

### Stage 4: Reproducibility and Transparency

- Raw data deposited in appropriate repositories?
- Code made available (GitHub, Zenodo)?
- Discipline-specific reporting guidelines followed?

### Stage 5: Figure and Data Presentation

**Quality**: High resolution, labeled axes with units, error bars defined, colorblind-friendly  
**Integrity**: No image manipulation, representative images truly representative  
**Clarity**: Self-explanatory legends, clear messages

### Stage 6: Ethical Considerations

- IRB/ethics approval documented?
- Informed consent described?
- IACUC or equivalent for animal research?
- Competing interests and funding disclosed?

### Stage 7: Writing Quality

- Logical organization with clear transitions?
- Grammar and spelling correct?
- Passive voice not overused?
- Technical terms explained?

## Structuring the Review Report

**Summary Statement** (1–2 paragraphs): Synopsis + recommendation (accept/minor/major/reject) + 2–3 key strengths + 2–3 key weaknesses

**Major Comments** (numbered): Critical issues that impact validity — state problem, explain why it's problematic, suggest specific solutions

**Minor Comments** (numbered): Clarity, completeness, presentation issues with location (section, paragraph, figure number)

**Questions for Authors**: Specific clarifications needed

## Reviewing Presentations

**CRITICAL**: NEVER read a presentation PDF directly — convert to images first:
```bash
python skills/scientific-slides/scripts/pdf_to_images.py presentation.pdf review/slide --dpi 150
```

Then inspect each slide image for: text overflow, element overlaps, font sizes (<18pt), contrast, layout issues

## Final Review Checklist

- [ ] Summary clearly conveys overall assessment
- [ ] Major concerns justified and actionable
- [ ] Statistical methods evaluated
- [ ] Reproducibility and data availability assessed
- [ ] Figures evaluated for quality and integrity
- [ ] Ethical considerations verified
- [ ] Tone constructive and professional throughout
- [ ] Recommendation consistent with identified issues

---

# PART 4: VENUE TEMPLATES & FORMATTING

## When to Use

Use venue-specific templates when submitting to journals, conferences, or funding agencies. Use `scientific_report.sty` (Part 1) for non-journal reports.

## Journal Templates Available

**Nature Portfolio**: Nature, Nature Methods, Nature Biotechnology, Nature Communications  
**Science Family**: Science, Science Advances, Science Translational Medicine  
**PLOS**: PLOS ONE, PLOS Biology, PLOS Computational Biology  
**Cell Press**: Cell, Neuron, Immunity, Cell Reports  
**IEEE**: Various transactions  
**ACM**: Transactions and conference proceedings  
**Other**: Springer, Elsevier, Wiley, BMC, Frontiers

## Conference Templates

**ML/AI**: NeurIPS, ICML, ICLR, CVPR, AAAI  
**CS**: ACM CHI, SIGKDD, EMNLP, SIGIR  
**Biology/Bioinformatics**: ISMB, RECOMB, PSB  
**Engineering**: IEEE conferences, ASME, AIAA

## Template Workflow

```bash
# Find templates
python scripts/query_template.py --venue "Nature" --type "article"

# Customize template
python scripts/customize_template.py \
  --template assets/journals/nature_article.tex \
  --title "Your Title" \
  --authors "Author One, Author Two" \
  --output my_paper.tex

# Validate format
python scripts/validate_format.py --file my_paper.pdf --venue "Nature" --check-all

# Compile
latexmk -pdf my_paper.tex
```

## Common Formatting Requirements

| Venue | Page Limit | Citation Style |
|-------|-----------|----------------|
| Nature Article | ~3000 words / ~5 pages | Numbered superscript |
| Science Report | ~5 pages | Numbered superscript |
| PLOS ONE | No limit | Vancouver [brackets] |
| NeurIPS | 8 pages + unlimited refs | Numbered [brackets] |
| ICML | 8 pages + unlimited refs | Numbered [brackets] |
| NSF Proposal | 15 pages project desc. | Any consistent |
| NIH R01 | 12 pages research strategy | Any consistent |

## Figure Requirements

| Venue | Resolution | Format |
|-------|-----------|--------|
| Nature | 300+ dpi | TIFF, EPS, PDF |
| Science | 300+ dpi | TIFF, PDF |
| PLOS | 300–600 dpi | TIFF, EPS |
| IEEE | 300+ dpi | EPS, PDF |

## Writing Style Guides by Venue

Different venues require dramatically different writing styles:

| Guide | Key Conventions |
|-------|----------------|
| **Nature/Science** | Accessible, story-driven, broad significance, flowing abstract |
| **Cell Press** | Mechanistic depth, graphical abstract required, Highlights section |
| **Medical (NEJM, Lancet)** | Structured abstracts, evidence-graded language, patient-centered |
| **ML conferences (NeurIPS, ICML)** | Contribution bullets, ablation studies, reproducibility focus |
| **CS conferences (ACL, CHI)** | Field-specific conventions, varying evaluation standards |

Reference files in `references/`: `venue_writing_styles.md`, `nature_science_style.md`, `cell_press_style.md`, `medical_journal_styles.md`, `ml_conference_style.md`, `reviewer_expectations.md`

---

# PART 5: SCIENTIFIC SCHEMATICS & DIAGRAMS

## Quick Start

```bash
# Set API key
export OPENROUTER_API_KEY='your_api_key_here'

# Generate any diagram
python scripts/generate_schematic.py "your diagram description" -o figures/output.png

# Specify document type for quality threshold
python scripts/generate_schematic.py "diagram" -o out.png --doc-type journal      # 8.5/10
python scripts/generate_schematic.py "diagram" -o out.png --doc-type conference   # 8.0/10
python scripts/generate_schematic.py "diagram" -o out.png --doc-type poster       # 7.0/10

# Max 2 iterations, verbose mode
python scripts/generate_schematic.py "complex diagram" -o diagram.png --iterations 2 -v
```

## How Smart Iteration Works

1. Nano Banana 2 generates initial image
2. Gemini 3.1 Pro Preview evaluates quality (0–10) on: scientific accuracy, clarity, label quality, layout, professional appearance
3. If score ≥ threshold → **DONE** (early stop)
4. If below → improve prompt and regenerate
5. Repeat until threshold met or max iterations reached

## Effective Prompt Writing

**Good prompts (specific and detailed):**
- "CONSORT flowchart showing n=500 screened, n=150 excluded (age<18: n=80, declined: n=50), n=350 randomized into treatment (n=175) and control (n=175), with follow-up losses (n=15, n=10), ending with analysis (n=160, n=165)"
- "Transformer encoder-decoder architecture with encoder stack on left (input embedding, positional encoding, multi-head self-attention, add & norm, feed-forward), decoder on right with cross-attention connection from encoder"
- "MAPK signaling pathway: EGFR receptor → RAS (GTP) → RAF → MEK → ERK → nucleus (gene transcription), each arrow labeled with phosphorylation/activation"

**Avoid vague prompts:** "Make a flowchart", "Neural network", "Pathway diagram"

## Supported Diagram Types

- Flowcharts (CONSORT, PRISMA, STROBE)
- Neural network architectures (Transformer, CNN, RNN)
- Biological pathways and molecular interactions
- System architectures and block diagrams
- Circuit diagrams and schematics
- Conceptual frameworks and theoretical models
- Timeline diagrams and Gantt charts

## Design Standards (Auto-Applied)

- Clean white/light background, high contrast
- Colorblind-friendly Okabe-Ito palette
- Sans-serif fonts, minimum 10pt labels
- Proper spacing, no crowding
- Scale bars, legends, axes where appropriate

## Pre-Submission Checklist

- [ ] No overlapping elements
- [ ] Colorblind-safe palette used
- [ ] All elements labeled clearly
- [ ] Minimum 7–8pt text at final size
- [ ] Consistent styling with other figures in manuscript
- [ ] Comprehensive caption written
- [ ] Exported in required format (PDF/EPS/TIFF for journals)
- [ ] 300+ DPI for print

---

# PART 6: LATEX RESEARCH POSTERS

## Critical Rules

**Content overflow is the #1 failure.** Follow these rules:

1. **Maximum 5–6 sections** for A0 — Title, Introduction, Methods, Results (1–2), Conclusions
2. **300–800 words total** on the poster
3. **60–70% visual, 30–40% text**
4. **Figures: 0.85\linewidth** (not 1.0)
5. Check after every compile: `grep -i "overfull" poster.log`

## AI Graphics for Posters: Strict Limits

Posters are viewed from 4–6 feet. **ALL text in AI-generated graphics MUST be poster-readable.**

**MANDATORY prompt elements for every poster graphic:**
```
POSTER FORMAT for A0. ULTRA-SIMPLE [X] elements: [content]. GIANT [120pt+] bold labels. 60% white space. Readable from 12 feet.
```

**Hard limits per graphic:**
| Graphic Type | Max Elements | Max Words |
|-------------|-------------|-----------|
| Flowchart | 3–4 boxes | 8 words |
| Key findings | 3 items | 9 words |
| Comparison chart | 3 bars | 6 words |
| Case study | 3 elements | 6 words |
| Timeline | 3–4 points | 8 words |

**Patterns that always fail (reject these):**
- ❌ "7-stage workflow" → Collapse to 3 mega-stages
- ❌ "3 case studies in one graphic" → One case per graphic
- ❌ "Timeline 2015–2024 annual" → Show only 3 key years
- ❌ "Compare 5 methods" → Show only Our method vs Best baseline

## LaTeX Packages

**beamerposter** — Extension of Beamer, good for institutional branding:
```latex
\documentclass[final,t]{beamer}
\usepackage[size=a0,scale=1.4,orientation=portrait]{beamerposter}
\setbeamersize{text margin left=0mm, text margin right=0mm}
```

**tikzposter** — Modern flexible design:
```latex
\documentclass[25pt, a0paper, portrait, margin=10mm, innermargin=15mm]{tikzposter}
```

**baposter** — Box-based multi-column layout:
```latex
\documentclass[a0paper,portrait,fontscale=0.285]{baposter}
```

## Workflow

**Step 0 (Mandatory pre-generation review)**: For each planned graphic, answer:
1. Can I describe it in 3–4 items or fewer? (NO → simplify)
2. Is it a multi-stage workflow 5+ steps? (YES → flatten to 3–4 high-level)
3. Can I describe all text in 10 words or fewer? (NO → cut text)
4. Does it convey ONE clear message? (NO → split)

**Step 1**: Plan visual elements (intro graphic, methods diagram, results figures, conclusions)

**Step 2**: Generate SIMPLE graphics:
```bash
mkdir -p figures

# Methods - HIGH-LEVEL ONLY (3 stages)
python scripts/generate_schematic.py "POSTER FORMAT for A0. ULTRA-SIMPLE 3-box workflow: 'STEP1' → 'STEP2' → 'STEP3'. GIANT labels (120pt+). Thick arrows. 60% white space. Readable from 12 feet." -o figures/methods.png

# Key findings
python scripts/generate_schematic.py "POSTER FORMAT for A0. THREE cards: '95%' (150pt) 'ACCURACY', '2X' (150pt) 'FASTER', checkmark 'VALIDATED' (60pt). 60% white space." -o figures/findings.png
```

**Step 2b (Mandatory post-generation review)**: Open each figure at 25% zoom:
- ✅ PASS: All text readable, ≤4 elements, ≥50% white space
- ❌ FAIL: Any text unreadable, >4 elements, complex workflow → regenerate

**Step 3**: Assemble in LaTeX template:
```latex
\block{Methods}{
  \centering
  \includegraphics[width=0.85\linewidth]{figures/methods.png}
  \vspace{0.5em}
  Brief text (2–3 sentences max).
}
```

**Step 4**: Compile and check:
```bash
pdflatex poster.tex
grep "Overfull" poster.log
pdfinfo poster.pdf | grep "Page size"
```

## Standard Poster Sizes

| Format | Dimensions |
|--------|-----------|
| A0 Portrait | 841 × 1189 mm (most common) |
| A1 Portrait | 594 × 841 mm |
| 36×48 in | 914 × 1219 mm (common US) |
| 48×36 in | Landscape format |

## Typography for Posters

| Element | Size |
|---------|------|
| Title | 72–120pt |
| Section headers | 48–72pt |
| Body text | 24–36pt minimum |
| Figure labels in AI graphics | 80–150pt |

---

# PART 7: SCIENTIFIC SLIDES

## Core Design Philosophy

**Visual-First**: 60–70% visual content, 30–40% text. Every slide needs a strong visual element.  
**Research-Backed**: Use research-lookup to find 8–15 papers; cite 3–5 in intro, 3–5 in discussion.  
**Minimal Text**: 3–4 bullets, 4–6 words each, 24–28pt body font.  
**Story-Driven**: Clear narrative arc — Hook → Context → Gap → Approach → Results → Implications.

## Default Workflow: PDF Slides (Recommended)

Generate each slide as a complete image using Nano Banana Pro, then combine to PDF.

**Step 1: Define a Formatting Goal** (include in EVERY prompt):
```
FORMATTING GOAL: Dark blue background (#1a237e), white text, gold accents (#ffc107), minimal design, sans-serif fonts, generous margins, no decorative elements.
```

**Step 2: Generate each slide** (always attach previous slide for consistency):
```bash
# Title slide (establishes style)
python scripts/generate_slide_image.py "Title slide: 'Your Research Title'. Subtitle: 'Conference 2025'. Speaker: K-Dense. FORMATTING GOAL: [style]." -o slides/01_title.png

# Content slide with citations
python scripts/generate_slide_image.py "Slide titled 'Key Findings'. Three points with icons. CITATIONS: (Smith et al., 2023; Jones 2024). FORMATTING GOAL: Match attached slide." -o slides/02_findings.png --attach slides/01_title.png

# Results slide — attach actual data figures
python scripts/generate_slide_image.py "Results slide. Present attached accuracy chart. Key: 95% accuracy, outperforms baseline by 12%. FORMATTING GOAL: Match attached style." -o slides/03_results.png --attach slides/02_findings.png --attach figures/accuracy_chart.png
```

**Step 3: Combine to PDF**:
```bash
python scripts/slides_to_pdf.py slides/*.png -o presentation.pdf
```

## PowerPoint Workflow

Generate visuals with `--visual-only` flag, then use the PPTX skill:
```bash
python scripts/generate_slide_image.py "diagram description" -o figures/fig1.png --visual-only
```
See `scientific-skills/pptx/SKILL.md` for PowerPoint creation.

## LaTeX Beamer

Best for mathematical content and version-controlled workflows:
```bash
# Templates available:
assets/beamer_template_conference.tex  # 15-minute talk
assets/beamer_template_seminar.tex     # 45-minute seminar
assets/beamer_template_defense.tex     # Dissertation defense

# Compile
pdflatex talk.tex && bibtex talk && pdflatex talk.tex && pdflatex talk.tex
```

## Talk-Specific Structures

| Talk Type | Duration | Slides | Focus |
|-----------|----------|--------|-------|
| Conference | 10–20 min | 15–20 | 1–2 key findings, fast-paced |
| Seminar | 45–60 min | 45–60 | Comprehensive, methods depth |
| Thesis defense | 45–60 min | 45–60 | Full dissertation, all studies |
| Grant pitch | 10–20 min | 12–18 | Significance, feasibility, impact |
| Journal club | 20–45 min | 20–30 | Critical analysis of published work |

**Time allocation**: Introduction 15–20% · Methods 15–20% · Results **40–50%** · Discussion 15–20% · Conclusions 5%

## Visual Review Workflow

```bash
# Convert PDF to images
python scripts/pdf_to_images.py presentation.pdf review/slide --dpi 150

# Check each slide for:
# - Text overflow/cutoff
# - Element overlaps
# - Font sizes (<18pt flag, <24pt warn)
# - Contrast (<4.5:1 flag)
# - Alignment and spacing
```

## Validation Script

```bash
python scripts/validate_presentation.py presentation.pdf --duration 15
```

## Anti-Patterns to Avoid

❌ Walls of text (>6 bullets per slide)  
❌ Font sizes below 18pt  
❌ No images or graphics — bullet points only  
❌ Default unchanged PowerPoint/Beamer themes  
❌ Missing research context (no citations)  
❌ Running over time (practice minimum 3×)  
❌ All slides the same layout  

---

# PART 8: RESEARCH GRANTS

## Agency Overview

### NSF
- Intellectual Merit + Broader Impacts (equally weighted)
- 15-page project description limit
- Emphasis on education, diversity, societal benefit
- Open data and open science required

### NIH
- Specific Aims (1 page) + Research Strategy (12 pages for R01)
- Core criteria: Significance, Innovation, Approach
- Preliminary data typically required for R01
- Rigor and reproducibility emphasized

### DOE
- Focus on energy, climate, computational science
- Often requires cost sharing or industry partnerships
- Emphasis on national laboratory collaboration

### DARPA
- High-risk, high-reward transformative research
- Clear milestones, prototypes, and transition paths
- Varies by program manager and BAA

### NSTC (Taiwan)
- CM03 Form as core technical format
- Bilingual abstract (Chinese + English) required
- Research Architecture Diagram is mandatory
- Primary focus: Innovation (創新性) and Feasibility (可行性)

## Core Proposal Components

### 1. Executive Summary / Abstract

**NSF**: 1-page Project Summary with Overview, Intellectual Merit, Broader Impacts  
**NIH**: 30 lines, standalone  
**Key elements**: Problem statement, significance/urgency, novel approach, expected outcomes, team qualifications

### 2. Project Description / Research Strategy

**NSF** (15 pages): Background → Objectives → Preliminary results → Research plan → Timeline → Broader impacts  
**NIH R01** (12 pages): Significance → Innovation → Approach (with preliminary data)  
**DARPA**: Technical challenge → Approach → Schedule/milestones → Deliverables → Risk assessment

### 3. Specific Aims (NIH) / Objectives

**NIH Specific Aims page (1 page)**:
- Opening: Gap in knowledge and significance
- Long-term goal and immediate objectives
- Central hypothesis
- 2–4 specific aims with rationale, working hypothesis, approach summary
- Payoff paragraph: transformative impact

**Each aim structure** (parallel format): Action verb aim statement → Rationale → Working hypothesis → Approach summary → Expected outcomes

### 4. Broader Impacts (NSF) — Equal Weight with Intellectual Merit

Address at least one area:
1. Advancing discovery while promoting teaching and training
2. Broadening participation of underrepresented groups
3. Enhancing research and education infrastructure
4. Broad dissemination (public outreach, K-12, policy)
5. Benefits to society (economic, health, workforce)

**Strategy**: Be specific with concrete activities and timelines. Show how impacts will be measured. Connect to institutional resources.

### 5. Innovation

Highlight: Conceptual, Methodological, Integrative, Translational, or Scale innovation  
**Distinguish**: Incremental vs. transformative. Provide feasibility evidence (preliminary data, proof-of-concept).

### 6. Research Approach and Methods

Include: Study design, detailed methods per aim, power calculations, data analysis plans, quality control, potential problems and alternatives, rigor and reproducibility measures

### 7. Preliminary Data and Feasibility

**NIH R01**: Substantial preliminary data required  
**NIH R21**: Less stringent  
**NSF**: Less commonly required but strengthens competitive proposals  

Show: Pilot studies, method development, access to unique resources, relevant publications

### 8. Timeline and Milestones

- Phased Gantt chart with clear milestones and dependencies
- Realistic timeframes with contingency time built in
- **DARPA**: Quarterly deliverables, phase-based structure with exit criteria

Generate timeline diagrams:
```bash
python scripts/generate_schematic.py "Gantt chart showing 3-year research timeline with 4 aims, quarterly milestones, and key deliverables" -o figures/timeline.png --doc-type grant
```

### 9. Budget Justification

**NSF**: Up to 2 months summer salary, graduate student support encouraged  
**NIH**: Modular budgets ≤$250K/year; salary cap ~$221,900  
**DOE**: Often requires cost sharing  
**DARPA**: Detailed by phase and task  

**Justify every line item**: Effort percentages, equipment necessity, travel conferences, consultant roles

## Review Criteria Summary

| Agency | Primary Criteria |
|--------|-----------------|
| NSF | Intellectual Merit + Broader Impacts |
| NIH | Significance, Investigator(s), Innovation, Approach, Environment |
| DOE | Scientific merit, methodology, personnel, budget, relevance |
| DARPA | Technical merit, DARPA mission alignment, cost realism |
| NSTC | Innovation (創新性), Feasibility (可行性), PI capability, Value |

## Writing Strategy

**Write for multiple audiences**: Technical reviewers (scrutinize methods), related-field reviewers (need context), program officers (agency goals alignment), panel members (need clear organization)

**Build compelling narrative**:
1. Hook → 2. Problem → 3. Solution → 4. Evidence → 5. Impact → 6. Team capability

**Language**: Active voice, strong verbs (investigate, elucidate, validate — not "look at" or "study"), precise language, no vague terms ("several," "various")

## Grant Development Timeline

| Phase | When | Key Activities |
|-------|------|----------------|
| Planning | 2–6 months before | Identify opportunity, assemble team, collect preliminary data |
| Drafting | 2–3 months before | Write specific aims first, then project description, budget, broader impacts |
| Internal review | 1–2 months before | Circulate draft, mock review, revise |
| Finalization | 2–4 weeks before | Final revisions, all required forms, proofreading |
| Submission | 1 week before | Institutional approval, upload 48 hours early |

**Critical tip**: Never wait until the deadline. Submit 48 hours early minimum.

## NIH Resubmission (A1)

Introduction (1 page): Summarize criticisms → describe specific changes → use bullet points → respectful tone → highlight improvements

Address every major criticism. Strengthen weak areas. Use full 37-month window if new data needed.

## Common Mistakes

**Conceptual**: Not explicitly addressing review criteria, mismatch with agency mission, vague objectives, insufficient innovation  
**Writing**: Poor organization, excessive jargon, missing context, inconsistent terminology  
**Technical**: Inadequate methods detail, overly ambitious, no preliminary data for required mechanisms  
**Formatting**: Exceeding page limits (automatic rejection), wrong font/margins, missing required sections  
**Strategic**: Wrong program mechanism, weak team, no broader impacts for NSF, late submission

---

# Integration Guide

## Choosing the Right Component

| Task | Use |
|------|-----|
| Write manuscript sections | Part 1: Scientific Writing |
| Literature review for introduction | Part 2: Literature Review |
| Evaluate a manuscript or grant | Part 3: Peer Review |
| Submit to specific journal/conference | Part 4: Venue Templates |
| Create diagrams and schematics | Part 5: Scientific Schematics |
| Create conference poster | Part 6: LaTeX Posters |
| Create presentation slides | Part 7: Scientific Slides |
| Write funding proposal | Part 8: Research Grants |
| Fix grammar errors in any text | Part 9: Grammar Checking |
| Reword / simplify / adapt text | Part 9: Paraphrasing |
| Proofread before submission | Part 9: Grammar + Paraphrasing workflow |
| Generate graphical abstract | Part 5 (mandatory for all papers) |

## Typical Full-Paper Workflow

1. **Literature search** (Part 2) → gather and verify citations
2. **Outline sections** (Part 1, Stage 1) → bullet-point drafts per section
3. **Generate schematics** (Part 5) → graphical abstract + methods flowchart + additional figures
4. **Convert outlines to prose** (Part 1, Stage 2) → full paragraphs per section
5. **Apply venue template** (Part 4) → format for target journal
6. **Compile and validate** → `latexmk -pdf paper.tex` + `validate_format.py`
7. **Self-review** (Part 3) → pre-submission quality check

## Typical Grant Workflow

1. **Research the funding opportunity** → review agency criteria (Part 8)
2. **Conduct literature review** (Part 2) → background section content
3. **Write specific aims/objectives first** (Part 8, Section 3)
4. **Generate figures** (Part 5) → conceptual framework, timeline/Gantt, methodology flowchart
5. **Write project description** (Part 8, Section 2) → full paragraphs (Part 1 principles)
6. **Prepare budget justification, biosketches, broader impacts** (Part 8)
7. **Self-review against agency criteria** (Part 3)
8. **Apply venue template** (Part 4) → agency-specific formatting

## Typical Poster Workflow

1. **Simplify paper content** → select 1–3 key messages
2. **Pre-generation review** (Part 6, Step 0) → plan simple visuals
3. **Generate poster graphics** (Part 5 via Part 6 commands) → simple, high-contrast, giant text
4. **Post-generation review** (Part 6, Step 2b) → check at 25% zoom
5. **Assemble LaTeX poster** (Part 6) → choose beamerposter/tikzposter/baposter
6. **Compile and overflow check** → `grep "Overfull" poster.log`
7. **PDF review** (Part 6, Section 11) → inspect all 4 edges at 100% zoom

## Typical Presentation Workflow

1. **Research-lookup** → find 8–15 papers for citations
2. **Define formatting goal** (Part 7) → color scheme, font style
3. **Plan each slide** → title, key points, visual elements, citations
4. **Generate slides** (Part 7) → `generate_slide_image.py`, attach previous slide each time
5. **Attach existing data figures** for results slides
6. **Combine to PDF** → `slides_to_pdf.py slides/*.png -o presentation.pdf`
7. **Visual review** → `pdf_to_images.py` + inspect each slide image
8. **Practice 3–5× with timer** → aim for 90% of allocated time

---

# PART 9: GRAMMAR CHECKING & PARAPHRASING

## Overview

Grammar checking and paraphrasing are sentence-level editing skills applied after a draft is written. Grammar checking catches errors in correctness, while paraphrasing improves clarity, reduces wordiness, avoids plagiarism, or adapts text for a different audience or register. Both must preserve scientific accuracy and terminology.

**When to use grammar checking**: After completing any draft — manuscript section, abstract, grant narrative, poster text, or slide notes.  
**When to use paraphrasing**: When simplifying dense text, adapting content across audiences (specialist → general), rewording source material to avoid self-plagiarism or over-quoting, or improving sentence variety and flow.

---

## Grammar Checking

### How to Request a Grammar Check

Provide the text and specify the context:
- "Grammar-check this Methods section for a Nature submission"
- "Check this abstract for grammatical errors and awkward phrasing"
- "Proofread this grant specific aims page — fix errors but keep scientific terminology"

Always specify: **preserve all scientific terms, numbers, units, gene/protein names, and statistical notation exactly as written.**

### Grammar Error Categories

**Category 1 — Hard Errors (always fix):**

| Error Type | Example (wrong → correct) |
|------------|--------------------------|
| Subject-verb disagreement | "The results *shows*" → "The results *show*" |
| Wrong article | "*A* unique finding" → "*A* unique finding" ✓ / "*An* unexpected result" |
| Dangling modifier | "Using the assay, *the cells were measured*" → "Using the assay, *we measured the cells*" |
| Wrong tense in methods/results | "We *measure* the samples" → "We *measured* the samples" |
| Pronoun agreement | "Each participant completed *their* survey" (acceptable in modern usage) |
| Missing comma after introductory clause | "After treatment the cells were lysed" → "After treatment, the cells were lysed" |
| Fused sentences / comma splice | "The data were collected, *they were then analyzed*" → "The data were collected and then analyzed" |
| Incorrect preposition | "compared *to*" vs "compared *with*" (use *with* for like things in science) |

**Category 2 — Style Errors (fix in scientific writing):**

| Error Type | Example (wrong → correct) |
|------------|--------------------------|
| Passive voice overuse | "It was found that…" → "We found that…" or "The results showed…" |
| Weak verb choice | "We *looked at* protein expression" → "We *quantified* protein expression" |
| Nominalisation | "performed an analysis of" → "analysed" |
| Redundancy | "the end result", "future plans", "past history" → drop the modifier |
| Hedging overuse | "It could possibly be suggested that perhaps…" → "These results suggest…" |
| Vague quantifiers | "several", "various", "a number of" → use exact numbers where possible |
| Double negatives | "not uncommon" → "common" (unless intentional for nuance) |

**Category 3 — Scientific Writing Conventions:**

| Convention | Rule |
|------------|------|
| Tense in sections | Methods & Results: past tense. Established facts & general truths: present tense. |
| Numbers | Spell out one through nine; use numerals for 10+, measurements, percentages, statistics |
| Abbreviations | Define at first use: "magnetic resonance imaging (MRI)"; thereafter use abbreviation only |
| Units | Always use SI units with a space before unit symbol: "5 mL", "37 °C", "p < 0.05" |
| Italics | Gene symbols (*BRCA1*), statistical variables (*p*, *n*, *t*, *r*), Latin terms (*in vitro*, *et al.*) |
| Hyphenation | "well-characterized protein" (adjective before noun) vs "the protein was well characterized" (after noun) |

### Grammar Check Workflow

1. **Read for meaning first** — ensure every sentence has a clear subject and verb
2. **Check tense consistency** within each section
3. **Verify all abbreviations** are defined at first use
4. **Confirm number/unit formatting** throughout
5. **Read aloud** — sentences that are hard to say aloud are usually hard to read
6. **Check transitions** between sentences and paragraphs for logical flow

### Common Scientific Grammar Mistakes

**Incorrect use of "which" vs "that":**
- "The assay *that* we used" (restrictive — defines which assay) ✓
- "The assay, *which* is widely used," (non-restrictive — adds extra info) ✓
- Wrong: "The assay *which* we used showed…" (missing comma for non-restrictive)

**"Data" is plural:**
- Wrong: "The data *was* collected" → Correct: "The data *were* collected"
- Wrong: "This data shows" → Correct: "These data show"

**"Amount" vs "number":**
- Countable: "a *number* of cells", "a *number* of studies"
- Uncountable: "an *amount* of protein", "an *amount* of time"

**"Since" vs "because":**
- Use "because" for causation: "We used ANOVA *because* the data were normally distributed"
- Reserve "since" for time: "Protein levels increased *since* treatment began"

**"While" vs "although/whereas":**
- Use "although" or "whereas" for contrast: "*Although* sensitivity was high, specificity was low"
- Reserve "while" for simultaneous actions

**"Affect" vs "effect":**
- Affect (verb): "Treatment *affected* cell viability"
- Effect (noun): "The *effect* of treatment on cell viability"
- Effect (verb, rare): "to *effect* a change"

### Proofreading Checklist

- [ ] Every sentence has a clear subject and main verb
- [ ] Tense is consistent within each section (past for methods/results, present for established facts)
- [ ] All abbreviations defined at first use, used consistently thereafter
- [ ] Numbers follow style rules (spell out <10, numerals for measurements)
- [ ] Units are SI with correct spacing (5 mL, not 5mL)
- [ ] Gene/protein names formatted correctly (italics for genes)
- [ ] No dangling modifiers or misplaced clauses
- [ ] No comma splices or fused sentences
- [ ] Articles (a/an/the) used correctly throughout
- [ ] No redundant or vague phrasing
- [ ] Transitions between paragraphs are logical
- [ ] Final sentence of each section summarises or leads naturally to the next

---

## Paraphrasing

### When to Paraphrase

| Situation | Goal |
|-----------|------|
| Avoiding plagiarism / over-quoting | Restate a source's idea in your own words |
| Simplifying dense text | Make complex prose accessible without losing meaning |
| Audience adaptation | Rewrite specialist text for a general/lay audience |
| Improving sentence variety | Break up monotonous structure or repetitive phrasing |
| Tightening wordiness | Say the same thing in fewer words |
| Changing register | Formal → neutral, or technical → accessible |

### How to Request a Paraphrase

Always specify the goal and any constraints:
- "Paraphrase this paragraph for a general audience — keep all technical terms but explain them briefly"
- "Rewrite this methods paragraph to avoid self-plagiarism from our 2022 paper — same procedure, new wording"
- "Simplify this discussion paragraph — it's too dense for a 15-minute conference talk"
- "Paraphrase these three sentences to reduce word count by 30% without losing the key finding"
- "Rewrite in active voice throughout"

### Paraphrasing Strategies

**1. Synonym substitution** — Replace words with accurate synonyms:
- "utilise" → "use"; "demonstrate" → "show"; "conduct" → "perform"; "investigate" → "examine"
- **Caution**: Never substitute scientific terminology (gene names, drug names, technique names) with informal synonyms

**2. Sentence restructuring** — Change sentence structure while keeping meaning:
- Original: "Due to the limited sample size, the generalisability of the findings is restricted."
- Paraphrased: "The small sample size limits how broadly these findings can be applied."

**3. Voice change** — Switch between active and passive:
- Passive: "The samples were incubated for 24 hours at 37 °C."
- Active: "We incubated the samples for 24 hours at 37 °C."

**4. Combining or splitting sentences** — Merge short choppy sentences or break up long complex ones:
- Short + short → combined: "Expression increased. This was statistically significant." → "Expression increased significantly."
- Long → split: Break at the main clause boundary when a sentence exceeds ~30 words

**5. Changing sentence opener** — Vary how sentences begin:
- Instead of always starting with "The": use "In this study,", "These results", "To assess…", "Notably,", "Consistent with…"

**6. Abstraction level shift** — Move between specific and general:
- Specific → general: "The p53 pathway was activated" → "Apoptotic signalling was upregulated"
- General → specific: "Gene expression changed" → "mRNA levels of *BCL2* decreased 3-fold"

### Paraphrasing for Different Contexts

**From paper to poster/slide (simplification):**
- Remove subordinate clauses; one idea per sentence
- Replace jargon with plain language where possible
- Lead with the finding, not the method
- Original: "Western blot analysis revealed a statistically significant 2.3-fold upregulation of BCL2 protein expression (p = 0.003) in the treatment group compared with vehicle-treated controls."
- Simplified: "BCL2 protein levels more than doubled after treatment (p = 0.003)."

**From paper to grant (persuasive reframing):**
- Emphasise significance and novelty rather than detail
- Use forward-looking language: "These findings establish a foundation for…"
- Original: "We observed a correlation between X and Y in a cohort of 45 patients."
- Grant version: "Our preliminary data in 45 patients reveal a novel association between X and Y, motivating the proposed larger-scale validation study."

**From specialist to lay audience:**
- Define every technical term in parentheses or a following phrase
- Use analogies to familiar concepts
- Replace Latin/Greek-derived terms with common equivalents where precise meaning is preserved
- Original: "Apoptosis was induced via the intrinsic mitochondrial pathway."
- Lay version: "The drug triggered a built-in self-destruction program inside the cancer cells."

**For avoiding self-plagiarism (reuse of own prior text):**
- Change sentence structure substantially (not just synonym swaps)
- Reorder information within a paragraph
- Approach the explanation from a different angle (e.g., start with the conclusion instead of the setup)
- Always cite your own prior work even when paraphrasing it

### What NOT to Change When Paraphrasing

The following must always be preserved exactly:
- Gene and protein names (*TP53*, p53, BRCA1)
- Drug names and chemical compounds
- Statistical values and results (p-values, effect sizes, sample sizes)
- Numerical data and units
- Established technique names (ELISA, CRISPR-Cas9, RT-qPCR)
- Taxonomy and species names
- Diagnostic criteria and classification systems (DSM-5, ICD-11)
- Acronyms after they have been defined

### Paraphrasing Quality Checklist

- [ ] Original meaning preserved completely — no information added, removed, or distorted
- [ ] Scientific terminology unchanged (gene names, technique names, drug names)
- [ ] Numerical data and statistics identical to source
- [ ] Sentence structure is genuinely different from the original (not just synonym swaps)
- [ ] If paraphrasing a source, the source is still cited
- [ ] Text reads naturally — not awkward from over-engineering
- [ ] Appropriate for the target audience and register
- [ ] Word count target achieved (if reduction was the goal)

### Common Paraphrasing Pitfalls

| Pitfall | Description | Fix |
|---------|-------------|-----|
| Patchwriting | Changing only a few words while keeping the same structure — still plagiarism | Restructure the sentence completely |
| Meaning drift | Subtle change in meaning through imprecise synonym choice | Re-read and compare with original after paraphrasing |
| Over-simplification | Removing nuance or qualifications that are scientifically important | Preserve hedging language ("may", "suggests", "was associated with") when it reflects genuine uncertainty |
| Under-simplification | Paraphrasing for a lay audience but keeping all jargon | Read through the lens of someone without domain knowledge |
| Omitting the citation | Not citing the source after paraphrasing it | Always cite — paraphrasing does not remove the obligation to credit |
| Changing statistical claims | Rounding p-values or effect sizes differently | Copy numerical values exactly |

---

## Grammar + Paraphrasing Workflow (Combined Editing Pass)

Use this order for a complete editing pass on any scientific text:

1. **Structural pass** — Is every paragraph focused on one idea? Does the argument flow logically?
2. **Paraphrasing pass** — Improve clarity, reduce wordiness, adapt register if needed
3. **Grammar pass** — Fix hard errors (agreement, tense, articles, punctuation)
4. **Style pass** — Replace weak verbs, reduce passive voice overuse, cut redundancy
5. **Terminology pass** — Verify all scientific names, units, and abbreviations are correct and consistent
6. **Read-aloud pass** — Read the final text aloud; anything that stumbles needs revision

---

## Field-Specific Language Quick Reference

| Field | Key Conventions |
|-------|----------------|
| Biomedical/Clinical | "participants" not "subjects"; ICD/DSM nomenclature; generic drug names first |
| Molecular Biology | Italics for gene symbols (*TP53*), regular for proteins (p53); HGVS for variants |
| Chemistry | IUPAC nomenclature; SMILES/InChI for novel compounds; SI concentration units |
| Ecology | Binomial nomenclature italicized; taxonomic authorities at first mention |
| Neuroscience | Standardized atlas nomenclature; stereotaxic coordinates; specify recording techniques |
| ML/CS | Contribution bullets; ablation studies; reproducibility details; code release |
| Social/Behavioral | Person-first language; APA bias guidelines; validated assessment names |
