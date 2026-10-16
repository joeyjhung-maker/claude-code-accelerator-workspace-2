# Google Trends rising-searches sweep

Run: 16 Oct 2026. US, Google Shopping searches, last 12 months, then 5-year shapes on the best finds.
Different from the earlier ranking: that one checked ideas we already had. This one goes looking for new ones.

## Headline
**Water is the theme.** 4 of the top 6 finds are about what's in your water:
- shower filters
- countertop filters
- portable filters
- espresso descaler

That lines up with Notion #10 (hard water) and #110 (descaler) from the first ranking. Water filtering is a whole category moving, not one product.

The hidden cause comes ready-made: "it's not your shampoo, it's your water."

## Ranked finds

Size and growth are measured against "cat water fountain", a product we know sells. Size 1.0 = same search volume.

| Rank | Product | Size | 5-year | Last 12 months | Last 3 months | Read |
|---|---|---|---|---|---|---|
| 1 | Portable water filter | 0.36 | 5.5x | **5.2x** | still rising | Fastest riser that's big enough to matter. Sawyer Mini and RV inline filters breaking out. Camping, travel and emergency prep in one product |
| 2 | Weighted sleep mask | small | 3.9x | **3.4x** | still rising | Early and speeding up. Nodpod is the brand breaking out. Light, $30–50, giftable. Fits Notion #12 (shift-worker sleep kit) as the hero item |
| 3 | Countertop water filter | 0.41 | 3.3x | +70% | dipping | Strong. Higher price and replacement filters (a refill model). Heavier than the others |
| 4 | Filtered shower head / shower filter | 0.34 / 2.4 | 4.7x / 1.6x | +24% / +19% | flat | The biggest market here, still growing. Over 10 brands broke out this year (Jolie, Afina, Filterbaby, Sonaki…), so it's proven and crowded. Cartridge refills. Hard-water story |
| 5 | Espresso machine descaler | tiny | 10x | +57% | still rising | Small but climbing. Natural subscription. Same signal as #110 in the first ranking |
| 6 | Mould remover spray | small | 1.7x | +42% | dipping | Lots of brand breakouts, but it's a liquid chemical sold by big brands. Weak for us |

### Checked and dropped
- **Sleep earbuds:** +99% last year, but it's tech. Your Notion filter excludes it.
- **Camera bird feeder:** grew 3.2x over 5 years but fell 26% last year. Peaked, and it's tech.
- **Laundry detergent sheets / non-toxic detergent:** flat and falling.
- **Natural pest control:** flat.
- **Camping heater:** falling, and a safety risk.
- **Interactive cat toy:** +40% last year, falling lately, small.
- **Car cleaning gel:** a spike that faded. Fad.
- **Cat bed for desk:** just appeared, too small to read yet. Worth a look in 3 months.
- **Elderly bed alarms and pads:** breakouts in Shopping, but too small to read on a 5-year line.

## UK and Australia check
- **Shower filters** are just as big in the UK and Australia, relative to the reference. They doubled over 5 years and were flat last year. **No lag.** Those markets have already caught up.
- **Filtered shower head, countertop filter, weighted sleep mask:** too small to read in the UK and Australia. They're US searches for now. Possibly an early window, but there's not enough data to say.
- Note: the UK says "shower head filter", not "filtered shower head". Wording matters.

## Watch-outs before anything goes further
- **Water filter claims need proof.** Saying it removes chlorine, lead or bacteria needs a real certification (NSF/ANSI) from the supplier. Only claim what the certificate says. That fits our "things we won't do" list.
- **Portable water filters are a safety product.** If it fails, someone gets sick. Certified suppliers only.
- **Shower filters:** "better hair and skin" is a health-ish claim. Keep it to what the filter removes.

## How this was done (and what went wrong)
- **Google changed something in March 2026.** Every term jumped about 3x in the same weeks, the reference product included. That's why everything looked like it had doubled in the first ranking. Fix: every product is pulled alongside the reference in the same request and measured against it week by week. The shared jump cancels out.
- **Shopping data is thin past broad terms.** Level 2 (rising searches for specific products) came back empty for most niche products. Most of the finds came from level 1.
- **Google rate-limits hard,** to about one request a minute after the first 20 or so. A full sweep takes 45–60 minutes.
- Seeds used: cat, dog, laundry, cleaning, coffee machine, water filter, sleep, elderly, apartment, pest control, mould, bird feeder, camping, baby, descaler, cat toy, shower, kitchen gadgets.

## Next
1. Decide if "water" is the lane. If yes: portable filter vs shower filter vs countertop.
2. Ad Library check on the top 4. Who's running ads, for how long, and at what price?
3. Supplier check: who sells certified versions, and at what landed cost?

Related: [[2026-10-16-google-trends-ranking]] [[research-playbook]] [[project]]
