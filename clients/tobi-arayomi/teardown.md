---
title: Business Teardown — The Watch Global + The TAP Institute
subject: Apostle Tobi Arayomi
status: prospect — internal audit, not client-facing
created: 2026-08-14
updated: 2026-08-14
skill: business-teardown (Second Brain)
---

# Business Teardown — The Watch Global + The TAP Institute

Internal. Not for sending. Run via the `business-teardown` skill, routed through the NHB/FF market-research wiki.

**Evidence tags:** `[OBSERVED]` = seen live or returned by a probe · `[INFERRED]` = reasoned, reasoning shown · `[UNKNOWN]` = flagged, never filled in.

**Scope:** the two commercial arms. Light London / Light V (the charity) and Verge are context only — see §10 for why that boundary matters.

Companion: [recon.md](recon.md).

---

# PASS 1 — MAP

## 1. Entities

| Entity | What it is | Status |
|---|---|---|
| **The Watch Global** | Prophetic training platform. Founded June 2022 by Tobi Arayomi; run day-to-day by Prophet Mutsa Samuwi | `[OBSERVED]` Live, fully productised |
| **The TAP Institute** | Entrepreneur/marketplace mentorship. Tobi is CEO, co-pioneered with Nicola | `[OBSERVED]` **Website offline** |
| Light London / Light V | Church network, charity 1171102, campuses across 6+ territories | Context only |
| Verge | Annual apostolic conference | Context only |

`[OBSERVED]` **Tobi Arayomi ≠ Tomi Arayomi** (RIG Nation, Houston). Different men, different ministries. Corrected in the Second Brain wiki on 2026-08-14.

## 2. Surface inventory

`[OBSERVED]` HTTP sweep, 2026-08-14, `curl -L`:

| Surface | Status |
|---|---|
| thewatchglobal.com/ | 200 |
| /store *(the ladder)* | 200 |
| /prophetic-words · /monk · /hope · /prayer-polis | 200 |
| /ebook-opt-in · /contact | 200 |
| **/prophet-school** | **404** ← hero CTA target |
| /login | 403 |
| **www.thetapinstitute.org** | **No DNS record at all** |
| **thetapinstitute.org** (apex) | **TLS handshake failure (alert 40); plain HTTP returns 409** |

Other surfaces `[OBSERVED]`: Telegram (7,500+, self-stated) · YouTube (Tobi Arayomi + Light London channels) · Instagram @tobiarayomi, @lightldn, @thetapinstitute, @tapreports · TikTok · Spotify · media credits TBN UK, and per their own copy BBC and Revelation TV.

`[UNKNOWN]` — **every audience number except Telegram.** YouTube sits behind a consent wall that wouldn't take input through the tooling; Social Blade and vidIQ both 403'd. This is the first thing to establish.

`[UNKNOWN]` — **paid acquisition.** No evidence found either way; Meta Ad Library unreachable from this network.

## 3. Money map

`[OBSERVED]` Two parallel rails on the same page.

**Rail A — Membership (access):**

| Tier | Monthly | Annual | Adds |
|---|---|---|---|
| WATCH+ | £49 | £490 | All courses, member library |
| WATCH COMMUNITY *("Most Popular")* | £149 | £1,490 | Bi-monthly Zoom w/ Prophet Mutsa & team, activations + Q&A, priority prayer/testimony room, challenges + cohorts |
| THE HIVE (Inner Circle) | £399 | £3,990 | Quarterly Zoom w/ Apostle Tobi & guests, priority hot seat, early access, BTS briefings |

**Rail B — Partnership (support):** Supporter £25/mo · Builder £50/mo · Kingdom Partner £99/mo.

Their framing: *"Partnership Supports the Mission. Membership Provides Access and Structured Training."*

**Annual pricing = 10 months for 12** across all three tiers (£588→£490, £1,788→£1,490, £4,788→£3,990). `[OBSERVED]` Consistent. **Never stated as a saving anywhere on the page.**

