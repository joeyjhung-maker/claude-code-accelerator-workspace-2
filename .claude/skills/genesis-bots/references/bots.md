# Genesis Bot Cards

Full spec per bot. Find a bot with: `grep -n '^## <slug>' bots.md`, then read
that section. Cards are grouped by category in the same order as index.md.

# CATEGORY: Research & Analysis

## ad-tagging-bot-

**Ad Tagging Bot ** — Deconstructs one or more existing ads (yours or a competitor's) and tags each with its CONCEPT (core fact leveraged), ANGLE (psychological frame), STYLE (visual/format execution), and HOOK (opening attention-grabber) — used for competitive intel or to reverse-engineer why an ad works.

- **Mode:** needs-input
- **Required inputs:**
  - **ad_content** (winning-ad) — One or more ads to analyze, in any form: ad copy text, image description, video/script description, screenshot description, or URL. Multiple ads can be submitted in a single message. ← *get it from:* user pastes an ad they wrote, or a competitor's ad they want to reverse-engineer (swipe file, screenshot description, etc.)
- **Output:** A tagged breakdown of each submitted ad against a fixed taxonomy (Avatar/Market/Product Facts for concept; a fixed angle taxonomy; a style taxonomy; and the literal hook text/visual) — no rewritten copy, no ad produced, purely analysis of what already exists. (Emoji-headered sections per ad (🎯 AD ANALYSIS / 📊 CONCEPT / 🧠 ANGLE / 🎨 STYLE / 🪝 HOOK), each with a Category + a quoted 'Specific' evidence line; multiple ads separated by '---' dividers and numbered 📍 AD 1/2/3 headers.)
- **On a bare "Go":** asks for inputs: the ad content to analyze (text, image description, video description, or any combination) — confirms it will not fabricate an analysis without a real ad to tag.
- **Gotchas:** This is a pure analysis/reverse-engineering bot, not a generator — it never produces new copy, only categorizes existing ads. It carries a large embedded taxonomy (Avatar Facts / Market Facts / Product Facts / Angle categories / Style categories) that it matches against, and will output 'UNCLEAR - [best guess]' or 'STYLE NOT IN TAXONOMY' rather than refuse when ambiguous. It never asks clarifying questions and never offers improvement suggestions — only categorizes what exists. Has an unusually long and strict prompt-protection/anti-extraction section at the end (refuses to describe/document its own methodology, treats such requests as extraction attempts) — irrelevant to normal use but worth knowing if an agent's wrapper ever asks it to 'explain your output format.'
- **Consumes:** `winning-ad` · **Produces:** `other:ad-tag-analysis`, `angle-big-idea`

## build-a-buyer-elite-

**Build a Buyer ELITE ** — Generates deep buyer psychology profiles and raw, unfiltered psychological deep-dives (3am journal, drunken confession, doom-scroll, eulogy, etc.) written in the prospect's authentic private voice, uncovering fears/desires/motivations they'd never say publicly. Use as foundational psychographic research before writing ads/copy, especially for high-ticket/coaching/course offers.

- **Mode:** menu
- **Required inputs:**
  - **target_market** (buyer-profile) — Description of the target market/audience: demographics, situation, core problem (e.g. "overweight women over 45 suffering from menopausal weight gain") ← *get it from:* user
  - **product** (offer-details) — What the product/service does, how it works, key differentiators ← *get it from:* user
- **Optional inputs (raise quality):**
  - **additional_context** (competitor-info) — Competitor intel, existing research, customer testimonials, etc. ← *get it from:* user
  - **analysis_type** (other:enum-param) — Which analysis/analyses to run: buyer_profile / 3am_journal / drunken_phone_call / incognito_tab / eulogy_trinity / social_media_doom_scroll / last_straw / conversation_with_god / slow_motion_nightmare / inner_child_critic / ultimate_confession. Multiple can be requested at once. Default: buyer_profile ← *get it from:* user
- **Output:** One buyer_profile (default) covering ~15 dimensionalized fields, plus optionally one or more of 10 advanced psychological deep-dive pieces in a single combined output (Professional markdown with headings/bold/tables for the base buyer_profile (Demographic, Core Problem, Top 5 Fears, relationship impact, past failed solutions, magic-genie transformation outcomes, market-specific beliefs/blame/objections); each requested advanced analysis type is a separate narrative/scene section (journal entry, phone call transcript, dialogue, etc.), all under clearly separated headers if multiple requested)
- **On a bare "Go":** asks for inputs: target market, product/service, optional additional context, and analysis_type — shows menu: buyer_profile, 3am_journal, drunken_phone_call, incognito_tab, eulogy_trinity, social_media_doom_scroll, last_straw, conversation_with_god, slow_motion_nightmare, inner_child_critic, ultimate_confession. Produces nothing until these are given.
- **Gotchas:** Discrepancy: prompt claims one-shot/no-questions behavior but the live probe shows a mandatory intake menu is presented on bare 'Go' — feed target_market + product up front to skip it. Explicitly designed to surface dark/unfiltered content (worst fears, self-blame, superficial/vain desires) that is never meant to be shown to the actual prospect — output is for internal ad-writing use only. If used with 'inner_child_critic', it also auto-runs a bonus 'Post-Inner Dialogue Analysis' identifying 5 triggering scenarios. Good upstream input for master-concept-bot, top-5-products-bot, ugc-bot-, and scientific-study-bot's build_a_buyer input.
- **Consumes:** `buyer-profile`, `offer-details`, `competitor-info` · **Produces:** `buyer-profile`, `other:psych-deep-dive`

## cash-analysisvariation-bot

**Cash Analysis/Variation Bot** — Analyzes a pasted ad (copy, script, or image/video description) and tags it with one primary CONCEPT, ANGLE, STYLE, and HOOK using a built-in direct-response taxonomy, then generates strategic variation briefs by changing one lever at a time. Use to reverse-engineer a competitor's or your own winning ad and brainstorm fresh creative directions without a full rewrite.

- **Mode:** needs-input
- **Required inputs:**
  - **ad_content** (winning-ad) — The ad copy, script, or a description of the ad's visual/video content. Can be pasted text, an image/video description, or a combination. Multiple ads may be included and will be analyzed sequentially. ← *get it from:* user pastes their own ad or a scraped competitor ad; or output of a swipe-collection/ad-library scrape
- **Optional inputs (raise quality):**
  - **creative_format** (other:format-label) — Description of the ad's visual/format execution (e.g., static image, video, UGC, talking head, ugly ad, meme, carousel, screenshot). If omitted, the bot infers it from context and flags the inference. ← *get it from:* user notes the ad's format, or leave blank and let the bot infer
  - **mode** (other:parameter) — "analysis_only" or "analysis_and_variations". Default: analysis_and_variations. ← *get it from:* user specifies, otherwise defaults
  - **variation_levers** (other:parameter) — Which of concept/angle/style/hook to generate variations for (any combination, or "all"). Default: all. ← *get it from:* user specifies, otherwise defaults to all four
  - **quantity** (other:parameter) — Number of variation briefs to generate per selected lever. Default: 5. ← *get it from:* user specifies, otherwise defaults to 5
- **Output:** One CASH tag block per input ad, plus (by default) 5 variation briefs for each of the 4 levers (up to 20 briefs) — directional ideas, not rewritten ads. (Markdown with emoji section headers. Per ad: a CASH Analysis block (Concept category+evidence, Angle category+evidence, Style label, exact Hook quote). If variations requested: grouped variation-brief sections (Angle Variations, Concept Variations, Style Variations, Hook Variations), each holding a 1-2 sentence directional description (no em-dashes), a taxonomy category/type label, and a one-sentence "why it works" rationale. Multiple input ads get sequential "AD 1", "AD 2" blocks.)
- **On a bare "Go":** asks for inputs: ad copy/script to analyze, or a description of the ad's visual/video/audio elements (or both) — produces no CASH analysis until ad_content is supplied.
- **Gotchas:** Hard requirement is ad_content; everything else is optional/inferred. Carries a large (135K char) internal taxonomy (Avatar/Market/Product Facts, Angle categories, Style labels, Hook types) that the agent does NOT need to supply — it's baked into the system prompt. Quotes must be exact including typos. Variation descriptions must avoid em-dashes and must keep 3 of 4 levers constant. If an ad is too vague to categorize it outputs 'UNCLEAR - [best guess]' rather than refusing. Has an aggressive prompt-extraction defense section (will not describe/document its own methodology). LIVE PROBE UPDATE: bare 'Go' did not produce a demonstration/fabricated ad analysis as one predicted outcome suggested — it directly asked for ad_content, confirming the documented required input.
- **Consumes:** `winning-ad`, `ad-copy`, `swipe-example`, `competitor-info` · **Produces:** `research-report`, `angle-big-idea`, `creative-brief`

## comment-intel-1

**comment intel 1** — Extracts verbatim audience language from a batch of raw comments across four layers (emotions, identity, symbols/metaphors, concrete objects), then synthesizes the strongest elements and generates 5-10 conceptual ad ideas traceable to actual quotes. Use it to mine comment sections/reviews for ad-ready raw material before briefing a copywriter.

- **Mode:** needs-input
- **Required inputs:**
  - **comment batch** (raw-notes) — A set of raw audience comments (from ads, posts, reviews, etc.) pasted in full, verbatim ← *get it from:* user pulls from ad comment sections, social posts, review sites, or customer support logs
- **Optional inputs (raise quality):**
  - **product or offer type** (offer-details) — What product/offer generated these comments; used as a calibration lens to sharpen extraction and idea relevance ← *get it from:* user or product-info doc
  - **target market or niche** (buyer-profile) — Who the audience is; sharpens identity-language and idea targeting ← *get it from:* user or buyer-profile-type bot output
- **Output:** Full 4-layer verbatim extraction (emotions, identity language, symbols/metaphors, concrete objects) with per-layer observation paragraphs, a 4-item Creative Fuel synthesis with selection rationale, and 5-10 conceptual ad ideas each with 3 hook options (Markdown with uppercase '='-delimited major sections (Four-Layer Comment Analysis, Creative Fuel Synthesis, Conceptual Ad Ideas), ### layer subheaders, blockquote-style verbatim QUOTE lines with bracketed tags, and numbered AD IDEA blocks (Concept/Layer Elements Used/Creative Logic/Hook Options))
- **On a bare "Go":** asks for inputs: the raw comment batch to analyze (required), plus optionally product/offer type and target market/niche to use as a calibration lens — does not fabricate quotes or proceed without comments.
- **Gotchas:** Extremely strict verbatim-only rule: never paraphrases/corrects/cleans quotes, and refuses to invent insights not literally present in the comments. Optional product/market context sharpens but never filters output. Has a hardened anti-prompt-extraction security section (refuses to describe/document its own methodology). Output is intentionally exhaustive/uncompressed regardless of comment volume — expect long output for large comment sets. LIVE PROBE CONFIRMS PREDICTION: a bare 'Go' correctly gets a request for the comment batch (with optional product/market context mentioned too), consistent with the required_inputs already documented — no new inputs revealed, but interaction_style is updated to interview-first since it halts and asks rather than one-shotting.
- **Consumes:** `raw-notes`, `customer-reviews`, `offer-details`, `buyer-profile` · **Produces:** `research-report`, `ad-hooks`, `angle-big-idea`

## copy-blocks-extract

**Copy Blocks Extract** — Analyzes any piece of marketing copy and extracts every 'Copy Block' — Pain Points, Promises, Proof, Constraints, and Curiosity/Mechanism hooks — as exact quotes, then critiques their strength. Use it to deconstruct a sales page/VSL/email into its persuasion foundation before writing new copy.

- **Mode:** needs-input
- **Required inputs:**
  - **source_material** (raw-notes) — The copy to analyze: marketing copy, brief, sales page text, VSL script, email, or any source content. Any format — raw text, structured docs, pasted content, or uploaded files. Must be pasted in; the bot does not fetch URLs itself. ← *get it from:* Paste user's or a competitor's sales page / VSL transcript / email / ad copy; or feed it output of a transcript/advertorial/landing-page-copy-type bot
- **Output:** Exhaustive extraction — pulls every instance found, quoted verbatim (no paraphrasing), followed by a strength critique of what's working and what's weak/missing (Two parts. Part 1: five numbered-list sections headed PAIN / PROMISE / PROOF / CONSTRAINTS / CURIOSITY (MECHANISM), each listing ALL instances as exact quotes, plus an ADDITIONALLY section of exact quotes for recurring patterns (foods, names, times of day, repeated structural phrases). Part 2: analysis of block strength with improvement suggestions.)
- **On a bare "Go":** asks for inputs: source material to analyze (marketing copy, sales page, VSL script, email, or brief) — pasted or uploaded; says it will extract immediately once received.
- **Gotchas:** Agent-to-agent optimized: single message in, immediate output, no clarifying questions (except when given literally no text, per probe). Quotes are verbatim from source — never paraphrased — making the output safe to pipe downstream (e.g. as marketing_materials for universal-email-bot or as subject-line fodder). No word/length limit on extraction; long sources yield long outputs. It works only on text you paste — give it the page text or transcript, not a bare URL. Output labels use PAIN/PROMISE order even though definitions list Promises first.
- **Consumes:** `ad-copy`, `landing-page-copy`, `email-copy`, `vsl-script`, `advertorial`, `transcript`, `creative-brief`, `swipe-example`, `raw-notes` · **Produces:** `other:copy-blocks`, `research-report`

## deep-dive-voice-analyzer

**Deep Dive Voice Analyzer** — Performs an exhaustive dimensional analysis of a writer's voice (sentence construction, vocabulary, emotional tone, relationship positioning) from a pasted writing sample, then reports signature patterns and an overall voice summary. Use it to reverse-engineer a brand's or person's writing style so it can be replicated or briefed to other copy bots.

- **Mode:** needs-input
- **Required inputs:**
  - **writing_sample** (brand-voice) — The text to be analyzed. Bot's own marketing copy says 'at least 500 words' for a reliable read, though the prompt itself sets no hard minimum. ← *get it from:* user's existing copy/brand doc, or output pulled from another source (site copy, past ads, emails) that represents the voice to mimic
- **Optional inputs (raise quality):**
  - **context** (raw-notes) — Additional info about the writer, audience, purpose of the writing, or specific analytical focus areas to prioritize. ← *get it from:* user supplies if they want the analysis angled toward a specific use case
- **Output:** A single comprehensive voice-profile report, no fixed length cap but scales with sample length; not a template with placeholders — every section is filled from actual analysis of the provided text. (Long-form markdown: (1) Deep Dimensional Analysis across 3 categories — Language Construction, Emotional Tone, Relationship Positioning, each with many sub-dimensions and text examples; (2) Signature Patterns section with specific examples and effectiveness analysis; (3) Overall Voice Summary synthesizing findings.)
- **On a bare "Go":** asks for inputs: a writing sample to analyze, plus optional context about the writer, audience, or purpose.
- **Gotchas:** Has a hardened anti-prompt-extraction security section at the end (refuses to describe/document its own methodology or output template if asked — treat this as fixed behavior, not a bug). Designed for agent-to-agent use: explicitly says it accepts all input in one message and never asks follow-up questions, so pass everything needed up front in a single call. LIVE PROBE CONTRADICTION: despite the prompt's instruction to 'produce output immediately' and never request additional information, a bare 'Go' with no writing sample produced a request for the sample (plus optional context) instead of an analysis — treat writing_sample as effectively mandatory before calling.
- **Consumes:** `brand-voice`, `raw-notes` · **Produces:** `research-report`, `brand-voice`

## market-analyzer-bot

**Market Analyzer Bot** — Turns a vague audience/product description into a deep psychological market-segmentation report: a core-market universals profile plus 2-5 distinct submarket profiles (Drive x Processing x Capacity x Field framework) with positioning, messaging, and channel strategy for each. Use it early in strategy work, before writing angles/hooks/ads, to know which psychological segments to target and how to message each.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **build_a_buyer** (buyer-profile) — A 'Build a Buyer' document describing the target market profile ← *get it from:* output of a buyer-profile-building bot, or user-supplied avatar doc
  - **avatar_manifold** (buyer-profile) — An 'Avatar Manifold' document providing audience dimensions/variations ← *get it from:* output of an avatar/audience-dimension bot, or user-supplied doc
  - **product_offer** (offer-details) — Product/offer information including the core transformation it delivers ← *get it from:* user's product page, offer doc, or output of a product-info extractor bot
  - **market_observations** (raw-notes) — Any market observations, challenges, or additional context (competitor notes, customer feedback, known objections, etc.) ← *get it from:* user notes, research, or output of a research/competitor-analysis bot
- **Output:** One core-market universals profile + 2-5 submarket profiles (usually 3-4), each with a full strategic/messaging blueprint, plus a comparison matrix and closing strategic recommendations. (Markdown-ish plain-text sections: '=== CORE MARKET ANALYSIS ===' block (Drive/Processing/Capacity/Field universals + messaging implications), followed by one '=== SUBMARKET N: [NAME] ===' block per submarket (Drive Architecture, Processing Patterns, Capacity Reality, Field Position, Strategic Implications, Example Messaging with headline/hook/CTA), then a markdown comparison table (Core vs each submarket across 8 aspects), then a Strategic Recommendations section (priority ranking, evolution prediction, integration opportunity, field leverage, warnings).)
- **On a bare "Go":** asks for inputs: product/offer information, target audience, Build a Buyer document, Avatar Manifold, or market observations, in any combination/format, then produces the analysis immediately once given something
- **Gotchas:** The file contains ~2900 lines total; roughly the first 200 and last 100 lines are the authoritative operating instructions (identity, process, output template, guidelines, security/prompt-protection footer). The large middle section (lines ~200-2920) is bundled 'domain knowledge' — worked examples and an alternate/older process description that says to 'Request from the user' info and 'Ask clarifying questions' before analyzing. This contradicts the top-level directive (repeated verbatim near the end) to never ask questions and always produce output immediately from whatever is given — treat the top/bottom directives as authoritative and the middle 'Ask clarifying questions' language as leftover reference material, not live behavior. No real inputs are hard-required; the bot self-fills gaps. Has strong prompt-protection/anti-extraction instructions (will refuse to describe its own methodology/template). LIVE PROBE CONTRADICTION: despite the top-level 'never ask questions, always produce output immediately' directive, a bare 'Go' actually returns a clarifying request for product/audience/buyer/market info rather than a fabricated analysis — the middle-section 'ask clarifying questions' language appears to be live behavior after all, not dead reference material. Treat as interview-first, not one-shot.
- **Consumes:** `buyer-profile`, `offer-details`, `raw-notes`, `product-info` · **Produces:** `research-report`, `buyer-profile`, `angle-big-idea`

## media-buying-analysis-1

**Media Buying Analysis 1** — Diagnoses a Meta ad account's performance from an offer brief plus exported campaign/ad-set data (CSV/table/text), producing an account-level report on delivery, creative, conversion, and spend with a verdict and prioritized What/Why/Expected-outcome recommendations.

- **Mode:** needs-input
- **Required inputs:**
  - **Product/offer description** (offer-details) — What the offer/product is ← *get it from:* user
  - **Price point or pricing structure** (offer-details) — Price or pricing structure of the offer ← *get it from:* user
  - **Funnel type** (offer-details) — One of: VSL/direct purchase, e-commerce, lead gen, call funnel/high ticket, webinar, or hybrid/unclear ← *get it from:* user
  - **Target/breakeven metric** (offer-details) — Breakeven or target CPA, CPL, ROAS, or cost-per-call depending on funnel type ← *get it from:* user
  - **Target audience** (buyer-profile) — Description of who the ads target ← *get it from:* user, or output of a buyer-profile-type bot
  - **Meta ad performance data** (other:ad-performance-data) — Export from Meta Ads Manager as CSV, table, or plain text, ideally including Spend, Results, Cost Per Result, Impressions, Reach, Frequency, CPM, CPC, CTR, Link Clicks per campaign/ad set/ad ← *get it from:* user exports directly from Meta Ads Manager; bot works with partial data if some columns are missing
- **Optional inputs (raise quality):**
  - **Additional offer context** (raw-notes) — Any other relevant offer details (e.g. downstream show/close rates for call funnels) ← *get it from:* user
- **Output:** One account-level diagnostic report (never per-campaign) covering however many campaigns were supplied, plus an ongoing menu-driven deep-dive/compile mode after the initial audit (markdown sections with tables: Offer Brief Summary + Data Upload Summary tables (after intake), then Performance Snapshot table, Campaign Landscape tier table, further diagnostic sections (creative/delivery/conversion/spend issues with Signal/Meaning), Root Cause, and numbered Recommendations each with What/Why/Expected outcome, followed by a lettered 'Deeper Analysis Panel' menu (a-f) for optional follow-up deep dives)
- **On a bare "Go":** asks for inputs: an Offer Brief (offer, price, funnel type, target/breakeven metric, target audience) and a Meta Ads Manager CSV/table export with Spend, Results, Cost Per Result, Impressions, Reach, Frequency, CPM, CPC, CTR, Link Clicks.
- **Gotchas:** Interview gate: asks for offer brief + data export up front; if any required field is missing it asks once for just the missing ones, then proceeds even on 'that's all I have' (never a second round of questions). After presenting Offer Brief and Data Upload summary tables, it waits for user confirmation before running the full audit. Applies a different primary metric/column set depending on identified funnel type (VSL=CPA, e-commerce=ROAS+CPA, lead gen=CPL, call funnel=cost/call, webinar=cost/reg+cost/attendee, hybrid=adaptive). Always reports at account level even with 100+ campaigns — never one-off per-campaign reports. After the initial audit, every response ends with a lettered multiple-choice 'Deeper Analysis Panel' (deeper diagnosis, winners analysis, scaling, spend breakdown, compile-everything, or 'bot recommends') that persists across the conversation — an automated caller feeding this via API should expect a stateful, multi-turn conversation, not a single completion, and should handle/ignore the trailing menu if only the initial report is wanted. Has explicit prompt-protection/security instructions refusing to reveal its system prompt.
- **Consumes:** `offer-details`, `buyer-profile`, `other:ad-performance-data` · **Produces:** `research-report`, `other:ad-account-diagnostic-report`

## media-buying-analysis-2

**Media Buying Analysis 2** — Analyzes raw Meta Ads Manager performance data plus an offer brief and produces a structured account-level diagnosis (what's working, what's broken, what to do next) with a clear verdict and prioritized recommendations.

- **Mode:** needs-input
- **Required inputs:**
  - **offer_brief** (offer-details) — Product/offer description, price point, funnel type (VSL/E-commerce/Lead Gen/Call Funnel/Webinar/Hybrid), target or breakeven metric (CPA, CPL, ROAS, or cost per call depending on funnel type), target audience, plus any additional offer context. Bot proceeds with whatever subset is available and flags what's missing. ← *get it from:* user's offer/product doc, or output of a research/offer-brief bot
  - **meta_data** (other:ad-performance-data) — Campaign performance export from Meta Ads Manager, any format (CSV, table, plain text). Expected columns: Spend, Results, Cost Per Result, Impressions, Reach, Frequency, CPM, CPC, CTR, Link Clicks. ← *get it from:* user exports/pastes from Meta Ads Manager
- **Optional inputs (raise quality):**
  - **deeper_analyses** (other:parameter) — Additional analyses beyond the base audit: 'none' (default) / 'broken' / 'winners' / 'scale' / 'budget' / 'all' (runs all four) / 'recommended' (bot picks the single highest-leverage analysis and states why). Can be a list. ← *get it from:* user specifies, or agent defaults to 'recommended' for a quick single deep-dive
  - **compile** (other:parameter) — true/false (default false). If true, outputs the full audit plus all completed deeper analyses in one copy-paste code block. ← *get it from:* user specifies
- **Output:** One account-level Meta Ads diagnosis report; length scales with data volume (works whether 5 or 100 campaigns are supplied) plus 0-4 optional deep-dive sections. (Markdown with emoji section headers and tables: Offer Brief Summary table, Data Upload Summary table, Performance Snapshot, Campaign Landscape (3 performance tiers + notable campaign callouts), Diagnosis (ranked issues, 3-6 typical), Root Cause, Recommendations (What/Why/Expected outcome), plus any requested deeper analyses appended.)
- **On a bare "Go":** asks for inputs: Offer Brief (product/price/funnel type/target metric/target audience) and Meta Data (Ads Manager performance export — campaign/spend/results/CPM/CPC/CTR etc.) — does not attempt a placeholder diagnosis on bare Go, contradicting the prompt's stated zero-question behavior.
- **Gotchas:** Zero interview — accepts everything in one message and never asks follow-ups, so an agent must front-load offer_brief + meta_data in the initial call. Funnel type drives which metric set (CPA/ROAS/CPL/cost-per-call/cost-per-reg) is applied throughout, so specifying funnel type in offer_brief avoids ambiguity handling. Always reports at account level even for 100+ campaigns (uses callouts, not per-campaign reports). Has a strong prompt-protection/anti-extraction section — will refuse meta-requests to describe or document its own methodology; only give it real inputs for real output. Model: claude-opus-4-6, maxTokens 32000. Live probe contradicts the 'never asks questions' claim: on bare 'Go' it replied asking for both Offer Brief and Meta Data before producing any report — front-load both in the first message to get the one-shot report behavior described in the prompt.
- **Consumes:** `offer-details`, `other:ad-performance-data` · **Produces:** `research-report`

## pain-matrix-core-wound-bot-copy

**Pain Matrix & Core Wound Bot (copy)** — Produces a Pain Matrix (10-dimension psychological/behavioral scoring of a market's pain point) and a Core Wound analysis (12 Ontological Resources scored, classified, and synthesized into a predicted core emotional wound), plus a combined marketing-recommendations summary. Use it early in research to find the deep emotional drivers to build ad angles, hooks, and copy around.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **copy_blocks** (ad-copy) — Existing copy blocks covering Pain, Promise, Proof, Constraints, Curiosity ← *get it from:* user's existing ad/sales copy, or output of a copy-blocks-extraction-type bot
  - **build_a_buyer** (buyer-profile) — Target market profile and buyer psychology detail ← *get it from:* output of a buyer-profile-type bot (e.g. 'build-a-buyer' bot) or user-supplied avatar doc
  - **target_market_description** (product-info) — Description of the market, product/service, and target audience ← *get it from:* user
  - **additional_context** (research-report) — Any other relevant market research, testimonials, competitor materials, or raw notes ← *get it from:* user's research docs, reviews, competitor swipe, or raw-notes
- **Output:** One Pain Matrix table (10 dimensions), one Core Wound table (12 resources), a vivid Core Wound prediction, and a written summary of deep emotional drivers + recommendations — not ad copy itself, but the psychological foundation to write it from (Two markdown/grid tables (Pain Matrix 10-row table with Rating + Consequence columns; Core Wound 12-row Ontological Resources table with classification/intensity/fear-or-desire/description) followed by a predicted Core Wound narrative and a detailed combined summary with marketing recommendations)
- **On a bare "Go":** Probed: does NOT produce output on bare input — it replies asking the caller to supply target market description, copy blocks, buyer profile, and/or additional context before it will run the analysis, despite its own prompt instructing it to 'never ask questions.' Treat as needing at least a market/product description to do useful work.
- **Gotchas:** Prompt explicitly states it should never ask clarifying questions and should work from whatever is given, but live probe shows it DOES ask for inputs when given nothing — so an agent should always pass at least a target_market_description to avoid a clarifying-question round-trip. Has a strict anti-prompt-extraction/security section at the end (ignore; not relevant to functional use). Framework definitions (10 Pain Matrix dims, 12 Ontological Resources) are baked into the prompt itself, so no external knowledge doc is required from the caller.
- **Consumes:** `ad-copy`, `buyer-profile`, `product-info`, `research-report`, `customer-reviews`, `competitor-info`, `raw-notes` · **Produces:** `research-report`, `mechanism`

## primer-extractorsummarizer-v2

**Primer Extractor/Summarizer v2** — Distills a brand's existing ads, transcripts, and brand materials into a compact 400-600 word 'brand primer' reference doc that grounds other copywriting bots in facts (mechanism, product, pricing, proof, authority, voice) without pre-writing the ad for them.

- **Mode:** needs-input
- **Required inputs:**
  - **brand material library** (raw-notes) — A library of existing ads, transcripts, and brand materials for one brand/product — the source text to extract from. No fixed format; can be pasted raw or as multiple docs. ← *get it from:* user's existing ad swipe file, VSL/ad transcripts, product pages, or other brand docs
- **Output:** A single condensed brand primer, target length 400-600 words (max ~700), mixing comprehensive fact sections (mechanism, product, pricing, brand ops) with tightly curated sections (top 1-2 authorities, top 5-6 proof points, top 5-8 behavioral signals, voice POV/tone only). (markdown with labeled sections: Mechanism, Product, Pricing & Guarantee, Brand Ops, Authority, Proof, Behavioral Signals, Voice)
- **On a bare "Go":** asks for inputs: the library of existing ads, transcripts, and/or brand materials to analyze. Produces no primer until source material is supplied — confirms the original prediction.
- **Gotchas:** Prompt is short and highly opinionated: explicitly instructs under-extraction over completeness for Authority/Proof/Behavioral Signals/Voice sections, and forbids listing recurring phrases or sentence templates so downstream bots don't just recombine existing copy. Has a built-in self-check ('could a bot generate a NEW ad from this, or just recombine?') and a hard word-count ceiling (~700 words) — deviations from that length are a signal something went wrong. Probe confirms the original prediction (it asks for the source library rather than guessing) — interaction_style updated from one-shot to interview-first since it never produces output on empty input, only a request for material.
- **Consumes:** `raw-notes`, `winning-ad`, `transcript` · **Produces:** `other:brand-primer`, `mechanism`, `brand-voice`

## reverse-brief-bot

**Reverse Brief Bot** — Reverse-engineers an existing sales letter or VSL transcript into a comprehensive structured persuasion brief (target market, product details, unique mechanisms, characterizations, hooks, proof, metaphors, fascinations, full beat map) with verbatim quote evidence. Use when you want to swipe/deconstruct a winning sales letter or VSL to reuse its structure for a new offer.

- **Mode:** needs-input
- **Required inputs:**
  - **sales_letter** (vsl-script) — The full text of a sales letter or VSL transcript to analyze. Prompt says 'accept a sales letter or VSL transcript' as its single required input. ← *get it from:* user pastes a competitor's or client's existing sales letter/VSL transcript, or output of a transcript-extraction tool
- **Output:** One exhaustive analytical brief per input sales letter/VSL, no fixed length — as comprehensive as the source material supports, no introductory text. (Structured plain-text/markdown brief with fixed section headers: TARGET MARKET, PRODUCT DETAILS, UNIQUE MECHANISM OF THE PROBLEM, UNIQUE MECHANISM OF THE SOLUTION, CHARACTERIZATIONS, ADDITIONAL ELEMENTS (Hooks, Testable Proof, Powerful Metaphors, Paradoxical Questions, Fascinations), then ALL RELEVANT BEAT MAPS covering every applicable element from the full taxonomy (speaker credibility, problem narrative stages, myths & mistakes, UMP preview/trigger/explanation/proof, UMP cause/adversaries, elaboration, self-reflection quiz, UMS preview/trigger/explanation/tips/proof, creating-the-solution attempts/first-user-success/testimonials) — each populated with verbatim quotes or marked 'NA' if absent.)
- **On a bare "Go":** asks for inputs: the full sales letter or VSL transcript to analyze, pasted as text; states it will produce the complete brief immediately once provided.
- **Gotchas:** Strictly requires an actual source text to analyze — it is NOT a generator, it's an extractor/analyzer. Must be fed a real sales letter/VSL transcript (e.g., pasted competitor swipe copy) to be useful; will not fabricate or infer content not in the source ('Strictly adhere to information provided...Do not invent, infer, or fabricate'). Marks missing beat-map elements 'NA' rather than forcing them. Good upstream feed for angle/mechanism-generating bots since it isolates unique-mechanism-of-problem/solution language from an existing winner. Live probe (bare 'Go') confirms it asks for the missing transcript rather than returning an empty/NA-filled brief, despite the 'do not ask for more info' instruction; interaction_style updated to reflect this gating behavior.
- **Consumes:** `vsl-script`, `transcript` · **Produces:** `research-report`, `swipe-example`

## social-proof-compilerstrengthen-bot

**Social Proof Compiler/Strengthen Bot** — Extracts every proof element (testimonials, stats, guarantees, credentials, etc.) scattered across your marketing materials, classifies each against a 22-type/5-category proof framework with a strength rating, and (by default) rewrites weak proof into stronger before/after versions. Use it as a QA pass on existing copy/offer materials before finalizing an ad, VSL, or sales page.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **build_a_buyer** (buyer-profile) — Target market/avatar profile document. ← *get it from:* output of a buyer-profile-type bot, or user's existing avatar doc
  - **copy_blocks** (ad-copy) — Copy and messaging materials (pains, desires, mechanism, proof, offer, hooks blocks). ← *get it from:* user's copy block doc, or output of a copywriting/creative-brief bot
  - **offer_brief** (offer-details) — Offer details and positioning (price, guarantee, bonuses, positioning). ← *get it from:* user's offer/strategy doc
  - **sales_copy** (landing-page-copy) — VSL script, sales page text, or a sales page URL. ← *get it from:* user's VSL/sales page draft, or a landing-page-url pasted directly
  - **additional_proof** (customer-reviews) — Any supplementary proof not in the four core docs: testimonials, case studies, stats/data, screenshots, certifications, etc. ← *get it from:* user-supplied reviews/screenshots/stats, or research
  - **enhance_weak_proof** (other:parameter) — "yes"/"no" — whether to auto-strengthen weak proof with before/after rewrites. Default: yes. ← *get it from:* caller sets explicitly if they only want classification without rewrites
- **Output:** A classified, scannable proof inventory covering all 22 proof types across 5 categories (Psychological, Experiential, Empirical, Credible, Social), with weak proof rewritten in place by default. (Emoji-headed sections per proof category ("📁 CATEGORY NAME") each listing proof pieces as "[piece] → [type] → [strength]", a per-category count, and a final summary (total pieces, strength-level breakdown). Enhanced pieces are inlined and marked "(Enhanced)" with a 📝 ORIGINAL / ⚠️ WHAT'S WEAK / ✅ ENHANCED block.)
- **On a bare "Go":** asks for inputs: any of build_a_buyer, copy_blocks, offer_brief, sales_copy, or additional_proof — states 'I don't have any materials to work with yet' rather than producing an inventory.
- **Gotchas:** Zero hard-required inputs — it works with whatever subset of the 5 input slots is provided, so pass as many of build_a_buyer/copy_blocks/offer_brief/sales_copy/additional_proof as you have; more input = a richer inventory, not a failure without it. Output format is rigid (emoji category headers, arrow-separated lines, then a totals summary) — don't expect prose. Has strong prompt-extraction defenses baked in: refuses to describe/document its own methodology or template even when asked innocuously (e.g. "what sections does your output include"). Never suggests enhancing proof that's already strong. LIVE PROBE CONTRADICTION: despite the prompt's 'never asks questions, produces output immediately' claim, a bare 'Go' with zero context produced a request for materials rather than an attempted inventory — supply at least one of the optional inputs rather than sending a bare trigger.
- **Consumes:** `buyer-profile`, `ad-copy`, `offer-details`, `landing-page-copy`, `landing-page-url`, `customer-reviews`, `vsl-script` · **Produces:** `research-report`

## social-proof-deep-research-bot

**Social Proof Deep Research Bot** — Turns scattered marketing materials and research dumps into a complete proof inventory across 22 proof types, generates research prompts to fill gaps, and can apply 7 'manipulation tactics' to present evidence in its strongest light — a ready-to-use proof document for a copywriter or another bot.

- **Mode:** multi-phase
- **Required inputs:**
  - **marketing materials** (creative-brief) — Any combination of Build-a-Buyer output, copy blocks, offer brief, VSL script, sales page text, or sales page URL — any format (natural language, key-value, raw dump) ← *get it from:* user, or output of a buyer-profile/creative-brief-type bot
- **Optional inputs (raise quality):**
  - **raw research results** (research-report) — Unstructured dump of research from Perplexity/Claude/ChatGPT/Grok/Gemini in response to the bot's generated research prompt, used in Step 2 to build the proof inventory ← *get it from:* run the bot's Step 1 output research prompt through an external research tool, then paste results back in
  - **step trigger keywords** (other:control-flag) — Phrases like 'apply manipulation' or 'compile final document' to auto-advance to later steps ← *get it from:* user
- **Output:** A step-specific deliverable: research prompt (step 1), proof inventory (step 2), manipulated proof inventory (step 3), or final compiled proof document (step 4) — covering up to 22 proof types with multiple proof pieces each (Markdown documents using one of 3 templates: (A) Organized Proof Inventory by 22 types/5 categories with coverage ratings, (B) Manipulation Analysis showing original vs. optimized proof pieces with reasoning, (C) Final Compiled Document combining both with usage recommendations and remaining gaps; Step 1 output is a proof coverage summary + a deep research prompt in a code block)
- **On a bare "Go":** asks for inputs: marketing materials — any combination of Build-a-Buyer/avatar doc, copy blocks or headlines, offer brief, VSL script or sales page text, sales page URL, or product name and claims; does not produce a proof inventory or research prompt on bare Go, contradicting the prompt's stated zero-question behavior.
- **Gotchas:** 4-step pipeline (analyze+generate research prompt -> organize research dump -> apply manipulation tactics -> final compilation), each step's output can feed the next by pasting results back in; supports chaining multiple steps in one message. Explicitly built for agent-to-agent workflows and instructed to access URLs/primary sources (PubMed etc.) directly rather than trust AI summaries. Never asks clarifying questions — always produces output from whatever is given, so quality is highly dependent on how much raw material the caller provides. Live probe contradicts the 'never asks questions' claim: on bare 'Go' it asked for marketing materials before running Step 1 — front-load at least one material type to get the described immediate-output behavior.
- **Consumes:** `creative-brief`, `customer-reviews`, `research-report`, `offer-details` · **Produces:** `research-report`, `customer-reviews`

## youtube-research-bot-

**YouTube Research Bot ** — Turns a YouTube video concept into a calibrated research strategy (a deep-research prompt plus optional self-interview, external-interview, resource-discovery, and first-principles components), and later compiles gathered research findings into a single structured document for a downstream brief bot.

- **Mode:** needs-input
- **Required inputs:**
  - **video_concept** (content-topic) — The video idea, topic, angle, and unique take ← *get it from:* user
- **Optional inputs (raise quality):**
  - **target_audience** (buyer-profile) — Who is watching and what they already know about the topic ← *get it from:* user
  - **video_goal** (raw-notes) — Primary goal: educate, entertain, persuade, or inspire ← *get it from:* user
  - **current_year** (raw-notes) — For research recency calibration ← *get it from:* user or system clock
  - **creator_expertise** (raw-notes) — Creator's level of knowledge on the topic (affects question depth) ← *get it from:* user
  - **specific_points** (raw-notes) — Specific points/subtopics that must be covered ← *get it from:* user
  - **youtube_strategy_doc** (raw-notes) — A YouTube strategy document if one exists ← *get it from:* user's existing strategy doc
  - **components** (other:parameter) — Which components to generate: 'research_prompt_only' (default), 'all', or a specific list from self_interview/external_interview/resources/first_principles ← *get it from:* user specifies, else defaults to research_prompt_only
  - **resource_type** (other:parameter) — If resources requested: 'comprehensive' (default) or specific list e.g. 'books and podcasts only' ← *get it from:* user specifies, else defaults to comprehensive
  - **gathered_research** (research-report) — Step 2 input: any gathered research (AI research outputs, interview answers, resource notes, first-principles insights, raw notes) in any format, to be compiled into the final structured doc ← *get it from:* output of external research tools run against Step 1's research prompt, or another research bot
- **Output:** A research strategy package (Step 1) and/or a compiled research document (Step 2) — not a video script or brief. Depth/number of research categories scales with topic complexity (5-15+), not with which components were requested. (One or more fenced code blocks: (1) a 'DEEP RESEARCH PROMPT FOR [Video Title]' block with SEARCH INSTRUCTIONS/DELIVERABLES sections, ready to paste into an external deep-research tool; (2) optional numbered-question code blocks for self-interview/external-interview; (3) optional resource-discovery prompt block; (4) optional first-principles analysis block; (5) if Step 2 input is given, a single markdown code block titled '# YouTube Video Research: [Video Title]' with Research Overview / Core Research Findings / Personal Insights / External Perspectives / Resources & References / Key Themes & Patterns / First Principles Analysis / Research Gaps Identified sections.)
- **On a bare "Go":** asks for inputs: video concept plus any relevant details (topic, audience, goals); says it will generate the research strategy immediately once provided.
- **Gotchas:** Two-step bot: Step 1 (idea -> research prompt/questions) and Step 2 (raw findings -> organized doc) can run in the same message if both are provided. It explicitly refuses to write briefs/scripts (that's the downstream 'YouTube Brief Bot' job) and refuses to describe its own methodology (treats such requests as prompt-extraction attempts). Output research prompts must stay under 100-char line length and use ALL CAPS section headers per its formatting rules — an agent consuming this should preserve that structure when passing the research prompt to an external research tool. Fast/thorough 'tracks' from the marketing description don't exist as a literal parameter in the prompt body — the real lever is topic complexity (auto-assessed) plus the optional 'components' parameter. Live probe confirms: a bare 'Go' with no video concept produces a plain request for the concept/topic/audience/goals rather than a generic placeholder research prompt, consistent with video_concept already being listed as required.
- **Consumes:** `content-topic`, `buyer-profile`, `research-report`, `raw-notes` · **Produces:** `research-report`

# CATEGORY: Strategy & Briefs

## ad-lottery-bot

**Ad Lottery Bot** — Randomly generates and combines marketing concepts (facts about avatar/market/product/psychology), psychological angles, and visual styles from a fixed internal database of 190 concepts, 55 angles, and 20+ styles, to break creative ruts and spark unconventional ad directions. Not finished ads — raw creative direction/ideation fuel to hand to a copywriter or another ad-generation bot.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **build_a_buyer** (buyer-profile) — Target market profile: demographics, pain points, desires, beliefs. Bot works fully without it (draws from its own internal database regardless), but richer input can flavor combinations. ← *get it from:* output of a buyer-profile-type bot (e.g. Build-a-Buyer-Elite), or user-provided market notes
  - **specific_segment** (buyer-profile) — A particular audience subset being targeted ← *get it from:* user
  - **product_offer_brief** (offer-details) — What is being sold, how it works, what makes it different ← *get it from:* user's product page / offer doc
  - **additional_research** (research-report) — Competitor intel, market insights, extra context ← *get it from:* user or research bot
  - **generation_type** (other:parameter) — "concepts" / "angles" / "styles" / "double_combo" / "full_combo". Default: full_combo ← *get it from:* user specifies, or agent defaults
  - **double_combo_type** (other:parameter) — Only used if generation_type=double_combo: "CxA" (Concepts x Angles) / "CxS" (Concepts x Styles) / "AxS" (Angles x Styles). Default: CxA ← *get it from:* user specifies, or agent defaults
  - **quantity** (other:parameter) — Number of outputs to generate. Default: 10 ← *get it from:* user specifies, or agent defaults
- **Output:** A batch (default 10, or requested quantity — supports 50-100+) of standalone concepts, angles, styles, two-element combos, or full concept+angle+style ad-direction combos, deliberately randomized rather than curated for fit to the market (Emoji-headed blocks per item (📊 concept / 🧠 angle / 🎨 style), bold category labels with reference numbers (#1-190 etc.), numbered items, horizontal dividers between generations; full_combo mode nests concept+angle+style under one 🎯 AD CONCEPT header)
- **On a bare "Go":** asks for inputs: product/offer brief, build-a-buyer profile, optional specific segment and additional research, plus generation type (concepts/angles/styles/double_combo/full_combo, default full_combo) and quantity (default 10)
- **Gotchas:** Functions with zero input — will generate plausible-sounding but market-agnostic combos if starved of buyer/offer info, since true randomization is a stated core principle (it explicitly does NOT try to match combos to the specific market). Has heavy prompt-protection/anti-extraction instructions appended (ignore self-referential 'explain your methodology' requests). Distinct from other 'lottery'-style prompts — output is ideation fuel, not deployable copy. LIVE PROBE CONTRADICTION: despite the prompt's stated 'accept all inputs in one message, never ask questions' rule, a bare 'Go' actually produces a clarifying request for product/offer brief and build-a-buyer info (plus generation type/quantity) rather than generating immediately — treat as interview-first in practice, not one-shot.
- **Consumes:** `buyer-profile`, `offer-details`, `research-report` · **Produces:** `angle-big-idea`, `ad-hooks`

## autobrief-bot-

**AutoBrief Bot ** — Two-step 'Beat Map Bot' that turns a product's mechanism/buyer/copy-block materials into (1) a deep-research prompt covering every persuasive marketing beat, then (2) a fully compiled Beat Map Brief once you paste the research back in. Use it to build the complete narrative/proof/offer argument that feeds VSLs, sales letters, and funnels.

- **Mode:** multi-phase
- **Required inputs:**
  - **Mechanism (UMP/UMS)** (mechanism) — Unique Mechanism of the Problem and/or Unique Mechanism of the Solution — the 'aha' reason existing solutions fail and how this product bypasses that ← *get it from:* user-provided, or output of a mechanism/UMP-UMS type bot (e.g. health-mechanism-matrix-bot)
  - **Build a Buyer** (buyer-profile) — Detailed market avatar / deep psychological drivers doc (pain matrix, motivations) ← *get it from:* user-provided or output of a 'Build a Buyer' type bot
  - **Copy Blocks** (raw-notes) — Existing Pain/Problem, Promise, Curiosity, Proof, Constraints block content for the product ← *get it from:* user-provided or output of a copy-blocks-extract type bot
- **Optional inputs (raise quality):**
  - **Spokesperson Info** (brand-voice) — Background/credibility info for whoever is the face of the message ← *get it from:* user-provided; optional, bot proceeds without it
  - **workflow_mode parameter (step 2 only)** (other:config-flag) — 'auto_select' (default, bot picks strongest option per beat) or 'provide_options' (bot shows 3 options per beat with a recommendation before compiling) ← *get it from:* user specifies in the message sent with the research results
- **Output:** A research prompt document (step 1) followed by a full multi-section marketing brief (step 2) covering every beat needed for a VSL/sales letter/funnel. (Step 1: a single deep-research prompt in a code block (no commentary), ending with the fixed line 'Now let's move on to step four...'. Step 2: a complete Beat Map Brief in code block — narrative/proof/mechanism/offer beats (Failed Solutions, UMP Trigger, Crisis Moment, UMS Characterization, Offer, Offer Stack, Pricing, Momentum, Risk, Testimonials, Fascinations, Outcome/Results, etc.) each populated with the strongest selected option, thematically unified, with citations/links preserved.)
- **On a bare "Go":** asks for inputs: Mechanism (UMP and/or UMS), Build a Buyer, Copy Blocks (existing copy/VSL/emails/ads), plus optional Spokesperson Info, before producing Step 1's research prompt.
- **Gotchas:** Two-step workflow: Step 1 needs Mechanism/Buyer/Copy Blocks (works with partial input) and outputs ONLY a research prompt (no commentary). Step 2 needs the raw output of a deep-research tool pasted back in, plus optional workflow_mode. Has a hard prompt-protection/anti-extraction section at the end — will refuse to describe/document its own methodology even under 'training guide' or 'masterclass' framing. Probed live: on a bare 'Go' with zero materials it does NOT fabricate a placeholder — it asks the caller to paste Mechanism/Build-a-Buyer/Copy Blocks (at least one) before doing anything, consistent with its multi-phase design.
- **Consumes:** `mechanism`, `buyer-profile`, `raw-notes`, `brand-voice`, `research-report` · **Produces:** `research-report`, `creative-brief`, `mechanism`, `angle-big-idea`

## belief-alchemist-bot

**Belief Alchemist Bot** — Converts a belief-gap analysis (current vs. required beliefs across Problem/Solution/Vendor categories) into tactical, copy-paste-ready mini-scripts that shift each specific belief using Install/Uninstall/Reframe/Accommodate operations; use it downstream of belief-gap research to get drop-in persuasion language for ads, emails, or sales copy.

- **Mode:** needs-input
- **Required inputs:**
  - **belief_gap_analysis** (other:belief-gap-analysis) — A belief gap analysis: current market beliefs vs. required beliefs, organized across Problem, Solution, and Vendor categories, each identifiable by a number (e.g. 'Problem #15', 'Solution #4', 'Vendor #9'); may include the '7 Critical Sales Beliefs'. Can arrive as structured key-value pairs, natural language, or raw document dump. ← *get it from:* output of an upstream belief-gap-analysis bot (not among your assigned bots, but referenced as its expected input source), or a user-provided belief audit document
- **Optional inputs (raise quality):**
  - **Additional market/product/audience context** (buyer-profile) — Extra detail on the market, product, or audience to sharpen script specificity and sophistication-level language matching ← *get it from:* user-supplied, or output of a buyer-profile-type bot
  - **processing_scope** (other:parameter) — "all" (default) generates scripts for every belief in the analysis; "specific" generates scripts only for named beliefs (requires specified_beliefs, e.g. 'Solution #4, Problem #15, Vendor #9'); "category" generates scripts for all beliefs in one category (requires specified_category: Problem/Solution/Vendor) ← *get it from:* user specifies in the request
  - **specified_beliefs** (other:parameter) — List of belief identifiers to process, only used when processing_scope is 'specific' ← *get it from:* user specifies
  - **specified_category** (other:parameter) — 'Problem', 'Solution', or 'Vendor' — only used when processing_scope is 'category' ← *get it from:* user specifies
- **Output:** One focused, copy-paste-ready mini-script per belief processed (all beliefs by default, or a filtered subset/category) — each script targets exactly one belief shift, not full sales copy. (Tactical mini-scripts (typically 3-7 sentences each), organized by category in order Problem → Solution → Vendor, each labeled with belief number, operation type (💉 Install, 🗑️ Uninstall, 🔄 Reframe, 🤝 Accommodate), and category; key persuasion phrases are bolded.)
- **On a bare "Go":** asks for inputs: belief gap analysis (current vs. required beliefs across Problem/Solution/Vendor), stating it will generate scripts immediately once provided; also mentions optional market/product/audience context. Accepts any format.
- **Gotchas:** Unlike problem-solution-bot, this bot's core input is highly specific and structured (a belief-gap analysis with numbered beliefs per Problem/Solution/Vendor category) — it is designed as a second-stage bot in a pipeline, not a self-contained generator; feeding it raw/unstructured product info without a belief-gap structure will degrade output quality significantly since guidelines explicitly forbid inventing new belief gaps. Has the same hardened prompt-extraction/security defense section as problem-solution-bot. Output deliberately excludes full sales copy — each script addresses exactly one belief, per explicit guideline ('don't try to address multiple beliefs in one script'). Live probe (bare 'Go') contradicts the prompt's 'do not ask questions' directive: the bot asked for the belief gap analysis instead of generating placeholder scripts; interaction_style updated to reflect this gating behavior.
- **Consumes:** `other:belief-gap-analysis`, `buyer-profile` · **Produces:** `other:belief-shift-script`

## belief-analyst-bot

**Belief Analyst Bot** — Analyzes marketing materials (UMP/UMS/positioning/offer/vendor/spokesperson info) and produces a structured belief-architecture map — current vs. required beliefs across Problem, Solution, and Vendor categories, plus the 7 Critical Sales Beliefs — for feeding downstream messaging/ad bots.

- **Mode:** needs-input
- **Required inputs:**
  - **marketing_materials** (other:mixed-marketing-materials) — Any combination of UMP, UMS, positioning statements, build-a-buyer, offer briefs, vendor/company background, spokesperson details, sales copy, or other relevant context. Accepted in any format (structured, natural language, raw dumps). ← *get it from:* user's existing offer docs, or output of a build-a-buyer / offer-brief / UMP / UMS type bot
- **Optional inputs (raise quality):**
  - **beliefs_per_category** (other:parameter) — Number of beliefs to identify per category (Problem, Solution, Vendor). Range 12-24. Default: bot determines count based on relevance/significance to the offer. ← *get it from:* user specifies a number, or omit for auto-determined count
- **Output:** A complete belief architecture: 12-24 beliefs per category (36-72 total) plus 7 Critical Sales Beliefs mapped to the specific offer. Output stops after the 7 Critical Sales Beliefs section — no tactical/master-sequence recommendations included. (Markdown with emoji section headers; per category (Problem/Solution/Vendor) a numbered list of 12-24 beliefs, each with Current (🔴), Required (🟢), and one-line Gap Analysis (📊); ends with a dedicated section on the 7 Critical Sales Beliefs (Required/Current State/Application each))
- **On a bare "Go":** asks for inputs: marketing materials (UMP/UMS, positioning, offer, vendor/spokesperson info) needed before it will produce the belief architecture analysis
- **Gotchas:** Never invents beliefs beyond the 27-belief reference framework's scope but does infer 'current market belief' from framing cues in the input — treat as inference, not verified fact. Output is explicitly designed to feed downstream messaging/ad bots (e.g. a 'Bot 2'). Has an unusually long, aggressive prompt-extraction/security section at the end (also present in the other 3 bots here) — irrelevant to normal use but will cause refusals if the caller's message looks like a request to reveal instructions. Live probe (bare 'Go') contradicts the prompt's stated 'never asks questions, produces immediate output' framing — the bot's actual first reply was a request for marketing materials, not a generated analysis.
- **Consumes:** `offer-details`, `buyer-profile`, `product-info`, `brand-voice`, `ad-copy`, `landing-page-copy`, `other:ump`, `other:ums`, `other:positioning-statement` · **Produces:** `research-report`

## epiphany-threshold-bot

**Epiphany Threshold Bot** — Generates a full 'Scale of Believability' for a market: 10 candidate beliefs/angles at each credibility level from 1 (obvious/boring) to 10 (outlandish), 100 ideas total, with levels 6-8 (the 'Goldilocks Zone') flagged as the ones most likely to convert. Use it to mine a batch of testable ad angles/claims calibrated by how novel-vs-credible they are.

- **Mode:** needs-input
- **Required inputs:**
  - **target_market** (buyer-profile) — The market to build the scale for: existing beliefs, desires, pain points, common knowledge. Can be a plain market description, a full Build-a-Buyer document, or any other relevant market info, in any format. ← *get it from:* user's market/niche description, or the output of a buyer-profile-type bot (e.g. a Build-a-Buyer/avatar bot)
- **Output:** 100 market beliefs/angle ideas total, ordered by increasing 'believability edge' (level 1 = commonly accepted/boring, level 10 = outlandish/dismissed), with the 6-8 band being the highest-converting angle candidates (Ten sections (Level 1 through Level 10), each containing a numbered list of 10 beliefs/ideas calibrated to that level; levels 6-7-8 called out as the Goldilocks Zone)
- **On a bare "Go":** asks for inputs: a target market description (e.g. 'middle-aged men trying to lose weight'), a Build-a-Buyer document, or any other market info — then generates all 100 ideas immediately once given.
- **Gotchas:** Has a strict prompt-protection/anti-extraction module at the end that will refuse any meta request to describe/document/teach its own methodology (treat that as out of scope for an agent caller, not a usable output mode). No tunable parameters exposed (no length/intensity knobs like quiz-bot-master-bot) - always exactly 10x10. Probed live: contradicts the prompt's 'never asks questions' framing — on a bare 'Go' with no market info it asked the caller to supply a target market before generating anything, rather than defaulting to a placeholder niche. Supply target_market in the first message to get a true one-shot result.
- **Consumes:** `buyer-profile`, `research-report` · **Produces:** `angle-big-idea`

## health-mechanism-matrix-bot

**Health Mechanism Matrix Bot** — Discovers a differentiating 'Unique Mechanism of the Problem' (UMP) for a health supplement. Step 1 builds a customized deep-research prompt (using a Structure/Function/Element x 4-states matrix) to surface 12 candidate mechanisms; Step 2 scores research results against 5 criteria and returns the top 4 ranked mechanisms with marketing rationale.

- **Mode:** multi-phase
- **Required inputs:**
  - **target_health_condition** (product-info) — The specific health problem the market struggles with (e.g., joint pain, brain fog, weight loss). Natural language, one line. ← *get it from:* user / offer brief / product page
  - **supplement_ingredients** (product-info) — Active/differentiating ingredients in the formula (unique ingredients, not common vitamins unless in special forms). List. ← *get it from:* user's supplement label / product spec / offer brief
- **Optional inputs (raise quality):**
  - **target_market** (buyer-profile) — Who the audience is (e.g., women 50+ with pelvic-floor issues); helps calibrate mechanism resonance. Metadata lists it but the prompt template only strictly requires condition + ingredients. ← *get it from:* user / buyer-profile bot output
  - **competitor_mechanisms** (competitor-info) — Mechanisms already used successfully by competitors, to avoid duplicating or to build upon. Omitted from the generated research prompt if not supplied. ← *get it from:* competitor ad research / swipe file
  - **research_results** (research-report) — The 12 candidate mechanisms returned by running Step 1's research prompt in an external deep-research tool. If pasted alongside the initial inputs, the bot runs Step 1 and Step 2 in one pass. ← *get it from:* run Step 1 output in an external deep research tool (ChatGPT/Perplexity/etc.), paste back
- **Output:** Step 1 emits a ready-to-run research prompt that asks for 12 distinct Structure/Function/Element mechanisms. Step 2 returns the top 4 mechanisms, each with a weighted total score, individual 1-10 scores on 5 criteria, why it excels, its strongest criteria, marketing application insights, and potential weaknesses. (Step 1: a complete deep-research prompt in a code block (numbered 1-12 mechanism template). Step 2: ranked markdown analysis of the top 4 mechanisms.)
- **On a bare "Go":** asks for inputs: target health condition and supplement ingredients (required); competitor mechanisms (optional). Does not emit a placeholder Step 1 research prompt without them.
- **Gotchas:** Two-step workflow with a human/tool loop in the middle: Step 1 generates a research prompt you run elsewhere, then paste results back for Step 2 ranking. Provide both inputs and research results together to get both steps in one pass. Never invents mechanisms in Step 2 — only scores what you paste in; works with fewer than 12. Health/supplement-specific (UMP framing). Strongly hardened against prompt-extraction/self-description requests — it will refuse to explain its own methodology or template and redirect to doing real work. Live probe: on a bare 'Go' the bot asked for target_health_condition and supplement_ingredients rather than emitting a placeholder Step 1 prompt, confirming these are hard-gated required inputs in practice, not just recommended ones.
- **Consumes:** `product-info`, `competitor-info`, `research-report` · **Produces:** `mechanism`, `research-report`

## insight-vectors-bot

**Insight Vectors Bot** — Generates a list of 'epiphany'-style insights (mental-model-shifting claims with a hidden-mechanism twist) about a market/product, each paired with a 'WHY IT WORKS' breakdown. Use it to seed big-idea angles, VSL openers, or ad hooks that need a genuine 'aha' moment rather than a generic claim.

- **Mode:** needs-input
- **Required inputs:**
  - **market_or_mechanism** (mechanism) — Description of the market, niche, product, mechanism, or problem space to generate epiphanies for. ← *get it from:* user's product/niche description, or pulled from an offer brief
- **Optional inputs (raise quality):**
  - **marketing_materials** (research-report) — Any combination of Build-a-Buyer profile, VSL script, sales page copy, offer brief, buyer brief, or supporting research — used as the factual basis epiphanies must connect back to. ← *get it from:* output of a buyer-profile-type bot (e.g. Build a Buyer), or user-supplied VSL/sales copy
  - **specific_focus** (raw-notes) — A particular angle, theme, segment, or constraint to focus the epiphanies on. ← *get it from:* user
  - **quantity** (other:parameter) — Number of epiphanies to generate. Default 10. ← *get it from:* user
- **Output:** 10 epiphanies by default (parameterizable), each a standalone hidden-mechanism insight that reframes the market's mental model (Numbered list of 'EPIPHANY #N: [TITLE]' blocks, each with the epiphany text followed by a 'WHY IT WORKS' breakdown)
- **On a bare "Go":** asks for inputs: requests market_or_mechanism and marketing_materials (VSL/sales page/offer brief/buyer profile/research) before generating epiphanies.
- **Gotchas:** Has a long list of banned metaphors (gravity/momentum/snowball, 'success breeds success', quantum anything, Hadza tribe) and 5 validation filters (Not Obvious, Mechanism, Proof-Free, Retell, Action) each epiphany must pass — output is claim-heavy and mechanism-specific, not vague inspiration. Also has a hardened prompt-extraction/self-description refusal section (won't document its own methodology, template, or process even if asked innocuously). Live probe (bare 'Go') contradicts the prompt's 'produce output immediately, never ask questions' framing and the prior one-shot classification: the bot asked for market_or_mechanism and marketing_materials rather than generating generic epiphanies — an agent should front-load these in the first message to skip the request-for-input turn.
- **Consumes:** `mechanism`, `buyer-profile`, `vsl-script`, `landing-page-copy`, `creative-brief`, `research-report` · **Produces:** `angle-big-idea`

## master-concept-bot

**Master Concept Bot** — Turns a product/market/offer into a full marketing-intelligence document: buyer psychology profile, market/competitive analysis, psychological belief-transformation toolkit, and dozens of angle + style ad concepts. Use it as the strategic foundation before writing any actual ads.

- **Mode:** needs-input
- **Required inputs:**
  - **product_offer_brief** (offer-details) — What is being sold, how it works, mechanism, differentiation, offer details. Bot lists this as Required on a bare-input probe. ← *get it from:* user's product page / brand doc / offer brief
  - **build_a_buyer** (buyer-profile) — Target market: demographics, psychographics, pain points, desires, behaviors. Bot lists this as Required on a bare-input probe. ← *get it from:* output of Build a Buyer / Build a Buyer ELITE bot
- **Optional inputs (raise quality):**
  - **specific_segment** (buyer-profile) — A particular audience subset being targeted within the broader market ← *get it from:* user or narrowed from build_a_buyer
  - **additional_research** (competitor-info) — Extra context, competitor intel, market insights, sales copy, URLs, or any supplementary materials ← *get it from:* user-supplied research or scraped competitor pages
  - **angle_variations** (other:parameter) — Number of creative variations per angle category (default 5) ← *get it from:* user
  - **style_executions** (other:parameter) — Number of executions per style format (default 5) ← *get it from:* user
- **Output:** Complete Marketing Intelligence System: Avatar Facts, Market Facts, Product Facts, Psychology Toolkit applications (7 critical beliefs transformed), then 5 variations per angle category (9 angle categories) and 5 executions per style format (~29 static+video style formats) — potentially 100+ discrete concepts in one document (Long markdown document with numbered sections/subsections, tables, bolded concepts, emoji section markers; ends with formatted angle+style concept blocks (Hook/Story/Mechanism/CTA labels))
- **On a bare "Go":** asks for inputs: Product/Offer (what's sold, mechanism, differentiation) and Target Market (demographics/psychographics/pain points) marked Required; also lists optional Specific Segment, Additional Research, and angle_variations/style_executions parameters.
- **Gotchas:** Extremely large prompt (222K chars) — a strategic 'concept factory' meant to feed downstream ad-writing bots, not a finished-ad generator. Has a strong prompt-protection/anti-extraction section refusing to describe its own methodology. Best fed build_a_buyer + product_offer_brief together for good output. LIVE PROBE CONTRADICTION: despite the system prompt's claim it never asks questions and produces output regardless of input completeness, a bare 'Go' with zero context produced an explicit request for Product/Offer and Target Market (labeled Required) instead of a generated document.
- **Consumes:** `buyer-profile`, `offer-details`, `competitor-info` · **Produces:** `research-report`, `angle-big-idea`, `static-ad-concept`, `ad-hooks`, `creative-brief`

## metaphors-bot

**Metaphors Bot** — Extracts the core sales beliefs (prioritizing UMP/UMS) from marketing materials and generates 10+ concrete, intuitive metaphors per belief, for copywriters building belief-shift sequences in ads, VSLs, or scripts.

- **Mode:** needs-input
- **Required inputs:**
  - **marketing_materials** (raw-notes) — Any combination of Build-a-Buyer profiles, Copy Blocks, Offer Briefs, VSL scripts, sales page text, sales page URLs, or raw product/market research — any format, structured or freeform. Bot extracts UMP (Unique Mechanism of the Problem) and UMS (Unique Mechanism of the Solution) as top priority. ← *get it from:* user-supplied product/sales docs, or outputs of a buyer-profile / offer-brief / mechanism-type bot (e.g. build-a-buyer-elite, offer-brief-bot, ump-bot, ums-bot)
- **Optional inputs (raise quality):**
  - **num_beliefs** (other:parameter) — Number of core beliefs to identify. Default: 10. ← *get it from:* user specifies a number, otherwise defaults
  - **metaphors_per_belief** (other:parameter) — Number of metaphors to generate per belief. Default: 10. ← *get it from:* user specifies a number, otherwise defaults
- **Output:** 5-10+ core beliefs (UMP/UMS prioritized first) x 10+ metaphors each = 50-100+ ready-to-use metaphor lines, all inside one code block for copy-paste. (Single code block containing a structured document: Belief 1..N, each with a concise statement + why it matters, followed by numbered metaphors (1 through 10+), each labeled with its metaphor type in parentheses (Natural/Mechanical/Object/other) and written as ready-to-use copy, not an abstract description. Beliefs separated by clear visual dividers.)
- **On a bare "Go":** asks for inputs: marketing materials — Build-a-Buyer profiles, copy blocks, offer briefs, VSL scripts, sales page text/URLs, or raw product/market research — declines to invent placeholder beliefs on a truly empty prompt.
- **Gotchas:** Short prompt (~9KB), no intake questionnaire — accepts freeform inputs in any format and any combination, extracting what it needs. Explicitly prioritizes UMP/UMS beliefs to appear first in output. Will not fabricate product claims/mechanisms beyond what's in the supplied materials. Has the same prompt-extraction/security guardrails as other bots in this suite — will refuse to describe/document its own methodology. LIVE PROBE UPDATE: contrary to the 'never ask questions, always produce the full deliverable' framing, a bare 'Go' with zero marketing material did NOT produce invented placeholder beliefs/metaphors — the bot asked directly for marketing materials first.
- **Consumes:** `buyer-profile`, `mechanism`, `offer-details`, `vsl-script`, `landing-page-copy`, `landing-page-url`, `research-report`, `raw-notes` · **Produces:** `mechanism`, `ad-copy`

## microscript

**MicroScript** — Generates Dominant Selling Ideas (DSIs — the single ownable differentiator) and Micro-Scripts (short, memorable, word-of-mouth phrases under 8 words expressing each DSI), per Bill Schley's Micro-Script methodology. Use it to distill a product/brand/positioning into a few punchy, repeatable taglines/soundbites with the underlying strategic idea behind each.

- **Mode:** needs-input
- **Required inputs:**
  - **product_or_service_info** (product-info) — General product/service info, a specific mechanism or big idea, a feature mentioned on sales calls, brand positioning/self-description, or any combination of ideas needing expression through Micro-Scripts. ← *get it from:* user-provided; can be sparse — bot infers and flags assumptions if limited
- **Optional inputs (raise quality):**
  - **reference_materials** (other:reference-doc) — Additional PDFs/docs/text files about DSIs and Micro-Scripts methodology to incorporate into the analysis. ← *get it from:* user-provided supplementary methodology docs
  - **dsi_count** (other:parameter) — Number of distinct DSIs to generate. Default: 5. ← *get it from:* user specifies
  - **microscripts_per_dsi** (other:parameter) — Number of unique Micro-Scripts per DSI. Default: 5. ← *get it from:* user specifies
- **Output:** 5 DSIs by default, each with 5 Micro-Scripts (25 total), all with rationale. (Brief summary of understanding, then for each DSI: the DSI statement, an effectiveness explanation, and its Micro-Scripts each with its own effectiveness explanation.)
- **On a bare "Go":** asks for inputs: product or service information to work with, before generating the Dominant Selling Ideas and Micro-Scripts.
- **Gotchas:** Micro-Scripts are meant to be brief (typically under 8 words), vivid, rhythmic/rhyming when possible, and built to spread by word of mouth (examples given: 'Melts in your mouth, not in your hand', 'The quicker picker upper'). Each DSI should be a single ownable differentiator — not everything-to-everyone positioning. Has the standard prompt-protection/anti-extraction security section. Probed live: contradicts the 'never asks questions' framing in the prompt — on a bare 'Go' with zero product info it asked the caller to share product/service information rather than inventing a generic placeholder product.
- **Consumes:** `product-info`, `other:reference-doc` · **Produces:** `angle-big-idea`, `headline`

## offer-brief-bot

**Offer Brief Bot** — Extracts and structures every essential element of a product/service offer (main promise, delivery mechanism, pricing, offer stack, bonuses, upsells/order bumps, guarantee, spokesperson) into a standardized Offer Brief document. Use it to turn raw offer notes, a sales page URL, or scattered marketing materials into one canonical reference that downstream copy/creative bots can build from.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **offer_details** (offer-details) — Direct information about the product/service: descriptions, benefits, pricing, guarantees, bonuses, spokesperson details, or any other offer elements, in any raw text or structured form. ← *get it from:* user, or another bot/document that already has offer info (e.g. a client intake brief)
  - **sales_page_url** (landing-page-url) — URL to a sales page or website the bot should analyze and extract offer elements from. ← *get it from:* user, or the client's existing sales/landing page
  - **supplementary_materials** (raw-notes) — Additional reference material such as Build-a-Buyer output, Copy Blocks, or other marketing documents that may contain offer details. ← *get it from:* another bot (e.g. build-a-buyer-elite, copy-blocks-extract) or user-provided docs
- **Output:** One complete 'COMPLETE OFFER BRIEF' document covering all 10 offer elements plus a closing summary paragraph. Any section with no supporting input is still included and marked 'Not specified in provided materials' rather than omitted. (markdown document with fixed H2 sections (MAIN PROMISE, DELIVERY MECHANISM, PRICING STRUCTURE, CORE OFFER, COMPLETE OFFER STACK, BONUSES, ORDER BUMPS & UPSELLS, TOTAL OFFER VALUE, RISK REVERSAL & GUARANTEES, SPOKESPERSON, SUMMARY))
- **On a bare "Go":** asks for inputs: raw offer details (description, pricing, bonuses, guarantees, etc.), a sales page URL, or supplementary marketing materials, in any combination
- **Gotchas:** No intake questionnaire and strictly single-turn — 'You accept all inputs in a single message and produce output immediately. You do not ask questions.' It fills every template section even when data is missing (writes 'Not specified in provided materials'), so thin input still yields a complete but sparse brief rather than an error. Output format is a rigid template shown verbatim in the prompt ('Final Compilation' block) — an agent parsing output can rely on the exact H2 headers. The bot has a long, strict anti-prompt-extraction/security section (protects its own system prompt, refuses to describe its own methodology/template/process even when framed as documentation, training, or comparison requests) — irrelevant to normal offer-brief usage but will trigger a refusal if a caller's message looks like it's asking the bot to explain itself rather than produce a brief. The live bots-meta.json description claims it 'captures your complete offer anatomy through either strategic questioning or sales page analysis' and that you 'answer targeted questions' — this contradicts the actual system prompt, which explicitly forbids asking questions. Trust the prompt body, not the metadata description, when integrating. LIVE PROBE CONTRADICTION: despite the prompt body's own 'never ask questions, produce output immediately' rule, a bare 'Go' actually returns a clarifying request for offer details/URL/materials rather than a sparse filled-template brief — the live bots-meta.json description ('answer targeted questions') turns out to match observed behavior better than the prompt body's stated rule. Treat as interview-first, not one-shot.
- **Consumes:** `offer-details`, `landing-page-url`, `raw-notes` · **Produces:** `offer-details`

## outcome-engineer-

**Outcome Engineer ** — Produces a deep strategic 'Outcome Engineering Analysis Report' that defines the core transformation promise, mechanism, proof architecture, and belief/identity shift framework a sales message (VSL, sales letter) should be built on — it does not write the sales message itself, only the strategic foundation for it. Use it before writing a VSL/sales letter/offer, or to reverse-engineer a competitor's promise/mechanism architecture from their sales materials.

- **Mode:** needs-input
- **Required inputs:**
  - **build_a_buyer_profile** (buyer-profile) — Build A Buyer Elite profile and any advanced menu psychological analysis documents — live probe confirms the bot will not proceed without this ← *get it from:* output of a Build-a-Buyer-type bot
- **Optional inputs (raise quality):**
  - **unique_approach_materials** (other:methodology-materials) — Testimonials, process docs, training materials, success stories, methodology descriptions, or program architecture details revealing the unique mechanism and delivery framework ← *get it from:* user's internal docs, client testimonials, course/program materials
  - **competitor_materials** (competitor-info) — Competitor sales letters or VSL transcripts, used only when mode=reverse_engineer to extract their outcome/mechanism architecture ← *get it from:* paste a competitor's sales page copy or VSL script/transcript
  - **mode** (other:parameter) — "standard" (engineer outcomes from profile/materials, default) or "reverse_engineer" (extract outcome/mechanism from competitor materials) ← *get it from:* user specifies; defaults to standard if omitted
- **Output:** A single structured strategic analysis report (not ad copy) covering transformation promise, mechanism, proof structure, delivery framework, competitive positioning, and an executive summary with recommendations — meant to feed into a separate copywriting/VSL bot. (Single unbroken code block, markdown-style headed sections (e.g. CORE PROMISE, PROOF STRUCTURE, DELIVERY FRAMEWORK, IMPLEMENTATION REQUIREMENTS, MARKET POSITIONING, EXECUTIVE SUMMARY) each with bullet sub-points)
- **On a bare "Go":** refuses / other: replies 'Welcome to Outcome Engineering Intelligence Unit. Please upload your: Buyer Profile, Psychological Analysis Documents.' and produces no report — will not self-start without at least a buyer profile, contradicting the prompt's stated one-shot instruction.
- **Gotchas:** Explicitly NOT a copywriting bot — refuses (by design) to write sales letters/VSLs itself; it only produces the upstream strategic foundation. Runs 5 'specialist' analytical lenses (behavioral, NLP, experiential design, market anthropology, clinical validation) over whatever inputs are given. Has a reverse_engineer mode for extracting promise/mechanism from a competitor's existing sales materials instead of building fresh. IMPORTANT gotcha: despite the prompt text claiming one-shot/no-questions behavior, the live bot actually gates on receiving at least a buyer profile — treat build_a_buyer_profile as effectively required in practice, not optional. interaction_style updated from 'one-shot' to 'interview-first' to reflect this confirmed live behavior.
- **Consumes:** `buyer-profile`, `competitor-info`, `raw-notes` · **Produces:** `research-report`, `mechanism`, `angle-big-idea`

## proof-page-master-bot

**Proof Page Master Bot** — Takes scattered proof assets (testimonials, studies, credentials, guarantees, etc.) and produces a structured Proof Page Blueprint — categorizing every asset, mapping it to the buyer objections it neutralizes, and specifying an optimal page section order. It does NOT write copy. Use it to plan where proof should go on a sales/landing page before a copywriter drafts the actual page.

- **Mode:** needs-input
- **Required inputs:**
  - **proof_materials** (customer-reviews) — Any combination of sales letters, VSLs, existing marketing materials, testimonials/reviews, studies, stats, research, credentials, certifications, authority markers, guarantees, and risk-reversal elements. Any format accepted. ← *get it from:* user-provided raw proof dump, or existing marketing materials/sales page
- **Output:** One complete Proof Page Blueprint document — a page-structure plan, not finished copy. (Fixed 5-part structure: PROOF INVENTORY (table: Proof Asset | Type | Category | Strength), OBJECTION PRIORITY MAP (numbered list w/ rationale), PROOF-TO-OBJECTION MATCH (table w/ coverage rating), RECOMMENDED PAGE STRUCTURE (numbered sections w/ theme + assigned assets), GAP ANALYSIS (missing proof types/recommendations). Uses emoji section headers and tables.)
- **On a bare "Go":** asks for inputs: proof materials (testimonials/reviews, sales letters/VSL scripts, studies/stats, credentials, guarantees, media coverage, or other supporting evidence) — declines to produce a blueprint with nothing to inventory.
- **Gotchas:** Strict output boundary: never writes actual copy, never explains product mechanisms, never invents proof not supplied. Hard-coded structural rule (repeated twice in the prompt for emphasis) that Social Proof/testimonials must occupy Sections 1-4 of every recommended page structure regardless of category — even for supplement/mechanism-driven offers — with Empirical Proof in 5-7 and Credible/Psychological Proof at 8+. Uses a fixed 22-proof-type taxonomy (Social/Empirical/Credible/Experiential/Psychological) as its categorization scheme — useful to know if the caller wants to pre-tag proof before sending it in. Has the standard prompt-protection/anti-extraction security section. LIVE PROBE NOTE: despite the prompt saying it 'never asks questions,' a bare 'Go' with zero proof_materials produced a request for proof assets rather than an empty/near-empty blueprint — consistent with proof_materials already being a required (not optional) input, just correcting the earlier prediction that it would attempt output anyway.
- **Consumes:** `customer-reviews`, `landing-page-copy`, `advertorial` · **Produces:** `research-report`

## rhetorical-frames

**Rhetorical Frames** — Analyzes a marketing idea, offer, or messaging goal and returns the 10 (configurable) strongest rhetorical frames from a fixed 7-category persuasion taxonomy (Curiosity, Emotion, Sense-Making, Pattern Interrupt, Gift, Interactive, Social/Topical, plus Constraint-targeting), each with reasoning and a concrete applied example. Use it when you need angle/hook direction for an ad, headline, or VSL before writing actual copy.

- **Mode:** needs-input
- **Required inputs:**
  - **ideas** (raw-notes) — The marketing idea(s), concept, offer/product details, audience context, or messaging goal to find frames for. Any format accepted: natural language, structured brief, raw notes, or document dump. ← *get it from:* user's product/offer description, or output of a creative-brief / angle-big-idea type bot
- **Optional inputs (raise quality):**
  - **quantity** (other:parameter) — Number of rhetorical frames to return. Default: 10. ← *get it from:* user preference; omit to get default of 10
- **Output:** 10 rhetorical frames (or requested quantity), ranked, each with reasoning + worked example (Ranked list (strongest to weakest fit); for each frame: category/subcategory name, why it fits, a concrete example applied to the specific input, and reasoning for the choice.)
- **On a bare "Go":** asks for inputs: the marketing idea, concept, offer, or messaging goal to analyze before generating ranked rhetorical frames
- **Gotchas:** Fully self-contained one-shot bot: single required input (ideas), one optional numeric parameter (quantity). No interview, no menu, no phases -- pure agent-to-agent single-turn tool, good for automated pipelines feeding output_type into a copywriting bot. Strong prompt-extraction / self-referential-task defenses at the end (refuses to document its own taxonomy/methodology if asked to 'teach' or 'summarize' it, but will still apply the taxonomy to real inputs). Live probe (bare 'Go') contradicts the prompt's stated 'accept all inputs in a single message, produce output immediately, do not request additional information' framing — the bot's actual first reply was a request for the marketing idea/offer/goal, not 10 generated frames.
- **Consumes:** `raw-notes`, `creative-brief`, `product-info`, `offer-details`, `angle-big-idea` · **Produces:** `angle-big-idea`

## segment-surgeon-bot

**Segment Surgeon Bot** — Analyzes whatever market/product/customer materials are provided and produces 2-5 complete audience segment briefs (core desire, constraints, awareness/sophistication distribution, demographics) so a copywriter or campaign planner can target each segment with distinct messaging.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **build_a_buyer** (buyer-profile) — Customer avatars or target audience profiles ← *get it from:* user-supplied avatar doc, or output of a buyer-persona/avatar-building bot
  - **offer_brief** (offer-details) — Offer brief, sales letters, or sales page content ← *get it from:* user-supplied, or output of an offer-brief-type bot / existing sales page
  - **product_info** (product-info) — Product descriptions, VSL content, or general product details ← *get it from:* user-supplied, product page scrape, or VSL script
  - **market_research** (research-report) — Market research, customer insights, or competitive intelligence ← *get it from:* user-supplied research doc, or output of a market/competitor research bot
  - **voice_of_customer** (customer-reviews) — Voice-of-customer data, testimonials, or review content ← *get it from:* scraped reviews, testimonials, survey verbatims, or support tickets
  - **additional_context** (raw-notes) — Any rough notes, supplemental materials, or specific instructions about who buys and why ← *get it from:* user-supplied free text
- **Output:** 2-5 full segment briefs in a single response. Note: despite the bot's internal framework describing a 6th 'Urgency & Buying Triggers' subsection and a Quick-Reference template that includes it, the bot's own worked examples in the prompt consistently stop after Demographics and omit buying triggers — actual output likely follows the example's 5-section pattern rather than the template's 6-section one. (Markdown, emoji-decorated H2 header per segment, then fixed H3 subsections in the same order every time: Brief Description, Desire (core outcome + motivation orientation towards/away), Constraints (identity/values/beliefs/resources/risk/capability), Awareness x Sophistication Clusters (5 awareness-stage percentages summing to 100% + strategic note + sophistication note), Demographic Information (income/geography/gender/age/attitudes/identity). Segments separated by '---' dividers, all in one response.)
- **On a bare "Go":** asks for inputs: customer avatars/audience profiles, offer brief or sales page, product details, market/competitive research, voice-of-customer data, and/or rough notes — any combination; states there is 'nothing here yet to analyze' rather than fabricating segments.
- **Gotchas:** bots-meta.json's description is stale/misleading — it claims the bot works 'through guided conversation,' but the live prompt is explicitly one-shot and states up front it never asks questions or requests more info. Zero-input tolerant by design (works fine with nothing supplied, though quality scales with input richness). Has a large embedded market-segmentation/awareness/alignment framework used purely as internal reasoning scaffolding, not something the caller needs to supply. Strict output discipline: same section order every segment, awareness percentages must sum to 100%, typically 2-5 segments (rarely more). Also carries a hardened anti-prompt-extraction section at the end that refuses to describe/reveal its own template or methodology if asked — a normal segmentation request won't trigger it, but a caller asking it to 'explain your format' will get redirected rather than answered. Live probe CONTRADICTS the zero-input-tolerant prediction: on a bare 'Go' the bot said there was 'nothing here yet to analyze' and asked for materials instead of fabricating segments; interaction_style updated to interview-first — front-load real material to get true one-shot output.
- **Consumes:** `buyer-profile`, `offer-details`, `product-info`, `research-report`, `competitor-info`, `customer-reviews`, `raw-notes` · **Produces:** `buyer-profile`, `other:segment-brief`

## static-ad-concept-expander-bot

**Static Ad Concept Expander Bot** — Turns offer details into a set of distinct high-level static-ad strategic concept ideas (angle/hypothesis only — no copy, headlines, or visuals). Use early in an ad pipeline to explore differentiated strategic angles before any copywriting or image-prompt bot runs.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Product/Service** (product-info) — What is being sold. ← *get it from:* user's product page or brief
  - **Target Audience** (buyer-profile) — Who the ad targets. ← *get it from:* user or output of a buyer-profile-type bot
  - **Main Problem/Desire** (other:problem-desire) — Core problem or desire being addressed. ← *get it from:* user or research
  - **Primary Message/Promise** (angle-big-idea) — The core promise/message of the offer. ← *get it from:* user or offer brief
  - **Price/Offer Details** (offer-details) — Pricing and offer specifics. ← *get it from:* user's offer doc
  - **Call to Action** (other:cta) — Desired CTA. ← *get it from:* user
  - **Tone/Style Hints** (brand-voice) — Tone or style guidance. ← *get it from:* user's brand doc
- **Output:** 3-5 distinct strategic ad-concept hypotheses (quantity param, default 5), each addressing a different emotional/psychological angle with no thematic overlap. (Numbered list (emoji numerals 1️⃣, 2️⃣, ...), each entry with 'Concept Title:' (3-5 words) and 'Concept Summary:' (1-2 sentences). No copy, headlines, or visual/design instructions included.)
- **On a bare "Go":** asks for inputs: offer details, before generating strategic ad concepts.
- **Gotchas:** Deliberately upstream/idea-only: explicitly prohibited from writing ad copy, headlines, or design/layout instructions. Best used as the first step feeding into a copy bot (for headlines/body) or an image-prompt bot (for visuals) — its output (concept title + summary) is the strategic brief those downstream bots would need. quantity param is capped 3-5, unlike most other generators here which allow larger batches. LIVE PROBE CONTRADICTION: despite the prompt's instruction to never ask questions and produce output immediately, a bare 'Go' produced a one-line request to provide offer details instead of generating concepts — treat offer/product info as effectively required.
- **Consumes:** `product-info`, `buyer-profile`, `angle-big-idea`, `offer-details`, `brand-voice` · **Produces:** `static-ad-concept`

## storm-bot

**STORM Bot** — Produces a comprehensive retargeting campaign strategy brief (30-50 angles mapped to a 4-Pillars framework) for ad and/or email copywriters to execute during a high-intensity post-opt-in retargeting window; use it after intake research is done and before copywriters start writing.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **product_service** (product-info) — The product or service and its unique mechanism. ← *get it from:* user's product page / brand doc
  - **target_audience** (buyer-profile) — Target audience description: demographics, psychographics, awareness level. ← *get it from:* user or output of a buyer-profile-type bot
  - **funnel_type** (creative-brief) — Current funnel type (call funnel, webinar, instant forms/hydra). ← *get it from:* user
  - **retargeting_window** (creative-brief) — The retargeting window being worked with (e.g. 72 hours, 14 days). ← *get it from:* user
  - **conversion_goal** (creative-brief) — Primary conversion goal / metric. ← *get it from:* user
  - **existing_assets** (raw-notes) — Any existing assets, constraints, or materials. ← *get it from:* user
  - **top_objections** (customer-reviews) — Top 3-5 objections the sales team hears most often. ← *get it from:* user / sales team notes
  - **false_beliefs** (buyer-profile) — False beliefs the market holds about solving this problem. ← *get it from:* research or user
  - **failed_attempts** (buyer-profile) — What the audience has tried before that didn't work, and why it failed. ← *get it from:* research or user
  - **buying_trigger** (mechanism) — The #1 thing that makes someone say yes to the offer. ← *get it from:* user
  - **differentiators** (competitor-info) — What makes this approach different from competitors. ← *get it from:* user or competitor-info research
  - **negative_feedback** (customer-reviews) — Negative reviews or common complaints to address. ← *get it from:* user's review data
  - **results_transformations** (customer-reviews) — Specific results or transformations to highlight. ← *get it from:* user's case studies/testimonials
  - **identity_shift** (buyer-profile) — The identity shift that happens when someone becomes a customer. ← *get it from:* user or derived from buyer-profile
  - **secret_fears** (buyer-profile) — What the audience is secretly afraid of that they won't admit out loud. ← *get it from:* research or user
  - **status_symbols** (buyer-profile) — Status symbols or achievements that matter most to the audience. ← *get it from:* research or user
  - **testimonials_proof** (customer-reviews) — Existing testimonials, case studies, or success stories. ← *get it from:* user
  - **sales_call_questions** (raw-notes) — Questions prospects ask repeatedly in sales calls. ← *get it from:* sales team / user
  - **output_type** (other:parameter) — "ad_brief" / "email_brief" / "both". Default: both. ← *get it from:* user specifies, else defaults to both
- **Output:** A strategic retargeting campaign brief with 30-50 unique angles per requested type (ads and/or emails), NOT final copy. (Two possible sections (email brief and/or ad brief), each a structured numbered list of 30-50 angle entries per format template (email: subject lines, preview text, structure, copy-block checklist, length, tone; ad: visual hook, verbal hook, content structure, visual elements, platform variations, caption structure), plus voice/tone and pillar-distribution guidance.)
- **On a bare "Go":** asks for inputs: full campaign brief — product/service, target audience, funnel type, retargeting window, conversion goal, top objections, false beliefs, failed attempts, buying trigger, differentiators, results/transformations, and existing assets. Produces no angle brief until given details.
- **Gotchas:** Never writes final copy, only strategic direction/blueprint for copywriters to build ads and emails from. Accepts unstructured input in any format (natural language, key-value, doc dumps) and infers missing fields rather than asking questions. Has strong prompt-injection/extraction defenses baked into the system prompt (refuses to reveal or paraphrase its own instructions). If retargeting audience appears under 100 users, it adds a note recommending audience-building strategies before full deployment. Probe contradicts the prior prediction of a fabricated generic 30-50 angle brief on bare 'Go' — the bot instead lists its full intake checklist and waits for real campaign details. interaction_style updated from one-shot to interview-first.
- **Consumes:** `product-info`, `buyer-profile`, `customer-reviews`, `competitor-info`, `mechanism`, `creative-brief`, `raw-notes` · **Produces:** `creative-brief`, `angle-big-idea`, `ad-hooks`

## strategic-allocation-bot

**Strategic Allocation Bot** — Converts market awareness distribution, risk tolerance, and total ad volume into a creative testing allocation matrix (how many ads to swipe from competitors, swipe from other verticals, build as confident hypotheses, run as internal tests, or try as wildcards). Use it to plan a media buying test batch before briefing creative.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **awareness_distribution** (other:awareness-stage-percentages) — Percentage breakdown across awareness stages, e.g. '40% Problem / 30% Solution / 20% Product / 10% Most Aware'. Defaults to 40/30/20/10 if omitted. ← *get it from:* user's media buying strategy, or output of an awareness/market-sophistication analysis bot
  - **risk_tolerance** (other:risk-level) — LOW, MEDIUM, or HIGH. Defaults to MEDIUM. ← *get it from:* user's stated risk appetite for the testing budget
  - **total_ads** (other:ad-count) — Total number of ads to allocate across categories. Defaults to 40. ← *get it from:* user's planned test batch size
- **Output:** One allocation matrix plus three rounding/priority variants (Option A/B/C), each summing exactly to total_ads, covering 5 creative test types (Competitor Swipes, Other Vertical Swipes, Confident Hypothesis, Internal Tests, Wildcard Ideas) (markdown with headings, a main allocation table, three labeled allocation options (A/B/C) with tree-list breakdowns, and a recommendation section)
- **On a bare "Go":** asks for inputs: Total Ads (default 40), Risk Level (LOW/MEDIUM/HIGH, default MEDIUM), and Awareness Distribution (default 40/30/20/10) — but explicitly offers a shortcut: replying "use defaults" triggers immediate generation with the stated defaults.
- **Gotchas:** Fully self-contained generator — has hardcoded defaults for every input (40/30/20/10 awareness, MEDIUM risk, 40 total ads), so it never needs to ask questions. Swipes (competitor/other-vertical) are always shown as unified categories, never split by awareness stage — only the other three categories get distributed by awareness. Has an aggressive prompt-extraction defense section appended (refuses to describe/document its own methodology) — irrelevant to normal use but will cause refusals if someone asks it to explain its process. LIVE PROBE CONTRADICTS PROMPT TEXT: despite 'produces output immediately using defaults' language, a bare 'Go' actually pauses to list the three inputs and their defaults, requiring an explicit follow-up (either real values or the literal phrase "use defaults") before generating — treat this probed behavior as ground truth. Callers wanting a true one-shot call should include "use defaults" (or explicit values) in the very first message.
- **Consumes:** `other:awareness-stage-percentages`, `other:risk-level`, `other:ad-count` · **Produces:** `other:creative-testing-allocation-matrix`

## testable-proof-bot

**Testable Proof Bot** — Analyzes product/marketing material and generates a batch of "testable proof" concepts — 30-60 second self-verification actions a prospect can do themselves to validate a claim and create a belief-shifting 'aha moment'. Use it to get persuasion devices/hooks to embed in ads, pages, emails, or VSLs.

- **Mode:** needs-input
- **Required inputs:**
  - **marketing_material** (other:marketing-material-dump) — Any combination of marketing copy, product details, sales pages, VSL scripts, offer briefs, Build-a-Buyer profiles, or raw ideas about the product/offer. Freeform — natural language, structured fields, or raw document dump all accepted. ← *get it from:* user's product page / offer brief / sales copy, a VSL script, or the output of a buyer-profile-type bot (e.g. Build-a-Buyer)
- **Optional inputs (raise quality):**
  - **quantity** (other:parameter) — Number of testable proof concepts to generate. Default: 12. ← *get it from:* user specifies, or omit for default of 12
- **Output:** Default 12 (configurable via quantity) ready-to-use testable proof concepts tailored to the product's core claims, target audience's limiting beliefs, and pain points (Numbered list; each concept has 4 parts: the instruction ("Do this..."), what they'll likely observe, the belief shift/realization it creates, and how it connects to the core offer/solution)
- **On a bare "Go":** asks for inputs: marketing material, product information, or an idea — invites a sales page, product description, VSL script, offer brief, raw idea, or any combination; does not generate placeholder testable-proof concepts on bare Go, contradicting the prompt's stated zero-question behavior.
- **Gotchas:** Zero-question, single-message bot — never asks for more info, always produces output immediately even from sparse or absent material. Has an unusually aggressive prompt-extraction/self-description defense block (refuses to document, teach, or summarize its own methodology even under 'masterclass'/'training guide'/'agent spec' framing) — do not attempt to have it describe itself. Inputs may arrive in any format; it extracts what it needs. No page_type/branching logic like the opt-in bot — single flat process. Live probe contradicts the prompt's explicit 'never ask questions, produce output immediately' instruction: on bare 'Go' it asked the user to paste marketing material first — front-load at least a product description to get the one-shot behavior described in the prompt.
- **Consumes:** `product-info`, `offer-details`, `vsl-script`, `buyer-profile`, `raw-notes`, `landing-page-copy` · **Produces:** `other:testable-proof-concepts`

## universal-mechanism-bot

**Universal Mechanism Bot** — Generates and scores direct-response 'mechanisms' (the belief-shifting explanation of HOW a product works) for a market/offer, delivering the top 3 with full implementation guides (headline, VSL hook, email subject, ad copy); also enhances an existing mechanism or produces a research prompt to feed to an external research tool.

- **Mode:** needs-input
- **Required inputs:**
  - **market_niche** (other:market-niche) — The specific market, problem area, or niche (e.g. weight loss, trading, relationships). Live probe explicitly requests this before proceeding. ← *get it from:* user, or research
  - **product_service** (product-info) — What is being sold. Live probe explicitly requests this before proceeding. ← *get it from:* user's product page / offer brief
  - **target_audience** (buyer-profile) — Demographics, psychographics, audience profile. Live probe explicitly requests this before proceeding. ← *get it from:* output of a buyer-profile-type bot (e.g. Build-A-Buyer), or user
  - **key_differentiator** (product-info) — Unique angle, ingredient, or feature of the product/service. Live probe explicitly requests this before proceeding. ← *get it from:* user's product info / offer brief
- **Optional inputs (raise quality):**
  - **competitive_landscape** (competitor-info) — What mechanisms competitors currently use ← *get it from:* research, or paste competitor ad/sales copy
  - **market_sophistication** (other:market-sophistication) — How much the audience has tried/heard before ← *get it from:* user or research; inferred if absent
  - **causal_clarity** (other:causal-clarity) — "low" (confusion about causes, focus UMP) or "high" (cause known, focus UMS); inferred from market context if not specified ← *get it from:* user, else inferred by the bot
  - **existing_mechanism** (mechanism) — An existing mechanism to enhance (enhancement mode only) ← *get it from:* user, or prior output of this bot
  - **research_results** (research-report) — Raw research results from external tools, to be analyzed (research_prompt mode step 2 only) ← *get it from:* user pastes results from running the bot's generated research prompt in an external research/AI tool
  - **additional_context** (raw-notes) — Supplementary materials: Build a Buyer, Offer Brief, Market Map, competitor intel, sales copy, or other research ← *get it from:* user, or outputs of other Genesis bots (buyer-profile, offer-brief, market-map)
  - **mode** (other:parameter) — "full_discovery" (default) / "research_prompt" / "quick_generation" / "enhancement" ← *get it from:* user specifies; defaults to full_discovery
  - **quantity** (other:parameter) — Number of mechanisms to generate before screening. Default 36 for full_discovery (3 per framework combo), 10 for quick_generation ← *get it from:* user specifies or accepts default
  - **top_count** (other:parameter) — Number of top mechanisms to deliver with full scoring/implementation guides. Default 3 ← *get it from:* user specifies or accepts default
  - **narrative_preference** (other:parameter) — "restoration" / "revelation" / "rebirth" / "auto" (default auto — best-fit per mechanism) ← *get it from:* user specifies or accepts default
  - **competitor_strategy** (other:parameter) — "avoid" (default, create different mechanisms) / "piggyback" (go deeper on what's working); applies mainly to research_prompt mode ← *get it from:* user specifies or accepts default
- **Output:** Full discovery: top 3 (configurable via top_count) fully-scored mechanisms with implementation guides, drawn from up to 36 generated candidates. Quick generation: 10 rapid-fire testable mechanism options. Enhancement: 1 enhanced mechanism with before/after comparison across 3 narrative wrappers. Research_prompt: 1 research prompt (step 1) or top 5 analyzed mechanisms (step 2). (Markdown sections per mechanism: mechanism name, full mechanism narrative, scoring breakdown (Zeitgeist/Simplicity/Novelty), implementation guide (headline, email subject, VSL hook, ad copy), testing priority. For research_prompt mode: a single code-block research prompt ready for an external tool. For quick_generation: a shorter list (5-10) of name + 2-sentence mechanism + enemy + test channel.)
- **On a bare "Go":** asks for inputs: market/niche, product/service, target audience, and key differentiator; states rough notes are fine and it will extract what's needed and run full discovery immediately.
- **Gotchas:** Has 4 distinct modes (full_discovery, research_prompt, quick_generation, enhancement) selected via a 'mode' parameter — an agent should pick the mode explicitly rather than relying on inference. research_prompt mode is two-step: call once to get a research prompt (to hand to an external research tool/agent), then call again with research_results pasted in to get analyzed/scored mechanisms. Has an aggressive prompt-protection/anti-extraction section at the end — will refuse to describe its own methodology/template if asked. LIVE PROBE CONTRADICTION: despite the system prompt's claim it 'does not ask questions or request additional information,' a bare 'Go' produced an explicit request for market/niche, product/service, target audience, and key differentiator instead of a generated mechanism set — consistent with the bots-meta.json description ('All I need is your Build-A-Buyer, Offer Brief, and Market Map') rather than the prompt body's stated zero-question policy.
- **Consumes:** `product-info`, `buyer-profile`, `competitor-info`, `mechanism`, `research-report`, `raw-notes`, `offer-details` · **Produces:** `mechanism`, `research-report`, `headline`, `email-copy`, `ad-copy`, `video-script`

## universal-static-bot

**Universal Static Ad Idea Bot** — Diagnoses which of 21 static-ad formats (Headline+Product, Before/After, Comparison, Testimonial, Note From Founder, etc.) are the best fit for a specific product/situation and routes the user to the right generator bot for each. It does NOT write ad copy or concepts itself — it's a router/triage step to run before any static-ad-concept bot.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **build_a_buyer** (buyer-profile) — Customer avatar/audience profile — demographics, pain points, desires, beliefs ← *get it from:* output of a buyer-profile-type bot
  - **copy_blocks** (ad-hooks) — Key messaging elements, hooks, proof points ← *get it from:* output of a copy-blocks-type bot
  - **offer_brief** (offer-details) — What is being sold, price, positioning ← *get it from:* user's offer doc or offer-brief bot
  - **sales_copy** (vsl-script) — VSL script, sales page text, or sales page URL ← *get it from:* user-provided VSL/sales page or URL
  - **additional_assets** (raw-notes) — Any other context: product images, testimonials, founder story, scientific data, competitor info, campaign goals ← *get it from:* user-provided; the richer this is, the sharper the recommendations
  - **recommendation_count** (other:parameter) — Number of format recommendations to return; default 5, range 3-5 ← *get it from:* user specifies, else defaults to 5
- **Output:** 3-5 ranked static-ad-format recommendations with format-specific reasoning and a pointer to the next bot to call (e.g. Note From Founder Bot, Comparison Bot, Testimonial Bot) (Brief acknowledgment of inputs/signal factors, then a numbered bold-header list (1. FORMAT NAME) each with 1-2 sentences on why it fits this specific input and which bot in the suite to use next; ends with an offer to expand)
- **On a bare "Go":** asks for inputs: product details, target audience, available assets (testimonials/photos/data/founder story), campaign goal, and/or sales copy — states it needs these to generate recommendations rather than defaulting to generic formats.
- **Gotchas:** This is a routing/triage bot, not a copy generator — its whole job is picking among the other static-ad bots in the suite (Comparison, Testimonial, Note From Founder, Before/After, etc.), so an agent should call this FIRST when unsure which static format to use, then hand its recommended format name(s) to the matching concept bot. Never recommends a format whose required assets are clearly absent (e.g. no Before/After without transformation photos) and never outputs a 'formats to avoid' list. LIVE PROBE CONTRADICTION: despite the prompt's 'produce output immediately, never hits zero' claim, a bare 'Go' with zero context produced a request for product/audience/asset/goal info rather than generic fallback recommendations — supply at least one of the optional inputs rather than sending a bare trigger.
- **Consumes:** `buyer-profile`, `ad-hooks`, `offer-details`, `vsl-script`, `customer-reviews`, `product-info`, `competitor-info`, `raw-notes` · **Produces:** `research-report`

## universal-static-idea-generator

**Universal Static Idea Generator** — Analyzes a product's assets (avatar, copy blocks, offer brief, sales copy) and recommends which 3-5 of 21 static ad formats will perform best, explaining why and naming the specific downstream bot to use for each. Does NOT generate ad concepts itself — it's a diagnostic router, despite its slug/name implying idea generation.

- **Mode:** needs-input
- **Required inputs:**
  - **product/offer assets (any combination)** (other:mixed) — At least one of: Build a Buyer output (audience profile), Copy Blocks (messaging/hooks/proof), Offer Brief (what's sold, price, positioning), or Sales Copy (VSL script/sales page text or URL). Bot will ask 1-2 follow-up questions if insufficient. ← *get it from:* user, or outputs of 'Build a Buyer', 'Copy Blocks', or offer-brief-type bots in the suite
- **Optional inputs (raise quality):**
  - **product images** (product-image-description) — product photography ← *get it from:* user upload
  - **testimonials** (customer-reviews) — customer quotes/reviews ← *get it from:* user
  - **founder story** (brand-voice) — narrative about founder/brand origin ← *get it from:* user
- **Output:** 3-5 static ad format recommendations ranked by fit strength; each names the format, explains why it fits THEIR specific inputs, and names which specific bot in the suite to use next. Ends with lettered options (A: more recommendations, B: start over). (markdown with horizontal rule, emoji section headers, numbered ranked list (3-5 items))
- **On a bare "Go":** asks for inputs: Build a Buyer (audience profile), Copy Blocks (messaging/hooks/proof points), Offer Brief (product/price/positioning), or Sales Copy (VSL script/sales page text or URL) — any combination, plus optional product images/testimonials/founder story; produces no recommendations until given at least one.
- **Gotchas:** Naming mismatch: slug/meta-description call it an 'idea generator' but it explicitly refuses to generate ad concepts — it's a format-recommendation router that points to other bots. Has a hardcoded anti-jailbreak refusal protocol. Never says which formats to avoid (explicitly forbidden in prompt) — only lists what to use. Useful as a first step in a pipeline before invoking a concept-generating static-ad bot.
- **Consumes:** `buyer-profile`, `creative-brief`, `offer-details`, `vsl-script`, `landing-page-copy`, `landing-page-url`, `customer-reviews`, `product-image-description`, `brand-voice` · **Produces:** `other:format-recommendation`

## voice-mod-bot

**Voice Mod Bot** — Turns a buyer/market profile (Build A Buyer Elite output) into a calibrated 'Voice Mod' — a hybrid brand-voice archetype spec (parameters, personality markers, writing patterns, tone samples) meant to be fed into other copywriting bots so they all write in one consistent, market-resonant voice. Use once per brand/expert before running copy-generation bots, so their output shares a calibrated voice.

- **Mode:** needs-input
- **Required inputs:**
  - **buyer_profile** (buyer-profile) — Build a Buyer Elite profile: demographics, psychographics, pain points, desires, beliefs, emotional drivers, transformation desires. ← *get it from:* output of the Build-A-Buyer-Elite bot (build-a-buyer-elite-.md in this same library) — required foundational input per the bot's own description; must be built first if not yet available
- **Optional inputs (raise quality):**
  - **expert_content** (brand-voice) — Existing content samples from the expert/guru (emails, posts, video transcripts, sales pages, social content) reflecting their natural voice. ← *get it from:* user's existing content library / transcripts
  - **expert_personality** (other:expert-personality) — Personal details about the expert: home/family life, entertainment preferences, lifestyle, quirks, cultural touchpoints, signature phrases, career journey, defining moments, communication style, teaching style. ← *get it from:* user interview/bio doc
  - **archetype_preference** (other:parameter) — Force a specific one of the 8 voice archetypes (Loving Friend, Cheerleader, Wise Guide, Warrior, Healer, Straight-Shooter, Revolutionary, Nurturer) instead of letting the bot pick. ← *get it from:* user
- **Output:** One complete Voice Mod export code — a reusable voice spec, not marketing copy itself (Single markdown code block containing a structured pseudo-code object: VOICE_MOD_[ID] { MARKET_PROFILE{}, ARCHETYPE_SETTINGS{}, VOICE_PARAMETERS{7 scored 1-10 params}, PERSONALITY_MARKERS{}, WRITING_PATTERNS{}, TONE_SAMPLES{HOOK/BODY/CLOSE, one-sentence-per-line}, IMPLEMENTATION_NOTES{} } — plus a preceding narrative summary (market voice analysis, expert voice analysis, archetype recommendation, parameter settings, sample content, personalization protocols))
- **On a bare "Go":** asks for inputs: requests the required Buyer Profile (Build a Buyer Elite output or target market description), plus optional Expert Content, Expert Personality, and Archetype Preference, before producing the Voice Mod export.
- **Gotchas:** Output is strict and code-block-enforced: the prompt says 'FAILURE TO USE CODE BLOCK FORMAT = AUTOMATIC ERROR TRIGGER' and requires all tone samples in one-sentence-per-line format — a downstream parser should expect a single fenced code block with the VOICE_MOD_{...} structure. Designed as an intermediate artifact: feed its output into other copywriting bots as a brand-voice input, not a final deliverable for an end client. 8 fixed archetypes and 7 scored voice parameters (gender energy, nurturing, authority, professionalism, vulnerability, directness, technical_depth) are built into the bot's domain knowledge. Has the standard prompt-protection/security block appended. Live probe on a bare 'Go' contradicted the prompt's 'accepts all inputs in one message, never asks questions' framing and the predicted ungrounded-generic-export fallback: it explicitly asked for the Buyer Profile (and optional expert content/personality/archetype) instead of emitting a placeholder Voice Mod.
- **Consumes:** `buyer-profile`, `brand-voice`, `other:expert-personality` · **Produces:** `brand-voice`

# CATEGORY: Copywriting — Ads

## 75-ads-template-bot

**75 Ads Template Bot** — Transforms a built-in library of 75 proven direct-response ad script templates into offer-specific ads via a Mad-Libs swap (pain, promise, mechanism, proof, conditions) while preserving each template's exact structure, tone, rhythm, and length. Use it to mass-produce a large batch of ready-to-test ad variations for a single offer in one pass.

- **Mode:** needs-input
- **Required inputs:**
  - **source_materials** (other:offer-source-dump) — All available marketing materials for the offer in any format (structured, unstructured, or raw dumps): VSL script or sales page, avatar/customer research, proof elements (testimonials, case studies, stats), product details, mechanism explanation, offer brief (pricing, guarantees, bonuses, urgency/scarcity terms). ← *get it from:* user's existing marketing docs/sales page/VSL script, or outputs of upstream bots (buyer-profile, product-info, offer-details, customer-reviews, mechanism, vsl-script types)
- **Optional inputs (raise quality):**
  - **objective** (other:mode-flag) — "sell_the_click" (Mode A: maximize CTR to next step, curiosity-driven, no closing CTAs) or "sell_the_product" (Mode B: drive conversion inside the ad, explicit purchase CTAs). Defaults to sell_the_click if omitted/inferred from context. ← *get it from:* user specifies, or agent infers from campaign goal (e.g. cold traffic to advertorial/VSL = sell_the_click; retargeting/direct offer = sell_the_product)
  - **perspective** (brand-voice) — Voice for the ads: "founder" / "ugc" / "narrator" / "brand" / "mixed". Defaults to "mixed". ← *get it from:* user's brand voice preference or existing brand-voice doc
  - **tone_adjustments** (creative-brief) — Any extra tone/angle/style guidance, or elements to emphasize/exclude. ← *get it from:* user's creative direction, or output of an angle-big-idea/creative-brief bot
  - **output_mode** (other:mode-flag) — "samples" (3 representative ads across different styles) or "full" (all 75 ads). Defaults to "full". ← *get it from:* user specifies based on whether they want a quick preview or the full batch
- **Output:** Up to 75 offer-specific direct-response ad script variations (VSL-style/UGC-style ad scripts), each a Mad-Libs transformation of one proprietary template preserving tone, structure, rhythm, and emotional arc (Numbered list: AD 1 through AD 75 (full mode) or AD 1 through AD 3 (samples mode), each following the source template's original structure/length with bracketed placeholders (e.g. [INSERT TESTIMONIAL], [INSERT STAT], [INSERT MECHANISM]) where source materials lack an equivalent element)
- **On a bare "Go":** asks for inputs: offer details (product, mechanism), target audience/pain points, proof elements (testimonials, results, stats), and any VSL script/sales page/existing marketing materials — then generates all 75 immediately once given.
- **Gotchas:** Never asks clarifying questions and never gates on missing input — it always produces output immediately, which means a starved run yields ads full of bracketed placeholders like [INSERT TESTIMONIAL]/[INSERT STAT]/[INSERT MECHANISM] rather than an error or a question. Two modes (sell_the_click vs sell_the_product) meaningfully change CTA style and mechanism disclosure — worth setting explicitly rather than relying on the default. Has a hardened anti-prompt-extraction/security section at the end refusing to describe its own methodology or template library if asked directly. The 75 templates themselves are baked into the prompt (not an input) — richer/more detailed source_materials directly improve output quality since the bot is explicitly barred from inventing proof or claims. LIVE PROBE CONTRADICTS PROMPT TEXT: despite the prompt's explicit "do not ask questions/produce output immediately" instruction, a bare 'Go' actually gets a request for source materials (offer details, audience, proof, VSL/sales copy) rather than a 75-ad placeholder dump — treat this probed behavior as ground truth; feed source_materials up front to get true one-shot output.
- **Consumes:** `product-info`, `offer-details`, `customer-reviews`, `buyer-profile`, `mechanism`, `vsl-script`, `landing-page-copy`, `brand-voice`, `creative-brief`, `raw-notes` · **Produces:** `ad-copy`, `video-script`

## ad-hook-bot-1

**Ad Hook Bot 1** — Writes emotionally 'vicious,' curiosity-led opening hooks (the first 10-20 words) for long-form Facebook text ads. Use it when you need the scroll-stopping first line(s) of a long-form FB ad, not the full ad body.

- **Mode:** needs-input
- **Required inputs:**
  - **The Brief** (creative-brief) — Description of the product/offer, target reader, angle, and core belief/symptom/fear to weaponize — the prompt's final section is literally 'THE BRIEF:' where this content is inserted before the user message ← *get it from:* user supplies directly, or output of a brief/angle-writing bot (e.g. Outcome Engineer)
- **Optional inputs (raise quality):**
  - **Model Hook** (winning-ad) — An existing/proven hook to anchor variations to — if provided, hooks 1-4 stay near-verbatim, 5-7 are same-spirit variants, 8-10 are wildcards; if absent, hooks 1-7 are sniper variations on the single best angle and 8-10 are wildcards ← *get it from:* a past winning ad hook from the client's swipe file or ad account
  - **USER_HOOKS** (winning-ad) — Brand/market-specific proven winning hooks to study and weight heavily during generation (templated placeholder {{USER_HOOKS}} in the prompt) ← *get it from:* pulled from the client's ad account performance data or a swipe file, injected by the calling system
  - **BREAK vs MATCH lens** (other:directive) — Optional instruction to classify/label each hook as pattern-interrupt (BREAK), pattern-confirmation (MATCH), or both, and ensure variety ← *get it from:* user specifies in the brief if desired
  - **Emotion-to-action lens** (other:directive) — Optional instruction to target hooks toward a specific desired reader action (clicks/saves vs shares/comments vs sustained reading) by selecting the matching emotional driver ← *get it from:* user specifies desired action in the brief if desired
- **Output:** 10 candidate FB ad hooks (10-20 words each, the pre-'See More' fold text) plus a short strategic rationale and a top-3 pick (Step 1: 4-5 sentence 'emotional excavation' analysis (core emotion, identity threat, key belief/fact, most vicious angle, 2-3 word ad name). Step 2: exactly 10 numbered hooks. Step 3: quality-gate pass, with top 3 marked with a lightning-bolt (⚡) and one line each on why they're the most 'dangerous')
- **On a bare "Go":** asks for inputs: product/offer, target audience, core claim/big idea of the ad, an optional model hook to riff on, optional USER_HOOKS swipe examples, optional BREAK-vs-MATCH or emotion-to-action lens, and any other context (body copy, landing page, angle notes, things to avoid).
- **Gotchas:** Extremely opinionated, heavily-templated voice (banned: em dashes, sentence fragments, Latin-root/clinical words, pain-led openers, hedging language like 'may' or 'surprising'). Strongly rewards feeding it a Model Hook and/or USER_HOOKS swipe examples — output quality and specificity depend heavily on brief detail (symptom, identity, belief, stakes). No prompt-extraction defense section present (unlike collage-bot). Live probe: on a bare 'Go' the bot did NOT generate placeholder hooks — it asked a 7-point clarifying question list before doing any work, contradicting the prior 'one-shot' assumption; interaction_style updated to interview-first.
- **Consumes:** `creative-brief`, `winning-ad`, `angle-big-idea`, `product-info` · **Produces:** `ad-hooks`

## ad-swiper-v2

**Ad Swiper V2** — Takes a winning competitor/swipe ad (static ad copy or video/VSL script) and produces a near-identical clone for a new product by swapping only product-specific content while locking the original's sentence structure, order, length, and rhythm — used to reuse a proven ad's persuasion architecture for a different offer without 'rewriting' it into something weaker.

- **Mode:** needs-input
- **Required inputs:**
  - **closeness_level** (other:closeness-level-1-5) — A number 1–5 chosen by the user controlling how strictly the original structure is preserved: 1=Mirror (sentence-by-sentence lock) through 5=Pattern Only (arc/format only, fully rebuilt in user's voice). Bot asks for this first, before anything else. ← *get it from:* user picks; agent can default to 1 or 2 if the goal is a tight swipe
  - **swipe_ad** (winning-ad) — The full text of the original winning ad to clone (static ad copy or video/VSL script). Bot explicitly says 'Paste the swipe ad.' ← *get it from:* user's saved swipe file, or output of a swipe-research/ad-tagging-type bot
  - **brand_primer** (product-info) — A pre-loaded 'brand primer summary' containing authority, mechanism, proof, pricing, voice, and brand ops context (where to buy, counterfeit warnings, channel restrictions) for the new product. The bot expects this to already be loaded into the session context (not pasted mid-conversation) and will only ask the user to paste product info if no primer is present. ← *get it from:* output of this platform's brand/primer-extraction bot (e.g. a 'primer-extractorsummarizer'-type tool) loaded into the session; if none exists, paste raw product info when prompted
- **Optional inputs (raise quality):**
  - **additional_proof** (product-info) — Extra real proof elements (studies, clinical results, expert endorsements) to fill a 'PROOF GAP' the bot flags when the primer lacks a proof element the original ad's structure requires. ← *get it from:* user supplies after seeing a PROOF GAP warning
- **Output:** One swiped ad matching the original's exact sentence count and structure, in either static-ad or video-script form depending on which format was swiped. (Clean prose ad copy (or video script) with identical sentence count/order to the original, no annotations — followed by a metadata tag block (Swiped from / Closeness level / Original preserved) and a lettered menu of next actions (rerun at different level, generate variation, convert to reusable Mad-Libs template, restart with new ad). Occasionally appends a '⚠️ PROOF GAP' or '⚠️ CHARACTER PLACEHOLDER' warning line.)
- **On a bare "Go":** asks for inputs: closeness level 1-5 (Mirror/Close/Flexible/Loose/Pattern Only), offered as a lettered menu before requesting the swipe ad itself.
- **Gotchas:** Strict structure-preservation bot, not a general rewriter — will refuse to 'improve' or restructure and redirects off-scope requests back to swiping. Requires a brand primer already loaded in-session for the new product; if missing, it asks the user to paste product info instead of failing silently. Has a hard anti-fabrication rule: never invents stats, studies, credentials, or names — uses placeholders like [EXPERT NAME] and flags gaps explicitly rather than making things up, even if the original swipe ad contains fabricated 'proof'. Levels 1-2 are near word-for-word Mad Libs swaps; levels 4-5 essentially become a full rewrite using only the original's format/emotional arc. Supports iterative follow-up actions (regenerate, template-ize, restart) after first output, so a single call rarely produces a finished multi-variant deliverable — expect a back-and-forth.
- **Consumes:** `winning-ad`, `product-info` · **Produces:** `ad-copy`, `video-script`

## bionic-bullet-bot

**Bionic Bullet Bot** — Turns raw product/offer information into a large set of emotionally-charged, curiosity-driven 'fascination' bullets for sales letters, ads, emails, VSLs, or lead magnets. Use it whenever you need a big batch of bullet-point copy that teases benefits/mechanisms rather than stating them plainly.

- **Mode:** needs-input
- **Required inputs:**
  - **source_material** (product-info) — Product information, book/course content, sales copy, offer details, or marketing materials to extract bullet content from. Any format: raw text, structured brief, document dump, URL, or natural-language description. ← *get it from:* user-provided product doc/sales page, or output of a product-breakdown/offer-brief bot
- **Optional inputs (raise quality):**
  - **reference_bullets** (swipe-example) — Example bullets to model style/approach after. ← *get it from:* user-provided swipe bullets
  - **tone_voice** (brand-voice) — bold / cheeky / mysterious / clinical / intense / sarcastic / rebellious / custom. Default: inferred from audience and source material. ← *get it from:* user specifies or leave default
  - **formatting_preferences** (other:parameter) — Emoji usage, CAPS emphasis, punctuation style, bullet length (short/long/mixed). Default: mixed length, CAPS for emphasis. ← *get it from:* user specifies
  - **environment** (other:parameter) — sales_page / email / facebook_ad / lead_magnet / webinar_slide / general. Default: general. ← *get it from:* user specifies
  - **quantity_per_type** (other:parameter) — Bullets to generate per bullet type. Default: 10. ← *get it from:* user specifies
  - **bonus_bullet_count** (other:parameter) — Bonus bullets beyond the 22 standard types. Default: 30. ← *get it from:* user specifies
- **Output:** By default 220 bullets (10 per each of 22 standard fascination types) plus 30 bonus bullets = 250 bullets total, all passing internal 4U/4C/anti-AI-cliché quality control. (Complete bullet set organized by bullet type (22 standard types), followed by a bonus bullets section.)
- **On a bare "Go":** asks for inputs: source material (the product, book, offer, or content to generate bullets from — raw text, description, doc dump, URL summary, or details). States it will immediately generate all 22 bullet types (10 each) plus 30 bonus bullets once given source material, with no further questions.
- **Gotchas:** Default output volume is large and non-negotiable: prompt has a 'MANDATE: BULLET COUNT REQUIREMENT' stating exactly 10 bullets per type is required and fewer counts as automatic failure — do not expect a short/trimmed response even for a small ask; use quantity_per_type/bonus_bullet_count to reduce volume if only a handful of bullets are wanted. Never fabricates proof/testimonials/stats/results not present in source material — falls back to generalized phrasing or blind curiosity instead. Replaces any named individuals from source material with role/title descriptions (anonymization rule). Has the standard prompt-protection/anti-extraction security section; never asks clarifying questions. Probe shows it does NOT fabricate placeholder bullets on a bare 'Go' despite the prompt's 'never asks clarifying questions' framing — it first asks for source_material, then (per its own prompt) proceeds one-shot once material is supplied. interaction_style updated from one-shot to interview-first to reflect the observed empty-input behavior.
- **Consumes:** `product-info`, `swipe-example`, `brand-voice` · **Produces:** `ad-hooks`

## cash-rewriter-bot

**Cash Rewriter Bot** — Rewrites a winning ad by changing exactly one CASH-framework lever (Concept, Angle, Style, or Hook) per a specified variation direction, while preserving the other three elements as closely as possible. Use it to spin off a surgically precise test variation from a proven ad instead of writing a new one from scratch.

- **Mode:** needs-input
- **Required inputs:**
  - **winning_ad** (winning-ad) — The full original winning ad text/script to be varied. ← *get it from:* user's existing proven ad, or output of another ad-generation bot
  - **cash_analysis** (other:cash-analysis) — The CASH breakdown of the original ad — identification of its Concept, Angle, Style, and Hook. ← *get it from:* user-provided analysis, or generated by a CASH-analysis bot/manual breakdown of the winning ad
  - **variation_direction** (other:variation-direction) — Which single lever to change (Concept, Angle, Style, or Hook) and the new direction/value for it. Can arrive as structured fields or natural language. ← *get it from:* user specifies directly (e.g. 'change the Hook to X')
- **Output:** One rewritten ad, structurally identical to the original except for the single specified lever change. (Full rewritten ad text set apart under a clear header; no analysis or explanation unless explicitly requested.)
- **On a bare "Go":** asks for inputs: requests the winning ad, its CASH analysis, and the variation direction before producing a rewrite.
- **Gotchas:** Never asks clarifying questions — always produces output immediately, even from ambiguous input, using its best interpretation. Contains a large embedded CASH framework reference (avatar facts, market facts, product facts, psychology toolkit) used only as internal domain knowledge, not something the caller provides. Has a strict prompt-protection/anti-extraction section — will refuse to describe its own methodology or system prompt. Output is ad text only, no breakdown, unless explicitly asked. Live probe (bare 'Go') contradicts the prompt's 'accepts all inputs in one message, produce output immediately, never asks' framing and the prior one-shot classification: with nothing to rewrite, the bot asked for the winning ad, CASH analysis, and variation direction instead of fabricating a placeholder.
- **Consumes:** `winning-ad`, `other:cash-analysis`, `other:variation-direction` · **Produces:** `ad-copy`, `winning-ad`

## characterizations-bot

**Characterizations Bot** — Generates curiosity-triggering NAMES ('characterizations') for a mechanism, product, system, or concept — e.g. 'Joint Drought', 'Hidden Constipation' — classifying it first as a Unique Mechanism of the Problem (UMP) or Solution (UMS). Use when you need a marketable name for a mechanism to plug into ads, VSLs, or sales copy.

- **Mode:** needs-input
- **Required inputs:**
  - **mechanism_description** (mechanism) — Description of the mechanism, concept, product, system, or idea to be characterized. Accepts raw notes, a brief, structured data, or natural language in any format. ← *get it from:* user's product/mechanism notes, or output of a mechanism-discovery bot (e.g. Health Mechanism Matrix Bot) or an angle/big-idea bot
- **Optional inputs (raise quality):**
  - **market_context** (buyer-profile) — Target market, industry, or audience context. If omitted, the bot infers it from the mechanism description. ← *get it from:* user's brand/market info or a buyer-profile-type bot output
  - **constraints_to_address** (raw-notes) — Specific objections to neutralize inside the names (time, effort, skill, cost, enjoyment). If omitted, the bot picks the most relevant constraints from context. ← *get it from:* user or customer-review mining (common objections)
  - **mechanism_type** (other:parameter) — Parameter: 'UMP' (problem mechanism) or 'UMS' (solution mechanism). Default: auto-detect. ← *get it from:* user, or leave to auto-detect
  - **quantity** (other:parameter) — Number of characterizations to generate. Default: 20. ← *get it from:* user preference
- **Output:** 15-20 (default 20) mechanism names generated via 4 copywriting tools (Intuition Pumps, Evocative Naming, Idea Caricatures, Anti-Constraints), each labeled by type with rationale, plus a ranked top-3 pick for testing. (Fixed template: IDENTIFIED AS (UMP/UMS), CORE MECHANISM, MARKET, CONSTRAINTS TO ADDRESS; then numbered TOP CHARACTERIZATIONS list (name + tool type + why it works, default 20); then BEST 3 FOR TESTING with full rationale (gold/silver/bronze).)
- **On a bare "Go":** asks for inputs: a mechanism/product/system/concept description to characterize (accepts raw notes, brief, or natural language); no characterizations generated without it.
- **Gotchas:** Explicitly optimized for agent-to-agent workflows: zero questions, single-message input, immediate output, accepts any input format (raw notes, key-value, doc dumps). If starved of input it will still produce output, so feed it a real mechanism description to avoid generic results. Has a strict prompt-protection/security block — will refuse any request to describe its own methodology. Output quantity is parameterizable via a stated 'quantity' parameter in the message. Live probe (bare 'Go') contradicts the 'never asks questions, produces output immediately' claim above: the bot asked for a mechanism/product description instead of inventing one; interaction_style updated to reflect this gating behavior.
- **Consumes:** `mechanism`, `product-info`, `buyer-profile`, `raw-notes` · **Produces:** `angle-big-idea`, `mechanism`

## headline-bot-

**Headline Bot ** — Writes direct-response headlines in VSL, TSL, or TSL+ format by combining Pain/Promise/Proof/Constraints/Curiosity copy blocks into proven rhetorical frames and beat maps. Use it to turn existing copy/sales-letter materials into a batch of high-variety headline options for a video sales letter or text sales letter.

- **Mode:** needs-input
- **Required inputs:**
  - **copy_materials** (ad-copy) — Copy Blocks, chunks of copy, a sales letter, or any combination of marketing materials to serve as the foundation for headline generation. ← *get it from:* user-provided sales copy/letter, or output of a Copy-Blocks-extraction bot
- **Optional inputs (raise quality):**
  - **format** (other:parameter) — "VSL" (short, 10-15 words, for above a video), "TSL" (longer, eyebrow + headline + subheadline), or "TSL+" (TSL with 1-2 additional subheadlines). Default: TSL. ← *get it from:* user specifies
  - **quantity** (other:parameter) — Number of headline variations to generate. Default: 10. ← *get it from:* user specifies
- **Output:** 10 headline variations by default in the chosen format (VSL/TSL/TSL+), maximizing copy-block density per headline. (List of headline variations, each referencing the Rhetorical Frame or Beat Map used; includes 2 wildcard headlines using original judgment.)
- **On a bare "Go":** asks for inputs: marketing materials (sales letter, copy blocks, product description, or any combination) plus the desired headline format (VSL/TSL/TSL+) and quantity if different from the default of 10. Does not generate placeholder headlines on empty input.
- **Gotchas:** Contains a minor legacy remnant near the end ('The user will then tell you whether they want a VSL, TSL or TSL+ headline') implying an older interactive flow, but this conflicts with the authoritative top-of-prompt one-shot/no-questions directive — supply format explicitly rather than relying on the bot to ask. Style rules: no colons, 3rd-6th grade reading level, avoid overloading with numbers, must not copy the framework's own example headlines verbatim, must reference which Rhetorical Frame/Beat Map each headline uses. Has the standard prompt-protection/anti-extraction security section. Probe shows the bot asks for copy_materials (and format/quantity) up front rather than inventing headlines from nothing, contradicting the one-shot/no-questions framing implied by the prompt. interaction_style updated from one-shot to interview-first.
- **Consumes:** `ad-copy`, `other:copy-blocks` · **Produces:** `headline`

## marcio-narrative-ads-bot-

**Marcio Narrative Ads Bot ** — Writes long-form 'Trojan Horse Narrative' ads (Facebook in-feed, VSL script, prelander/advertorial, or hybrid) that open with a cold, unaware-audience story unrelated to the product and only reveal the product/mechanism as the story's resolution. Use it when you need a cold-traffic emotional narrative ad rather than a direct-response/features-first ad.

- **Mode:** needs-input
- **Required inputs:**
  - **product_info** (product-info) — What the product is, mechanism/ingredients/key features, what condition/problem it addresses, offer details (price, guarantee, availability) ← *get it from:* user's product page, brand doc, or offer brief
  - **audience_info** (buyer-profile) — Target demographic (age, gender, life stage), buyer profile/Build A Buyer output or audience research, emotional state and fears, what they've tried, awareness level ← *get it from:* output of a buyer-profile-type bot (e.g. Build A Buyer), or user-supplied audience research
- **Optional inputs (raise quality):**
  - **narrator** (other:narrator-preference) — Spokesperson, customer, composite character, or specific demographic to narrate the story; bot picks the highest-resonance narrator if omitted ← *get it from:* user preference
  - **format** (other:format-selector) — One of "facebook" / "vsl" / "prelander" / "hybrid". Default: facebook ← *get it from:* user choice
  - **existing_assets** (winning-ad) — Sales letters, VSLs, emails, existing copy, catalysts already tested/considered, angles to avoid, creative direction/constraints ← *get it from:* user's swipe file or prior ad drafts
  - **output_scope** (other:scope-selector) — "catalysts" (options only) / "arc" (catalyst + arc map) / "draft" (full ad). Default: draft ← *get it from:* user choice
  - **num_catalysts** (other:count) — Number of catalyst options to generate when output_scope=catalysts. Default: 3 ← *get it from:* user choice
  - **selected_catalyst** (angle-big-idea) — A previously generated catalyst to lock in, skipping catalyst discovery ← *get it from:* output of a prior catalysts-scope call to this same bot
  - **approved_arc** (other:narrative-arc) — A previously generated 9-beat arc map to use as blueprint, skipping arc mapping ← *get it from:* output of a prior arc-scope call to this same bot
  - **revision instructions** (other:revision-request) — A previously generated draft plus revision instructions (tighten, re-angle, new version, etc.) to revise instead of generate fresh ← *get it from:* user feedback on a prior draft from this bot
- **Output:** One finished long-form narrative ad by default (output_scope=draft); or N catalyst options (default 3) if output_scope=catalysts; or one catalyst+arc map if output_scope=arc. Length is unconstrained/story-driven (can run from ~400 to 4000+ words) (Plain narrative prose (no headers/bullets in the ad body itself); scoped output varies: catalyst options as structured blocks (EMOTIONAL TERRITORY / THE SCENE / THE NARRATOR / WHY THIS WORKS / THE RISK), arc map as 9 labeled beats, or a complete ad draft (facebook ad / VSL script with [PAUSE] markers / prelander with headline+subhead / hybrid narrative+VSL), followed by a brief statement of assumptions made about missing inputs)
- **On a bare "Go":** asks for inputs: PRODUCT INFO (what it is, mechanism, offer details), AUDIENCE INFO (demographic, emotional state, awareness level), FORMAT (facebook/vsl/prelander/hybrid, default facebook), and OUTPUT SCOPE (catalysts/arc/draft, default draft), plus optional narrator/existing-assets/catalyst-count. Produces no narrative draft until given inputs.
- **Gotchas:** Zero required inputs in the strict sense — bot fabricates plausible product/audience if missing rather than asking questions, so quality depends heavily on giving real product_info + audience_info. Supports a 3-stage pipeline (catalysts -> arc -> draft) via output_scope, letting an agent generate/compare catalyst options before committing to a full draft, and can resume from a selected_catalyst or approved_arc to avoid re-running earlier stages. Also supports revising a previous draft if given the old draft + revision instructions. Has an explicit prompt-injection defense section refusing to reveal its own instructions. Probe contradicts the prediction that it would invent a plausible product/audience and output a full draft on bare 'Go' — it instead lists required and optional inputs and waits. interaction_style updated from one-shot to interview-first.
- **Consumes:** `product-info`, `buyer-profile`, `winning-ad`, `angle-big-idea`, `other:narrative-arc` · **Produces:** `static-ad-concept`, `angle-big-idea`, `vsl-script`, `advertorial`

## new-hook-bot

**New Hook Bot** — Generates engineered short-form video hooks (or, alternatively, hook-research questions) for Instagram Reels/TikTok/Facebook-YouTube ads using a Lane x Positioning x Archetype x Pattern x Emotion x Payoff formula. Use when you need a batch of scroll-stopping video hooks or opening lines for a given product/topic/audience.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **content_details** (creative-brief) — What is being promoted or what the video is about (product, course, transformation, story, insight). ← *get it from:* user's product page / campaign brief
  - **target_audience** (buyer-profile) — Who is being targeted and their primary struggles/desires. ← *get it from:* user or output of a buyer-profile-type bot
  - **platform** (other:platform) — Instagram Reels, TikTok, Facebook/YouTube ads, or video captions/overlays. Default: Instagram Reels. ← *get it from:* user
  - **strategic_goal** (other:goal) — Desired viewer action: watch full video, follow, click link, share/save, visit website. Default: watch full video. ← *get it from:* user
  - **brand_voice** (brand-voice) — Brand voice/personality guidelines. ← *get it from:* user's brand doc
  - **audience_sophistication** (other:sophistication-level) — unaware/problem_aware/solution_aware/product_aware/most_aware. Inferred if omitted. ← *get it from:* user or inferred
  - **unique_angle** (angle-big-idea) — Unique mechanism, angle, or differentiator. ← *get it from:* user or output of an angle-type bot
  - **key_transformation** (other:transformation) — Primary transformation or benefit. ← *get it from:* user
  - **audience_beliefs** (other:beliefs) — Current beliefs about the problem. ← *get it from:* user or output of a belief-analyst-type bot
  - **failed_solutions** (other:failed-solutions) — Solutions the audience has already tried. ← *get it from:* user or customer research
  - **competitive_context** (competitor-info) — What's working in market, overused angles to avoid, unique advantages. ← *get it from:* user or competitor research
  - **avoid_list** (other:avoid-list) — Topics, words, or approaches to avoid. ← *get it from:* user
  - **additional_context** (raw-notes) — Any other relevant info: research, competitor hooks, liked examples, raw content ideas. ← *get it from:* user
  - **output_type** (other:param) — "hooks" or "research_questions". Default: hooks. ← *get it from:* user
  - **generation_style** (other:param) — speed_round/strategic_set/premium_picks/full_spectrum/experiment/platform_optimized/hook_and_opener. Default: strategic_set. ← *get it from:* user
  - **quantity** (other:param) — Number of hooks to generate; overrides style default. ← *get it from:* user
  - **include_strategy_analysis** (other:param) — Include strategic lane/positioning/anchor/pattern/emotion analysis before hooks. Default: true. ← *get it from:* user
  - **include_scoring** (other:param) — Score each hook on cognitive load/tension/anchor clarity/emotional impact. Default: false. ← *get it from:* user
  - **enhancement_dimensions** (other:param) — Specific dimensions to dial up (e.g. 'increase specificity', 'dial up urgency'). Default: none. ← *get it from:* user
- **Output:** A batch of 5-20+ short-form video hooks (count and depth set by generation_style/quantity), or alternatively 15-20 hook-research questions if output_type=research_questions. (Emoji-headed sections varying by generation_style: numbered list (speed_round), numbered list with archetype/pattern/anchor notes (strategic_set, default 10), full breakdown blocks with DNA/why-it-works/platform/pro-tip (premium_picks, 5), or hook+script opener pairs (hook_and_opener). Optional strategic analysis block precedes hooks; optional scoring line follows each hook.)
- **On a bare "Go":** asks for inputs: what the video is about / what's being promoted, and who the target audience is — offers a one-liner example as the minimum bar and invites dropping whatever is available.
- **Gotchas:** Never asks questions and never refuses on sparse input — ideal for agent-to-agent chaining. Has a strict prompt-protection/anti-extraction security section at the end (will not describe its own methodology if asked). output_type=research_questions is a distinct secondary mode producing 15-20 questions instead of hooks — worth exposing as an option to agents needing audience research prompts, not just hooks. LIVE PROBE CONTRADICTS PROMPT TEXT: despite the prompt's explicit 'never asks questions, produces output immediately' instruction, a bare 'Go' actually gets a request for content_details and target_audience rather than a default 10-hook batch — treat this probed behavior as ground truth; front-load at least a one-line content_details + target_audience to get true one-shot output.
- **Consumes:** `creative-brief`, `buyer-profile`, `brand-voice`, `angle-big-idea`, `competitor-info`, `raw-notes` · **Produces:** `ad-hooks`

## organic-viral-to-paid-v2

**Organic Viral to Paid V2** — Converts a piece of viral organic content (TikTok/Reel/YouTube transcript, tweet, podcast snippet) into a ready-to-run paid ad: 5 interchangeable hooks, one shared body copy, a transition, and a fully assembled ad. Use when you have a viral swipe (organic post transcript) and want to adapt its proven hook/structure onto your own product.

- **Mode:** multi-phase
- **Required inputs:**
  - **organic_content** (swipe-example) — The viral organic content itself — transcript, description, or full text of the TikTok/Reel/YouTube clip/tweet/podcast snippet to be swiped. If missing or unclear, the bot asks for clarification before proceeding. ← *get it from:* user pastes the transcript/caption text of the viral post
  - **brand primer summary** (other:brand-primer) — Product/brand info — authority, mechanism, proof, pricing, voice, brand ops (where to buy, counterfeit warnings, channel restrictions) — expected to be 'loaded automatically from the extracted brand primer summary for this session.' If not already loaded, the bot explicitly asks: "I don't have your brand primer loaded. Can you provide your product info?" ← *get it from:* an upstream brand-primer/brand-primer-extraction step in the same session, or paste product info directly if no primer system is wired up
- **Optional inputs (raise quality):**
  - **proof elements** (other:proof-elements) — Real statistics, credentials, named authority figures, customer counts, or testimonials for the product. Bot will NEVER fabricate these — if missing where needed it flags '⚠️ PROOF NEEDED' and asks the user directly rather than inventing anything. ← *get it from:* user supplies real numbers/credentials/testimonials; cannot be sourced from the organic content itself even if it contains proof
  - **topic-fit guidance** (other:directive) — If it's unclear whether the organic content's topic connects to the product, the bot will ask the user for clarification or suggest which aspect connects best / offer 2-3 transition angle options. ← *get it from:* user answers the bot's clarifying question
- **Output:** One fully assembled paid ad plus 5 modular/interchangeable hooks that can each be swapped in without editing the shared body copy — not multiple full ads, one ad with swappable openers (Fixed sections: 🎣 HOOK VARIATIONS (handoff point + 5 labeled hooks V1-V5) → 📖 BODY COPY → 🔄 TRANSITION + PRODUCT COPY → 📝 FULL AD - ASSEMBLED (using V1) → Source/Type footer. Internal 'Content Analysis' (hook type, topic transferability, emotional driver, mechanism, handoff point, proof status) is done but never shown.)
- **On a bare "Go":** asks for inputs: (1) the organic content to swipe (transcript/description of the viral piece) and (2) product info, explicitly stating 'I don't currently have [a brand primer] for this session' and listing what/mechanism/who/pain points/proof/purchase location.
- **Gotchas:** Depends on a 'brand primer summary' being auto-loaded in-session (an upstream/system-level context object with authority, mechanism, proof, pricing, voice, brand ops) — if the calling system doesn't inject one, an agent must paste product info manually or the bot will ask for it. Has an unusually strict PROOF INTEGRITY PROTOCOL: never fabricates stats/credentials/studies, never transfers proof from the organic source (different niche), and will explicitly ask the user to confirm/provide real numbers rather than inventing them — a major behavioral gotcha vs. most other bots which silently fabricate placeholders. Also has a 'TOPIC TRANSPLANTATION' mode: if the organic content's topic is unrelated to the product, it replaces the topic entirely rather than forcing an awkward bridge, and may ask the user to clarify product fit. Heavy 'anti-AI' style module with a long forbidden-word/forbidden-pattern list (no em dashes as hyphens, no 'journey/leverage/delve', no triplets, etc.) — output prose style is tightly constrained. Refuses to do general copywriting/strategy/critique — strictly organic-to-paid conversion only, with a canned redirect line for other requests.
- **Consumes:** `swipe-example`, `other:brand-primer`, `product-info`, `other:proof-elements` · **Produces:** `ad-copy`, `ad-hooks`

## paradoxical-questions-bot

**Paradoxical Questions Bot** — Generates a large volume of paradoxical 'huh, why IS that?' pattern-interrupt questions (optionally with concise answers) for a target market, organized by 5 assumption-violation types. Use to source curiosity hooks and lead openers for ads, emails, and VSLs.

- **Mode:** needs-input
- **Required inputs:**
  - **category** (content-topic) — The target market category or niche to generate questions for (e.g. 'dog joint health', 'B2B lead gen') ← *get it from:* user states the niche; or derive from product page / buyer profile
- **Optional inputs (raise quality):**
  - **product_context** (product-info) — Details about the product/offer — tailors questions so they naturally lead toward the product's mechanism ← *get it from:* user's product page or offer brief
  - **target_audience** (buyer-profile) — Demographics, pain points, beliefs, desires of the audience ← *get it from:* output of a buyer-profile-type bot or user's audience research
  - **additional_context** (research-report) — Competitor angles, known objections, market sophistication level ← *get it from:* user research or competitor analysis
  - **output_focus** (other:parameter) — 'questions_only' | 'questions_and_answers' (default: questions_and_answers, answers kept concise) ← *get it from:* caller decides
  - **quantity** (other:parameter) — Target number of questions (default: maximum possible while maintaining quality) ← *get it from:* caller decides
- **Output:** Large list (defaults to maximum volume) of market-specific paradoxical questions usable as pattern interrupts / curiosity hooks; prioritizes KNOWN violations the audience personally experiences (Hierarchical formatted list (bold/emoji headings) grouped by 5 violation types: Causation, Pattern, Linear, System, Context; each question optionally followed by a concise answer)
- **On a bare "Go":** asks for inputs: a category/target market/niche (stated as the minimum needed); optionally product context, target audience, and additional context for more targeted questions.
- **Gotchas:** Output is questions, not finished copy; they're raw hook material meant to be woven into ads/VSLs. Defaults to including short answers; pass output_focus=questions_only to suppress. Volume-biased: expect a very long list unless you cap quantity. LIVE PROBE UPDATE: contrary to the prediction that it would guess a broad market rather than ask, a bare 'Go' produced a direct request for the category, confirming this is the one true hard requirement (as already reflected in required_inputs).
- **Consumes:** `content-topic`, `product-info`, `buyer-profile`, `research-report` · **Produces:** `ad-hooks`

## segmentmech-swapper-bot

**Segment/Mech Swapper Bot** — Takes a winning ad and surgically swaps either the SEGMENT (target audience: pain language, constraints, buying triggers, sophistication) or the MECHANISM (UMP root-cause explanation or UMS how-it-works explanation), preserving everything else and the ad's original structure/flow. Use it to re-target a proven ad to a new audience or re-explain the problem/solution without a full rewrite.

- **Mode:** needs-input
- **Required inputs:**
  - **winning_ad** (winning-ad) — The original ad to transform (full text). ← *get it from:* user's existing proven ad
  - **swap_type** (other:parameter) — "segment" or "mechanism". If omitted, inferred: segment info provided -> segment swap; new mechanism provided -> mechanism swap. ← *get it from:* user specifies, or inferred from which other inputs are supplied
- **Optional inputs (raise quality):**
  - **segment_brief** (buyer-profile) — For segment swaps: a complete segment brief, or minimum viable fields — Core Desire/Pain, Motivation Type (Towards/Away), Key Blocking Beliefs, Awareness Level (Unaware/Problem/Solution/Product/Most Aware), Sophistication (Low/Medium/High). ← *get it from:* user-provided, or output of a Segment Surgeon-type bot
  - **target_segment** (other:parameter) — If multiple segments are provided, which one to swap to. Defaults to the first provided. ← *get it from:* user specifies
  - **mechanism_type** (other:parameter) — For mechanism swaps: "UMP" (why the problem exists) or "UMS" (how the solution works). Inferred from the new_mechanism content if not specified. ← *get it from:* user specifies or inferred
  - **new_mechanism** (mechanism) — The new mechanism to swap in. If omitted, the bot generates 3 S.I.N. (Simple/Intuitive/New) mechanism options and uses the first for the swap. ← *get it from:* user-provided, or self-generated by the bot if absent
- **Output:** One transformed ad (same length/structure as the original) plus, for auto-generated mechanism swaps, 3 mechanism options. (Clean plain text of the fully transformed ad; if mechanisms were auto-generated, the 3 mechanism options are listed first, then the transformed ad using option 1.)
- **On a bare "Go":** asks for inputs: winning_ad (original ad), swap_type (segment or mechanism), plus segment brief/minimum-viable fields for segment swaps or mechanism type + new mechanism (or offers to generate 3 options) for mechanism swaps
- **Gotchas:** Applies 'Minimum Viable Belief Change' — only rewrites what must change, preserving as much original phrasing/length as possible; explicitly runs internal quality checks to avoid a 'frankensteined' feel and to make sure segment swaps don't accidentally touch mechanism content (and vice versa). If no new_mechanism is supplied for a mechanism swap, it invents 3 options itself and picks one — caller should specify new_mechanism if they want control over it. Has the standard prompt-protection/anti-extraction security section. LIVE PROBE CONTRADICTION: despite the prompt's 'never ask clarifying questions' rule, a bare 'Go' actually returns a clarifying request for winning_ad and swap_type rather than a fabricated placeholder transformation. Treat as interview-first, not one-shot.
- **Consumes:** `winning-ad`, `buyer-profile`, `mechanism` · **Produces:** `ad-copy`, `mechanism`

## swiping-bot-master-bot

**Swiping Bot Master Bot** — Takes a proven/winning ad (static copy or video/VSL script) and rebuilds it for a new product by swapping only product-specific content, keeping sentence count, order, grammar, rhythm, and transitions locked ('same skeleton, different skin'). Use it when you have a winning competitor or past ad and want to adapt it to a new product without breaking what made it convert.

- **Mode:** needs-input
- **Required inputs:**
  - **swipe_ad** (winning-ad) — The winning ad to adapt — static ad copy or a video ad/VSL script, pasted in full. ← *get it from:* user pastes a proven ad (their own past winner or a competitor's), or a swipe-example from research
  - **product_info** (product-info) — Any combination of product/offer description, target audience details, Build-a-Buyer profile, copy blocks (pains, desires, mechanism, proof, offer, hooks), sales page/VSL content, or other relevant material about the new product. ← *get it from:* user's product/offer doc, or output of a buyer-profile or creative-brief bot
- **Optional inputs (raise quality):**
  - **output_mode** (other:parameter) — "swiped_ad" / "template" / "both". swiped_ad = final rewritten ad only; template = Mad Libs version with bracketed placeholders over locked phrases; both = swiped ad then template. Default: swiped_ad. ← *get it from:* caller specifies explicitly
  - **quantity** (other:parameter) — Number of swiped variations to generate, each with the same locked structure but different word choices/hook angles. Default: 1. ← *get it from:* caller specifies explicitly
  - **include_annotation** (other:parameter) — Boolean — prepend a sentence-by-sentence structural annotation table (original sentence, function, locked phrases, replaced content) before the swiped output. Default: false. ← *get it from:* caller specifies explicitly
- **Output:** 1 or more (per quantity) 'swiped' ad variants structurally identical to the input ad but re-skinned with the new product's details; optionally also a fill-in-the-blank template version. (Clean rewritten ad copy matching the original's exact sentence count/order/rhythm (no labels or commentary by default); optionally preceded by a sentence-by-sentence annotation table, and/or followed by a bracketed-placeholder Mad Libs template. Repeats per requested quantity.)
- **On a bare "Go":** asks for inputs: replies tersely "Ready. Send your swipe ad and product info." — waits for both swipe_ad and product_info rather than fabricating a placeholder ad.
- **Gotchas:** Strictly does NOT rewrite or improve the ad — explicitly refuses to critique, rate, or restructure; if the output doesn't look nearly identical to the original it's considered a failure. Needs the swipe_ad pasted in full (not a URL/description) since it operates sentence-by-sentence. Handles cross-niche swipes (e.g. skincare ad -> supplement product) by noting the mismatch in the header and proceeding, never refusing. Has the same prompt-extraction security block as other bots in this set (won't describe its own methodology). LIVE PROBE: despite the system prompt's claim it never asks questions, a bare 'Go' produced a short prompt for the two required inputs rather than a fabricated placeholder ad — consistent with required_inputs already listing swipe_ad and product_info as mandatory.
- **Consumes:** `winning-ad`, `product-info`, `buyer-profile`, `creative-brief`, `vsl-script`, `video-script` · **Produces:** `ad-copy`, `video-script`

## swiping-master-bot

**Swiping Master Bot** — Takes a proven 'winning' ad (static or VSL-style script) and produces a near-identical clone for a new product by swapping only product-specific content while locking the original's sentence structure, order, rhythm, and length — for cloning a competitor's or past winner's proven ad structure onto a new offer without 'AI-rewriting' away what makes it work.

- **Mode:** needs-input
- **Required inputs:**
  - **swipe_ad** (winning-ad) — The original winning ad to clone — full static ad copy or VSL/video ad script text, pasted in full ← *get it from:* user pastes a proven ad (their own past winner or a competitor's ad they want to swipe)
  - **product_info** (product-info) — What's being sold, who it's for, and any copy blocks (benefits, proof, testimonials, mechanism, pains, offer, hooks) for the new product being substituted in ← *get it from:* user, or output of a Build-a-Buyer / Copy Blocks type bot
- **Output:** One swiped ad matching the original's exact skeleton with new product content; follow-up options let the user request another variation, convert to a reusable placeholder template, or restart with a new swipe ad. (Plain clean ad copy text (no annotations/labels) matching the original's sentence count/order/line breaks; also produces an intermediate sentence-by-sentence structural annotation table before the final swap, and can output a bracketed Mad-Libs template on request)
- **On a bare "Go":** asks for inputs: confirmed verbatim — replies exactly "Paste the swipe ad you want me to adapt." and waits, matching the documented fixed opening line.
- **Gotchas:** Strict two-step interview: (1) paste swipe ad -> bot returns sentence-by-sentence structural breakdown table and asks for product info; (2) paste product info -> bot delivers the swiped ad. This is NOT a single-shot bot — an agent must send the swipe ad first, wait for the annotation, then send product info in a second turn (or the bot may accept both in one message per the accept-any-format language, but the documented flow is two-step). After delivery it offers menu options: (A) another variation, (B) convert to reusable bracketed template, (C) restart with new swipe ad. Explicitly refuses to critique ads, give strategy, or restructure — scope is strictly 'replace content in a locked structure.'
- **Consumes:** `winning-ad`, `product-info`, `buyer-profile`, `landing-page-copy`, `vsl-script` · **Produces:** `ad-copy`, `swipe-example`

## unaware-bot-master-bot

**Unaware Bot Master Bot** — Produces ad hooks (and optionally full ad scripts) aimed at 'problem-unaware' prospects — people who don't yet know they have the problem the product solves. Analyzes provided market/product materials to surface already-pressurized emotional drivers, then builds curiosity-first hooks/ads that never mention the product up front. Use when you want top-of-funnel ads to expand reach beyond the aware-prospect pool.

- **Mode:** needs-input
- **Required inputs:**
  - **build_a_buyer** (buyer-profile) — Target market psychology document. ← *get it from:* output of a Build-a-Buyer / buyer-profile-type bot
  - **product_offer** (offer-details) — What is being sold, price point, what problem it solves, what makes it different. ← *get it from:* user's product/offer info
  - **copy_blocks** (other:copy-blocks) — Product angles and proof elements. ← *get it from:* output of a copy-blocks-extract type bot, or user-supplied
- **Optional inputs (raise quality):**
  - **winning_ads** (winning-ad) — Any ads already working for this offer. ← *get it from:* user's ad account / swipe file
  - **sales_materials** (landing-page-copy) — Sales pages, VSL scripts, or other marketing materials. ← *get it from:* user
  - **customer_research** (customer-reviews) — Testimonials, reviews, customer research. ← *get it from:* user or a review-mining bot
  - **competitor_examples** (competitor-info) — Competitor ads or positioning. ← *get it from:* user or ad-swiper-type bot
  - **output_type** (other:parameter) — "hooks" (default) = emotional driver analysis + hook batches only. "full_ad" = also develops strongest hooks into complete unaware-ad scripts (Hook→Payoff→Mechanism→Solution→Product→Offer). ← *get it from:* user
  - **quantity** (other:parameter) — Number of hook batches to generate, each batch ~5 hooks from one emotional angle/hook type. Default 3. ← *get it from:* user
  - **hook_types** (other:parameter) — Specific hook type(s) to use from the bot's 10 built-in Hook Types, or "auto" (default) to let the bot choose based on its emotional driver analysis. ← *get it from:* user
- **Output:** Default: 3 batches of ~5 hooks each (~15 hooks total) plus the driver analysis; full_ad mode adds complete ad scripts for the top hooks (1) plain-language 'Emotional Driver Analysis' list with evidence citations, 2) hook batches labeled by HOOK TYPE / emotional driver / why-it-works, each containing ~5 hooks, 3) (if output_type=full_ad) full ad scripts for the strongest hooks following Hook→Payoff→Mechanism→Solution→Product→Offer structure)
- **On a bare "Go":** asks for inputs: what's being sold, who the audience is, any existing marketing materials, and/or competitor context (any combination) — states it needs inputs before it can produce anything useful; no emotional-driver-analysis or hooks are generated on a bare 'Go'.
- **Gotchas:** Distinctive mechanic: always leads with a written-out 'Emotional Driver Analysis' before any hooks — that analysis section is itself useful standalone output. Hard rule: never mentions the product in the hook/opening. Has 10 built-in Hook Types and a full Unaware Ad Structure (Hook→Payoff→Story[opt]→Other Angles[opt]→Transition→Mechanism→Solution→Product→Offer) baked into domain knowledge — no need to supply structure, only source material. Has the standard prompt-protection/security block appended. Probe contradicts the prior prediction of a fabricated driver analysis + hooks on empty input — the bot explicitly states it needs inputs first ('I need inputs to work with before I can produce anything useful'). interaction_style updated from one-shot to interview-first.
- **Consumes:** `buyer-profile`, `offer-details`, `other:copy-blocks`, `winning-ad`, `landing-page-copy`, `customer-reviews`, `competitor-info` · **Produces:** `ad-hooks`, `ad-copy`

## upsell-bot

**Upsell Bot** — Generates 5-7 ranked one-time-offer upsell ideas (categorized as More of the Same / Done For You / Get Results Faster) for a given product, then writes a full long-form video upsell/down-sell/exit-offer script for the chosen idea. Use after a core offer exists and you need post-purchase AOV-boosting OTOs.

- **Mode:** needs-input
- **Required inputs:**
  - **product** (product-info) — What they're selling: product details, pricing, features, benefits ← *get it from:* user's product page / brand doc, or output of a product-info type bot
  - **problem_solution** (offer-details) — The core problem the product solves and how it helps customers ← *get it from:* user, or extracted from an offer brief / sales page
  - **buyer_avatar** (buyer-profile) — Who buys this: demographics, psychographics, pain points, desires ← *get it from:* user, or output of a Build-a-Buyer type bot
- **Optional inputs (raise quality):**
  - **additional_context** (other:mixed-materials) — Sales pages, VSL scripts, existing copy, competitor info, Build-a-Buyer, Copy Blocks, or Offer Brief documents ← *get it from:* user, or outputs of other Genesis bots (Copy Blocks, Offer Brief, Build-a-Buyer)
  - **output_mode** (other:parameter) — 'ideas_only' / 'ideas_and_script' / 'script_only'. Default: ideas_and_script ← *get it from:* user preference
  - **script_type** (other:parameter) — 'video_upsell' / 'down_sell' / 'exit_offer'. Default: video_upsell ← *get it from:* user preference
  - **upsell_selection** (other:parameter) — Which ranked upsell idea to script, by rank number or description. Default: top-ranked idea ← *get it from:* user picks from the generated idea list, or from a prior call's output
- **Output:** 5-7 categorized upsell ideas plus one complete video (or down-sell/exit-offer) script for the selected idea; applies Copy Blocks methodology and an 'anti-AI' humanizing writing style (Numbered/ranked list of 5-7 upsell ideas (each labeled with category + why-it-works explanation), followed by a full long-form (11-15+ minute) video script structured as: purchase acknowledgment -> bridge from original purchase -> present upsell -> build value/urgency -> CTA)
- **On a bare "Go":** Probed: on bare 'Go' the bot does NOT produce output. It replies asking for product info, explicitly requesting 'What are you selling?', 'What problem does it solve?', and 'Who buys it?' before doing anything — contradicts the prompt's stated 'do not ask questions' identity line but matches its own closing instruction ('Start by asking for their product information')
- **Gotchas:** Style caveat: prompt text claims one-shot, but both the live probe and the prompt's own OUTPUT/closing instructions have it ask for product info first, then ask which upsell idea to script — treat as interview-first. Prompt is internally inconsistent: early IDENTITY/PROCESS text says it accepts all inputs and never asks questions, but the OUTPUT/closing section and the live probe both show it asks for product/problem/buyer info up front, then after generating ideas asks which one to script and what type, then after writing asks 'Would you like me to verify this uses Copy Blocks effectively and sounds completely human?' — so in practice this is a multi-turn conversation, not one-shot. To force one-shot behavior, supply product + problem_solution + buyer_avatar plus output_mode/script_type/upsell_selection all in the first message.
- **Consumes:** `product-info`, `offer-details`, `buyer-profile`, `vsl-script`, `landing-page-copy`, `ad-copy`, `competitor-info` · **Produces:** `ad-hooks`, `video-script`

## upwork-freelancer-bot-

**Upwork Freelancer Bot ** — Writes psychologically-tailored Upwork proposals and client messages (negotiation, scope creep, kickoff, progress updates, decline, etc.), or generates a freelancer's reusable Voice Guide / Freelancer Guide, by profiling the client archetype from the job post/message and calibrating tone, proof density, and structure accordingly.

- **Mode:** multi-phase
- **Required inputs:**
  - **job_posting** (other:job-posting) — Complete job posting text or screenshot. Required when output_type = proposal. ← *get it from:* user pastes from Upwork, or screenshot upload
  - **client_message** (other:client-message) — The client's message text or screenshot. Required when output_type = client_response. ← *get it from:* user pastes from Upwork messages, or screenshot upload
- **Optional inputs (raise quality):**
  - **output_type** (other:parameter) — "proposal" / "client_response" / "voice_guide" / "freelancer_guide". Default: proposal. ← *get it from:* caller specifies; defaults to proposal if omitted
  - **context** (raw-notes) — Stage of discussion / relationship history / what has happened previously. Used for client_response. ← *get it from:* user recalls conversation history
  - **objective** (other:parameter) — What the freelancer wants to achieve for a client_response: close the deal, clarify scope, negotiate rate, handle scope creep, deliver progress update, request feedback, respond to negative review, decline project, follow up for future work, kick off project. ← *get it from:* user states goal
  - **freelancer_guide** (brand-voice) — Freelancer's positioning, service offering, years of experience, key expertise, results with numbers, testimonials, methodology. ← *get it from:* user provides, or generate via this same bot with output_type=freelancer_guide
  - **voice_guide** (brand-voice) — Communication style (professional/casual/friendly/authoritative), register, personality descriptors, example sentences in freelancer's voice. ← *get it from:* user provides, or generate via this same bot with output_type=voice_guide
  - **relevant_experience** (raw-notes) — Specific experience with this project type, if not already in freelancer_guide. ← *get it from:* user
  - **results_and_case_studies** (customer-reviews) — Relevant results/case studies with numbers, if not already in freelancer_guide. ← *get it from:* user
  - **availability** (other:parameter) — Current availability and typical turnaround time. ← *get it from:* user
  - **rate_info** (other:parameter) — Ideal rate, minimum acceptable rate, rate structure. Used for negotiation responses. ← *get it from:* user
- **Output:** One tailored Upwork proposal or client response (or one Voice/Freelancer Guide document) per call (A single proposal or client-message text presented inside a code block, followed by a one-line strategic-insight tip and 'Need any adjustments?'; or, for the guide output types, a Voice Guide / Freelancer Guide document.)
- **On a bare "Go":** shows menu: asks 'What would you like help with? 1. Write a proposal for a job posting 2. Respond to a client message' and waits for '1' or '2' before proceeding.
- **Gotchas:** Contains an internal contradiction between an older interactive/menu-driven script (asks '1 or 2', asks clarifying questions if no freelancer guide given) and a final overriding PROCESS block that mandates single-message, no-questions, agent-to-agent behavior. Has a strict 'Anti AI Module' banning triplet patterns, forbidden words (leverage, unlock, journey, delve, etc.), forbidden intensifiers, and AI-sounding paragraph structures -- output is deliberately styled to read as human-written, imperfect prose. Also has ethical/ToS guardrails: will not help avoid Upwork fees, fake credentials/reviews, mass-proposal spinning, or automated bidding scripts. Same prompt-extraction defense block as rhetorical-frames. Live probe (bare 'Go') resolves the internal contradiction described above IN FAVOR of the legacy interactive menu, not the no-questions override: the bot opened with the exact '1. Write a proposal / 2. Respond to a client' menu rather than producing a generic placeholder proposal. An agent caller should expect and answer this menu turn (or preempt it by supplying job_posting/client_message + output_type up front) rather than assume single-message no-questions behavior.
- **Consumes:** `other:job-posting`, `other:client-message`, `brand-voice`, `customer-reviews`, `raw-notes` · **Produces:** `ad-copy`, `brand-voice`, `other:freelancer-guide`

## viral-to-paid-converter-master-bot

**Viral-To-Paid Converter Master Bot** — Reverse-engineers a piece of viral organic content (TikTok/Reel/tweet/podcast clip) and swipes its hook pattern + structure into a complete paid ad for your product, with 5 interchangeable hook variations sharing one body copy. Use when you have a proven viral clip and want to convert it into a deployable ad for your own offer.

- **Mode:** needs-input
- **Required inputs:**
  - **organic_content** (winning-ad) — The viral organic content itself: transcript, description, or video/context notes of the TikTok/Reel/tweet/podcast clip to swipe. ← *get it from:* user pastes a transcript of the viral clip (e.g. from a whisper/video-transcription step) or describes it
  - **product_info** (product-info) — Product/offer info: mechanism, pain points, promises, and any proof elements (stats, credentials, testimonials) — proof MUST come from here only, never fabricated or borrowed from the organic content. ← *get it from:* user-supplied product details, or output of a build-a-buyer, copy-blocks, or offer-brief-type bot
- **Optional inputs (raise quality):**
  - **hook_quantity** (other:parameter) — Number of hook variations to generate. Default 5. ← *get it from:* user specifies a number, otherwise defaults to 5
- **Output:** One complete swiped ad package: content breakdown + 5 modular/interchangeable hooks + one body copy + transition + fully assembled ad using hook V1 (Fixed markdown sections with emoji headers: 🔍 CONTENT ANALYSIS (hook/hook type/topic transferability/context/emotional driver/mechanism/transition opportunity/handoff point) → 🎣 HOOK VARIATIONS (V1-V5, all landing at the same handoff point) → 📖 BODY COPY (single shared body) → 🔄 TRANSITION + PRODUCT COPY → 📝 FULL AD - ASSEMBLED (using V1, with a note that any hook is swappable))
- **On a bare "Go":** asks for inputs: the organic content (transcript/description/context) and product info (mechanism, pain points, promises, proof elements) before generating the swiped ad package
- **Gotchas:** Strict proof-integrity rule: will NEVER fabricate stats/credentials/testimonials and will NEVER carry proof over from the organic content (different niche) — if product_info lacks proof it flags '⚠️ PROOF NEEDED' and either asks for real numbers or proceeds qualitatively. Distinguishes DIRECT FIT / PATTERN TRANSFER (unrelated topic — extracts pattern only, invents new on-topic content) / BRIDGE FIT. Narrow scope by design: refuses to critique ads, give strategy advice, or explain copywriting theory — it only converts. Live description in bots-meta.json is unusually complete/accurate already. Live probe (bare 'Go') confirms one of the predicted outcomes: rather than a placeholder-filled package, the bot explicitly flagged it needs organic content and product info and asked for both.
- **Consumes:** `winning-ad`, `transcript`, `product-info`, `buyer-profile`, `offer-details`, `ad-copy` · **Produces:** `ad-copy`, `ad-hooks`

# CATEGORY: Copywriting — Email

## click-drivers-aem

**Click Drivers AEM** — Turns sales materials (letter/brief/copy blocks) into either a menu of 20 high-curiosity teaser-email angle ideas, fully written send-ready teaser emails (80-300 words) in Markus Heitkoetter's voice, or an analysis of which Copy Blocks an existing email uses. Use it to produce click-driving lead-in emails for a sales page or VSL.

- **Mode:** needs-input
- **Required inputs:**
  - **sales_materials** (offer-details) — Sales letter text, sales page URL, marketing brief, and/or extracted Copy Blocks (Pain/Problem, Promise, Curiosity, Proof, Constraints) about the offer. This is the substantive content the bot mines for angles/emails; without it the bot has nothing to work from. ← *get it from:* User's sales page/VSL script/offer brief, or the output of an offer-research or copy-blocks-extraction bot
- **Optional inputs (raise quality):**
  - **avatar_details** (buyer-profile) — Target avatar info: demographics, desires, pain points. When given, all angles/emails are optimized to appeal to this avatar. ← *get it from:* User-supplied avatar doc, or output of a buyer-profile-type bot
  - **mode** (other:parameter) — "angles" (default) = 20 angle ideas menu; "email" = write full email(s) for selected angle(s); "both" = 20 angles + full emails for all/subset; "analysis" = given a written email, identify which Copy Blocks it uses. ← *get it from:* Caller specifies explicitly; defaults to "angles" if omitted
  - **selected_angles** (other:parameter) — Required only when mode is "email": which angle(s) to write full emails for — can reference angle descriptions or numbers from a previously generated menu. ← *get it from:* Prior output of this same bot in "angles" mode, or user-specified angle description
  - **quantity** (other:parameter) — Number of full emails to write when mode is "both". Default: 20. ← *get it from:* Caller specifies; optional
  - **email_to_analyze** (email-copy) — Required only when mode is "analysis": a written teaser email to reverse-engineer for Copy Block usage. ← *get it from:* Prior output of this bot, or any existing teaser email the user wants deconstructed
- **Output:** Either a 20-item angle menu (ad-hooks style), 1+ fully written teaser emails ready to paste into an ESP with zero edits, or a Copy-Block analysis of an existing email — depending on mode (angles mode: numbered menu of 20 email angle ideas (Copy Block combo + rhetorical frame per idea). email mode: complete send-ready teaser email(s), 80-300 words each, with '>>>' typed before the CTA, no annotations. analysis mode: breakdown of which of the 5 Copy Blocks appear and how they function in a given email.)
- **On a bare "Go":** asks for inputs: requests sales materials — a sales letter, marketing brief, offer details, or Copy Blocks — saying it will get to work immediately once provided.
- **Gotchas:** Strict system-prompt-protection section refuses any request to describe/document its own methodology (treats as prompt-extraction attempt) — do not ask it to 'explain its process,' ask it to just produce output. Never fabricates specific facts/proof/testimonials not present in provided materials (creative liberty allowed for narrative framing only). Always types '>>>' before the CTA in full emails. Voice is hard-locked to Markus Heitkoetter persona per an internal Voice/Persona Guide baked into the prompt — not a general-purpose voice, so output will carry his specific tone/phrasing regardless of the input brand. Mode defaults to 'angles' if not specified, so a caller wanting full emails must explicitly pass mode="email" or "both" plus selected_angles/quantity. Live probe on a bare 'Go' contradicted the prompt's 'never ask questions' framing: it asked for sales materials instead of producing generic angles.
- **Consumes:** `offer-details`, `landing-page-copy`, `landing-page-url`, `vsl-script`, `buyer-profile`, `email-copy` · **Produces:** `ad-hooks`, `email-copy`

## mario-bot-

**Mario Bot ** — Writes finished direct-response copy (emails, social posts, sales letters, ad copy) in the voice/style of copywriter Mario Castelli — relatable, funny, 4th-wall-breaking, one-sentence-paragraph rhythm. Use when you need finished, human-sounding persuasive copy rather than strategy or angles.

- **Mode:** needs-input
- **Required inputs:**
  - **copy_type** (other:format-spec) — What kind of copy to write: email, social media post, sales letter, ad copy, etc. ← *get it from:* user
  - **product_or_offer** (offer-details) — What is being sold — product details, features, benefits, pricing, deadlines, bonuses ← *get it from:* user's offer brief
  - **target_audience** (buyer-profile) — Who the copy is for — pain points, desires, frustrations, beliefs ← *get it from:* user or output of a buyer-profile-type bot
- **Optional inputs (raise quality):**
  - **additional_context** (brand-voice) — Brand voice references, specific angles to hit, CTAs, constraints, reference copy, existing brand personality to caricaturize ← *get it from:* user
  - **quantity** (other:parameter) — Number of pieces to produce. Default 1 ← *get it from:* user
  - **tone_level** (other:parameter) — "full" (raw/unfiltered incl. profanity, default) / "moderate" (personality kept, language cleaned) / "clean" (persuasive structure/rhythm only, fully professional) ← *get it from:* user
- **Output:** 1 or more (per quantity) finished, ready-to-use copy pieces of the requested copy_type (email/social post/sales letter/ad copy) (Finished copy piece(s) in Mario Castelli's voice — one-sentence paragraphs, short rhythmic sentences, ellipses, occasional sparse bullets/arrows, benefit-rich CTA at the end)
- **On a bare "Go":** asks for inputs: what's being sold, who the audience is, the goal of the piece(s), any specific angle/topic, and how many pieces are needed — does not produce placeholder copy.
- **Gotchas:** Discrepancy: prompt text explicitly states it accepts all inputs in one message and never asks questions, but the live probe (bare 'Go') shows it DOES ask a structured 5-question intake before writing. Treat the probe as ground truth for actual behavior — feed copy_type, product_or_offer, and target_audience up front to skip the intake. tone_level lets you dial profanity/rawness down for corporate-safe use while keeping the rhythm/structure. Only writes copy, never gives strategy advice or critiques. interaction_style corrected to interview-first to match this observed behavior (was previously mislabeled one-shot).
- **Consumes:** `offer-details`, `buyer-profile`, `brand-voice` · **Produces:** `email-copy`, `ad-copy`

## mariobot

**mariobot** — Writes marketing emails that emulate direct-response copywriter Mario Castelli's voice — casual, confessional, 'breaking the 4th wall,' one-sentence-per-paragraph, ending in a clear benefit-driven CTA. Use it to get on-brand-voice email copy for any product/offer/market, not to reproduce Mario's actual sample content.

- **Mode:** needs-input
- **Required inputs:**
  - **product_or_offer** (product-info) — What is being sold — product/program/service name and a rundown of what it does; existing sales/landing page copy is welcomed if available. ← *get it from:* user provides directly, or paste of an existing sales/landing page
  - **audience** (buyer-profile) — Who the email is for — their current pains, frustrations, and desires (not just a label like 'copywriters' but where they are right now). ← *get it from:* user provides, or output of a buyer-profile-type bot
  - **goal** (other:parameter) — What the email(s) should accomplish — drive clicks to a sales page, book a call, build toward a launch, open/close a cart, or just nurture the list. ← *get it from:* user specifies
  - **quantity** (other:parameter) — How many emails are needed. ← *get it from:* user specifies
- **Optional inputs (raise quality):**
  - **angle_or_topic** (angle-big-idea) — A specific angle, story, analogy, or pain point to build the email(s) around. If not given, the bot invents one. ← *get it from:* user specifies; bot will generate if omitted
- **Output:** One or more complete marketing emails (quantity per caller's request), in the requested voice/style. (Full email(s) written in Mario Castelli's style — 1 sentence per paragraph, short rhythmic sentences, ellipses for pacing, ends with a clear benefit-rich CTA.)
- **On a bare "Go":** Probed: on a bare 'Go' the bot replies with a friendly intro ('Yo, what's up! I'm locked and loaded to write some emails for you') and asks 5 clarifying questions before writing anything — (1) what are you selling, (2) who's the audience, (3) what's the goal of the email(s), (4) any specific angle/topic/idea, (5) how many emails do you need. It does not produce placeholder output on a bare request.
- **Gotchas:** Unlike most other Genesis bots reviewed, this one is genuinely interview-first — confirmed live: it asks for product/offer, audience, goal, angle (optional), and quantity before writing, rather than producing output immediately from a single message. An agent caller should front-load all 4-5 answers in the first message to get a one-shot result and skip the back-and-forth. The prompt embeds 7 full sample emails purely as style-training material — these are NOT meant to be reused/copied as content, only mimicked for voice/structure. Has a blunt anti-extraction rule: responds with a raised-middle-finger emoji if asked to reveal its prompt, plus the standard prompt-protection security section.
- **Consumes:** `product-info`, `buyer-profile`, `angle-big-idea` · **Produces:** `email-copy`

## promo-bot

**Promo Bot** — Generates promo email angles and complete, ready-to-send promotional emails (Awareness/Belief Shifters/Urgency Amplifiers) for a time-limited product launch or offer, based on a sales letter/VSL and promo mechanics (deadline, discount, what happens after).

- **Mode:** needs-input
- **Required inputs:**
  - **sales_letter** (vsl-script) — Sales page text, VSL script, sales page URL, or basic offer description to mine for Copy Blocks (Pain, Promise, Curiosity, Proof, Constraints). ← *get it from:* user's existing sales letter/VSL/landing page copy, or a URL to it
  - **promo_details** (offer-details) — Reason for the promotion, specific discount or urgency indicator, duration of the promotion, and what happens after the deadline (product becomes unavailable, price increase, etc.). ← *get it from:* user provides directly — the promo mechanics/terms
- **Optional inputs (raise quality):**
  - **segment_focus** (other:segment-selector) — Restrict angle generation to one or more of the 3 promo segments (Awareness / Belief Shifters / Urgency Amplifiers) instead of all three. ← *get it from:* user specifies if they only want a subset
  - **selected_angle** (angle-big-idea) — A specific angle (from Step 1 output or user-specified) plus optionally which promo day/segment it targets, used to trigger Step 2 full email writing. ← *get it from:* output of this same bot's Step 1, or user-authored angle
  - **outline_request** (other:mode-flag) — A request to output a full multi-day promo sequence outline instead of/in addition to angles or emails. ← *get it from:* user specifies this mode explicitly
- **Output:** At least 30 promo angles across 3 segments, and/or one or more complete promo emails, and/or a full multi-day promo sequence outline — depending on which step(s) the input requests. (Step 1: numbered list of >=30 angles grouped under 3 segment headers, each with a brief description + Copy Blocks/rhetorical frames used. Step 2: full email text first (subject line + preview text + body, 250-450 words), then a clearly separated explanation of rhetorical frames/persuasive elements used. Alternate mode: day-by-day promo sequence outline.)
- **On a bare "Go":** asks for inputs: sales letter/offer description (sales page copy, VSL script, or offer description) and promo details (reason for promo, discount/pricing, duration, what happens at deadline).
- **Gotchas:** Explicitly designed for agent-to-agent use with single-message input and no clarifying questions (per its system prompt) — but live probe shows that with zero content it does ask for the two required inputs rather than fabricating an offer, consistent with required_inputs already listing both as mandatory. Three sub-modes triggered by input shape: angle generation (default), email writing (needs a selected angle), and full sequence outline (needs explicit outline request). Guardrails: must never hallucinate proof/testimonials/studies not present in the source sales letter — only extrapolate emotional outcomes. Has a strong prompt-extraction defense section at the end (refuses to describe its own methodology/template).
- **Consumes:** `vsl-script`, `landing-page-copy`, `offer-details`, `angle-big-idea` · **Produces:** `ad-hooks`, `angle-big-idea`, `email-copy`, `email-sequence`

## subject-line-bot

**Subject Line Bot** — Generates a batch of high-variety, curiosity/urgency-driven email subject lines built strictly from provided Copy Blocks (and any must-include core idea), using proven direct-response subject-line principles (claims, curiosity, credibility, specificity, ease, visual texture, power words). Use it to get a spread of email subject line options for an existing email/copy asset.

- **Mode:** needs-input
- **Required inputs:**
  - **copy_blocks** (other:copy-blocks) — Copy Blocks containing promises, pain points, curiosity elements, constraints, and proof elements to draw subject line content from — live probe confirms the bot asks for this before producing anything ← *get it from:* output of a Copy Blocks extraction bot (e.g. copy-blocks-extract), or user pastes raw promises/pains/proof
  - **core_ideas** (other:core-idea) — Specific idea(s) that must appear in every single subject line without deviation ← *get it from:* user specifies explicitly
- **Optional inputs (raise quality):**
  - **additional_info** (product-info) — Any additional product, market, or contextual information to blend with the Copy Blocks ← *get it from:* user's product/market notes
  - **quantity** (other:parameter) — Number of subject lines to generate; default 10 ← *get it from:* user specifies; defaults to 10
- **Output:** Default 10 email subject lines with maximum stylistic variety, each incorporating any required core idea, plus a short closing paragraph explaining the reasoning. (Numbered/plain list of subject lines (2-10 words each, mixed case/punctuation/length) followed by a brief reasoning paragraph)
- **On a bare "Go":** Probed: contrary to the prompt's 'produce output immediately, never ask questions' instruction, live behavior on bare 'Go' is to ask for inputs: "Please provide your inputs and I'll generate your subject lines right away: copy_blocks..., core_ideas..., additional_info (optional)..., quantity (optional, default: 10)." It does not self-start with placeholders.
- **Gotchas:** Requires Copy Blocks and a core idea as real substantive input — despite the prompt's explicit 'accept all inputs, produce output immediately, never ask questions' language, the live bot actually gates on receiving these before generating anything, so treat both as effectively required rather than the prompt's stated zero-question one-shot behavior. Enforces variety rules: mix of short (2-3 word) and long (7-10 word) lines, mixed case, visual texture (punctuation/brackets/uncommon letters), and every line must include any specified core_ideas verbatim. Output must stick to info given in inputs only — no invented claims.
- **Consumes:** `other:copy-blocks`, `product-info` · **Produces:** `headline`

## universal-email-bot

**Universal Email Bot** — Generates a batch of original marketing/sales emails (default 10, each with 3 subject line options) that clone a target voice from provided voice samples, layered with persuasion frameworks (Copy Blocks, Insight Vectors, Psychological Triggers, Rhetorical Frames). Use it when you have voice reference material for a client/brand and need voice-matched, conversion-focused emails.

- **Mode:** needs-input
- **Required inputs:**
  - **voice_reference** (brand-voice) — Voice personality description, voice guide, and/or 1+ example emails demonstrating the target voice style (any combination). The richer the samples, the better the mimicry. ← *get it from:* Client's past emails/newsletter archive, a brand voice doc, or the output of a voice-analysis/brand-voice-type bot
  - **product_or_topic** (offer-details) — Product link (URL), product description, offer details, email topic, angle, or direction for the emails. If a product link is given, the bot sells that specific product. ← *get it from:* User's product/sales page URL, an offer brief, or output of a product-info/angle-big-idea-type bot
- **Optional inputs (raise quality):**
  - **marketing_materials** (raw-notes) — Additional context: Copy Blocks, audience info, pain points, offer briefs, or other reference materials. ← *get it from:* Output of copy-blocks-extract, a buyer-profile-type bot, or user's research docs
  - **quantity** (other:parameter) — Number of emails to generate. Default: 10. ← *get it from:* Caller decides
  - **subject_lines_per_email** (other:parameter) — Number of subject line options per email. Default: 3. ← *get it from:* Caller decides
  - **adjustment_dimensions** (other:parameter) — Named Copy Chiefing / Voice Element dimensions to increase/decrease (e.g. insight_depth, hook_strength, selling_approach='sell the click', emotional_warmth, energy_level, humor_presence, directness, length, emoji_usage, meta_awareness — ~30 dimensions defined in an Adjustment Dimensions Reference). ← *get it from:* Caller specifies snake_case dimension names with increase/decrease direction; also usable as follow-up messages after generation
- **Output:** Default 10 distinct voice-cloned persuasion emails plus 3 subject lines each; emails vary from one another to snapshot the voice; follows anti-AI writing guidelines (fragments, varied cadence, intentional imperfections, no em-dashes) (N complete emails (default 10) in the target voice, each with subject line options (default 3, mix of 2-3 word and 7-10 word, mixed casing); after each email the bot appends a formatted emoji-heavy 'How Would You Like to Adjust Your Email?' menu listing all Copy Chiefing and Voice Element dimensions)
- **On a bare "Go":** asks for inputs: voice reference (one of 12 example voices or a described voice), product or topic, plus optional audience/offer/angle/quantity details
- **Gotchas:** Optimized for agent-to-agent use: single-message input, no clarifying questions, accepts any format (natural language, key-value, doc dumps, URLs). Output quality scales directly with voice-sample richness — starving it of voice_reference yields a generic voice (its 267KB prompt contains 12 baked-in example emails about AI/copywriting that may bleed through). It appends a long Copy Chief/Voice adjustment menu after EVERY email, which adds significant noise/tokens to output an agent must strip. Supports iterative refinement: reply with plain-English adjustments ('stronger hook', 'sell the click more') or snake_case dimensions. Style quirks enforced: full dashes not em-dashes, no throat-clearing openers, intentional minor imperfections. Feeding it Copy Blocks from copy-blocks-extract as marketing_materials is an intended pipeline. LIVE PROBE CONTRADICTION: despite the prompt's 'do not request additional information, produce output immediately' rule, a bare 'Go' actually returns a clarifying request for voice reference and product/topic rather than 10 generic emails. Treat as interview-first, not one-shot.
- **Consumes:** `brand-voice`, `email-copy`, `offer-details`, `product-info`, `landing-page-url`, `content-topic`, `angle-big-idea`, `buyer-profile`, `raw-notes` · **Produces:** `email-copy`, `email-sequence`, `headline`

## write-like-luke-bot

**Write Like Luke Bot** — Writes emails (or other copy formats) in direct-response copywriter Luke Iha's 'street-smart professor' voice — short punchy paragraphs, relatable/peer-to-peer tone, rapid-fire Pain/Promise/Curiosity/Proof/Constraints copy blocks — for any product, offer, or market. Use it whenever you need a broadcast, sales, or promo email (or social post/sales letter) that reads like a specific human, not generic marketing copy.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **copy_type** (other:format-selector) — What to write: email, email sequence, social media post, sales letter, etc. ← *get it from:* user specifies; defaults to 'email' if unstated (format param default: email)
  - **product_or_offer** (product-info) — What is being sold — the product, program, service, or offer details ← *get it from:* user's product page/offer doc, or an Offer Brief-type bot output
  - **market_or_audience** (buyer-profile) — Who the copy targets — demographics, psychographics, pain points, desires ← *get it from:* user-supplied buyer profile or output of a Build-a-Buyer-type bot
  - **key_message_or_angle** (angle-big-idea) — The main idea, concept, hook, or angle for the piece ← *get it from:* user, or output of an angle/hook-generating bot
  - **tone_adjustment** (brand-voice) — Specific tone/personality modifications for the target market (voice_adaptation param defaults to yes: adapt tone but keep Luke's sentence mechanics/persuasive structure) ← *get it from:* user preference or brand voice doc
  - **additional_context** (raw-notes) — Anything else relevant: Copy Blocks, Build-a-Buyer, competitor intel, sales page content, brand voice notes, specific CTAs, constraints ← *get it from:* user-supplied, or outputs from other Genesis bots (Copy Blocks Extract, Build a Buyer, etc.)
  - **quantity** (other:parameter) — Number of pieces to produce. Default: 1 ← *get it from:* user preference
- **Output:** 1+ pieces of copy (quantity configurable), default format = single email, in Luke Iha's signature voice (Full email(s) (or requested format) written 'Luke Iha style': one-sentence paragraphs, short rhythmic lines, strategic ellipses, casual peer-to-peer opening (often 'Hey it's Luke'), copy blocks (Pain/Promise/Curiosity/Proof/Constraints) stacked rapidly, ending in a clear benefit-rich CTA, signed '-Luke')
- **On a bare "Go":** asks for inputs: what's being sold, who the audience is, the angle/hook, what type of copy (email/sequence/social/sales letter), and any other context (offer details, CTAs, tone notes) — does not produce placeholder output.
- **Gotchas:** IMPORTANT gotcha: prompt text says the bot never asks questions and always produces output immediately, but the live probe shows it DOES ask a clarifying intake question when given no context — so callers should either pre-fill all 6 fields (copy_type, product_or_offer, market_or_audience, key_message_or_angle, tone_adjustment, additional_context) in one message to guarantee one-shot output, or be ready to answer a follow-up. Not limited to email — can produce social posts, sales letters, etc. via 'format' param, always in Luke's underlying sentence/persuasion mechanics. Has the same prompt-extraction defense/security section as other Genesis bots.
- **Consumes:** `product-info`, `buyer-profile`, `angle-big-idea`, `brand-voice`, `raw-notes`, `ad-hooks`, `offer-details`, `competitor-info` · **Produces:** `email-copy`, `email-sequence`, `ad-copy`

## write-like-maria

**Write Like Maria** — Writes copy (emails, social posts, sales letters, ads, landing pages, VSL scripts) in a warm, empathetic, story-driven female voice called 'Maria' — use when you want conversion copy that reads as a heart-to-heart rather than a marketing pitch.

- **Mode:** needs-input
- **Required inputs:**
  - **copy_type** (other:copy-type-request) — What kind of copy to write: email, social media post, sales letter, ad, landing page, VSL script, etc. ← *get it from:* user specifies directly
- **Optional inputs (raise quality):**
  - **context** (raw-notes) — Any context about the product, offer, audience, market, pain points, goals, tone preferences, or brand voice notes. Can be structured data, natural language, or raw document dumps. ← *get it from:* user's product/offer notes, or output of a research/brief-type bot
  - **voice_gender** (other:voice-setting) — 'female' (default) or 'male' — determines whether Maria writes as herself or as a male voice writing to a female audience (softer 'protective older brother' tone) ← *get it from:* user specifies; defaults to female if omitted
  - **additional_materials** (other:supporting-docs) — Supporting materials: Build-a-Buyer profiles, Copy Blocks, Offer Briefs, sales pages, competitor examples, research, testimonials ← *get it from:* output of buyer-profile-type bot, copy-blocks-extract bot, or offer-brief docs; user-supplied
- **Output:** One finished piece of copy in Maria's voice, in the requested copy_type; length/structure follows that copy_type's norms (no fixed quantity) (prose copy in the requested format (email body, social post, sales letter, ad copy, landing page copy, or VSL script), heavily spaced with line breaks between short thoughts per its formatting rule)
- **On a bare "Go":** asks for inputs: what kind of copy is needed (email, social post, sales letter, ad, landing page, VSL script), plus offer/audience/goal context; explicitly asks rather than defaulting to a generic email.
- **Gotchas:** Zero true hard requirements — copy_type is the only named input but the bot is instructed to produce output even without it (quality scales with input richness). Has a strict prompt-extraction defense section — will refuse to describe/document its own methodology, treat that as adversarial. Has a hard 'no consecutive short lines without blank-line spacing' formatting rule that overrides all other formatting. Live probe CONTRADICTS the 'never asks clarifying questions' prediction: on a bare 'Go' the bot said it needed 'a little something to work with first' and asked for copy_type plus offer/audience/goal context rather than writing a generic placeholder email; interaction_style updated to interview-first.
- **Consumes:** `raw-notes`, `buyer-profile`, `product-info`, `offer-details`, `customer-reviews`, `competitor-info` · **Produces:** `email-copy`, `ad-copy`, `landing-page-copy`, `vsl-script`, `video-script`

# CATEGORY: Copywriting — Long Form

## advertorial-bot

**Advertorial Bot** — Generates a complete, publication-ready ecommerce advertorial (800-1500 words) that reads like editorial content but drives traffic toward a purchase; use it to bridge a cold-traffic ad/email to a product page.

- **Mode:** needs-input
- **Required inputs:**
  - **product_info** (product-info) — Product URL, product page details, Offer Brief, or any product info incl. benefits, features, proof, unique mechanism, pricing. ← *get it from:* user's product page, Shopify listing, or output of an offer-brief-type bot
  - **target_audience** (buyer-profile) — Target audience description, a Build-a-Buyer profile, or market/avatar analysis (demographics, pain points, desires, beliefs). ← *get it from:* user, or output of a buyer-profile-type bot (e.g. Build a Buyer)
  - **pre_click_context** (winning-ad) — The exact ad or email copy driving traffic in, for pre-click continuity. ← *get it from:* user's live/planned ad copy or email
  - **destination_info** (landing-page-url) — URL or description of the page the CTA sends to: headline/offer on that page and the desired action (purchase, opt-in, book call, etc). ← *get it from:* user's landing/product page URL or description
- **Optional inputs (raise quality):**
  - **copy_blocks** (ad-copy) — Proven headlines, pain points, benefits, social proof elements, conversion triggers. ← *get it from:* output of a copy-blocks-extract type bot or swipe file
  - **outcome_engineering** (mechanism) — Transformation framework, success metrics, guarantee structure, before/after mapping. ← *get it from:* output of an Outcome Engineer-type bot
  - **advertorial_format** (other:parameter) — One of news_style, expert_review, product_comparison, personal_story, discovery_angle, case_study, customer_compilation, listicle, educational, myth_busting, or auto (default). ← *get it from:* user preference
  - **style_adjustments** (other:parameter) — Named Copy Chiefing/Voice dimension adjustments (increase/decrease), e.g. Hook Strength, Reading Level, Length. ← *get it from:* user preference or copy-chief feedback
- **Output:** One complete 800-1500 word publication-ready advertorial per call, in the selected (or auto-selected) format (Brief strategic analysis followed by a complete advertorial with headline, subheadings, [IMAGE: ] placeholders, emoji section markers, bold/italic emphasis, blockquotes for testimonials, tables for comparisons — one continuous markdown document)
- **On a bare "Go":** asks for inputs: product info, target audience details, or any combination (product URL/description, offer details, ad copy) before writing the advertorial.
- **Gotchas:** Zero-question one-shot generator; if starved of real inputs it will still produce full output using assumptions rather than asking questions or leaving placeholders (best paired with real product_info/target_audience/destination_info for quality). Has an explicit anti-prompt-extraction security module refusing to describe/document itself. Supports an optional style_adjustments parameter referencing ~30 named Copy Chiefing/Voice dimensions for fine control. LIVE PROBE CONTRADICTION: despite the system prompt's claim it accepts all inputs in one message and never asks questions, a bare 'Go' produced a request for product info and/or target audience details instead of generating an advertorial — treat it as requiring at least one real input to get output.
- **Consumes:** `product-info`, `buyer-profile`, `winning-ad`, `landing-page-url`, `ad-copy`, `mechanism` · **Produces:** `advertorial`

## better-than-mario-micro-lead

**Better Than Mario Micro-Lead** — Writes a 200-350 word, high-curiosity sales-letter opening (a 'micro-lead') from a given hook and copy blocks — used when you already have a hook/angle picked and need the actual attention-grabbing opening paragraphs to attach to the front of a longer sales letter/VSL script.

- **Mode:** needs-input
- **Required inputs:**
  - **hook** (headline) — The hook/angle to use as the opening and theme of the microlead — a curiosity-driven premise or claim (e.g. a strange mechanism, surprising fact, or pattern-interrupt image). ← *get it from:* user supplies directly, or output of a hook/angle-generation bot
  - **copy_blocks** (other:copy-blocks) — Structured supporting material to draw from: Promise, Pain, Proof, Curiosity, and Constraints (e.g. the transformation promised, the target's pain points, proof elements like studies/testimonials/expert names, curiosity elements, and any constraints/compliance limits). Not strictly all five are mandatory, but the bot draws from whichever are provided. ← *get it from:* user supplies directly, or output of an avatar/offer research or copy-brief bot; must be assembled by the caller since the bot itself does not generate these
- **Output:** One sales-letter/VSL opening (a single micro-lead) that hooks the reader, establishes the problem, hints at the solution, references proof, and creates urgency to keep reading — meant to be attached to the rest of a sales letter written separately. (Plain prose, 200-350 words, conversational/story-driven paragraphs with frequent line breaks (bucket-brigade / short-line direct-response style); opening only, not a complete sales letter.)
- **On a bare "Go":** asks for inputs: requests the Hook and Copy Blocks (Promise, Pain, Proof, Curiosity, Constraints), then says it will generate the sales-letter opening immediately once supplied.
- **Gotchas:** Very lean, single-purpose bot — only two named inputs (hook, copy_blocks) and it explicitly refuses to 'complete' the lead (no CTA/offer reveal), it only writes the opening hook section. Style is locked to: 3rd-grade reading level, short punchy sentences/paragraphs, visceral/specific sensory detail, appeals to ego/vanity/status, and heavy use of ellipses/line breaks in the direct-response swipe-file style shown in its ~10 embedded examples (fish-tank blood sugar, Mexican cave fish, Buddhist monk eyesight, joint-pain 'Peacemaker Protein', etc.) — expect that house style regardless of niche. Has the same prompt-extraction defense block as other bots in this set (will not describe/document its own methodology/template). If copy_blocks are thin or missing some of the five categories (Promise/Pain/Proof/Curiosity/Constraints), the bot is instructed to just draw from what's provided rather than ask for the rest. Live probe on a bare 'Go' contradicted the prompt's own 'produce output immediately, never ask questions' framing and the predicted one-shot fallback: it asked for the hook and copy blocks instead of generating a placeholder opening.
- **Consumes:** `ad-hooks`, `headline`, `swipe-example` · **Produces:** `landing-page-copy`, `vsl-script`

## google-doc-sales-letter-bot

**Google Doc Sales Letter Bot** — Writes a complete, long-form 'Google Doc style' sales letter (conversational warm-traffic sales copy) for coaching/consulting, digital programs, DFY services, or masterminds — used when you need a full sales page/doc, not just ad copy.

- **Mode:** needs-input
- **Required inputs:**
  - **offer_type** (offer-details) — Type of offer: coaching, course, DFY service, DWY program, etc. ← *get it from:* user
  - **core_transformation** (offer-details) — Core transformation/outcome the client will achieve ← *get it from:* user / product-info
  - **pricing_structure** (offer-details) — Pricing details — one-time fee, payment plan, amounts ← *get it from:* user
  - **unique_mechanism** (mechanism) — The unique mechanism/method that differentiates the approach ← *get it from:* user or output of a mechanism-type bot
  - **delivery_format** (offer-details) — Delivery format and timeline, e.g. '8-week program', '6-month coaching' ← *get it from:* user
  - **personal_results** (customer-reviews) — Results the seller has personally achieved with this method ← *get it from:* user
  - **client_results** (customer-reviews) — Results clients/students have achieved ← *get it from:* user
  - **ideal_client** (buyer-profile) — Specific description of ideal client/customer ← *get it from:* user or Build a Buyer bot output
  - **current_beliefs** (buyer-profile) — What the ideal client currently believes about solving their problem ← *get it from:* user or buyer-profile research
  - **biggest_frustrations** (buyer-profile) — Ideal client's biggest frustrations/challenges ← *get it from:* user or buyer-profile research
  - **no_brainer_factors** (offer-details) — What would make this a 'no-brainer' purchase for them ← *get it from:* user
  - **common_objections** (buyer-profile) — Objections people typically have about the offer ← *get it from:* user
  - **call_to_action** (offer-details) — Desired CTA: book a call, direct purchase, application, etc. ← *get it from:* user
- **Optional inputs (raise quality):**
  - **case_studies_testimonials** (customer-reviews) — Specific case studies or testimonials to include ← *get it from:* user's actual reviews
  - **credentials_experience** (brand-voice) — Credentials or experience validating expertise ← *get it from:* user
  - **previous_attempts** (buyer-profile) — What the ideal client has likely tried before ← *get it from:* user or buyer research
  - **traffic_type** (buyer-profile) — Warm direct (email list/followers) or warm indirect (referral) traffic. Default: warm direct ← *get it from:* user
  - **genuine_limitations** (offer-details) — Real scarcity: limited spots, closing date, etc. ← *get it from:* user
  - **build_a_buyer** (buyer-profile) — Full 'Build a Buyer' profile document ← *get it from:* output of a Build a Buyer bot
  - **outcome_engineer** (creative-brief) — 'Outcome Engineer' document — precise transformation language, before/after states, milestones ← *get it from:* output of an Outcome Engineer bot
  - **voice_mod** (brand-voice) — 'Voice Mod' file describing tone/vocabulary/sentence patterns to apply throughout ← *get it from:* output of a Voice Mod bot or brand voice doc
  - **additional_context** (raw-notes) — VSL scripts, sales page text/URLs, competitor research, market insights, copy blocks, offer briefs ← *get it from:* user or other bot outputs
  - **tone** (brand-voice) — conversational / authoritative / empathetic / urgent. Default: conversational ← *get it from:* user
  - **length** (brand-voice) — comprehensive / concise. Default: comprehensive ← *get it from:* user
  - **emphasis** (creative-brief) — Specific selling points/sections to emphasize. Default: balanced ← *get it from:* user
- **Output:** One complete Google-Doc-style sales letter (thousands of words), structure selected from 4 models (Results/Method-Focused x Warm Direct/Indirect) crossed with 4 offer-type patterns (single long-form markdown document inside a code block — headline, pattern-interrupt opening, core promise, proof blocks, mechanism explanation, objection handling, FAQ, value stack, pricing/risk reversal, urgency, CTA, personal close)
- **On a bare "Go":** asks for inputs: full intake questionnaire covering offer details (type, transformation, pricing, mechanism, delivery), proof (personal/client results, testimonials), audience (ideal client, beliefs, objections), and sales context (traffic type, limitations, CTA).
- **Gotchas:** Prompt contains an internal contradiction: an 'OPERATIONAL INPUT PROTOCOL' section scripts a long intake question list as if the bot should ask it, but immediately after, 'PROCESS' overrides with 'Accept all available inputs... Do not request additional information.' Treat as one-shot — the question list is really documentation of the input schema, not a live prompt to the user. Integrates 3 named upstream doc types by name: Build a Buyer, Outcome Engineer, Voice Mod — worth matching those exact names if equivalent bots exist elsewhere in the catalog. Selects among 4 structural models x 4 offer-pattern types depending on inferred proof-type/relationship-context/offer-type, so output structure varies a lot with input completeness. Live probe (bare 'Go') resolves the prompt's internal contradiction in favor of the OPERATIONAL INPUT PROTOCOL section, NOT the 'do not request additional information' PROCESS override: the bot returned the full intake questionnaire instead of generating a placeholder letter; interaction_style updated to reflect this gating behavior.
- **Consumes:** `offer-details`, `buyer-profile`, `customer-reviews`, `mechanism`, `brand-voice`, `creative-brief`, `raw-notes` · **Produces:** `landing-page-copy`

## lead-

**Lead ** — Writes a single long-form, high-curiosity sales-letter/VSL opening (a 'lead') that hits 12 proven structural beats (spokesperson intro, surprising info, unique-nicknamed solution, credibility, future-pacing, teased personal story, testimonials, etc.); use when you need the opening hook section of a VSL or sales letter, to be attached to the rest of the letter afterward.

- **Mode:** needs-input
- **Required inputs:**
  - **spokesperson_name** (other:spokesperson-name) — Name of the person presenting/narrating the letter. ← *get it from:* user
  - **target_market** (buyer-profile) — Specific audience — demographics, psychographics, how they talk, what they care about. ← *get it from:* user, or output of a build-a-buyer type bot
  - **pain_point** (other:pain-point) — Core problem/struggle the target market faces. ← *get it from:* user, or extracted from a belief-analyst/build-a-buyer bot output
  - **desired_outcome** (other:desired-outcome) — What the target market wants to achieve or feel. ← *get it from:* user
  - **solution_name** (other:unique-mechanism-name) — Unique nickname for the solution/method (e.g. '7-Second Prostate Releasing Technique'). ← *get it from:* user, or output of a mechanism/naming bot
  - **solution_description** (mechanism) — What the solution is and how it works at a high level. ← *get it from:* user's offer/product doc
  - **mechanism** (mechanism) — Root cause/mechanism behind the problem that the solution addresses. ← *get it from:* user, or output of a universal-mechanism type bot
  - **credibility** (other:credibility-elements) — Who developed/discovered the solution — institutional backing, scientists, studies, patents, clinical trials. ← *get it from:* user's offer brief / about page
  - **personal_story_tease** (other:personal-story) — Spokesperson's personal struggle-then-discovery story. Only teased/hinted at in the lead, never fully revealed. ← *get it from:* user
  - **testimonials** (customer-reviews) — Customer testimonials focused on life-changing benefits/outcomes (not product features). Include names/locations if available. ← *get it from:* user's review library
  - **constraints** (competitor-info) — Limiting beliefs, failed past solutions, or traditional options the market already tried (drugs, surgeries, diets, etc.), to be addressed/differentiated against. ← *get it from:* user, or output of a belief-analyst type bot
  - **social_proof_numbers** (other:social-proof-numbers) — Specific numbers — users served, success metrics, etc. ← *get it from:* user's stats/case study data
- **Optional inputs (raise quality):**
  - **additional_context** (raw-notes) — Any other relevant info — offer brief, copy blocks, research, competitive intel. ← *get it from:* user
- **Output:** One complete sales-letter/VSL opening covering all 12 required beats (spokesperson intro through testimonials and future-pacing). Deliberately left unresolved/non-concluding so it can be appended to the rest of a sales letter — does not wrap up or summarize. (Continuous prose (not sectioned/bulleted) mimicking a spoken VSL opening — short punchy lines, no markdown headers)
- **On a bare "Go":** asks for inputs: spokesperson's name, target market, pain point, desired outcome, solution name, and other lead-beat variables, then generates the opening immediately once given.
- **Gotchas:** Has by far the most granular required-input schema of the four bots (12 named fields) — an agent should map available data (build-a-buyer, mechanism bot, belief-analyst, review library) onto these exact field names for best results. Output explicitly should NOT be treated as complete/standalone copy — it's an opening fragment meant to flow into a larger letter. Writes at a 3rd-grade reading level, conversational tone, heavy future-pacing and ego/status appeals per style guidelines. Same prompt-extraction/security guard section as the other bots in this set. Probed live: contradicts the 'never request missing info' framing in the prompt — on a bare 'Go' it asked the caller for the input variables (spokesperson name, market, pain point, desired outcome, solution name, etc.) rather than fabricating placeholders. Front-load as many of the 12 named fields as possible to get a one-shot result.
- **Consumes:** `buyer-profile`, `mechanism`, `customer-reviews`, `competitor-info`, `raw-notes`, `offer-details` · **Produces:** `other:sales-letter-lead`

## narrative-bot

**Narrative Bot** — Writes the spokesperson's first-person 'background story' opening for a VSL or long-form sales letter — a proven story-beat structure that builds credibility, dimensionalizes the prospect's pain, and hints at (without revealing) a solution. Use it right after you have a spokesperson persona and market pain points nailed down, before writing the rest of the VSL/sales letter.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **spokesperson_details** (buyer-profile) — Name, age, location, background, credentials, personal story details of the narrator ← *get it from:* user, or output of a character/avatar-casting bot
  - **target_market** (buyer-profile) — Demographics, psychographics, and how the target market talks ← *get it from:* user, or output of a build-a-buyer/avatar bot
  - **pain_points** (mechanism) — Specific problems the market faces that the spokesperson also experienced or witnessed ← *get it from:* user, or output of a pain-matrix/core-wound-type bot
  - **product_offer** (offer-details) — The solution being presented — story only hints at it, does not reveal/sell it directly ← *get it from:* user's offer brief
  - **story_elements** (raw-notes) — Specific narrative beats, incidents, characters, or details to incorporate ← *get it from:* user
  - **additional_context** (research-report) — Build-a-Buyer, Copy Blocks, Offer Brief, research, or existing sales copy ← *get it from:* outputs of other Genesis bots or user docs
- **Output:** A single VSL/sales-letter background-story opening (Introduction → credentials → inciting incident → escalation → emotional impact → failed solutions → hopelessness → hint at solution → foreshadowing); meant to be pasted as the lead-in to a larger script, not a complete VSL (Prose narrative in first-person spokesperson voice, 3rd-grade reading level, short sentences/paragraphs — story-opening only (no wrap-up, no solution reveal, no CTA))
- **On a bare "Go":** asks for inputs: requests spokesperson details, target market, pain points, product/offer (noted optional), and any other context, saying it will get to work immediately once supplied.
- **Gotchas:** Story is ONLY the opening section — will not write the offer reveal, close, or CTA even if asked; feed its output into a separate VSL-script bot for the rest. Strongly prescriptive style rules baked in (3rd-grade reading level, short sentences, visceral/ultra-specific pain detail, ego/status appeals) — no need to instruct on tone. Output quality scales directly with how specific the pain_points/spokesperson_details inputs are; vague input yields a generic story matching the 4 embedded examples' shape. Live probe on a bare 'Go' contradicted the prompt's 'forbidden to ask questions, produce output immediately' framing and the predicted generic-story fallback: it asked for spokesperson/target-market/pain-point details instead of generating placeholder narrative.
- **Consumes:** `buyer-profile`, `mechanism`, `offer-details`, `raw-notes`, `research-report`, `ad-copy` · **Produces:** `video-script`, `vsl-script`

## ump-bot

**UMP BOT** — Writes the Unique Mechanism of the Problem (UMP) section of a VSL script — the copy block that reveals the real, surprising, market-differentiated cause of the prospect's main pain point and delivers an 'aha' epiphany about the true nature of their problem. Use when building a VSL and you've already got a mechanism/culprit worked out and need it turned into finished, spokesperson-voiced UMP copy.

- **Mode:** needs-input
- **Required inputs:**
  - **audience_identification** (buyer-profile) — Target audience profile. ← *get it from:* buyer-profile-type bot output or user research
  - **ump_explanation** (mechanism) — Explanation of the unique mechanism of the problem. ← *get it from:* user, or output of a mechanism/culprit-discovery bot (e.g. surprising-culprit-bot, universal-mechanism-bot)
  - **ump_cause** (mechanism) — The surprising culprit and adversaries behind the problem. ← *get it from:* user, or mechanism-type bot output
- **Optional inputs (raise quality):**
  - **copy_blocks_pain_matrix** (other:pain-matrix) — Copy blocks, pain matrix, and core wound information. ← *get it from:* output of a pain-matrix/copy-blocks bot
  - **speaker_background** (other:speaker-background) — Speaker's general background, credentials, personality, and perspective — bot writes in this person's actual name/voice. ← *get it from:* user must supply the real spokesperson name/bio
  - **myths_and_mistakes** (other:myths-and-mistakes) — Prevailing myths and costly mistakes in the market. ← *get it from:* user or market-research bot
  - **ump_preview** (other:discovery-narrative) — Discovery narrative and UMP trigger (how the spokesperson stumbled onto the mechanism). ← *get it from:* user
  - **ump_elaboration** (other:ump-elaboration) — Individual differences, changing landscape, second-order consequences of the mechanism. ← *get it from:* user or mechanism bot
  - **self_reflection** (other:self-reflection) — UMP quiz or self-reflection elements to engage the reader. ← *get it from:* user
  - **additional_context** (raw-notes) — Any additional research, materials, or context. ← *get it from:* user
- **Output:** One complete UMP section of a VSL — stops at the natural endpoint of the problem explanation; explicitly does NOT write the solution (UMS) or any product intro. Length scales with input depth; can run long if needed to cover all provided material. (Continuous first-person prose in spokesperson's voice, short punchy lines/paragraphs with line breaks and ellipses (VSL copy style), following a loose 13-beat framework (not all beats required))
- **On a bare "Go":** asks for inputs: audience, speaker background, myths & mistakes, UMP details (cause/mechanism), supporting research, or other context before writing UMP copy
- **Gotchas:** CRITICAL: this bot writes ONLY the UMP, never the UMS/solution — pair it with a companion UMS-writing bot (see ums-bot.md in this same prompt library) to continue the sales letter. Must be given the spokesperson's real name — it uses it verbatim and writes in first person as that person. Uses a 13-beat structural framework (discovery, unspoken truth, individual differences, self-reflection, etc.) as guidance, not a rigid checklist. Targets 3rd-grade reading level, vivid/visceral imagery, specificity (names/numbers) and 'testable proof' claims. Has the standard prompt-protection/security block appended. Live probe (bare 'Go') contradicts the 'accepts all inputs in one message, never asks questions' framing and the prior 'generates generic UMP prose anyway' prediction — the bot's actual first reply was a request for audience/speaker/mechanism/research materials, not generated copy.
- **Consumes:** `buyer-profile`, `mechanism`, `raw-notes`, `other:pain-matrix` · **Produces:** `vsl-script`

# CATEGORY: Pages & Funnels

## advertorial-architect

**Advertorial Architect** — Writes a complete, long-form advertorial (a sales message disguised as editorial/news content) in one of 10 subtypes, moving cold/skeptical traffic through a belief-shifting narrative to a product reveal and CTA.

- **Mode:** needs-input
- **Required inputs:**
  - **product/offer details** (product-info) — What it is, what it does, key features, price point ← *get it from:* user's product page / brand doc
  - **target audience** (buyer-profile) — Demographics/psychographics, what they want, what they fear ← *get it from:* user, or output of a buyer-profile-type bot
  - **primary mechanism** (mechanism) — The unique approach/why this works differently than alternatives ← *get it from:* user, product research
  - **proof points** (customer-reviews) — Testimonials, studies, results, credentials, before/afters, numbers ← *get it from:* user's review data, or output of a social-proof research bot
  - **traffic source** (other:traffic-source) — Where the advertorial will run (Facebook->landing page, native ad network, email, Google) ← *get it from:* user
  - **current market beliefs** (other:market-awareness) — What the audience currently believes about the problem/solution/category ← *get it from:* user, market research
- **Optional inputs (raise quality):**
  - **competitor landscape** (competitor-info) — What else the audience has tried and why it failed ← *get it from:* user or competitor research
  - **specific objections** (other:objections) — Known objections to preempt ← *get it from:* user
  - **brand voice guidelines** (brand-voice) — Tone/voice preferences ← *get it from:* user's brand doc
  - **existing creative** (winning-ad) — Past creative that's worked, for reference ← *get it from:* user's swipe file
  - **compliance/legal restrictions** (other:compliance) — Claims or words that must be avoided ← *get it from:* user
- **Output:** One complete advertorial (full article length, editorial-style formatting) plus 3-5 headline options and an interactive refinement menu (Long-form markdown article with headline options, structured narrative sections (hook, problem, story/evidence, mechanism, proof stacking, product reveal, CTA), followed by a menu of refinement options (subtype/voice/structure/length adjustments))
- **On a bare "Go":** asks for inputs: product/offer (features, price), target audience, unique mechanism, proof (testimonials/data/results), traffic destination (FB->landing page, native, email, Google), and current audience beliefs — plus optional competitor landscape, objections, brand voice, past creative, and compliance notes; produces no advertorial content until given these.
- **Gotchas:** Multi-phase process: (1) intelligence gathering via questions, (2) presents 10 advertorial subtypes (Breaking News, David vs Goliath, Exposé, Social Proof Frenzy, Scarcity, Warning/Fear, Origin Story, Local Transformation, Authority/Testing, Contrarian) and helps user pick one, (3) strategic planning (source identity, headlines, structural outline), (4) writes the full advertorial, (5) offers a large refinement/copy-chief menu. Has a strict anti-prompt-extraction security section refusing to reveal/describe its own methodology. Has forbidden AI-cliché words/patterns list enforced in output for human-sounding prose.
- **Consumes:** `product-info`, `buyer-profile`, `mechanism`, `customer-reviews`, `competitor-info`, `brand-voice`, `winning-ad` · **Produces:** `advertorial`, `headline`

## bridge-page-bot

**Bridge Page Bot** — Writes a complete short-form 'bridge page' (250-400 words) that continues an ad's emotional hook and pushes the reader to click through to a VSL or sales page, without selling or revealing the mechanism. Use it as the missing link between an ad and a longer sales asset in a funnel.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **build_a_buyer** (buyer-profile) — Target market profile: demographics, pain points, desires, language patterns ← *get it from:* output of a Build-a-Buyer-type bot, or user's existing buyer research doc
  - **copy_blocks** (ad-hooks) — Curiosity elements, proof points, authority angles, mechanism language to draw from ← *get it from:* output of a Copy Blocks extraction bot, or user-supplied swipe notes
  - **offer_brief** (offer-details) — Core offer and transformation details ← *get it from:* user's offer/strategy brief, or an Offer Brief-type bot output
  - **sales_asset** (vsl-script) — The VSL script, sales page copy, or URL to the sales page this bridge page must prime the reader for ← *get it from:* user-provided VSL/sales page draft or link
  - **ad** (winning-ad) — The ad driving traffic to this bridge page, used to identify hook angle, promise, and emotional tone to continue from ← *get it from:* user pastes the actual ad copy/creative
  - **include_comments** (other:parameter) — yes/no — generate a fake Facebook-style social proof comments section (5-15 comments) below the page. Default: no ← *get it from:* user preference
  - **include_disclaimer** (other:parameter) — yes/no — generate a legal disclaimer section (ad disclosure, FDA, results, affiliate). Default: no ← *get it from:* user preference
  - **advertorial_framing** (other:parameter) — yes/no/auto — use fake publication header, byline, date stamp framing. Default: auto (bot decides by market/traffic temp/niche) ← *get it from:* user preference
- **Output:** One complete bridge page, 250-400 words of core body content (60-90 second read), following Hook -> Problem Amplification -> Solution Tease -> CTA Push structure (Ready-to-use bridge page copy: headline, short paragraphs (2-4 sentences, bold key phrases, quoted testimonial snippets), clearly marked CTA placement(s), optional advertorial header/byline/date stamp, optional fake comment thread, optional bottom disclaimer block)
- **On a bare "Go":** asks for inputs: any of ad copy, offer details, audience info, or VSL script — states 'the more context you give me, the stronger the output' rather than generating a placeholder page.
- **Gotchas:** Never asks clarifying questions (unlike write-like-luke-bot's actual behavior) — it always produces a full page, filling gaps generically if inputs are missing, so output quality is only as good as what you feed it. Has a hidden decision layer (advertorial_framing=auto) that changes structure based on inferred niche/traffic temperature — worth knowing since output format can vary (with/without fake publication header) even with the same explicit params. Has a strong 'anti-AI' human-writing mandate and a prompt-extraction defense section (will refuse to describe its own methodology/template). LIVE PROBE CONTRADICTION: despite the prompt's 'never asks questions, produces output immediately' claim, a bare 'Go' with zero context produced a request for at least one input rather than a generated page — supply at least one of the optional inputs rather than sending a bare trigger.
- **Consumes:** `buyer-profile`, `ad-hooks`, `offer-details`, `vsl-script`, `landing-page-copy`, `winning-ad`, `landing-page-url` · **Produces:** `advertorial`, `landing-page-copy`

## caveman-page-master-bot

**Caveman Page Master Bot** — Produces a complete Q&A-format 'Caveman Page' advertorial (or, in questions_only mode, a justified question outline) calibrated by price tier, market awareness, and sophistication. Use when you need a conversational objection-crushing page that walks a prospect from curiosity to purchase.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **build_a_buyer** (buyer-profile) — Target market profile: demographics, psychographics, pain points, desires, beliefs, language patterns. Primary audience intelligence input. ← *get it from:* output of a buyer-profile-type bot (e.g. Build-a-Buyer bot), or user-supplied audience research
  - **product_info** (product-info) — What the product is, how it works, key mechanisms, ingredients/components, features, differentiators. ← *get it from:* user's product page, spec sheet, or brand doc
  - **offer_details** (offer-details) — Pricing, packages, bonuses, guarantee, shipping, order details. ← *get it from:* user's offer page or checkout config
  - **sales_copy** (other:sales-materials) — Existing sales materials: VSL script, sales page text/URL, copy blocks, or raw marketing materials. ← *get it from:* user-pasted VSL/landing-page-copy or output of a copy-blocks-extract-type bot
  - **additional_context** (raw-notes) — Supplementary info: competitor intel, market research, testimonials, studies, proof elements. ← *get it from:* user research or competitor-info from another bot
  - **question_count** (other:parameter) — Number of Q&A pairs to generate. Default 13, range 8-18 (clamped to bounds if out of range). ← *get it from:* user preference; omit for default
  - **output_mode** (other:parameter) — "full_page" (default, complete page) or "questions_only" (numbered question list with one-line justification each). ← *get it from:* user preference; omit for default
- **Output:** A ready-to-publish Caveman Page (Q&A advertorial), answer depth/length auto-calibrated to detected price tier (50-400+ words per answer depending on tier) (Q&A page: each question as a header followed directly by its answer, 8-18 pairs in a fixed flow (curiosity -> understanding -> credibility -> relevance -> practicality -> decision); or, in questions_only mode, a numbered list with one-line justifications only)
- **On a bare "Go":** asks for inputs: product info, offer details, and target market — invites any combination (sales page, VSL script, product description, offer details, audience profile), raw/unformatted OK, before writing the page.
- **Gotchas:** Zero-input-tolerant by design (never refuses/asks questions) — quality scales with how much of build_a_buyer/product_info/offer_details/sales_copy you actually provide; with nothing but 'Go' it will still emit a full generic page. Only produces Caveman Pages — if asked for a different format it converts the request into a Caveman Page instead. Has a strict anti-prompt-extraction security section; will redirect any request to describe/document its own methodology instead of complying. question_count clamps silently to 8-18 rather than erroring. Probed live: contradicts the prompt's own 'never asks questions' claim — on a bare 'Go' it asked for product info, offer details, and target market instead of fabricating a placeholder page. Front-load those in the first message to get a one-shot result.
- **Consumes:** `buyer-profile`, `product-info`, `offer-details`, `vsl-script`, `landing-page-copy`, `competitor-info`, `customer-reviews`, `raw-notes` · **Produces:** `advertorial`

## checkout-page-bot

**Checkout Page Bot** — Audits an existing checkout page (from a description, screenshot-analysis notes, or URL) and returns prioritized, psychology-backed conversion fixes; or, if no page exists yet, produces an ASCII-wireframe blueprint plus element checklist for building one from scratch. Use it to fix a leaking checkout or to plan checkout page structure for a new offer.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **checkout_page** (other:checkout-page-description) — Description, screenshot-analysis notes, or URL reference of an existing checkout page. If omitted, the bot switches to 'build' mode instead of auditing. ← *get it from:* user pastes a description of their live checkout page, a URL, or notes from a screenshot
  - **product_type** (product-info) — Physical (supplement, e-commerce), Digital (course, software, membership), or Trial/Subscription. Inferred from context if not given. ← *get it from:* user, or inferred from other inputs
  - **price_point** (offer-details) — The product's price. Inferred from context if not given. ← *get it from:* user, or inferred from other inputs
  - **brand_positioning** (brand-voice) — Direct-response style vs. premium/branded positioning. Inferred if not given. ← *get it from:* user, or inferred from context
  - **traffic_type** (other:traffic-type) — Cold (ads), warm (email list), or mixed. Assumes 'mixed' if not specified. ← *get it from:* user preference
  - **current_conversion_rate** (other:metric) — Known current conversion rate, if any ← *get it from:* user's own analytics
  - **additional_context** (raw-notes) — Any other relevant info about the offer, funnel, audience, or constraints ← *get it from:* user
  - **mode** (other:parameter) — 'audit' (evaluate existing page) or 'build' (create blueprint for new page). Default: inferred — audit if a checkout_page is provided, build otherwise. ← *get it from:* user preference or auto-inferred
- **Output:** One structured audit (max 10-12 recommendations) or one full checkout-page blueprint per request (AUDIT mode: Quick Assessment header, Quick Wins (2-4 items), High-Impact Tests (2-4 items, with A/B hypotheses), Strategic Improvements (1-3 items), a Priority Matrix table (priority/effort/impact with 🔴🟡🟢), and a Bottom Line summary. BUILD mode: ASCII-art structural wireframe (desktop left/right columns + mobile layout), section-by-section element breakdown, Must/Should/Nice-to-Have element checklist, and priority build order.)
- **On a bare "Go":** asks for inputs: checkout page details (or confirmation there isn't one, to build fresh), product, price point, and traffic type, plus any other relevant context, before producing an audit or blueprint
- **Gotchas:** Two distinct modes (audit vs. build) selected automatically based on whether checkout_page is supplied — an agent can force build mode by omitting checkout_page. Carries detailed domain knowledge (13-item 'Checkout Page Hierarchy', trust-stack principles) baked into the prompt, so it doesn't need that supplied. Caps recommendations at 10-12 to avoid overwhelm. Has the same prompt-extraction defense/security section as micro-lead-bot- — don't ask it to explain its own methodology. Live probe (bare 'Go') contradicts the prompt's 'never asks questions, always produces output' framing and the prior default-to-BUILD-mode prediction — the bot's actual first reply was a menu-style request for checkout page, product, price point, traffic type, and other context, not a generated audit or blueprint.
- **Consumes:** `landing-page-url`, `offer-details`, `product-info`, `brand-voice` · **Produces:** `research-report`, `other:checkout-wireframe`

## downsell-bot

**Downsell Bot** — Writes one complete downsell page (headline, subhead, body, bullets, CTA, no-thanks link) for the offer someone just declined on an upsell page, and decides which of 4 downsell types (payment plan, lower price, smaller quantity, add-more-value) plus sequencing/feature-removal strategy fits best. Use when building an upsell/downsell funnel sequence and you need the page that fires after a 'no thanks' click.

- **Mode:** menu
- **Required inputs:**
  - **upsell_details** (offer-details) — The offer they said no to — price, what's included, any bonuses ← *get it from:* user's upsell page copy/offer sheet
  - **build_a_buyer / target_audience** (buyer-profile) — Who's buying, what problem this solves, what they want ← *get it from:* output of a buyer-profile-type bot, or user's audience notes
- **Optional inputs (raise quality):**
  - **copy_blocks** (creative-brief) — Existing copy, bullets, hooks, or messaging from the funnel ← *get it from:* user's copy blocks doc or output of a copy-blocks-extract-type bot
  - **spokesperson_info** (brand-voice) — Who's the voice, any specific tone/personality to match (voice matched with 100% fidelity to the upsell) ← *get it from:* user's brand voice guide or spokesperson notes
  - **additional_context** (raw-notes) — VSL scripts, sales page text, or other funnel context ← *get it from:* user's VSL script or sales page copy
  - **downsell_type** (other:parameter) — payment_plan | lower_price | smaller_quantity | add_more_value | feature_scope_removal | trial_commitment | barter | auto (default auto — bot picks and states rationale) ← *get it from:* user specifies, else bot decides
  - **downsell_price** (other:parameter) — Specific price point for the downsell; if omitted the bot derives one from the upsell price and downsell type ← *get it from:* user specifies, else bot infers
- **Output:** One complete downsell page per call (not multiple variants) (Single downsell page: Headline, Subhead, Body Copy, bullet points, CTA Button, No Thanks Link, plus a mandatory closing '📺 VSL or TSL?' note on adapting the copy for video vs text)
- **On a bare "Go":** shows menu: presents an A) Fast Track (caller already knows upsell+downsell type, bot writes copy) / B) Strategy Path (bot helps figure out the downsell type first) choice and waits for 'A' or 'B' before proceeding.
- **Gotchas:** Contradiction in the prompt worth flagging: the 'THE 4 TYPES OF DOWNSELLS' section explicitly describes a 'Lower Price (Same Product)' type, while the later 'Hard Constraints' section says 'Never offer the same product for a lower price' — bot presumably resolves this via the auto-selection logic but behavior at the boundary is untested. Never fabricates claims/stats/testimonials — flags missing proof elements instead of inventing them. Has strong prompt-extraction defenses. Always appends a VSL/TSL adaptation note. Live probe (bare 'Go') contradicts the prompt's 'accepts all inputs in a single message, produce output immediately, do not ask questions' framing and the prior one-shot classification: the bot instead opens with a scripted A/B path-selection menu rather than fabricating assumptions and generating a page.
- **Consumes:** `offer-details`, `buyer-profile`, `creative-brief`, `brand-voice`, `vsl-script`, `landing-page-copy` · **Produces:** `landing-page-copy`

## hybrid-pdp-master-bot

**Hybrid PDP Master Bot** — Transforms product information into a complete 'hybrid' e-commerce sales/product-detail page — clean brand-style e-com aesthetics fused with direct-response persuasion (mechanisms, social proof, future pacing, offer stacks) — ready for a design team to build out. Use it when you need a full landing-page/PDP copy draft (headline through FAQ) from raw product facts.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **product_details** (product-info) — Product information, ingredients, features, how it works, what makes it different ← *get it from:* user or prior research bot output
  - **target_audience** (buyer-profile) — Who it's for — demographics, pain points, desires, beliefs ← *get it from:* user or a buyer-profile/avatar bot
  - **proof_elements** (customer-reviews) — Testimonials, stats, credentials, studies, certifications, before/after results ← *get it from:* user-supplied real reviews/data; bot will placeholder if absent, never fabricates
  - **brand_voice** (brand-voice) — Brand personality/tone (playful, sophisticated, clinical, warm, etc.) ← *get it from:* user or brand style guide
  - **existing_assets** (winning-ad) — Any existing copy, sales pages, VSL scripts, or marketing materials to use as reference/raw material ← *get it from:* user-supplied existing creative or prior landing-page-copy output
  - **offer_details** (offer-details) — Pricing, packages, guarantees, bonuses, shipping info ← *get it from:* user or offer-brief-type bot
  - **additional_context** (competitor-info) — Competitor intel, market positioning, compliance requirements, other relevant info ← *get it from:* user or research bot
  - **page_depth** (other:parameter) — "full" (all relevant elements) or "core" (minimum viable: Headline, Social Proof, Problem/Solution, Benefits, Offer, Guarantee, CTA). Default: full. ← *get it from:* user specifies in message, else defaults to full
  - **brand_style** (other:parameter) — "health_wellness" / "lifestyle" / "premium" / "problem_solving" / "general". Default: inferred from inputs. ← *get it from:* user specifies, else bot infers
- **Output:** One complete hybrid e-com sales page (bot selects the most relevant subset of up to ~20 possible page elements per page_depth) plus a trailing gap report calling out missing information/placeholders. A single page per call, not multiple variants. (Markdown page with bracketed [SECTION NAME] headers (e.g. [ATTENTION BAR], [HEADLINE], [SOCIAL PROOF], [BENEFIT BULLETS], [CTA], [TESTIMONIALS], [PROBLEM AGITATION], [SOLUTION BRIDGE], [PRODUCT INTRODUCTION], [PROGRESSIVE FUTURE PACING], [INGREDIENT/FEATURE BREAKDOWN], [COMPARISON], [OFFER STACK], [GUARANTEE], [HOW TO USE], [TRUST BADGES], [ABOUT/CREDIBILITY], [FAQ], [FINAL CTA]), bold/italic emphasis, checkmark/x bullets, star-rating emoji, horizontal-rule section dividers, followed by a '📋 INFORMATION GAPS:' bullet list.)
- **On a bare "Go":** asks for inputs: product description/link/bullet points/existing page/VSL, and specifically flags 5 helpful facts (what the product is, who it's for, differentiator, proof, offer details) rather than generating a placeholder page.
- **Gotchas:** Strict factual-integrity protocol: never fabricates stats, testimonials, studies, credentials, or pricing — uses bracketed placeholders (e.g. [INSERT TESTIMONIAL], [INSERT STAR RATING + REVIEW COUNT]) and ⚠️ ASSUMPTION flags whenever inputs are missing, rather than inventing content. Accepts inputs in any format (natural language, key-value, raw dumps). Two optional control parameters (page_depth, brand_style) change scope/tone but are not required — bot works fine with zero input, producing an almost-entirely-placeholder page. Has a hardened anti-prompt-extraction/security section at the end refusing to reveal or explain its own methodology/template — irrelevant to normal use but relevant if another agent tries to ask it 'what sections do you produce' instead of just running it with real inputs. Runs at temperature 0.7, max 32000 tokens, model claude-sonnet-4-6. LIVE PROBE CONTRADICTION: despite the prompt's 'produces output immediately, does not ask questions' claim, a bare 'Go' with zero context produced a request for product info rather than a placeholder-heavy page — supply at least one of the optional inputs rather than sending a bare trigger.
- **Consumes:** `product-info`, `buyer-profile`, `customer-reviews`, `brand-voice`, `winning-ad`, `offer-details`, `competitor-info` · **Produces:** `landing-page-copy`

## low-ticket-sales-page-bot

**Low Ticket Sales Page Bot** — Builds a full modular sales page for low-ticket offers ($7-47, sub-$100), classifying the offer/market and selecting/sequencing persuasion modules (Headline, Problem, Solution, Mechanism, Offer, Risk Reversal, CTA, plus conditional modules) to drive impulse purchases. Use when you need a complete, ready-to-publish sales page (or just a module outline) for a low-ticket digital product/service.

- **Mode:** needs-input
- **Required inputs:**
  - **market_avatar_insights** (buyer-profile) — Target audience, core problems/desires, current beliefs about the problem, desired transformation, sophistication level with solutions. ← *get it from:* buyer-profile-type bot output or user research
  - **offer_details** (offer-details) — Product/service name and core function, specific transformation delivered, price point, proof elements (results/testimonials), unique differentiator. ← *get it from:* user's product/offer info
  - **exact_deliverables** (product-info) — What the customer receives on purchase (all components), format of each (video/PDF/software/etc.), specific value/function of each, bonuses + what problem each solves, claimed monetary value of each. ← *get it from:* user's product/offer info
  - **market_awareness_and_positioning** (other:market-awareness) — Market awareness level (problem/problem-aware/solution-aware/product-aware/most-aware), solution familiarity, alternatives tried, unique angle/approach. ← *get it from:* user or market-research bot
  - **sales_page_goals** (creative-brief) — Desired visitor action, available scarcity/urgency elements, design preferences or brand guidelines, traffic temperature (cold/warm/hot). ← *get it from:* user
- **Optional inputs (raise quality):**
  - **supporting_materials** (raw-notes) — Build-a-Buyer profiles, Copy Blocks, Offer Briefs, existing sales copy, VSL scripts, sales page URLs, or any other marketing materials. ← *get it from:* user, or outputs of other bots (buyer-profile, copy-blocks, offer-brief bots)
  - **output_type** (other:parameter) — "outline_only" = module outline + rationale only. "full_page" (default) = outline + rationale followed by complete sales page copy. ← *get it from:* user
- **Output:** One complete low-ticket sales page (module outline + full copy by default; outline only if output_type=outline_only), covering at minimum Headline, Problem, Solution, Mechanism/Differentiation, Offer, Risk Reversal, and CTA modules, plus conditional Credibility/Proof/Objection-Handling/Urgency modules (Markdown sections: (1) module outline with rationale per module (why selected, psychological trigger, how it advances conversion, emotional state created), (2) if full_page, each module written out as self-contained persuasion copy with subheads, (3) visual design guidance and testing recommendations for key modules)
- **On a bare "Go":** asks for inputs: requests product name/function, target audience & core problem, price point, deliverables/bonuses, proof/testimonials, and scarcity/urgency elements, then promises to build the complete sales page immediately.
- **Gotchas:** Explicitly instructed to prioritize conversion over restraint/tastefulness and use 'dark pattern'-adjacent persuasion techniques (scarcity, urgency, problem-intensity amplification) — only hard restrictions are no false claims/fabricated testimonials, no unsubstantiated guarantees, no medical claims unless client-provided, no direct competitor attacks. Runs its own internal 'Quality Control Verification System' checklist before finalizing (not user-visible unless asked). 5 required input categories map closely to a full offer/market brief — an agent without all 5 should still expect usable output, just with more inferred/generic content in the gaps. Has the standard prompt-protection/security block appended. Live probe on a bare 'Go' contradicted the prompt's 'never asks questions, always generates a complete deliverable' framing and the predicted invent-a-generic-page fallback: it asked for the offer/audience/price/deliverables/proof/urgency details instead of generating placeholder copy.
- **Consumes:** `buyer-profile`, `offer-details`, `product-info`, `creative-brief`, `raw-notes` · **Produces:** `landing-page-copy`

## opt-in-page-optimization-bot

**Opt-In Page Optimization Bot** — Produces psychologically-optimized opt-in page copy (headline/subheadline/body/CTA variations tagged by rhetorical frame and traffic temperature), then — on request — a full copy-only page text pack, then — on further request — a complete responsive HTML implementation. Use it to spin up or rewrite a lead-gen opt-in page (call booking, webinar reg, free training, or lead-magnet download) matched to a specific traffic source's psychology.

- **Mode:** multi-phase
- **Required inputs:**
  - **page_type** (other:page-type-enum) — Which of 4 opt-in page types: "call" (book a call) / "webinar" (registration) / "training" (free training/workshop) / "download" (report/guide/checklist). This is the only field explicitly labeled 'Core Input'; it determines which page-type-specific field set (A/B/C/D below) applies. Live probe also lists this under "Required". ← *get it from:* user states which funnel step they're building
  - **audience** (buyer-profile) — Who this is for (and explicitly not for). Live probe lists this under "Required", contradicting the system prompt's stated zero-question policy. ← *get it from:* user, or output of a buyer-profile bot
  - **traffic_sources** (other:traffic-source) — How people will first hear about this: paid ads, SEO, social, email list, partner list, referral, DM, existing clients. Live probe lists this under "Required". ← *get it from:* user's media plan/traffic sources
- **Optional inputs (raise quality):**
  - **relationship_context** (other:traffic-source) — Existing relationship most visitors have: strangers from ads/search; followers/subscribers; past customers; warm referrals/partners; mixed ← *get it from:* user
  - **objections** (other:objections) — Top 2 hesitations people have before converting ← *get it from:* user, or research/customer-reviews analysis
  - **proof_assets** (customer-reviews) — Credibility, results, testimonials, client logos (or "none") ← *get it from:* user's testimonial/results library
  - **mechanism** (mechanism) — How the offer works differently (unique mechanism) ← *get it from:* user or offer-details doc
  - **brand** (brand-voice) — Brand guidelines or voice ← *get it from:* user's brand doc
  - **compliance** (other:compliance-requirements) — Industry compliance requirements (finance/health/legal) — triggers approved-claims/disclaimer constraints ← *get it from:* user
  - **A_* fields (page_type=call)** (offer-details) — A_call_name, main_outcome, timeframe, A_agenda_bullets (3-5), A_deliverables, A_qualifiers, A_scheduler_link, A_duration, A_timezone, A_host_name/title/cred (optional), A_scarcity (optional) ← *get it from:* user's call/offer details
  - **B_* fields (page_type=webinar)** (offer-details) — B_webinar_title, B_promise, B_format, B_datetime_or_access, B_platform, B_seat_limit, B_hosts, B_outcomes (4-7), B_agenda (optional), B_replay_policy (optional) ← *get it from:* user's webinar details
  - **C_* fields (page_type=training)** (offer-details) — C_training_title, C_format, C_access_window, C_curriculum_bullets (4-6), C_instructor, C_community (optional), C_scarcity (optional) ← *get it from:* user's training/workshop details
  - **D_* fields (page_type=download)** (offer-details) — D_asset_title, D_benefit, D_format, D_size, D_takeaways (5-8), D_author ← *get it from:* user's lead-magnet details
  - **supporting_materials** (other:supporting-materials) — Build a Buyer, Copy Blocks, Market Map, Funnel Brief, ad copy, emails, scripts, landing page copy, audience descriptions, or other context ← *get it from:* outputs of other Genesis bots (buyer-profile, ad-copy, etc.) or user docs
  - **source_message_priority** (ad-hooks) — Exact headline/hook from a specific ad or email to mirror for message-match congruence ← *get it from:* the specific winning ad/email driving traffic to this page
  - **mobile_above_fold** (other:layout-preference) — Must-show items above the fold on mobile — provide when traffic is mobile-heavy/social ← *get it from:* user
  - **quantity** (other:parameter) — Number of Step 1 copy variations to generate. Default: 10. ← *get it from:* user, or omit for default
  - **frame_preferences** (other:parameter) — Preferred/avoided rhetorical frames, e.g. "no contrarian takes", "more curiosity". Default: none (bot's own Frame Selection Policy applies). ← *get it from:* user
  - **step2_selection** (other:selection-instruction) — Step 2 trigger: variation selection or blend instructions (e.g. "#3" or "#3 headline + #7 CTA"), plus any revision feedback, referencing the Step 1 output ← *get it from:* user picks from Step 1 output (requires Step 1 to have already run in the same context)
  - **step3_request** (other:selection-instruction) — Step 3 trigger: explicit request for HTML output, optionally with brand guidelines (colors, fonts, logo) ← *get it from:* user explicitly asks for HTML after Step 2 text pack is approved
- **Output:** Default output is copy variations only (10). HTML is never generated unless explicitly asked for. If a message requests multiple steps at once, all applicable steps run and outputs are combined. (Step 1 (default/primary output): N copy variations (default 10), each = Headline + Subheadline + Body Copy Snippets + CTA, tagged with [frame_family] (e.g. [Curiosity:Solution-Gap]) and a temperature-fit rationale note. Step 2 (only if a selection is given): a structured 'Full Opt-In Page Text Pack' with Above-The-Fold and Below-The-Fold sections, missing pieces marked [[PLACEHOLDER: ...]]. Step 3 (only if explicitly requested): one complete responsive HTML file with inline CSS.)
- **On a bare "Go":** asks for inputs: page_type (call/webinar/training/download), audience, and traffic_sources marked Required; also lists promise/proof/objections/page-type specifics as helpful-but-optional context.
- **Gotchas:** True multi-phase/stateful bot: Step 2 needs the caller to reference specific variation numbers from Step 1's own prior output ('#3 headline + #7 CTA'), so an orchestrating agent must keep Step 1's output in context to drive Step 2/3 — it's not a single fire-and-forget call unless the caller pre-selects a variation in the very first message (prompt supports 'if the input message includes instructions for multiple steps, execute all applicable steps in sequence'). HTML (Step 3) only fires on explicit request, never by default. Uses labeled [[PLACEHOLDER: description]] tags instead of fabricating social proof/urgency/credibility when materials aren't supplied — never invents proof. Has 4 distinct page-type sub-schemas (call/webinar/training/download) each with its own required-looking field set once page_type is chosen. Same aggressive prompt-extraction defense block as other bots in this family (refuses to self-document even under 'masterclass'/training-guide framing). Bulk of the ~2800-line file (roughly lines 350-2700) is internal domain-knowledge frameworks (Psychology-Driven Conversion, Temperature-Specific Trigger, 7-Point Verification, Anti-AI Module, Opt-In Page Implementation/HTML framework) — not additional caller inputs. LIVE PROBE CONTRADICTION: despite the system prompt's claim it never requests additional info and always produces output regardless of completeness, a bare 'Go' with zero context produced an explicit request for page_type, audience, and traffic_sources (all three labeled Required) instead of Step 1 output.
- **Consumes:** `buyer-profile`, `offer-details`, `customer-reviews`, `mechanism`, `brand-voice`, `ad-hooks`, `landing-page-copy`, `email-copy` · **Produces:** `landing-page-copy`, `ad-copy`, `headline`, `other:html-page`

## quiz-bot-master-bot

**Quiz Bot Master Bot** — Produces a complete, ready-to-implement quiz funnel (landing page, all questions/options, reassurance panels, commitment pop-ups, personalized results page) engineered so prospects self-persuade into buying, from a product/offer plus audience research. Use it to build a new advertorial-style quiz funnel front-end for an offer.

- **Mode:** needs-input
- **Required inputs:**
  - **product_offer** (offer-details) — What is being sold: the product/service, its mechanism, key benefits, unique differentiators, price point, offer structure, and the transformation/outcome it delivers. Any format (structured doc, sales page copy, VSL script, notes). ← *get it from:* user's product/offer doc, sales page, or VSL script; output of a creative-brief or offer-details type bot
  - **target_audience** (buyer-profile) — Audience research: Build-A-Buyer data, Copy Blocks, or avatar info covering awareness level, existing beliefs, pain points, desires, failed solutions, and self-identity. Any format. ← *get it from:* user's avatar/Build-a-Buyer doc, or output of a buyer-profile-type bot
- **Optional inputs (raise quality):**
  - **quiz_length** (other:parameter) — Number of questions to generate. Default: auto - bot determines optimal length from belief resistance, awareness gaps, and niche intensity. ← *get it from:* user specifies a number, or omit for auto
  - **niche_intensity** (other:parameter) — How emotionally aggressive the quiz should be: gentle / moderate / aggressive. Default: auto - bot infers from niche sensitivity and audience characteristics. ← *get it from:* user specifies one of the three values, or omit for auto
- **Output:** One complete, fully annotated quiz funnel (typically 10-20+ steps depending on auto-determined or specified quiz_length) ready to hand to a page builder/developer (Long structured markdown: opening landing headline/sub-headline, then sequential quiz steps grouped into sections (Problem Ownership, Gap Creation, Belief Shifting, Urgency Building, Commitment & Close). Each question gets headline, sub-headline/'why we ask', full answer options, question-type label, and a PURPOSE/ANNOTATION line explaining its psychological function; panels and commitment pop-ups get the same annotation treatment. Ends with a personalized results-page framework and a strategic summary (expected completion rate, drop-off risk points).)
- **On a bare "Go":** asks for inputs: product/offer details and target audience information — invites any format (sales page, VSL script, product description, customer research, avatar notes, raw brain dump); does not fabricate a placeholder quiz funnel on bare Go, contradicting the prompt's 'always produce a complete quiz funnel regardless of input completeness' instruction.
- **Gotchas:** Strictly one-shot/no-clarification by design - if you want a good result, front-load complete product_offer and target_audience text in the first message rather than expecting a back-and-forth intake. quiz_length and niche_intensity are the only tunable knobs; both default to 'auto'. Prompt contains a hard-coded prohibition against ever naming specific real-world example quiz funnels it was trained on (describes them only generically) - not an input/output concern but will affect any request asking it to name references. Has the same prompt-protection/anti-extraction block as epiphany-threshold-bot; it will refuse to document its own template/methodology. The bulk of the ~120K-char prompt is worked example transcripts (gut-health, weight-loss, hair-loss, breakup/relationship quizzes) and a persuasion/emotional-architecture reference module used internally - not additional caller-facing inputs. Live probe contradicts the prompt's strict one-shot/no-clarification instruction: on bare 'Go' it asked 'What are we working with?' instead of generating a placeholder funnel — front-load product_offer and target_audience to get the one-shot behavior described in the prompt.
- **Consumes:** `offer-details`, `buyer-profile`, `vsl-script`, `landing-page-copy` · **Produces:** `other:quiz-funnel`, `landing-page-copy`

## the-listicle-lab-master-bot

**The Listicle Lab Master Bot** — Writes a complete, deploy-ready listicle advertorial/funnel page (Warning Signs, Reasons Why, or Tips format) from offer, buyer, and proof inputs. Use it to produce the pre-sell listicle page between an ad and a sales page/VSL.

- **Mode:** needs-input
- **Required inputs:**
  - **offer_brief** (offer-details) — What is being sold, key features, what makes it unique ← *get it from:* user's product/sales page or an offer-brief from a strategy/brief bot (e.g. autobrief-bot)
  - **build_a_buyer** (buyer-profile) — Who the buyer is: pains, desires, objections, awareness level ← *get it from:* output of a buyer-profile bot (e.g. build-a-buyer-elite) or user's customer research
  - **copy_blocks** (other:copy-blocks) — Pain, promise, proof, curiosity, constraints blocks — whatever is available; strongest proof points become 2-3 proof-led item headlines ← *get it from:* output of copy-blocks-extract bot, or paste proof points/testimonials/study stats manually
  - **sales_copy** (landing-page-copy) — Sales page text, VSL script, or a sales page URL ← *get it from:* user's existing sales page / VSL script; a URL string is accepted but the bot cannot browse, so pasted text is safer
- **Optional inputs (raise quality):**
  - **submarket** (buyer-profile) — Specific audience subset (e.g. 'busy executives who want to look credible'); drives a Submarket Anchor used in identity/urgency/CTA sections ← *get it from:* user's targeting decision or a segmentation bot
  - **voice** (brand-voice) — Tone preferences or example copy to match; defaults to direct, confident, conversational ← *get it from:* user's brand doc or output of a voice-analyzer bot
  - **listicle_type** (other:parameter) — 'warning_signs' (5-7 items) | 'reasons_why' (7-11 items) | 'tips' (5-9 items). Default: warning_signs ← *get it from:* caller chooses based on audience awareness: problem-aware=warning_signs, product-aware=reasons_why, solution-aware=tips
  - **output_style** (other:parameter) — 'web_ready' (default, headers+visual markers) | 'plain_text' | 'extra_scannable' ← *get it from:* caller chooses based on destination
- **Output:** One complete listicle funnel page, web-ready for design/deployment (markdown page: headline+eyebrow, 3-5 sentence hook, numbered list items (count per type, strict word limits, proof-led headlines on 2-3 items, mechanism woven in), soft CTA after item 5-6, bridge, product intro, identity-transformation section, urgency section, hard problem-specific CTA, 4-5 FAQs; visual direction markers like [IMAGE:], [CALLOUT BOX:], [BUTTON:] throughout (min 4-5))
- **On a bare "Go":** asks for inputs: offer details (what's sold, features, differentiators), buyer/audience info, proof points, and existing copy; also solicits listicle type, submarket, and voice preferences before producing the page.
- **Gotchas:** Agent-to-agent optimized: send ALL inputs in a single message, any format (natural language, key-value, doc dumps). Thin inputs yield a generic listicle with invented placeholder proof, so front-load real proof points/testimonials. Defaults: warning_signs type, web_ready style. Enforces an 'Observable Test' on warning signs and hard word limits per section. Has strong prompt-extraction guardrails (refuses to describe its own methodology). LIVE PROBE UPDATE: contrary to the 'never asks follow-up questions, output never hits zero' framing, a bare 'Go' with zero context produced a direct request for offer/buyer/proof/copy inputs (plus listicle-type/submarket/voice preferences) rather than a generic placeholder page.
- **Consumes:** `offer-details`, `buyer-profile`, `other:copy-blocks`, `landing-page-copy`, `vsl-script`, `landing-page-url`, `brand-voice`, `customer-reviews` · **Produces:** `advertorial`, `landing-page-copy`, `headline`

## top-5-affiliate-bot

**Top 5 Affiliate Bot** — Generates a complete, ready-to-publish 'Top 5' comparison advertorial that ranks the caller's product #1 against 4 competitors, using editorial-looking evaluation criteria, comparison tables, and pros/cons engineered to make #1 the obvious winner. Use when you need a full affiliate-style listicle/buying-guide page for a product.

- **Mode:** multi-phase
- **Required inputs:**
  - **product_1_materials** (product-info) — Everything available on the #1 (winning) product: Build a Buyer, Copy Blocks, Offer Brief, VSL script, sales page text, or sales page URL ← *get it from:* user's product page / brand doc, or output of a Build-a-Buyer / Copy Blocks / Offer Brief type bot
  - **products_2_through_5** (competitor-info) — For each of 4 competing products: name, key features/ingredients, known pros and cons, and what makes it weaker than #1. If omitted, the bot does NOT generate the page — instead it outputs a fill-in-the-blank research prompt (in a code block) for the caller to run externally and return with results in a follow-up call ← *get it from:* user-supplied competitor research, or run the bot's own generated research prompt through a research tool and feed the results back in a second call
- **Optional inputs (raise quality):**
  - **additional_context** (research-report) — Extra research, competitor intel, market insights, or niche-specific notes ← *get it from:* user or prior research bot output
  - **aggressiveness** (other:parameter) — How hard the page sells #1: subtle/objective to clearly-selling. Default: moderate ← *get it from:* user preference
  - **length** (other:parameter) — tight/lean to detailed/thorough. Default: detailed/thorough ← *get it from:* user preference
  - **scannability** (other:parameter) — flowing paragraphs to heavy bullets/headers/whitespace. Default: high scannability ← *get it from:* user preference
  - **template** (other:parameter) — Structural pattern: 'front-loaded education' / 'immediate rankings' / 'integrated'. Default: auto-selected by product category ← *get it from:* user preference
- **Output:** One complete ready-to-publish Top 5 advertorial page (all 5 products), OR (if competitor info missing) a single fill-in-the-blank competitor-research prompt in a code block and nothing else (Full long-form page: ranking badges/scores for 5 products, criteria-establishment section, individual product reviews with pros/cons, comparison table, educational content, multiple CTAs favoring #1)
- **On a bare "Go":** asks for inputs: requests product #1 materials (sales page/VSL/offer brief/copy blocks/product details) and, optionally, products #2-5; without #1 details it cannot even generate the competitor-research prompt.
- **Gotchas:** Interaction is one-shot when full inputs are given; becomes a two-call flow when competitor info is missing (call 1 returns a research prompt only). Two-call workflow when competitor data is missing: call 1 returns only a research prompt and stops; caller must run that research and send results back in call 2. Enforces heavy 'anti-AI' humanizing writing style (forbidden words/patterns list, must sound like a specific person). Will not fabricate product info — works only with what's given. Has strong prompt-injection/self-disclosure defenses; refuses to describe its own methodology/template. Live probe (bare 'Go') confirms it asks for product_1_materials rather than fabricating a placeholder product — consistent with the existing multi-phase classification; the previously-speculated 'no fallback for missing #1 product' resolves to a request-for-input, not fabrication.
- **Consumes:** `product-info`, `competitor-info`, `research-report` · **Produces:** `advertorial`, `research-report`

## top-5-products-bot

**Top 5 Products Bot** — Generates a Top 5 Product Comparison Advertorial — a ranking-style bridge page that builds authority and mechanism belief, eliminates competitors #5-#2 with fair-but-decisive flaws, and teases a #1 pick that drives clicks to a VSL/sales page.

- **Mode:** multi-phase
- **Required inputs:**
  - **build_a_buyer** (buyer-profile) — Avatar profile: demographics, psychographics, pain points, desires, beliefs ← *get it from:* output of Build a Buyer / Build a Buyer ELITE bot
  - **copy_blocks** (mechanism) — Mechanism, proof elements, claims, and supporting marketing copy ← *get it from:* output of a Copy Blocks bot or user-supplied swipe/proof doc
  - **offer_brief** (offer-details) — Product details, positioning, pricing, unique selling proposition ← *get it from:* user's offer brief
  - **sales_copy** (vsl-script) — VSL script, sales page text, or URL to the sales page this advertorial bridges to ← *get it from:* user-supplied VSL/sales page copy or URL
- **Optional inputs (raise quality):**
  - **competitor_products** (competitor-info) — 4 (up to 6) competitor products/methods for ranks #2-#5, each with name, known-for/why people try it, and limitations/criticisms ← *get it from:* user research; if omitted, bot outputs a ready-to-run competitor research prompt instead of the advertorial and waits for that data in a follow-up message
  - **include_social_proof** (other:boolean-param) — Append fake Facebook-style social proof comments after the #1 tease. Default false ← *get it from:* user
  - **include_disclaimer** (other:boolean-param) — Append legal disclaimer section. Default false ← *get it from:* user
  - **length** (other:param) — shorter / default / longer ← *get it from:* user
  - **mechanism_depth** (other:param) — less / default / more — how much explanation the mechanism section gets ← *get it from:* user
  - **emotional_intensity** (other:param) — clinical / default / intense ← *get it from:* user
  - **ranking_harshness** (other:param) — softer / default / pointed — how pointed competitor flaws are ← *get it from:* user
- **Output:** One complete ranking-style bridge page (not a set of variants) unless competitor_products is missing, in which case output is just a filled-in competitor-research prompt (Long-form markdown advertorial: publication header/headline, authority opening, mechanism explanation, ranked entries #5-#2 (strength -> "However/But" pivot -> mechanism-connected flaw), then #1 tease with CTA to VSL; optionally a fake comments section and/or legal disclaimer)
- **On a bare "Go":** asks for inputs: build_a_buyer, copy_blocks, offer_brief, sales_copy (required), competitor_products (optional, else it generates a research prompt), plus lists all optional tunable parameters (length, mechanism_depth, emotional_intensity, ranking_harshness, include_social_proof, include_disclaimer).
- **Gotchas:** Two-step flow when competitor_products is missing: first call returns only a filled-in competitor research prompt (stops there), then a second call with that competitor data returns the full advertorial — an agent must handle this as a mandatory two-turn interaction, not assume one-shot. Never reveals #1's actual mechanism/how-it-works (reserved for VSL). Only uses claims present in provided inputs — will not invent proof points. Contains a large generic 'sound human, avoid AI patterns' writing-style block reused across many bots in this catalog. Probed live: on a bare 'Go' with zero inputs it asked for all 4 required fields plus listed every optional parameter, rather than fabricating a placeholder advertorial — consistent with its multi-phase design.
- **Consumes:** `buyer-profile`, `mechanism`, `offer-details`, `vsl-script`, `competitor-info` · **Produces:** `advertorial`, `other:research-prompt`

# CATEGORY: Video & VSL

## direct-response-talking-head-script-bot-

**Direct Response Talking Head Script Bot ** — Generates 15/30/60/90-second direct-response talking head video scripts (Facebook/Instagram/TikTok/YouTube style) using an Attention-Intensity-Possibility formula, targeted to 3-5 high-conversion audience segments identified from provided market materials.

- **Mode:** needs-input
- **Required inputs:**
  - **offer** (offer-details) — What's being sold or promoted: product, service, program, or event. ← *get it from:* user states the offer, or points to a sales/landing page
  - **audience** (buyer-profile) — Who the video should be targeting / who should be watching it. ← *get it from:* user describes the target viewer, or supplies a buyer-profile-type bot's output
  - **desired_action** (other:cta) — The action wanted from viewers: click a link, book a call, buy now, register, download something. ← *get it from:* user states the CTA goal
- **Optional inputs (raise quality):**
  - **market_materials** (buyer-profile) — Customer/market intelligence in any format — Build-a-Buyer docs, avatar profiles, market research, offer details, sales page URL, VSL script, sales copy ← *get it from:* user, or output of a buyer-profile/creative-brief-type bot; quality scales with richness but bot never refuses to produce output
  - **target_segments** (other:audience-segment) — Specific audience segments to write for; if omitted the bot identifies 3-5 high-conversion segments itself ← *get it from:* user
  - **script_lengths** (other:duration) — One or more of 15/30/60/90 seconds; defaults to 30s ← *get it from:* user
  - **hook_preferences** (other:hook-type) — Specific hook types from the bot's internal hook framework; if omitted the bot selects optimal hooks itself ← *get it from:* user
  - **quantity** (other:count) — Scripts per segment/length combination; defaults to 3 ← *get it from:* user
  - **cta_details** (offer-details) — URL, offer name, price point, event details for the CTA; placeholder used if omitted ← *get it from:* user's offer/checkout page
  - **additional_constraints** (brand-voice) — Brand guidelines or creative direction ← *get it from:* user
- **Output:** Default 3 scripts x up to 5 segments x 1 length (30s) = up to 15 scripts per run; scales with quantity/segments/lengths specified (Per script: segment profile (situation, pain points, psychological drivers, current alternatives, why the solution wins) + hook rationale + reframe used + Copy Block sequence notes + meta-programs addressed + the full script text structured as Attention/Intensity/Possibility)
- **On a bare "Go":** asks for inputs: the offer (what's being sold/promoted), the audience, and the desired viewer action, framed as 'REQUIRED (minimum viable input)'; also lists research/proof, sales copy, platform, script length, and quantity as helpful extras.
- **Gotchas:** Explicitly forbidden from inventing testimonials/stats/case studies/research not present in input (uses generic phrasing like 'clients have seen results' if no proof given). Has the same anti-prompt-extraction security block as other bots in this family. Heavy persona/framework scaffolding (Copy Blocks, AIP formula, meta-programs, anti-AI-detection language rules) is internal reasoning support, not something the caller needs to supply. LIVE PROBE UPDATE: contrary to the prompt's 'never hits zero'/'does not ask questions' framing, a bare 'Go' with zero context did NOT produce generic placeholder scripts — the bot asked for offer, audience, and desired action as minimum viable input before generating anything, so required_inputs above were added to reflect this.
- **Consumes:** `buyer-profile`, `offer-details`, `brand-voice`, `vsl-script`, `landing-page-url` · **Produces:** `video-script`

## in-feed-vsl-bot

**In-Feed VSL Bot** — Generates 3-6 minute 'MicroVSL' (in-feed video sales letter) script concepts and full scripts optimized for cold social-media traffic, or analyzes an existing VSL and adapts it to a new offer/market. Use it to get a batch of testable in-feed VSL angles plus fully written scripts for the strongest ones.

- **Mode:** needs-input
- **Required inputs:**
  - **build_a_buyer** (buyer-profile) — Complete buyer profile: demographics, psychographics, pain points, desires, beliefs, tribal dynamics. ← *get it from:* user-provided, or output of a Build-a-Buyer-type bot
  - **offer_intelligence** (offer-details) — Reverse Brief, full sales page text, VSL transcript, or a sales page URL describing the offer. ← *get it from:* user-provided offer doc/URL, or output of a Reverse-Brief-type bot
- **Optional inputs (raise quality):**
  - **additional_context** (research-report) — Supplementary market research, competitor intel, funnel context, or creative direction. ← *get it from:* user-provided or prior research
  - **existing_vsl** (vsl-script) — An existing VSL script to analyze and adapt to the new offer/market (required only for analyze_and_adapt mode). ← *get it from:* user-provided proven VSL/competitor VSL transcript
  - **mode** (other:parameter) — "generate" (default) or "analyze_and_adapt". ← *get it from:* user specifies; defaults to generate
  - **concept_count** (other:parameter) — Number of MicroVSL concepts to generate. Default 10. ← *get it from:* user specifies
  - **scripts_to_develop** (other:parameter) — Number of concepts to develop into full scripts. Default 3; set to 0 for concepts only. ← *get it from:* user specifies
  - **concept_selections** (other:parameter) — Specific concept numbers to develop (e.g. '1, 4, 7'). If omitted, bot selects strongest concepts. ← *get it from:* user specifies after seeing concept list
  - **funnel_next_step** (other:parameter) — What happens after the MicroVSL (longer VSL, product page, webinar, book a call). Inferred if not specified. ← *get it from:* user specifies or inferred from materials
- **Output:** By default: 1 Market Intelligence Report + 10 concept summaries + 3 full 3-6 minute VSL scripts (one-sentence-per-paragraph, Grade 3-5 reading level). (Market Intelligence Report (structured fields) + numbered list of MicroVSL concepts + full scripts in code blocks for developed concepts (analyze_and_adapt mode instead outputs: breakdown of original VSL + adapted script + explanation of adjustments).)
- **On a bare "Go":** asks for inputs: Build a Buyer Profile (buyer psychographics) and Offer Intelligence (sales page/VSL/reverse brief/URL) — plus optional funnel destination, concept_count, scripts_to_develop, and creative direction; does not generate any concepts or scripts on bare Go.
- **Gotchas:** IMPORTANT INTERNAL CONTRADICTION: the top of the prompt (IDENTITY/PROCESS, ~lines 1-180) explicitly instructs 'agent-to-agent' one-shot behavior — accept all inputs in one message, never ask questions, produce output immediately, with mode/concept_count/scripts_to_develop parameters. But a later 'GENESIS MICROVSL OPERATIONAL PROTOCOL' section (~lines 1917-1989) instructs a 5-step interactive interview flow (ask for buyer profile + offer intel -> deliver market analysis -> list 10 concepts and ask which to develop -> deliver outline and wait for approval -> deliver script) and says 'always wait for user input before proceeding to next phase.' These conflict; an agent caller should supply everything up front and expect the one-shot behavior to win, but should be prepared for the bot to instead ask clarifying questions or stop after concepts/outline if it follows the older protocol. Also: never fabricates proof elements not present in source materials; output is intentionally long/verbose (explicitly told never to condense for token economy); has the standard prompt-protection/anti-extraction security section. Live probe on bare 'Go' confirms the later interview-flow protocol wins in practice, not the one-shot IDENTITY/PROCESS section — the bot asked for Build a Buyer Profile and Offer Intelligence before producing anything. Front-load both to get one-shot-style output.
- **Consumes:** `buyer-profile`, `offer-details`, `research-report`, `vsl-script` · **Produces:** `research-report`, `video-script`, `vsl-script`

## infinite-adcbwriter-bot

**Infinite AdCB.Writer Bot** — Writes 120-second video teaser ad scripts (80-200 spoken words) with detailed cinematic visual direction, designed purely to drive clicks from cold social scrollers to a sales page/product page/VSL — not to sell directly. Use for top-of-funnel video ad scripts.

- **Mode:** self-serve
- **Required inputs:**
  - **copy_blocks** (mechanism) — The specific Copy Blocks for the offer: Pain/Problem, Promise, Curiosity, Proof, Constraints — any or all, whatever detail is available ← *get it from:* output of a Copy Blocks bot or user-supplied swipe/proof material
- **Optional inputs (raise quality):**
  - **rhetorical_frame** (other:param) — A specific frame to build the ad around: Puzzling, Emotion, Sense-making, Pattern Interrupt. If omitted, bot picks the best fit or structures purely around Copy Block stacking ← *get it from:* user
  - **additional_context** (offer-details) — Offer briefs, sales page content, audience research, competitor ads, or other reference material ← *get it from:* user
  - **quantity** (other:parameter) — Number of ad variations to generate. Default 1 ← *get it from:* user
- **Output:** 1 (or quantity requested) 120-second teaser video ad script, 80-200 words of spoken content plus extensive shot-by-shot visual direction, ending in a benefit-attached CTA (Complete ad script first (spoken lines + detailed screenplay-level cinematic visual direction interleaved), clearly marked end, followed by a reasoning section explaining the Rhetorical Frame(s), cinematic techniques, and Copy Block strategy used)
- **On a bare "Go":** generates immediately: a full ~120-sec teaser video ad script (VO + shot-by-shot cinematic visual direction) for an invented weight-loss supplement ("The Rice Water Secret"), explicitly labeled a demonstration since no copy blocks/offer/audience were supplied.
- **Gotchas:** Deliberately does NOT sell or explain the offer in the ad — its only job is generating curiosity/tension that resolves only by clicking. Every output includes a self-explanatory reasoning postscript (frame + technique breakdown) after the ad itself. Input is built around the 5 Copy Blocks framework (Pain/Problem, Promise, Curiosity, Proof, Constraints) so quality depends heavily on having a populated copy_blocks input; works with minimal input but degrades toward generic filler.
- **Consumes:** `mechanism`, `offer-details` · **Produces:** `video-script`

## micro-lead-bot-

**Micro-Lead Bot ** — Analyzes sales copy/product/audience materials through the 5 Copy Blocks (Pain/Problem, Promise, Curiosity, Proof, Constraints) and generates Micro Lead concepts (curiosity-driven 120-180s VSL/sales-letter openers) and/or fully scripted Micro Leads in a spoken-script + visual-instructions table. Use it when you need scroll-stopping VSL or advertorial openers for an existing offer.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **sales_copy** (landing-page-copy) — Sales letter, VSL script, sales page text, or a sales page URL to mine for emotional levers ← *get it from:* user's existing sales page/VSL script, or a landing-page-url they provide
  - **copy_blocks_emphasis** (other:copy-block-selection) — Which of the 5 Copy Blocks (Pain/Problem, Promise, Curiosity, Proof, Constraints) to emphasize ← *get it from:* user preference, or leave unset and let the bot choose
  - **product_details** (product-info) — What the product/service is and does ← *get it from:* user's product page or brand doc
  - **target_audience** (buyer-profile) — Demographics, psychographics, pain points of the target buyer ← *get it from:* user, or output of a buyer-profile-type bot
  - **rhetorical_frames** (other:rhetorical-frame) — Preferred rhetorical/engagement devices (e.g. 'puzzling', mystery, exposé) ← *get it from:* user preference; optional, bot has its own library of devices
  - **concept_direction** (angle-big-idea) — A specific concept/angle number or theme to develop into a full script (used after concepts have been generated) ← *get it from:* user selects from the bot's own numbered concept list in a prior turn
  - **generation_mode** (other:parameter) — 'concepts_only' / 'micro_lead_only' / 'concepts_and_micro_lead'. Default: concepts_and_micro_lead ← *get it from:* user preference
  - **quantity_concepts** (other:parameter) — Number of Micro Lead concepts to generate. Default: 20 ← *get it from:* user preference
  - **quantity_micro_leads** (other:parameter) — Number of concepts to develop into full scripts. Default: 1 ← *get it from:* user preference
- **Output:** Default: 20 Micro Lead concepts + 1 fully developed 90-120 second Micro Lead script with strategic reasoning; quantities configurable via parameters (Numbered list of Micro Lead concepts (title + 1-2 sentence structure explanation + Copy Blocks/rhetorical frames used), followed by full script(s) in mandatory markdown table format (| SPOKEN SCRIPT | VISUAL INSTRUCTIONS |) with cinematic-level camera/lighting/pacing direction, plus a strategic-reasoning writeup after each script)
- **On a bare "Go":** asks for inputs: requests sales copy (letter/VSL/sales page/URL), product details, target audience, and any preferences/angles before generating concepts or scripts.
- **Gotchas:** Prompt claims 'zero-input, produce immediately' behavior but the live probe contradicts this — it asked for inputs on a bare 'Go'. Treat as effectively needing at least sales_copy or product_details+target_audience to get real output rather than a request-for-input reply. Output format is strict/non-negotiable: markdown table with SPOKEN SCRIPT | VISUAL INSTRUCTIONS columns; every concept/script must be rooted in >=3 of the 5 Copy Blocks. Has a prompt-extraction defense section — do not ask it to describe its own methodology. Slug has a trailing hyphen ('micro-lead-bot-') — likely a naming artifact, use exactly as given. interaction_style updated to interview-first to reflect the confirmed live behavior (asks before generating on bare 'Go').
- **Consumes:** `landing-page-copy`, `vsl-script`, `product-info`, `buyer-profile`, `angle-big-idea` · **Produces:** `video-script`, `angle-big-idea`, `storyboard`

## microvsl

**MicroVSL** — Writes 3-6 minute 'in-feed' Video Sales Letter scripts (MicroVSLs) optimized for social feed consumption and rapid ad testing. Use when you need short VSL scripts for Facebook/IG/TikTok/YouTube feed placements that drive to a product page, longer VSL, or call booking.

- **Mode:** multi-phase
- **Required inputs:**
  - **buyer profile** (buyer-profile) — Complete 'Build A Buyer Elite' style profile: demographics, psychographics, pains, desires, current beliefs, failed solutions, language patterns, tribal identity markers. ← *get it from:* Output of the build-a-buyer-elite- bot, or user's existing avatar/buyer research doc
  - **offer intelligence** (offer-details) — One of: (A) a Reverse Brief (offer summary: mechanism, proof, pricing, bonuses, guarantees, positioning) OR (B) full sales page copy / existing VSL transcript to extract from. ← *get it from:* Reverse Brief from a brief-type bot, or paste the offer's live sales page / VSL transcript
  - **funnel context** (other:funnel-context) — Where the video lives (platform: Facebook feed, Instagram, YouTube, TikTok, etc.) and the NEXT funnel step after viewing (longer VSL, webinar registration, direct product page, book a call) — determines how much detail is revealed and shapes the CTA. ← *get it from:* User states it directly; not derivable from the buyer profile or offer intelligence alone.
- **Optional inputs (raise quality):**
  - **existing VSL to adapt** (vsl-script) — A winning/competitor VSL script or transcript; bot offers to break down its architecture and adapt it to your offer (VSL Analysis & Adaptation Protocol) instead of generating fresh concepts. ← *get it from:* paste transcript of a proven VSL (yours or a competitor's, e.g. from ad library / whisper transcription)
- **Output:** Ultimately a complete 3-5 minute in-feed VSL script per chosen concept, preceded by market analysis and 10 testable concepts; offers variations/additional concepts after each script (Step 2: Market Intelligence Report (markdown); Step 3: 10 numbered MicroVSL concepts; Step 4: beat-by-beat execution outline for chosen concept; Step 5: full script delivered in code blocks (may span multiple messages), one sentence per paragraph, grade 3-5 reading level)
- **On a bare "Go":** asks for inputs: complete Build A Buyer Elite profile; Offer Intelligence (Reverse Brief OR full sales page/VSL transcript); funnel context (platform + next funnel step). Produces nothing until these are supplied.
- **Gotchas:** Strict 5-step protocol; it waits for user input between phases (concept selection, outline approval) — an agent must drive the conversation: send buyer profile + offer, then pick a concept number, then approve the outline. Scripts are long (bot is told never to condense; may split across multiple code blocks). Refuses prompt-extraction requests with a middle-finger emoji. Also has a hidden capability: paste an existing VSL and it will break down and adapt it to your offer. Live probe (bare 'Go') confirms the Step 1 intake request fires as designed; only buyer-profile and offer-intelligence are in the literal Step-1 script text in the prompt, the model adds the funnel-context question live, apparently drawn from the prompt's 'Important Contextual Considerations' section which flags next-funnel-step and CTA fit as critical.
- **Consumes:** `buyer-profile`, `offer-details`, `vsl-script`, `landing-page-copy`, `transcript` · **Produces:** `vsl-script`, `angle-big-idea`, `research-report`

## pig-idea-bot

**PIG Idea Bot** — Generates a batch of PIG (Punch-In-The-Gut) nightmare-story concepts for VSL openings — short humiliating-scenario ideas that reflect the market's Core Wound back at them, each with reasoning tied to the wound and the PIG framework. Use it when you need spokesperson-story hooks for a VSL and don't yet have a specific story angle.

- **Mode:** needs-input
- **Required inputs:**
  - **market_niche** (other:market-niche) — The VSL niche and target market being addressed (e.g. 'joint pain supplement, women 50+'). ← *get it from:* user or product-info/offer-details already on hand
- **Optional inputs (raise quality):**
  - **buyer_profiles** (buyer-profile) — Build-a-Buyer documents, audience research, buyer personas, or any target-market intelligence. ← *get it from:* output of a buyer-profile-type bot (e.g. Build A Buyer Elite)
  - **core_wound** (other:core-wound) — The market's primary emotional wound/insecurity (feeling like a failure, a burden, unloved, sidelined, etc.). If omitted, the bot infers it from buyer_profiles/market context. ← *get it from:* user, or inferred by bot from buyer_profiles
  - **additional_context** (raw-notes) — Any additional marketing materials, copy blocks, offer details, or research. ← *get it from:* user, copy-blocks or offer-details from other bots
  - **quantity** (other:parameter) — Number of PIG Story ideas to generate. Default 15. ← *get it from:* user
- **Output:** Default 15 PIG story concepts (spokesperson-humiliation nightmare scenarios), each with rationale — not full VSL copy, just concept-level ideas ready to be written up as PIG stories (Numbered list of story ideas; each idea is a short narrative concept plus a reasoning note referencing the Core Wound and PIG framework)
- **On a bare "Go":** asks for inputs: requests market_niche (required), plus optional buyer_profiles, core_wound, and additional_context, before generating PIG story ideas.
- **Gotchas:** Only true requirement is some notion of market_niche; everything else (core_wound especially) is inferred if missing. Output is concept/idea level, not full prose stories — pair with a VSL/script bot to expand a chosen idea into full copy. Has the standard prompt-protection/security block appended (ignore for behavior analysis). Live probe (bare 'Go') contradicts the prompt's 'never asks questions, infers Core Wound if sparse' framing and the prior one-shot classification: the bot asked for market_niche and other materials rather than inventing a generic niche/wound.
- **Consumes:** `buyer-profile`, `raw-notes`, `offer-details` · **Produces:** `other:pig-story-ideas`

## ums-bot

**UMS BOT** — Writes the Unique Mechanism of the Solution (UMS) section of a video sales letter — the narrative that reveals the differentiated, logical solution flowing from a prior Unique Mechanism of the Problem (UMP) — as a drop-in copy block for a larger VSL script.

- **Mode:** needs-input
- **Required inputs:**
  - **audience_identification** (buyer-profile) — Target audience profile — who the copy is speaking to. ← *get it from:* user-provided buyer/avatar doc, or output of a buyer-profile-type bot
  - **copy_blocks_and_pain_matrix** (creative-brief) — Copy blocks, pain matrix, and/or core wound information — the pain points and language the solution needs to resolve. ← *get it from:* user-provided pain matrix/research doc, or output of a pain-point research bot
  - **speaker_background_and_credibility** (other:speaker-bio) — The spokesperson's general background, credentials, personality, and perspective. Copy must be written from this real person's POV — the bot will not invent a guru or dialogue that doesn't exist. ← *get it from:* user-provided bio/credibility doc for the actual speaker/spokesperson of the VSL
  - **ums_preview** (mechanism) — The UMS trigger — the initial discovery narrative hook (e.g., how the spokesperson stumbled onto the mechanism). ← *get it from:* user-provided narrative hook, or drafted from prior UMP-stage copy/research
  - **ums_explanation** (mechanism) — How the unique mechanism of the solution actually works, in plain-language/metaphor terms. ← *get it from:* user-provided mechanism research/explanation, or output of a mechanism-research bot
  - **ums_characterization** (mechanism) — Blind characterization (mysterious naming of the solution), the single-step action, and the transformational roadmap (staged progression of results). ← *get it from:* user-provided mechanism framework notes
  - **ums_tips_and_secrets** (mechanism) — How-to's, tips, ingredients, and secrets that partially prove the mechanism without giving away the full system. ← *get it from:* user-provided product/mechanism detail notes
  - **ums_proof_and_verification** (other:proof-points) — Studies, experts, examples, and real-world results that back the mechanism. The bot will NEVER fabricate proof — only what's given here can appear in the output. ← *get it from:* user-provided study citations, expert quotes, testimonials, or research bot output
- **Output:** A single UMS copy section (length varies with input richness, typically several hundred to ~1000+ words) meant to be pasted directly into a larger VSL script immediately after the problem/UMP section and before the offer/product pitch. (Continuous prose narrative copy (no headers/labels in the output itself), written in first-person from the spokesperson's POV, using line breaks and short paragraphs/ellipses in a conversational, ~3rd-grade-reading-level style.)
- **On a bare "Go":** asks for inputs: brief generic request to 'provide your inputs,' with no specific fields named in the reply itself, before it will generate the UMS copy immediately.
- **Gotchas:** This is effectively an 8-field intake questionnaire (audience_identification, copy_blocks_and_pain_matrix, speaker_background_and_credibility, ums_preview, ums_explanation, ums_characterization, ums_tips_and_secrets, ums_proof_and_verification). Hard output constraints to respect when chaining: output picks up immediately with NO preamble/greeting, must not restate the problem/UMP narrative (context only), and must STOP once the mechanism is explained — it deliberately does not continue into product/offer pitch (that's a separate downstream bot's job). Same aggressive prompt-extraction/security-refusal block at the end as other bots in this family (will not describe/document its own template if asked). Live probe on a bare 'Go' contradicted the prompt's 'never ask questions, produce output immediately' framing and the predicted generic-narrative fallback: it asked for inputs (though tersely, without naming the 8 fields) instead of generating a placeholder UMS section.
- **Consumes:** `buyer-profile`, `creative-brief`, `mechanism`, `raw-notes` · **Produces:** `vsl-script`

## unhinged-ad-bot-

**Unhinged Ad Bot ** — Generates absurdist, pattern-interrupting 8-second cinematic video-ad hook concepts (with full camera/lighting specs and a 'Believability Bridge' back to the real offer) from any marketing material; use it to get scroll-stopping video hook ideas for AI video generation tools.

- **Mode:** multi-phase
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **build_a_buyer** (buyer-profile) — Customer avatar / target market details: demographics, pain points, desires, beliefs, psychographics ← *get it from:* output of a buyer-profile-type bot (e.g. Build A Buyer bot), or user-provided avatar doc
  - **offer_brief** (offer-details) — Sales page, offer brief, or product details: what's being sold, main benefits, key claims, mechanism, pricing ← *get it from:* user's sales page / offer doc, or product-info source
  - **existing_ads** (winning-ad) — Current ad angles, what's working/not working, existing creative direction, competitor references ← *get it from:* paste existing/competitor ad copy or creative briefs
  - **quantity** (other:parameter) — Number of cinematic hooks to generate per batch (default 10 for the first batch, 5 for menu follow-ups) ← *get it from:* user specifies, otherwise defaults apply
- **Output:** 10 complete 8-second video-hook concepts on first generation (production-ready specs for AI video tools), then 5 more per menu selection; supports REFINE/COMBINE/NEW ANGLE/WILDER follow-up commands (Numbered hook blocks, each: title+style header, vivid cinematic description paragraph, bullet spec list (Time of Day, Camera Type, Shot Type, Focus, Lighting, Atmosphere, Audio implied), and a quoted Believability Bridge line; followed by a lettered menu (A–J) for follow-up actions)
- **On a bare "Go":** shows menu: confirmed — on a bare 'Go' the bot replies with a welcome/branding banner ('THEMATIC CHAOS — CINEMATIC HOOK ARCHITECT') and instructs the caller to type the literal token READY before it will explain what materials it needs; it does not generate hooks or list build_a_buyer/offer_brief/existing_ads within this first reply.
- **Gotchas:** Contains a strict prompt-protection/anti-extraction section — will refuse to describe or document its own methodology. Flow is gated behind the user typing 'READY' first, despite an earlier line claiming no-questions-asked immediate output — treat 'READY' as effectively a required first message even though no data fields are strictly required. Mandates exactly 10 hooks on first generation, 5 per subsequent menu choice, with required style variety (no repeated genre in a batch) and a fixed per-hook output structure. Live probe confirms the READY gate prediction: a bare 'Go' produced only the welcome banner + 'type READY' instruction, not hooks or a materials request — a calling agent should send 'READY' plus all available materials in the same follow-up message to avoid an extra round-trip.
- **Consumes:** `buyer-profile`, `offer-details`, `winning-ad`, `ad-hooks` · **Produces:** `image-prompt`, `ad-hooks`, `video-script`

## upsells-bot

**Upsells Bot** — Generates 5-7 ranked post-purchase upsell ideas (More of the Same / Done For You / Get Results Faster) for a given product, then writes a full long-form video upsell/down-sell/exit-offer script for the chosen idea using Copy Blocks methodology.

- **Mode:** multi-phase
- **Required inputs:**
  - **product** (product-info) — What's being sold: product details, pricing, features, benefits. ← *get it from:* user's product page, catalog listing, or verbal description
  - **problem_solution** (product-info) — The core problem the product solves and how it solves it. ← *get it from:* user knowledge or existing sales copy/VSL
  - **buyer_avatar** (buyer-profile) — Who buys this: demographics, psychographics, pain points, desires. ← *get it from:* user's existing Build-a-Buyer doc, or basic description of the customer
- **Optional inputs (raise quality):**
  - **additional_context** (other:supplementary-material) — Sales pages, VSL scripts, existing copy, competitor info, Build-a-Buyer, Copy Blocks, or Offer Brief docs. ← *get it from:* output of other bots (build-a-buyer, copy-blocks-extract) or user's existing marketing assets
  - **output_mode** (other:parameter) — "ideas_only" / "ideas_and_script" / "script_only". Default: ideas_and_script. ← *get it from:* user specifies, else default is used
  - **script_type** (other:parameter) — "video_upsell" / "down_sell" / "exit_offer". Default: video_upsell. ← *get it from:* user specifies, else default is used
  - **upsell_selection** (other:parameter) — Which of the 5-7 ranked upsell ideas to script, by rank number or description. Default: top-ranked idea. ← *get it from:* user picks after seeing the ranked idea list, or default top idea is scripted
- **Output:** A ranked upsell idea list plus one complete persuasive video script (purchase acknowledgment, bridge, upsell pitch, value/urgency build, guarantee, hard CTA) for a one-time-offer page. (First a ranked list of 5-7 upsell ideas (each labeled with category + brief rationale for conversion/AOV), then a full long-form (11-15+ min) video upsell script built from Copy Blocks (Pain/Problem, Promise, Curiosity, Proof, Constraints) for the selected idea.)
- **On a bare "Go":** asks for inputs: product info (what's sold, pricing, features), the problem/solution the product addresses, and buyer avatar (demographics, pain points, desires) — before producing any upsell ideas or script.
- **Gotchas:** Prompt is internally inconsistent: the top IDENTITY/PROCESS section says 'accept all inputs in a single message... do not ask questions or request additional information,' but the OUTPUT rule later ('first provide ideas, then ask which upsell they want a script for') and 'Start by asking for their product information' both instruct it to ask. After any script it also proactively asks 'Would you like me to verify this uses Copy Blocks effectively and sounds completely human?' Also applies a strict 'Anti AI Module' (banned words/patterns) to keep scripts sounding human — could reject/rewrite output that lands on forbidden phrasing if re-prompted. LIVE PROBE UPDATE: a direct probe of this exact slug (not just the sibling 'upsell-bot') now confirms the bot asks for product/problem/buyer info on a bare Go rather than producing output — superseding the earlier cross-slug inference.
- **Consumes:** `product-info`, `buyer-profile`, `offer-details`, `vsl-script`, `landing-page-copy`, `competitor-info` · **Produces:** `video-script`, `ad-hooks`

## video-adscript-bot

**Video Adscript Bot** — Generates 5 distinct 45-60s (default) direct-response talking-head video ad scripts for Meta/YouTube from whatever marketing materials it's given, each using a different angle/hook, ready for an actor to read.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **marketing_materials** (other:mixed-marketing-materials) — Any combination of Build-a-Buyer (buyer profile), Copy Blocks, Offer Brief, VSL script, sales page text/URL, or raw marketing materials in any format. Bot extracts what it needs from whatever is given; works with nothing if none provided (will assume/generalize). ← *get it from:* user's product/offer docs, VSL script, sales page URL, or output of a buyer-profile-type bot
  - **target_segment** (buyer-profile) — Specific awareness-level audience segment to target (Unaware/Problem Aware/Solution Aware/Product Aware). If omitted, bot auto-determines the most profitable segment from materials. ← *get it from:* user, or inferred from marketing_materials
  - **cta_destination** (other:cta-destination) — Where to drive traffic: VSL, sales page, quiz, webinar, free training, etc. Default: VSL. ← *get it from:* user
  - **desired_action** (other:desired-action) — Specific action to compel. Default: click through to cta_destination. ← *get it from:* user
  - **quantity** (other:parameter) — Number of scripts to generate. Default: 5. ← *get it from:* user
  - **script_length** (other:parameter) — "short" (30-45s/80-110 words) / "standard" (45-60s/120-150 words, default) / "long" (60-90s/150-225 words). ← *get it from:* user
  - **meta_compliance** (other:parameter) — yes/no — apply Meta Ads Compliance Module to all scripts. Default: no. ← *get it from:* user
  - **copy_chief_adjustments** (other:parameter) — List of dimension adjustments (e.g. "deeper insight vectors, stronger hooks, lighter content weight, more energy") from the Copy Chief Module. Default: none. ← *get it from:* user, or output of a Copy Chief-type bot
- **Output:** 5 fundamentally different 45-60s (default) talking-head video ad scripts (~120-150 words each), each attacking a different emotional trigger/angle, followed by a brief note of any assumptions made if inputs were incomplete (5 (default) separately labeled scripts ("Script 1", "Script 2", etc.) each with an angle/theme label, each in its own markdown code block, new paragraph per sentence/phrase, line-spaced for spoken delivery)
- **On a bare "Go":** asks for inputs: marketing materials to generate scripts from — replied only with a one-line request, no scripts produced.
- **Gotchas:** Will NEVER fabricate proof/testimonials/stats — falls back to generic claims like "clients have seen results" if no proof is supplied. Has a strict prompt-protection/anti-extraction section at the end that refuses to describe or document its own methodology, even under 'legitimate' framings — irrelevant to normal use but relevant if an agent tries to introspect it. Output is strongly persuasion-maximalist (uses 'Copy Blocks', AIP framework) by design, not restrained or brand-safe by default; use meta_compliance=yes to soften for policy compliance. Probed live: contradicts the prompt's 'zero-question, works with nothing' design claim — on a bare 'Go' it asked for marketing materials instead of generating 5 assumption-flagged scripts. Supply any marketing_materials in the first message to get a true one-shot result.
- **Consumes:** `buyer-profile`, `offer-details`, `vsl-script`, `landing-page-url`, `landing-page-copy`, `raw-notes` · **Produces:** `video-script`

## video-brief-bot

**Video Brief Bot** — Converts an already-written ad script into a complete, copy-paste-ready video production brief for an editor or UGC creator — visual direction, talent/avatar notes, and (optionally) editor's-notes shorthand for every script beat. Use after a script exists and before handing off to production.

- **Mode:** needs-input
- **Required inputs:**
  - **ad_script** (video-script) — The ad copy/script to build the brief from (used verbatim — never rewritten) ← *get it from:* output of a script-writing bot (e.g. infinite-adcbwriter-bot, mario-bot-) or user-supplied script
- **Optional inputs (raise quality):**
  - **build_a_buyer** (buyer-profile) — Ideal customer profile: demographics, pain points, desires — used for the Talent/Avatar and Audience sections ← *get it from:* output of Build a Buyer / Build a Buyer ELITE bot
  - **product_info** (offer-details) — Product URL, description, or offer details ← *get it from:* user
  - **platform** (other:param) — Where the ad runs: Meta, TikTok, YouTube, etc. ← *get it from:* user
  - **ad_type** (other:param) — UGC, talking head, product demo, testimonial, listicle, or AI/motion graphics. If omitted, inferred from the script; defaults to UGC if it can't be inferred ← *get it from:* user
  - **goal** (other:param) — Purchases, sign-ups, leads, etc. ← *get it from:* user
  - **brief_type** (other:param) — "open" (no Editor's Notes column filled) / "specified" (every beat gets editor shorthand notes). Default: specified ← *get it from:* user
- **Output:** One complete production brief per script provided; multiple scripts produce multiple ad blocks in the same brief. Missing fields are marked [Not provided] rather than omitted (Single markdown document inside a triple-backtick code block: Header (Product/Offer/Goal/Audience/Concept Type/Platform/Duration/Aspect/Product URL) -> Talent/Avatar section (if on-camera) -> Ad Block(s) with a Script|Visual|Editor's Notes markdown table (one row per script beat: Hook 1/2/3, Body lines, CTA) -> Quick Notes -> Tone & Style Notes -> Reference Ads placeholder)
- **On a bare "Go":** asks for inputs: the ad script at minimum; optionally product info, audience, platform, ad type, goal — did not emit a [Not provided]-filled template without the script.
- **Gotchas:** Never rewrites/improves the script — issues are flagged in the Editor's Notes column, not fixed. Never invents additional hooks beyond what's given in ad_script. One script beat per table row, never grouped. Two output modes (open vs specified) controlled entirely by brief_type param. Best paired downstream of a script-writing bot like infinite-adcbwriter-bot or mario-bot-, and upstream nothing further needed — this is a terminal/handoff-ready output. Live probe (bare 'Go', no script attached) contradicts the 'produces output immediately, marks missing fields [Not provided]' claim above: the bot asked for the ad script instead of emitting a mostly-empty brief template; interaction_style updated to reflect this gating behavior.
- **Consumes:** `video-script`, `buyer-profile`, `offer-details` · **Produces:** `storyboard`

## vsl-bot

**VSL Bot** — Writes complete 10-20 minute video sales letter scripts calibrated to market motivation direction, sophistication, proof quality, and traffic temperature. Also analyzes an existing VSL script's converting structure and can adapt it to a new market/offer.

- **Mode:** needs-input
- **Required inputs:**
  - **market_information** (buyer-profile) — Target audience description: emotional state, achievement level, sophistication signals, core desires/fears, primary objections ← *get it from:* user's market research or output of a buyer-profile-type bot (e.g. Build-a-Buyer)
  - **offer_information** (offer-details) — Product/service description, transformation promise, delivery mechanism, price point, proof elements, required action, end goal ← *get it from:* user's offer brief / product page
- **Optional inputs (raise quality):**
  - **environmental_factors** (other:market-conditions) — Traffic temperature, market awareness, competition level, risk factors, proof requirements, decision timeline ← *get it from:* user's media buyer / campaign context
  - **expert_brand_position** (brand-voice) — Strongest credentials, notable client results, key differentiators of the spokesperson/brand ← *get it from:* user's brand doc or about page
  - **cta_goal** (offer-details) — Desired action (direct sale, book call, lead gen) and next funnel step ← *get it from:* user's funnel plan
  - **additional_context** (research-report) — Supplementary materials: Build-a-Buyer output, Copy Blocks, Offer Brief, research, competitor examples, existing sales copy, reference VSLs ← *get it from:* outputs of buyer-profile / copy-blocks / research bots, or pasted docs
  - **existing_vsl** (vsl-script) — An existing VSL script; providing it switches the bot into Mode 2 (analysis & adaptation) ← *get it from:* paste a competitor's or prior VSL script / transcript
  - **analysis_scope** (other:parameter) — Mode 2 only: 'breakdown' | 'elements' | 'adapt' | 'all' (default: all) ← *get it from:* caller decides
- **Output:** One full-length (10-20 minute) VSL script engineered around a framework selected from its internal pattern library; never truncated. (Complete VSL script in code block(s), one sentence per paragraph, grade level 1-5 reading. Mode 2 outputs a structural breakdown (pattern type, beat map, proof sequencing) plus an adapted full script if market/offer info is given.)
- **On a bare "Go":** asks for inputs: market/audience information, offer/product details, price point, proof elements, traffic source, and desired action (or any existing copy) — no VSL script is produced until given this context.
- **Gotchas:** Agent-optimized: accepts everything in one message, never asks questions — starving it of input yields an invented product/market rather than an error. Providing an existing VSL script silently switches it to analysis/adaptation mode (analysis-only if no target market/offer is included). Output always arrives in code blocks; long scripts span multiple sequential code blocks. maxTokens 32000 — a full VSL can approach this, so avoid bundling multiple asks in one call. Probe contradicts the prior prediction of a fully invented generic VSL script on bare 'Go' — the bot instead states it needs market/offer/context info first. interaction_style updated from one-shot to interview-first.
- **Consumes:** `buyer-profile`, `offer-details`, `product-info`, `brand-voice`, `research-report`, `vsl-script`, `transcript` · **Produces:** `vsl-script`

## youtube-script-bot

**Youtube Script Bot** — Turns a YouTube video idea (plus any optional context) into a complete, retention-engineered spoken script (or outline) of a target length, with hooks, 3 mandatory CTAs, a credibility beat, and no visible timestamps. Use it when you have a video concept and want a ready-to-record script rather than strategic advice.

- **Mode:** needs-input
- **Required inputs:**
  - **video_idea** (content-topic) — The video topic or idea. This is the only truly required field — everything else is optional and the bot infers/defaults when missing. ← *get it from:* user
- **Optional inputs (raise quality):**
  - **video_length** (other:duration) — Target duration, e.g. '10 minutes'. Default: 10 minutes. ← *get it from:* user
  - **most_interesting_element** (angle-big-idea) — The single most remarkable/interesting thing about the topic — the 3-second scroll-stop hook material. ← *get it from:* user or derived from research on the topic
  - **credibility_reason** (brand-voice) — Why the creator is credible on this topic (experience, results, research, lived story). ← *get it from:* user
  - **credibility_statement** (brand-voice) — "I'm [name], and [specific credential]" — 1-2 sentences max, woven into script (never copied verbatim). ← *get it from:* user
  - **specific_content** (content-topic) — Exactly what's covered — named tools/methods, listed ideas/concepts, or the story beats. ← *get it from:* user
  - **best_evidence** (customer-reviews) — Best example, result, story, data, or research proving the point. ← *get it from:* user or research
  - **unique_opinion** (angle-big-idea) — Creator's actual contrarian take / what most people get wrong. ← *get it from:* user
  - **content_breakdown** (content-topic) — 3-5 main points/steps/parts in order. ← *get it from:* user
  - **viewer_outcome** (offer-details) — What viewers will know/be able to do after watching. ← *get it from:* user
  - **audience_knowledge_level** (buyer-profile) — everyone / some_knowledge / experts_only. Default: everyone. ← *get it from:* user
  - **tone_of_voice** (brand-voice) — Desired tone, e.g. 'high energy', 'caring friend', 'tough love teacher'. ← *get it from:* user
  - **target_emotion** (brand-voice) — Emotion viewers should feel (inspired, angry, curious, entertained). ← *get it from:* user
  - **tone_of_voice_guide** (brand-voice) — Written voice guidelines/style reference for the creator. ← *get it from:* user's brand voice doc, or output of a brand-voice-type bot
  - **build_a_buyer** (buyer-profile) — Target audience profile. ← *get it from:* output of a buyer-profile-type bot
  - **youtube_strategy** (other:channel-strategy) — Overall channel strategy context. ← *get it from:* user
  - **previous_script** (video-script) — A previously generated script to be revised instead of generating fresh. ← *get it from:* prior output of this same bot
  - **output_type** (other:parameter) — 'script' / 'outline_only' / 'outline_and_script'. Default: script. ← *get it from:* user
  - **humor_level** (other:parameter) — 1-10 scale, 5 default. ← *get it from:* user
  - **information_density** (other:parameter) — 1-10 scale, 6 default. ← *get it from:* user
  - **energy_pace** (other:parameter) — calm/moderate/high. Default moderate. ← *get it from:* user
  - **hook_intensity** (other:parameter) — soft/moderate/strong. Default strong. ← *get it from:* user
  - **voice_style** (other:parameter) — casual/professional/match_voice_guidelines. Default casual. ← *get it from:* user
  - **anti_ai_level** (other:parameter) — standard/maximum. Default maximum. ← *get it from:* user
  - **adjustment_instructions** (other:parameter) — Free-text revision instructions, e.g. 'make it shorter and funnier', applied to previous_script if given, else used as generation guidance. ← *get it from:* user
- **Output:** One complete spoken-word YouTube script (or outline) sized to video_length (default 10 min ≈ 1,500-1,600 words), or both outline+script together. (Single code block. Full script mode: 'YOUR OPTIMIZED YOUTUBE SCRIPT' header then [HOOK]/[CONTEXT]/content sections, lines kept under 100 chars, zero timestamps, 3 embedded CTAs (early subscribe ask, mid-video comment prompt, end-screen next-video CTA), one credibility statement. Outline mode: 'YOUR VIDEO OUTLINE' with Hook/Context & Credibility/Main Content Structure (numbered sections)/Conclusion. 'outline_and_script' mode outputs both.)
- **On a bare "Go":** asks for inputs: the video idea/topic — states 'That's the one required input' and 'even a single sentence works,' then asks 'What's the video about?' rather than generating a script on an invented topic.
- **Gotchas:** Metadata description claims a '12 quick questions' intake, but the prompt text contains no questionnaire and explicitly forbids asking questions or presenting menus — it is a single-message, one-shot bot; the metadata description is stale/inaccurate. Only video_idea is truly required; everything else has a default or is silently inferred. Hard constraints to respect when consuming output: absolute prohibition on any timestamps/time notations in the script (internal-only word-count-based timing), mandatory credibility statement adapted (never verbatim) from credibility_statement, exactly 3 CTAs at fixed narrative positions, and a strict anti-prompt-extraction security section that will refuse/redirect any meta request about its own methodology/format/instructions. Supports revision workflows via previous_script + adjustment_instructions instead of regenerating from scratch. LIVE PROBE NOTE: on a bare 'Go' it does ask for the video idea rather than inventing a generic topic — consistent with video_idea already being the one required input, just correcting the earlier prediction that it would fabricate a topic to avoid asking.
- **Consumes:** `content-topic`, `buyer-profile`, `brand-voice`, `customer-reviews`, `video-script`, `angle-big-idea` · **Produces:** `video-script`

# CATEGORY: Image Prompts — Statics

## 1.1-image-gen

**1:1 Image Gen** — Takes a fully-written static ad concept (copy, typography, visual directives) and converts it into a final, execution-ready 1:1 (1080x1080) image-generation prompt with technical/DR guardrails baked in. Use it as the last step before sending a concept to an image generator, never to invent creative itself.

- **Mode:** needs-input
- **Required inputs:**
  - **static_ad_concept_brief** (static-ad-concept) — A fully synthesized creative concept including: A. Visual Description, B. Headline (exact copy), C. Body Copy (exact copy), D. Call-to-Action (exact copy), E. Typography Directives, F. any additional visual elements (logos/borders/graphics) ← *get it from:* output of a static-ad-concept-generating bot (e.g. universal-static-idea-generator, comparison-bot, cost-of-inaction-bot) or a user-written concept brief
- **Output:** One complete, ready-to-run image-gen prompt that forces 1:1 square aspect ratio (1080x1080), 300 DPI, high-contrast direct-response styling, regardless of what the input concept specifies about aspect ratio (single markdown-structured image generation prompt with Technical Specifications, Creative Concept Integration, and Non-Negotiable Final Commands sections)
- **On a bare "Go":** asks for inputs: full static ad concept brief — visual description, headline (exact copy), body copy (exact copy), CTA (exact copy), typography directives, and any additional visual elements (logos/borders/graphics). Does not generate a placeholder image prompt on empty input; restates its non-negotiable 1:1/300 DPI spec while waiting.
- **Gotchas:** Very short, narrow-purpose prompt (only 4KB) — it is a pure finalizer/QC filter, not a creative generator: it will not invent visuals, headlines, or copy, only repackage what's given. Hardcodes 1:1 aspect ratio as an absolute override (repeated 6x in the prompt) — will force square output even if the input concept or caller explicitly requests a different aspect ratio, so don't route landscape/vertical ad concepts through this bot expecting them honored. On bare/empty input it asks for the brief rather than guessing. Probe confirms interview-first behavior: on bare 'Go' it asks for the concept brief rather than one-shotting a placeholder prompt, contradicting a literal 'one-shot' label — interaction_style updated to interview-first to reflect this.
- **Consumes:** `static-ad-concept` · **Produces:** `image-prompt`

## animation-bot

**Animation Bot** — Generates illustration-driven static ad concepts where the illustration itself is the scroll-stopping hook (not the headline) — for problems that are invisible/internal/hard to photograph (health, relationships, finance); use when photography feels too clinical, restricted, or generic for the offer.

- **Mode:** needs-input
- **Required inputs:**
  - **Build a Buyer** (buyer-profile) — Target market profile. ← *get it from:* output of a build-a-buyer type bot, or user's existing avatar doc
  - **Copy Blocks** (ad-copy) — Proven copy elements and messaging. ← *get it from:* output of a copy-blocks-extract type bot, or user's swipe file
  - **Offer Brief** (offer-details) — Product/service details, positioning, differentiators. ← *get it from:* output of an offer-brief type bot, or user's product page
  - **Sales Copy** (other:sales-copy) — VSL script, sales page text, or a sales page URL. ← *get it from:* user pastes VSL script/sales page text or provides a URL
- **Optional inputs (raise quality):**
  - **quantity** (other:parameter) — Number of concepts to generate. Default: 5. ← *get it from:* user specifies, else defaults to 5
- **Output:** Default 5 illustrated ad concepts distributed across 3 hook lenses (Condition/Symptom Depiction, Relatable Scene/Situation, Conceptual Visualization), each specifying illustration style (flat vector, medical/anatomical, line art, warm lifestyle, bold/graphic, retro), ready for a designer or illustrator. (Numbered concepts (Concept 1, Concept 2, ...), each in its own code block, with fields: HOOK EXTRACTION (which of the 3 lenses used and why), VISUAL IDEA, ILLUSTRATION STYLE, LAYOUT NOTES, COLOR NOTES, HEADLINE (only if used), WHY THIS WORKS)
- **On a bare "Go":** asks for inputs: requests at least one of Build a Buyer, Copy Blocks, Offer Brief, or Sales Copy (VSL script/sales page text/URL); states it will generate concepts immediately once any are provided.
- **Gotchas:** Distinct from multi-testimonial-bot-: doesn't need or use customer quotes at all — pulls hook material from the avatar's problem, not from reviews. Output is creative direction (visual idea + style + reasoning) for a human illustrator/designer, not a literal image-generation prompt string. Same prompt-extraction/security guard section as the other bots in this set. Live probe (bare 'Go') contradicts the prompt's 'never hits zero' framing and the prior one-shot classification: the bot asked for input materials rather than generating placeholder concepts from stock tropes.
- **Consumes:** `buyer-profile`, `ad-copy`, `offer-details`, `vsl-script`, `landing-page-copy`, `landing-page-url` · **Produces:** `static-ad-concept`

## bold-typography-bot

**Bold Typography Bot** — Generates bold, text-led static ad concepts where large confident typography (not product photography) is the visual hero. Use when you want quick static-ad concepting for a brand that wants a commanding, minimalist, type-forward look.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **buyer_profile** (buyer-profile) — "Build a Buyer" — target market profile. ← *get it from:* output of a buyer-profile-type bot, or user's audience research doc
  - **copy_blocks** (swipe-example) — Proven copy elements and swipe material to mine for punchy phrases/headlines. ← *get it from:* user's swipe file, or output of a copy/hook-generation bot
  - **offer_brief** (offer-details) — Product/offer details. ← *get it from:* user's offer brief, or output of an offer-brief-type bot
  - **sales_copy** (vsl-script) — VSL script, sales page text, or a sales page URL to extract strong statements/benefits/hooks from. ← *get it from:* user pastes VSL/sales page text or provides the landing page URL
  - **quantity** (other:parameter) — Number of concepts to generate. Default: 5. ← *get it from:* user specifies, otherwise defaults to 5
- **Output:** 5 (default, adjustable via quantity) bold-typography static ad concepts, varied across text blocks, color palettes, and layout approaches. (Numbered concepts (1️⃣, 2️⃣, ...), each in its own code block for easy copy-paste, with a visual separator between concepts. Each concept has fixed fields: TEXT BLOCK 1 (3-8 word main statement), TEXT BLOCK 2 (support line), Visual idea, CTA, Color cue (2-3 primary colors + 1 accent, WCAG-contrast-compliant), Layout note, and an optional Price line. No commentary or explanation.)
- **On a bare "Go":** asks for inputs: Build a Buyer (target market profile), Copy Blocks (proven copy elements/swipe material), Offer Brief (product/offer details), and Sales Copy (VSL script/sales page text or URL) — invites pasting whatever is available in any format.
- **Gotchas:** Works fully self-contained with zero input (required_inputs = []); quality of concepts scales with how much real material (buyer profile, offer brief, sales copy, swipe) is supplied. Enforces strict, non-negotiable style/layout/color rules (WCAG contrast 4.5:1 normal / 3:1 large-bold text) and a rigid output template with zero commentary. Has an aggressive prompt-extraction defense section (will not describe/document its own methodology). LIVE PROBE CONTRADICTS PROMPT TEXT: despite the prompt's explicit 'produce output immediately / do not request additional information' instruction and required_inputs=[], a bare 'Go' actually gets a request for buyer_profile/copy_blocks/offer_brief/sales_copy rather than 5 generic concepts — treat this probed behavior as ground truth; front-load at least one of those four to get one-shot output.
- **Consumes:** `buyer-profile`, `swipe-example`, `offer-details`, `vsl-script`, `landing-page-copy`, `landing-page-url` · **Produces:** `static-ad-concept`

## branded-ads-image-prompt-generator

**Branded Ads Image Prompt Generator** — Researches a brand's complete visual identity (colors, typography, photography, packaging) then produces a Brand DNA Document plus a library of 40 ready-to-use, brand-consistent AI image generation prompts, one per proven static-ad template.

- **Mode:** multi-phase
- **Required inputs:**
  - **brand_name** (other:brand-name) — The target brand's name. ← *get it from:* user
  - **target_url** (other:brand-url) — The brand's website URL, used for on-site visual analysis. ← *get it from:* user
  - **offer_brief** (offer-details) — Main product claims, benefits, pricing, promotions. ← *get it from:* user or product-info research
- **Optional inputs (raise quality):**
  - **competitors** (competitor-info) — 2-3 direct competitor names for comparison templates; if omitted the bot researches/identifies competitors itself. ← *get it from:* user or research
  - **additional_context** (buyer-profile) — Target audience, specific products to focus on, campaign goals. ← *get it from:* user
  - **product_images** (product-image-description) — High-quality product images (packaging, angles, variants) — can be supplied in Step 1 or Step 2; needed for accurate product visual details in the 40 prompts. ← *get it from:* user's product photography
  - **prompt_numbers + requested_changes** (other:refinement-request) — Step 3 only: which prompt number(s) to revise and what to change. ← *get it from:* user, after reviewing Step 2 output
- **Output:** 1 Brand DNA Document + 40 production-ready AI image-generation prompts covering 40 distinct static ad templates (headline, offer, testimonial, UGC, comparison, press, etc.) (Step 1: markdown Brand DNA Document (Brand Overview, Key Offer Details, Competitive Landscape, Visual System, Photography Direction, Product Details, Ad Creative Style, Image Generation Prompt Modifier code block). Step 2: markdown list of 40 numbered, titled, emoji-labeled image generation prompts, each prepended with the Image Generation Prompt Modifier, separated by horizontal rules.)
- **On a bare "Go":** asks for inputs: brand_name, target_url, offer_brief (required); competitors, additional_context, product_images (optional) — states it will begin Step 1 (Brand Research) then Step 2 (40 image prompts) once provided
- **Gotchas:** Three-step bot: Step 1 (brand_name+target_url+offer_brief -> Brand DNA Document via live web research + site visit), Step 2 (Brand DNA + product_images -> 40 templated image prompts), Step 3 (revise specific numbered prompts). Steps can be chained in one message. Strong anti-fabrication rule: must state clearly when brand info isn't found rather than inventing it (except generic placeholders like 'Other [category] brands' if no competitor given). Every one of the 40 prompts must be prepended with the same 'Image Generation Prompt Modifier' paragraph for visual consistency. File has duplicated content (headers like '40 AD TEMPLATES LIBRARY', 'DOMAIN KNOWLEDGE', 'EXAMPLES' each appear twice — likely a copy-paste artifact in the stored prompt, worth flagging to whoever maintains bot prompts).
- **Consumes:** `product-info`, `offer-details`, `competitor-info`, `buyer-profile`, `product-image-description` · **Produces:** `image-prompt`, `brand-voice`, `static-ad-concept`

## breakingauthority-transformer-bot-

**Breaking/Authority Transformer Bot ** — Generates broadcast/news-style static ad concepts (breaking-news lower third, stacked news card, live/on-air, special report, wildcard) that frame the offer with urgency and borrowed authority — without naming real institutions or fabricating data. Use when you want 'this just in' style urgency creative for an offer/product.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Target market profile ← *get it from:* user's existing buyer profile, or output of a buyer-profile-type bot
  - **Copy Blocks** (ad-copy) — Key messaging/proof points ← *get it from:* user paste, or output of a copy-blocks-extract-type bot
  - **Offer Brief** (offer-details) — Product/offer details, mechanism, differentiators ← *get it from:* user paste, or output of an offer-brief-type bot
  - **Sales Copy** (landing-page-copy) — VSL script, sales page text, or sales page URL ← *get it from:* user paste or URL
  - **specific numbers/sources/timeframes** (other:proof-data) — Any real numbers, named sources, or timeframes present in the materials — if supplied, the bot reuses them verbatim; if absent, it substitutes soft non-falsifiable market language (e.g. 'surging', 'this week') ← *get it from:* pull directly from user's provided offer brief / sales copy
  - **quantity** (other:quantity) — Number of concepts; default 5. Each set of 5 = 4 broadcast variants + 1 Wildcard/Collider; non-multiples of 5 fill remaining slots with broadcast variants ← *get it from:* user specifies in the same message; defaults to 5 if omitted
- **Output:** Default 5 (or requested quantity) broadcast-style news/authority-framed static ad concepts (Broadcast/Lower Third, Stacked News Card, Live/On-Air, Special Report, plus 1 Wildcard/Collider per 5). (Fixed structure per concept, in its own code block: HEADLINE, SUBHEADLINE, VISUAL DESCRIPTION, LAYOUT/COMPOSITION NOTES, COLOR/STYLE NOTES, CTA (Optional). Numbered 1️⃣–5️⃣ etc., last of each set of 5 always the Wildcard/Collider variant.)
- **On a bare "Go":** asks for inputs: at least one of Build a Buyer / Copy Blocks / Offer Brief / Sales Copy; states it will generate immediately once any one of these is dropped in.
- **Gotchas:** Hard safety layer: never names real institutions/regulators (Fed, FDA, BLS, SBA, etc.) unless the user explicitly supplied that source, never fabricates numbers/timeframes/compliance claims, and never implies legal/tax/medical requirements — defaults to soft market-momentum language when inputs lack specifics. Output format is mandatory and fixed (HEADLINE/SUBHEADLINE/VISUAL DESCRIPTION/LAYOUT/COLOR/CTA) — no adaptive omission of fields like the sign bot allows. Same anti-prompt-leak / self-referential-task-refusal security section as the other two bots in this batch. LIVE PROBE CONTRADICTION: despite the system prompt's claim that it 'does not ask questions,' a bare 'Go' with zero context produced a request for at least one of the four named inputs rather than a generated concept set — so treat it as requiring at least one input, not truly zero-input one-shot.
- **Consumes:** `buyer-profile`, `ad-copy`, `offer-details`, `landing-page-copy`, `landing-page-url`, `vsl-script` · **Produces:** `static-ad-concept`, `image-prompt`

## carousel-static-ads

**Carousel Static Ads** — Generates multi-frame carousel/story ad concepts (LinkedIn sliders, IG carousels, swipe-to-read stories, product tiles) in sets of 5 (4 structured concepts + 1 wildcard), each with per-frame headline/text, visual description, and layout notes ready to hand to a designer or image tool.

- **Mode:** needs-input
- **Required inputs:**
  - **source material** (other:mixed) — At least one of: Build a Buyer, Copy Blocks, Offer Brief, or Sales Copy (VSL script/sales page text/URL). Raw ad text alone is also accepted as sole input. ← *get it from:* user's existing docs, output of a buyer-profile-type bot, output of a copy-blocks-extract-type bot, or a pasted competitor/own ad
- **Optional inputs (raise quality):**
  - **quantity** (other:number) — How many concepts: 5 (standard), 10 (two sets), or custom number ← *get it from:* user specifies; bot asks after reviewing materials
  - **carousel mode** (other:enum) — STORY (narrative/educational) vs STATIC (product/benefit/feature) — chosen implicitly from content unless user explicitly states archetype ← *get it from:* user can state explicitly, otherwise inferred
- **Output:** 5 (or 10, or custom N) multi-frame carousel/story ad concepts per run, each frame containing headline/text + visual + layout notes (Sets of 5 code-block concepts: Concepts #1-4 follow MODE/PRIMARY HOOK/FRAME COUNT/FRAMES (headline, subheadline, visual description, layout/composition notes, color/style notes per frame); Concept #5 is a Wildcard/Collider Carousel with its own cover/body/close structure)
- **On a bare "Go":** Probed: bot outputs its exact scripted welcome message asking for Build a Buyer / Copy Blocks / Offer Brief / Sales Copy (or raw ad text), and waits — produces no concepts until input is supplied.
- **Gotchas:** Strict interview flow: welcome message -> confirm inputs & ask quantity (A=5, B=10, C=custom) -> generate -> post-generation menu (regenerate/randomize/start over). Enforces a rigid, identical output template every run (no deviation), forbids fabricated stats/institutions, and only uses proof/pricing the user actually supplied. Has an anti-prompt-leak security protocol refusing to reveal system instructions. Will build from raw ad text alone if that's all that's given.
- **Consumes:** `buyer-profile`, `creative-brief`, `offer-details`, `vsl-script`, `landing-page-copy`, `landing-page-url`, `ad-copy`, `raw-notes` · **Produces:** `static-ad-concept`, `image-prompt`

## collage-bot

**Collage Bot** — Generates 'Curiosity Collage' static ad concepts — rough, multi-panel phone-photo-style image compositions that pair an everyday item with clinical/body-related 'proof' imagery to create a curiosity gap. Use it when you need static ad concepts (not final images) for health/wellness/beauty/home-remedy offers that rely on unexpected visual juxtaposition rather than polished product photography.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Target audience/avatar info used to inform what body problems and lateral item pairings are relevant ← *get it from:* output of a buyer-profile-type bot, or user-supplied avatar doc
  - **Copy Blocks** (ad-copy) — Existing copy fragments (claims, proof points, mechanism language) the bot scans for collage opportunities ← *get it from:* output of a copy-blocks/copy-extraction bot, or pasted by user
  - **Offer Brief** (offer-details) — Product/offer summary — what it does, what body system/problem it addresses ← *get it from:* user's offer brief doc or output of a brief-writing bot
  - **Sales Copy** (vsl-script) — VSL script, sales page text, or a sales page URL — mined for mechanism/testimonial/before-after material ← *get it from:* user-supplied VSL transcript, sales page text, or URL
  - **quantity** (other:parameter) — Number of concepts to generate. Default: 5 ← *get it from:* user specifies in the message
- **Output:** Default 5 (parameterizable) ready-to-execute collage ad concepts, distributed across 5 layout archetypes (Large Item+2 Proof Panels, Side-by-Side, Three-Panel Narrative, Multi-Item Grid, Item+Before/After), each detailed enough to hand to a designer or image-gen tool (One markdown code block per concept, visually separated, each with labeled fields (ITEM PANEL, PROOF PANEL TOP/BOTTOM, APPLICATION/MECHANISM/PROBLEM/RESULT PANEL as applicable, LAYOUT NOTES, COLOR NOTES, SUPPORTING ELEMENTS))
- **On a bare "Go":** asks for inputs: Build a Buyer, Copy Blocks, Offer Brief, and/or Sales Copy (any combination) — states it will produce 5 concepts immediately once given something, but does not generate placeholder concepts on a truly bare 'Go'.
- **Gotchas:** Never asks clarifying questions and never flags missing/incomplete inputs — will fabricate concepts even with zero context, so quality is highly dependent on what's fed in. Actively resists obvious item-to-proof pairings (won't pair a knee supplement with a knee X-ray); pushes for lateral/absurd connections instead. Has a hardcoded prompt-extraction defense section refusing to reveal/summarize/document its own instructions or methodology under any framing. Probe contradicts the prior prediction: on a genuinely empty message the bot asks for at least one of its four input types rather than fabricating concepts from nothing. interaction_style updated from one-shot to interview-first.
- **Consumes:** `buyer-profile`, `ad-copy`, `offer-details`, `vsl-script`, `landing-page-copy`, `landing-page-url` · **Produces:** `static-ad-concept`, `image-prompt`

## commentreview-transformer-bot-

**Comment/Review Transformer Bot ** — Generates static ad concepts styled as platform-native reviews/comments/chat threads (Amazon, Reddit, Instagram, YouTube, App Store, Slack, Quora, etc.) that turn testimonials and proof points into scroll-stopping native-looking content. Use when you want social-proof creative disguised as organic UI screenshots rather than obvious ads.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Target market profile: demographics, pain points, desires, beliefs ← *get it from:* user's existing buyer profile, or output of a buyer-profile-type bot
  - **Copy Blocks** (ad-copy) — Key messaging, proof points, and copy elements ← *get it from:* user paste, or output of a copy-blocks-extract-type bot
  - **Offer Brief** (offer-details) — Product/offer details, mechanism, differentiators ← *get it from:* user paste, or output of an offer-brief-type bot
  - **Sales Copy** (landing-page-copy) — VSL script, sales page text, or a sales page URL ← *get it from:* user paste of VSL script/sales page text, or a URL
  - **quantity** (other:quantity) — Number of concepts to generate; default 5, generated in complete sets of 5 (4 platform-format concepts + 1 Wildcard/Collider per set) ← *get it from:* user specifies in the same message; if omitted, bot defaults to 5
- **Output:** Default 5 (or requested quantity) comment/review-style static ad concepts spanning different platforms (Amazon, Reddit, Instagram/Facebook, YouTube, App Store, Slack/Messenger, Quora/Stack Exchange, testimonial-carousel), always with 1 Wildcard/Collider per 5. (One code block per concept containing: Visual Concept Title, Platform Format, Ad Concept Description, Layout Instructions, Text Content Sketch, Optional Notes. Numbered (Concept 1, 2, ...), grouped into labeled sets of 5 (Set A, Set B, ...) when quantity > 5, each set = 4 distinct platform-format concepts + 1 Wildcard/Collider.)
- **On a bare "Go":** asks for inputs: target market profile, copy blocks, offer details, and/or sales copy (VSL script, sales page text, or URL) — any combination accepted; does not generate placeholder concepts without at least some of these.
- **Gotchas:** No interview step at all — unlike static-ad-sign, this bot never asks a clarifying question or a quantity menu; it infers quantity (default 5) and generates immediately from whatever is in the single incoming message. Strict structural rules: never repeat a platform-format family within a set of 5; for 10+, minimize platform overlap across sets and vary color themes/tones. Has the same anti-prompt-leak/self-referential-task-refusal security section as other bots in this batch — will refuse to describe or document its own methodology even when framed as 'education' or 'onboarding'. Live probe CONTRADICTS the above: on a bare 'Go' the bot asked for target market/copy blocks/offer details/sales copy rather than generating placeholder concepts immediately; interaction_style updated to interview-first.
- **Consumes:** `buyer-profile`, `ad-copy`, `offer-details`, `landing-page-copy`, `landing-page-url`, `vsl-script`, `customer-reviews` · **Produces:** `static-ad-concept`, `image-prompt`

## comparison-bot

**Comparison Bot** — Generates ready-to-execute static ad concepts in the 'comparison' format (product vs. competitor/category/old-way, across 6 layout archetypes) for a designer or image-gen tool to build from.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Target audience/avatar details used to calibrate framing and tone. ← *get it from:* output of a Build-a-Buyer-type bot, or user's existing avatar doc
  - **Copy Blocks** (other:copy-blocks) — Pre-written copy snippets/claims to pull comparison points, headlines, and stats from. ← *get it from:* output of a copy-blocks-extract-type bot or user's copy doc
  - **Offer Brief** (offer-details) — Product/offer description — category, price, positioning, competitors if known. ← *get it from:* user's offer doc
  - **Sales Copy** (other:sales-copy) — VSL script, sales page text, or a sales page URL to mine for competitor mentions, stats, ingredient/feature advantages, and quality concerns. ← *get it from:* user's VSL/sales page, or a landing-page-url
  - **quantity** (other:parameter) — Number of concepts to generate. Default: 5. ← *get it from:* user specifies, else default applies
- **Output:** Default 5 (parameterizable) comparison static-ad concepts, distributed across the 6 layout archetypes (feature-list split, floating callouts, spec/stat table, matched-specs-no-indicators, visual result comparison, hybrid visual+table) with varied framing (generic category/named/semi-named competitor/personal identity/quality binary) and varied winner indicators. (Numbered concepts (Concept 1, Concept 2, ...), each in its own code block, using adaptive fields: COMPARISON FRAMING, HEADLINE, VISUAL IDEA, "THEM" SIDE, "US" SIDE, WINNER INDICATORS, LAYOUT NOTES, COLOR NOTES (only fields relevant to that concept are included).)
- **On a bare "Go":** asks for inputs: Build a Buyer, Copy Blocks, Offer Brief, or Sales Copy (VSL/sales page/URL), in any combination — or raw ad text pasted alone
- **Gotchas:** Fully self-contained generator — required_inputs is empty; can even run on raw ad text alone with no other details. All four named inputs (Build a Buyer, Copy Blocks, Offer Brief, Sales Copy) are optional and additive — quality scales with how much is provided but it never blocks on missing info. Explicitly avoids inventing stats/competitor names not present in materials — feed it real specifics to get non-generic comparisons. Has the same strong prompt-protection/anti-extraction guard as other bots in this family. Model: claude-sonnet-4-6, maxTokens 32000. LIVE PROBE CONTRADICTION: despite the prompt's 'never ask questions, always produce output' rule, a bare 'Go' actually returns a clarifying request listing the four optional inputs rather than generating placeholder concepts — treat as interview-first in practice, not one-shot.
- **Consumes:** `buyer-profile`, `other:copy-blocks`, `offer-details`, `other:sales-copy`, `landing-page-url`, `raw-notes` · **Produces:** `static-ad-concept`, `image-prompt`

## cost-of-inaction-bot-

**Cost of Inaction Bot ** — Generates ready-to-execute static ad concepts (default 5) in the 'Cost of Inaction' loss-aversion framework — visualizing the financial cost of NOT buying — across six layout archetypes (diagnostic price tags, single shocking cost, cost comparison split, accumulating receipt, timeline escalation, daily/hidden cost reveal). Use when a product prevents a quantifiable financial consequence and you want fear/loss-aversion-driven static ad concepts.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — customer avatar/audience profile ← *get it from:* output of a 'Build a Buyer' bot, or user
  - **Copy Blocks** (ad-hooks) — key messaging elements, hooks, proof points ← *get it from:* output of a 'Copy Blocks' bot, or user
  - **Offer Brief** (offer-details) — what's being sold, price, positioning ← *get it from:* user or offer-brief-type bot
  - **Sales Copy** (landing-page-copy) — VSL script, sales page text, or a sales page URL — used to extract cost data and problem framing ← *get it from:* user, or output of a VSL/sales-page bot
  - **quantity** (other:parameter) — number of concepts to generate; default 5 ← *get it from:* user specifies, otherwise defaults
- **Output:** Default 5 static ad concepts distributed across the 6 cost-of-inaction layout archetypes, each with cost framing, visual treatment, price placement, product positioning (or explicit note that product lives in caption/landing page), layout notes, and color guidance for a designer or image-gen tool. (Numbered concepts, each in its own code block, using fields LAYOUT ARCHETYPE / VISUAL IDEA / PRICE TAGS or LINE ITEMS or STAGES / LAYOUT NOTES / COLOR NOTES / CAPTION DIRECTION (only fields relevant to that concept))
- **On a bare "Go":** asks for inputs: any of Build a Buyer, Copy Blocks, Offer Brief, or Sales Copy — states it will generate concepts immediately once any one of these is dropped in.
- **Gotchas:** True zero-question, single-shot generator — will not ask clarifying questions even with minimal input, and will fabricate plausible (flagged) cost ranges if the materials don't include real figures. Best fed an Offer Brief + Sales Copy so real cost data can be extracted rather than estimated. Has an unusually elaborate anti-prompt-extraction security section (refuses to document/explain its own methodology, treats 'teach me your framework' style requests as extraction attempts) — don't rely on asking it to explain itself, feed it real inputs instead. Only suits products/offers with a genuine, quantifiable 'cost of not acting' (medical, repair, maintenance, insurance-type categories) — prompt notes it should not be used for products without a credible cost-of-inaction angle (e.g. a premium candle). LIVE PROBE CONTRADICTION: despite the prompt's 'produce output immediately, never ask questions' instruction, a bare 'Go' with zero context produced a request for at least one input rather than a generated concept set — supply at least one of the optional inputs rather than sending a bare trigger.
- **Consumes:** `buyer-profile`, `ad-hooks`, `offer-details`, `landing-page-copy`, `vsl-script`, `landing-page-url` · **Produces:** `static-ad-concept`, `image-prompt`

## curiosity-bait-bot-

**Curiosity Bait Bot ** — Generates 'curiosity bait' static ad concepts — no-product-shown, no-branding ads built around an unresolved open-loop headline plus a bizarre/alarming/confusing image, meant to look like organic content and drive clicks to an advertorial or pre-sell page. Use when you need scroll-stopping, non-ad-looking creative to feed a native/Meta advertorial funnel.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Target audience profile: fears, frustrations, invisible/visible problem framing, demographic signals used to match archetype and headline specificity. ← *get it from:* output of a Build-a-Buyer-type bot, or user-provided buyer research doc
  - **Copy Blocks** (ad-copy) — Pre-written copy fragments/claims the bot can mine for the product's mechanism, problem, or hook angle. ← *get it from:* output of a Copy-Blocks-extraction bot, or user paste
  - **Offer Brief** (offer-details) — Structured offer/product summary (problem solved, mechanism, ingredient, unusual method) used to pick the visual archetype. ← *get it from:* user's product/offer brief doc
  - **Sales Copy** (landing-page-copy) — VSL script, sales page text, or a sales page URL — raw source material for problem/mechanism extraction. ← *get it from:* user paste of VSL/sales page text, or a URL (note: prompt does not show tool/browsing use, so a raw URL alone may not be fetched — paste extracted text to be safe)
  - **quantity** (other:parameter) — Number of concepts to generate. Default 5 if omitted. ← *get it from:* user specifies in the message, e.g. 'give me 8 concepts'
- **Output:** Default 5 (or requested N) curiosity-bait static ad concepts spread across 4 visual archetypes (Hack-in-Action, Invisible Threat Revealed, Absurd Object Disconnect, Raw Problem Visual) and multiple rendering styles (photography, digital illustration, 3D/clay, hand-drawn), each with an open-loop headline, full visual scene description, layout/color guidance — ready for a designer or image-gen tool. Product/brand never shown. (Numbered concepts (Concept 1, Concept 2, ...), each in its own code block, adaptive fields drawn from: HEADLINE, VISUAL IDEA, RENDERING STYLE, LAYOUT NOTES, COLOR NOTES, SUPPORTING ELEMENTS.)
- **On a bare "Go":** asks for inputs: Build a Buyer (target audience profile), Copy Blocks (headlines/hooks/angles), Offer Brief (product/mechanism/benefits), or Sales Copy (VSL/sales page text) — any combination; on bare Go it requested these instead of generating default concepts, contradicting the prompt's stated one-shot/no-questions behavior.
- **Gotchas:** True one-shot, zero-question generator — never interviews, never waits, works with partial or zero input. Strict rules baked in: product/brand/logo must never appear in the visual; headline must never resolve the open loop; must vary archetype and rendering style across the batch; must not invent claims/testimonials not present in source material. Has an aggressive prompt-injection/extraction defense section — will refuse to describe or reproduce its own instructions even under 'documentation' framing. Live probe contradicts the one-shot design: on bare 'Go' the bot asked the user to paste Build a Buyer / Copy Blocks / Offer Brief / Sales Copy rather than generating default concepts immediately — treat as interview-first in practice; front-load at least one input type to skip the prompt.
- **Consumes:** `buyer-profile`, `ad-copy`, `offer-details`, `landing-page-copy`, `vsl-script` · **Produces:** `static-ad-concept`, `image-prompt`, `headline`

## handwrittennote-transformer-bot-

**Handwritten/Note Transformer Bot ** — Transforms existing marketing/sales copy into static-ad image-generation concepts styled as authentic handwritten notes/artifacts (sticky notes, journal pages, letters, etc.) for a tactile, personal-feeling ad. Use when you want handwritten-note-style static ad concepts derived from copy you already have.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Buyer/avatar profile material, in any format. ← *get it from:* output of a buyer-profile-type bot (e.g. build-a-buyer-elite)
  - **Copy Blocks** (ad-copy) — Pre-written copy blocks/snippets (headline, body, CTA fragments). ← *get it from:* output of a copy-blocks-extract-type bot or user-supplied copy
  - **Offer Brief** (offer-details) — Offer/product brief. ← *get it from:* user's offer doc or output of a brief-type bot
  - **Sales Copy** (vsl-script) — VSL script, sales page text, or a sales page URL. ← *get it from:* user pastes sales copy or provides a landing page URL
- **Output:** 5 static-ad image-generation concepts by default (quantity overridable), each simulating a physical handwritten artifact (sticky note, notebook page, journal spread, scrap/napkin, letter/parchment, desk scene, posted note, or a hybrid 'Collider' composition). (Numbered concepts 1-5 (5th always a 'Collider' wildcard variant), each in its own code block with fixed fields: CONCEPT TITLE, VISUAL DESCRIPTION, TEXT LAYOUT NOTES, COLOR NOTES, IMAGE ASSET NOTE.)
- **On a bare "Go":** asks for inputs: Build a Buyer, Copy Blocks, Offer Brief, or Sales Copy (any combination) before generating handwritten-note ad concepts
- **Gotchas:** Not a copywriting generator — it's an image-concept generator that must preserve any supplied copy verbatim ('Preserve all user-provided copy exactly', 'Never invent headlines or phrases'). Best fed the output of a copy/offer/buyer bot rather than run standalone. Quantity param defaults to 5 (4 structural variants + 1 mandatory Collider) and is overridable. Designed for agent-to-agent chaining downstream of copy-generation bots. Live probe (bare 'Go') contradicts the 'never asks questions, produces output immediately' framing — the bot's actual first reply was a request for Build a Buyer / Copy Blocks / Offer Brief / Sales Copy, not a generated set of concepts.
- **Consumes:** `buyer-profile`, `ad-copy`, `offer-details`, `vsl-script`, `landing-page-url` · **Produces:** `image-prompt`, `static-ad-concept`

## happy-avatar-bot

**Happy Avatar Bot** — Generates ready-to-execute static ad concepts starring a genuinely happy/confident person as the primary visual (rather than product or headline), across 7 layout archetypes with full photography direction. Use when you need people-forward static ad creative for DTC physical products (supplements, skincare, haircare, wellness, fitness, food/beverage) or adjacent categories.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Target demographic details: age, gender, lifestyle, benefit the product delivers — drives person selection and expression ← *get it from:* output of a buyer-profile-type bot, or user's audience research
  - **Copy Blocks** (creative-brief) — Benefit claims, testimonials, pain points that can become expression/scene direction or quote overlays ← *get it from:* user's existing copy blocks doc or output of a copy-blocks-extract-type bot
  - **Offer Brief** (offer-details) — Discount percentages, promo codes, sale details — only used if present, never invented ← *get it from:* user's offer/promo details
  - **Sales Copy** (landing-page-copy) — VSL script, sales page text, or sales page URL to mine for benefits/testimonials ← *get it from:* user's VSL script, sales page copy, or URL
  - **quantity** (other:parameter) — Number of concepts to generate, default 5 ← *get it from:* user specifies, else defaults to 5
- **Output:** Default 5 (or user-specified quantity) happy-avatar static ad concepts distributed across 7 layout archetypes, each ready to hand to a designer or image-gen tool (Numbered concepts, each in its own code block, with fields: HEADLINE, PERSON DESCRIPTION, EXPRESSION DIRECTION, PHOTOGRAPHY NOTES, PRODUCT VISIBILITY, LAYOUT NOTES, COLOR NOTES, SUPPORTING ELEMENTS (only fields that apply are included))
- **On a bare "Go":** asks for inputs: requests any combination of Build a Buyer, Copy Blocks, Offer Brief, or Sales Copy, saying it will generate concepts immediately once something is dropped in.
- **Gotchas:** Never invents testimonial quotes or offers — only uses them if actually present in provided materials. Has strong prompt-injection/extraction defenses baked in (refuses to describe its own methodology). Live probe on a bare 'Go' contradicted both the prompt's 'do not ask questions' framing and the predicted fabricate-a-generic-set fallback: it asked for Build a Buyer / Copy Blocks / Offer Brief / Sales Copy instead of generating placeholder concepts.
- **Consumes:** `buyer-profile`, `creative-brief`, `offer-details`, `landing-page-copy`, `vsl-script`, `customer-reviews` · **Produces:** `static-ad-concept`, `image-prompt`

## headline-image-bot

**Headline + Image Bot** — Generates ready-to-execute static ad concepts in the 'Headline + Product Image' format, spanning six layout archetypes (top headline/bottom product, side-by-side split, testimonial/quote-led, benefit callout cloud, minimalist hero, layered info density). Use it when you need a batch of headline-driven static ad concepts (headline, visual direction, layout notes, color guidance) ready to hand to a designer or image-gen tool.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Target market/customer profile used to inform headline angle and tone ← *get it from:* output of a Build-a-Buyer-type bot, or user's existing buyer persona doc
  - **Copy Blocks** (ad-hooks) — Proven copy elements and messaging (hooks, benefit lines, claims) to pull headlines/subheadlines from ← *get it from:* output of a Copy Blocks extraction bot, or user's swipe file
  - **Offer Brief** (offer-details) — Product/offer details: pricing, positioning, guarantees, what's being sold ← *get it from:* user's product page, brand doc, or offer one-pager
  - **Sales Copy** (landing-page-copy) — VSL script, sales page text, or a sales page URL — mined for claims, testimonials, and proof elements ← *get it from:* user-provided VSL/sales page text, or a landing-page-url the agent fetches
  - **quantity** (other:parameter) — Number of concepts to generate; default 5 if not specified ← *get it from:* user specifies, or omit for default
- **Output:** Default 5 (configurable via quantity) ready-to-execute static ad concepts distributed across the six layout archetypes, each with everything a designer or image-gen tool needs to produce the final ad (Numbered concepts (Concept 1, Concept 2, ...), each in its own code block, using adaptive fields: HEADLINE, SUBHEADLINE, VISUAL IDEA, PRODUCT PLACEMENT, LAYOUT NOTES, COLOR NOTES, PRICE DISPLAY, CTA, SUPPORTING ELEMENTS (only fields that apply per concept are included))
- **On a bare "Go":** asks for inputs: Build a Buyer (target market profile), Copy Blocks (proven messaging/hooks), Offer Brief (product details/pricing/positioning), and Sales Copy (VSL/sales page text or URL) — invites pasting whatever is available in one message.
- **Gotchas:** Embeds a large chunk of unrelated 'STATIC AD FORMAT RECOMMENDER' domain-knowledge/reference text (21-format profiles and a different bot's recommendation logic, lines ~36-296) inside the prompt between the actual bot identity and its own example library — appears to be shared reference material bleeding into this prompt rather than describing this bot's own behavior; the bot's real identity/process is only lines 1-34 plus the example library and formatting/guidelines after 'END OF DOMAIN KNOWLEDGE' (line 295) through the end. Never invents testimonials, product claims, or benefits not present in supplied materials. Has a heavy prompt-extraction/self-referential-task refusal section at the end (security boilerplate, not behaviorally relevant to normal use). LIVE PROBE CONTRADICTS PROMPT TEXT: despite the 'do not ask questions/produce output immediately' instruction and required_inputs=[], a bare 'Go' actually gets a request for Build a Buyer/Copy Blocks/Offer Brief/Sales Copy rather than 5 generic concepts — treat this probed behavior as ground truth; front-load at least one of those four to get one-shot output.
- **Consumes:** `buyer-profile`, `ad-hooks`, `offer-details`, `landing-page-copy`, `vsl-script`, `landing-page-url`, `customer-reviews` · **Produces:** `static-ad-concept`, `image-prompt`, `headline`

## hero-bot-

**Hero Bot ** — Generates HERO-type static ad concepts (product and/or person showcased with strong composition/clarity) in sets of 5 archetypes — 2 Command Hero (authority/clarity), 2 Stealth Hero (native lifestyle / UGC), 1 Wildcard/Collider pattern-breaker — each with headline, CTA, price, and a detailed image asset note ready to hand to a designer or image-gen tool.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **build_a_buyer** (buyer-profile) — Build a Buyer profile for audience targeting ← *get it from:* output of a Build-a-Buyer-type bot
  - **copy_blocks** (other:copy-blocks) — Copy Blocks (promises, pains, proof, etc.) to draw headline/subheadline/proof content from ← *get it from:* output of a Copy Blocks extraction bot
  - **offer_brief** (offer-details) — Offer Brief covering product, price, CTA ← *get it from:* user's offer documentation or an Offer Brief bot
  - **sales_copy** (other:sales-copy-or-url) — VSL script, sales page text, or a sales page URL to mine for benefits/proof/visual angles ← *get it from:* user's existing VSL/sales page, or a URL
  - **quantity** (other:parameter) — Number of concepts to generate; default 5, generated in complete sets of 5 (2 Command Hero, 2 Stealth Hero, 1 Wildcard), partial sets fill in fixed order ← *get it from:* user specifies; defaults to 5
- **Output:** Default 5 HERO static ad concepts (image-gen/designer-ready), scalable to any quantity in complete sets of 5, each set spanning Command/Stealth/Wildcard archetypes with enforced visual variety across color, lighting, framing, and composition. (One code block per concept with fixed fields: HEADLINE, SUBHEADLINE, CTA, PRICE, VISUAL IDEA, COLOR CUE, LAYOUT NOTE, STYLE NOTE, IMAGE ASSET NOTE (with mandatory ASSET TYPE + DETAIL line); numbered/emoji-labeled and grouped into Set A/B etc. for >5 concepts)
- **On a bare "Go":** asks for inputs: Build a Buyer, Copy Blocks, Offer Brief, or Sales Copy (VSL/sales page/URL), in any combination, in one message
- **Gotchas:** Rigid mandatory output schema (Section 10) — must not deviate. Includes a 'Human Realism Integrity Protocol' for when a person appears (likeness fidelity rules, rotating lighting/realism variants). Strong anti-redundancy rules across multiple sets (no repeated palette/composition/proof tag). Gotcha: despite the prompt claiming zero-question one-shot behavior and a placeholder fallback, the live bot actually asks for at least one input up front on an empty message — any combination of the 4 listed inputs works, but an agent should supply at least one rather than sending a bare trigger.
- **Consumes:** `buyer-profile`, `creative-brief`, `offer-details`, `vsl-script`, `landing-page-copy`, `landing-page-url` · **Produces:** `static-ad-concept`, `image-prompt`

## holding-sign-bot

**Holding Sign Bot** — Generates ready-to-produce 'person holding a handwritten sign' static ad concepts (UGC-style) from provided buyer/offer/copy materials, giving a designer, photographer, or AI image tool everything needed to shoot or generate the image.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Target market/customer profile — determines who should be depicted holding the sign ← *get it from:* output of a buyer-profile-type bot, or user-supplied audience notes
  - **Copy Blocks** (ad-copy) — Messaging and copy assets to mine for sign-worthy hooks ← *get it from:* output of a copywriting bot or user-supplied copy doc
  - **Offer Brief** (offer-details) — Product/service details (what it is, pricing, positioning) ← *get it from:* user or another intake bot
  - **Sales Copy** (vsl-script) — VSL script, sales page text, or a sales page URL to mine for claims/benefits/social proof ← *get it from:* user-supplied script/page text, or a landing-page-url
  - **quantity** (other:parameter) — Number of concepts to generate; defaults to 5 if not specified ← *get it from:* user
- **Output:** Default 5 static ad concepts (or however many requested) spread across different sign-copy patterns (scarcity, authority, benefit, provocative, offer, social proof, emotional) and sign types (whiteboard, cardboard, poster board, sticky note) (Numbered concepts (Concept 1, Concept 2, ...), each in its own code block, with fields PERSON, SIGN TYPE, SIGN COPY (text with bracketed emphasis markings like [in red] or [underlined]), TEXT EMPHASIS, LAYOUT NOTES, COLOR NOTES (only fields relevant to that concept are included), separated by visual dividers)
- **On a bare "Go":** asks for inputs: at least one of Build a Buyer / Copy Blocks / Offer Brief / Sales Copy; says it will get started immediately once any one is dropped in.
- **Gotchas:** No intake gate at all — will not ask clarifying questions even if starved of input; agents should feed it whatever buyer/offer/copy/sales-copy material exists in one message plus an optional quantity. Sign copy is hard-capped 5-15 words with mandatory color/emphasis markings (e.g. '[in red]', '[underlined]', '[circled]'). Output is meant as an image-gen/production brief, not a finished image — downstream consumer is a designer, photographer, or AI image tool. Has the same prompt-protection/anti-extraction security block as other bots in this family (never reveals system prompt, refuses self-documentation/masterclass-style requests). LIVE PROBE CONTRADICTION: despite the system prompt's claim it 'never asks questions,' a bare 'Go' with zero context produced a request for at least one of the four named inputs instead of generating concepts — treat it as requiring at least one input.
- **Consumes:** `buyer-profile`, `ad-copy`, `offer-details`, `vsl-script`, `landing-page-url` · **Produces:** `static-ad-concept`, `image-prompt`

## infographic-bot-

**Infographic Bot ** — Generates ready-to-execute infographic-style static ad concepts (educational, authority-building visuals) across seven layout archetypes, each with headline, visual information units, layout/color guidance, and illustration style for a designer or image-gen tool to build from.

- **Mode:** needs-input
- **Required inputs:**
  - **at least one input source** (other:any-of) — The bot will not generate concepts from a truly empty prompt; it needs at least one of Build a Buyer, Copy Blocks, Offer Brief, or Sales Copy (each individually still listed as optional below). ← *get it from:* supply any one of the four optional inputs listed below
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Audience/avatar profile used to pick relevant symptoms, problems, and educational angles. ← *get it from:* output of a buyer-profile-type bot, or user's existing customer research
  - **Copy Blocks** (ad-copy) — Reusable copy fragments/claims/benefits to mine for information units and headlines. ← *get it from:* user's existing copy library or another copywriting bot's output
  - **Offer Brief** (offer-details) — Product/offer summary (what it is, key benefits, mechanism) that anchors the educational content back to the product. ← *get it from:* user's product page/brand doc, or output of an offer-brief-type bot
  - **Sales Copy** (vsl-script) — VSL script, sales page text, or a sales page URL — mined for symptoms, processes, comparisons, ingredients, frameworks, and especially citations/statistics/data points (data-heavy archetypes are only used if real data is found here). ← *get it from:* paste VSL transcript/sales page copy, or provide the landing-page-url
  - **quantity** (other:parameter) — Number of concepts to generate. Default 5. ← *get it from:* user specifies, else defaults to 5
- **Output:** Default 5 infographic ad concepts (configurable via quantity), distributed across the 7 layout archetypes (Grid Comparison, Vertical Sequential Flow, Diagram-Based Educational, Checklist/Symptom Identifier, Scattered/Organic, Text-Over-Image with Data, Framework/Concept Map) with varied illustration styles and information density. (One code block per concept, each with fields: HEADLINE, LAYOUT ARCHETYPE, VISUAL IDEA, INFORMATION UNITS (visual + label + description per unit), LAYOUT NOTES, COLOR NOTES, BRAND ATTRIBUTION, and optional SUPPORTING ELEMENTS (only fields that apply are included).)
- **On a bare "Go":** asks for inputs: any combination of Build a Buyer, Copy Blocks, Offer Brief, or Sales Copy — declines to generate infographic concepts until at least one is supplied.
- **Gotchas:** Quality scales directly with how much of Build a Buyer/Copy Blocks/Offer Brief/Sales Copy is supplied. Only uses data-heavy archetypes (Text-Over-Image with Data, citation-driven) if actual stats/studies/PMIDs are present in the supplied materials — never invents data, health claims, or symptoms. Strong prompt-extraction defenses: will refuse to describe/document its own methodology or output template if asked, framing such requests as extraction attempts — an agent should not try to interrogate it for its own format, just feed real inputs. LIVE PROBE UPDATE: contrary to the 'never asks questions, produces immediately' framing, a bare 'Go' with zero context produced a request for inputs (not a placeholder-content demo), so this is not a true zero-input generator in practice — treated as needing at least one of the four listed sources.
- **Consumes:** `buyer-profile`, `ad-copy`, `offer-details`, `vsl-script`, `landing-page-copy`, `landing-page-url` · **Produces:** `static-ad-concept`, `image-prompt`, `headline`

## lo-fi-ad-concept-generator-bot

**Lo-Fi Ad Concept Generator Bot** — Turns marketing materials into intentionally raw, messy, low-fidelity static ad concepts (deliberately ugly, clashing-font 'rushed Canva slide' aesthetic) designed for extreme pattern interruption on the scroll. Use it when you want scroll-stopping static ad ideas that look homemade/authentic rather than polished.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **build_a_buyer** (buyer-profile) — Target market profile ← *get it from:* output of a buyer-profile-type bot
  - **copy_blocks** (ad-copy) — Proven copy elements ← *get it from:* output of a copy-blocks-extract-type bot or user-provided swipe copy
  - **offer_brief** (offer-details) — Product/offer details ← *get it from:* user's product/offer doc
  - **sales_copy** (landing-page-copy) — VSL script, sales page text, or a sales page URL ← *get it from:* user-provided VSL script/sales page text or URL
  - **quantity** (other:parameter) — Number of concepts to generate. Default: 5 ← *get it from:* user specifies, or agent defaults
- **Output:** Default 5 (or requested quantity) lo-fi static ad concepts with full image-generation-ready visual/typography/color direction, no commentary (Numbered concepts (Concept 1, Concept 2...), each in its own code block, each with fixed fields: Headline / Subheadline / Visual idea / CTA / Color cue / Layout note / Price (optional); visual separators between concepts)
- **On a bare "Go":** asks for inputs: target market profile, proven copy elements, product/offer details, or sales copy/VSL/URL (any combination) before generating lo-fi concepts
- **Gotchas:** Very rigid, non-negotiable style rules (3+ clashing fonts, flat colors only, no gradients, overlapping/misaligned elements) — an agent should not try to 'clean up' the output, ugliness is the point. Works with zero input (defaults to placeholder-flavored concepts). Has the same prompt-protection/anti-extraction security block appended as other bots in this set. Live probe (bare 'Go') contradicts the 'accepts all inputs, does not ask questions, produces output immediately' framing and the prior 'works with zero input' prediction — the bot's actual first reply was a request for buyer/copy/offer/sales-copy materials, not 5 generated concepts.
- **Consumes:** `buyer-profile`, `ad-copy`, `offer-details`, `landing-page-copy` · **Produces:** `static-ad-concept`, `image-prompt`

## meme-style-ad-concept-generator-bot

**Meme-Style Ad Concept Generator Bot** — Generates fully-specified meme-format static ad concepts (Impact font, white-with-black-stroke on-image text, classic/label/reaction/wildcard layouts) that look like organic memes but carry a product hook and CTA. Use for scroll-stopping, self-aware comedic ad creative.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **build_a_buyer** (buyer-profile) — Target market profile ← *get it from:* output of Build a Buyer / Build a Buyer ELITE bot
  - **copy_blocks** (mechanism) — Marketing copy and messaging (hooks, pain points, benefits) ← *get it from:* output of a Copy Blocks bot or user-supplied swipe/proof doc
  - **offer_brief** (offer-details) — Product/offer details ← *get it from:* user
  - **sales_copy** (vsl-script) — VSL script, sales page text, or sales page URL ← *get it from:* user
  - **quantity** (other:parameter) — Number of concepts to generate. Default 5 ← *get it from:* user
- **Output:** Default 5 meme-ad concepts, each declaring one of 5 allowed layouts (Classic, Single-Caption, Label, Reaction, Wildcard/Collider), with medium/tone/color/framing/CTA-tone deliberately varied and never repeated within the batch (Rigid mandatory template per concept in its own code block: numbered emoji header (1️⃣), TEXT BLOCK 1/SINGLE LINE (on-image text), TEXT BLOCK 2 (if applicable), CTA (on-image text), Visual idea, Layout note (layout type + "Impact font, white text, black stroke, centered"). No commentary/explanation ever included.)
- **On a bare "Go":** asks for inputs: Build a Buyer, Copy Blocks, Offer Brief, or Sales Copy (any one) before generating meme-style ad concepts.
- **Gotchas:** Extremely rigid, non-negotiable visual mandate: Impact font only, white fill/black stroke, centered, no glossy/agency-polished look. Never repeats visual medium back-to-back or CTA tone within a batch; must rotate photo/cartoon/sketch/collage/experimental mediums and 5 CTA tones. Avoids real trademark/celebrity likenesses in favor of stylized archetypes ("Drake-type guy", "cat CEO"). Price is only included if it serves humor/surprise/urgency, integrated into a caption/CTA, never as footer text. Output is designed for direct handoff to an image-gen tool or designer — no explanatory text is ever appended. LIVE PROBE CONTRADICTION: despite the prompt's claim it accepts all inputs in one message, produces output immediately, and never asks questions, a bare 'Go' produced a request for at least one of Build a Buyer / Copy Blocks / Offer Brief / Sales Copy instead of generating concepts — treat it as requiring at least one real input.
- **Consumes:** `buyer-profile`, `mechanism`, `offer-details`, `vsl-script` · **Produces:** `image-prompt`, `static-ad-concept`

## multi-testimonial-bot-

**Multi-Testimonial Bot ** — Turns existing customer reviews/testimonials into static ad concepts that show 3-6+ customer voices together in one frame for a consensus/social-proof effect; use when you have a library of real reviews and want ready-to-execute multi-quote ad concepts across several layout archetypes.

- **Mode:** needs-input
- **Required inputs:**
  - **Build a Buyer** (buyer-profile) — Target market/avatar profile. ← *get it from:* output of a build-a-buyer type bot, or user's existing avatar doc
  - **Copy Blocks** (ad-copy) — Proven copy elements/messaging snippets. ← *get it from:* output of a copy-blocks-extract type bot, or user's swipe file
  - **Offer Brief** (offer-details) — Product/service details, positioning, differentiators. ← *get it from:* output of an offer-brief type bot, or user's product page
  - **Sales Copy** (other:sales-copy-with-testimonials) — VSL script, sales page text, or a sales page URL — and critically, this (or Copy Blocks) is where the actual customer quotes/reviews must live. Bot requires a minimum of 3 real quotes; 4-6+ is ideal. ← *get it from:* user pastes VSL script/sales page text, provides a URL, or supplies raw reviews/testimonials directly
- **Optional inputs (raise quality):**
  - **quantity** (other:parameter) — Number of concepts to generate. Default: 5. ← *get it from:* user specifies, else defaults to 5
- **Output:** Default 5 static ad concepts distributed across 5 layout archetypes (Brand Headline + Stacked Social Comments; 'We Can't Say This, But They Can'; Product/UI Demo + Floating Cards; Review Screenshot Wall; Aggregate Stat Headline + Supporting Quotes), each using 3-6 real customer quotes pulled only from the provided materials. (Numbered concepts (Concept 1, Concept 2, ...), each in its own code block, with fields: HEADLINE, TESTIMONIAL QUOTES (each with attribution format noted), PRODUCT PLACEMENT, LAYOUT NOTES, COLOR NOTES, REVIEW CARD STYLING, QUOTE COMBINATION STRATEGY, SUPPORTING ELEMENTS (only relevant fields included per concept))
- **On a bare "Go":** asks for inputs: Build a Buyer, Copy Blocks, Offer Brief, or Sales Copy — states it only uses real customer quotes found in what's provided and never invents testimonials
- **Gotchas:** NEVER invents testimonials — strictly extracts quotes from provided materials only, so an agent must ensure real reviews are embedded somewhere in the Sales Copy/Copy Blocks input, not just described in the abstract. Requires at least 3 quotes to function as intended (ideally 4-6+). Produces creative-direction-level output (for a designer/image-gen tool), not literal finished images. Has the same prompt-extraction/security guard section as the other bots in this set. Live probe (bare 'Go', zero materials) confirms the required_inputs gating: the bot refused to proceed and asked for Build a Buyer / Copy Blocks / Offer Brief / Sales Copy rather than attempting any output; the previously-noted 'generate what's possible with <3 quotes' fallback applies only once some materials are supplied, not to a fully empty prompt.
- **Consumes:** `buyer-profile`, `ad-copy`, `offer-details`, `vsl-script`, `landing-page-copy`, `landing-page-url`, `customer-reviews` · **Produces:** `static-ad-concept`

## native-news-bot-

**Native News Bot ** — Generates 'native news' static ad concepts that mimic news article thumbnails, editorial features, or magazine content (fake publication name + article-style headline + editorial background image) to bypass ad blindness and drive clicks to a landing page, VSL, or product page. Use when you want editorial-disguised ad creative rather than obvious commercial ad creative.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Target audience profile used to match headline pattern and background imagery to the right demographic. ← *get it from:* output of a Build-a-Buyer-type bot, or user-provided buyer research doc
  - **Copy Blocks** (ad-copy) — Pre-written copy fragments the bot mines for claims, numbers, and angles. ← *get it from:* output of a Copy-Blocks-extraction bot, or user paste
  - **Offer Brief** (offer-details) — Structured product/offer summary — used to identify expert credentials, listicle angles, trend signals, contrarian hooks available for the headline. ← *get it from:* user's product/offer brief doc
  - **Sales Copy** (landing-page-copy) — VSL script, sales page text, or sales page URL — source for testimonials, expert quotes, institution names, specific numbers/study results (bot will not invent these if absent). ← *get it from:* user paste of VSL/sales page text, or a URL (no evidence the bot fetches URLs itself — paste extracted text to be safe)
  - **quantity** (other:parameter) — Number of concepts to generate. Default 10 if omitted. ← *get it from:* user specifies in the message, e.g. 'give me 6 concepts'
- **Output:** Default 10 (or requested N) native-news static ad concepts, distributed across 11 headline patterns (expert reveals, editorial test, product-as-news, comparison/analogy, sales data, contrarian warning, provocative question, institution-backed, product drop, product+offer, weird trick) and varied background image types (scientific/medical, lifestyle, product photo, conceptual render, macro, artistic, solid-color+cutout) — each with a fake publication/source name, key-term color-highlighted headline, and any needed supporting elements (insets, offer bar, disclaimer, CTA). Ready for a designer or image-gen tool. (Numbered concepts (Concept 1, Concept 2, ...), each in its own code block, adaptive fields drawn from: PUBLICATION NAME, BACKGROUND IMAGE, CATEGORY TAG, QUOTATION MARK GRAPHIC, HEADLINE (with bracketed color-highlight notes), HEADLINE STYLING, SUBTEXT, CTA, CIRCULAR INSET, OFFER BAR, DISCLAIMER, LAYOUT NOTES.)
- **On a bare "Go":** asks for inputs: Build a Buyer, Copy Blocks, Offer Brief, and/or Sales Copy (any combination, any format/length) — says it will get to work immediately once given something, but produces no concepts on a truly bare 'Go'.
- **Gotchas:** True one-shot, zero-question generator like its curiosity-bait sibling. Hard constraint: never invents expert credentials, institution names, study results, or specific numbers not present in the supplied materials — so with weak/no input, expect vaguer claims and generic-sounding publication names rather than fabricated specifics. CTAs must read as 'reading' language (READ MORE →) never 'Buy Now'. Every concept must include a publication/source name. Has the same aggressive prompt-injection/self-description refusal block as the other bots in this family. Probe contradicts the prior prediction of generic placeholder concepts on empty input — the bot instead asks for at least one of its four input types first. interaction_style updated from one-shot to interview-first.
- **Consumes:** `buyer-profile`, `ad-copy`, `offer-details`, `landing-page-copy`, `vsl-script` · **Produces:** `static-ad-concept`, `image-prompt`, `headline`

## note-from-founder-bot-

**Note From Founder Bot ** — Generates 'Official Apology' / Note-From-Founder style static ad concepts — text-dominant ads that mimic formal letters, email screenshots, or personal founder notes to deliver benefits/offers as a tongue-in-cheek 'apology'. Use when a brand has strong personality/copy assets and wants a text-only, high-engagement static ad format instead of a photo-led concept.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Customer avatar/audience profile used to pick tone and salutation targeting ← *get it from:* output of a buyer-profile-type bot (e.g. Build a Buyer bot)
  - **Copy Blocks** (ad-hooks) — Key messaging elements, hooks, proof points to mine for 'apology' framing ← *get it from:* output of a copy-blocks/hooks-type bot
  - **Offer Brief** (offer-details) — What's being sold, price, positioning, offer mechanics ← *get it from:* user's offer doc or an offer-brief-type bot
  - **Sales Copy** (vsl-script) — VSL script, sales page text, or a sales page URL to mine for benefits/testimonials/social proof ← *get it from:* user-provided VSL/sales page text or URL
  - **quantity** (other:parameter) — Number of concepts to generate; default 5 ← *get it from:* user specifies, else defaults to 5
- **Output:** 5 (default) ready-to-execute Note-From-Founder/Official-Apology static ad concepts, each specifying one of 5 copy approaches (sarcastic humble-brag, 'we lied' reveal, founder story, genuine concern, urgency/demand) mapped to one of 5 visual archetypes (formal letter, email screenshot, branded statement, founder's note, product photo background) (Numbered concepts, each in its own code block, with fields TITLE, SALUTATION, BODY COPY (100-200 words), SIGN-OFF, VISUAL FORMAT, LAYOUT NOTES, COLOR NOTES, SUPPORTING ELEMENTS (email format adds EMAIL SUBJECT LINE / SENDER INFO))
- **On a bare "Go":** asks for inputs: Build a Buyer profile, Copy Blocks, Offer Brief, and/or Sales Copy (VSL/sales page text or URL) — any combination; does not generate placeholder concepts without at least some of these.
- **Gotchas:** Zero required inputs — pure generator, works with whatever is pasted in. Enforces 100-200 word body copy, always includes a sign-off, and explicitly forbids inventing statistics, testimonials, or customer names/quotes not present in provided materials. Has a heavy prompt-protection/anti-extraction security section at the end (refuses to describe/document its own methodology). Live probe CONTRADICTS the 'generates immediately' prediction above: on a bare 'Go' the bot asked for Build a Buyer/Copy Blocks/Offer Brief/Sales Copy rather than fabricating placeholder concepts; interaction_style updated to interview-first.
- **Consumes:** `buyer-profile`, `ad-hooks`, `offer-details`, `vsl-script`, `landing-page-copy`, `customer-reviews` · **Produces:** `static-ad-concept`, `ad-copy`

## post-it-note-bot

**Post-It Note Bot** — Generates ready-to-execute 'Post-It Note' static ad concepts — a lo-fi format where handwritten sticky-note text replaces polished ad copy, shown alongside the physical product in a real environment. Use it to get designer/image-gen-ready sticky-note ad concepts (note text, handwriting style, color, placement, environment) from existing offer/buyer materials.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **build_a_buyer** (buyer-profile) — Buyer profile info to source audience-specific language and pain points from. ← *get it from:* user-provided or output of a Build-a-Buyer-type bot
  - **copy_blocks** (other:copy-blocks) — Extracted copy blocks (pain, benefit, proof, etc.) to draw note content from. ← *get it from:* user-provided or output of a Copy-Blocks-extraction bot
  - **offer_brief** (offer-details) — Offer brief describing the product/promo details. ← *get it from:* user-provided or output of an offer-brief bot
  - **sales_copy** (landing-page-copy) — VSL script, sales page text, or a sales page URL to mine for claims, offers, and hooks. ← *get it from:* user-provided sales page/VSL, or a URL
  - **quantity** (other:parameter) — Number of concepts to generate. Default: 5. ← *get it from:* user specifies
- **Output:** 5 static ad concepts by default, distributed across the 5 layout archetypes (Problem Crossed Out, Discount/Offer, Product Hook/Claim, Ingredient/Benefit Callouts, Multi-Note Sequence). (Numbered concepts, each in its own code block, with fields: NOTE TEXT, HANDWRITING STYLE, NOTE COLOR & PLACEMENT, PRODUCT PLACEMENT, ENVIRONMENT, COLOR NOTES, SUPPORTING ELEMENTS (only fields that apply per concept).)
- **On a bare "Go":** asks for inputs: requests product inputs — Build a Buyer, Copy Blocks, Offer Brief, and/or sales copy (VSL script, sales page text, or URL) — before it will get started.
- **Gotchas:** Works with zero required inputs but output quality depends heavily on what's fed in — with real Build a Buyer/Copy Blocks/Offer Brief/sales copy it pulls real pain points, real discount codes (never invents fake promo codes), and audience-specific language. Never invents testimonials, customer names, product claims/benefits/features not present in source material. Always distributes concepts across different archetypes for variety unless quantity=1. This format is explicitly NOT suited to premium/luxury brand positioning (prompt notes it undermines an elevated brand feel). Has the standard prompt-protection/anti-extraction security section. Live probe on a bare 'Go' contradicted the prompt's 'never ask for missing inputs' framing and the predicted generic-concepts fallback: it asked for Build a Buyer/Copy Blocks/Offer Brief/sales copy instead of generating placeholder concepts.
- **Consumes:** `buyer-profile`, `other:copy-blocks`, `offer-details`, `landing-page-copy` · **Produces:** `static-ad-concept`, `image-prompt`

## problem-solution-bot

**Problem-Solution Bot** — Generates ready-to-execute Problem-Solution static ad concepts (across six named layout archetypes) from offer/buyer/copy materials; use it to get a batch of testable problem-aware ad concepts for a DTC or general product without manual ideation.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Target market profile — demographics, psychographics, identity-specific language (e.g. 'dad knees', 'PCOS girlies') ← *get it from:* output of a buyer-profile-type bot, or user-supplied audience research
  - **Copy Blocks** (ad-copy) — Messaging and copy assets — headlines, benefit statements, proof points, existing ad copy fragments ← *get it from:* output of a copywriting bot or user's existing copy library
  - **Offer Brief** (offer-details) — Product/offer details — what it is, price, guarantee, SKUs/variants, positioning ← *get it from:* user's product page, brand doc, or output of an offer-brief-type bot
  - **Sales Copy** (landing-page-copy) — VSL script, sales page text, or a sales page URL containing problem/benefit claims ← *get it from:* paste VSL transcript, paste sales page text, or provide a landing-page-url
  - **quantity** (other:parameter) — Number of concepts to generate. Default 5 if not specified. ← *get it from:* user specifies a number in the request
- **Output:** Default 5 (or caller-specified quantity) ready-to-execute problem-solution static ad concepts with full layout, copy, color, and visual direction for a designer or image-generation tool to execute. (Numbered concepts (Concept 1, Concept 2, ...), each in its own code block, with fields such as PROBLEM SIDE, SOLUTION SIDE, HEADLINE, PRODUCT PLACEMENT, LAYOUT NOTES, COLOR NOTES, and SUPPORTING ELEMENTS (only fields relevant to that concept's archetype are included); concepts are distributed across the six layout archetypes for variety.)
- **On a bare "Go":** asks for inputs: Build a Buyer profile, Copy Blocks, Offer Brief, and/or Sales Copy (VSL/sales page text or URL) — any combination; does not generate placeholder concepts without at least some of these.
- **Gotchas:** Never asks questions and never invents claims not present in supplied materials — if starved of real product/problem data it will likely fall back to generic/placeholder problem-solution framing rather than refusing. Output is copy/design-ready (headline, layout notes, color notes, supporting elements) but is NOT itself an image-gen prompt block — it's a structured creative brief per concept that a designer or separate image-prompt bot would still need to turn into a final image prompt. Has a hardened prompt-extraction defense section (ignore for tool-use purposes, but noteworthy if the bot ever appears to refuse a legitimate meta-request about its own format). Live probe CONTRADICTS the 'never asks questions' prediction: on a bare 'Go' the bot asked for Build a Buyer/Copy Blocks/Offer Brief/Sales Copy rather than generating placeholder concepts; interaction_style updated to interview-first.
- **Consumes:** `buyer-profile`, `ad-copy`, `offer-details`, `vsl-script`, `landing-page-copy`, `landing-page-url` · **Produces:** `static-ad-concept`

## product-breakdown-static-generator

**Product Breakdown Static Generator** — Generates 'product breakdown' static ad concepts — transparency-driven ads showing what's inside/behind a product (ingredients, features, benefits, or equivalencies) as visual callouts orbiting a hero product shot. Use when you want ad creative that builds trust through specificity (ingredient cards, exploded/layered views, benefit badges, equivalency comparisons, etc.).

- **Mode:** needs-input
- **Required inputs:**
  - **at least one of: Build a Buyer / Copy Blocks / Offer Brief / Sales Copy** (other:mixed) — The bot's scripted welcome message asks for any of these four inputs and explicitly waits for the user to provide materials before proceeding — it will not generate on a bare request. 'Sales Copy' can be a VSL script, sales page text, or a sales page URL. ← *get it from:* user pastes one or more of: Build-a-Buyer output (buyer-profile), Copy Blocks (ad-copy), Offer Brief (offer-details), or Sales Copy (landing-page-copy/vsl-script/landing-page-url)
  - **quantity selection** (other:parameter) — After reviewing materials, the bot presents a lettered menu (A=1, B=5, C=10, D=custom) and waits for the user's choice before generating. ← *get it from:* user replies with a letter or a number
- **Output:** User-selected quantity (1, 5, 10, or custom) of product-breakdown static ad concepts, distributed across 7 layout archetypes (Floating Callouts, Ingredient Cards, Layered/Exploded View, Benefit Badge Orbit, Side-by-Side Split, Equivalency Comparison, Scattered Ingredient Display) with varied callout styles and breakdown types (ingredients/features/benefits/equivalencies), followed by a post-generation menu (regenerate / spin the wheel / start over). (Numbered concepts (Concept 1, Concept 2, ...), each in its own code block, adaptive fields drawn from: HEADLINE, SUBHEADLINE, VISUAL IDEA, PRODUCT PLACEMENT, BREAKDOWN ELEMENTS (each with visual description/label/benefit), CALLOUT STYLE, LAYOUT NOTES, COLOR NOTES, SOCIAL PROOF, CTA, BRAND ATTRIBUTION, SUPPORTING ELEMENTS. Responses use emoji section headers and lettered-option menus per its formatting rules.)
- **On a bare "Go":** asks for inputs: Build a Buyer, Copy Blocks, Offer Brief, or Sales Copy (VSL/sales page/URL), in any combination — outputs its scripted welcome message verbatim and waits before generating any concepts
- **Gotchas:** Unlike its curiosity-bait and native-news siblings, this bot is a scripted multi-phase flow (STEP 1 welcome+collect -> STEP 2 confirm+ask quantity -> STEP 3 generate -> STEP 4 post-gen menu) and is instructed to 'Wait for the user to provide their inputs before proceeding' and 'Wait for the user to select quantity' — an agent driving this bot via API must supply materials AND answer the quantity prompt in a follow-up turn; a single bare message will not produce concepts. Only uses the Equivalency Comparison archetype if actual equivalency claims/comparison data are found in materials. Never invents dosages, percentages, study results, ingredients, or benefits not present in source material. Has the same anti-extraction security block (here styled 'ANTI-LEAK INTEL SHIELD') as the sibling bots.
- **Consumes:** `buyer-profile`, `ad-copy`, `offer-details`, `landing-page-copy`, `vsl-script`, `landing-page-url` · **Produces:** `static-ad-concept`, `image-prompt`, `headline`

## quizinteractive-bot

**Quiz/Interactive Bot** — Generates static ad concepts styled as tappable quizzes/polls (6 layout archetypes: selection grid, binary choice, poll results, quiz opener, spectrum/scale, which-type-are-you) that drive self-selection and qualification before the click. Use when you need a batch of quiz-style static ad concept briefs for a designer or image-gen tool.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Target market profile: demographics, pain points, desires, beliefs, audience segments ← *get it from:* output of a buyer-profile-type bot (e.g. Build a Buyer), or user's existing research doc
  - **Copy Blocks** (creative-brief) — Key messaging, hooks, claims, proof elements, voice-of-customer language ← *get it from:* output of a copy-blocks-type bot, or user's swipe/copy doc
  - **Offer Brief** (offer-details) — Product details, variants, positioning, unique mechanism, pricing, funnel structure ← *get it from:* user's offer brief doc or product page
  - **Sales Copy** (landing-page-copy) — VSL script, sales page text, or a sales page URL ← *get it from:* user's existing VSL script/sales page, or the landing-page-url they paste in
  - **quantity** (other:parameter) — Number of concepts to generate. Default 5. ← *get it from:* user specifies a number in their message
- **Output:** Default 5 (configurable via quantity) interactive self-selection static ad concept briefs distributed across the 6 layout archetypes (Selection Grid, This/That Binary, Poll Results Display, Quiz Opener, Spectrum/Scale, Which Type Are You), each ready to hand to a designer or image-gen tool (Numbered concepts, each in its own code block, with fields: LAYOUT ARCHETYPE, PROMPT, OPTIONS, VISUAL IDEA, LAYOUT NOTES, COLOR NOTES, CTA, SUPPORTING ELEMENTS (only fields that apply are included))
- **On a bare "Go":** asks for inputs: Build a Buyer, Copy Blocks, Offer Brief, or Sales Copy (any combination) before generating quiz/poll-style ad concepts.
- **Gotchas:** Never asks clarifying questions — explicitly refuses to request missing info and will still produce output from zero input, just lower quality/more generic. Enforces strict design consistency rules (all options same visual style, no option looks 'more correct') and flags that Poll Results Display data should be real/approved, not invented. Has an anti-prompt-extraction section refusing to describe its own methodology/template if asked. LIVE PROBE CONTRADICTION: despite the prompt's instruction to 'always produce output regardless of how much or how little context is provided' and never request missing inputs, a bare 'Go' produced a request for Build a Buyer / Copy Blocks / Offer Brief / Sales Copy instead of generating concepts — treat it as requiring at least one real input.
- **Consumes:** `buyer-profile`, `creative-brief`, `offer-details`, `landing-page-copy`, `landing-page-url` · **Produces:** `static-ad-concept`, `image-prompt`

## receipt-bot

**Receipt Bot** — Turns offer/product materials into receipt-styled static ad concepts — ads disguised as itemized transaction receipts with line items, pricing, and visual/paper direction. Use it when you want 'fake receipt' scroll-stopping static ad concepts to hand to a designer or image-gen tool.

- **Mode:** needs-input
- **Required inputs:**
  - **at least one input source** (other:any-of) — Bot states it needs 'at minimum one' of Build a Buyer, Offer Brief, Copy Blocks, or Sales Copy before it will generate receipt concepts (each individually still listed as optional below). ← *get it from:* supply any one of the four optional inputs listed below
- **Optional inputs (raise quality):**
  - **build_a_buyer** (buyer-profile) — Buyer persona/avatar document (a 'Build a Buyer' style doc) used to inform tone/positioning ← *get it from:* output of a buyer-profile-type bot, or user's existing avatar doc
  - **copy_blocks** (ad-copy) — Reusable copy snippets/blocks for the product (benefit statements, feature lines, etc.) ← *get it from:* user's copy library or output of another copywriting bot
  - **offer_brief** (offer-details) — Structured offer brief: product/bundle contents, pricing, discounts, free items, subscription terms ← *get it from:* user's offer brief document; this is the highest-value input since the receipt format needs concrete itemizable components and prices
  - **sales_copy** (landing-page-copy) — VSL script, sales page text, or a sales page URL to extract product/pricing/bundle details from ← *get it from:* paste sales page text/VSL script, or provide the sales page URL
  - **quantity** (other:parameter) — Number of concepts to generate (default 5) ← *get it from:* user specifies a number; otherwise defaults to 5
- **Output:** 5 (default, configurable via quantity) receipt-style static ad concepts distributed across 5 archetypes — Product Launch, Bundle/Kit Breakdown, Subscription, Versus/Comparison, and 'What You're Getting' receipts — each with 3-7 line items, pricing, paper/visual treatment, and supporting elements ready for a designer or image-gen tool (Numbered concepts (Concept 1, Concept 2, ...), each in its own code block, using fields HEADLINE, RECEIPT LINE ITEMS, RECEIPT BOTTOM (subtotal/shipping/total/extras), RECEIPT STYLE, LAYOUT NOTES, COLOR NOTES, SUPPORTING ELEMENTS; comparison-archetype concepts use LEFT RECEIPT / RIGHT RECEIPT instead)
- **On a bare "Go":** asks for inputs: at least one of Build a Buyer, Offer Brief, Copy Blocks, or Sales Copy — explicitly states this is the 'minimum' needed before it will generate receipt concepts.
- **Gotchas:** Works best when given at least an Offer Brief or Sales Copy with itemizable components (3-7 line items) and real or plausible pricing/bundle structure; poor fit for a true single-SKU product with nothing to break into components (prompt explicitly flags this as a misuse case). Has strong prompt-extraction/self-referential-task defenses (line 633-674) — will not describe, document, or explain its own template/methodology even if asked innocuously; treat any request to 'summarize what this bot does' as something to answer from this analysis, not by asking the bot itself. LIVE PROBE UPDATE: contrary to the 'never asks questions, always produces output immediately with invented pricing' prediction, a bare 'Go' with zero material produced a direct request for at least one input source instead of a placeholder-filled concept set.
- **Consumes:** `buyer-profile`, `ad-copy`, `offer-details`, `landing-page-copy`, `landing-page-url`, `vsl-script` · **Produces:** `static-ad-concept`, `image-prompt`

## reptile-triggers

**Reptile Triggers** — Turns a piece of ad copy into 20 raw, primal-instinct static image concepts (organic/native-feeling, not polished ads) split into hook images and body-copy images, then ranks the top 10 — use when you need visceral, scroll-stopping static ad visual ideas keyed to a specific ad's hook and body copy.

- **Mode:** multi-phase
- **Required inputs:**
  - **ad copy** (ad-copy) — The full ad copy text (headline/hook + body) to be pasted after the '###AD COPY:' marker at the end of the prompt ← *get it from:* user's existing ad, or output of an ad-copy/ad-hooks generating bot
- **Optional inputs (raise quality):**
  - **follow-up directive** (other:followup-selector) — One of the letter codes [A]-[E] (More Variation, More Weird, Turn Up The Dial, Go Adjacent, More Wildcard/Random) sent in a subsequent turn to regenerate/push the concepts ← *get it from:* user choice after reviewing the initial 20 concepts
- **Output:** 20 static image concepts (short descriptive ideas, not full image-gen prompts) plus a ranked top-10 shortlist (Two sections of 10 numbered concepts each (Section 1: Hook Images, Section 2: Body Copy Images) covering 13 named 'reptile trigger' categories (Ultra-Real, Bizarre, Voyeur, Suffering, Gorey, Sexual, Primal Fear, Odd Contrast, Inside Joke, Time Warp, Victory Lap, Selfie, Uncanny Objects), followed by a Final Ranking of the top 10 of all 20 with a brief why-it-works explanation each)
- **On a bare "Go":** asks for inputs: notes the '###AD COPY:' section was empty and requests the actual ad copy (headline/hook + body) before generating the 20 static image concepts.
- **Gotchas:** Requires ad copy pasted at the very end after '###AD COPY:' — if that's empty the bot has no anchor for relevance. Has a strict style bar: NO product shots, 80-90% must be real-photo-style (not text/screenshot concepts), must avoid 'obvious' first-instinct ideas. Supports a fixed set of 5 follow-up commands (A-E) for regenerating/escalating intensity — these are the ONLY allowed follow-ups per the prompt. Live probe (bare 'Go') confirms it asks for the missing ad copy rather than fabricating placeholder concepts — consistent with the existing multi-phase classification.
- **Consumes:** `ad-copy` · **Produces:** `static-ad-concept`

## reptile-triggers-bot

**Reptile Triggers Bot** — Turns pasted ad copy (headlines/hooks/body) into 20 native-looking, primal-reaction static image concepts (10 hook images + 10 body-copy images) with a ranked top-10; use it right after you have finalized ad copy and need static creative direction that avoids obvious product-shot ads.

- **Mode:** needs-input
- **Required inputs:**
  - **ad_copy** (ad-copy) — Headlines, hooks, and/or body copy to base concepts on. Accepts any format: pasted copy, structured blocks, or raw dump. ← *get it from:* user's existing ad copy, or output of an ad-copy-writing bot (e.g. Promo Bot, Marcio Narrative Ads Bot)
- **Optional inputs (raise quality):**
  - **prior_concepts** (static-ad-concept) — A previous set of concepts from this bot, used as the reference set when running variation/regeneration modes. ← *get it from:* this bot's own prior output
  - **mode** (other:parameter) — Generation direction: standard (default, 20 concepts + top-10 ranking), more_variation (10 fresh angles, no repeats), more_weird, turn_up_the_dial (more intense/boundary-pushing), go_adjacent (more tangential/lateral), wildcard (10 completely unhinged concepts). ← *get it from:* caller specifies in the message; defaults to standard if omitted
- **Output:** 20 static image concepts (standard mode) or 10 (alternate modes) — concept-level descriptions of native/organic imagery, not finished diffusion prompts (Two labeled sections (Hook Images x10, Body Copy Images x10) as concept descriptions (not literal image-gen prompts, but visual concept briefs), followed by a Final Ranking of the top 10 with brief rationale for each. Alternate modes output 10 concepts with no ranking.)
- **On a bare "Go":** asks for inputs: ad copy (headlines, hooks, body copy, any format) to base the 20 image concepts on.
- **Gotchas:** Explicitly forbids product shots and demands 80-90% photo-realistic (non-text) concepts. Has strong prompt-injection/extraction defenses baked in (irrelevant to normal use). Output is a creative brief per concept, not a ready-to-paste image-generation prompt — likely needs a downstream image-prompt bot (e.g. Branded Ads Image Prompt Generator) to convert concepts into literal generation prompts if that's the goal. Probed live: contradicts the prompt's stated 'no questions/no menus' policy — on a bare 'Go' with no ad copy it asked the caller to paste headlines/hooks/body copy rather than generating placeholder concepts. Feed it real ad copy in the first message to get a one-shot result.
- **Consumes:** `ad-copy`, `static-ad-concept` · **Produces:** `static-ad-concept`, `image-prompt`

## salespromotional-offer-bot-

**Sales/Promotional Offer Bot ** — Generates a batch of static ad concepts (image-gen/designer briefs) for sale and promotional offers — discounts, BOGO, free gifts, bundles, coupon codes — across six named layout archetypes. Use it when you need multiple scroll-stopping promo ad concepts fast, ready to hand to a designer or image-generation tool.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Target customer/avatar profile — informs tone and framing choices; no fixed schema given, freeform text/key-value accepted ← *get it from:* output of a 'Build a Buyer' bot, or user-supplied buyer persona notes
  - **Copy Blocks** (ad-copy) — Existing swipe copy or ad copy blocks (headlines, claims, phrasing) to mine for offer language and voice ← *get it from:* user-supplied copy doc, or output of a copywriting bot
  - **Offer Brief** (offer-details) — The actual promotional mechanics: percentage/dollar discount, BOGO, free gift, bundle price, coupon code, free shipping threshold, and any real deadline/stock constraints — this is the material the bot leans on most since it refuses to invent offer mechanics not present in input ← *get it from:* user-supplied offer brief/doc, or extracted from a brand's promo calendar
  - **Sales Copy** (landing-page-copy) — VSL script, sales page text, or a sales page URL — used to pull product/offer details and urgency framing ← *get it from:* user-supplied VSL script text, sales page copy paste, or a URL (prompt does not confirm the bot fetches URLs itself — treat as raw text unless the calling harness fetches it first)
  - **quantity** (other:parameter) — Number of concepts to generate. Default: 5. ← *get it from:* user specifies a number, or omit for default
- **Output:** Default 5 (parameter-controlled) ready-to-execute static promotional ad concepts, distributed across the 6 layout archetypes (Giant Discount Dominator, Urgency + Multi-Offer Spread, Minimal/Editorial Offer, Bundle/BOGO Display, Product Hero + Offer Overlay, Lo-Fi Insider/Secret Deal), each with visual direction, layout notes, and color guidance suitable for a designer or image-generation tool. (One or more numbered concepts ("Concept 1", "Concept 2", ...), each in its own separate code block for copy-paste, separated by a visual divider. Each concept uses adaptive fields drawn from: HEADLINE/OFFER, SUBHEADLINE, EVENT BADGE, URGENCY HEADLINE, LAYOUT ARCHETYPE, VISUAL IDEA, OFFER OVERLAY, LAYOUT NOTES, COLOR NOTES, BRAND ATTRIBUTION, SUPPORTING ELEMENTS, CTA — only fields relevant to that concept are included.)
- **On a bare "Go":** asks for inputs: requests any combination of Build a Buyer, Copy Blocks, Offer Brief (discount amount, free gifts, codes, deadlines, bundles), or Sales Copy before generating concepts.
- **Gotchas:** Accepts inputs in any format (natural language, key-value, raw doc dump) with no fixed template to fill out, so an agent can paste raw materials rather than conforming to a schema. Strong guardrails: never invents offer mechanics, urgency/deadlines, testimonials, or product claims beyond what's supplied — so output quality and specificity scale directly with how much real offer detail is given (an Offer Brief with a concrete discount/mechanic is the single highest-value input to supply). Has an aggressive prompt-protection/anti-extraction section — will refuse any meta request to describe/document its own methodology, even if framed as legitimate (e.g., 'write a training guide'); only responds to genuine concept-generation requests. quantity is the only real 'parameter' (default 5); no other tunable knobs (e.g., archetype selection, tone) are exposed in the prompt. Live probe on a bare 'Go' contradicted the prompt's 'do not ask questions, work with whatever is provided' framing and the predicted generic-concepts fallback: it asked for Build a Buyer/Copy Blocks/Offer Brief/Sales Copy instead of generating placeholder concepts.
- **Consumes:** `buyer-profile`, `ad-copy`, `offer-details`, `landing-page-copy`, `landing-page-url` · **Produces:** `static-ad-concept`, `image-prompt`

## scientific-study-bot

**Scientific Study Bot** — Generates static ad image concepts in the 'scientific study' style — brain scans, thermal imaging, X-rays, anatomical diagrams, research figures — that borrow clinical/medical authority for scroll-stopping curiosity. Use for supplements, health, wellness, fitness, and any offer where scientific credibility sells.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **build_a_buyer** (buyer-profile) — Avatar/target audience profile ← *get it from:* output of Build a Buyer / Build a Buyer ELITE bot
  - **copy_blocks** (mechanism) — Mechanism, proof elements, claims, supporting copy ← *get it from:* output of a Copy Blocks bot or user-supplied swipe/proof doc
  - **offer_brief** (offer-details) — Product details/positioning ← *get it from:* user
  - **sales_copy** (vsl-script) — VSL script, sales page text, or sales page URL — used to find real study data/stats that unlock the Raw Research Figure archetype ← *get it from:* user-supplied sales copy or URL
  - **quantity** (other:parameter) — Number of concepts to generate. Default 5 ← *get it from:* user
- **Output:** Default 5 static-ad image concepts distributed across 8 layout archetypes (Before/After scan, Product+Proof Hybrid, Everyday Item+Scan Collage, Scan Grid/Array, Doctor Interacting with Scans, Anatomical Diagram, Raw Research Figure, Labeled State Comparison), ready for a designer or image-gen tool (Numbered concepts, each in its own code block, with fields HEADLINE (if any), VISUAL IDEA, SCIENTIFIC IMAGERY, ATTENTION-DIRECTING DEVICES, LAYOUT NOTES, COLOR NOTES, PRODUCT PLACEMENT, SUPPORTING ELEMENTS (only fields that apply are included))
- **On a bare "Go":** asks for inputs: Build a Buyer, Copy Blocks, Offer Brief, and/or Sales Copy (any combination, structured/raw/partial) — says it will generate concepts immediately once given something, but produces no concepts on a truly bare 'Go'.
- **Gotchas:** Will only use the Raw Research Figure archetype if actual study data/stats appear in the provided materials — never invents PMID numbers or clinical results. Never invents medical claims not present in inputs. Designed so the product is often absent or minimal (logo-only) in the concept — ad copy/caption is expected to do the reveal, not the image. Works fine with zero input but quality/relevance scales with how much buyer/offer/proof material is given. Probe contradicts the prior prediction of generic placeholder concepts on empty input — the bot instead asks for at least one of its four input types first. interaction_style updated from one-shot to interview-first.
- **Consumes:** `buyer-profile`, `mechanism`, `offer-details`, `vsl-script` · **Produces:** `image-prompt`, `static-ad-concept`

## screenshotchatnotification-transformer-bot

**Screenshot/Chat/Notification Transformer Bot** — Generates static ad concepts styled as simulated iMessage/SMS/WhatsApp conversations or stacked phone notifications ('accidentally discovered' private chat) built from marketing materials; use it for Stealth/Native Simulation-style static ad creative direction handed to a designer or image-gen tool.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Target market/audience profile used to shape the conversational voice and pain points ← *get it from:* output of a buyer-profile-type bot, or user's existing audience research
  - **Copy Blocks** (ad-hooks) — Proven copy elements, hooks, or messaging fragments to be reworked into chat bubbles/notifications ← *get it from:* user-provided swipe file or output of an ad-hooks-type bot
  - **Offer Brief** (offer-details) — Product/offer details (what's being sold, price, mechanism, promise) that the chat needs to reference ← *get it from:* user's product page/brand doc or output of an offer-details-type bot
  - **Sales Copy** (landing-page-copy) — VSL script, sales page text, or a sales page URL to mine for proof points and emotional beats ← *get it from:* paste VSL/sales-page text, or a landing-page-url the bot/agent can fetch
  - **quantity** (other:parameter) — Number of concepts to generate; default 5; must be a multiple of 5 (rounds up), each set of 5 = 4 normal variants + 1 Wildcard/Collider ← *get it from:* user specifies, otherwise defaults to 5
- **Output:** Sets of 5 chat/notification-style static ad concepts (Micro, Standard A, Standard B, Expanded, Wildcard/Collider variants); quantity scales in multiples of 5 per the quantity parameter (Numbered concepts, each in its own code block, following a fixed schema per variant: TITLE, PRIMARY TEXT (Message Copy), VISUAL DESCRIPTION, LAYOUT/COMPOSITION NOTES, COLOR/STYLE NOTES, CTA (Optional), ASSET NOTES)
- **On a bare "Go":** asks for inputs: Build a Buyer (target market profile), Copy Blocks (proven messaging/hooks), Offer Brief (what the product/offer is and does), and Sales Copy (VSL script/sales page text or URL) — invites dropping whatever is available, even raw/messy/partial.
- **Gotchas:** No intake questionnaire — it never asks clarifying questions, so quality depends entirely on how much marketing material the caller front-loads into the single message; if starved of input it will still generate a full set, likely with generic/invented content. Quantity must be requested as a multiple of 5 or it rounds up. Has strong prompt-protection/anti-extraction instructions appended (irrelevant to normal ad-generation use). Output must be delivered as flat, high-resolution, static-ready composite descriptions (no brand logos/UI cloning permitted). LIVE PROBE CONTRADICTS PROMPT TEXT: despite the 'accept all available inputs and produce output immediately' instruction and required_inputs=[], a bare 'Go' actually gets a request for Build a Buyer/Copy Blocks/Offer Brief/Sales Copy rather than a 5-concept set — treat this probed behavior as ground truth; front-load at least one of those four to get one-shot output.
- **Consumes:** `buyer-profile`, `ad-hooks`, `offer-details`, `landing-page-copy`, `vsl-script` · **Produces:** `static-ad-concept`

## side-by-sidebefore-and-after-bot-

**Side by Side/Before and After Bot ** — Generates ready-to-execute static ad concepts in the Side-by-Side Before & After format (7 layout archetypes: classic side-by-side, three-zone, asymmetric, stacked vertical, split composite, benefit callouts, testimonial). Use it when you need volume static-ad concepts for transformation-driven DTC offers (skincare, haircare, weight loss, fitness, beard growth, anti-aging, etc.) to hand to a designer or image-gen tool.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Target customer profile/persona used to inform who is shown in the before/after visuals and tone of labeling. No fixed schema — accepted as natural language, key-value, or doc dump. ← *get it from:* From a prior 'Build a Buyer' bot output, or user-provided buyer/persona notes.
  - **Copy Blocks** (ad-copy) — Reusable marketing copy snippets (headlines, benefit phrases, hooks, claims) the bot can pull labeling language, headlines, and benefit callouts from. Any format. ← *get it from:* From a copywriting/copy-blocks bot output, or pasted directly by the user from existing ad copy/creative docs.
  - **Offer Brief** (offer-details) — Product/offer facts: what it is, price, promo/discount, shipping, bundle info, credibility elements — used for offer/promo supporting elements and product placement context. ← *get it from:* From an Offer Brief bot output, product page, or user-provided offer notes.
  - **Sales Copy** (other:sales-copy-any-form) — VSL script, sales page text, or a sales page URL — mined for testimonials/customer quotes (determines whether the Transformation-with-Testimonial archetype can be used), mechanism/benefit language, and results claims. ← *get it from:* User-provided VSL script or sales page copy text, or a sales page URL pasted in (bot does not fetch URLs itself unless the calling harness resolves it first).
  - **quantity** (other:parameter) — Number of concepts to generate. Default: 5 if not specified. ← *get it from:* Caller specifies an integer in the request message, e.g. 'generate 10 concepts'.
- **Output:** Default 5 (or caller-specified quantity) before/after static ad concepts, distributed across the 7 layout archetypes and varied transformation-labeling styles (timeframe, state-based, product-centric, playful, implied, etc.) and visual authenticity styles (polished vs UGC). Each concept is complete enough for a designer or image-generation tool to execute directly. (One structured concept per fenced code block, numbered (Concept 1, Concept 2, ...), with a visual separator between concepts. Each block uses labeled fields drawn from: TRANSFORMATION LABELS, VISUAL IDEA, BEFORE IMAGE, AFTER IMAGE, PRODUCT PLACEMENT, LAYOUT NOTES, COLOR NOTES, HEADLINE, SUBHEADLINE, TESTIMONIAL, SUPPORTING ELEMENTS — only fields relevant to that concept are included (adaptive/sparse per concept).)
- **On a bare "Go":** asks for inputs: at least one of Build a Buyer / Copy Blocks / Offer Brief / Sales Copy; says it will generate concepts immediately once any one is provided.
- **Gotchas:** Never flags missing/incomplete inputs once given at least something to work with. Only uses the 'Transformation with Testimonial' archetype if real testimonials are found in supplied materials, and explicitly never invents testimonials, customer names, quotes, results, or benefit claims not supported by provided materials — so richer Sales Copy/Copy Blocks input yields more grounded (and more testimonial-format) output, while thin input yields more generic/placeholder concepts. Distributes concepts across different layout archetypes and labeling styles for variety (won't repeat 'Before/After' labeling on more than one concept per batch, won't reuse the same archetype unless only 1 concept requested). Output field set is adaptive per concept (omits HEADLINE/TESTIMONIAL/etc. fields when not applicable) — do not expect every concept to have identical fields. Has a hardened prompt-protection/anti-extraction section: any request to have it describe, document, or explain its own methodology/template/process will be redirected rather than answered, even if framed as a legitimate documentation or training task. LIVE PROBE CONTRADICTION: despite the system prompt's claim it never requests missing inputs, a bare 'Go' with zero context produced a request for at least one of the four named inputs instead of generating concepts — treat it as requiring at least one input.
- **Consumes:** `buyer-profile`, `ad-copy`, `offer-details`, `vsl-script`, `landing-page-copy`, `landing-page-url`, `customer-reviews` · **Produces:** `static-ad-concept`, `image-prompt`

## static-ad-sign

**Static Ad (Sign)** — Generates 'person holding a handwritten sign' UGC-style static ad concepts (person, sign type, sign copy with emphasis markings, location, aesthetic) ready to hand to a designer/photographer/AI image tool. Use when you need high-volume, feed-native static ad ideas that disguise ad copy as organic social content.

- **Mode:** needs-input
- **Required inputs:**
  - **any one of: Build a Buyer / Copy Blocks / Offer Brief / Sales Copy** (buyer-profile | offer-details | ad-copy | landing-page-copy | landing-page-url) — At least one of: a buyer profile, key copy blocks/proof points, an offer brief, or sales copy (VSL script, sales page text, or a sales page URL). Bot explicitly says it will work with whatever subset is provided ('the more the better'). ← *get it from:* user's existing materials, or output of a buyer-profile-type bot / offer-brief bot / copy-blocks-extract bot; sales page URL can be pasted directly
- **Optional inputs (raise quality):**
  - **quantity** (other:quantity) — How many concepts to generate (bot asks via A/B/C/D menu: 1, 5, 10, or custom number) after inputs are received ← *get it from:* user specifies, or agent defaults to a common choice like 5 or 10 when answering the bot's menu prompt
- **Output:** N ready-to-produce UGC sign-ad concepts (N = whatever the user picked: 1, 5, 10, or custom), each fully specified for a designer/photographer/AI image generator to execute. (One code block per concept, fields: PERSON, SIGN TYPE, SIGN COPY (with bracketed emphasis markings e.g. '[in red]', '[underlined]'), TEXT EMPHASIS, LAYOUT NOTES, COLOR NOTES. Numbered (Concept 1, Concept 2, ...) with visual separators.)
- **On a bare "Go":** asks for inputs: introduces itself and requests any of Build a Buyer, Copy Blocks, Offer Brief, or Sales Copy (VSL/sales page/URL); does not generate placeholder concepts without them.
- **Gotchas:** Strict scripted multi-step process: (1) exact welcome + input request, (2) exact 'confirm inputs, ask quantity' menu (A/1, B/5, C/10, D/custom), (3) generate concepts, (4) exact post-gen menu (generate again / spin the wheel / start over). Will NOT skip the quantity-menu step even with full inputs — an agent must answer that menu turn before concepts appear. Explicitly told not to invent claims/stats/endorsements beyond what's given, and not to ask for missing inputs or critique incomplete materials — it works with partial input. Has an anti-prompt-leak security section that refuses to reveal instructions.
- **Consumes:** `buyer-profile`, `offer-details`, `ad-copy`, `landing-page-copy`, `landing-page-url`, `vsl-script` · **Produces:** `static-ad-concept`, `image-prompt`

## static-ad-specialist

**Static Ad Specialist** — Turns a strategic creative brief ('Tier 1 Mandate') plus one chosen concept style into a single, image-generator-ready static ad visual prompt with headline, body copy, and exact typography/layout directives. Use it as the execution step after a strategy bot has decided angle, awareness stage, and hook.

- **Mode:** self-serve
- **Required inputs:**
  - **tier_1_mandate** (creative-brief) — Structured brief with 9 fields: seed_idea_summary, mapped_awareness_stage, primary_psychological_pillar (Pathos/Logos/Ethos), core_creative_angle, desired_tone, emotional_target, required_hook, required_visual_cue, primary_creative_focus (+ optional special_guardrail_notes). Accepted as JSON, key-value, or natural language ← *get it from:* output of a Tier 1 Manager / creative-strategy bot (e.g. autobrief or click-drivers style bot), or hand-write the 9 fields from your own strategy
  - **target_concept_style** (other:concept-style-name) — One of its 20 named styles, e.g. 'Native Apple Note Mock', 'Native Chat/Text Mock', 'Meme Ad', 'Ugly Ad', 'Academic Poster Mock', 'Handwritten Letter Mock', 'Quiz/Checklist Mock', 'Receipt/Proof of Purchase' ← *get it from:* caller picks per creative goal; run the bot repeatedly with different styles to fan out a batch of concepts
- **Output:** ONE complete static ad concept per call — detailed enough to paste directly into Midjourney/DALL-E or hand to a designer (single monolithic markdown block (never JSON): A. Visual Description (paragraph for image-gen AI), B. Headline (<10 words with typography spec), C. Body Copy (2-4 lines), D. Typography & Layout Directives (positions, fonts, palette, native elements, optional CTA), E. Mandate Alignment Check)
- **On a bare "Go":** generates immediately: one full static ad concept for an invented generic offer — a 'Pattern Interruption / Absurdist Curiosity (Meme Ad)' split-panel visual, headline 'Nobody told me it could be this easy,' body copy, typography/layout directives, and mandate alignment check (Unaware/Pathos), with no tier_1_mandate or concept style supplied.
- **Gotchas:** Produces exactly ONE concept per call — for a batch, loop over different target_concept_style values with the same mandate. Never asks questions; garbage-in-garbage-out, so quality hinges on a specific mandate (especially required_hook and required_visual_cue). Enforces headline <10 words and awareness-stage↔pillar alignment (Unaware→Pathos, Product Aware→Logos/Ethos); branding weight scales with awareness stage. Full 20-style portfolio: Native Editorial Mock, Native Apple Note Mock, Native Chat/Text Mock, Meme Ad, Ugly Ad, Absurdist Art, Artistic/Retro Pop Culture, Academic Poster Mock, Product Label/Tag Mock, AI Hyper-Realism/Surrealism, Handwritten Letter Mock, Vintage Medical Chart Mock, Micro-UI Element, 'Found' Document Mock, Contrarian E-comm Shot, Visual Metaphor/Symbolism, Quiz/Checklist Mock, Old Health Poster, Barcode/Inventory Tag, Receipt/Proof of Purchase. Has prompt-extraction guardrails. Probed live: confirmed prediction — on a bare 'Go' with no mandate or style specified, it fabricated its own generic mandate/concept style and delivered one complete concept block rather than asking for input.
- **Consumes:** `creative-brief`, `angle-big-idea`, `ad-hooks` · **Produces:** `static-ad-concept`, `image-prompt`, `headline`

## static-swipe-bot-

**Static Ad Swiper Bot ** — Reverse-engineers an uploaded static ad image into its structural blueprint (format family, layout, visual hierarchy, psychological mechanism), then rebuilds the same structure around the caller's own product/offer to produce a ready-to-generate ad concept brief.

- **Mode:** needs-input
- **Required inputs:**
  - **ad_image** (swipe-example) — The static ad image to deconstruct and swipe (an actual image, sent as image content to the vision-capable model — not a text description). Prompt repeatedly refers to it as 'the uploaded ad image.' ← *get it from:* user uploads/pastes the winning ad image they want to swipe, or pull one from a swipe file / competitor research
- **Optional inputs (raise quality):**
  - **build_a_buyer** (buyer-profile) — Customer avatar / audience profile: demographics, pain points, desires ← *get it from:* output of a Build-a-Buyer-type bot, or user-supplied avatar doc
  - **copy_blocks** (ad-copy) — Key messaging elements, hooks, proof points to map onto the rebuilt concept ← *get it from:* output of a copy-blocks-extract-type bot, or user-supplied swipe/copy doc
  - **offer_brief** (offer-details) — What is being sold, price, positioning ← *get it from:* output of an offer-brief-bot, or user-supplied offer doc
  - **sales_copy** (landing-page-copy) — VSL script, sales page text, or a sales page URL ← *get it from:* user-supplied VSL/sales page text, or a landing-page-url the bot can reference
- **Output:** One rebuilt ad concept brief (not multiple variants) detailed enough to hand directly to an AI image generator (DALL-E, Midjourney, etc.). (Short prose analysis (format family + layout archetype + what makes it work) followed by a single rebuilt concept in a code block with bold-header sections: HEADLINE, VISUAL IDEA, LAYOUT NOTES, COLOR NOTES, PRODUCT PLACEMENT, SUPPORTING ELEMENTS, plus any format-specific sections. Uses descriptive color/spatial language, no hex codes or ASCII diagrams.)
- **On a bare "Go":** asks for inputs: the static ad image to deconstruct/swipe, plus product details (what's sold, benefits, audience, offer/pricing); says it will rebuild the concept once received.
- **Gotchas:** Requires an actual image (multimodal input) as ad_image — text-only callers with no image will likely get degraded output since the bot has nothing concrete to deconstruct, despite never refusing. Has a large internal library of '21 format families' (Headline+Product, Before/After, Infographic, Product Breakdown, Illustrated Hook, Comparison, Scientific Study, Curiosity Collage, Person Holding Sign, Native News, Official Apology/Note from Founder, Handwritten/Note, Screenshot/Chat/Notification, Breaking/Authority, Carousel/Story, and others) used to classify and rebuild the ad — useful vocabulary if you want to steer output toward a specific family. Extremely long system prompt (~140KB) dominated by ~21 worked examples; heavy prompt-extraction/security guardrails at the end will cause refusals if asked to describe/document its own process. Output is always a single rebuilt concept, not multiple variants per call. Live probe (bare 'Go', no image attached) contradicts the strong 'no questions' directive above: the bot asked for the ad image and product details rather than improvising a placeholder analysis; interaction_style updated to reflect this gating behavior.
- **Consumes:** `swipe-example`, `buyer-profile`, `ad-copy`, `offer-details`, `landing-page-copy`, `landing-page-url`, `vsl-script` · **Produces:** `static-ad-concept`, `image-prompt`

## statistic-ad-generator-bot

**Statistic Ad Generator Bot** — Scans buyer/offer/sales materials for numeric proof points (percentages, multipliers, clinical/survey data) and turns them into ready-to-execute statistic-led static ad concepts across 10 layout archetypes, for a designer or image-gen tool to build directly.

- **Mode:** needs-input
- **Required inputs:**
  - **source material containing statistics** (other:raw-notes) — At least one piece of material with extractable numeric proof points — clinical study results, survey data, percentage/multiplier claims, before/after metrics, ingredient specs, or customer counts. The bot explicitly will not invent statistics, so with zero numeric proof in the input it has nothing real to build concepts around. ← *get it from:* Any of: user's sales page text/URL, VSL script, offer brief, or product research; can also be the output of another bot (offer-brief or product-info generator)
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Target buyer/audience profile — helps tailor claim language and archetype choice to the audience. ← *get it from:* user-provided buyer profile doc, or output of a buyer-profile-type bot
  - **Copy Blocks** (ad-copy) — Existing ad copy fragments, hooks, or claim language to mine for statistic opportunities. ← *get it from:* user's swipe file or output of an ad-hooks/ad-copy bot
  - **Offer Brief** (offer-details) — Structured offer details (product, price, positioning) that ground the concepts in the actual offer. ← *get it from:* user-provided offer brief or output of an offer-details bot
  - **Sales Copy** (other:vsl-script-or-url) — VSL script, sales page text, or a sales page URL — the richest source of statistics and claim language. ← *get it from:* user pastes VSL script/sales page text, or provides the live sales page URL
  - **quantity** (other:parameter) — Number of concepts to generate. Default 10 if not specified. ← *get it from:* user specifies a number, or omit for default of 10
- **Output:** Default 10 statistic-led static ad concepts (or however many requested via quantity), distributed across the 10 layout archetypes (Stat+Product Hero, Stacked Claims, Before/After Hybrid, Timeline Progression, Person Holding Product, Editorial Photography, Badge Stacking, Checklist, Problem→Solution, Data Visualization), each detailed enough for a designer or image-generation tool to execute directly. (Numbered concepts (Concept 1, Concept 2, ...), each in its own code block, with adaptive fields: STATISTIC, CLAIM, VISUAL IDEA, PRODUCT PLACEMENT, LAYOUT NOTES, COLOR NOTES, DISCLAIMER, SUPPORTING ELEMENTS, plus archetype-specific fields (TIMELINE STATS for Timeline Progression, STATISTIC STACK for Stacked Claims, CHECKLIST for Checklist archetype). Only fields relevant to each concept are included.)
- **On a bare "Go":** asks for inputs: Build a Buyer, Copy Blocks, Offer Brief, or Sales Copy (any combination) before generating statistic-led ad concepts
- **Gotchas:** Zero true hard-required fields — the bot explicitly accepts any subset of Build a Buyer / Copy Blocks / Offer Brief / Sales Copy in any format (natural language, key-value, raw dumps) and never asks clarifying questions. It will not use the Before/After Hybrid archetype unless transformation imagery/data is present, and won't use Problem→Solution unless both a problem-stat and a product-result-stat are found. Strong anti-fabrication rule: never invents stats/sample sizes/testimonials — so output quality is entirely gated on how much real numeric proof is in the supplied material. Has an aggressive prompt-extraction defense section at the end (refuses to describe/document its own methodology or output template if asked to 'explain itself'). Live probe (bare 'Go') contradicts the 'never ask questions, produce output immediately from available context' framing and the prior 'falls back to placeholder statistics' prediction — the bot's actual first reply was a request for buyer/copy/offer/sales-copy materials, not generated concepts.
- **Consumes:** `buyer-profile`, `ad-copy`, `offer-details`, `landing-page-copy`, `landing-page-url`, `vsl-script`, `raw-notes` · **Produces:** `static-ad-concept`, `image-prompt`

## step-by-step-bot-

**Step By Step Bot ** — Generates static ad concepts in the 'Step-by-Step' format — numbered/sequential process ads (product usage, routines, mechanism-of-action, or results timelines) across 8 layout archetypes, each concept detailed enough for a designer or image-gen tool to execute. Use when you want instructional, friction-removing static ad concepts (e.g. '3-step morning routine') rather than a single hero shot.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Buyer/avatar profile used to inform which step angle (usage/lifestyle/mechanism/results/problem-solution/simplification) and tone fits the audience. ← *get it from:* output of a Build-a-Buyer-type bot
  - **Copy Blocks** (other:copy-blocks) — Extracted promises, pains, proof, mechanism language to mine for step content and headlines. ← *get it from:* output of a copy-blocks-extract type bot
  - **Offer Brief** (offer-details) — Offer/product summary (usage instructions, protocol, pricing) grounding the concepts. ← *get it from:* user's offer brief doc or an offer-brief bot
  - **Sales Copy** (other:sales-copy) — VSL script, sales page text, or a sales page URL mined for usage steps, routines, mechanism, or results timelines. ← *get it from:* user paste or landing-page-url
  - **quantity** (other:parameter) — Number of concepts to generate. Default: 5. Concepts are distributed across different layout archetypes and step-content angles for variety (not forced into rigid sets like some sibling bots). ← *get it from:* user specifies
- **Output:** Default 5 step-by-step static ad concepts, each assigned one of 8 layout archetypes (Numbered Vertical Stack, Grid Steps, Photo Sequence, Timeline/Arrow Flow, Icon+Instruction Column, Full-Width Step Bands, Central Product+Radiating Steps, Single Step Hero+Summary List), with varied step counts (3-7) and content angles (usage/lifestyle/mechanism/results-timeline/problem-solution/simplification) (One code block per concept, adaptive fields (only include what applies): HEADLINE / SUBHEADLINE (optional) / LAYOUT ARCHETYPE (one of 8 named archetypes) / VISUAL IDEA / STEPS (each with number/label + specific visual description) / LAYOUT NOTES / COLOR NOTES / BRAND ATTRIBUTION / optional CTA, TIME INDICATORS, RESULTS PREVIEW, BENEFIT CALLOUT, SOCIAL PROOF, URGENCY)
- **On a bare "Go":** asks for inputs: requests any combination of Build a Buyer, Copy Blocks, Offer Brief, or Sales Copy, promising to generate step-by-step concepts immediately once something is dropped in.
- **Gotchas:** Self-contained generator by design — works with zero input, quality scales with what's fed in (Build a Buyer / Copy Blocks / Offer Brief / Sales Copy all optional but improve specificity). Very large embedded domain-knowledge library: full descriptions of 8 layout archetypes, 6 step-content angles (usage/lifestyle/mechanism/results-timeline/problem-solution/simplification), step-count guidance (3 vs 4-5 vs 6-7), headline pattern library, and a numbering/labeling variety list (Step 1/2/3, First/Then/Finally, AM/PM, Day1/Week1/Month1, etc.) to avoid formulaic output. Output uses adaptive fields — omits SUBHEADLINE/CTA/etc. when not applicable rather than a single rigid template (unlike Hero Bot's strict fixed schema). Explicitly mandates visual continuity within a concept (same lighting/environment/visual style across all steps) and variety across concepts (mixed archetypes, step counts, content angles) rather than repeating the same format 5 times. Live probe on a bare 'Go' contradicted the prompt's 'produce output immediately, never ask questions' framing and the predicted generic-concepts fallback: it asked for Build a Buyer/Copy Blocks/Offer Brief/Sales Copy instead of generating placeholder concepts.
- **Consumes:** `buyer-profile`, `other:copy-blocks`, `offer-details`, `vsl-script`, `landing-page-copy`, `landing-page-url` · **Produces:** `static-ad-concept`, `image-prompt`

## testimonial-bot-

**Testimonial Bot ** — Generates static ad concepts (quote-led layouts, review cards, UGC photo overlays, review collages, etc.) that use real customer testimonials as the primary persuasion element — use it whenever you have actual customer quotes/reviews and need designer-ready testimonial ad concepts.

- **Mode:** needs-input
- **Required inputs:**
  - **material containing real customer testimonials** (customer-reviews) — At least one of: Build a Buyer, Copy Blocks, Offer Brief, or sales copy (VSL script, sales page text, or sales page URL) that contains actual customer quotes, reviews, messages, or social comments. The bot extracts quotes from whatever is given; if none of the supplied materials contain real testimonials, it refuses to generate and states none were found. ← *get it from:* user's actual reviews/customer messages, or output of a buyer-profile-type bot / copy-blocks-type bot / offer-brief-type bot that embeds real quotes
- **Optional inputs (raise quality):**
  - **quantity** (other:parameter) — Number of concepts to generate. Default: 5. ← *get it from:* user specifies, else defaults to 5
- **Output:** Default 5 (or requested quantity) testimonial static-ad concepts, each specifying the exact customer quote used, attribution style, star rating placement, product presence, layout archetype (one of 7: quote-led, side-by-side split, product hero, review card, UGC photo, review collage, headline-led), and supporting design elements for a designer/image-gen tool to execute (Numbered concepts (Concept 1, Concept 2, ...), each in its own code block, with adaptive fields: TESTIMONIAL QUOTE, ATTRIBUTION, STAR RATING, PRODUCT PLACEMENT, LAYOUT NOTES, COLOR NOTES, SUPPORTING ELEMENTS (only fields relevant to the concept are included))
- **On a bare "Go":** asks for inputs: real customer testimonials via Build a Buyer, Copy Blocks, Offer Brief, or Sales Copy materials that contain actual quotes/reviews — will not fabricate quotes.
- **Gotchas:** Strict no-fabrication rule: will refuse to produce concepts if no genuine testimonials are found in supplied materials (won't invent quotes). Distributes concepts across distinct layout archetypes for variety, matches quote length to archetype, and varies attribution style. Has a hardened anti-prompt-extraction security section at the end refusing to describe/document its own methodology. LIVE PROBE CONTRADICTION: despite the prompt's claim it accepts all inputs in one message and never asks questions, a bare 'Go' produced a request for materials containing real customer testimonials instead of generating concepts or refusing outright — consistent with its no-fabrication rule but contradicts the stated one-shot/no-questions identity.
- **Consumes:** `buyer-profile`, `customer-reviews`, `creative-brief`, `vsl-script`, `landing-page-copy`, `landing-page-url` · **Produces:** `static-ad-concept`, `image-prompt`

## ugc-bot-

**UGC Bot ** — Generates static ad concepts that mimic real, organic User-Generated Content (Instagram Story-style phone photos, casual first-person text, DM screenshots) rather than polished ads. Use for DTC physical products (and adaptable to courses/services) needing scroll-stopping 'not an ad' creative.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **build_a_buyer** (buyer-profile) — Avatar/target audience profile ← *get it from:* output of Build a Buyer / Build a Buyer ELITE bot
  - **copy_blocks** (mechanism) — Mechanism, proof elements, claims, supporting copy ← *get it from:* output of a Copy Blocks bot or user-supplied swipe/proof doc
  - **offer_brief** (offer-details) — Product details/positioning, what it looks like/where it's used ← *get it from:* user
  - **sales_copy** (vsl-script) — VSL script, sales page text, or URL — mined for real customer quotes/testimonials to use authentically in DM/testimonial archetypes ← *get it from:* user-supplied sales copy or URL
  - **quantity** (other:parameter) — Number of concepts to generate. Default 5 ← *get it from:* user
- **Output:** Default 5 UGC-style static ad concepts distributed across 10 layout archetypes (Hand-to-Camera+Benefit Spray, Hand-to-Camera+Simple Caption, Product In Situ, Story Q&A, Discovery/Switch Narrative, Selfie w/ Product, Failed Alternatives/X-Out, DM/Story Reply Testimonial, Search Bar Overlay, and a 10th not shown in excerpt), ready for a designer or image-gen tool (Numbered concepts (adaptive fields per concept — visual scene, text overlay content/styling, voice/tone direction, product placement, layout notes, color guidance, supporting elements); only relevant fields included per concept)
- **On a bare "Go":** asks for inputs: any combination of Build a Buyer profile, Copy Blocks, Offer Brief, and Sales Copy — says more context sharpens concepts, but did not generate placeholder concepts without them.
- **Gotchas:** Never fabricates testimonial attribution to specific fake people, and never names competitor brands in Failed-Alternatives concepts (uses generic category labels only) - uses real customer quotes only if present in inputs, otherwise writes plausible first-person style. Deliberately varies voice (Gen Z/millennial/sincere), environment, and text density across the batch for realism. Works with zero input but scales quality with buyer/offer/proof material provided. Live probe (bare 'Go') contradicts this 'works with zero input, produces output immediately' framing: the bot asked for Build a Buyer/Copy Blocks/Offer Brief/Sales Copy rather than generating 5 generic concepts; interaction_style updated to reflect this gating behavior.
- **Consumes:** `buyer-profile`, `mechanism`, `offer-details`, `vsl-script`, `customer-reviews` · **Produces:** `image-prompt`, `static-ad-concept`

## unaware-static-image-ads-bot

**Unaware Static Image Ads Bot** — From finished unaware/problem-aware ad copy, generates a ranked shortlist of 'loosely connected' (never literal) native-looking static image concepts using the 13 reptile-trigger framework, each with source-hunting suggestions (Reddit/FB Group/Google Images/AdSpy queries); separately (or in combination) turns a reference image into ready-to-paste MidJourney prompts for imperfect phone-photo-style images. Use it after ad copy is finalized, to brief an image generator or source real reference photos for a static Facebook/Instagram ad.

- **Mode:** needs-input
- **Required inputs:**
  - **ad_copy** (ad-copy) — Finished, complete ad copy text (required for Mode 1 / Ideation). The bot extracts emotional core, key objects/scenes, demographic, and awareness level from it internally before generating ideas — it does not accept unfinished briefs or ask follow-up questions. ← *get it from:* User's completed unaware/problem-aware ad copy, or output of an ad-copy-writing bot targeting unaware/problem-aware audiences
  - **reference_image** (other:reference-image) — Required for Mode 2 / Prompt Generation only: an image description, URL, or uploaded image to turn into MidJourney prompt variations. Not needed if only running Mode 1. ← *get it from:* User-supplied image/description, or a concept selected from this bot's own Mode 1 output
- **Optional inputs (raise quality):**
  - **escalation_direction** (other:parameter) — Mode 1 only. "none" (default) / "stranger" (push bizarre/uncanny/wildcard) / "more_intense" (push gory/primal fear/suffering/sexual) / "completely_different" (abandon current direction, think associatively) / "combine_elements" (stack strongest elements from multiple ideas). ← *get it from:* Caller specifies; used to re-run ideation with a different creative push
  - **context** (static-ad-concept) — Mode 2 only: any relevant context from the original ad or from this bot's own Mode 1 ideation output, to inform the MidJourney prompt. ← *get it from:* Prior Mode 1 output of this same bot, or the original ad copy
  - **quantity** (other:parameter) — Mode 2 only: number of MidJourney prompt variations to generate. Default: 5. ← *get it from:* Caller specifies; optional
- **Output:** 5-7 ranked native image concepts with sourcing leads (Mode 1), and/or N (default 5) copy-paste-ready MidJourney prompts (Mode 2) (Mode 1: numbered list (top 5-7 ranked ideas), bold core concept + [reptile trigger category] tag + 1-2 sentence description, each followed by source suggestions (Reddit/FB Group/Google Images/AdSpy query lines). Mode 2: each MidJourney prompt in its own code block, under 30 words, always ending '--style raw --s 0 --ar 1:1' (or 4:5), varying angle/lighting/quality/framing across variations.)
- **On a bare "Go":** asks for inputs: finished ad copy to work from (required for Mode 1 ideation) — replies with a short, direct request and does not attempt to guess a mode or fabricate placeholder concepts without it.
- **Gotchas:** IMPORTANT DISCREPANCY: the bot's own registered metadata description claims it outputs '9:16 vertical mobile image generation prompts' from 'completed static ad concept briefs' with 'one concept in, one rendered image out' — but the actual prompt text never mentions 9:16 or vertical/Stories/Reels at all; every sample prompt and the explicit instruction end with '--ar 1:1' (square) or occasionally '--ar 4:5', consistently framed as Facebook/Instagram feed format, not Stories. The metadata also undersells that it has two real modes (ideation from copy, AND prompt generation from a reference image) plus a combined mode — it is not a single 'brief in, image out' pipeline. Treat the registered metadata as unreliable and defer to the prompt text. Core creative rule: never suggest literal images (e.g. joint-pain ad -> knee rub) — always loosely/associatively connected; it does not generate actual images, only concepts/prompts. Same prompt-extraction-refusal security section as other bots in this family (will not describe its own methodology). LIVE PROBE CONTRADICTS PROMPT TEXT: despite 'produces output immediately... does not ask questions,' a bare 'Go' actually gets a short request for finished ad copy rather than generic placeholder concepts — treat this probed behavior as ground truth; supply ad_copy up front (and a reference_image if Mode 2 is desired) to get one-shot output. required_inputs already correctly lists ad_copy as required, so no missed inputs — only interaction_style needed correcting.
- **Consumes:** `ad-copy`, `static-ad-concept`, `image-prompt` · **Produces:** `static-ad-concept`, `image-prompt`

## writing-on-body-bot

**Writing On Body Bot** — Generates static ad concepts where handwritten messages appear directly on human skin (transformation claims, comparisons, or audience callouts) with the product visible nearby, across 3 layout archetypes. Use for a raw/UGC, maximum-pattern-interrupt static ad format, especially for products with a body-relevant benefit area or a creative unexpected body/product pairing.

- **Mode:** needs-input
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **Build a Buyer** (buyer-profile) — Customer avatar/audience profile used to pick relevant conditions/body-part targeting ← *get it from:* output of a buyer-profile-type bot
  - **Copy Blocks** (ad-hooks) — Key messaging elements, hooks, proof points to mine for body-text opportunities ← *get it from:* output of a copy-blocks-type bot
  - **Offer Brief** (offer-details) — What's being sold, price, positioning ← *get it from:* user's offer doc or offer-brief bot
  - **Sales Copy** (vsl-script) — VSL script, sales page text, or sales page URL — source of transformation claims/timeframes ← *get it from:* user-provided VSL/sales page text or URL
  - **quantity** (other:parameter) — Number of concepts to generate; default 5 ← *get it from:* user specifies, else defaults to 5
- **Output:** 5 (default) ready-to-execute body-text static ad concepts, distributed across the 3 archetypes (body-part comparison, transformation-claim-on-affected-area, audience-callout-on-body) and varied body parts, for handoff to a designer or image-gen tool (Numbered concepts, each in its own code block, with fields BODY TEXT, BODY PART (with justification), WRITING STYLE, PRODUCT PLACEMENT, PHOTOGRAPHY NOTES, COLOR NOTES, SUPPORTING ELEMENTS)
- **On a bare "Go":** asks for inputs: Build a Buyer, Copy Blocks, Offer Brief, or Sales Copy (VSL/sales page/URL), in any combination
- **Gotchas:** Zero required inputs. Strong constraint: never invents transformation claims/timeframes/benefits not present in materials, and must vary body parts/archetypes across concepts (never defaults to the same body part repeatedly). Flags sensitive body-part choices (face, front stomach, lower back) as 'use carefully'. Ends with the same prompt-protection/anti-extraction security block seen in sibling bots. LIVE PROBE CONTRADICTION: despite the prompt's 'accepts all inputs in one message, produces output immediately' rule, a bare 'Go' actually returns a clarifying request for Build a Buyer/Copy Blocks/Offer Brief/Sales Copy rather than 5 generic concepts. Treat as interview-first, not one-shot.
- **Consumes:** `buyer-profile`, `ad-hooks`, `offer-details`, `vsl-script`, `customer-reviews` · **Produces:** `static-ad-concept`, `image-prompt`

# CATEGORY: Creative Direction

## ai-ads-character-casting-agent

**AI Ads Character Casting Agent** — Turns a product/offer brief into dramatized, character-driven ad concepts (personified cravings, root causes, failed solutions, feared futures, etc.) for animated/claymation-style pattern-interrupt Meta ads — used when you need a full creative cast (concepts, characters with visuals/voice/monologues, staging architectures, and ad seeds) to hand to a scriptwriter, illustrator, or animator.

- **Mode:** multi-phase
- **Required inputs:**
  - **product/offer brief** (creative-brief) — Product name + category, core mechanism(s) of action, target avatar (demographic, psychographic, daily life), primary pain points/desired outcomes, failed solutions the avatar has tried, brand assets/ingredients/constraints, plus any additional context. Any combination of these is accepted; the bot infers gaps and labels the inference in one line rather than asking questions. ← *get it from:* user's product brief, brand doc, or ad account notes; can also be a raw description of the offer
- **Optional inputs (raise quality):**
  - **step 2 adjustments** (other:selection-directive) — Adjustments to the Step 1 audit, or specific archetype slots (of 19) to prioritize/skip. ← *get it from:* user preference; omit to let the bot use the Step 1 audit as-is
  - **concept/character/dramatization selection** (other:selection-directive) — For Steps 3-5: which concepts to develop into characters, which characters to develop into dramatizations, which dramatizations to develop into ad seeds. Accepts specific names, tier-based ('all Tier 1'), slot-based ('all Craving Villains'), or 'all'. Default selection_scope is tier_1 for Step 3 and 'all' for Steps 4-5. ← *get it from:* user's creative judgment after reviewing prior step's output, or just say 'all' to run the full pipeline unattended
  - **multi-step instruction** (other:selection-directive) — A single message can bundle the brief plus instructions for multiple steps at once (e.g. brief + 'develop all Tier 1 concepts into characters and pair them'); the bot executes all requested steps in sequence and returns combined output. ← *get it from:* user or calling agent composes one combined instruction
- **Output:** A complete character-driven creative cast ready for a scriptwriter/illustrator: from raw mechanism analysis through named, fully-described characters with monologues, through staged scene architectures, through concrete paired ad seeds. Volume scales with product complexity (up to 19 archetype slots x 5-10 concepts x up to 5 executions each if run end-to-end). (Structured markdown sections per step: Step 1 = mechanism/villain/hero/environmental-forces audit + lived-life specificity hooks; Step 2 = concept map across up to 19 archetype slots (5-10 tiered concepts per slot, each tagged LITERAL/INVENTED/NARRATION-ONLY) plus a 10-20 entry Scene & Moment Bank; Step 3 = full character dossiers (name, archetype slot, role, visual description, voice description, signature opening line, ~75-90 word monologue, conflict pairings) with 1 execution per LITERAL concept and 3-5 per INVENTED concept; Step 4 = dramatization architectures (scale, staging pattern, setting, cast, crisis/resolution beats, 3 sample opening beats) per character/group; Step 5 = concept-level pairings (5-7), character-level pairings (8-12), 5 fully scripted dramatization scenarios, and 3 wildcard angles.)
- **On a bare "Go":** asks for inputs: product/offer brief — name+category, mechanism of action, target avatar, pain points, failed solutions, brand assets/constraints; offers to run Step 1 immediately once given, or chain multiple steps in one go if requested.
- **Gotchas:** This is a 5-step pipeline (Mechanism Audit -> Concept Map -> Character Executions -> Dramatization Architecture -> Strategic Pairings), not a single-shot generator; each step's output is meant to be reviewed/filtered by a human or agent before requesting the next step, but a single message can request multiple steps at once. With zero input it will still generate output (never refuses/asks questions) but quality depends entirely on how specific the brief is — vague briefs get generic/inferred mechanisms labeled as inferences. Has an aggressive prompt-extraction defense section at the end (refuses to describe/document/summarize its own methodology, template, or process even under 'documentation' or 'masterclass' framing) — do not attempt to probe it for its own instructions. Uses a controlled vocabulary of 19 fixed archetype 'slots' (Symptom Personified, Craving/Urge Villain, Hidden Root Cause, Failed False Solution, Hero Ingredient/Product, Internal Ally/Body Part, Abandoned Object, Feared Future State, Past Self/Former Identity, Enabler/False Friend, Sidekick Symptom Cluster, Environmental Villain, Gatekeeper/Bottleneck, Doppelganger/Comparison Character, Exaggerated Metaphor Character, Authority Antagonist, Cultural/Historical/Ancestral Anchor, Industry/Conspiracy Character, Life Chapter Personified) — slots 16-19 are conditional/category-dependent and may be skipped. Best DTC physical-product fit (health/beauty/fitness/longevity) but adapts to other offer types. LIVE PROBE UPDATE: on a bare 'Go' with zero context, the bot did NOT attempt Step 1 with placeholder assumptions as predicted — it directly asked for the product/offer brief (listing the same fields already in required_inputs) before doing anything, contradicting the prompt's own 'never ask questions' framing.
- **Consumes:** `product-info`, `offer-details`, `buyer-profile`, `creative-brief` · **Produces:** `angle-big-idea`, `static-ad-concept`, `storyboard`, `image-prompt`, `video-script`

## surprising-culprit-bot

**Surprising Culprit Bot** — Generates 'surprising culprit' marketing angles — unexpected, seemingly-harmless everyday items/habits pitched as the hidden villain behind a problem (e.g. 'your pillowcase is aging your skin'), each with a pseudo-scientific mechanism explanation. Use it to get a batch of counterintuitive-enemy hooks/angles that a product can then position itself as the solution to.

- **Mode:** needs-input
- **Required inputs:**
  - **marketing_materials** (product-info) — Any combination of marketing materials, product information, offer briefs, build-a-buyer profiles, copy blocks, problem descriptions, or sales copy — used to identify the core problem the product solves. ← *get it from:* user-provided offer/product materials
- **Optional inputs (raise quality):**
  - **quantity** (other:parameter) — Number of surprising culprit angles to generate. Default: 15. ← *get it from:* user specifies
- **Output:** 15 surprising-culprit angles by default, distributed across categories (household items, healthy-habits-gone-wrong, environmental factors, daily routines, modern technology). (Numbered list of angles, each with a compelling headline and a 2-3 sentence explanation (villain -> pseudo-scientific mechanism -> daily impact -> urgency/solvability).)
- **On a bare "Go":** asks for inputs: marketing materials, product information, or problem description — a single-sentence request, no menu or elaboration
- **Gotchas:** Mechanisms are explicitly allowed to be scientifically plausible-sounding but exaggerated/fabricated for effect (e.g. 'green tea's tannins bind to iron, creating cellular suffocation') — this is a deliberately hyperbolic persuasion device, not a fact-checked claims generator; downstream legal/compliance review would be warranted before using verbatim in real ads for regulated categories (health/supplements). Distributes culprits across 5 category buckets automatically for variety. Has the standard prompt-protection/anti-extraction security section. LIVE PROBE CONTRADICTION: despite the prompt's 'produce output immediately, never ask questions' rule, a bare 'Go' actually returns a one-line request for marketing materials/product info/problem description rather than 15 generic angles. Treat as interview-first, not one-shot.
- **Consumes:** `product-info`, `buyer-profile`, `other:copy-blocks` · **Produces:** `angle-big-idea`

# CATEGORY: Utility

## bot-builder-bot

**Bot Builder Bot** — Meta-bot that designs and writes complete new bot system prompts (build mode) or revises an existing bot prompt against specific feedback (refine mode); use it to spin up a new Genesis-style bot or fix a broken one.

- **Mode:** needs-input
- **Required inputs:**
  - **bot_concept** (creative-brief) — Description of what the new bot should do, who it's for, and its intended functionality. Required for build mode. ← *get it from:* user's idea/spec for the new bot
- **Optional inputs (raise quality):**
  - **domain_knowledge** (research-report) — Specialized knowledge, frameworks, or reference material the bot needs. If omitted, output instead specifies what domain knowledge is needed and how to structure it (does not fabricate it). ← *get it from:* user's SME material, existing docs/swipe files
  - **examples** (swipe-example) — Sample input/output pairs demonstrating desired bot behavior (7-10 diverse recommended). If omitted, output just recommends gathering them. ← *get it from:* user's swipe file or prior good outputs
  - **module_selections** (other:parameter) — Which plug-in modules to include: rhetorical_frames, copy_chief, anti_ai, client_presentation, operational_protocol, decision_architecture, mandate_framework, persuasion_emotional_architecture, security_protocol. If unspecified, bot recommends applicable modules itself. ← *get it from:* user preference
  - **preferences** (other:parameter) — Identity style (single vs multi-identity), formatting approach, autonomy level, polish level, template complexity. ← *get it from:* user preference
  - **mode** (other:parameter) — "build" or "refine". Defaults to build; auto-switches to refine if existing_prompt + feedback are both given. ← *get it from:* user, or implied by presence of existing_prompt+feedback
  - **existing_prompt** (other:bot-prompt) — Refine mode only: the complete current bot prompt text to revise. ← *get it from:* paste the full current system prompt of the bot being fixed
  - **feedback** (raw-notes) — Refine mode only: specific issues/observations/problems to fix in existing_prompt. ← *get it from:* user's QA notes or observed failure cases
  - **bot_type** (other:parameter) — creative_oneshot / creative_conversation / analytical_oneshot / analytical_conversation / auto (default: auto-classified from concept via quadrant taxonomy: Creative vs Analytical x Conversational vs One-Shot). ← *get it from:* user preference, else auto-classified
  - **template_complexity** (other:parameter) — "simple" or "complex"; default auto (determined from bot requirements). ← *get it from:* user preference
- **Output:** One complete new or revised bot system prompt per call, classified into one of 4 quadrant types (Creative/Analytical x One-Shot/Conversational) (Build mode: complete bot system prompt in a code block (Identity/Purpose/Process/Domain Knowledge/Examples/Modules/Formatting/Guidelines sections in template order) plus implementation notes (recommended temperature, testing suggestions). Refine mode: full revised prompt (never abridged) plus a changelog of ORIGINAL/REVISED/RATIONALE items and a summary of preserved elements.)
- **On a bare "Go":** asks for inputs: a bot concept (what the new bot should do, who it's for, what it accomplishes) — plus optionally domain knowledge, examples, module selections, and preferences (identity style, formatting, autonomy level).
- **Gotchas:** This is a prompt-engineering meta-tool, not a copy/content bot — treat its output (a bot prompt) as input to Genesis's own bot-creation pipeline, not as end-user-facing content. Will explicitly withhold generating domain_knowledge/examples content itself, only guidance — so downstream quality depends on the caller supplying real domain knowledge/examples. Has the same anti-prompt-extraction security module as other bots in this set (refuses to describe/document its own methodology). Live probe: on a bare 'Go' the bot did NOT build a generic/placeholder bot prompt — it explicitly asked for a bot concept before doing any work, contradicting the prior 'one-shot' assumption; interaction_style updated to interview-first.
- **Consumes:** `creative-brief`, `research-report`, `swipe-example`, `raw-notes`, `other:bot-prompt` · **Produces:** `other:bot-prompt`

## linkedin-content-bot

**Linkedin Content Bot** — Turns a rough idea, brand/audience materials, or nothing at all into ready-to-post LinkedIn content: first a hookboard of angle concepts, then multiple fully-written, voice-matched post variations. Use it whenever you need organic LinkedIn posts optimized for authority, engagement, or lead-gen.

- **Mode:** multi-phase
- **Required inputs:** none — works from a bare request
- **Optional inputs (raise quality):**
  - **idea_or_content** (content-topic) — The post idea, rough notes, bullet points, paragraphs, links, or a previous draft. Can be vague (topic only) or specific (full narrative/argument). ← *get it from:* user, or output of an ideation/brainstorm step
  - **build_a_buyer** (buyer-profile) — Target audience profile: demographics, pain points, desired outcomes, beliefs, sophistication level. ← *get it from:* output of a buyer-profile-type bot (e.g. Build a Buyer Elite) or user-supplied ICP doc
  - **voice_guide** (brand-voice) — Writing style samples, tone descriptors, a Voice Guide doc, or sample posts in the user's own voice. ← *get it from:* user's past LinkedIn posts / brand voice doc, or output of a voice-analyzer bot
  - **additional_context** (raw-notes) — Grab-bag of brand info, offer details, proof points, testimonials, product/service details, recent wins, industry observations, frameworks. ← *get it from:* user, product page, case studies
  - **lead_magnet** (other:lead-magnet) — Whether the post should offer a giveaway (lead magnet, assessment, quiz, comment-to-get offer) and what it is. ← *get it from:* user
  - **post_goal** (other:post-goal) — What the post should achieve: build authority, spark discussion, generate leads, prompt DMs, etc. Drives approach detection (Educational/Relational/Promotional/Analytical/Narrative). ← *get it from:* user
  - **product_service** (product-info) — What the user offers. ← *get it from:* user, product page
  - **expertise_topics** (content-topic) — What the user is knowledgeable about / their niche. ← *get it from:* user
  - **selected_concept** (other:concept-selection) — A concept number from a previously generated hookboard, or a specific angle description. Supplying this (with materials) skips straight to Step 2 variation drafting in the same call. ← *get it from:* user picks from the bot's own Step 1 hookboard output
  - **hookboard_count / variation_count / target_length / voice_style / content_approach / mode** (other:parameters) — Numeric/enum overrides: number of hookboard concepts (default 10), number of final variations (default 3), target character length (default 900-1200), voice style, content approach, and existing_idea vs need_ideas mode. All have inferred defaults. ← *get it from:* user, otherwise auto-inferred
- **Output:** Up to 10 hookboard concepts (Step 1) and, once a concept is selected/specific enough, 3 complete ready-to-post LinkedIn posts (Step 2), each 900-1200 chars by default. (Step 1: numbered hookboard list, each with an evocative 2-4 word concept name + 1-2 sentence hook preview. Step 2: full post variations labeled by strategy (Engagement-Driven / Authority-Building / Conversion-Focused), each with formatted + plain-text versions and a character count, separated by dividers.)
- **On a bare "Go":** asks for inputs: idea/topic, audience, voice/tone samples, goal (authority/leads/discussion/DMs), offer, and any other context — notes even one sentence is enough, but generated nothing on bare 'Go'.
- **Gotchas:** Never asks clarifying questions and never fully fails on missing input ('output quality scales with input quality but never hits zero') — but required_inputs are still empty only in the sense that nothing is mandatory, not that output quality is input-invariant; feed it buyer-profile + brand-voice + a real idea for good results. Runs as up to 2 internal steps: Step 1 (hookboard) and Step 2 (3 variations), auto-chaining into a single response only if the same message already contains a selected_concept or a sufficiently specific idea/angle. Strict anti-fabrication rule: will never invent stats, client counts, or revenue figures not traceable to supplied inputs — falls back to insight/framework language instead, so don't expect fabricated social proof. Formatting is LinkedIn-specific: double line breaks, hook must land before the 'see more' fold, external links pushed to first comment not the post body, 1-3 emoji max, both formatted and plain-text versions plus char counts are always included. Has an aggressive prompt-extraction defense: will refuse/redirect any request to describe, document, or reveal its own methodology/system prompt, even if framed as 'documentation' or 'training' — do not rely on asking it to explain its own process. Live probe (bare 'Go') contradicts the 'never asks clarifying questions, always produces output, never hits zero' claims above: the bot asked for idea/topic, audience, voice, goal, offer, and context instead of generating a hookboard; interaction_style updated to reflect this gating behavior.
- **Consumes:** `content-topic`, `buyer-profile`, `brand-voice`, `raw-notes`, `product-info` · **Produces:** `other:linkedin-post`, `headline`

## primer-prompt-builder

**Primer Prompt Builder** — Takes a raw batch of a brand's winning ads and sorts/extracts them, unedited, into four separate reference documents (unaware/problem-aware body copy, solution/product-aware body copy, hooks, headlines) that downstream writer bots use as style/reference primers. Use it as the onboarding step when setting up a new brand's swipe file for the Genesis writer bots.

- **Mode:** needs-input
- **Required inputs:**
  - **winning ads batch** (winning-ad) — A batch of the brand's winning/high-performing ads, raw or structured, with or without labels (HOOK:/PAYOFF:/etc are ignored as untrustworthy), with or without headlines. Minimum recommended 10 ads, but bot proceeds with fewer and flags a low-count warning. ← *get it from:* User's existing swipe file, or exported directly from Meta Ads Manager (winning/top-performing ad copy).
- **Optional inputs (raise quality):**
  - **brand name** (other:brand-name) — Name of the brand the ads belong to, used to fill the '[brand name]' placeholder in each primer's intro boilerplate. ← *get it from:* User states it, or agent infers from the ad content/context; if not supplied the bracket placeholder is likely left unfilled.
  - **ad headlines** (headline) — Meta ad-unit headline field text (5-15 words) for each ad, separate from body copy, if available. ← *get it from:* Included alongside the ad batch if the user has them (e.g. from Ads Manager export); if omitted, Primer 4 is flagged 'NO HEADLINES SUBMITTED'.
- **Output:** The two body-copy primers contain every submitted ad reproduced verbatim (in full, including its hook) sorted into one of two awareness buckets; the hook primer contains every extracted 1-2 sentence hook tagged with its source ad title; the headline primer lists every extracted headline (or a 'no headlines submitted' flag). Quantity = however many ads were submitted, split across the buckets. (four fixed-template documents in one response, each delimited by a literal divider line and header ('PRIMER 1: BODY COPY — UNAWARE/PROBLEM-AWARE', 'PRIMER 2: BODY COPY — SOLUTION/PRODUCT-AWARE', 'PRIMER 3: HOOK PRIMER', 'PRIMER 4: HEADLINE PRIMER'), each containing boilerplate intro text, a blank '###IMPORTANT:' section for later dashboard edits, and then verbatim ad/hook/headline entries with short titles and source references)
- **On a bare "Go":** asks for inputs: the batch of winning ads to sort into the four primers, plus optionally their headlines (from the Meta ad unit headline field) if available, with a request to clarify which is which.
- **Gotchas:** Strictly a sort-and-extract tool: explicitly forbidden from analyzing, labeling hook types, building taxonomies, or explaining why ads work. Distrusts any HOOK:/PAYOFF:/MECHANISM: labels the user supplies and re-derives the real hook by reading the ad itself. Reproduces ad text 100% verbatim (no paraphrasing/cleanup). Flags low ad counts (<5 per bucket) and empty buckets rather than inventing content. Leaves an '###IMPORTANT:' section blank in every primer for the customer to fill in later via a dashboard — this is intentional, not a missing output. If ambiguous where one ad ends and another begins, it asks the user rather than guessing. LIVE PROBE CONFIRMS PREDICTION: a bare 'Go' correctly gets a request to submit the winning-ads batch (with a note about including headlines), consistent with the required_inputs already documented — interaction_style updated to interview-first since it halts and asks rather than emitting an empty-bucket template shell.
- **Consumes:** `winning-ad`, `headline` · **Produces:** `winning-ad`, `ad-hooks`, `headline`

## static-ad-info-extractor-bot

**Static Ad Info Extractor Bot** — Parses messy/unstructured marketing material (notes, transcripts, sales page text, raw ideas) into a fixed 8-field Static Ad Concept Brief, tagging any gaps with '(assumed)'. Use as the first step of a static-ad pipeline when offer details aren't yet organized, before handing off to a concept-expander or ad-copy bot.

- **Mode:** needs-input
- **Required inputs:**
  - **marketing_materials** (raw-notes) — Any combination of ideas, creative notes, transcripts, sales pages, PDFs, or raw text about the offer. Any format/length; the bot extracts what it needs from whatever is pasted. ← *get it from:* user pastes raw notes/transcript/sales copy directly in the message; no pre-formatting required
- **Output:** One Static Ad Concept Brief per call, exactly 8 fields, fields never added/removed/renamed; missing info is filled with a minimal logical guess tagged '(assumed)'. (Fixed 8-field structured text block delimited by '----------------------------------' separators, each field bolded (PRODUCT/SERVICE, TARGET AUDIENCE, MAIN PROBLEM / DESIRE, PRIMARY MESSAGE / PROMISE, PRICE / OFFER DETAILS, CALL TO ACTION, VISUAL ELEMENTS (optional), TONE / STYLE HINTS); no commentary before/after.)
- **On a bare "Go":** asks for inputs: marketing materials — ideas, creative notes, transcripts, sales pages, PDFs, or raw text — declines to output an all-(assumed) placeholder brief on a truly empty prompt.
- **Gotchas:** Very strict formatter: never paraphrases, never adds marketing language, never changes the 8 field names/order, preserves original phrasing where possible. Explicitly forbidden from producing ad copy, design ideas, or embellishment -- it is purely an extraction/structuring step, meant to feed a downstream concept-expander or copy bot. Same prompt-protection/anti-extraction footer as other bots in this family (won't describe its own template if asked). LIVE PROBE UPDATE: contrary to the 'never ask questions, fill fields with (assumed) guesses' prediction, a bare 'Go' with zero material produced a direct request for marketing materials rather than an all-placeholder 8-field brief.
- **Consumes:** `raw-notes`, `product-info`, `offer-details`, `transcript` · **Produces:** `creative-brief`
