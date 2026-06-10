# The Folder Scaffold — every folder, what lives in it, and why

This is the complete annotated map of the creative-strategy workspace. The master skill creates this
on first run. It IS the system: one folder, local-first, opened in Claude Code. Each folder maps to
one of the seven node types. Build it once, then fill it node by node.

```
creative-system/                       # holds many brands
├── .claude/skills/                    # built bots become invokable (shared across brands) + bot-builder bonus
└── <brand>/                           # one per brand
    └── <product>/                     # one per product — a brand can hold MANY products
        ├── .env
        ├── profile.md
        ├── README.md
        ├── knowledge/
        │   ├── primers/
        │   │   ├── payload/
        │   │   ├── conceit/           # specific TYPES: animation · skit · podcast · pixar · thumb-war · dr-skit
        │   │   ├── hooks.md
        │   │   └── headlines.md
        │   ├── swipe-bank/            # index.md · organic/YYYY-MM-DD.md · swipes/YYYY-MM-DD.md · raw/<id>.json · README
        │   └── frameworks/
        ├── bots/
        ├── code/                      # pull_ig · pull_fb · pull_meta_report · score_ads · scrape_reviews · kie_render · format_doc · orchestrate
        ├── data/                      # …incl. seeds/YYYY-MM-DD.md (tagged)
        ├── creative/                  # refs/ · templates/ · video-references.md · YYYY-MM-DD/ (outputs + renders)
        └── surfaces/
```

Start with a single brand/product if that's all they have — just don't bake in a structure that can't
grow to more. `.claude/skills/` sits at the workspace root so built bots are shared across every brand.

---

## Per-product files (each `<brand>/<product>/`)

### `.env` — CONNECTION keys (never commit this)
All credentials live here; Claude Code and your scripts read them. Add keys only as the node that
needs them comes online — you do **not** wire everything on day one.
```
ANTHROPIC_API_KEY=        # runs the model — needed for scripting AND as the Genesis provider key
GENESIS_API_KEY=          # optional — unlocks the trained Genesis bots
GENESIS_BASE_URL=         # e.g. https://gas.copycoders.ai/api/v1
EXODUS_API_KEY=           # optional — the done-for-you Exodus pipeline
EXODUS_API_URL=           # e.g. https://good-cod-360.convex.site
META_ACCESS_TOKEN=        # Meta Marketing API — Analysis (pull) + Ship (push)
META_AD_ACCOUNT_ID=
KIE_API_KEY=              # ONE key = images (GPT-Image + Nano Banana Pro) AND video (Veo/Kling/Sora)
SCRAPECREATORS_API_KEY=   # swipes / organic pulls (paste FB/IG links → text, media, transcript)
HIGGSFIELD_API_KEY=       # optional — stylized video only
APIFY_TOKEN=              # scrape reviews / comments / ad library (Research intake)
```

### `profile.md` — the brand context (from onboarding)
The winning-ad inventory, which keys they have, and what they want first — that's the core. Brand /
product / market only if the ads actually need it (keep onboarding light). Everything downstream reads
this. Keep it short; the *ads* carry the real truth, not a fact-sheet.

### `README.md` — the operator's own map
A one-page note: where things are, which nodes are built, what's next. Their personal index.

---

## `knowledge/` — KNOWLEDGE nodes (read/injected; never act)

Plain markdown. The single highest-leverage folder in the system. Claude Code reads it straight off
disk; an Obsidian vault works equally well.

### `knowledge/primers/` — the heart of output quality
A primer = **raw winning ads + a light meta-instruction wrapper**. The ads ARE the brand truth.
Do NOT replace them with product info or buyer docs — *the only information you need is what's in the
winning ad, because it already worked.* Spend real time here; every winner you earn gets added, so
primers tighten over time (the flywheel).

Two layers, applied in sequence (not multiplied into slots):

- **`payload/`** — what to SAY, cut by **awareness × length**:
  - `long-unaware-problem.md` — 500–1500w story-driven, pattern-interrupt, education.
  - `long-solution-product.md` — comparison, differentiation, positioning, offer.
  - `short-form.md` — punchy text ads, ~50–200w.
  - `most-aware.md` — direct offer, urgency, social proof, retargeting.
- **`conceit/`** — what SHAPE to pour it into, cut by **format** (the vehicle), each a *specific TYPE*
  (a story is NOT a conceit): `animation.md`, `skit.md`, `podcast.md`, `pixar.md`, `thumb-war.md`,
  `dr-skit.md`, `cue-card.md`, `customer-call.md`, `street-interview.md`, … Each = winning ads of that
  conceit + a light wrapper (beat→structure map, voice, native hook type, visual cues).
- **`hooks.md`** — winning hooks only (the hook primer).
- **`headlines.md`** — winning headlines.

Each primer file format: 8–12 full winning ads (nothing truncated) + a short wrapper —
`use this, don't copy it exactly, copy the style` + dos/don'ts you keep updating.

### `knowledge/swipe-bank/` — STORMING-S source (a Database node)
Competitor + organic ads you admire, saved with source/links + media + transcript. Structure:
`index.md` (1-line catalog per swipe — date · platform · creator · theme · link — search across ALL
dates) · `organic/YYYY-MM-DD.md` (keep the hook verbatim) · `swipes/YYYY-MM-DD.md` (competitor FB ads,
kept separate — these get Mad-Libbed) · `raw/<shortcode|adID>.json` (full JSON, keyed by ID — no dupes /
no wasted credits) · `README.md`. Feeds ideation and the conceit primers.