**Access equity:** "Emerging Nations Access" — regionally adjusted pricing by application for lower-income economies or genuine hardship.

**Load-bearing rail:** `[INFERRED]` Rail A. It's the only one with structure, tiering, and a product behind it. `[UNKNOWN]` — actual revenue split.

## 4. Offer ladder

**Bottom — a hole.** Free ebook → free Telegram → **£49/mo**. `[OBSERVED]` Nothing paid in between. No tripwire, no one-off, no self-liquidating entry.

**Middle — sound.** £49 → £149 → £399 is a clean 3x/2.7x progression, and each rung adds a genuinely different *kind* of thing (content → community + facilitator access → founder access). That's well built.

**Top — stops dead at £3,990/yr.** `[OBSERVED]` No high-ticket, no 1:1, no done-with-you, no mastermind, no certification/licensing above The Hive.

**Format problem** — via `[[hierarchy-of-value]]`: WATCH+ sells *courses and a library*. That's the high-customer-energy end of the format ladder — the member does all the work of reading, interpreting and applying. The doctrine is explicit that this caps price elasticity at the bottom. £49/mo for self-serve content is priced above what the format normally sustains, while The Hive at £399 delivers four founder touches a year. **The energy-to-price curve is inverted at both ends.**

## 5. Attention engine

`[OBSERVED — Social Blade, 2026-08-14]` The audience is far larger than the recon assumed.

| Surface | Size | Activity |
|---|---|---|
| **Instagram @tobiarayomi** | **281K followers** | 2.8K posts · 0.45% ER · ~1.2K avg likes, 66 avg comments |
| **YouTube "Tobi Arayomi"** (@tobiarayomiproductions) | **108K subs · 8.4M lifetime views · 674 videos** | Created **Jul 2022** · ~375K views/mo · 13 uploads in 14 days |
| Instagram @lightldn | 26K followers | 2.3K posts · **1.1% ER** · 263 avg likes |
| YouTube "Light Ldn" (@lightldn) | 16.3K subs · 912K views · 301 videos | Created **Nov 2016** · ~6K views/mo — near dormant |
| YouTube "Nicola Arayomi" (@nickellabian) | 15.8K subs · 993K views · **28 videos** | Created 2011 · dormant · **~35K views/video** |
| Telegram (The Watch) | 7,500+ | Live prayer, fasting, teaching |
| @thetapinstitute (IG) | Not indexed by Social Blade | — |

**Three things fall straight out of this table.**

**(a) The attention is on the man, not the institution.** Tobi's personal channel launched in **2022**; the church channel launched in **2016**. The younger channel has **6.6x the subscribers and roughly 60x the monthly views.** `[INFERRED]` Six extra years of head start counted for nothing. This is `[[brand-vs-personality-and-recurring-problems]]` in hard numbers — and it means every acquisition lever runs through him personally.

**(b) The Telegram is 2.7% of the Instagram following.** `[OBSERVED]` 7,500 vs 281K. The community that the £49 product is sold into is a rounding error against the audience that exists. Via `[[converting-audiences]]`, this is the already-in-motion audience the doctrine says is the cheapest thing in marketing to redirect — and 97% of it has never been asked.

**(c) The church account out-engages the personal account 2.4:1** (1.1% vs 0.45% ER) on a tenth of the followers. `[INFERRED]` The 281K is broader and cooler; the 26K is smaller and hotter. Those two audiences want different things and should not receive the same message.

**Nicola is an idle asset.** `[OBSERVED]` 28 videos, 993K views — ~35K views per video, versus Tobi's ~12.5K lifetime average. **Roughly 2.8x his per-video pull, on 1/24th the output.** Whatever she does on camera works, and she does almost none of it.

`[OBSERVED]` Owned: email list (size unknown), the sites. Rented: everything above.

`[INFERRED]` The whole business is downstream of Tobi's speaking and media presence. Via `[[converting-audiences]]`, this is the classic already-in-motion audience — people who have done the hard work of getting into motion around the prophetic, and who follow him specifically. The doctrine's line is that redirecting existing motion is far cheaper than starting it. **The Watch exists precisely to do that. Whether it's actually doing it is unmeasurable from outside.**

