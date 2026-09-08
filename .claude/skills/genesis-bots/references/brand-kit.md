# The Brand Kit — build your inputs once, reuse everywhere

Most Genesis bots don't want "a product." They want *processed assets*: a buyer
profile, an offer brief, extracted copy blocks, real customer language. Across the
catalog, **108 bots consume a buyer-profile, 90 consume offer-details, 30 consume
customer-reviews, 24 consume a brand-voice.** If you generate those assets **once
per brand** and cache them, you can drive almost any bot without a cold start.

That cached bundle is the **Brand Kit**. Build it first; then every downstream bot
call is just "here's the brand kit + this one specific ask."

## The one raw input you must gather from the human

Everything else is derived. You need **source material about the offer** — as much
as exists, in rough priority order:

1. **A sales page / product page URL or its full text** (richest single source)
2. **A VSL or webinar transcript** if one exists
3. **Existing ads or emails** that already run (even screenshots/text)
4. **Customer reviews / testimonials** (Amazon, Trustpilot, site reviews, DMs)
5. **A plain description** of the product, price, and who it's for (fallback if 1–4 are thin)

Ask the user for these up front. If they only have #5, the kit still builds — quality
just scales with how much real material you feed the foundation bots.

## The 6 foundation assets (build in this order)

Each is produced by one bot. Run them once, save each output to a file, and treat
that file as a reusable asset. Foundation bots that take raw material reply to a bare
call by *asking for it* — so always pass the source material in the first message.

| # | Asset | Bot (slug) | Feed it | Save as |
|---|-------|-----------|---------|---------|
| 1 | **Offer Brief** | `offer-brief-bot` | sales page URL/text, pricing, bonuses, guarantee | `kit/offer-brief.md` |
| 2 | **Buyer Profile** | `build-a-buyer-elite-` | target market + product (from the offer brief) | `kit/buyer-profile.md` |
| 3 | **Copy Blocks** | `copy-blocks-extract` | existing sales page / VSL / emails | `kit/copy-blocks.md` |
| 4 | **Reverse Brief** | `reverse-brief-bot` | a full sales letter or VSL transcript | `kit/reverse-brief.md` |
| 5 | **Social Proof** | `social-proof-deep-research-bot` | reviews, testimonials, marketing materials | `kit/social-proof.md` |
| 6 | **Brand Voice** | `deep-dive-voice-analyzer` | a writing sample in the brand's voice | `kit/brand-voice.md` |

> Assets 1–2 are the backbone (needed by the most bots). 3–6 are high-leverage add-ons.
> If the brand has no existing copy yet, skip 3/4/6 and generate them later from whatever
> the first ad round produces — the kit is meant to grow.

### Minimal build sequence (copy/paste shape)

```bash
K=kit; mkdir -p "$K"
H=".claude/skills/genesis-bots/scripts/genesis-stream.mjs"

# 1. Offer Brief — paste everything you gathered about the offer
node "$H" offer-brief-bot  raw-offer.txt        "$K/offer-brief.md"

# 2. Buyer Profile — target_market + product; feed it the offer brief as context
node "$H" build-a-buyer-elite-  buyer-input.txt  "$K/buyer-profile.md"
#    (buyer-input.txt = "Target Market: <who>\nProduct: <paste kit/offer-brief.md>\nAnalysis Type: buyer_profile")

# 3. Copy Blocks — only if existing sales copy exists
node "$H" copy-blocks-extract  existing-copy.txt "$K/copy-blocks.md"

# 4–6 as material allows
```

## Using the kit

For any downstream bot, assemble the prompt as **kit assets + the specific ask**:

```bash
cat kit/buyer-profile.md kit/offer-brief.md kit/copy-blocks.md > _ctx.md
{ cat _ctx.md; echo; echo "TASK: write 75 ads for the Facebook feed."; } > prompt.txt
node "$H" 75-ads-template-bot prompt.txt out/75-ads.md
```

A bot only reads the asset types it cares about (`references/bots.md` lists each bot's
required/optional inputs), so over-supplying context is safe and cheaper than a
round-trip where the bot stops to ask. **When in doubt, front-load the whole kit.**

## What the kit does NOT cover (still human-supplied per task)

- **`winning-ad` / swipe** — a specific competitor or proven ad to model. 18 bots want
  one; no bot manufactures it. Keep a `kit/swipe/` folder of ads worth modeling.
- **`competitor-info`** — live competitor/market intel. Gather with web research or the
  research bots per campaign.
- **`landing-page-url`** — the destination a given asset points to; task-specific.
- **Real numbers/proof** — several bots refuse to fabricate statistics; supply real ones.
