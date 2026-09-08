# Genesis Bot Index

One line per bot: what it makes and what it needs. For full input details on a
bot, grep `references/bots.md` for `## <slug>`. For how to produce the inputs,
see `references/recipes.md` and `references/brand-kit.md`.

**Modes** (what happens when you call it): `needs-input` = it asks for its
materials if you send nothing, then produces in one pass — front-load the
brand kit and it one-shots (this is most bots). `self-serve` = generates on a
bare call; add context only to steer. `menu` = offers a choose-a-path menu or
asks a decision, so expect one turn. `multi-phase` = a multi-step pipeline.

> **Rule of thumb:** almost every bot gates on input. Call one cold and it hands
> you its shopping list instead of output. Assemble inputs first (brand-kit.md),
> pass them in the first message, and you skip the round-trip.

## Research & Analysis (15)

| slug | what it does | mode | needs |
|---|---|---|---|
| `ad-tagging-bot-` | Tags any ad (yours or a competitor's) with its Concept, Angle, Style, and Hook using a fixed taxonomy — one ad or a batch, no rewriting. | needs-input | winning-ad |
| `build-a-buyer-elite-` | Generates raw, private-voice buyer psychology profiles plus 10 deep-dive formats (3am journal, confession, doom-scroll, etc.) | menu | buyer-profile, offer-details |
| `cash-analysisvariation-bot` | Tags any ad's Concept/Angle/Style/Hook, then generates up to 20 one-lever-at-a-time variation briefs. | needs-input | winning-ad |
| `comment-intel-1` | Mines raw audience comments into 4 layers of verbatim ad language + 5-10 traceable conceptual ad ideas with hooks | needs-input | raw-notes |
| `copy-blocks-extract` | Extracts every Pain/Promise/Proof/Constraint/Curiosity block from pasted copy as exact quotes, plus a strength critique. | needs-input | raw-notes |
| `deep-dive-voice-analyzer` | Reverse-engineers a writer's voice from a 500+ word sample into a full dimensional report + signature patterns. | needs-input | brand-voice |
| `market-analyzer-bot` | Splits an audience into 2-5 psychological submarkets (Drive/Processing/Capacity/Field) with positioning + messaging each | needs-input | context (any brand-kit asset) |
| `media-buying-analysis-1` | Turns a Meta Ads export + offer brief into an account-level profit diagnosis with ranked What/Why/Expected-outcome fixes | needs-input | buyer-profile, offer-details, other:ad-performance-data |
| `media-buying-analysis-2` | Turns a Meta Ads export + offer brief into a tiered account diagnosis with ranked issues, root causes, prioritized fixes | needs-input | offer-details, other:ad-performance-data |
| `pain-matrix-core-wound-bot-copy` | Scores a market on a 10-dim Pain Matrix + 12-resource Core Wound framework; predicts the core emotional wound | needs-input | context (any brand-kit asset) |
| `primer-extractorsummarizer-v2` | Condenses a brand's ad/transcript library into a 400-600 word fact primer (mechanism, pricing, proof, voice) for other copy bots. | needs-input | raw-notes |
| `reverse-brief-bot` | Deconstructs a pasted sales letter/VSL transcript into a full persuasion-beat-map brief (mechanisms, hooks, proof, metaphors) with verbatim quotes. | needs-input | vsl-script |
| `social-proof-compilerstrengthen-bot` | Classifies all proof in your copy/offer docs into a 22-type framework by strength, rewrites weak proof as strong before/after examples. | needs-input | context (any brand-kit asset) |
| `social-proof-deep-research-bot` | Builds a 22-type proof inventory from your materials, generates research prompts for gaps, and strengthens evidence with 7 manipulation tactics | multi-phase | creative-brief |
| `youtube-research-bot-` | Turns a video idea into a deep-research prompt (+ optional interview Qs, resource list, first-principles lenses), then compiles gathered findings into one structured doc. | needs-input | content-topic |

## Strategy & Briefs (23)

| slug | what it does | mode | needs |
|---|---|---|---|
| `ad-lottery-bot` | Randomly combines 190 concepts, 55 psych angles & 20+ styles into 10-100 wild ad-direction ideas to break creative ruts | needs-input | context (any brand-kit asset) |
| `autobrief-bot-` | Turns mechanism + buyer profile + copy blocks into a deep-research prompt, then compiles the research into a full Beat Map Brief for VSLs/sales letters. | multi-phase | buyer-profile, mechanism, raw-notes |
| `belief-alchemist-bot` | Turns a belief-gap analysis into tactical Install/Uninstall/Reframe/Accommodate mini-scripts, one per belief, ready to drop into copy. | needs-input | other:belief-gap-analysis |
| `belief-analyst-bot` | Maps 12-24 current-vs-required beliefs per Problem/Solution/Vendor plus 7 Critical Sales Beliefs from offer materials. | needs-input | other:mixed-marketing-materials |
| `epiphany-threshold-bot` | Builds a 100-idea Scale of Believability (levels 1-10) for your market, flagging the 6-8 Goldilocks Zone angles. | needs-input | buyer-profile |
| `health-mechanism-matrix-bot` | Finds a supplement's unique mechanism-of-the-problem: builds a 12-mechanism deep-research prompt, then ranks the top 4 by 5 criteria. | multi-phase | product-info |
| `insight-vectors-bot` | Generates 10 hidden-mechanism 'aha moment' epiphanies (with WHY IT WORKS breakdowns) from your market, mechanism, or buyer research. | needs-input | mechanism |
| `master-concept-bot` | Turns buyer profile + offer into full psych profile, market analysis, and 100+ angle/style ad concepts in one doc | needs-input | buyer-profile, offer-details |
| `metaphors-bot` | Turn your UMP/UMS or sales beliefs into 50-100+ ready-to-use natural, mechanical, and object metaphors. | needs-input | raw-notes |
| `microscript` | Generate 5 Dominant Selling Ideas plus 5 Micro-Scripts each (25 total) — short, memorable, word-of-mouth phrases for any offer. | needs-input | product-info |
| `offer-brief-bot` | Compiles offer details, a sales page URL, or raw materials into one 11-section Offer Brief (promise, pricing, stack, bonuses, guarantee, spokesperson). | needs-input | context (any brand-kit asset) |
| `outcome-engineer-` | Engineers the core transformation promise, mechanism, and proof architecture behind a sales message — the strategic brief a VSL/sales letter bot writes from. | needs-input | buyer-profile |
| `proof-page-master-bot` | Turn raw testimonials/studies/credentials into a page blueprint: proof inventory, objection map, and section-by-section placement plan. | needs-input | customer-reviews |
| `rhetorical-frames` | Ranks the 10 best persuasion frames for a marketing idea from a 7-category taxonomy, with reasoning + worked examples | needs-input | raw-notes |
| `segment-surgeon-bot` | Turns product/offer/research/VOC input into 2-5 markdown segment briefs: desire, constraints, awareness %, demographics. | needs-input | context (any brand-kit asset) |
| `static-ad-concept-expander-bot` | Generates 3-5 distinct strategic static-ad concept ideas (title + 1-2 sentence angle) from offer details — no copy or visuals, pure strategy layer. | needs-input | context (any brand-kit asset) |
| `storm-bot` | Generates a 30-50 angle retargeting campaign brief (ads and/or emails) mapped to a 4-Pillars framework for copywriters to execute. | needs-input | context (any brand-kit asset) |
| `strategic-allocation-bot` | Turns awareness split + risk level + ad count into a 5-category testing allocation matrix with 3 rounding options | needs-input | context (any brand-kit asset) |
| `testable-proof-bot` | Turns product/offer material into 12 self-verifiable 'testable proof' hooks that create instant belief-shift aha moments | needs-input | other:marketing-material-dump |
| `universal-mechanism-bot` | Generates 36 candidate direct-response mechanisms, scores them, and delivers top 3 with headlines/VSL hooks/ad copy/email subjects. | needs-input | buyer-profile, other:market-niche, product-info |
| `universal-static-bot` | Recommends the 3-5 best-fit static ad formats (of 21) for a product and tells you which generator bot to run next | needs-input | context (any brand-kit asset) |
| `universal-static-idea-generator` | Diagnoses your assets, recommends 3-5 of 21 static ad formats plus which bot to run next; won't write concepts | needs-input | other:mixed |
| `voice-mod-bot` | Builds a reusable hybrid brand-voice spec (archetype + scored parameters + tone samples) from a buyer profile. | needs-input | buyer-profile |

## Copywriting — Ads (18)

| slug | what it does | mode | needs |
|---|---|---|---|
| `75-ads-template-bot` | Mad-Libs-transforms your offer into 75 proven ad-template scripts in one pass (or 3-sample preview), preserving each template's structure and tone. | needs-input | other:offer-source-dump |
| `ad-hook-bot-1` | Writes 10 emotionally vicious, curiosity-led FB ad hooks (first 10-20 words) from a creative brief, ranks top 3 | needs-input | creative-brief |
| `ad-swiper-v2` | Clones a winning ad's exact structure/rhythm for a new product — swaps only product details, keeps sentence count and skeleton locked. | needs-input | other:closeness-level-1-5, product-info, winning-ad |
| `bionic-bullet-bot` | Generate 220+30 curiosity-driven fascination bullets (10 per type across 22 types, plus 30 bonus) from product info. | needs-input | product-info |
| `cash-rewriter-bot` | Rewrite a winning ad changing only one CASH lever (Concept/Angle/Style/Hook) you specify — output is a ready-to-test variation. | needs-input | other:cash-analysis, other:variation-direction, winning-ad |
| `characterizations-bot` | Names your mechanism: 20 curiosity-hook characterizations (UMP/UMS classified) plus a ranked top-3 to test. | needs-input | mechanism |
| `headline-bot-` | Generate 10 VSL/TSL/TSL+ direct-response headline variations from copy blocks or a sales letter, tagged by rhetorical frame used. | needs-input | ad-copy |
| `marcio-narrative-ads-bot-` | Writes a cold-traffic long-form narrative ad (FB/VSL/prelander/hybrid) that hides the product inside an emotional story until the reveal. | needs-input | buyer-profile, product-info |
| `new-hook-bot` | Generates 5-20+ psychologically-engineered short-video hooks (IG Reels/TikTok/FB ads) via Lane x Archetype x Pattern formula, with strategy notes and scoring. | needs-input | context (any brand-kit asset) |
| `organic-viral-to-paid-v2` | Turns a viral TikTok/Reel/tweet transcript into a paid ad: 5 swappable hooks + one shared body + transition + full assembled ad. | multi-phase | other:brand-primer, swipe-example |
| `paradoxical-questions-bot` | Generates dozens of niche-specific paradoxical curiosity questions (5 violation types) for ad/VSL/email hooks. | needs-input | content-topic |
| `segmentmech-swapper-bot` | Swap an ad's target segment or its problem/solution mechanism while keeping the winning structure and the other element intact. | needs-input | other:parameter, winning-ad |
| `swiping-bot-master-bot` | Rebuilds a winning ad for your product by swapping only product details, keeping structure/rhythm/length locked sentence-for-sentence. | needs-input | product-info, winning-ad |
| `swiping-master-bot` | Clones a winning ad's exact sentence structure/rhythm/length onto a new product — swaps only product-specific content, never rewrites. | needs-input | product-info, winning-ad |
| `unaware-bot-master-bot` | Analyzes audience emotional drivers, then writes unaware-prospect ad hooks (3 batches of ~5) or full ad scripts. | needs-input | buyer-profile, offer-details, other:copy-blocks |
| `upsell-bot` | Ranks 5-7 post-purchase upsell ideas by category, then writes a full 11-15min video OTO script for your pick | needs-input | buyer-profile, offer-details, product-info |
| `upwork-freelancer-bot-` | Turns an Upwork job post or client message into a psychologically-profiled proposal/reply, or a reusable Voice Guide | multi-phase | other:client-message, other:job-posting |
| `viral-to-paid-converter-master-bot` | Swipes a viral clip's hook/structure into your product ad: 5 interchangeable hooks + 1 shared body + assembled ad. | needs-input | product-info, winning-ad |

## Copywriting — Email (8)

| slug | what it does | mode | needs |
|---|---|---|---|
| `click-drivers-aem` | Turns a sales letter/offer brief into 20 click-driving teaser email angles or full 80-300 word send-ready emails. | needs-input | offer-details |
| `mario-bot-` | Writes finished emails/social posts/ad copy in copywriter Mario Castelli's raw, funny, direct-response voice | needs-input | buyer-profile, offer-details, other:format-spec |
| `mariobot` | Write marketing emails in Mario Castelli's casual, confessional direct-response voice for any product, market, or CTA goal. | needs-input | buyer-profile, other:parameter, product-info |
| `promo-bot` | Turns a sales letter/VSL + promo terms into 30+ promo angles and full 3-7 day launch emails (Awareness, Belief, Urgency). | needs-input | offer-details, vsl-script |
| `subject-line-bot` | Generates 10 (adjustable) high-variety, curiosity-driven email subject lines from your Copy Blocks + a required core idea, with reasoning. | needs-input | other:copy-blocks, other:core-idea |
| `universal-email-bot` | Clones a client's voice from sample emails and writes 10 persuasion emails, 3 subject lines each; tunable via ~30 dials. | needs-input | brand-voice, offer-details |
| `write-like-luke-bot` | Writes emails (or social/sales copy) in Luke Iha's street-smart-professor voice using stacked Pain/Promise/Curiosity/Proof/Constraints blocks. | needs-input | context (any brand-kit asset) |
| `write-like-maria` | Writes one piece of copy (email, ad, sales page, VSL script) in a warm story-driven 'Maria' voice from whatever product/audience context you give it. | needs-input | other:copy-type-request |

## Copywriting — Long Form (6)

| slug | what it does | mode | needs |
|---|---|---|---|
| `advertorial-bot` | Writes one 800-1500 word publication-ready advertorial from product info + audience + source ad + destination page, in 10 selectable formats | needs-input | buyer-profile, landing-page-url, product-info, winning-ad |
| `better-than-mario-micro-lead` | Turns a hook + Promise/Pain/Proof/Curiosity copy blocks into a 200-350 word sales-letter opening. | needs-input | headline, other:copy-blocks |
| `google-doc-sales-letter-bot` | Writes a full long-form Google-Doc-style sales letter for coaching/course/DFY/mastermind offers to warm traffic, with objection handling, proof, and CTA. | needs-input | buyer-profile, customer-reviews, mechanism, offer-details |
| `lead-` | Writes one long-form VSL/sales-letter opening hitting all 12 lead beats from spokesperson/offer/testimonial inputs. | needs-input | buyer-profile, competitor-info, customer-reviews, mechanism, other:credibility-elements, other:desired-outcome, other:pain-point, other:personal-story, other:social-proof-numbers, other:spokesperson-name, other:unique-mechanism-name |
| `narrative-bot` | Writes the spokesperson's first-person VSL background-story opening (credibility>pain>hopelessness>solution hint) | needs-input | context (any brand-kit asset) |
| `ump-bot` | Writes the VSL 'Unique Mechanism of the Problem' section — the surprising real cause of the pain; stops pre-solution. | needs-input | buyer-profile, mechanism |

## Pages & Funnels (12)

| slug | what it does | mode | needs |
|---|---|---|---|
| `advertorial-architect` | Interviews you for product/audience/proof, then writes a full long-form advertorial in 1 of 10 news-disguised subtypes with refinement menu | needs-input | buyer-profile, customer-reviews, mechanism, other:market-awareness, other:traffic-source, product-info |
| `bridge-page-bot` | Turns a Build-a-Buyer + Copy Blocks + Offer Brief + ad + VSL/sales page into one 250-400 word bridge page that drives the click. | needs-input | context (any brand-kit asset) |
| `caveman-page-master-bot` | Writes a complete 8-18 question Q&A advertorial page from product/offer/buyer inputs, calibrated to price tier | needs-input | context (any brand-kit asset) |
| `checkout-page-bot` | Audits a checkout page and returns a prioritized fix list (Quick Wins/Tests/Strategic) or builds an ASCII wireframe blueprint for a new one. | needs-input | context (any brand-kit asset) |
| `downsell-bot` | Writes one full downsell page (headline/body/bullets/CTA), auto-picking the best downsell type from upsell details | menu | buyer-profile, offer-details |
| `hybrid-pdp-master-bot` | Builds a full ecom-style PDP sales page (headline through FAQ/CTA) blending brand aesthetics with DR persuasion; flags gaps instead of faking proof. | needs-input | context (any brand-kit asset) |
| `low-ticket-sales-page-bot` | Generates a full modular low-ticket ($7-47) sales page: headline, problem, offer, risk-reversal, CTA modules. | needs-input | buyer-profile, creative-brief, offer-details, other:market-awareness, product-info |
| `opt-in-page-optimization-bot` | Generates 10 opt-in page copy variations by traffic temperature, then a full text pack, then optional deployable HTML. | multi-phase | buyer-profile, other:page-type-enum, other:traffic-source |
| `quiz-bot-master-bot` | Turns your offer + buyer profile into a full annotated quiz funnel: every question, panel, pop-up, and results page. | needs-input | buyer-profile, offer-details |
| `the-listicle-lab-master-bot` | Turns offer+buyer+proof inputs into a complete listicle advertorial (Warning Signs/Reasons Why/Tips) with CTAs & FAQs | needs-input | buyer-profile, landing-page-copy, offer-details, other:copy-blocks |
| `top-5-affiliate-bot` | Builds a 'Top 5' comparison advertorial ranking your product #1; emits a competitor-research prompt if rivals missing | multi-phase | competitor-info, product-info |
| `top-5-products-bot` | Builds a Top 5 competitor-ranking bridge page that teases a #1 pick and drives clicks to your VSL | multi-phase | buyer-profile, mechanism, offer-details, vsl-script |

## Video & VSL (13)

| slug | what it does | mode | needs |
|---|---|---|---|
| `direct-response-talking-head-script-bot-` | Generates 3+ direct-response talking head video scripts (15-90s) per audience segment, with hook/reframe/CTA reasoning included | needs-input | buyer-profile, offer-details, other:cta |
| `in-feed-vsl-bot` | Generate 10 in-feed MicroVSL concepts + full 3-6 min scripts for 3 of them from a buyer profile and offer details. | needs-input | buyer-profile, offer-details |
| `infinite-adcbwriter-bot` | Writes 120-sec cold-traffic teaser video ad scripts with cinematic shot direction, built to drive clicks not sales | self-serve | mechanism |
| `micro-lead-bot-` | Turns a sales letter/VSL + product & audience info into 20 Micro Lead concepts plus a full 90-120s scripted opener (script+visuals table). | needs-input | context (any brand-kit asset) |
| `microvsl` | 3-5 min in-feed VSL scripts: analyzes your buyer profile + offer, pitches 10 concepts, writes full scripts on request | multi-phase | buyer-profile, offer-details, other:funnel-context |
| `pig-idea-bot` | Generates 15 PIG (punch-in-the-gut) VSL nightmare-story concepts with Core Wound-based reasoning for each. | needs-input | other:market-niche |
| `ums-bot` | Writes the UMS (solution-mechanism) section of a VSL script from audience, pain-matrix, speaker, and proof inputs. | needs-input | buyer-profile, creative-brief, mechanism, other:proof-points, other:speaker-bio |
| `unhinged-ad-bot-` | Turns an offer/avatar/existing ads into 10 absurdist 8-sec cinematic video-hook concepts with full camera specs + belief bridge, then a style menu for more. | multi-phase | context (any brand-kit asset) |
| `upsells-bot` | Ranks 5-7 post-purchase upsell ideas by AOV potential, then writes a full 11-15min video upsell/downsell script for the pick. | multi-phase | buyer-profile, product-info |
| `video-adscript-bot` | Writes 5 alternate 45-60s talking-head video ad scripts (different hooks/angles) from any marketing materials, zero questions asked | needs-input | context (any brand-kit asset) |
| `video-brief-bot` | Turns a finished ad script into a copy-paste production brief with per-beat visual + editor shorthand notes | needs-input | video-script |
| `vsl-bot` | Writes complete 10-20 min VSL scripts from your market + offer info; can also break down and adapt an existing VSL. | needs-input | buyer-profile, offer-details |
| `youtube-script-bot` | One-shot: video idea in, full retention-engineered YouTube script or outline out (hooks, 3 CTAs, no timestamps). | needs-input | content-topic |

## Image Prompts — Statics (42)

| slug | what it does | mode | needs |
|---|---|---|---|
| `1.1-image-gen` | Finalizes any static ad concept into a locked 1:1, 300 DPI, high-contrast image-gen prompt; aspect override is absolute | needs-input | static-ad-concept |
| `animation-bot` | Generates 5 illustrated-hook static ad concepts (visual IS the hook, no photography) from your offer/buyer/copy inputs. | needs-input | ad-copy, buyer-profile, offer-details, other:sales-copy |
| `bold-typography-bot` | Generates 5 bold, text-led static ad concepts (typography as hero) from any brief, swipe copy, or VSL/sales page. | needs-input | context (any brand-kit asset) |
| `branded-ads-image-prompt-generator` | Researches a brand's visual identity from its URL, then outputs 40 brand-consistent AI image-gen prompts across proven static ad templates. | multi-phase | offer-details, other:brand-name, other:brand-url |
| `breakingauthority-transformer-bot-` | Turns offer/proof info into 5 (or N) breaking-news/authority static ad concepts (lower third, news card, live, wildcard) | needs-input | context (any brand-kit asset) |
| `carousel-static-ads` | Turns buyer/offer/sales copy into 5 multi-frame carousel or story ad concepts (4 structured + 1 wildcard), per-frame layout notes included. | needs-input | other:mixed |
| `collage-bot` | Generates 5 curiosity-collage static ad concepts (item+proof photo pairings) across 5 layout archetypes for designers/image-gen | needs-input | context (any brand-kit asset) |
| `commentreview-transformer-bot-` | Turns proof points/offer info into 5 (or N) platform-native review/comment/chat static ad concepts, incl. 1 Wildcard | needs-input | context (any brand-kit asset) |
| `comparison-bot` | Generates 5+ comparison static-ad concepts (us vs. competitor/category) across 6 layouts, ready for image-gen | needs-input | context (any brand-kit asset) |
| `cost-of-inaction-bot-` | Generates 5 loss-aversion static ad concepts (price tags, receipts, cost timelines) making NOT buying feel costly | needs-input | context (any brand-kit asset) |
| `curiosity-bait-bot-` | Generates 5+ no-product-shown curiosity-bait static ad concepts (headline, scene, style, layout, color) from offer copy | needs-input | context (any brand-kit asset) |
| `handwrittennote-transformer-bot-` | Turns existing sales copy into 5 handwritten-note-style static ad image concepts (sticky note, journal, letter, etc.) plus one wildcard Collider variant. | needs-input | context (any brand-kit asset) |
| `happy-avatar-bot` | Generates 5+ people-forward static ad concepts (7 layout archetypes) with full photo direction from copy inputs | needs-input | context (any brand-kit asset) |
| `headline-image-bot` | Turns a buyer profile, copy blocks, offer brief, and sales copy into 5+ headline+product static ad concepts across 6 layout archetypes. | needs-input | context (any brand-kit asset) |
| `hero-bot-` | Generates 5 (scalable) HERO static ad concepts per batch — 2 Command, 2 Stealth, 1 Wildcard — each with full image-gen asset notes. | needs-input | context (any brand-kit asset) |
| `holding-sign-bot` | Generates 5 (or N) person-holding-handwritten-sign UGC ad concepts with sign copy, emphasis, person, location details. | needs-input | context (any brand-kit asset) |
| `infographic-bot-` | Turns buyer profile, copy blocks, offer brief, and sales copy into 5 educational infographic ad concepts across 7 layout archetypes. | needs-input | other:any-of |
| `lo-fi-ad-concept-generator-bot` | Generates 5+ intentionally ugly, clashing-font 'rushed Canva slide' static ad concepts for pattern-interrupt scroll-stopping | needs-input | context (any brand-kit asset) |
| `meme-style-ad-concept-generator-bot` | Generates ready-to-render meme-format static ads (Impact font, 5 layout types) with on-image text and CTA, 5 at a time | needs-input | context (any brand-kit asset) |
| `multi-testimonial-bot-` | Turns your reviews/testimonials into 5 multi-quote static ad concepts (3-6 quotes each) across 5 layout archetypes. | needs-input | ad-copy, buyer-profile, offer-details, other:sales-copy-with-testimonials |
| `native-news-bot-` | Generates 10 fake-editorial 'native news' static ad concepts (publication, headline, image, insets, CTA) from offer copy | needs-input | context (any brand-kit asset) |
| `note-from-founder-bot-` | Turns offer/VSL copy into 5 text-only 'Official Apology'/founder-note static ad concepts across 5 tone + visual archetypes | needs-input | context (any brand-kit asset) |
| `post-it-note-bot` | Generate 5 sticky-note static ad concepts (note text, handwriting, color, placement, environment) from offer/buyer materials. | needs-input | context (any brand-kit asset) |
| `problem-solution-bot` | Turns buyer/offer/copy inputs into 5+ problem-solution static ad concepts across 6 layout archetypes, ready for design or image-gen. | needs-input | context (any brand-kit asset) |
| `product-breakdown-static-generator` | Collects buyer/offer/sales materials, asks quantity, then makes N product-breakdown static ad concepts in 7 layouts | needs-input | other:mixed, other:parameter |
| `quizinteractive-bot` | Generates 5+ quiz/poll-style static ad concepts (grid, binary, poll, spectrum, persona types) from buyer/offer/copy inputs | needs-input | context (any brand-kit asset) |
| `receipt-bot` | Turns offer/sales copy into 5 receipt-style static ad concepts (line items, pricing, paper style) across 5 archetypes, ready for design or image-gen. | needs-input | other:any-of |
| `reptile-triggers` | Turns ad copy into 20 visceral native-feeling static image concepts across 12 trigger types, ranks top 10 | multi-phase | ad-copy |
| `reptile-triggers-bot` | Turns pasted ad copy into 20 native-feeling, primal/reptile-brain static image concepts (10 hook + 10 body), ranked top-10, no product shots. | needs-input | ad-copy |
| `salespromotional-offer-bot-` | Turns offer/buyer/sales-copy input into 5 static promo ad concepts across 6 layouts, with visual, layout & color notes. | needs-input | context (any brand-kit asset) |
| `scientific-study-bot` | Generates clinical/medical-imagery static ad concepts (scans, X-rays, thermal maps) across 8 layout archetypes, 5 at a time | needs-input | context (any brand-kit asset) |
| `screenshotchatnotification-transformer-bot` | Turns product/offer/copy into 5 fake-chat or notification-stack static ad concepts (4 variants + 1 wildcard) with full design notes. | needs-input | context (any brand-kit asset) |
| `side-by-sidebefore-and-after-bot-` | Turns buyer profile, offer brief, copy blocks & sales copy into 5+ before/after static ad concepts across 7 layouts. | needs-input | context (any brand-kit asset) |
| `static-ad-sign` | Turns buyer/offer/sales-copy inputs into N 'person holding sign' UGC static ad concepts (person, sign copy, location) | needs-input | buyer-profile | offer-details | ad-copy | landing-page-copy | landing-page-url |
| `static-ad-specialist` | Brief + 1 of 20 concept styles → one image-gen-ready static ad prompt: visual scene, <10-word headline, layout specs | self-serve | creative-brief, other:concept-style-name |
| `static-swipe-bot-` | Upload a winning static ad; get its layout/psychology blueprint rebuilt into a full image-gen concept brief for your product. | needs-input | swipe-example |
| `statistic-ad-generator-bot` | Turns offer/buyer/sales copy into 10 statistic-led static ad concepts (stat, claim, layout, disclaimer) for designers. | needs-input | other:raw-notes |
| `step-by-step-bot-` | Generates 5 step-by-step static ad concepts (numbered routines/protocols) across 8 layout archetypes, ready for design or image-gen. | needs-input | context (any brand-kit asset) |
| `testimonial-bot-` | Turns real customer quotes/reviews into 5 (or N) testimonial static-ad concepts across 7 layout archetypes, ready for a designer. | needs-input | customer-reviews |
| `ugc-bot-` | Generates organic-looking UGC static ad concepts (phone-photo style, casual voice) across 10 layout archetypes, 5 at a time | needs-input | context (any brand-kit asset) |
| `unaware-static-image-ads-bot` | Ranks 5-7 native reptile-brain image concepts from ad copy, then generates copy-paste MidJourney phone-photo prompts. | needs-input | ad-copy, other:reference-image |
| `writing-on-body-bot` | Turns offer/VSL copy into 5 handwritten-on-skin static ad concepts (comparison, transformation claim, or audience callout) with body-part rationale | needs-input | context (any brand-kit asset) |

## Creative Direction (2)

| slug | what it does | mode | needs |
|---|---|---|---|
| `ai-ads-character-casting-agent` | Brief in, full character cast out: 19-slot concept map, character dossiers w/ monologues, staging, and paired ad seeds. | multi-phase | creative-brief |
| `surprising-culprit-bot` | Generate 15 'surprising villain' marketing angles (unexpected everyday culprit + pseudo-science mechanism) for a product's problem. | needs-input | product-info |

## Utility (4)

| slug | what it does | mode | needs |
|---|---|---|---|
| `bot-builder-bot` | Designs a complete new bot system prompt from a concept (or surgically revises one with feedback) using an 8-block template system | needs-input | creative-brief |
| `linkedin-content-bot` | Builds a 10-concept LinkedIn hookboard, then drafts 3 voice-matched posts: engagement, authority, conversion. | multi-phase | context (any brand-kit asset) |
| `primer-prompt-builder` | Sorts a batch of winning ads verbatim into 4 primers (2 awareness buckets, hooks, headlines) for writer bots. | needs-input | winning-ad |
| `static-ad-info-extractor-bot` | Extracts an 8-field static-ad brief (product, audience, problem, promise, price, CTA, visuals, tone) from raw notes | needs-input | raw-notes |
