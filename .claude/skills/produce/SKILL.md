---
name: produce
description: The writing stage — a locked brief becomes the actual ad. Use when Joey says "produce", "write it", "produce the burnout ad", names a brief to write, or says "write brief X" after a /brief run. mariobot drafts (hooks → body → headlines, routed by the brief's Source route + Awareness), the copy-rubric judges BEFORE Joey reads it, then it saves to copy/ and flips the brief to written. This is the ONLY stage where copy gets written. No new strategy — the brief already locked the DNA.
---

# /produce — the brief becomes the ad. mariobot writes, the judge grades, then you read.

Everything upstream was decisions made while they were still cheap. This is
the one stage where copy actually gets written — and where the two-brain trick
runs: **mariobot drafts the floor, the copy-rubric grades it, and only the
clean version reaches Joey.**

**mariobot writes or NO ONE writes.** Never draft the copy yourself. If the
Genesis route is down or the keys are blank, STOP and escalate — see step 1.
The only exception is Joey explicitly asking for something fast-and-loose.

## The run

### 1. Load the brief, check the keys
Joey names a brief (or says "produce" — then show the `status: ready` briefs in
`clients/{name}/briefs/` and let him pick). Read the DNA block.

Refuse a brief that isn't `status: ready` — if it's already `written`, ask
whether he wants a fresh variant (`_v02`) or to overwrite.

Then check the writer is reachable BEFORE writing a word: `clients/.env` must
carry non-blank `GENESIS_API_KEY` + `ANTHROPIC_API_KEY`. Blank or missing →
STOP, tell Joey the route is down, do not self-draft. (Banked hard rule —
[[always-use-mariobot-to-write]].)

### 2. Pick the primers — Awareness routes
The brief's **Awareness** picks the body payload primer:
- **unaware / problem** → long-form, pain-led BODY primer (pain amplifies in
  the body — the hook still leads curiosity-first per the rubric)
- **solution / product** → comparison / offer primer
- **most-aware** → direct-offer primer

Hooks always prime from the hook primer (`clients/{name}/primers/hooks.md`).
Say which primer you applied. If the exact primer for an awareness level
doesn't exist yet, name the closest and flag it.

### 3. Write — by Source route
The brief's **Source route** decides the path. All three go through Genesis
bots via the stateless prime→instruct protocol (`scripts/run_*.py`):

- **regular** (hook bot → body → headlines):
  1. **Hooks** — `scripts/run_hookbot.py` (`ad-hook-bot-1`, 20 hooks via the
     mandatory double-pass). Grade all 20 against **`rubrics/hook-rubric.md`**
     (the Four Moves, the Loop/Ineffective gates, the flinch test, the 8
     vicious-hook principles) before presenting them — a too-polite or
     fully-disclosed hook is a FAIL, not a safe default. **Then run Gate 9**:
     tag each hook's dominant vehicle (Curiosity/Call-Out/Authority/Proof/
     Emotion/Contrarian/Urgency) and check the spread across the batch — fewer
     than 4 vehicles represented, or any one vehicle over 50%, is a batch-level
     FAIL even if every individual hook passed. On a Gate 9 fail, run a second
     targeted pass naming the missing/thin vehicles specifically, don't blindly
     regenerate 20 more. Present **all 20** (or the combined set after a
     targeted pass) in one flat list regardless of grade. Joey picks one or
     steers. **Never pick the hook for him.** If the whole set reads tame or
     naff, say so and push for a hotter pass — or run it through the rubric's
     Four Moves yourself — rather than presenting 20 timid ones. The hook is
     80% of the ad — spend the time here.
  2. **Body** — `scripts/run_mario.py` (`mariobot`) from the chosen hook. It
     prepends the style contract automatically.
  3. **Headlines** — mariobot writes them in the SAME conversation as a
     follow-up turn (body and headlines share one context).
