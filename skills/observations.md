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

---

### Observation 5: `faith-thread` drafted only from the Second Brain wiki note, not the raw source it summarises — Joey called the posts flat

**Status:** ACTIONED (2026-09-05) — SKILL.md step 2 rewritten to require reading the raw source before drafting
**Date:** 2026-09-05
**Skill:** `faith-thread`
**Issue:** Ran `/faith-thread Biblical Meditation`, drafted 5 options straight from `Second Brain/wiki/biblical-meditation.md`. Joey rejected all of them: "you are writing posts from these summarised notes and they miss all the nuance and depth of the full raw sources." Checked the wiki note's own `sources:` frontmatter and read the raw files it was built from (`Prophet School - Session 12 - August 26.md` + two YT transcript notes) — they contain the actual vivid, quotable, specific language (the front-door/kitchen demonstration, the magnifying-glass image, "Pentecostalism is loud: it's a cover-up for disconnection," "a man who starved to death locked inside a supermarket") that the wiki note had compressed into flat one-line paraphrases ("Confidence in prayer is developed through proximity" with none of the surrounding contrast that makes it land). The wiki is a *good* index — it's just not the thing to draft the actual post text from.
**Fix applied:** `faith-thread/SKILL.md` step 2 now splits into (a) use the wiki note to confirm the topic exists and find its cross-references, then (b) look up that note's `sources:` frontmatter, locate the matching file(s) under `Second Brain/raw-sources/`, and read those in full — draft the actual post language from the raw source's specific quotes, images, and demonstrations, not from the wiki's paraphrase.

---

### Observation 6: `faith-thread` defaulted to `structure-bank.md` devices instead of the account's real voice — rejected a third time, plus a same-day reading-level rule reversed

**Status:** ACTIONED (2026-09-05) — SKILL.md step 3 now leads with the personal-processing register; the grade-2 reading-level lock from earlier the same day was reversed
**Date:** 2026-09-05
**Skill:** `faith-thread`
**Issue:** Even after fixing Observation 5 (raw source over wiki paraphrase), Joey rejected the redraft too: "its the way you are writing and explaining the concepts." He pointed at his real Google Sheets archive. Reading the actual 190-post archive (not `structure-bank.md`'s mined evidence, not `threads-voice.md`'s summary of it) showed the real gap: most real posts are first-person realisation/processing ("The more I pray, the more I realise this...", "I used to pray for God to change my situation. Sometimes he did. But then...", "Something that took me far too long to learn:") — not the named rhetorical devices (Definition Flip, Cleared Suspect, Counter-Intuitive Method) the skill was defaulting to for every draft. Those devices are real and evidenced, but they're a mined slice of high-rate outliers, not the baseline voice. `threads-voice.md` already listed the real recurring openers ("The more I…", "I used to…", "Something I…") but the skill never drew on them — it went straight to `structure-bank.md` every time.

**Compounding finding, same session:** a `~grade 2` reading-level rule had just been locked (from one narrow example) earlier the same day. Checking it against the real archive showed actual posts run grade 2.3–14.3, averaging ~5-6 — the grade-2 rule was a one-example overgeneralization that would have kept pulling drafts away from the real voice. Reversed before it did more damage. General lesson for both: **a rule locked from a single example, or a summary file (wiki note, structure-bank, voice-file summary) built from a mined/curated slice, needs checking against the full raw underlying data before being trusted as "the pattern"** — this is the same root issue as Observation 5, recurring at a different layer (voice register and reading level, not source material).

