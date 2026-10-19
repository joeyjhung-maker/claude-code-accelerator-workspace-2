# WinningHunter process (from @daily.ecommerce reel) + first sweep

Source: https://www.instagram.com/reels/DXuViMrKF3Z/ (caption plus burned-in video captions and screen footage; no audio transcript, no speech-to-text installed).
Run: 2026-10-18. US ads, first page (20 ads) only. Revenue figures are WinningHunter estimates, not facts.

## His process
1. Open WinningHunter, no filters. Looks for fresh ads the tool hasn't categorized yet.
2. Check active ad count first.
3. Skip anything that looks fake.
4. Skip brands running ads for multiple products.
5. Keep single product, one page.
6. Confirm in Meta Ad Library which ad is carrying the money, and check how long it has been running (his example: nose patch brand, ~660 ads, best ad live since Nov 2025).
7. Open the store page, check the page and the ad angle.
His rejected example: pet supplement brand, 331 ads, good page, too many products.

## Update: audio transcripts (reel 1 and a second reel, instagram.com/reel/Deb3uvzsVj9/)
Reel 1 audio matches the caption. "Fresh" means the tool's own default feed: he leaves filters empty on purpose so WinningHunter's ranking surfaces new finds on top. It is not a date filter.
Reel 2 adds:
- His one rule: active ads. He only reads the black pill showing how many ads a brand runs. Everything else is a reject check after that.
- Reject example: 943 ads, mini glass bouquet, but the store launches 50-100 random products a month. Not a single-product business.
- Accept example: 350 ads, all going to one product. "Clarity."
- He found a claimed $14M/month one-product store by asking Claude (via the WinningHunter connector): find one-product businesses that are crushing it, for Q4. He took the second result and opened it in WinningHunter. His number, unverified.
- Correction to the sweep below: I sorted by longest running, which is the opposite of his fresh-first view. Rerun with default sort.

## Mapping to the tools
- find_winning_products: forces active + winning + product pages, auto-applies min 50 active ads for US.
- max_products_on_store=3 is the single-product filter. 934 matches with min_active_ads=100.
- get_store_details: product count, est. 30d revenue, traffic trend, Trustpilot complaints.
- get_store_top_ads: longest-running ad per store.

## First sweep (max 3 products, 100+ active ads, longest running)
| Store | Product | Active ads | Est. 30d revenue | Note |
|---|---|---|---|---|
| oliviablaire.com | Iron Wand Mascara, $24.95 | 184 | $240K-600K | 1 product. Reviews: doesn't hold curl, refund trouble, review gating |
| peasmaker.nl | Plant-based pieces, ~EUR 35 | 243 | EUR 500K-900K | NL/BE only. Traffic 31K (Mar) to 99K (Sep) |
| wowcombo.com | Mascara, $18 | 126 | $560K-1M | Complaints: clumping, ads over-promise |
| snuuzu.com | Tesla car mattress, ~$900 | 108 | $175K-300K | High ticket, 2 models |
| shopnovahair.com | Instant dye shampoo | 145 | $1K-2K | Traffic collapsed to ~800 visits. Ad count lying. REJECT |
| jawliner.com | Hard gum, $24.95 | 90 | $700K-1.3M | 34 products on store. Fails strict single-product |

## Rerun his way (default sort, max 3 products, no other filters): 5,207 matches, first 20 ads
| Store | Product | Active ads | Traffic / est. revenue | Verdict |
|---|---|---|---|---|
| scandilights.fi | LED wall lights (4 listed) | 842 | 2.2K visits, $0 est. | Multi-product, tiny traffic. Reject |
| heektor.pl | Heektor V2 (3 listings, same product), 79 zl | 367 | 117K visits Jul to 21K Sep; $48-85K/30d | Real but fading, Poland only |
| weartitans.com | Leakproof boxers, $32 | 286 | store made Jul 2026, no traffic data | Unverified |
| biolabs.se | Turmeric curcumin, 299 kr | 278 | no traffic data | Unverified, supplement claims risk |
| hairfix.store | Hair tool, EUR 36 | 170 | 865 visits, $0 est. | Reject |
Pattern: the default feed is mostly small non-US markets (FI, SE, PL) and brand-new stores with no traffic history. High ad count alone did not mean money.

## US sweep (US, 100+ active ads, max 3 products, 1,000+ monthly visits): 691 matches, first 20 ads
| Store | Product | Active ads | Traffic | Est. 30d revenue | Verdict |
|---|---|---|---|---|---|
| avernio.com | Travel sleep gadgets (4-5 products) | 182 | 2.4K (May) to 48K (Sep), 100% US | $350-650K | Best momentum, fails single-product. Reviews: product differs from ads, missing deliveries |
| maclir.co | Creatine gummies, EUR 40 | 124 | 1.8K (Jul) to 14.5K (Sep), 100% Ireland | $70-130K | Single product, growing, but not US and health-claims product |
| ouvra.store | Car locks, GBP 34-44 | 163 | 178K (Dec) to 40K (Sep) | $79-157K | Declining. Lock jams in seatbelt buckle reviews |
| aurkina.com | Supplements | 111 | ~4K | $6-10K | Too small, 4 products listed |
No clean winner on page one: none is single-product, US, growing and low-risk together.

