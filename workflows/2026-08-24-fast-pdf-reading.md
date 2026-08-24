# Workflow: Reading a PDF — use the persistent pypdf venv, not poppler

*Status: locked. Root cause found and fixed; verified working on a 188-page book in ~5s.*

Related: [[Promotion]] [[hormozi-100m-money-models-synthesis]]

## When to use this

Any time a task needs the actual text of a PDF — ingesting a book, reading a contract, pulling a report. Don't reach for the `Read` tool's built-in PDF page-rendering (`pages:` param) as the first move; on this machine it silently depends on `poppler` (`pdftoppm`), which isn't installed and is *not* worth installing.

## What happened

Asked to ingest Alex Hormozi's *$100M Money Models* PDF. `Read` with a `pages` range failed: `pdftoppm is not installed`. Ran `brew install poppler` to fix it — poppler pulls in `cmake` as a build dependency, and Homebrew had no bottled (prebuilt) binary for this machine's OS version, so it fell back to compiling `cmake` from source. That took over 25 minutes and was still linking when it got killed — never actually finished. Meanwhile a `python3 -m venv` + `pip install pypdf` round-trip, done in parallel out of impatience, took about 10 seconds to set up and 5 seconds to extract the full 188-page book to text. The brew route was purely wasted time; it should never have been the first attempt.

## The steps (locked)

A persistent tool now lives outside any git-tracked project, so it survives across sessions and workspaces:

1. **Venv** (already created, don't recreate): `~/.claude/tools/pdf-venv` — a Python venv with `pypdf` installed.
2. **Script** (already written, don't recreate): `~/.claude/tools/pdf_extract.py` — takes a PDF path (and optional output path), writes plain text with `===PAGE N===` markers so a long extraction can be chunk-read afterward without losing your place.
3. **Run it**:
   ```
   ~/.claude/tools/pdf-venv/bin/python3 ~/.claude/tools/pdf_extract.py '<input.pdf>' '<scratchpad>/out.txt'
   ```
   Always single-quote paths — filenames starting with `$` (e.g. `$100M Money Models - Alex Hormozi.pdf`) get shell-expanded by bash inside double quotes or unquoted, silently truncating the filename.
4. **Read the output** with the normal `Read` tool in chunks (offset/limit), same as any other large text file. Delete the extracted `.txt` from scratchpad once digested — it's a full copy of copyrighted text and shouldn't linger, even in a temp dir.
5. If `~/.claude/tools/pdf-venv` is ever missing (new machine, wiped `~/.claude`), recreate it in seconds: `python3 -m venv ~/.claude/tools/pdf-venv && ~/.claude/tools/pdf-venv/bin/pip install --quiet pypdf`. Do **not** reach for `brew install poppler` — same source-build trap.

## What good looks like

5 seconds to extract 255K characters from a 188-page PDF, versus 25+ minutes of a `cmake` source compile that never finished. No system-level install, no `sudo`, no risk to the Homebrew environment — just a throwaway-feeling venv that turned out to be worth keeping.
