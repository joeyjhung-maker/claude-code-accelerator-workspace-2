---
name: produce-skool
description: The writing stage for Skool community posts — a locked skool-brief becomes the actual post. This is the community-post analog to /produce, which writes Facebook/Meta ads — do not use /produce for Skool posts or this skill for ads. Use when Joey says "produce skool", "write the skool post", names a skool brief, or says "write skool brief X" after a /brief-skool run. mariobot drafts in Dan's Skool voice, the copy-rubric's "Dan — Skool Community Posts" section judges BEFORE Joey reads it, then it saves to copy/ and flips the brief to written. This is the ONLY stage where Skool post copy gets written. No new strategy — the brief already locked Room/Job/Mechanic/Ask.
---

# /produce-skool — the brief becomes the post. mariobot writes, the judge grades, then you read.

Same two-brain trick as /produce: **mariobot drafts the floor, the judge
grades it, and only the clean version reaches Joey.**

**mariobot writes or NO ONE writes.** Never draft the copy yourself. If the
Genesis route is down or the keys are blank, STOP and escalate — see step 1.
The only exception is Joey explicitly asking for something fast-and-loose.

Don't confuse this with /produce. That skill writes Facebook/Meta ads,
routes by Awareness into ad body primers, and grades against the ad rubric's
Concept/Angle brief-match. This skill writes for a room full of people who
already know Dan — routes by Tap position, and grades against a completely
different section of the rubric.

## The run

### 1. Load the brief, check the keys
Joey names a skool brief (or says "produce skool" — then show the `status:
ready` briefs in `clients/{name}/{project}/briefs/` and let him pick). Read
the DNA block: Room, Job, Tap position, Mechanic, The Ask, Avatar, Proof,
Format, Cross-seed check.

Refuse a brief that isn't `status: ready` — if it's already `written`, ask
whether he wants a fresh variant or to overwrite.

Then check the writer is reachable BEFORE writing a word: `clients/.env`
must carry non-blank `GENESIS_API_KEY` + `ANTHROPIC_API_KEY`. Blank or
missing → STOP, tell Joey the route is down, do not self-draft.
([[always-use-mariobot-to-write]].)

### 2. Pick the primer — Tap position routes
The brief's **Tap position** sets how direct the post is allowed to be:
- **T1** → hook-forward, curiosity or value-led, soft or no direct ask. The
  job is attention and a reason to keep reading, not a conversion.
- **T2** → a real but low-friction question — a handraiser that sorts the
  room (see the copy-rubric's "engagement ask should SEGMENT, not just ask"
  rule) without pushing anyone toward a purchase decision.
- **T3** → the actual invite/offer post. Direct ask, clear single CTA, no
  hedging the mechanism away.

Primer source: `clients/{name}/primers/dan-skool-posts-body.md` — read the
shipped examples for structure (headline → body → engagement close → sign-off
→ P.S.) before drafting. This is the whole primer; there's no separate
hook/body/headline split like the ad path — a Skool post is one artifact.

### 3. Write — by Source route and Mechanic
All routes go through Genesis bots via the stateless prime→instruct protocol
(`scripts/run_*.py`). **mariobot** (`scripts/run_mario.py`) writes the whole
post in one pass, primed with the Tap-position shape and the brief's Mechanic:

- **real-event / UGC source route** → keep the brief's real names, numbers,
  and quotes exactly as given; mariobot writes connective tissue only. If
  mariobot's draft embellishes a real fact, that's a FAIL at the judge stage,
  not a style choice.
- **competitor-structure source route** → borrow only the sequencing/shape
  named in the brief; the actual sentences must be written fully fresh, never
  Mad-Libbed from the competitor's language.
- **everything else** → mariobot writes fresh from the Mechanic's shape
  (NAP / Poll / Auction / Handraiser / 2-Step / domino-assignment /
  proof-post / philosophy-stance) and the primer examples.

**Format branches what mariobot produces:**
- **Skool community post** (default) → headline + body + engagement close +
  sign-off, P.S. where the brief calls for one.
- **email dupe** → body only, no headline/subhead, matching
  [[flexxable-output-format]].
- **DM script** → short, conversational, no headline — this is a message,
  not a post.

### 4. Judge BEFORE showing — the gate
Nothing reaches Joey ungraded. **If the scorecard isn't shown, the grading
didn't happen.**

Provenance first: grade and auto-fix **mariobot's** lines hard. Any line
**Joey** wrote gets FLAGGED for him, never silently corrected.
([[judge-provenance-rule]], [[dont-verify-user-written-claims]].)