**Fix applied:** `faith-thread/SKILL.md` step 3 restructured to try the personal-processing register (pulling from `threads-voice.md`'s recurring-openers list, shaped around the raw source content) first, and treat `structure-bank.md` devices as a secondary option only when a note's content is a clean paradox/list/distinction. `threads-voice.md` gained a "Default voice register" section with the real quoted examples and a testimony-line caveat (generic "I used to…" framing is fine; an invented specific dated event is not). The grade-2 reading-level rule was reversed to no fixed target.

---

### Observation 7: `faith-thread` fix from Observation 6 overcorrected — 3 of 5 drafts used the same "realisation" opener shape under different structure-bank names

**Status:** ACTIONED (2026-09-05) — SKILL.md step 3 now requires variety across three families, capped at one personal-processing post per batch
**Date:** 2026-09-05
**Skill:** `faith-thread`
**Issue:** Observation 6's fix told the skill to default to the personal-processing register. Applied literally, that meant labelling three different drafts as three different structure-bank devices while all three actually opened with the same shape ("The more I…", "I used to…", "Something I…" — all realisation-openers). Joey: "options 1,2,3 are too similar in that they ALL start with a realisation. We only need 1 option for this." The fix for Observation 6 was correct about the register existing, but didn't say anything about capping how often it's used per batch — "vary the shape" was in the instructions but wasn't specific enough to catch three structurally-identical openers hiding under different names.

Joey then supplied 4 more real posts from his own archive, unprompted, as models for structures the skill didn't have at all: a "problem illumination" post (name a felt problem, reframe it as training, explain why, 8.43% eng), a "never/don't" warning post (permission clause + urgency + scripture citation + casual aside, 8.85% eng, 13 reposts), a "you know you've truly X when Y" diagnostic with two branching outcomes (**14.53% eng — the highest confirmed rate in the account so far**), and a Bible-story typology post (Moses' staff, 7.58% eng). None of these were in `structure-bank.md` despite being real, evidenced, high-performing posts from his own archive — the mining pass that built the bank simply missed them.

**Fix applied:** Added these four as structures #20-23 in `structure-bank.md` (Part 1, evidenced from Joey's own archive with real engagement numbers). `faith-thread/SKILL.md` step 3 rewritten around three families — personal-processing (Family A, capped at one per batch), Joey's newly-mined structures #20-23 (Family B, first-class not fallback), and the original mined devices (Family C, used only when content calls for one) — with an explicit instruction to vary across families, not just across named structures within one family.

---

### Observation 8: The old Skool judge optimized technical cleanliness and flattened Mariobot's selling voice

**Status:** ACTIONED (2026-09-08) — added a Dan-specific light judge and removed the legacy style-contract/lint gate from the Dan Skool route
**Date:** 2026-09-08
**Skill:** `produce-skool` + `scripts/run_mario.py`
**Issue:** Joey repeatedly found that raw general-model copy and his own edits sold harder than the output from the full Mariobot production setup. The bottleneck was not missing notes. The generation prompt was over-constrained by a legacy style contract, then the judge optimized for compliance, lint cleanliness, and a visible scorecard. This selected against the cheeky lines, concrete micro-scenes, uneven rhythm, and purposeful roughness that make Dan's copy feel human. The process was protecting rules instead of protecting the sale.
**Fix applied:** Added `rubrics/dan-skool-chatgpt-rubric.md`, added `run_mario.py --no-style-contract`, and rewrote both copies of `produce-skool` so truth and the brief remain hard gates while the style judge makes only one to three high-impact edits. Mechanical lint and the old copy rubric are no longer automatic gates for Dan Skool drafts.

---

### Observation 9: The light judge preserved voice but missed the emotional bridge

**Status:** ACTIONED (2026-09-08) — added the resistance-then-disarm check to the Dan Skool judge
**Date:** 2026-09-08
**Skill:** `produce-skool`
**Issue:** The mobile-follow-up draft correctly explained that calling is more powerful than email or LinkedIn, but it stopped at rational advice. Joey's edit named why readers avoid the call (“need some cojones”) and immediately made it feel safer by explaining that the gift has already opened the door. He also restored a functional headline and Dan sign-off despite requesting an informal FYI note.
**Fix applied:** The Dan judge now checks whether practical advice names the reader's emotional resistance and disarms it with the mechanism. It also no longer interprets “informal FYI” as an automatic instruction to remove the headline and sign-off.
