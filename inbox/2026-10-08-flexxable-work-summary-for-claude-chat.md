# Joey × Flexxable: work summary (Jun–early Oct 2026)

Paste this into Claude chat as background. Built from the Claude Code workspace: daily notes, git log, client files, winners/, losers/, workflows/. Written 8 Oct 2026.

**Coverage warning:** the workspace only goes back to 9 Jun 2026. Jan–May 2026 isn't in it, so this summary has nothing on that stretch. Fill it from your own memory or old chats.

---

## 1. Who and what

- **Me:** Joey Hung. Marketing director for coaching brands. Paid creative, ad copy, hooks and the strategy under them. Own agency: **Heuromi Media**.
- **Main client: Flexxable** (Dan Wardrope). Infoproducts and coaching that teach 9-5ers and agency owners to start a performance-based AI automation agency.
- **Core offer:** *The Instant AI Agency* book ($14.40). Promise: earn 30–50% of client profits, AI does the work. Back-end: **ROYA** coaching.
- **Billing:** monthly invoice to Flexxable Ltd via FirstSeed LTD. About $10k/mo retainer, plus $300 per ROYA commission (8 of those landed in July, so INV-61 was $12,400). INV-62 and INV-63 are drafted in Canva, not yet sent.
- **Heuromi goal:** land one more creative-strategy client to reach ~$20k/mo. Longer term, buy a business next year. Client #2 criteria and the acquisition target are still undefined.
- **Dan's voice:** Australian, not British. The old "British-inflected" note was wrong and has been fixed in `brand/voice.md`. Casual, direct, texting-a-mate. Short punchy lines. Banned words: leverage, solution, deliverable, onboarding.

## 2. How the work is set up (this changed most since early 2026)

Everything now runs through **Claude Code** in a Git/Obsidian workspace, with Codex working against the same repo sometimes.

