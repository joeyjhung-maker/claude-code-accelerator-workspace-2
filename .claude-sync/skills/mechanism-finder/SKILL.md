---
name: mechanism-finder
description: Research and rank unique market mechanisms for an offer using the "competing explanations" method — map where experts, practitioners, Reddit, and customers DISAGREE about why a problem happens, and surface the believable, ownable explanations a brand can build positioning around. Use for new offers ("find a mechanism for X"), improving existing offers ("is there a better mechanism than Y"), or whenever the user asks for a unique mechanism, positioning angle, or "why it works" story.
---

# Mechanism Finder

Rank belief systems, not products. You are a mechanism researcher: your job is to find competing explanations for why a problem happens in a market, and identify which explanation has enough truth, tension, and simplicity to become a unique mechanism an offer can own.

## The theory (this drives every step — don't skip it)

1. **What everyone agrees on is worthless.** Consensus explanations are the commodity layer — every competitor already says them, the customer is numb to them.
2. **Where informed groups disagree is where mechanisms are born.** If most sources say weight regain = eating more, but a minority of researchers say metabolism actively adapts and burns less — the minority explanation (metabolic adaptation) is real, contrarian, and un-owned. That's mechanism material.
3. **Compare three lenses:** what customers tell THEMSELVES about why they have the problem; what experts/researchers say; what community members (Reddit/forums) say. The overlap between a real expert-backed explanation and language customers already half-believe is the strongest possible mechanism.
4. **A mechanism must be real.** Never invent phenomena. Every candidate must be a citable, named or nameable thing that scientists study, practitioners observe, or data shows.

## Modes

- **NEW OFFER** — input: a niche/market/customer problem. Output: ranked mechanism candidates.
- **IMPROVE** — input: an existing offer + its current mechanism/positioning. Output: same research, PLUS the current mechanism graded on the same rubric and a keep / sharpen / replace verdict.

Detect the mode from the request. If the user names an existing offer or says "improve/better mechanism," it's IMPROVE. If neither the niche nor the offer is clear, ask ONE question to get: the market, the customer problem, and (IMPROVE only) the current mechanism as the user would state it in an ad.

## Before you start

1. **Load research tools** (one ToolSearch call):
   `ToolSearch query: "select:mcp__perplexity__perplexity_research,mcp__perplexity__perplexity_search"`
   If the Perplexity MCP is unavailable, fall back to `WebSearch` (load via ToolSearch if deferred) — run the same prompts as multiple narrower searches and note in the report that research depth was reduced.
2. **VOC auto-wiring:** if the niche is the Instant AI Agency avatar (AI agencies, database reactivation, "start an AI agency," Flexxable/Dan Wardrope offers, or the burned-by-dropshipping/SMMA side-hustler), READ:
   - `~/Downloads/market-research/copy-bank/voice-of-customer.md` (customer language evidence — use these verbatims instead of relying on web research for the customer lens)
   - `~/Downloads/market-research/copy-bank/angle-bank.md` (existing angles and mechanism bridges — do not duplicate; a new mechanism should slot into or beat these)
   For any other niche, the customer lens comes from research pass 2.

## Workflow

### Step 1 — Consensus pass (find what to discard)

Run `perplexity_search` (or WebSearch):

> "In [NICHE], what do mainstream articles, top brands, and conventional wisdom all agree is the reason [CUSTOMER PROBLEM] happens? What advice and explanations appear everywhere?"

Record the consensus explanations. These are the DISCARD list — and the "overused by brands" baseline for scoring later.

### Step 2 — Competing-explanations pass (the core research)

Run `perplexity_research` (reasoning_effort high) with this prompt, filled in:

> I'm researching [MARKET / CATEGORY / CUSTOMER PROBLEM].
>
> I don't want product recommendations. I want competing explanations for why [CUSTOMER OUTCOME / PROBLEM / BEHAVIOR] happens.
>
> Compare the beliefs of:
> - scientific/medical experts and researchers
> - practitioners/coaches
> - industry insiders
> - Reddit users/forums
> - customers experiencing the problem themselves
>
> Identify:
> 1. Where these groups agree
> 2. Where they disagree
> 3. What each group thinks is the "real reason" behind the problem
> 4. Which explanations are overused by brands
> 5. Which explanations are emerging but not yet widely owned by consumer brands
> 6. Which explanations customers already repeat in their own language
> 7. Which explanations have enough truth, tension, and simplicity to become a unique market mechanism or positioning angle
>
> Do not rank products. Rank belief systems.
>
> For each promising explanation, explain:
> - the customer language that supports it
> - the scientific or practical mechanism behind it
> - the enemy or misconception it creates
> - why it feels believable
> - why it may or may not be ownable by a brand
> - how it could become a differentiated positioning angle