1. **Lint** — `python3 scripts/copy_lint.py <draft>` FIRST for the mechanical
   STRUCTURE rules. Remember the Skool-specific exemptions already banked in
   `rubrics/copy-rubric.md`: the ellipsis ladder (three trailing lines
   building to an "and") is a Dan device, not a fragment-stack FAIL — check
   the trailing-`…` test before flagging it. Rewrite every genuine FAIL,
   re-lint until clean.
2. **Scorecard** — grade against `rubrics/copy-rubric.md`'s **"Dan — Skool
   Community Posts"** section specifically, not the general ad VOICE/
   PERSUASION rules above it. As an explicit rule-by-rule PASS/FAIL
   tick-list, check at minimum:
   - Register: Aussie (not British), spoken contractions (ya/'em/gonna),
     double `!!` reserved for the actual climax, CAPS roughly one word every
     few lines, scare quotes for irony, loose capitalization left alone.
   - Structure: ellipsis ladder used correctly (trailing beats, not
     decoration), P.S. present as a structural beat where the brief calls
     for one, sign-off "Dan".
   - Persuasion: weakness/confession before the flex where it fits, the
     WHAT-CHANGED shown before the conclusion is named (not just asserted),
     asked-for proof present (never write around a proof gap — stop and ask
     Joey for the number instead), the engagement ask SEGMENTS the room
     rather than asking flatly, name-and-demote rather than scrub a thing
     the brief says not to center.
   - The reversal-fragment scan: check headline, body, AND P.S. separately
     for "That's not X… it's Y" / "Not X. Y." constructions — these survive
     in whichever section gets checked last, so check all three.
3. **Brief-match check** — does the draft still deliver the locked Room, Job,
   Mechanic, and The Ask? Did the Tap position hold (a T1 that's drifted into
   a hard T3 pitch, or a T3 that's gone too soft to actually ask)? Does it
   respect the Room's locked avatar/framing rule? If a CTA type was locked,
   does the draft actually follow that shape (e.g. a `two-step` brief that
   drifted into a bare `direct-promo` with no qualifier framing)? Does an
   asking post still deliver real, substantial value BEFORE the ask, per
   [[taylor-welch synthesis]]'s "never a bare ask" rule? Flag any drift as
   its own PASS/FAIL line — a drift isn't automatically a rewrite, but it
   must be SEEN and named before Joey reads it.
4. **Cross-seed check** — if the brief flagged one, restate it here as a
   reminder before the post ships, not just at brief time.

Rewrites are edits to mariobot's draft, not you re-writing the post — show
the scorecard (rubric ticks + brief-match + cross-seed line) with the copy.

### 5. Save, then flip
Two moves, both required:
- **Save** the finished post to `copy/`, matching the existing naming
  convention: `copy/YYYY-MM-DD-{room-slug}-skool-post-{descriptive-slug}.md`.
  For the Flexxable house spec (Arial, body 12, headline 35; emails
  body-only), see [[flexxable-output-format]] if this needs to go to the
  Drive folder as well.
- **Flip** the brief's frontmatter `status: ready → written` and add a
  `copy:` pointer to the saved file.
- **Log the cadence.** Append one row to
  `clients/{name}/{project}/skool-cta-cadence.md` (create it if it doesn't
  exist, matching the header/format of the existing one):
  `YYYY-MM-DD | room | job | has_ask (y/n) | cta_type | copy file`.
  This is what makes /brief-skool's cadence check meaningful for the NEXT
  brief — skipping this step silently breaks the ratio tracking for
  everyone downstream.

**Do NOT promote the lesson here.** Saving the work and promoting why it
worked/died are separate moves — promotion is /reflect at session end.

### 6. Hand off
Show the clean copy + the scorecard. Close with the saved path, confirm the
brief flipped to `written`, and: "Another skool brief, or /reflect to
promote what we learned?"

## Rules that bite here
- **mariobot writes or no one writes.** Blank/missing keys → STOP and
  escalate. Never self-draft as a fallback (unless Joey asks for
  fast-and-loose).
- **Grade against the Skool section of the rubric, not the ad rules above
  it.** Different register, different structural devices, different
  persuasion checklist.
- **Scorecard or it didn't happen.** Lint first, Skool-rubric tick-list
  second, brief-match + cross-seed check third.
- **Never write around a missing proof number.** Stop and ask Joey for the
  real figure or niche before drafting — a vague version is not a safe
  default.
- **Provenance holds.** Grade AI lines hard; only FLAG Joey's own.
- **Never invent a result, number, or quote.** If it's not in the project or
  client file, ask.
- **Save AND flip.** Copy to `copy/`, brief status to `written` with a
  pointer.

Related: [[storm-skool]] [[brief-skool]] [[taylor-welch synthesis]]
[[always-use-mariobot-to-write]] [[run-judge-before-showing-copy]]
[[judge-provenance-rule]] [[flexxable-output-format]] [[dan-truth-constraint]]
