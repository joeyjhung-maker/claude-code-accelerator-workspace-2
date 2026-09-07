# Genesis & Exodus — the key forks (full wiring)

Three tiers of power. The system works on all three; the keys make it better.
- **Plain Claude Code** — local prompt-bots in `bots/`. You can do every node manually.
- **Genesis API key** — the trained server bots (pro-grade output) + deep-build calls.
- **Exodus app/key** — the done-for-you pipeline (runs the majority of the flywheel for you).

Detect at onboarding: read `.env` for `GENESIS_API_KEY` and `EXODUS_API_KEY`. Route accordingly.
Always confirm `ANTHROPIC_API_KEY` exists — Genesis needs it as the provider key.

---

## GENESIS — the trained bots

**Endpoint & auth.** Base URL admin-provided, e.g. `https://gas.copycoders.ai/api/v1`.
Every call needs BOTH headers:
```
Authorization: Bearer $GENESIS_API_KEY
X-Provider-Key: $ANTHROPIC_API_KEY      # the key that actually runs the model
```
- **List bots:** `GET $GENESIS_BASE_URL/models` → live roster with IDs + descriptions (new bots get
  added; always check live).
- **Call a bot:** `POST $GENESIS_BASE_URL/chat/completions`
  ```json
  { "model": "<bot-id>", "messages": [ … ], "stream": true }
  ```
  `stream: true` is **required**. Wait 1–2s between protocol steps. Sequential calls only on one key.
- **Calls are slow and ~1-concurrent** — a single call can take 2+ min; a 2-minute timeout is not
  enough, give it 5-8.
- **Force UTF-8 on the response before reading it.** If calling with Python `requests`, the SSE
  response has no charset in its Content-Type header, so `requests` silently falls back to
  ISO-8859-1/Latin-1 for `iter_lines(decode_unicode=True)`. Every em-dash, curly quote, or emoji the
  bot sends then comes out as mojibake (`—` → `â€"`, `'` → `â€™`) and gets baked into the saved file.
  Set `r.encoding = 'utf-8'` right after the request, before iterating. (Caught 2026-09-01 — two saved
  bot outputs had to be repaired after the fact with `text.encode('latin-1').decode('utf-8')`, which
  round-trips cleanly IF the corruption is exactly this Latin-1-misread pattern — don't rely on that
  fix, just set the encoding correctly up front.)

**The 2-step protocol (every bot is stateless — replay the whole history each call):**
1. **Prime** — send the full primer (winning ads). Bot replies "I've absorbed the patterns."
2. **Instruct** — send as a conversation: `[primer] → [bot's confirmation] → [your instruction]`.
3. **(Hooks only) Double-pass** — same conversation, push to Level 3: 10 hooks → sharpen → 10 more.

**Quick-pick bot roster (the ones reached for most):**

| Stage | Bot ID | Does |
|---|---|---|
| Analysis | `media-buying-analysis-1` | Ads Manager CSV → spend/CPA/CTR/ROAS, star ads, budget issues |
| Analysis | `cash-analysisvariation-bot` | Deep read of top 5–10 ads — why they work, variation openings |
| Analysis | `comment-intel-1` | Ad comments → audience language, objections, buying signals |
| Ideation | `insight-vectors-bot` | Hidden patterns inside winners (Internal Vectors — I seeds) |
| Ideation | `75-ads-template-bot` | Extract a winning ad into a mad-lib template (Templates — T seeds) |
| Copy · hooks | `ad-hook-bot-1` | Hooks via 2-step + mandatory double-pass (20 total) |
| Copy · body+headlines | `mariobot` | 700–1500w body, headlines in the SAME conversation |
| Copy · swipes | `swiping-master-bot` | Faithful competitor swipe, run parallel to ad-hook-bot-1 |
| Video hook concepts | `unhinged-ad-bot-` | 10 absurdist 8-sec cinematic video-hook concepts w/ full camera specs + belief bridge per hook, then a style-menu for more |
| Strategy · mechanism naming | `characterizations-bot` | Names your mechanism: 20 curiosity-hook characterizations (UMP/UMS classified) + ranked top-3. Use this instead of hand-steering ad-hook-bot-1 toward a name. (Found 2026-08-10.) |
| Strategy · mechanism finding | `universal-mechanism-bot` | Generates 36 candidate mechanisms, scores them, delivers top 3 with headlines/hooks/emails. |
| Strategy · metaphors | `metaphors-bot` | Turns a UMP/UMS or belief into 50-100+ metaphor options. |

