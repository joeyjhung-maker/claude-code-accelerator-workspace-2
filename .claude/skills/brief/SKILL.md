---
name: brief
description: The inflection point — seeds become briefs with locked DNA. Use when Joey picks seeds by number from the seed bank ("brief T3, R1 and I2", "brief seeds 4 and 7"), or says "build briefs" after a /storm run. Locks Segment, Awareness, Mechanism, Problem-name, The Image, Spokesperson, CTA, Guidelines, and Source-routing per ad BEFORE any copy exists. One brief file per ad in clients/{name}/briefs/. No copywriting — the brief is the last cheap decision; /produce writes.
---

# /brief — select, then specify. The last cheap decision.

Everything before this was divergent: pull wide, save everything. The brief
is where it goes convergent — a cloud of seeds collapses into one ad with
fixed DNA. Everything downstream inherits the brief; after this point,
changes cost money. So this is where we slow down.

**No copywriting here.** The brief carries the seed verbatim + decisions.
The writing is /produce.

## The run

### 1. SELECT
Joey names seeds by number from `clients/{name}/seeds/`. If he hasn't picked
yet, show the latest seed file's index (number + hook, one line each) and let
him pick. Never pick for him. He can steer ("T3 but aim it at 9-5 escapees
instead").

### 2. SPECIFY — lock the DNA per seed
For each picked seed, propose the full DNA **pre-filled** from the seed's
tags and the client file, then he confirms or edits. One block per ad:

- **Segment** — from the seed tag; check against strategy-map segments.
- **Awareness** — from the seed tag. This picks the payload primer downstream
  (unaware/problem → long-form pain-led BODY primer — pain is the amplifier in
  the body, the hook still leads curiosity-first; solution/product →
  comparison/offer primer; most-aware → direct offer). **For unaware/problem,
  name the belief this ad works** — the existing worldview it VALIDATES ("finally
  someone gets it") or CHALLENGES ("that's wrong"). Carried from the seed's R-door
  tag; if it's blank, you don't have an unaware ad yet — you have a hook floating
  in space.
- **Concept** — the flat fact underneath (no spin, no villain, no "you").
- **Angle** — the door in (fear, contrarian, discovery, remove-the-blame…).
  Concept and Angle are named SEPARATELY — if you can't state the concept
  flat, you don't have one yet.
- **Mechanism** — client default unless the seed says otherwise (Flexxable:
  AI + SMS revives the business's dead leads; performance-based, 30-50% of
  profits).
- **Problem name** — give the enemy a name the market has never heard but
  instantly gets. "Estrogen leak." "Joint drought." "Cortisol belly." "Skinny
  bacteria." "Soft tallow." The formula: body-part/concept + dysfunction word,
  so it sounds like a real diagnosis without being jargon. A good name carries
  the why-now, implies the fix (a leak gets plugged, a drought gets watered),
  and often dodges the compliance trap — the NAME sells while the claim stays
  accurate. The name becomes the mechanism's handle in every downstream ad.
  If a cognitive binary suggests itself, name it here too — dead oil vs living
  oil, horse pills vs micro-strip: the bad side is life WITHOUT the mechanism,
  the good side is life WITH it. Both optional but high-leverage; propose,
  Joey keeps or kills.
- **The Image** — one picture a 10-year-old could draw, that shows the
  mechanism in a single glance. Not a line of copy — a PICTURE. (Green body /
  red brain for brain-energy depletion. Money flushed down the toilet for
  wasted supplements. A dog at a slot machine for overstimulation.) If you
  can't name the picture, the mechanism isn't concrete yet — push it until a
  picture appears. This is the highest-leverage field on the page: the ad that
  owns the clearest picture wins, and this is the last stage cheap enough to fix it.
  The image can be literal or absurd — it doesn't have to depict the product,
  it has to make the mechanism obvious or the scroll stop.
- **Spokesperson** — WHO is talking, and the archetype that positions them.
  The positioning must be a natural extension of who's presenting (a CIA agent
  ≠ a life coach; a magician CURES, a scientist DISCOVERS — match the frame to
  the person). Name the archetype (rebellious expert / accidental millionaire /
  scientific authority / reluctant genius / outsider who asked the dumb
  question). For Flexxable the spokesperson is **Dan**, so his archetype is the
  lens AND the guard-rail: first-person claims must be true to Dan — no
  invented backstory. See [[dan-truth-constraint]]. If the spokesperson is
  interchangeable, the positioning isn't locked yet.
- **CTA** — client default unless overridden (Flexxable: the $14.40 book +
  bonuses, 30-day keep-everything guarantee).
- **Format** — text ad / static / video. If video with a specific conceit
  (skit, customer call, podcast…), name the conceit — it changes how the
  script gets written in /produce.
- **Guidelines** — Joey's steering for this ad. Ask; empty is fine.
- **Source route** — from the seed's source tag:
  - `swipe` → Mad-Lib in /produce: near-verbatim, near-same length, swap the
    specifics. Carry the OG link.
  - `organic` → keep the EXACT hook, write the rest fresh.
  - everything else → regular path (hook bot → body → headlines).
- **Proof** — any names/numbers the seed leans on, verified against the
  client file with line reference. Unverified proof gets flagged in the
  brief, never silently kept. (Never invent a result — if it's not in the
  client file, ask.)

Present all proposed DNA blocks at once. He edits. Lock.

**Before you save — run the one-breath test ([[The Lock]]).** Say the whole ad
in ONE breath: segment, mechanism, image, spokesperson, binary, proof, solution
— 3–4 sentences where every clause implies the next. If it flows and the ending
feels inevitable, the DNA rhymes — that's full lock. If you keep needing "and
also…", a dimension isn't rhyming yet (the star ingredient doesn't embody the
mechanism, the spokesperson could be swapped out, the pain and solution don't
share a root metaphor).

