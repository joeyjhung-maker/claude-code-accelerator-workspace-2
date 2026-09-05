---
name: brief-skool
description: The inflection point for Skool community posts — seeds become briefs with locked DNA, before any copy exists. This is the community-post analog to /brief, which is for Facebook/Meta ads — do not use /brief for Skool posts or this skill for ads. Use when Joey picks seeds by number from the skool-seed bank ("brief skool SK3 and SK7"), or says "build skool briefs" after a /storm-skool run. Locks Room, Job, Tap position, Mechanic, The Ask, Avatar, Proof, and a cross-seed check per post BEFORE any copy exists. One brief file per post in clients/{name}/{project}/briefs/. No copywriting — /produce-skool writes.
---

# /brief-skool — select, then specify. The last cheap decision, Skool edition.

Same shape as /brief: everything before this was divergent. The brief goes
convergent — a cloud of seeds collapses into one post with fixed DNA.
Everything downstream inherits the brief.

**No copywriting here.** The brief carries the seed verbatim + decisions.
The writing is /produce-skool.

Don't confuse this with /brief. /brief locks Concept/Angle/Awareness/The
Image for an ad — that DNA doesn't exist here. A Skool post isn't trying to
win a single scroll-stopping moment; it's one beat in an ongoing relationship
with a room full of people who already know Dan. The DNA below reflects that.

## The run

### 1. SELECT
Joey names seeds by number from `clients/{name}/{project}/skool-seeds/`. If
he hasn't picked yet, show the latest seed file's index (number + mechanic +
room + one line each) and let him pick. Never pick for him. He can steer
("SK3 but aim it at ROYA instead").

### 2. SPECIFY — lock the DNA per seed

For each picked seed, propose the full DNA **pre-filled** from the seed's
tags and the project file, then he confirms or edits. One block per post:

- **Room** — which Skool group this posts in (from the seed tag). Check it
  against the project file's room map and, critically, its **locked
  avatar/framing rules for that room** — e.g. B2B Leads Lab's "anyone landing
  meetings with high-value prospects, NOT escape-9-5" note versus AAA
  Ninjas's escape-9-5-is-fine framing. If the seed's angle doesn't match the
  room's locked avatar, flag it before locking anything else.
- **Job** — recruit into the group / deepen engagement inside it / ascend
  free→paid. One job per post. If a seed is trying to do two, that's a signal
  to split it into two briefs rather than force one post to carry both.
- **Tap position** — T1 (hook/awareness, soft, no hard ask) / T2 (qualify,
  a real but low-friction question) / T3 (the actual offer/invite, direct
  ask), from the seed tag. This is the closest thing here to the ad brief's
  Awareness field — it sets how direct the post is allowed to be.
- **Mechanic** — NAP / Poll / Auction / Tap / Handraiser / 2-Step /
  domino-assignment / proof-post / philosophy-stance, carried from the seed.
  Confirm or change; name it, don't leave it vague.
- **The Ask** — the literal micro-action wanted from the reader: comment a
  specific word, DM, show up to something, report back next week. Must be
  ONE concrete action a reader could do in the next 30 seconds — "engage
  more" or "get excited about this" is not an ask.
- **CTA type** — required whenever Job is `recruit` or `ascend` (both carry
  an ask by definition); optional for `engage`. Name one of Taylor Welch's
  four types ([[taylor-welch synthesis]], `mentors/taylor-welch/synthesis.md`),
  carried from the seed's tag or chosen fresh:
  - `comment` — real value first, ask lands in the last paragraph, re-pitch
    in the first comment.
  - `off-the-heels` — an implicit ask; the room asks YOU how to get in.
  - `direct-promo` — plain "grab it now," used sparingly, only when there's
    something people already want but forgot about.
  - `two-step` — "comment KEYWORD and we'll send it." Swipe the SHAPE only
    from `mentors/taylor-welch/swipes/2-step-master-list.md` — the
    qualifier conditions and scarcity framing, never the language or
    numbers. **Default the second qualifier condition toward "report back
    with your results" over "promise you'll actually use it"** — a
    report-back ask filters the same way Taylor's passive version does, but
    also plants a standing reason for the reader to return with a result,
    seeding the next domino/proof-post seed (banked 2026-09-02 from the
    Topa database post — see [[taylor-welch synthesis]]).
  A soft handraiser with no offer attached is `engagement-only`, not one of
  the four — don't force a real CTA type onto a post that's just asking a
  question.
- **Avatar** — pulled from the room's locked framing in the project file.
  State it explicitly in the brief even when it seems obvious — this is the
  field most likely to drift silently between rooms.
