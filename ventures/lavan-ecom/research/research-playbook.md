# Product research playbook

Stage 1 of the roadmap. Goal: 3 products that pass the filter, and you'd both buy them.

The rule: **follow money that's already being spent.**
Clever ideas are guesses. Ads that keep running are proof.

## The methods, strongest signal first

### 1. Ads that won't die (Meta Ad Library)
An ad that has run for 30+ days is almost always paying for itself. Nobody keeps funding a loser.
- Search niche keywords, plus buying words: "free shipping", "shop now", "50% off", "sold out", "back in stock".
- Filter: active ads, your target country.
- Look for: start date 30–90+ days ago, **lots of versions of the same ad** (that means they're scaling), several stores selling the same thing.
- Click through to the store. Note the price and offer.
- Who: Joey (ads are your world). Claude: `meta-ads-extractor` then `ads-analyst` to pull and break down a competitor's whole library.

### 2. Real sales data (TikTok)
The closest you get to seeing actual sales numbers for free.
- TikTok Creative Center: Top Products, Top Ads, trending hashtags. Filter by your country.
- TikTok Shop best-sellers. Paid trackers (Kalodata, FastMoss) show sales per product. Worth a one-month sub if TikTok looks promising.
- Look for: products with steady sales over weeks, not one viral spike.

### 3. Amazon
Demand plus the best free customer research there is.
- Movers & Shakers (what's climbing now) and Best Sellers in your niche.
- Lots of reviews coming in recently = selling now.
- **Read the 1–3 star reviews.** They list every defect to avoid and hand you the angle ("finally one that doesn't break after a week").
- Claude: pull and sort reviews into complaints, wishes and the words buyers use.

### 4. Look inside competitor stores
Once you've found a store selling it, see what's actually moving.
- Add `/collections/all?sort_by=best-selling` to a Shopify store's address to see their best sellers.
- Free browser extensions (Koala Inspector, PPSPY) show theme, apps and launch dates.
- Similarweb gives a rough traffic number.
- Claude: `landing-page-analysis` on their product page. What's the offer, what's the proof, what's missing.

### 5. Problems people are already moaning about (Reddit, groups, comments)
Finds demand before the ads do, and gives you the angle.
- Search: "I wish there was", "does anyone know a product that", "what's the best X for Y", "tired of".
- Subreddits for the niche, Facebook groups, comments under competitor ads.
- Claude: `last30days` (Reddit, X, web from the last month), `comment-goldmine` on competitor ad comments.

### 6. Check the trend and the supply
Do this on the shortlist, not the longlist.
- Google Trends, 5 years: climbing, flat, a fad spike, or only at Christmas?
- AliExpress / CJ Dropshipping / Alibaba: landed cost, order counts, how many suppliers.
- If it's on Temu at a quarter of your price looking identical, that's a red flag. You'll need a better version or a better angle.

### 7. Your own lives
What have you two bought that you rave about? What problem do you have that nothing fixes properly?
Weakest proof, but it gives you real belief and a story to tell. Use it to pick niches, then prove it with methods 1–4.

## The scorecard

Score each idea 1–5 on each line. Anything under 20 is out.

| Score it on | 1 | 5 |
|---|---|---|
| Proof of demand | Nobody's selling it | Ads running 60+ days, many stores |
| 3-second demo | Needs explaining | Jaw drops in one shot |
| Margin | Under 2x landed cost | 3x+ landed cost, sells for $30–80 |
| Problem or delight | Nice to have | Real pain or real "ooh" |
| Room for an angle | Everyone says the same thing | Reviews full of complaints you can fix |
| Easy to ship | Fragile, heavy, sizes, batteries | Light, tough, one size |

**Any one of these and it's out, whatever the score:**
- It needs health, medical or safety claims to sell
- Kids' safety risk, or a regulated category (supplements, cosmetics with active ingredients, anything you plug into the mains without proper marks)
- It copies a brand, a trademark or a patent
- It only sells one month a year
- You wouldn't buy it yourselves

### Example of how to score (made-up rows, not research)
| Product | Demand | Demo | Margin | Pain/delight | Angle | Ship | Total | Call |
|---|---|---|---|---|---|---|---|---|
| Example A: gadget with a clear before/after | 4 | 5 | 4 | 4 | 3 | 5 | 25 | Shortlist |
| Example B: "posture fixer" | 5 | 3 | 4 | 4 | 2 | 4 | 22 | **Out.** It only sells on health claims |

## The 5-day sprint

| Day | What | Output |
|---|---|---|
| 1 | Pick 3 niches. Write 10 keywords each | Niche list in `research/` |
| 2 | Joey sweeps the Ad Library. Lavan sweeps TikTok and Amazon. Claude sweeps Reddit and reviews | Longlist of about 30 |
| 3 | Score all 30 | Top 10 |
| 4 | Deep dive the 10: reviews, competitor stores, Trends, supplier cost | Top 3 |
| 5 | Both agree the 3. Order samples | Stage 1 gate cleared |

## Where results go
- Longlist and scores: `research/longlist.md` (or a shared Sheet if that's easier for both of you)
- Each shortlisted product: `product/{name}.md`
- The pick, and why: `decisions.md`

Related: [[project]] [[roadmap]]