**Full lock is the AIM, not a pass/fail gate.** It's the dream state we reach
for — but plenty of good ads never get there, and we do NOT discount an ad,
mechanism, or seed just because it won't fully lock. Note WHERE the rhyme is
loose, tighten what's cheap to tighten, then ship the brief anyway. The test is
a compass pointing at "tighter," not a bar every brief must clear. One breath,
see how close, save.

### 3. Name + save
One file per ad: `clients/{name}/briefs/OUTCOME_Persona_Facet_Angle_FORMAT_v01.md`
— CamelCase inside fields, underscores between, broad→narrow, so a sorted
folder reads as strategy. Outcome/format from a fixed vocabulary; angle is
freeform. Example: `ESCAPE_BurntAgencyOwner_Belief_MoreClientsLie_TEXT_v01.md`

Brief file contents: the DNA block (The Image included, written out) + the
seed verbatim + links + date + `status: ready`. /produce reads The Image and
briefs it to statics/video — the picture is the through-line from brief to
creative, not a note that dies here. When /produce runs it, status flips to `written` with a
pointer to the copy file.

### 4. Hand off
Close with the list of locked briefs (full paths) and: "Ready for /produce —
which brief first?" Do not start writing.

## Rules that bite here
- Never pick the seed, the hook, or the angle FOR him. Propose, he decides.
- Concept stated flat or it isn't a concept. Angle named or it's not locked.
- Push hard for The Image. "Can you draw it on a whiteboard? Can a 10-year-old
  picture it?" If no, push the mechanism — a half-baked, un-picturable mechanism
  is the #1 killer of otherwise good copy. But like the Lock, it's an aim: if
  nothing lands after real pushing, flag it as the loosest dimension and let
  Joey decide. Never kill a brief over it.
- Proof verified with a line reference or flagged. No exceptions.
- Defaults are allowed everywhere — but say what default you applied.
- The plan yields to a great idea, never the reverse.
- No copy. Not even a "sample line to show the direction."