`[OBSERVED]` The Telegram is described as carrying "prayer, fasting and prophetic live teachings" — i.e. **live, recurring, experiential contact with 7,500 people.** Via `[[levels-of-trust]]`, that is Level 5 (Experience), the most effective and most expensive level to reach. They already have it. It is not visibly wired to the ladder.

## 5b. What the audience was actually built on

`[OBSERVED — yt-dlp, 25 most recent long-form uploads, 2026-04-18 → 2026-08-12]`

| Views | Date | Title |
|---:|---|---|
| 82,702 | Apr 18 | What Western Media Won't Tell You About Iran |
| 46,814 | Aug 4 | They Took Our Crown \| The Queen of Warri Tells Her Story |
| **37,026** | Jul 1 | **Mastering Meditation: Everything You Need to Know** |
| 29,099 | Jul 2 | What God Showed Me About Tommy Robinson |
| 19,763 | Jun 11 | What God Told Me About Aliens Will Shock You |
| **19,606** | Jul 4 | **Mastering Meditation: I Met a Man of God in the Spirit…** |
| 18,104 | Jul 22 | Islam's Own Sources vs. the 'Religion of Peace' Narrative \| Part One |
| 17,276 | May 8 | KIER STARMER: Child Of Davos |
| 16,611 | May 13 | The Demonic System Behind Labour's Collapse |
| … | | |
| 4,384 | Aug 5 | Is the Quran 'Letter Perfect'? Ask the Ashes \| **Part Two** |
| 4,198 | Aug 7 | Fauci LIED To The World and Now He's In Trouble |

Total across the 25: **443,409 views, averaging 17,736** — **42% above the channel's 12,472 lifetime average.** The channel is getting better, not decaying.

*Caveat: raw view counts favour older videos. April uploads have had four months to accumulate; August uploads have had days. Treat the ordering as directional, not a clean ranking.*

**The dominant content is geopolitical and discernment commentary, not prophetic training.** Iran, Tony Blair, Starmer/Davos, MKUltra, Fauci, Epstein, Tommy Robinson, "Who Actually Runs Britain." `[INFERRED]` The 281K/108K audience was largely assembled by a Christian-discernment-on-current-events promise. The product it's being sold — structured prophetic formation at £49/mo — is a different purchase. Via `[[criteria-of-markets]]` and `[[levels-of-awareness]]`, **there is a real gap between what the audience showed up for and what the store page asks them to buy.**

**But the bridge exists, and it outperforms.** Both "Mastering Meditation" videos land in the top six (37,026 and 19,606). "Prophets Have Access To A Cloud System," "How I Meditate to Enter the Spirit," "You MUST know these truths when facing spiritual warfare" are all in the recent set. **This is the seam** — content that is both native to the channel and directly upstream of Prophet School. And the existing lead magnet, *"7 Ways God Speaks,"* is aimed at exactly this seam. `[INFERRED]` The magnet is right. What's missing is the routing from the videos that earn the attention to the magnet that captures it.

**Series drop-off is severe.** `[OBSERVED]` Islam Part One: 18,104. Part Two: 4,384. **A 76% fall between two halves of one argument.** Whatever is happening between parts — titling, thumbnail, no in-video handoff, gap between uploads — is losing three quarters of an already-committed audience.

**The channel is monetised at approximately zero.** `[OBSERVED]` Social Blade estimates $2–$38/day in ad revenue against ~375K monthly views. `[INFERRED]` That attention is currently worth more as a traffic asset than it will ever be worth as AdSense, and it is not being used as one.

**They are not short of production capacity.** `[OBSERVED]` 13 uploads in 14 days per Social Blade, against 5 long-form videos in the same window per yt-dlp. `[INFERRED]` The difference is Shorts and live streams — so there's an existing high-cadence content operation. Creative testing would not be starting from zero.

## 6. Funnel joins

Walking it click by click `[OBSERVED]`:

