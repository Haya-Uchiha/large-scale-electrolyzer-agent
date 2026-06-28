# Scientific Publication Suite — Quick Reference

Fast lookup for the most common tasks. For full details, see `SKILL.md`.

---

## Diagram Generation

```bash
# Any diagram (default quality 7.5/10)
python scripts/generate_schematic.py "description" -o figures/out.png

# Journal quality (8.5/10)
python scripts/generate_schematic.py "description" -o figures/out.png --doc-type journal

# Graphical abstract (REQUIRED for every paper)
python scripts/generate_schematic.py "Graphical abstract: workflow from input → methods → findings → conclusion" \
  -o figures/graphical_abstract.png --doc-type journal

# Photo-realistic illustration
python scripts/generate_image.py "description" -o figures/out.png
```

---

## Manuscript Writing

| Section | Tense | Notes |
|---------|-------|-------|
| Abstract | Past (methods/results), present (significance) | No labeled subsections unless journal requires |
| Introduction | Present | Cite 5–10 recent papers, end with objectives |
| Methods | Past | Enough detail to reproduce; ethics approval statement |
| Results | Past | Objective; no interpretation; integrate figures/tables |
| Discussion | Present + past | Interpret, compare to literature, state limitations |

**Writing rule**: Outline with bullet points → convert to full prose. Never submit bullets.

---

## Citation Styles at a Glance

| Style | In-text | Used by |
|-------|---------|---------|
| AMA | ¹ superscript | Medicine |
| Vancouver | [1] brackets | Biomedical |
| APA 7 | (Smith, 2023) | Social sciences |
| IEEE | [1] brackets | Engineering/CS |
| Nature | ¹ superscript | Nature journals |

Verify all DOIs: `python scripts/verify_citations.py manuscript.md`

---

## Reporting Guidelines

| Study Type | Guideline |
|-----------|-----------|
| RCT | CONSORT |
| Observational (cohort/case-control) | STROBE |
| Systematic review / meta-analysis | PRISMA |
| Diagnostic accuracy | STARD |
| Prediction model | TRIPOD |
| Animal research | ARRIVE |
| Case report | CARE |

---

## Literature Review Commands

```bash
# Step 1 — broad academic search
parallel-cli search "topic" -q "kw1" -q "kw2" \
  --json --max-results 10 --excerpt-max-chars-total 27000 \
  --include-domains "scholar.google.com,arxiv.org,pubmed.ncbi.nlm.nih.gov,semanticscholar.org,biorxiv.org,nature.com,cell.com" \
  -o sources/search-academic.json

# Step 2 — extract full text from a URL
parallel-cli extract "https://doi.org/10.xxxx/yyyy" --json

# Step 3 — deduplicate + rank results
python scripts/search_databases.py combined.json --deduplicate --rank citations --output results.md

# Step 4 — verify citations
python scripts/verify_citations.py my_review.md

# Step 5 — generate PDF
python scripts/generate_pdf.py my_review.md --citation-style nature --output review.pdf
```

---

## Venue Templates

```bash
# Find a template
python scripts/query_template.py --venue "Nature" --type "article"

# Customize it
python scripts/customize_template.py \
  --template assets/journals/nature_article.tex \
  --title "Title" --authors "A, B" --output paper.tex

# Validate compiled PDF
python scripts/validate_format.py --file paper.pdf --venue "Nature" --check-all

# Compile
latexmk -pdf paper.tex
```

---

## Poster Graphics Rules (CRITICAL)

Every AI-generated poster graphic must follow these hard limits:

| Rule | Limit |
|------|-------|
| Elements per graphic | 3–4 max |
| Words per graphic | 10 max |
| White space | 60% minimum |
| Key number font size | 120–150pt |
| Label font size | 80–100pt |

**Mandatory prompt prefix**: `"POSTER FORMAT for A0. ULTRA-SIMPLE [N] elements: ..."`

**Patterns that always fail**: 7-stage workflows · 3+ case studies in one image · year-by-year timelines · 5+ method comparisons

**Overflow check after compile**:
```bash
grep "Overfull" poster.log          # Fix ALL warnings before proceeding
pdfinfo poster.pdf | grep "Page size"
```

---

## Slide Generation

```bash
# Title slide (establishes style)
python scripts/generate_slide_image.py \
  "Title slide: 'Your Title'. Speaker: K-Dense. FORMATTING GOAL: dark blue, white text, gold accents, minimal." \
  -o slides/01_title.png

# Each subsequent slide — ALWAYS attach previous
python scripts/generate_slide_image.py \
  "Slide: 'Key Findings'. 3 bullets. CITATIONS: (Smith 2023). FORMATTING GOAL: match attached." \
  -o slides/02_findings.png --attach slides/01_title.png

# Results slide with existing data figure
python scripts/generate_slide_image.py \
  "Results slide. Present attached chart. FORMATTING GOAL: match attached." \
  -o slides/03_results.png --attach slides/02_findings.png --attach figures/chart.png

# Combine to PDF
python scripts/slides_to_pdf.py slides/*.png -o presentation.pdf

# Convert PDF to images for review
python scripts/pdf_to_images.py presentation.pdf review/slide --dpi 150
```

