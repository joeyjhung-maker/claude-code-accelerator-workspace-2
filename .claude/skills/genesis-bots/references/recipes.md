# Chains & Recipes — stringing bots together

Genesis bots are designed to hand off. One bot's output is the next bot's input.
This file gives proven chains. All assume you've built the [Brand Kit](brand-kit.md)
(`kit/offer-brief.md`, `kit/buyer-profile.md`, etc.) — most chains start from it.

`H=.claude/skills/genesis-bots/scripts/genesis-stream.mjs` in the examples.
**Bots run one stream at a time per key** — chain steps are naturally sequential.

## How to read a chain

Each step is `bot-slug —(produces)→ next bot`. To wire two bots by hand: take the
output file of the first, `cat` it (plus any brand-kit context) into the prompt file
of the second. The receiving bot's server-side prompt knows how to parse it.

---

## Recipe 1 — Cold offer → full static-ad set (the everyday path)

Goal: brand new product, no assets yet, want a batch of static ad concepts to test.

```
raw offer material
  └─ offer-brief-bot            → kit/offer-brief.md
       └─ build-a-buyer-elite-  → kit/buyer-profile.md
            └─ master-concept-bot         → concepts.md   (angles/big ideas)
                 └─ universal-static-idea-generator → picks formats per concept
                      └─ <format bot>       → final image-gen prompts
```

The last step routes to a specific statics bot by format — e.g. `meme-style-ad-concept-generator-bot`,
`scientific-study-bot`, `side-by-sidebefore-and-after-bot-`, `note-from-founder-bot-`.
See `index.md` → *Image Prompts — Statics* for the full menu. Every statics bot happily
takes the buyer profile + offer brief as optional context and produces better concepts with it.

## Recipe 2 — Offer → 75 ads (copywriting workhorse)

```
kit/offer-brief.md + kit/buyer-profile.md (+ kit/copy-blocks.md if you have it)
  └─ 75-ads-template-bot   → 75 ads
       └─ ad-tagging-bot-   → tags/sorts them by angle
       └─ bionic-bullet-bot → mines the best lines into bullet variations
```

`75-ads-template-bot` explicitly asks for offer details + audience + proof + existing
copy on a bare call — so front-load the kit and it generates all 75 immediately.

## Recipe 3 — Existing sales page → advertorial → bridge page

```
sales page URL/text
  └─ reverse-brief-bot   → kit/reverse-brief.md   (deconstructs the winning structure)
       └─ advertorial-bot / advertorial-architect → advertorial.md
            └─ bridge-page-bot → pre-sell page that hands off to the offer
```

`advertorial-architect` is interview-first (asks 6 things); `advertorial-bot` is one-shot
(front-load product info + audience + the driving ad + destination). Pick by whether you
want to answer questions or dump context.

## Recipe 4 — Video / VSL pipeline

```
kit/buyer-profile.md + kit/offer-brief.md
  └─ microvsl            → micro-VSL scripts   (wants buyer profile + reverse brief + funnel context)
       └─ in-feed-vsl-bot / video-adscript-bot → platform-specific cuts
```

## Recipe 5 — Email

```
kit/copy-blocks.md (or kit/offer-brief.md)
  └─ click-drivers-aem / universal-email-bot → email bodies
       └─ subject-line-bot → subject lines for each   (feed it the copy blocks + core ideas)
```
`universal-email-bot` appends an emoji "adjust this email" menu after each email — strip it
before saving. `mariobot` (email) is genuinely interview-first: it asks ~5 questions first.

## Recipe 6 — Voice-matched everything

```
a writing sample in the brand's voice
  └─ deep-dive-voice-analyzer → kit/brand-voice.md
       └─ voice-mod-bot        → VOICE_MOD_[ID] token
            └─ (paste that token alongside any copy bot's input to shift its voice)
```

---

## Chain-building rules of thumb

- **Backbone first.** `offer-brief` and `buyer-profile` unlock the most bots — build
  them before anything else.
- **A bot that stops to ask is telling you its dependency.** Its question *is* the
  spec for what to feed it — grab that from the kit or an upstream bot and retry in one shot.
- **Over-supply context freely.** Bots ignore asset types they don't use; a round-trip
  costs more than extra tokens.
- **Don't fabricate proof.** Several bots refuse invented statistics/testimonials — pull
  real ones via `social-proof-deep-research-bot` or from the user.
- **Producer lookup:** to satisfy any required input, `references/chains-data.md` lists
  which bots produce each asset type. If a type has no producer, it's user/research-supplied.
