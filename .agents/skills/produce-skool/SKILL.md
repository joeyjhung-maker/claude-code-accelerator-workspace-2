---
name: produce-skool
description: The writing stage for Skool community posts — a locked skool-brief becomes the actual post. Mariobot drafts in Dan's voice, then the light Dan-specific ChatGPT judge protects selling power and personality before the post is saved.
---

# /produce-skool — the brief becomes the post. Mariobot writes, the light judge aligns.

Mariobot creates the voice and surprise. The ChatGPT judge makes a small number
of high-impact corrections using `rubrics/dan-skool-chatgpt-rubric.md`.

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

For Dan Skool posts, invoke `run_mario.py` with `--no-style-contract`. The
legacy contract over-constrains the draft and strips out the personality this
route is meant to produce. Put essential truth and format constraints in the
brief itself.

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

### 4. Judge BEFORE showing — the light alignment pass

Read `rubrics/dan-skool-chatgpt-rubric.md` and judge the raw Mariobot draft
against Joey's final specimens.

Truth, the explicit ask, and brief match are hard gates. After those, judge
five things: opening, concreteness, sales spine, Dan voice, and reader action.

Make only the **one to three edits** that most improve attention, desire,
clarity, or voice. Preserve jokes, odd phrasing, fragments, ellipses, loose
capitalization, and deliberate roughness when they add personality. Do not
run `copy_lint.py` or the legacy `copy-rubric.md` as an automatic rewrite gate.

Do not show Joey a technical scorecard or narrate minor faults. Show the best
finished copy. Mention only a hard factual uncertainty or a decision that
genuinely blocks the copy.

Provenance still holds: never silently rewrite wording Joey supplied as final.
When Joey returns an edited version, save it, compare it with what he received,
and update the judge only when the correction is repeated or consequential.

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
Show the clean copy. Close with the saved path, confirm the
brief flipped to `written`, and: "Another skool brief, or /reflect to
promote what we learned?"

## Rules that bite here
- **mariobot writes or no one writes.** Blank/missing keys → STOP and
  escalate. Never self-draft as a fallback (unless Joey asks for
  fast-and-loose).
- **Use the Dan-specific light judge.** Selling power and personality matter
  more than technical cleanliness.
- **One to three high-impact edits.** Do not polish Mariobot flat.
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