## Read for Lavan
- Use as a demand signal, not a clone list. Our ground rules rule out copying over-promising claims and review gating.
- Next run: set price band, US only, ads started in the last 90 days, then do his Meta Ad Library check per store.

Related: [[Lavan Ecom Test]] [[Promotion]]

## Search A: rising one-product US stores (run 2026-10-18)
Filters: Shopify store search, US main visitor country, max 5 products, min $100K est. 30d revenue, traffic up 100%+ over 3 months, sorted by 3-month growth. One run each for Health, Beauty, Pet Supplies (15 results max each).

| Store | Product | Active ads | Traffic | Est. 30d revenue | Read |
|---|---|---|---|---|---|
| lymphoria.co | Lymphatic drainage drops, $39.99 | 4,240 | 350K (Apr) to 5.4M (Sep) | $32-58M | Biggest find. Same lymphatic theme as Endo Sculptor |
| primal-storm.com | Men's supplement (+ ashwagandha) | 2,225, rising | 59K (Jul) to 878K | $5.2-9.5M | Strong, scaling now |
| flowpouch.com | Flavoured pouches, $20 | 157 | 25K (Apr) to 426K | $2.7-5.2M | Fast growth; check what the pouch is |
| auniva.co | Amla, garlic, pomegranate capsules | 1,870 | 228K | $1.2-2.5M | Older-buyer supplement, 4.5 on 1,595 Trustpilot reviews |
| officialmeimei.com | K-beauty NAD+ firming serum, $45 | 666, rising | 15K (Jul) to 213K | $1.5-2.7M | Fresh, anti-aging for women |
| skinklean.co | EMS + LED sculpting belt, $249 | 833, rising | 27K (Jul) to 219K | $1.1-1.9M | High-ticket device |
| trysleepease.co | Anti-snoring device, $299 + patches | 441 | 10K (May) to 126K | $720K-1.35M | Steady climb |
| trypeakflex.com | Knee sleeve, $60-70 | 191 | 0 (Jun) to 68K | $550-950K | No-claim product; ads mostly target AT/DE |
| pawsylabs.com | Parasite cleanse drops for pets, $42 | 87 | 44K, flat | $180-360K | Human product repositioned for pets |
Dropped: holior.com and studiodermal.com (traffic falling month on month), holisticnex.com (only 12 ads left), smaller stores under 100 ads.
Pets lane is thin: no pet store has big ad volume yet.
WinningHunter's daily ad counts jump around (Lymphoria shows 2 ads on one day, 4,240 a week later), so read the trend, not one day.

## The list now lives in the Google Sheet
"daily.ecommerce: brands and products he showcases". Product finds tab: 40 single-product stores (5 or fewer live listings). Multi-product tab: 28 stores that failed the live check.
Rule learned: never trust WinningHunter's product count. Check `/products.json` on the live store (Holdmate slipped through on the tool's number).

## Other channels tried (2026-10-18)
- Funnel search, live ads only (last seen in the past 7 days): only 3 advertisers. Primal Storm (already listed), OrthoFit (10 listings), Uproot Clean (91). The first run forgot the live-only filter and returned dead ads.
- TikTok Shop, sorted by revenue growth, min $150K: almost all big multi-SKU brands. That was the wrong sort, not a dead channel.
- TikTok Shop done right: `search_tiktok_shops` sort_by=product_count asc, min_revenue=50000. First 2 pages = ~70 shops with 1-2 products doing $50K+/30d. Then `get_tiktok_shop` slice=products to see the actual product. 10 added to Product finds (rows 45-54). TikTok shops have no store domain, so the live check doesn't apply; the link is the WinningHunter shop page.
- Google ads: keyword search is fuzzy and mostly returns big brands. A few small advertisers surfaced (Cata-Kor, Serlino Lab, Contours Rx) but all failed the live check.
- YouTube: `search_google_ads` with format=video, US, live, 30+ days running. With no keyword the results are mostly political ads. Keyword search is fuzzy ("doctor" matched "door" and "decor"). Out of 17 small advertisers checked, 3 passed: Attaboy (one supplement, peaked in July), MosquitoNix (one mister, seasonal) and LiceGuard (tiny).
Verdict: Meta (Shopify store search plus the live check) and TikTok Shop (sorted by fewest products) both find one-product stores. Google and YouTube are thin; use them to check demand for a product we've already picked.
