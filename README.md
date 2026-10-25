# CV Automation

**ATS-friendly résumé/CV pipeline.** One command generates every version of my CV:
3 flagship LaTeX documents (PT / EN / Rust-focused) and 14 role-specific resumes
(7 PT-BR + 7 EN) as `.docx`, then verifies that every generated PDF survives an
applicant tracking system parse — single column, real text, standard headings,
no vendor names.

![License](https://img.shields.io/badge/license-MIT-yellow.svg)
![Python](https://img.shields.io/badge/python-3.12%2B-blue.svg)
![LaTeX](https://img.shields.io/badge/LaTeX-Tectonic-008080.svg)
![ATS](https://img.shields.io/badge/ATS-friendly-brightgreen.svg)

*Leia em português: [README.pt-BR.md](README.pt-BR.md)*

---

## What it produces

```
output/
├── docx/
│   ├── pt-BR/                      # 7 role-specific resumes (.docx)
│   └── en/                         # same 7 roles in English (.docx)
├── pdf/
│   ├── pt-BR/                      # PDFs converted from .docx
│   └── en/
└── latex/                          # 3 general PDFs (PT, EN and EN-Rust)
```

## Quick start

```sh
# requirements: uv, tectonic, (optional) libreoffice
make all      # docx + latex + pdf + ATS check
make docx     # 14 role-specific .docx (output/docx/pt-BR, output/docx/en)
make latex    # 3 LaTeX PDFs            (output/latex)
make pdf      # convert .docx -> .pdf (output/pdf/)
make check    # ATS verification of every generated PDF
make clean
```

Tools are overridable, e.g. `make latex TECTONIC=~/.local/bin/tectonic`.

### Installing the toolchain

| Tool | Install |
|---|---|
| [uv](https://docs.astral.sh/uv) | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| [tectonic](https://tectonic-typesetting.github.io) | `cargo install tectonic` (or grab a release binary) |
| LibreOffice (optional, for DOCX -> PDF) | system package manager |

Python dependencies are resolved on the fly by `uv run --with ...` — there is no
virtualenv to create and no `requirements.txt` to maintain.

## How it works

- **`src/latex/`** — one shared `cv-preamble.tex` (Arial via `fontspec`, single
  column, hyphenation disabled so words are never split) plus one `.tex` per CV.
  Compiled with Tectonic (self-contained XeTeX).
- **`src/docx/`** — `gen_docx_base.py` holds the styling helpers and the shared
  content blocks (experience, education, languages); `gen_all.py` declares the
  per-role content (summary, project picks, skill groups) and renders the 14
  files with [python-docx](https://python-docx.readthedocs.io).
- **`src/tools/check_ats.py`** — extracts text from every generated PDF and asserts:
  standard section headings, contact info in the body, no corrupted glyphs,
  consistent dates, expected keywords. Output: one line per file, `OK` or the
  list of problems.

## ATS rules applied

Based on current ATS guidance for 2026:

- single-column layout, no tables, no text boxes, no images
- contact details as real text in the body (never in page headers/footers)
- standard section names (`Professional Summary`, `Experience`, `Skills`,
  `Education`, ...) so parsers can map fields
- standard font (Arial), 9-16 pt, embedded and selectable text
- simple `-` bullets, no icon fonts or decorative glyphs
- one date format everywhere (`Feb 2025 - Present` / `Fev 2025 - Atual`)
- keywords from each job description, backed by real project bullets
- no em dashes, no vendor names, no keyword stuffing

## Make it yours

The content is data, not code: fork the repo, then

1. edit the per-role content in `src/docx/gen_all.py` (summaries, projects, skills)
   and the shared blocks in `src/docx/gen_docx_base.py`;
2. edit or replace the `.tex` files in `src/latex/`;
3. run `make all` and check the report at the end.

Every claim in the output should map to something verifiable — mine map to
public repositories at [github.com/luis-ota](https://github.com/luis-ota).

## License

MIT — take the pipeline, the template and the ATS rules, keep your own story.