1. **Attention** → social/YouTube/speaking.
2. **Capture** → `/ebook-opt-in`, "7 Ways God Speaks." Page is a headline, a subhead, an email field and a **required country dropdown with ~250 options**. On a two-field opt-in, that dropdown is the heaviest element on the page.
3. **Nurture** → Telegram (rented, no export, no segmentation) and presumably email `[UNKNOWN]`.
4. **Offer** → `/store`. **The hero CTA on the homepage points at `/prophet-school`, which 404s.** The nav item *labelled* "PROPHET SCHOOL" routes to `/store` instead. So the primary named path into the product is broken; the working path is a differently-labelled link.
5. **Ascend** → tier upgrades inside the store. No visible ascension mechanic beyond the pricing table itself.

**The break:** there is no paid step between a free download and a recurring subscription, and the named route to the paid offer 404s. Via `[[pre-conversions]]`, the emotional and logical conversions may well be happening — the financial one is being asked for in a single leap with a dead link on the main path.

## 7. Market & audience

- **Criteria of the market** (`[[criteria-of-markets]]`) — what a prophetic-training buyer needs met, and coverage:
  - Legitimate spiritual authority behind the teaching — **met, strongly**
  - Doctrinal soundness / not flaky — **met** (structured curriculum, named leaders)
  - Practice, not just theory — **met** (activations, Q&A, prayer rooms)
  - Community of peers doing the same thing — **met** (cohorts, challenges)
  - Access to the man himself — **met, but rationed** (The Hive, quarterly)
  - Affordable from a non-Western economy — **met** (Emerging Nations Access)
  - Proof this develops real prophetic capability — `[UNKNOWN]` no testimonials observed on the store page
  - Low risk to try — **not met** (no trial, no low-ticket, no guarantee observed)
- **Limiting-belief mix** (`[[core-limiting-beliefs]]`) — `[INFERRED]` **helpless-dominant.** This audience believes prophecy is real and available; what they doubt is their own ability to hear clearly and act. "7 Ways God Speaks" is pitched exactly there. Some worthless ("am I even called?"), little hopeless.
- **Awareness** (`[[levels-of-awareness]]`) — solution-aware to product-aware. They know prophetic training exists; they're choosing whose.
- **Identity level** (`[[identity-level-markets]]`) — **fully identity-level.** "Prophet," "watchman," "intercessor" are worn identities, judged by a community. The store copy already speaks in "who" language ("Raising and Releasing Watchmen and Prophets"). Correctly pitched.
- **Currency** (`[[target-audience-currency]]`) — `[INFERRED]` mixed and geographically split. Emerging Nations Access existing at all says money is the binding constraint for a meaningful chunk of the base.

## 8. Positioning & moat

**Position owned:** the apostolic/prophetic training authority for a globally distributed, largely diaspora-and-emerging-market audience, with UK institutional credibility (TBN, charity status, physical campuses) behind it. `[INFERRED]` That combination is genuinely hard to copy — via `[[creating-a-competitive-moat]]`, the moat is the twenty-year ministry track record and the church network. Not replicable with money.

**Philosophy imposed** (`[[imposition-of-philosophy]]`): the prophetic belongs outside church walls — in business, government, media. "Every sphere of influence." This is a real, ownable argument against a real incumbent position (prophecy as a Sunday-morning, in-building activity).

**Club material, sold as a feature list.** Via `[[deep-positioning-and-club-membership]]`: they have every raw ingredient of access-gated positioning — named levels, a room, an inner circle, someone you have to go through, silent qualifiers. And it's presented as a three-column pricing table with bullet points. The doctrine's distinction is exact: you can own a thing, you can't own a club. The Hive is currently sold as a thing.

## 9. Brand vs personality

Via `[[brand-vs-personality-and-recurring-problems]]`:

**Key-man exposure is high but *not* total — and that's the interesting part.** `[OBSERVED]` Prophet Mutsa Samuwi runs The Watch day-to-day and fronts the £149 tier's live contact. Nicola is a co-founder and co-visionary. Campus leadership is devolved to named apostle/prophet couples. `[INFERRED]` Someone has already been building the succession layer — deliberately or not, the £149 tier is the de-risked product and the £399 tier is the founder-dependent one.