This quick-pick table is a starting point, not the ceiling — the live roster is much bigger (see below).
Before hand-writing something a specialized bot likely already does well (naming, belief-mapping,
angle-scoring, proof structuring), check the full list. Worth a quick check any time the job feels like
"strategy" rather than raw copywriting.

**Full live roster (143 bots, pulled 2026-09-01) — grouped by category.** Re-pull anytime with
`GET $GENESIS_BASE_URL/models` (headers: `Authorization: Bearer $GENESIS_API_KEY`,
`X-Provider-Key: $ANTHROPIC_API_KEY` or `$OPENROUTER_API_KEY`) and grep `_genesis.description` — new
bots get added, this list will drift stale over time.

<details>
<summary><strong>Strategy</strong> (23)</summary>

| Bot ID | Does |
|---|---|
| `ad-lottery-bot` | Randomly combines 190 concepts, 55 psych angles & 20+ styles into 10-100 wild ad-direction ideas to break creative ruts |
| `autobrief-bot-` | Turns mechanism + buyer profile + copy blocks into a deep-research prompt, then compiles the research into a full Beat Map Brief for VSLs/sales letter |
| `belief-alchemist-bot` | Turns a belief-gap analysis into tactical Install/Uninstall/Reframe/Accommodate mini-scripts, one per belief, ready to drop into copy. |
| `belief-analyst-bot` | Maps 12-24 current-vs-required beliefs per Problem/Solution/Vendor plus 7 Critical Sales Beliefs from offer materials. |
| `epiphany-threshold-bot` | Builds a 100-idea Scale of Believability (levels 1-10) for your market, flagging the 6-8 Goldilocks Zone angles. |
| `health-mechanism-matrix-bot` | Finds a supplement's unique mechanism-of-the-problem: builds a 12-mechanism deep-research prompt, then ranks the top 4 by 5 criteria. |
| `insight-vectors-bot` | Generates 10 hidden-mechanism 'aha moment' epiphanies (with WHY IT WORKS breakdowns) from your market, mechanism, or buyer research. |
| `master-concept-bot` | Turns buyer profile + offer into full psych profile, market analysis, and 100+ angle/style ad concepts in one doc |
| `metaphors-bot` | Turn your UMP/UMS or sales beliefs into 50-100+ ready-to-use natural, mechanical, and object metaphors. |
| `microscript` | Generate 5 Dominant Selling Ideas plus 5 Micro-Scripts each (25 total) — short, memorable, word-of-mouth phrases for any offer. |
| `offer-brief-bot` | Compiles offer details, a sales page URL, or raw materials into one 11-section Offer Brief (promise, pricing, stack, bonuses, guarantee, spokesperson) |
| `outcome-engineer-` | Engineers the core transformation promise, mechanism, and proof architecture behind a sales message — the strategic brief a VSL/sales letter bot writes from |
| `proof-page-master-bot` | Turn raw testimonials/studies/credentials into a page blueprint: proof inventory, objection map, and section-by-section placement plan. |
| `rhetorical-frames` | Ranks the 10 best persuasion frames for a marketing idea from a 7-category taxonomy, with reasoning + worked examples |
| `segment-surgeon-bot` | Turns product/offer/research/VOC input into 2-5 markdown segment briefs: desire, constraints, awareness %, demographics. |
| `static-ad-concept-expander-bot` | Generates 3-5 distinct strategic static-ad concept ideas (title + 1-2 sentence angle) from offer details — no copy or visuals, pure strategy layer. |
| `storm-bot` | Generates a 30-50 angle retargeting campaign brief (ads and/or emails) mapped to a 4-Pillars framework for copywriters to execute. |
| `strategic-allocation-bot` | Turns awareness split + risk level + ad count into a 5-category testing allocation matrix with 3 rounding options |
| `testable-proof-bot` | Turns product/offer material into 12 self-verifiable 'testable proof' hooks that create instant belief-shift aha moments |
| `universal-mechanism-bot` | Generates 36 candidate direct-response mechanisms, scores them, and delivers top 3 with headlines/VSL hooks/ad copy/email subjects. |
| `universal-static-bot` | Recommends the 3-5 best-fit static ad formats (of 21) for a product and tells you which generator bot to run next |
| `universal-static-idea-generator` | Diagnoses your assets, recommends 3-5 of 21 static ad formats plus which bot to run next; won't write concepts |
| `voice-mod-bot` | Builds a reusable hybrid brand-voice spec (archetype + scored parameters + tone samples) from a buyer profile. |