- **swipe** → Mad-Lib via `swiping-master-bot`: near-verbatim, near-same
  length, swap the specifics for this brief's segment/mechanism. Carry the OG
  link from the brief.
- **organic** → keep the brief's EXACT hook verbatim; mariobot writes the rest
  fresh.

**Format branches what mariobot produces:**
- **text ad** → primary text + headline(s).
- **email** → body only. No headline, no subhead.
- **squeeze / landing** → headline + subhead + body.
- **video** → script to the conceit named in the brief (skit, customer call,
  podcast…). No named conceit → straight VSL.

### 4. Judge BEFORE showing — the gate
Nothing reaches Joey ungraded. **If the scorecard isn't shown, the grading
didn't happen.**

Provenance first: grade and auto-fix **mariobot's** lines hard. Any line
**Joey** wrote gets FLAGGED for him, never silently corrected — never touch his
dashes or signposts. ([[judge-provenance-rule]], [[dont-verify-user-written-claims]].)

1. **Lint** — `python3 scripts/copy_lint.py <draft>` FIRST. It catches the
   mechanical STRUCTURE rules a feel-based pass misses. Rewrite every AI FAIL,
   re-lint until clean.
2. **Scorecard** — grade the taste rules in `rubrics/copy-rubric.md` as an
   explicit rule-by-rule **PASS / FAIL tick-list — never a prose summary.**
   Any FAIL → rewrite that line, re-grade.

Rewrites are edits to mariobot's draft, not you re-writing the ad — the writer
already set the floor; the judge lifts it. Show the scorecard with the copy.

### 5. Save, then flip
Two moves, both required:
- **Save** the finished copy to `copy/` (markdown working copy). For the
  formatted Flexxable deliverable, output to the Drive folder in the house
  spec — **Arial, body 12, headline 35, subhead 30; emails body-only** —
  per [[flexxable-output-format]]. Mirror the emphasis fingerprint (bold =
  skim-path spine, CAPS = one punch-word per line, `!` rationed, `…` for
  rhythm).
- **Flip** the brief's frontmatter `status: ready → written` and add a
  `copy:` pointer to the saved file. If the pipeline can't trace brief → copy,
  the thread is lost.

**Do NOT promote the lesson here.** Saving the work and promoting why it
won/died are two separate moves — promotion is /reflect at session end. Don't
collapse them.

### 6. Hand off
Show the clean copy + the scorecard. Close with the saved path, confirm the
brief flipped to `written`, and: "Another brief, or /reflect to promote what
we learned?"

## Rules that bite here
- **mariobot writes or no one writes.** Blank/missing keys → STOP and escalate.
  Never self-draft as a fallback (unless Joey asks for fast-and-loose).
- **Never pick the hook for him.** All 20, one flat list, he chooses.
- **Two passes, two mindsets — write vicious, dial back second.** The creative
  brain and the compliance brain can't run at once. Let mariobot write hot;
  handle compliance as a SEPARATE editing pass (aim 7/10, flag the risk, don't
  neuter while writing). Trying to be safe mid-draft produces the tepid copy
  that dies in the feed. (Lesson 22.)
- **Scorecard or it didn't happen.** `copy_lint.py` first (mechanical), rubric
  tick-list second (taste). A prose "judge pass" is not a grade.
- **Provenance holds.** Grade AI lines hard; only FLAG Joey's own. His dashes,
  his signposts, his call.
- **Never invent a result, number, or quote.** The brief carries verified proof
  with line references. If a claim isn't there, ask — don't fill the gap.
- **Save AND flip.** Copy to `copy/`, brief status to `written` with a pointer.
- **Save now, promote later.** The lesson goes to winners/losers/brand via
  /reflect, not here.

Related: [[always-use-mariobot-to-write]] [[run-judge-before-showing-copy]] [[flexxable-output-format]] [[judge-provenance-rule]] [[hook-rubric]] [[creative-coverage]]