- **CLAUDE.md ("the Script")** is read every session: voice rules, rules that bite, where everything lives.
- **Folders:** `clients/{name}/` (client.md, strategy-map, seeds, briefs, winning ads), `copy/` and `creatives/` for output, `winners/` and `losers/` for lessons, `workflows/` for repeatable plays, `brand/` for voice and hooks, `jv/`, `swipes/`, `mentors/`, `daily/`.
- **Pipeline (creative-strategy flywheel):** `/account-read` → `/storm` (seeds) → `/brief` (locks segment, awareness, mechanism, hypothesis before any copy) → `/produce` (the only stage that writes) → judge.
- **Writer:** **MarioBot** (Genesis bot) drafts. A judge pass follows: `copy_lint.py` plus a copy rubric.
- **Genesis bots** (Dan's creative-strategy bot library, called via API): hook bots, VSL bot, segment-swapper, Message Isolator and others.
- **Save vs promote:** work gets saved in `copy/` or `creatives/`. The lesson (why it won or died) gets promoted to `winners/`, `losers/`, `brand/` or `workflows/`. Daily note logged every session.
- **Rules I enforce:**
  - Never invent a client result, number or quote.
  - Don't open with student proof.
  - Pain is the amplifier, not the opener.
  - No walls of text.
  - Video: frame 0 must already show the hook line.
- **Skills built or installed since June:** `/produce`, `/produce-skool`, `/storm-skool`, `/brief-skool`, `/jv-onboarding`, `/flexxable-invoice`, `/timeline-ad`, `/multiply`, `business-teardown`, `offer-audit`, `reflect`, `task-observer`, `handoff`, `dashboard-setup`, `defuddle`, `obsidian-markdown`. Also the five Genesis "Winning Ad Workflows": horizontal-scaling, formats-conceits, comment-goldmine, organic-hooks, plus the styles list under `/multiply`. The Genesis ones and `/timeline-ad` and `/multiply` have **not been run yet**.
- **Automation:** weekly Routine (Tuesdays) runs `/storm` for Flexxable and drafts proposed briefs. It stops short of full automation on purpose. The brief step says "propose, he decides".
- **Image pipeline:** `run_image.py` → KIE (nano-banana-2 for text-heavy statics). Tested gpt-image-2 against nano-banana-2 on 1 Sep. It does **not** fix small-text garbling. Real fix: render a clean base image, overlay text in Canva.
- **Video pipeline:** `run_video.py` (Veo 3.1 / Kling via KIE), Whisper captions, synthesized SFX, loudness-balanced mixing (VO -16 LUFS, master -14).
- **Concurrency rule:** Claude Code and Codex can both be working in the repo. Never `git add -A`. Stage only named files.

## 3. Timeline

### June: setup and first copy
- **9 Jun:** workspace built. Flexxable added as first client, 10 winning ads parsed, strategy map and hook primer written. First Genesis hook run: 8 mechanism hooks for the 9-5 escapee segment (dead-leads reactivation angle).
- **10 Jun:** built the judge half of the engine (`copy-rubric.md`). Rule: judge the machine's lines hard, only flag Joey's own. Captured Flexxable's formatting and emphasis fingerprint (bold = skim path, CAPS = one punch word). Hulk squeeze page v2 and the Blue Ocean / Hulk Reveal email.
- **24 Jun:** reactivation FB ads for cold old leads and book buyers ("Add Androids, not clients" and a 3-variant student-roll-call → Hulk set). Hand drafts fell flat; MarioBot's output with light edits won. Promoted the MarioBot body-copy workflow.

### July: statics and JV
- **6 Jul:** cold IAA book FB ad on the "CRM is worth more than your ad budget" hook. Result still pending. New rule: "ladder the big pivot" (ellipsis ladder).
- **10 Jul:** built `/produce`. First live run: the BURNOUT belief-validation ad. First statics via KIE (15 SCRAWLS concepts, 3 rendered).
- **16 Jul loser:** Ryan Magdanz Rainmaker webinar sold high-ticket straight off a webinar with no ladder. Converted about 0. This birthed the JV ladder rules (below).
- **21 Jul:** Buildy (Bill Macintosh) JV webinar campaign. Mined Dan's 2024 book for concepts and built the ROYA master-concepts doc. Reworked the webinar deck (hero title built on "$1,030,000 in sales… $222,600 banked as a pure commission split"). Wrote the 8-email reg sequence. Built a reusable **Partner Voice** system. Winners note decodes my 10 editing instincts. Loser: reordering the cold open for clarity was wrong for a warm JV.

### August: JV, Threads, Skool
- **5 Aug:** new JV partner Matt Leitz / BotBuilders. Lighter cadence. Hedge-fund "2 and 20" email, Old Plan/New Plan, whiskey-bottle story email.
- **10 & 13 Aug:** infrastructure. Tool-vetting workflow (passed on claude-mem, OmniRoute, headroom, Agent Reach). Installed `task-observer`, `obsidian-markdown`, `defuddle`. Long-form midwife-swipe IAA ad. Lesson: long-form unaware ads run on **one repeated drumbeat word** ("flat vs a cut"). Found `copy_lint.py` false-cleans files that use `---` section breaks.
- **14 Aug:** new `business-teardown` skill. First run: full teardown of Apostle Tobi Arayomi (prospect work, not Flexxable). 22 findings; the TAP Institute site was offline. A Trustpilot fraud allegation was **unverified**, so I haven't acted on it. Also an offer audit and paste-ready WATCH+ sales page.
- **15 Aug:** **Threads growth system** for my personal @joeyhung_ account (1,173 followers, 5,000 target by 15 Nov). 403-post archive, 17-skeleton structure bank, 23 seed accounts, 80-post swipe file. Best post ever was a fitness structure with the nouns swapped, used once in 403 posts. Posting volume collapsed Jan→Mar (115 posts → 16) and growth tracked it. This lane is separate from Dan's voice.
- **17 Aug:** argument bank (cold-traffic arguments), 246-headline bank from live statics, the 48-Hour Android concept locked (two ads). Three contrast-hook rules promoted to `brand/hooks.md` (beat 2 is a gut punch not an argument; need an inversion, not just a loser; peers must read as wrong-turned, not useless).
- **19 Aug:** **B2B Leads Lab** project started: Dan's Skool community for landing 8/9/10-figure meetings with "AI Enriched" lumpy mail (physical gifts like whiskey bottles). Sales-call clip post, 10 opener variations, About-page copy, hero image prompt. Offer name locked: "The 4-Hour Dream 100 Shortcut". Avatar is anyone who books meetings with high-value prospects, **not** the escape-the-9-5 audience.
- **24 Aug:** Diversity Decoder audit on the live account (75 active ads, UK). Score 64/100, 68% Solution-Aware vs 2.7% Unaware. Gap #1: no Unaware content for the burnt-out agency owner. 8 briefs, U6 "Retainer Lie" text + 6 statics and V3 "9PM Message" video script shipped. New `hook-rubric.md` (Four Moves + vehicle variety). Dan hasn't filmed V3 yet.
- **26 Aug:** B2B Leads Lab DFY beta waitlist page and onboarding sequence. IAA "Learner Brain" static campaign (Dan Henry swipes, segment swap to 9-5er, Genesis static pipeline). "Visceral Mechanism" statics: 3 of 12 produced. **From 1 Sept I own all content for four Skool groups:** AAA Ninjas, ROYA, Million Dollar AI Deals, B2B Leads Lab. Built Heuromi Command Center dashboard (artifact).

### September: Skool content machine, Topa, CAP
- **1 Sep:** built the weekly storm-refill Routine.
- **4–7 Sep:** Topa/Nat launch call filed. B2B Gifts internal launch 14 Sep, UK launch 21 Sep (Yeti Rambler only), £39.99 wine / £54.99 Yeti. Ingested Travis Sago's PSM+BTEM course notes and corrected a standing error (CAP is Child/Adult/Parent, not Cause/Action/Payoff). **Key lesson ("loose briefs beat constraint stacks"):** heavily constrained MarioBot briefs give flat copy; looser fact-dump briefs give better hooks. Confirmed twice head to head against my own ChatGPT prompts.
- **5 Sep:** BotBuilders reverse leg: rewrote their affiliate emails 1, 2, 4 into Dan's voice (emails 3, 5, 6, 7 and the real affiliate link still open).
- **7 Sep:** ROYA Scale Proof Bank built. Proof-led testimonial video draft (three hooks, one shared body) is still 249–261 words against a <220 limit. Faith Threads runs for my personal account.
- **8–9 Sep:** **Dan Skool route rebuilt.** MarioBot now runs without the legacy style contract. A light "ChatGPT-style" judge (`rubrics/dan-skool-chatgpt-rubric.md`) makes 1–3 high-impact edits only and keeps Dan's cheeky roughness. Also a run of B2B Leads Lab posts: LinkedIn-first "warm the lead first" teaser, lumpy-mail fishing poll, mobile-follow-up post with the "some cojones" bridge. Genesis Bots skill installed. 14 Sep: Zack Kravits reel swipe (named-mechanism), "one vs ten" experiment video brief, and 20 vetted hooks. I haven't picked one.
- **11 Sep:** AAA Ninjas "land and expand" NAP, plus a 355-word cut. Cut three AI-slop contrast clusters by hand.
- **15–24 Sep:** I was away. Handover doc and content-plan colour key. Long-form "pillar posts" as the lead magnet in place of funnels (Dream 100 scorecard, comment to get access).
- **20 Sep:** Wingman 2.0 live-release post (Netflix model), Pierre's ROYA proof post (two rejected drafts, then my edit became canonical), Dream 100 Scorecard teaser. New judge rule: gated teasers sell the stakes, never publish the payload.
- **25 Sep:** restored Genesis/MarioBot (invalid provider key). 22 Skool seeds. Four Skool posts shipped. Wrote the **Dan copy correction loop** (save → diff → learn → improve). Fact-safe "backwards agency scoreboard" FB variation, with 10 hooks pending my pick.
- **26 Sep:** ROYA LinkedIn Automation early-access post at $79/mo. Needs Jonathan's Topa fact-check before publish.
- **28 Sep:** **CAP doctrine corrected and locked** as the architecture for the Topa LinkedIn Automation campaign: Child (desire) posts first, Adult (mechanism) next, Parent (proof/objections) last. Added the CDCDCD offer test. Hedge Fund FB ad (week of 28 Sep) is final. Built a target-market desire bank.
- **29 Sep–3 Oct:** animated video series for the IAA **"Locked Whiskey Bottle"** ad (Dan's original VO). Versions built:
  - doodle v1–v5
  - 16-bit game v1–v2
  - heist v1
  - hybrid doodle + Dan on-camera v1
  - **Pixar v1–v5**
  - Pixar v4 uses full word-for-word captions. Pixar v5 puts the hook on frame 0.
  - Spend: about $12 on heist, KIE auto top-up on. Sales Androids storyboard (37 scenes) is paused until the original audio arrives.

### Early October: strategy library
- **2–3 Oct:** Locked Gift lead-magnet image brief for Codex (Dan's doc; coupon flow via Topa.io, code DANWARDROPELEADS = 200 free leads). Ingested ~11 creative-strategy sources (Volkwyn, Kam $100M series, Genesis first-batch method, Luke's vicious hooks) into the Second Brain wiki (238 pages). Built `/timeline-ad` and `/multiply` and the Ad Genome concept note. Drafted a **creative-strategy client onboarding checklist** for Heuromi client #2. RYZE "Red Flags" swipe broken down, with a Flexxable book slot map and two seeds. **Video rule banked:** frame 0 carries the hook.

## 4. What's worked (promoted lessons)

- **MarioBot drafts, human final edit.** Hand drafts from Claude flopped on Dan's voice. MarioBot output with light edits shipped.
- **For Dan Skool:** run MarioBot raw, then judge lightly. Over-judging (rubric/lint/GPT rewrites) flattened it. Preserve personality and selling power, make 1–3 edits, surface only hard factual risks.
- **Loose briefs beat constraint stacks.**
- **Partner Voice for JV emails** and flow over staccato fragments. My stated pet hate: "stop giving me AI slop."
- **Preserve a swipe section's persuasive function,** not just its label.
- **Proof goes in as the consequence,** not as the opener.
- **Ask for the real number before drafting.** Don't write elegantly around a gap.
- **Image requests mean an image-gen prompt,** not an HTML mockup.
- **Statics:** one targeted fix per edit pass, chained off the best prior output.
- **Video:** check runtime against Dan's ~100 wpm pace, first frame carries the hook, every word captioned, mix VO-first by loudness not peak.
- **Truth constraint:** burnout pain must read as a closed chapter, never present-tense. Never invent biography, quotes or numbers.

## 5. What died

- Ryan Magdanz webinar: high-ticket off a webinar to a cold audience, no ladder. ~0 conversions.
- Clarity-first cold-open reorder for a warm JV webinar.
- The old lint/scorecard judge on Dan Skool posts (replaced 8 Sep).
- Threads swipe corpus (17 Aug loser note: corpus diagnosed as broken).
- Custom Claude artifact content-calendar dashboard (rejected, now a Google Sheet).
- Heavily constrained MarioBot briefs.

## 6. JV partnership rules (hard-earned)

- Never sell ROYA cold off a webinar. ROYA is the ascension.
- The webinar sells a **$497–997 reversible front-end** with a real guarantee.
- Never sell the book over a webinar. It's a free lead magnet or an order bump.
- Cheap rung = self-serve cart. High rung = conversation plus partner co-close.
- The front-end's job is indoctrination and a first dollar, not revenue.
- Add to the partner's model, never ask for a pivot.
- Partners so far: Ryan Magdanz (Leadbase), Bill Macintosh (Buildy.ai), Matt Leitz (BotBuilders), Gary Capps (myCRMSIM), Rich Schefren (Strategic Profits). Each runs both legs: sell their offer to our list, sell ours to theirs.

## 7. Still open (as of 3 Oct)

**Unresolved calls**
- **Red Flags ad (picking up Mon 5 Oct):** who's on camera for the four symptom skits, whether a pain-led opener is right, and whether to use Rob's $341,042 line. The 9-5er version still needs four sourced symptoms.
- Hook selection pending on the "one vs ten" video and the Marcio "backwards agency scoreboard" variation.
- **Tension:** Kevin Just says proof goes first; my Script says never open with student proof. Noted, not resolved.
- Do full captions go on the doodle, 16-bit and heist versions too?

**Production and launches**
- BotBuilders emails 3, 5, 6, 7 and the real affiliate link.
- Topa fact-check on the LinkedIn Automation early-access post, plus raffle/lifetime-access confirmation.
- Locked Gift lead magnet: final CTA link for the QR code, plus the Topa coupon-field screenshot.
- Dan to film V3. Sales Androids animation paused until the editor delivers the original audio.
- Testimonial video script needs trimming to <220 words.
- B2B Leads Lab paid tier (target 30 Sept), the $7/mo Skool and $99/mo LinkedIn funnels and welcome sequences, two webinars, Hulk replay reuse (six moves; sequencing is my call).
- Flexxable invoices INV-62 and INV-63 are drafted, **not yet sent.**

**System and housekeeping**
- None of the newest skills (`/timeline-ad`, `/multiply`, the four Genesis workflows) have been run yet.
- Second Brain wiki lint is due. 14 Volkwyn videos still un-ingested.
- I need to rehearse the "testing process / dissect an ad" interview answer (draft in `concepts/Ad Genome.md`).
- Heuromi client #2 criteria and acquisition target are undefined.
- **Security:** a live Genesis API key sits in `daily/2026-06-09.md` in git history. Rotate it. A Threads token was also pasted into chat on 15 Aug and needed regenerating.

---
*Source: `daily/`, `git log`, `clients/flexxable/`, `winners/`, `losers/`, `workflows/`, `jv/`, `heuromi-media/`. Dates are session dates.*