</details>

<details>
<summary><strong>Research</strong> (15)</summary>

| Bot ID | Does |
|---|---|
| `ad-tagging-bot-` | Tags any ad (yours or a competitor's) with its Concept, Angle, Style, and Hook using a fixed taxonomy — one ad or a batch, no rewriting. |
| `build-a-buyer-elite-` | Generates raw, private-voice buyer psychology profiles plus 10 deep-dive formats (3am journal, confession, doom-scroll, etc.) |
| `cash-analysisvariation-bot` | Tags any ad's Concept/Angle/Style/Hook, then generates up to 20 one-lever-at-a-time variation briefs. |
| `comment-intel-1` | Mines raw audience comments into 4 layers of verbatim ad language + 5-10 traceable conceptual ad ideas with hooks |
| `copy-blocks-extract` | Extracts every Pain/Promise/Proof/Constraint/Curiosity block from pasted copy as exact quotes, plus a strength critique. |
| `deep-dive-voice-analyzer` | Reverse-engineers a writer's voice from a 500+ word sample into a full dimensional report + signature patterns. |
| `market-analyzer-bot` | Splits an audience into 2-5 psychological submarkets (Drive/Processing/Capacity/Field) with positioning + messaging each |
| `media-buying-analysis-1` | Turns a Meta Ads export + offer brief into an account-level profit diagnosis with ranked What/Why/Expected-outcome fixes |
| `media-buying-analysis-2` | Turns a Meta Ads export + offer brief into a tiered account diagnosis with ranked issues, root causes, prioritized fixes |
| `pain-matrix-core-wound-bot-copy` | Scores a market on a 10-dim Pain Matrix + 12-resource Core Wound framework; predicts the core emotional wound |
| `primer-extractorsummarizer-v2` | Condenses a brand's ad/transcript library into a 400-600 word fact primer (mechanism, pricing, proof, voice) for other copy bots. |
| `reverse-brief-bot` | Deconstructs a pasted sales letter/VSL transcript into a full persuasion-beat-map brief (mechanisms, hooks, proof, metaphors) with verbatim quotes. |
| `social-proof-compilerstrengthen-bot` | Classifies all proof in your copy/offer docs into a 22-type framework by strength, rewrites weak proof as strong before/after examples. |
| `social-proof-deep-research-bot` | Builds a 22-type proof inventory from your materials, generates research prompts for gaps, and strengthens evidence with 7 manipulation tactics |
| `youtube-research-bot-` | Turns a video idea into a deep-research prompt (+ optional interview Qs, resource list, first-principles lenses), then compiles gathered findings |

</details>

<details>
<summary><strong>Copywriting / Ads</strong> (18)</summary>

| Bot ID | Does |
|---|---|
| `75-ads-template-bot` | Mad-Libs-transforms your offer into 75 proven ad-template scripts in one pass (or 3-sample preview), preserving each template's structure and tone. |
| `ad-hook-bot-1` | Writes 10 emotionally vicious, curiosity-led FB ad hooks (first 10-20 words) from a creative brief, ranks top 3 |
| `ad-swiper-v2` | Clones a winning ad's exact structure/rhythm for a new product — swaps only product details, keeps sentence count and skeleton locked. |
| `bionic-bullet-bot` | Generate 220+30 curiosity-driven fascination bullets (10 per type across 22 types, plus 30 bonus) from product info. |
| `cash-rewriter-bot` | Rewrite a winning ad changing only one CASH lever (Concept/Angle/Style/Hook) you specify — output is a ready-to-test variation. |
| `characterizations-bot` | Names your mechanism: 20 curiosity-hook characterizations (UMP/UMS classified) plus a ranked top-3 to test. |
| `headline-bot-` | Generate 10 VSL/TSL/TSL+ direct-response headline variations from copy blocks or a sales letter, tagged by rhetorical frame used. |
| `marcio-narrative-ads-bot-` | Writes a cold-traffic long-form narrative ad (FB/VSL/prelander/hybrid) that hides the product inside an emotional story until the reveal. |
| `new-hook-bot` | Generates 5-20+ psychologically-engineered short-video hooks (IG Reels/TikTok/FB ads) via Lane x Archetype x Pattern formula, with strategy notes |
| `organic-viral-to-paid-v2` | Turns a viral TikTok/Reel/tweet transcript into a paid ad: 5 swappable hooks + one shared body + transition + full assembled ad. |
| `paradoxical-questions-bot` | Generates dozens of niche-specific paradoxical curiosity questions (5 violation types) for ad/VSL/email hooks. |
| `segmentmech-swapper-bot` | Swap an ad's target segment or its problem/solution mechanism while keeping the winning structure and the other element intact. |
| `swiping-bot-master-bot` | Rebuilds a winning ad for your product by swapping only product details, keeping structure/rhythm/length locked sentence-for-sentence. |
| `swiping-master-bot` | Clones a winning ad's exact sentence structure/rhythm/length onto a new product — swaps only product-specific content, never rewrites. |
| `unaware-bot-master-bot` | Analyzes audience emotional drivers, then writes unaware-prospect ad hooks (3 batches of ~5) or full ad scripts. |
| `upsell-bot` | Ranks 5-7 post-purchase upsell ideas by category, then writes a full 11-15min video OTO script for your pick |
| `upwork-freelancer-bot-` | Turns an Upwork job post or client message into a psychologically-profiled proposal/reply, or a reusable Voice Guide |
| `viral-to-paid-converter-master-bot` | Swipes a viral clip's hook/structure into your product ad: 5 interchangeable hooks + 1 shared body + assembled ad. |

</details>

<details>
<summary><strong>Copywriting / Email</strong> (8)</summary>

| Bot ID | Does |
|---|---|
| `click-drivers-aem` | Turns a sales letter/offer brief into 20 click-driving teaser email angles or full 80-300 word send-ready emails. |
| `mario-bot-` | Writes finished emails/social posts/ad copy in copywriter Mario Castelli's raw, funny, direct-response voice |
| `mariobot` | Write marketing emails in Mario Castelli's casual, confessional direct-response voice for any product, market, or CTA goal. |
| `promo-bot` | Turns a sales letter/VSL + promo terms into 30+ promo angles and full 3-7 day launch emails (Awareness, Belief, Urgency). |
| `subject-line-bot` | Generates 10 (adjustable) high-variety, curiosity-driven email subject lines from your Copy Blocks + a required core idea, with reasoning. |
| `universal-email-bot` | Clones a client's voice from sample emails and writes 10 persuasion emails, 3 subject lines each; tunable via ~30 dials. |
| `write-like-luke-bot` | Writes emails (or social/sales copy) in Luke Iha's street-smart-professor voice using stacked Pain/Promise/Curiosity/Proof/Constraints blocks. |
| `write-like-maria` | Writes one piece of copy (email, ad, sales page, VSL script) in a warm story-driven 'Maria' voice from whatever product/audience context you give it. |

</details>

<details>
<summary><strong>Copywriting / Long Form</strong> (6)</summary>

| Bot ID | Does |
|---|---|
| `advertorial-bot` | Writes one 800-1500 word publication-ready advertorial from product info + audience + source ad + destination page, in 10 selectable formats |
| `better-than-mario-micro-lead` | Turns a hook + Promise/Pain/Proof/Curiosity copy blocks into a 200-350 word sales-letter opening. |
| `google-doc-sales-letter-bot` | Writes a full long-form Google-Doc-style sales letter for coaching/course/DFY/mastermind offers to warm traffic, with objection handling, proof, and CTA |
| `lead-` | Writes one long-form VSL/sales-letter opening hitting all 12 lead beats from spokesperson/offer/testimonial inputs. |
| `narrative-bot` | Writes the spokesperson's first-person VSL background-story opening (credibility>pain>hopelessness>solution hint) |
| `ump-bot` | Writes the VSL 'Unique Mechanism of the Problem' section — the surprising real cause of the pain; stops pre-solution. |

</details>

<details>
<summary><strong>Video Pipelines</strong> (13)</summary>

| Bot ID | Does |
|---|---|
| `direct-response-talking-head-script-bot-` | Generates 3+ direct-response talking head video scripts (15-90s) per audience segment, with hook/reframe/CTA reasoning included |
| `in-feed-vsl-bot` | Generate 10 in-feed MicroVSL concepts + full 3-6 min scripts for 3 of them from a buyer profile and offer details. |
| `infinite-adcbwriter-bot` | Writes 120-sec cold-traffic teaser video ad scripts with cinematic shot direction, built to drive clicks not sales |
| `micro-lead-bot-` | Turns a sales letter/VSL + product & audience info into 20 Micro Lead concepts plus a full 90-120s scripted opener (script+visuals table). |
| `microvsl` | 3-5 min in-feed VSL scripts: analyzes your buyer profile + offer, pitches 10 concepts, writes full scripts on request |
| `pig-idea-bot` | Generates 15 PIG (punch-in-the-gut) VSL nightmare-story concepts with Core Wound-based reasoning for each. |
| `ums-bot` | Writes the UMS (solution-mechanism) section of a VSL script from audience, pain-matrix, speaker, and proof inputs. |
| `unhinged-ad-bot-` | Turns an offer/avatar/existing ads into 10 absurdist 8-sec cinematic video-hook concepts with full camera specs + belief bridge, then a style menu for more |
| `upsells-bot` | Ranks 5-7 post-purchase upsell ideas by AOV potential, then writes a full 11-15min video upsell/downsell script for the pick. |
| `video-adscript-bot` | Writes 5 alternate 45-60s talking-head video ad scripts (different hooks/angles) from any marketing materials, zero questions asked |
| `video-brief-bot` | Turns a finished ad script into a copy-paste production brief with per-beat visual + editor shorthand notes |
| `vsl-bot` | Writes complete 10-20 min VSL scripts from your market + offer info; can also break down and adapt an existing VSL. |
| `youtube-script-bot` | One-shot: video idea in, full retention-engineered YouTube script or outline out (hooks, 3 CTAs, no timestamps). |

</details>

<details>
<summary><strong>Image Prompts</strong> (43)</summary>

| Bot ID | Does |
|---|---|
| `1.1-image-gen` | Finalizes any static ad concept into a locked 1:1, 300 DPI, high-contrast image-gen prompt; aspect override is absolute |
| `animation-bot` | Generates 5 illustrated-hook static ad concepts (visual IS the hook, no photography) from your offer/buyer/copy inputs. |
| `bold-typography-bot` | Generates 5 bold, text-led static ad concepts (typography as hero) from any brief, swipe copy, or VSL/sales page. |
| `branded-ads-image-prompt-generator` | Researches a brand's visual identity from its URL, then outputs 40 brand-consistent AI image-gen prompts across proven static ad templates. |
| `breakingauthority-transformer-bot-` | Turns offer/proof info into 5 (or N) breaking-news/authority static ad concepts (lower third, news card, live, wildcard) |
| `carousel-static-ads` | Turns buyer/offer/sales copy into 5 multi-frame carousel or story ad concepts (4 structured + 1 wildcard), per-frame layout notes included. |
| `collage-bot` | Generates 5 curiosity-collage static ad concepts (item+proof photo pairings) across 5 layout archetypes for designers/image-gen |
| `commentreview-transformer-bot-` | Turns proof points/offer info into 5 (or N) platform-native review/comment/chat static ad concepts, incl. 1 Wildcard |
| `comparison-bot` | Generates 5+ comparison static-ad concepts (us vs. competitor/category) across 6 layouts, ready for image-gen |
| `cost-of-inaction-bot-` | Generates 5 loss-aversion static ad concepts (price tags, receipts, cost timelines) making NOT buying feel costly |
| `curiosity-bait-bot-` | Generates 5+ no-product-shown curiosity-bait static ad concepts (headline, scene, style, layout, color) from offer copy |
| `handwrittennote-transformer-bot-` | Turns existing sales copy into 5 handwritten-note-style static ad image concepts (sticky note, journal, letter, etc.) plus one wildcard Collider variant |
| `happy-avatar-bot` | Generates 5+ people-forward static ad concepts (7 layout archetypes) with full photo direction from copy inputs |
| `headline-image-bot` | Turns a buyer profile, copy blocks, offer brief, and sales copy into 5+ headline+product static ad concepts across 6 layout archetypes. |
| `hero-bot-` | Generates 5 (scalable) HERO static ad concepts per batch — 2 Command, 2 Stealth, 1 Wildcard — each with full image-gen asset notes. |
| `holding-sign-bot` | Generates 5 (or N) person-holding-handwritten-sign UGC ad concepts with sign copy, emphasis, person, location details. |
| `infographic-bot-` | Turns buyer profile, copy blocks, offer brief, and sales copy into 5 educational infographic ad concepts across 7 layout archetypes. |
| `lo-fi-ad-concept-generator-bot` | Generates 5+ intentionally ugly, clashing-font 'rushed Canva slide' static ad concepts for pattern-interrupt scroll-stopping |
| `meme-style-ad-concept-generator-bot` | Generates ready-to-render meme-format static ads (Impact font, 5 layout types) with on-image text and CTA, 5 at a time |
| `multi-testimonial-bot-` | Turns your reviews/testimonials into 5 multi-quote static ad concepts (3-6 quotes each) across 5 layout archetypes. |
| `native-news-bot-` | Generates 10 fake-editorial 'native news' static ad concepts (publication, headline, image, insets, CTA) from offer copy |
| `note-from-founder-bot-` | Turns offer/VSL copy into 5 text-only 'Official Apology'/founder-note static ad concepts across 5 tone + visual archetypes |
| `post-it-note-bot` | Generate 5 sticky-note static ad concepts (note text, handwriting, color, placement, environment) from offer/buyer materials. |
| `problem-solution-bot` | Turns buyer/offer/copy inputs into 5+ problem-solution static ad concepts across 6 layout archetypes, ready for design or image-gen. |
| `product-breakdown-static-generator` | Collects buyer/offer/sales materials, asks quantity, then makes N product-breakdown static ad concepts in 7 layouts |
| `quizinteractive-bot` | Generates 5+ quiz/poll-style static ad concepts (grid, binary, poll, spectrum, persona types) from buyer/offer/copy inputs |
| `receipt-bot` | Turns offer/sales copy into 5 receipt-style static ad concepts (line items, pricing, paper style) across 5 archetypes, ready for design or image-gen. |
| `reptile-triggers` | Turns ad copy into 20 visceral native-feeling static image concepts across 12 trigger types, ranks top 10 |
| `reptile-triggers-bot` | Turns pasted ad copy into 20 native-feeling, primal/reptile-brain static image concepts (10 hook + 10 body), ranked top-10, no product shots. |
| `salespromotional-offer-bot-` | Turns offer/buyer/sales-copy input into 5 static promo ad concepts across 6 layouts, with visual, layout & color notes. |
| `scientific-study-bot` | Generates clinical/medical-imagery static ad concepts (scans, X-rays, thermal maps) across 8 layout archetypes, 5 at a time |
| `screenshotchatnotification-transformer-bot` | Turns product/offer/copy into 5 fake-chat or notification-stack static ad concepts (4 variants + 1 wildcard) with full design notes. |
| `side-by-sidebefore-and-after-bot-` | Turns buyer profile, offer brief, copy blocks & sales copy into 5+ before/after static ad concepts across 7 layouts. |
| `static-ad-sign` | Turns buyer/offer/sales-copy inputs into N 'person holding sign' UGC static ad concepts (person, sign copy, location) |
| `static-ad-info-extractor-bot` | Extracts an 8-field static-ad brief (product, audience, problem, promise, price, CTA, visuals, tone) from raw notes |
| `static-ad-specialist` | Brief + 1 of 20 concept styles → one image-gen-ready static ad prompt: visual scene, <10-word headline, layout specs |
| `static-swipe-bot-` | Upload a winning static ad; get its layout/psychology blueprint rebuilt into a full image-gen concept brief for your product. |
| `statistic-ad-generator-bot` | Turns offer/buyer/sales copy into 10 statistic-led static ad concepts (stat, claim, layout, disclaimer) for designers. |
| `step-by-step-bot-` | Generates 5 step-by-step static ad concepts (numbered routines/protocols) across 8 layout archetypes, ready for design or image-gen. |
| `testimonial-bot-` | Turns real customer quotes/reviews into 5 (or N) testimonial static-ad concepts across 7 layout archetypes, ready for a designer. |
| `ugc-bot-` | Generates organic-looking UGC static ad concepts (phone-photo style, casual voice) across 10 layout archetypes, 5 at a time |
| `unaware-static-image-ads-bot` | Ranks 5-7 native reptile-brain image concepts from ad copy, then generates copy-paste MidJourney phone-photo prompts. |
| `writing-on-body-bot` | Turns offer/VSL copy into 5 handwritten-on-skin static ad concepts (comparison, transformation claim, or audience callout) with body-part rationale |

</details>

<details>
<summary><strong>Pages & Funnels</strong> (12)</summary>

| Bot ID | Does |
|---|---|
| `advertorial-architect` | Interviews you for product/audience/proof, then writes a full long-form advertorial in 1 of 10 news-disguised subtypes with refinement menu |
| `bridge-page-bot` | Turns a Build-a-Buyer + Copy Blocks + Offer Brief + ad + VSL/sales page into one 250-400 word bridge page that drives the click. |
| `caveman-page-master-bot` | Writes a complete 8-18 question Q&A advertorial page from product/offer/buyer inputs, calibrated to price tier |
| `checkout-page-bot` | Audits a checkout page and returns a prioritized fix list (Quick Wins/Tests/Strategic) or builds an ASCII wireframe blueprint for a new one. |
| `downsell-bot` | Writes one full downsell page (headline/body/bullets/CTA), auto-picking the best downsell type from upsell details |
| `hybrid-pdp-master-bot` | Builds a full ecom-style PDP sales page (headline through FAQ/CTA) blending brand aesthetics with DR persuasion; flags gaps instead of faking proof. |
| `low-ticket-sales-page-bot` | Generates a full modular low-ticket ($7-47) sales page: headline, problem, offer, risk-reversal, CTA modules. |
| `opt-in-page-optimization-bot` | Generates 10 opt-in page copy variations by traffic temperature, then a full text pack, then optional deployable HTML. |
| `quiz-bot-master-bot` | Turns your offer + buyer profile into a full annotated quiz funnel: every question, panel, pop-up, and results page. |
| `the-listicle-lab-master-bot` | Turns offer+buyer+proof inputs into a complete listicle advertorial (Warning Signs/Reasons Why/Tips) with CTAs & FAQs |
| `top-5-affiliate-bot` | Builds a 'Top 5' comparison advertorial ranking your product #1; emits a competitor-research prompt if rivals missing |
| `top-5-products-bot` | Builds a Top 5 competitor-ranking bridge page that teases a #1 pick and drives clicks to your VSL |

</details>

<details>
<summary><strong>Creative</strong> (2)</summary>

| Bot ID | Does |
|---|---|
| `ai-ads-character-casting-agent` | Brief in, full character cast out: 19-slot concept map, character dossiers w/ monologues, staging, and paired ad seeds. |
| `surprising-culprit-bot` | Generate 15 'surprising villain' marketing angles (unexpected everyday culprit + pseudo-science mechanism) for a product's problem. |

</details>

<details>
<summary><strong>Other</strong> (3)</summary>

| Bot ID | Does |
|---|---|
| `bot-builder-bot` | Designs a complete new bot system prompt from a concept (or surgically revises one with feedback) using an 8-block template system |
| `linkedin-content-bot` | Builds a 10-concept LinkedIn hookboard, then drafts 3 voice-matched posts: engagement, authority, conversion. |
| `primer-prompt-builder` | Sorts a batch of winning ads verbatim into 4 primers (2 awareness buckets, hooks, headlines) for writer bots. |

</details>

**Parallelization (multiple Anthropic keys):** up to 3 briefs at once (one key each); body-1 / body-2
parallel; headlines wait for their body (same convo); swipe path parallel to hook path; sequential on
one key.

**Creative — images & video:** not on the Genesis server. One `KIE_API_KEY` covers BOTH — statics
(GPT-Image + Nano Banana Pro) and video (Veo / Kling / Sora). Higgsfield is a separate key, stylized
video only. Full render reference: `knowledge/kie-render-reference.md`.

**No Genesis key?** Use `bots/hook-bot.md`, `bots/writing-bot.md`, etc. on plain Claude. Still good —
just not the trained models. Recommend Genesis for serious volume/quality.

---

## EXODUS — the done-for-you pipeline

Exodus runs most of the flywheel for the operator. If they have it, route to the `exodus` CLI instead
of building the heavy nodes by hand.

**API (raw):** `EXODUS_API_URL=https://good-cod-360.convex.site`, `Authorization: Bearer $EXODUS_API_KEY`
(e.g. `GET /api/v2/swipe-library` → scraped competitor ads). **Pipeline keys it needs in `.env`:**
Anthropic + KIE (renders); ElevenLabs for video/Pixar.

**Command surface (what's reliable):**

| Capability | Command | Notes |
|---|---|---|
| Build primer | `exodus primer --file <winning-ads.md> --yes` | async; 4-primer split (body unaware/problem · body solution/product · hooks · headlines), built from their winning ads |
| Primer steering | `exodus primer steering` | set always-use / don't-use per primer |
| Write ads (workhorse) | `exodus genesis run --brief <brief.md>` | the reliable path; also the swipe path |
| From a reel/post | `exodus genesis --reel "<url>"` | canonical `/reel/<id>/` or `/p/<id>/` |
| Static images | `exodus image --ad "<copy>"` | infers native; copy-derived bundles Reptile/SCRAWLS |
| Templated statics | `exodus image --type template` | `--realism realistic`, `--mode manual --quantities` |
| Poll a long run | `exodus read-doc <runId>` | fire runs with `--no-wait`, then poll |

**The faithful swipe recipe** (use this, not `mirror`): `exodus genesis run --brief` with a brief that
has ① a numbered **beat-map** of the source ad (each beat's function), ② a **mechanism-swap** to the
brand's mechanism, ③ a **brand guard** ("do NOT mention <competitor/ingredients>"), ④ the **full source
ad** pasted at the bottom.

**Gotchas to know (so you don't misread a run):**
- Runs are long + server-side → `--no-wait` then poll `read-doc`. The "no documents yet" message
  contains the word **"failed"** — do NOT grep for "failed" to detect failure.
- Genesis VPS is ~1-concurrent — don't fire many at once (they queue/stall).
- KIE drops ~1–2 renders per batch (429) — re-fire.
- After any `exodus update`, `chmod +x node_modules/.bin/exodus`.
- `mirror` modes are unreliable (modular can ship the wrong brand) — prefer the brief recipe.

**What Exodus does for you (the speed-up):** categorizes winning ads into primer slots, writes briefs,
pulls from multiple brands, auto-generates reptile triggers + templates, runs the writing/static
pipelines. A good majority of the manual build — not 100%, but most of it.

---

## The routing rule (for the skill)

For any node the user wants:
- **Has Exodus?** → is there an `exodus` command for it? Use it (done-for-you). Else fall through.
- **Has Genesis key?** → route writing/analysis to the trained bots via the 2-step protocol.
- **Neither?** → use the local `bots/` on plain Claude Code.

Always be honest about the tier: plain = you can do it; Genesis = pro bots; Exodus = it does it for you.
