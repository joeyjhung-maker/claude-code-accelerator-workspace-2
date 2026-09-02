---
name: fast-pdf-reading
description: "Never use brew install poppler or Read's PDF page-rendering as the first move for a PDF — use the persistent ~/.claude/tools/pdf-venv (pypdf) instead"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6cc31f60-dbea-48c4-8688-4a1da3aa0dc2
  modified: 2026-08-24T12:20:26.708Z
---

For reading PDF text, do not start with the `Read` tool's `pages` parameter (it silently requires `poppler`/`pdftoppm`, not installed on this machine) or with `brew install poppler` (pulls in `cmake` as a build dependency with no prebuilt bottle here, so it falls back to compiling from source — took 25+ minutes and never finished when tried).

**Why:** on 2026-08-24, ingesting Hormozi's *$100M Money Models* PDF hit exactly this trap. The fix that actually worked — a throwaway Python venv with `pypdf` — took 10 seconds to set up and 5 seconds to extract a 188-page book. That venv is now persistent at `~/.claude/tools/pdf-venv`, with a reusable script at `~/.claude/tools/pdf_extract.py`. Full writeup: [[fast-pdf-reading-workflow]] (`workflows/2026-08-24-fast-pdf-reading.md`).

**How to apply:** for any PDF-reading task, go straight to:
```
~/.claude/tools/pdf-venv/bin/python3 ~/.claude/tools/pdf_extract.py '<input.pdf>' '<output.txt>'
```
then `Read` the output in chunks. Single-quote paths — filenames starting with `$` get shell-expanded otherwise. If `~/.claude/tools/pdf-venv` is missing, recreate in seconds with `python3 -m venv` + `pip install pypdf`; do not fall back to poppler/brew.

Related: [[hormozi-100m-money-models-synthesis]]