- **Proof** — any names/numbers/quotes the seed leans on, verified against
  the project/client file with a line reference. Unverified proof gets
  flagged in the brief, never silently kept. Never invent a result — if it's
  not in the file, ask.
- **Format** — Skool community post (the default) / email dupe of the post /
  DM script. The house voice pattern lives in `rubrics/copy-rubric.md`'s
  "Dan — Skool Community Posts" section — /produce-skool grades against it.
- **Guidelines** — Joey's steering for this post. Ask; empty is fine.
- **Source route** — from the seed's source tag:
  - `real-event` / UGC-sourced → keep the real names, numbers, and quotes
    verbatim in the brief; mariobot writes connective tissue only, never
    invents the specifics.
  - `competitor-structure` → borrow the sequencing/shape only, written fully
    fresh — never Mad-Lib a competitor's actual language.
  - everything else → mariobot writes fresh from the mechanic's shape and the
    house primer (`clients/{name}/primers/dan-skool-posts-body.md`).
- **Cross-seed check** — one line: does this post compete with or feed
  another room's funnel (the standing example: does a B2B Leads Lab plug
  inside AAA Ninjas risk starving the AAA→ROYA ascension)? Surface it here
  even when the answer is "no risk" — never leave the field blank. If the
  seed carried `[caution: cross-seed]`, this line is mandatory, not optional.

Present all proposed DNA blocks at once. He edits. Lock.

### Cadence check — mandatory before locking any asking brief
If Job is `recruit` or `ascend` (or CTA type is anything but blank/
`engagement-only`), read `clients/{name}/{project}/skool-cta-cadence.md`
before locking. Count that room's last 3-4 logged posts:
- If the room's recent posts are already ask-heavy (more asks than the
  75/25 target allows — roughly, no more than 1 in 3-4 should carry an ask),
  say so plainly and suggest either: (a) briefing a pure-value `job: engage`
  post for that room first, or (b) proceeding anyway with an explicit flag
  that this brief is knowingly running hot on asks. Never silently lock an
  ask-heavy brief without surfacing the count — this is the exact mistake
  Joey flagged after the fact once already.
- If the log doesn't exist yet or has no entries for this room, say so and
  proceed — there's nothing to check against yet.
- Remember the log's own limitation: it only reflects posts shipped through
  /produce-skool, not everything Nat/Joey/Dan post directly in Skool. Treat
  a "looks fine" read as a soft signal, not proof the real cadence is safe.

**Before you save — say the whole post in one breath.** Room, job, tap
position, mechanic, the ask, proof — 3–4 sentences where every clause implies
the next. If you keep needing "and also," a dimension isn't pulling its
weight yet — usually it's the Ask being vague, or the Mechanic not actually
matching the Tap position (a T1 with a hard direct ask is the most common
miss). This is a lighter version of [[The Lock]], not the full ad ritual — a
Skool post that's mostly rhyming is fine to ship; note where it's loose and
move on.

### 3. Name + save
One file per post, matching the existing convention in this folder:
`clients/{name}/{project}/briefs/skool-post-{descriptive-slug}.md`

Brief file contents: the DNA block above + the seed verbatim + a `status:
ready` line + date. /produce-skool reads this brief directly. When
/produce-skool runs it, status flips to `written` with a pointer to the
saved copy file.

### 4. Hand off
Close with the list of locked briefs (full paths) and: "Ready for
/produce-skool — which one first?" Do not start writing.

## Rules that bite here
- Never pick the seed, the room, the mechanic, or the ask FOR him. Propose,
  he decides.
- **Room, Job, Mechanic, and The Ask must all be named explicitly**, not
  implied by the seed's idea line. A brief where the Ask is still "get people
  excited" isn't locked yet.
- The room's locked avatar/framing rule from the project file is a hard
  constraint, not a suggestion — flag any seed that drifts from it before
  locking the rest of the DNA.
- Cross-seed check is mandatory on every brief, even when the honest answer
  is "no conflict here" — the field exists so the question gets asked every
  time, not just when someone remembers to worry about it.
- Cadence check against `skool-cta-cadence.md` is mandatory on every brief
  that carries an ask. Every ask-post must still deliver real value in the
  same post, never a bare ask — this is Taylor Welch's rule underneath the
  ratio, not just the ratio itself.
- Proof verified with a line reference or flagged. No exceptions.
- No copy. Not even a "sample line to show the tone."

Related: [[storm-skool]] [[produce-skool]] [[b2b-leads-lab-project]]
[[hopper-millions synthesis]] [[taylor-welch synthesis]] [[naps-nurture-and-picks]]
[[dan-truth-constraint]] [[The Lock]]