**The recurring-problem test — they pass.** Hearing God is not a problem that resolves and goes away. It's a lifelong practice with a natural, self-renewing cadence. Via the doctrine, that is the structural precondition for recurring revenue, and it's why a subscription is the right shape here. Most coaching businesses have to manufacture recurrence. This one doesn't.

**The god-model tension** (`[[conceptual-god-model]]`): the doctrine says bring the god down — demystify the mechanics, focus on similarity, because followers must believe in themselves to keep believing in the leader. The Hive monetises the opposite: distance from Tobi is the scarce good being sold. `[INFERRED]` Worth naming, but **the doctrine may simply not transfer cleanly here** — apostolic authority is a theological category, not a marketing pose, and "demystify the apostle" is not advice this prospect will or should take. Flagging it as an honest limit of the framework rather than a recommendation. See §10.

## 10. Trust & constraint

**Trust level:** `[INFERRED]` the *sales surface* runs at Level 1–2 (tell, plus borrowed third-party authority via TBN/BBC). The *actual relationship* already runs at Level 5 (live prayer, fasting, teaching with 7,500 people). Via `[[integrated-sales-processes]]`, the ladder is a staged, trust-depleting funnel bolted onto a relationship that has already replaced trust with direct experience. **The store page is doing work the relationship already did.**

**Mission-fit boundary — binding on everything in Pass 3:**

1. Nothing that monetises the church, the congregation, or pastoral relationships. The charity stays out of scope.
2. Nothing touching the Partnership rail. Giving is giving; it doesn't get funnel-optimised.
3. No urgency or scarcity manufactured around spiritual outcomes. Deadline pressure on "hearing God" is where this becomes indefensible.
4. Emerging Nations Access is protected. Any pricing change preserves it — it's a moral commitment and, incidentally, a positioning asset.
5. No advice that requires flattening his apostolic authority into guru-relatability. That's a doctrinal position, not a conversion lever.

Anything that fails these is not a lever. It's a way to lose the account in the first meeting.

---

# PASS 2 — DIAGNOSE

## What they're excellent at

Real, and worth saying first.

1. **The ladder architecture is genuinely well designed.** Three tiers where each adds a different *kind* of value rather than more of the same. Most people at this level sell one thing at one price.
2. **They built recurring revenue on a naturally recurring problem.** Structurally correct, and rarer than it sounds.
3. **The positioning argument is sharp and ownable** — prophetic authority beyond church walls, into business and government. A real counter-argument against a real incumbent belief.
4. **They already operate at the highest level of trust there is.** Live, recurring, experiential contact with thousands of people, weekly.
5. **Emerging Nations Access.** Access equity built into the pricing architecture, with a dignified application route rather than a discount code. Most operators never think of it.
6. **Succession has quietly started.** Mutsa fronting the community tier is the single smartest structural thing in the business, whether or not it was designed as such.
7. **Identity-level language, correctly used.** "Raising and Releasing Watchmen and Prophets" is "who" language in a market that is judged socially. Right register.

## Scorecard

Scored only where observable. Unscoreable dimensions say so rather than carry an invented number.

| Dimension | /10 | Why |
|---|---|---|
| Offer ladder (structure) | 7 | Well-tiered middle; holes at both ends |
| Offer ladder (format/price fit) | 4 | Energy-to-price curve inverted — see §4 |
| Money architecture | 4 | Two rails that cross; support money buys less than access money |
| Attention engine (reach) | 9 | 281K IG + 108K YT, ~375K views/mo, high cadence, improving |
| Attention engine (conversion of it) | 2 | Telegram is 2.7% of the IG following; AdSense ~$2–38/day; no visible route from video to magnet |
| Funnel integrity | 3 | Named path to the product 404s; no paid step before subscription |
| Positioning clarity | 8 | Ownable argument, real moat, correct register |
| Market fit of message | 7 | Correctly aimed at a helpless-dominant, identity-level market |
| Trust & relationship | 8 | Level 5 already achieved — just not connected to the ladder |
| Backend depth | 3 | Ceiling at £3,990/yr; nothing above |
| Brand durability | 6 | High key-man exposure, but succession layer visibly forming |
| Operational hygiene | 2 | Commercial site offline; 404 on hero CTA; three typos on the money page |

