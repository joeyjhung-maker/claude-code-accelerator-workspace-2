# Skill Observations

Running backlog of corrections and repeated patterns worth turning into a skill change. Logged by task-observer, actioned via /save-as-skill (new skills) or /upskill (existing-skill fixes).

Status key: OPEN = not yet actioned | ACTIONED (YYYY-MM-DD) — what changed | DECLINED (YYYY-MM-DD) — why

Related: [[Promotion]] [[Memory Loop]]

---

### Observation 1: Global npm installs need sudo on this machine — prefer npx

**Status:** OPEN
**Date:** 2026-08-13
**Skill:** Cross-cutting (hit during the CLI update, then again in defuddle)
**Issue:** `/usr/local/lib/node_modules` is root-owned, so any `npm install -g` fails with EACCES and needs a sudo password Claude can't supply. This came up twice in one day: updating the Claude Code CLI, then installing defuddle. Each time it cost a detour before landing on the workaround.
**Suggested fix:** Default to `npx --yes <tool>` for any Node CLI rather than a global install. Only escalate to `sudo npm install -g` (run by Joey in his own terminal) when a tool genuinely can't run via npx. Worth a line in the Script if it bites a third time.

---

### Observation 2: `copy_lint.py` reports a false clean on any file using `---` as a section break

**Status:** OPEN
**Date:** 2026-08-13
**Skill:** `scripts/copy_lint.py` (used by /produce and every judge pass)
**Issue:** `body_lines()` splits the file on `\n---\n` and lints only `parts[1]` — it assumes `---` means frontmatter delimiters. A 9-section long-form ad that uses `---` as its section breaks therefore linted as **"1 FAIL, 0 FLAG"** when the real count was 65 FAIL / 2 FLAG. The gate passed silently on a draft it should have stopped. Only caught it because the number looked implausibly good against a draft that had failed 72 times ten minutes earlier.
**Suggested fix:** Treat `---` as frontmatter only when it appears in the first few lines of the file (or only when the file OPENS with `---`). Otherwise lint the whole body. Until it's fixed, any long-form/multi-section draft has to be linted with the breaks stripped: `sed 's/^---$/SECTIONBREAK/'`.

---

### Observation 3: `copy_lint.py` and the copy-rubric pass both missed long run-on sentences — only caught on Joey's read

**Status:** OPEN
**Date:** 2026-08-28
**Skill:** `scripts/copy_lint.py` + `rubrics/copy-rubric.md` (used by /produce and every judge pass)
**Issue:** Produced 7 Most-Aware static-ad copy pieces, ran `copy_lint.py` on all of them, all came back clean (0 FAIL / 0 FLAG or trivial flags only). Joey then flagged one on read: "sentences are too long" — e.g. "The book itself is the full blueprint for landing performance-based AI clients who pay you 30-50% of the revenue you generate, with no upfront cost to them." (26 words, 3 clauses, one period). `copy_lint.py`'s "two+ full sentences on one line" rule only fires when a line has multiple SENTENCES (multiple end-stops) — a single long compound/run-on sentence with one final period passes clean no matter how many clauses it stacks with commas, "and," or "who." The copy-rubric's taste pass (graded before this went to Joey) didn't catch it either — nothing in either gate explicitly checks clause-count or word-count per sentence against the Script's house rule ("Short punchy paragraphs. One idea per line. Each sentence earns its own line.").
**Suggested fix:** Add a mechanical check to `copy_lint.py` — flag any line/sentence over ~15-18 words or containing 2+ comma-joined independent clauses, since that's almost always "one idea per line" being violated even when it's grammatically one sentence. Until fixed, the judge pass needs an explicit manual step: read each sentence and ask "is this one idea?" — not just check for multiple sentences per line.
**Also noted:** the same production run showed `copy_lint.py` scanning a saved copy-file's ANNOTATION PROSE (the write-up above the `## Hook` section) as if it were ad copy, because that prose sits between the frontmatter `---` and the first section `---` — same root cause as Observation 2. Fix: lint only the isolated `## Body` section content, not the whole markdown file, until Observation 2 is fixed upstream.

---

### Observation 4: `copy_lint.py` throws a false FAIL on abbreviations like "Inc." — the opposite failure mode from Observations 2/3

**Status:** OPEN
**Date:** 2026-09-05
**Skill:** `scripts/copy_lint.py` (used by /produce and every judge pass)
**Issue:** The "two+ full sentences on one line" check splits on `(?<=[.!?])\s+` — any period followed by whitespace counts as a sentence end. On the BotBuilders JV email rewrites, this fired on genuinely single sentences that happen to contain an abbreviation: "They just hit #710 on the Inc. 5000 list of America's fastest-growing private companies in America." reads as two sentences to the regex because "Inc." ends in a period. Hit this twice in one session (Email 1 and Email 4 of the same JV sequence) — both had to be manually verified as false positives rather than rewritten.
**Suggested fix:** Add a short abbreviation exception list to the split regex (Inc., vs., etc., Mr., Mrs., Dr., U.S., a.m., p.m.) so a period immediately after one of these doesn't count as a sentence boundary. Until fixed, any FAIL on a line containing an abbreviation needs a by-eye check before rewriting it — don't trust the count blindly.
