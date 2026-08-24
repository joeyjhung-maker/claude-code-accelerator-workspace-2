---
name: storm
description: The STORMING ideation run — fill the seed bank. Use when Joey says "storm", "run storming", "find seeds", "ideation run", or has a Production Plan that needs ideas. Pulls from the 8 STORMING sources (swipes, templates, organic, research, matrix, internal vectors, new styles, gambits), producing seeds — verbatim hook/swipe + one-line idea — saved tagged to the client's seed bank. No copywriting, no brief-building; the output is a seed pile for /brief to pick from.
---

# /storm — pull wide, save everything, brief the best (later)

You don't invent in a vacuum and you don't map all of creative space.
You raid live sources and diversity falls out. The output of this skill is
**seeds**, nothing more.

**A seed = the verbatim hook or swipe + a one-line description of the idea.
NOTHING ELSE.** The moment you start writing the ad inside a seed, you've
jumped the gun. You are not a copywriter here.

## The run

### 1. Client, mode, target
Load `clients/{name}/` — strategy-map.md, hypotheses.md, the latest
`account-reads/` plan if one exists, and `parsed-hooks-bodies-headlines.md`.

Ask which mode (or read it from what Joey says):
- **Pointed** — the plan pulls: "I need 3 unaware ads for {segment}." Sources
  get aimed at that order.
- **Open** — fishing for bangers. Walk more doors, wider net, and a great find
  is allowed to bend the plan.

**The inventory is the clock.** If a Production Plan exists, its ad count is
the stop condition — once seeds cover N, stop and point at /brief. No plan?
Ask roughly how many seeds he wants before we call it (default: 20–40).

### 2. Walk the doors
Never say a source is "blocked." Explain how it runs, what he can paste, and
what a key would unlock — then offer to wire it. Push every source 2–3
passes; the first pass is always the boring one.

- **S — Swipes** (competitor ads, these get Mad-Libbed later)
  Paste FB Ad Library links or ad text/screenshots; or run meta-ads-extractor
  on a competitor page. Save the asset, not just the hook — full text +
  link into `clients/{name}/swipe-bank/swipes/YYYY-MM-DD.md`. Longevity is
  the tell: months running = money.
- **T — Templates** (proven shapes, filled with this brand)
  Genesis: `python3 scripts/run_genesis.py --bot 75-ads-template-bot` with a
  winning ad as primer. No key handy → run template shapes locally.
- **O — Organic** (different incentives, faster signal)
  Paste reels/posts/screenshots. Video → facebook-transcriber for the spoken
  transcript (the hook comes from the transcript, not the caption line). Keep
  verbatim → `swipe-bank/organic/YYYY-MM-DD.md`. Organic seeds keep their
  exact hook downstream.