## Findings ledger

| Tier | Count |
|---|---|
| Critical | 3 |
| Major | 11 |
| Minor | 4 |
| **Total** | **18** |

*Revised 2026-08-14 after audience data landed (M8–M11 added).*

### CRITICAL

**C1 — The TAP Institute's website is offline.** `[OBSERVED — verified from two clients over ~20 min]` `www.thetapinstitute.org` has no DNS record. The apex fails TLS handshake (alert 40) and returns 409 over plain HTTP. Nameservers are Squarespace + NS1; the domain isn't correctly attached. **Every Google-indexed URL for the commercial arm sits on `www` and is therefore a dead link** — including the Winners Circle page and the Trustpilot listing. *Cost:* 100% of TAP's inbound, for as long as it's been down. *Caveat:* tested from one network; re-check before citing, though a missing DNS record isn't transient.

**C2 — The two revenue rails cross.** `[OBSERVED]` A Kingdom Partner giving £99/mo receives less than a member paying £49/mo. The most generous supporters are routed into the thinner experience. Via `[[hierarchy-of-value]]`, price and delivered value have come uncoupled in the one place a buyer compares them side by side — the same page. *Cost:* every supporter who would have paid more for more, and every member who notices.

**C3 — Nothing between free and £49/mo.** `[OBSERVED]` Ebook → Telegram → recurring subscription, in one jump. Via `[[cash-conversion-cycle]]`, a low-ticket entry is the primary structural lever for recouping acquisition spend and getting a first "yes" on the board; via `[[pre-conversions]]`, the financial conversion is being asked for without a smaller financial commitment preceding it. *Cost:* the entire warm-but-not-yet-paying middle of the audience.

### MAJOR

**M1 — The hero CTA 404s.** `[OBSERVED — browser + curl]` Homepage hero links to `/prophet-school`; returns 404. The nav item labelled "PROPHET SCHOOL" points at `/store` instead. The named path to the product is broken.

**M2 — No backend above £3,990/yr.** `[OBSERVED]` Via `[[industry-backend-model]]`, the winning move in a maturing category shifts to owning the backend. For a founder positioned as a seven-figure entrepreneur, there is no 1:1, no done-with-you, no certification, no licensing, no mastermind above The Hive.

**M3 — Format/price inversion.** `[INFERRED from OBSERVED pricing]` £49/mo buys self-serve courses and a library — maximum customer energy, the cheap end of `[[hierarchy-of-value]]`'s format ladder. £399/mo buys four founder contacts a year. Both rungs are priced against the wrong end of the energy curve.

**M4 — Level 5 trust is not wired to the ladder.** `[OBSERVED]` 7,500 people in live prayer, fasting and teaching. Via `[[integrated-sales-processes]]` and `[[levels-of-trust]]`, this is direct experience — the most effective and expensive trust level, already achieved and already paid for. The store page sells by *telling* instead. The asset and the ask are not connected.

**M5 — The club is sold as a pricing table.** `[OBSERVED]` Via `[[deep-positioning-and-club-membership]]`: levels, a room, an inner circle, gated access to the founder — every ingredient of access-gated positioning, presented as three columns of bullet points. Silent qualifiers replaced with feature lists.

**M6 — The only stated audience number is on rented land.** `[OBSERVED]` 7,500 on Telegram — a platform with no export, no segmentation, and no ownership. `[UNKNOWN]` email list size. Via `[[list-management-as-relationship-management]]`, the relationship at scale is being held somewhere they don't control.