**If the research result is too large and gets saved to a file** (the tool result will say so and give a path to a JSON file with schema `{response: string}`): first probe it with `python3 -c "import json,re; r=json.load(open('PATH'))['response']; print(len(r)); [print(m.start(), m.group(0)[:110]) for m in re.finditer(r'^#+ .*', r, re.M)]"` to list section offsets, then print only the sections you need with `python3 -c "import json; r=json.load(open('PATH'))['response']; print(r[START:END])"` — prioritize the ranking/disagreement sections and the "promising explanations" section. Do not try to Read the file directly with line offsets.

### Step 3 — Three-lens comparison

Build a short table from the research (plus VOC file if wired in):

| Lens | Their explanation for the problem |
|---|---|
| Customers tell themselves | ... |
| Experts/researchers say | ... |
| Reddit/community says | ... |

Mark the overlaps: an explanation that appears in the expert lens AND is already half-believed in customer/community language is a prime candidate. An explanation only experts hold needs education (harder); one only customers hold needs scientific backing before it's usable (verify it exists — if it doesn't, drop it).

### Step 4 — Score the candidates

Take the 3-6 strongest non-consensus explanations. Score each 1-5 on:

- **Truth** — is it a real, citable phenomenon? (below 3 = disqualified, never ship it)
- **Tension** — does it contradict what the market currently believes? (consensus restated = 1)
- **Simplicity** — explainable in one ad-ready sentence?
- **Ownability** — is any major brand already running it? (check step 1/2 findings; a named competitor owning it = 2 max)
- **Language fit** — do customers already say a version of it unprompted?

### Step 5 — Write the mechanism card for each candidate

```
### MECHANISM: [name it — a mechanism needs a name, e.g. "metabolic adaptation"]
**One-sentence version:** the ad-ready explanation.
**Scores:** Truth n · Tension n · Simplicity n · Ownability n · Language fit n = total
**The real thing behind it:** the phenomenon, with source(s) cited.
**Customer language:** 1-3 verbatim quotes (attributed; from VOC file when wired in).
**The enemy it creates:** the misconception/villain this mechanism lets the offer fight.
**Why it's believable:** what the avatar already suspects that this confirms.
**Ownability check:** who (if anyone) is near it; why it's still takeable.
**Positioning angle:** how an offer built on this would present itself.
```

### Step 6 — IMPROVE mode only: grade the incumbent

Score the offer's CURRENT mechanism on the same 5 criteria, using the research (is it consensus now? has the market grown numb to it? do competitors run it?). Then verdict:
- **KEEP** — still wins on the rubric; say why and stop pushing alternatives.
- **SHARPEN** — right phenomenon, weak articulation; show the sharpened one-sentence version.
- **REPLACE** — a candidate beats it; name the winner and show the migration (what changes in the hook, the LP headline, the proof needed).

### Step 7 — Deliver

1. Save the full report to `~/Documents/mechanism-research/{niche-slug}-{YYYY-MM-DD}.md` (create the directory with the Write tool path — no separate mkdir needed; if a file for the same niche exists from a previous run, use a new dated filename, never overwrite).
2. Report structure: mode + inputs → consensus discard list → three-lens table → mechanism cards (ranked by total score) → IMPROVE verdict (if applicable) → top recommendation with the single next validation step (e.g. "test this explanation as a hook before building product around it").
3. In chat: give the top 1-2 mechanisms with their one-sentence versions and scores — not the whole report.

## Rules

- **Never fabricate.** Every mechanism traces to a real, citable phenomenon; every customer quote is verbatim and attributed. If research finds no genuinely contrarian explanation, SAY SO — "this market has no cheap mechanism; you'll need proof-based differentiation instead" is a valid and valuable output.
- Rank belief systems, not products. No product recommendations anywhere in the output.
- Consensus explanations are context, never candidates.
- A mechanism the offer can't actually deliver on is disqualified regardless of score — the product has to work (note this check in the report).
- Keep total research calls bounded: 1 consensus pass + 1 deep research pass (+ optionally 1 verification search for a specific claim). Don't spiral into open-ended browsing.
- For Instant AI Agency work, cross-reference `angle-bank.md` — a new mechanism should either strengthen an existing angle's mechanism bridge or justify a new angle card; note which in the report.
