# Scientific Publication Suite

A single, self-contained agent skill that covers every stage of scientific publication — from first draft to submission-ready manuscript, conference poster, presentation deck, and funding proposal. Built by combining nine individual skills into one cohesive reference.

---

## What's Inside

| Part | Capability | Use When |
|------|-----------|----------|
| **1** | Scientific Writing | Drafting IMRAD manuscripts, abstracts, discussion sections |
| **2** | Literature Review | Systematic multi-database search, PRISMA, citation verification |
| **3** | Peer Review | Evaluating manuscripts, grants, and presentations |
| **4** | Venue Templates | Formatting for 50+ journals, conferences, grants |
| **5** | Scientific Schematics | AI-generated diagrams, flowcharts, pathway figures |
| **6** | LaTeX Posters | Conference posters (beamerposter / tikzposter / baposter) |
| **7** | Scientific Slides | PDF, PowerPoint, and Beamer presentation decks |
| **8** | Research Grants | NSF, NIH, DOE, DARPA, Taiwan NSTC proposals |
| **9** | Grammar & Paraphrasing | Proofreading, rewriting, audience adaptation |

---

## Quick Start

### Writing a manuscript section
```
"Write the Discussion section for a Nature submission on [topic]. 
Use IMRAD structure. Cite in numbered superscript format. 
Generate a graphical abstract and one methods flowchart."
```

### Running a literature review
```
"Conduct a systematic literature review on [topic] covering 2018–2025. 
Use PubMed, arXiv, and Semantic Scholar. Follow PRISMA. 
Output a formatted markdown document with verified citations."
```

### Creating a conference poster
```
"Create an A0 portrait poster in tikzposter for [conference]. 
Generate all visual elements as simple AI graphics (3 elements max per figure). 
Keep total text under 600 words."
```

### Building a slide deck
```
"Create a 15-minute conference talk PDF slide deck on [topic]. 
Dark blue and white color scheme. Attach existing figures from figures/. 
Include citations from research-lookup. 1 slide per minute, visual-first."
```

### Writing a grant proposal
```
"Write an NSF standard research proposal for [topic]. 
Include Project Summary, 15-page Project Description, 
Broader Impacts, and a Gantt chart figure. 
Follow NSF PAPPG formatting."
```

### Grammar check + paraphrase
```
"Grammar-check and proofread this Methods section for a journal submission. 
Fix hard errors only — preserve all gene names, statistics, and units exactly."

"Paraphrase this paragraph for a general audience. 
Keep technical terms but explain each one briefly on first use."
```

---

## How to Install in Another Project

Copy this folder into your project's skills directory:

```
your-project/
└── scientific-skills/
    └── scientific-publication-suite/
        ├── SKILL.md              ← Main skill (load this)
        ├── README.md             ← This file
        └── QUICK_REFERENCE.md   ← Fast lookup cheat sheet
```

Then point your agent at `SKILL.md`. No additional dependencies beyond what is already required by your project's scientific-skills environment.

> **Note on scripts**: Some commands in SKILL.md reference scripts (`generate_schematic.py`, `generate_slide_image.py`, `verify_citations.py`, etc.) that live in the original individual skill folders. If you need those scripts, copy the relevant `scripts/` and `assets/` folders from the source skills alongside this one, or install the full scientific-agent-skills repository.

---

## Source Skills

This combined skill was assembled from the following individual skills in the `scientific-agent-skills` repository:

| Source Skill | Maps To |
|-------------|---------|
| `scientific-writing` | Part 1 |
| `literature-review` | Part 2 |
| `peer-review` | Part 3 |
| `venue-templates` | Part 4 |
| `scientific-schematics` | Part 5 |
| `latex-posters` | Part 6 |
| `scientific-slides` | Part 7 |
| `research-grants` | Part 8 |
| *(new — not in original repo)* | Part 9 |

---

## Key Principles

1. **Always write in full paragraphs** — bullet points are for planning only; final manuscripts use flowing prose.
2. **Every paper requires a graphical abstract** — generated via Part 5 before finalising any document.
3. **Minimum figure counts are enforced** — 5 figures for research papers, 4 for reviews, 4 for grants.
4. **Poster graphics have strict complexity limits** — maximum 3–4 elements per AI-generated figure; giant fonts (120pt+); 60% white space.
5. **Grammar checks preserve scientific terminology exactly** — gene names, statistics, units, and drug names are never changed.
6. **Grant submissions require 48-hour early submission** — never wait until the deadline.

---

## Supported Venues (Sample)

**Journals**: Nature, Science, Cell, NEJM, Lancet, JAMA, PNAS, PLOS ONE, IEEE Transactions, ACM, Frontiers, BMC, Springer, Elsevier, Wiley  
**Conferences**: NeurIPS, ICML, ICLR, CVPR, ACM CHI, ISMB, RECOMB  
**Funding Agencies**: NSF, NIH (R01/R21/R03/K/F awards), DOE, DARPA, Taiwan NSTC  
**Poster Sizes**: A0, A1, 36×48 in, 48×36 in (landscape)  

---

## Reporting Guidelines Covered

CONSORT · STROBE · PRISMA · STARD · TRIPOD · ARRIVE · CARE · SPIRIT · CHEERS · SQUIRE

---

## License

MIT — see `LICENSE.md` in the root of `scientific-agent-skills`.