**M7 — Opt-in friction on the only capture page.** `[OBSERVED]` A required ~250-option country dropdown is the heaviest element on a two-field lead-magnet form. *(Likely there to drive Emerging Nations pricing — so the fix is to move it, not delete it.)*

**M8 — 97% of the audience has never been asked.** `[OBSERVED]` 281K Instagram followers and 108K YouTube subscribers; 7,500 in the Telegram. Via `[[converting-audiences]]`, an already-in-motion audience is the cheapest conversion in marketing, and this one is 40x the size of the community the product is actually sold into. *This is now the single largest finding in the audit.*

**M9 — Audience/product mismatch, with the bridge sitting unused.** `[OBSERVED + INFERRED]` The channel's reach is built on geopolitical and discernment commentary; the store sells prophetic formation. The two "Mastering Meditation" videos (37,026 and 19,606 views, both top-six) are the seam between them, and the existing lead magnet is aimed squarely at it. Nothing observable routes viewers from those videos to that magnet.

**M10 — Nicola is an idle asset.** `[OBSERVED]` ~35K views per video across 28 videos — roughly 2.8x Tobi's lifetime per-video average, on 1/24th the output. Via `[[brand-vs-personality-and-recurring-problems]]`, she's also the most obvious hedge against the key-man exposure in M6/§9.

**M11 — Series drop-off of 76%.** `[OBSERVED]` Islam Part One 18,104 views → Part Two 4,384. Three quarters of an audience that had already committed to a two-part argument did not come back for the conclusion.

### MINOR

**m1 — Three typos on the revenue page.** `[OBSERVED]` "CIRRICULUM" (curriculum), "Watchen" (Watchmen), "INTERCESORS" (Intercessors). All on `/store`. Small, but they sit on the page where money changes hands, and one of them misspells the audience's own identity word.

**m2 — The annual saving is never stated.** `[OBSERVED]` Annual pricing is 10 months for 12 across all three tiers — a real ~17% discount, unadvertised. Free conversion lift, zero cost.

**m3 — No risk reversal observed.** `[OBSERVED]` No trial, no guarantee, no go-back mechanism on any tier. Via `[[risk-and-risk-reversal]]`, low-risk-to-try is an unmet market criterion (§7).

**m4 — No proof on the store page.** `[OBSERVED]` No testimonials, no student outcomes, no "prophets we've raised." In an identity-level market where the buyer's question is *will this actually develop me*, the money page answers it with nothing.

---

# PASS 3 — LEVERS

## Ranked

| # | Lever | Impact | Speed to cash | Effort | Needs him? | Joey's competency? |
|---|---|---|---|---|---|---|
| 1 | Reactivate the existing free audience into the existing £49 tier | High | **Days** | Low | No | **Yes — pure copy** |
| 1b | Route the 375K monthly video views to the existing lead magnet (end screens, pinned comments, descriptions, Shorts CTAs) | **Very high** | **Days** | Low | No | **Yes** |
| 2 | Fix the 404 + typos + state the annual saving | Low-med | Immediate | Trivial | No | Yes |
| 3 | Restore the TAP site | High (for TAP) | Immediate | Trivial | No | No — dev/DNS |
| 4 | Build a low-ticket paid entry (£19–£47) from existing content | High | Weeks | Med | No | **Yes** |
| 5 | Uncross the two rails — rebuild Partnership so giving buys *more*, not less | High | Weeks | Med | Some | **Yes — offer architecture** |
| 6 | Wire the Telegram/live experience into the sale | High | Weeks | Med | Some | **Yes** |
| 7 | Add proof + risk reversal to the store page | Med | Weeks | Low | Some | **Yes** |
| 8 | Paid acquisition on the lead magnet | High | Months | High | No | **Yes** |
| 9 | Build the backend above The Hive | Very high | Months | High | **Yes** | Partly |
| 10 | Migrate the Telegram relationship onto owned infrastructure | Med | Months | High | No | Partly |

Levers 3 and 10 are not his work — flagged so the recommendation stays honest.