### `knowledge/frameworks/` — the thinking tools (copy the whole folder from this kit)
`hook-quality.md` · `editing-rules.md` · `segments.md` · `iterations.md` · `copy-blocks.md` ·
`scrawls-statics.md` · `README.md` (the index + STORMING). CAST lives one level up at
`knowledge/02-cast-video-grammar.md`. Reference, not procedure — held for facility.
*(When scaffolding, copy the entire `frameworks/` folder as-is — don't hand-list filenames.)*

---

## `bots/` — BOT nodes (active markdown; transform input→output)

Prompt/skill files that *do*: `hook-bot.md`, `writing-bot.md`, `editing-bot.md`, `after-session.md`
(folds your edit feedback back into steer-prompts + primers), `classifier-bot.md`, `ideation-engine.md`,
`brief-builder.md`, `conceit-bot.md`. On plain Claude Code these are your writers. With a Genesis key,
the trained server bots stand in for the heavy ones (hook, writing, analysis). A bot you want to
invoke directly gets promoted to `.claude/skills/`.

> Bot vs Knowledge: both markdown. A **Bot acts** (produces output); **Knowledge informs** (gets read
> into a bot). A primer never wrote an ad — it makes the thing that writes the ad better.

---

## `code/` — CODE nodes (deterministic Python; run on demand)

Mechanical recipes that need no taste: `pull_ig.py` / `pull_fb.py` (scrape organic/swipes → text, media,
and transcript into the swipe bank), `pull_meta_report.py` (Analysis intake), `score_ads.py` (classify
by ROAS + spend), `scrape_reviews.py` (Apify → reviews/comments for new-segment mining), `kie_render.py`
(render statics/video via KIE), `format_doc.py` (finish → Google Doc), `orchestrate.py` (glue a stage
end-to-end). Run them right in
Claude Code (`run this`). Only reach for a scheduler (cron / trigger.dev) when something must run
unattended.

---

## `data/` — DATABASE nodes (queried by row; start as files)

Begin as flat files; graduate only when a Surface needs live data or scale demands it.
- `strategy-map.md` — Strategy's artifact: the living terrain of segments, coverage, and ranked gaps.
- `hypotheses.md` — Analysis bets: what won/lost and the guess why. (→ SQLite + chat/RAG when big.)
- `coverage.json` — which segments × awareness your real ads cover → where the gaps are.
- `seeds/YYYY-MM-DD.md` — every idea saved **with tags, organized by day** (Ideation output). A seed =
  the verbatim hook/swipe + a one-line description (no copywriting). Nothing here until ideation runs.
- `brief-store.md` — every brief built, saved for reuse (Ideation output).
- `visual-styles.md` — styles spotted in organic/swipes; feeds Creative (STORMING-N).
- `saved-edit-rules.md` — before/after edits worth reusing → feed back into editing steer-prompts.
- `personas/` — full Todd-Brown profiles per committed segment (key e.g. `brand-sleep-women-50`).
Ladder: files → SQLite (one local file) → Airtable/Sheets (visual) → Supabase/Convex (app-backing).

---

## `creative/` — render workspace (statics & video outputs)

`refs/` (reference images — save screenshots to a stable path here FIRST; pasted ones vanish from temp)
· `templates/` (reusable per-format static prompts with slots + a `README.md`) · `video-references.md`
(source primers for video) · `YYYY-MM-DD/` (dated prompt sets + renders). Render via `code/kie_render.py`;
full craft + endpoints in `knowledge/kie-render-reference.md`.

---

## `surfaces/` — SURFACE nodes (one HTML file; a screen you act in)

Single self-contained HTML, opened `file://`, written by Claude Code. `segment-studio.html` (map +
coverage + gaps), `editing-canvas.html` (paste an ad, steer it). Optional — much of the system runs
with no screen. Graduate to a hosted app (Netlify/Vercel + a real DB) only when it needs live data or
sharing.

---

## `.claude/skills/` — built bots become invokable, + the bot-builder

When a bot earns its keep, promote it to `.claude/skills/<name>/SKILL.md` so it's invokable across
the workspace. The **bot-builder** bonus skill lives here too — the factory that builds new
bots/skills with you. (Stub for now; built together as its own skill.)

---

## The build order (don't go left-to-right — go by leverage)

1. **First win:** paste winning ads → parse into hooks / body / headlines, demonstrate, offer Google
   Drive (no primer-building required to feel the magic).
2. `knowledge/frameworks/editing-rules.md` + `bots/editing-bot.md` → clean to voice.
3. `knowledge/swipe-bank/` → swipe-to-ad.
4. `knowledge/primers/` full library (payload + conceit).
5. `surfaces/segment-studio.html` + `data/coverage.json` → segments & gaps (Strategy).
6. `code/pull_meta_report.py` + `.env` Meta keys → Analysis (needs the connection).
7. Creative: statics (SCRAWLS) → CAST video → animation.
8. `data/` graduates, `code/orchestrate.py` wires a stage → toward Automated.

Each step is one node. Pick by what you do most / what hurts most. You never have to build it all —
and the moment a node wants to be automated/scheduled/shared is exactly where Exodus + Genesis fit.