- **R — Research** (the market's own words)
  Paste comments/reviews, or run hook-miner when he wants a full mined sweep.
  3-star reviews are gold — they list exactly what failed.
  Two moves live here before you pull hooks:
  - **Map the belief system first — "what do these people believe?"** You can't
    write an unaware/problem ad without it. Get the audience's existing beliefs
    and fears on the table, then aim: VALIDATE their worldview (nodding, "finally
    someone gets it") or CHALLENGE it (heated, "that's wrong") — both drive
    engagement, flat neither. For unaware seeds, tag the belief the seed is
    validating or challenging so /brief can lock it. `brand/concepts-and-angles.md`'s
    Avatar Facts (self-concept beliefs, pain matrix, core wound) and Psychology
    Toolkit (the 7 critical beliefs) sections are the structured version of this
    step when nothing's pasted yet — use them to shape WHICH beliefs to go dig
    for, not to invent beliefs wholesale.
  - **Go deep on the trigger words.** Pull `clients/{name}/trigger-words.md`
    (the words that keep earning engagement — /account-read fills the
    conversion side, the Monday competitor sweep fills the spend side; a word
    on BOTH sides goes first). For each one, mine the
    history, tribal references, conspiracy and suppression angles around that
    EXACT word — that's the raw material for the suppression/zeitgeist angle
    families below.
- **M — Matrix** (chad logic poured into the gaps)
  The strategy-map gaps + the plan's openings. For each gap: state the gap,
  give ONE sample concept to illustrate, stop. Never pick the type or hook
  for him.
- **I — Internal vectors** (patterns across his own winners)
  Genesis: `insight-vectors-bot` via run_genesis.py over the whole winners
  corpus — not just this week's batch. Or do the pattern read manually from
  parsed-hooks-bodies-headlines.md.
- **N — New styles** (visual formats nobody's running yet)
  Anything spotted while looking → one line each into
  `clients/{name}/swipe-bank/visual-styles.md`. This branch feeds /statics
  and /video, not copy.
- **G — Gambits** (wildcards, longer shots)
  Fed by hypotheses.md + comments. Label them gambits so the risk is priced in.

### The saffron move — one mechanism, many angles
The most reliable way to fill a bank isn't 30 mechanisms with 1 angle each.
It's ONE proven mechanism milked for 30 angles. (The doc's saffron seller:
one Amazon supplement, one mechanism, 344k followers — a different trending
problem tied to the same pill every day. Parasites. Menopause. Hair loss.
Cortisol. Belly fat. Same product, same mechanism, new door each time.)

So when a winner or a client mechanism is working, don't hunt for a new one —
run it through the angle families below and each pass drops a fresh seed.
This is the engine of the iterate-on-a-winner loop. The student's usual
mistake is the opposite: 3 mechanisms and 1 angle, when they need 1 mechanism
and 30 angles.

**Angle families** (the doors INTO one mechanism — name the family on the seed):
- **Cause-effect flip** — the good thing they do that quietly makes it worse
  (the healthy habit, the supplement they already take, that's backfiring).
- **Bad-thing-that's-actually-good** — reframe a feared symptom/trait as the
  signal it's working, or the hidden advantage.
- **Star-ingredient / differentiator** — pick the ONE weird element (not the
  most effective — the most CURIOUS) and build the whole angle on it.
- **Zeitgeist entry** — bolt the mechanism onto a conversation already running
  this week (a trend, a news story, a thing the market is already arguing about).
- **Suppression / hidden-history** — who buried it, who profits from you not
  knowing, the patent/ritual/scandal that makes it feel discovered not sold.
- **Identity / archetype** — aim the same mechanism at a different persona's
  self-image (the prepared parent, the smart-not-crazy one, the accidental winner).
- **New mental picture** — same mechanism, a different single image to draw it
  (this branch feeds The Image field the brief will lock).

Run a working mechanism through 4–5 families in one pass; that's 4–5 seeds,
each tagged with its family, none of them a new mechanism.

### The fact-pantry move — one FACT, many angles
A second multiplication engine, parallel to the saffron move. Where saffron milks a
proven MECHANISM across angle families, this one milks a single AVATAR/MARKET/PRODUCT
FACT across the full angle taxonomy in `brand/concepts-and-angles.md` — the fact-
collection + angles system (Avatar Facts, Market Facts, Product Facts, Psychology
Toolkit, and a large Angles Taxonomy with worked examples like Conspiracy, Geographic,
Accidental Discovery, Countdown, Enemy Admission).

Use it when the R or M doors need fresh raw material and nothing's been pasted yet:
1. Pick ONE already-established fact for this client — a pain/desire outcome from
   strategy-map.md, a belief from a research pull, a core-wound read if one exists.
   Never invent a fact that isn't already grounded in something the client said or
   something pasted from the market.
2. Run that ONE fact through 4–5 angle types from the taxonomy (pick types that fit
   the fact, don't force all of them).
3. Tag each resulting seed `[family: <angle-type-name>]`, same convention as saffron
   families, so /brief can see which angle did the work.

This is a technique, not a 9th door — it feeds seeds into whichever door you're
already walking (usually R for belief-mapping, M for gap-filling), never invents
market language on its own.

### 3. Save the seeds
Every seed, no matter the door, lands in
`clients/{name}/seeds/YYYY-MM-DD.md`:

```
## S3 [source: swipe] [segment: burnt-out lead-gen owners] [awareness: problem] [gap: CRM-as-asset]
Hook (verbatim): "..."
Idea: one line.
Link: <og-link if any>
```

Two optional tags when they apply (both get locked downstream in /brief):
- `[belief: validates|challenges "the market's belief, quoted"]` — required on
  unaware/problem seeds from the R-door.
- `[family: cause-effect-flip]` — when the seed came from a saffron-move pass,
  name its angle family.

Numbered so Joey can pick by number in /brief. Tags make the bank searchable
later ("show me every seed for {segment}").

### 4. Present + hand off
Show **ALL seeds in one flat list** — every one, copy-paste-able, no indents,
no decoration, no "best four." Joey's eye does the filtering; that's the
human flywheel turning.

If a door surfaced a genuinely NEW outcome or segment, propose adding it to
strategy-map.md — propose, don't write it in.

Close: "Seed bank has N. Pick numbers when you're ready to brief —
that's /brief." Do not start briefing in this run.

## Rules that bite here
- Seeds stay small. Verbatim + one line. No copy, no "improved" hooks.
- Full lists, all at once. Never sample.
- The allocation mix guides which doors get weight — it is never stamped
  onto a seed.
- Organic ≠ swipe. Organic keeps its exact hook, swipes get Mad-Libbed —
  mark the source on every seed because it routes the work downstream.
- Never invent market language. If a door needs material he hasn't pasted
  and no tool is wired, say what would unlock it and move to the next door.
- Save raw pulls to the swipe-bank so credits/effort are never spent twice.