Every lever above clears the §10 mission-fit boundary. Nothing touches the church, the congregation, or the Partnership rail's *purpose* — lever 5 restructures what supporters receive, never whether giving is asked for.

## The opener (free, before any pitch)

**Tell him the TAP Institute site is down.** One sentence, with the evidence: `www` has no DNS record, the apex fails TLS, every Google result for the Institute is a dead link. It costs nothing, it's verifiable in ten seconds, and it demonstrates that someone actually looked. This is the door, not the deal.

## The wedge

**Capture and convert the audience he already has. Copy and routing only — no new product, no new tech, no founder time.**

Two halves of one motion:

1. **Route the traffic.** ~375K monthly views currently exit to nothing. End screens, pinned comments, descriptions and Shorts CTAs pointed at "7 Ways God Speaks" — starting with the two "Mastering Meditation" videos, which are top-six performers *and* topically upstream of Prophet School.
2. **Convert the capture.** An email + Telegram sequence written to the helpless-dominant belief the magnet already selects for, moving those people into WATCH+.

**Why this one, over everything else on the list:**

- Every other lever requires something to be built. This requires nothing that doesn't already exist — the audience, the magnet, the product, the price and the trust are all in place. The only missing component is **the ask**, and the ask is the thing he'd be hiring for.
- **The size of the gap is arithmetic, not opinion.** 281K Instagram followers and ~375K monthly video views feed a 7,500-person Telegram. Whatever the right conversion rate turns out to be, it is being applied to 2.7% of the available audience.
- The current monetisation of that attention is **$2–38/day of AdSense.**

**The arithmetic of the gap** — *illustrative only, using their observed traffic against explicitly assumed rates. These are not projections and must never be presented to him as forecasts:*

> 375,000 monthly views × 1% opt-in = 3,750 leads/month.
> 3,750 × 2% to WATCH+ = 75 members × £49 = **£3,675 in new MRR per month, compounding.**
>
> Both rates are placeholders. **The point is not the number — it's that no rate is currently being applied at all**, because there is no route from the video to the magnet.

- **What it costs him:** no build, no dev, no calendar time. One approval pass so the theology is right.
- **What it proves:** an opt-in rate and a subscription conversion rate on his own traffic. Those two numbers are what turn levers 4, 5 and 8 from guesses into decisions.
- **What it opens onto:** the low-ticket entry offer (lever 4), then paid traffic against a funnel with known economics (lever 8).

## The case — say it out loud

> "Your TAP Institute site is down — `www` doesn't resolve at all, so every Google result for it is a dead link. That's a ten-minute fix and I'm not charging you for it.
>
> The bigger thing. You've got 281,000 people on Instagram and about 375,000 views a month on YouTube. Your Telegram has 7,500 in it. That's under 3% of the people who already follow you.
>
> And the videos that pull hardest are the ones closest to what you actually sell — both Mastering Meditation videos are in your top six. Those are the people who'd pay £49 a month for Prophet School. Right now they finish the video and there's nowhere for them to go.
>
> YouTube is paying you a few pounds a day for that attention.
>
> You don't have a traffic problem. You've got people who trust you further than most brands ever get near, and nobody's asking them. Let me build the route from the video to the ebook and write the sequence that asks. No new product, no build, nothing on your calendar.
>
> Then we look at the two numbers that come back and decide what's next."

---

## Open items

| # | To establish | Blocks |
|---|---|---|
| 1 | ~~Audience sizes~~ — **closed 2026-08-14.** 281K IG · 108K YT · ~375K views/mo. Email list size still unknown | Sizing the wedge |
| 2 | Do they run paid ads anywhere? | Lever 8 |
| 3 | WATCH+ current conversion rate | Baseline for the wedge |
| 4 | Is TAP dormant by choice or broken by accident? | Whether TAP is in scope at all |
| 5 | Verification on the recon §5 allegations | Whether to pitch — **open, logged, unverified** |
| 6 | Re-test the TAP domain from a second network | Before C1 is said out loud |

---

Related: [[recon]] [[The Lock]] [[Promotion]]