**Talk timing**: ~1 slide/minute · 40–50% of time on results · never skip conclusions

---

## Grant Proposal Checklists

### NSF
- [ ] Project Summary (1 page): Overview + Intellectual Merit + Broader Impacts
- [ ] Project Description (≤15 pages, 10pt+, 1-inch margins)
- [ ] Broader Impacts (concrete activities, timelines, metrics)
- [ ] Timeline / Gantt chart figure
- [ ] Biosketch (3 pages per senior personnel)
- [ ] Data Management Plan

### NIH R01
- [ ] Specific Aims (1 page) — write this FIRST
- [ ] Research Strategy (≤12 pages): Significance → Innovation → Approach
- [ ] Preliminary data included and tied to aims
- [ ] Power calculations documented
- [ ] Budget: modular (≤$250K/yr) or detailed (>$250K/yr)
- [ ] Biosketch (5 pages)

### DARPA
- [ ] Heilmeier Catechism answered: What? Why now? Who cares? What if you succeed?
- [ ] Phase-based structure with exit criteria
- [ ] Quarterly milestones with measurable metrics
- [ ] Transition and commercialisation plan

### NSTC (Taiwan)
- [ ] CM03 Form
- [ ] Bilingual abstract (Chinese + English)
- [ ] Research Architecture Diagram (mandatory visual)
- [ ] Strong preliminary data (critical for credibility)

---

## Grammar Quick Fixes

| Wrong | Correct | Rule |
|-------|---------|------|
| "The data was collected" | "The data **were** collected" | Data is plural |
| "Since treatment increased X…" (causal) | "**Because** treatment increased X…" | Since = time only |
| "Using the assay, the cells were measured" | "Using the assay, **we measured** the cells" | Dangling modifier |
| "compared to controls" (like things) | "compared **with** controls" | With = like things |
| "performed an analysis of" | "**analysed**" | Avoid nominalisation |
| "It was found that…" | "We found that…" / "Results showed…" | Avoid impersonal passive |
| "While X was high, Y was low" (contrast) | "**Although** X was high, Y was low" | While = simultaneous |

**Tense rules**: Methods & Results = past tense · Established facts = present tense · Introduction/Discussion = present tense for general claims

---

## Paraphrasing Quick Guide

**Do change**: Word choice, sentence structure, voice (active/passive), sentence length, opening phrase  
**Never change**: Gene/protein names · drug names · statistical values · units · technique names · species names

| Goal | Strategy |
|------|----------|
| Simplify for poster/slide | One idea per sentence; lead with finding, not method |
| Adapt for lay audience | Define every term; use analogies; replace Latin terms |
| Reduce for grant | Emphasise significance; use forward-looking language |
| Avoid self-plagiarism | Change structure substantially; cite own prior work |

---

## Figure Requirements by Venue

| Venue | Min DPI | Formats |
|-------|---------|---------|
| Nature | 300 | TIFF, EPS, PDF |
| Science | 300 | TIFF, PDF |
| PLOS | 300–600 | TIFF, EPS |
| IEEE | 300 | EPS, PDF |
| Poster (print) | 300 | PDF (vector preferred) |
| Slides | 150 screen / 300 print | PNG, PDF |

---

## Complete Workflow Summaries

### Full Paper (end to end)
1. Literature search (Part 2) → verified citation list
2. Outline each section with bullet points
3. Generate graphical abstract + figures (Part 5)
4. Expand outlines to full paragraphs (Part 1)
5. Grammar check + paraphrase (Part 9)
6. Apply journal template (Part 4) → `latexmk -pdf`
7. Self-review against reporting guideline checklist (Part 3)

### Grant (end to end)
1. Read agency solicitation → note page limits and review criteria
2. Write Specific Aims / Objectives page FIRST
3. Conduct supporting literature review (Part 2)
4. Generate Gantt chart + methodology figures (Part 5)
5. Write project description in full paragraphs (Parts 1 + 8)
6. Add broader impacts, budget justification, biosketches
7. Grammar check every section (Part 9)
8. Validate against agency formatting rules (Part 4)
9. Submit ≥48 hours before deadline

### Poster (end to end)
1. Select 1–3 key messages from paper
2. Pre-generation review — plan ≤4-element, ≤10-word graphics
3. Generate ULTRA-SIMPLE AI graphics (Part 5 / Part 6)
4. Post-generation review at 25% zoom — all text readable?
5. Assemble in tikzposter / beamerposter / baposter (Part 6)
6. Compile → check `poster.log` for Overfull → inspect all 4 edges

### Presentation (end to end)
1. Research-lookup → 8–15 papers for citations
2. Define formatting goal (colors, fonts)
3. Plan slides: title / key points / visual / citations per slide
4. Generate slides with `generate_slide_image.py` (attach previous each time)
5. Attach data figures to results slides
6. Combine → `slides_to_pdf.py` → review with `pdf_to_images.py`
7. Practice 3–5× with timer; aim for 90% of allotted time
