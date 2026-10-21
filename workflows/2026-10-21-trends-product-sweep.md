# Google Trends product sweep

Related: [[Promotion]] [[research-playbook]] [[2026-10-16-trends-rising-sweep]]

## The play
Use Trends to find products, not just to check ideas we already have.

1. **Seeds.** 15–20 problem areas, not single products (cat, laundry, sleep, shower, pest control…).
2. **Rising searches.** Google Shopping only, US, last 12 months. Shopping counts buyers, not readers.
3. **Dig.** Take each product-looking rising search and pull its rising searches too.
4. **Filter.** Drop brands, staples (food, litter), heavy or sized items, regulated items, and anything that fails the Notion filter (felt problem, hidden cause).
5. **Shape.** Pull 5 years for each survivor, **in the same chart as a reference product** ("cat water fountain"). Measure it against the reference week by week.
6. **Country lag.** Same check in the UK and Australia, with the same reference.
7. **Write up** in the venture's `research/` folder: size, 5-year, last 12 months, last 3 months, peak month, one-line read.

## Why the reference product matters
- In March 2026 every search term jumped about 3x in the same weeks, the reference included. That's Google's data, not demand.
- Without a reference, everything looks like it doubled. The first ranking (16 Oct) got fooled.
- Measuring against a reference in the same request cancels it out.

## What to expect
- Claude pulls the data from inside trends.google.com in the browser (the explore → widget data endpoints). No paid tool needed.
- Google allows about 20 quick requests, then roughly one a minute. Space them 12s+ apart, and wait 60s after a "too many requests" error. A full sweep takes 45–60 minutes.
- Level 2 (digging) mostly comes back empty on Shopping. Most finds come from level 1.
- Broad terms ("emergency kit", "food allergy") are huge because they catch everyone. Don't trust their size.
- Tiny terms (mostly zeros) are noise. Check those on Amazon or the Ad Library.
- Trends shows interest, not sales. The Ad Library check comes next.

## Run so far
- 16 Oct 2026: 46-idea ranking, then an 18-seed sweep. Found the water lane (portable, countertop and shower filters, descaler) and weighted sleep masks.
