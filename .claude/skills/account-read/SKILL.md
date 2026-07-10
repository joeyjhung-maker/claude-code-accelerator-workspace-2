---
name: account-read
description: The weekly Analysis loop — the stage that starts the creative-strategy wheel. Use when Joey says "read the account", "account read", "weekly read", pastes a Meta reporting export, or wants to turn account results into hypotheses, gaps, and this week's production plan. Brackets ads by KPI, banks hypotheses, overlays coverage on the client's strategy map, re-ranks gaps, and ends with a Production Plan + Allocation Mix. Analysis only — no copywriting here (that is /produce territory).
---

# /account-read — read the account until you can feel what to do

The wheel starts here. One client per run. The job is two things at once:
saturate Joey's gut on what actually won, and fill the system's banks
(hypotheses, coverage, openings) so everything downstream writes better.

**This stage never writes copy.** It ends at a plan. If Joey wants ads written,
that's the next stage — say so and stop.

## Joey's defaults (override per client in `clients/{name}/analysis-config.md`)
- **KPI:** ROAS / CPA — the ad made money or it didn't.
- **Data in:** pasted reporting export (CSV, table, or numbers + ad copy).
- **Brackets:** Winners / Traction / Losers.
- **Mix:** ask each run — never assume the net-new / variations / scaling split.

## The run (gates are real — stop at each one)

### 1. Client + data in
Ask which client if not obvious. Load `clients/{name}/client.md`,
`strategy-map.md`, and `analysis-config.md` (create config from the defaults
above on first run).

Take the pasted export. Save the raw paste to
`clients/{name}/account-reads/YYYY-MM-DD.md` before doing anything with it.
If ad copy isn't in the export, ask for the copy of the notable ads — don't
guess at what an ad says from its name.

### 2. Bracket
Sort every ad into Winners / Traction / Losers against the KPI.
Show the full bracketed list at once — every ad, one line each
(name · spend · KPI number · one-phrase description). No sampling.
Then stop: "Anything mis-bracketed?" Joey corrects, you re-sort.

### 3. The two reads — keep them separate
**Hypotheses (backward, this account).** For each winner and each notable
loser: why. Chunky, testable claims — "the CRM-as-asset hook is carrying the
cold IAA ads", not attribution science. Append to
`clients/{name}/hypotheses.md`, dated, tagged `[YYYY-MM-DD]`, with the ad it
came from. Show them all; Joey edits or kills any before they're banked.

**Openings (forward, everywhere).** Three streams converge into ONE ranked
list:
- **Gaps** — overlay this week's ads on the strategy map. Loose classification
  only (segment + rough awareness: unaware/problem vs solution/product vs most
  aware). Empty or thin cells = gaps.
- **Hypothesis-driven** — a hypothesis that generates a bet ("cortisol carries
  joints → test it on the next outcome over").
- **External** — anything Joey pastes or mentions: competitor moves, comments,
  what's trending. Don't fabricate external signals; if he has none this week,
  the list runs on gaps + hypotheses.

Rank the openings with chad logic (urgency · TAM · gap size · genuinely new ·
reachable) and present the whole list. Joey re-ranks. His order wins.

### 4. Coverage back to the map
Update `clients/{name}/strategy-map.md` coverage from this week's ads —
mark cells covered/fatigued/open. If the read surfaced a NEW outcome or
segment (from comments, a weird winner), propose adding it to the map spine —
propose, don't just write it in.

### 5. Production Plan + Allocation Mix (the output)
Ask: **"How many ads this week?"** — suggest a number only if he doesn't have
one. Ask the mix: net-new / variations / scaling split.

Then write the plan: N ads, which openings they attack, what type, what rough
awareness level. Variations get a CASHED note (which knob to turn on which
winner: Concept · Angle · Style · Hook · Edit · Demographic — D and S buy new
reach, C/A/H/E buy conversion). Save to
`clients/{name}/account-reads/YYYY-MM-DD.md` under the raw data.

The plan guides ideation — it is never stamped onto a seed. If a great idea
breaks the plan later, the plan yields.

### 6. Close the flywheel
Any Winner not yet in `clients/{name}/primers/` → offer to promote it
(full text, into the right primer). Any lesson worth keeping → offer
winners/ or losers/ per the data dictionary. Offers, not actions.

## Rules that bite here
- Ask, don't invent — his KPI, his mix, his corrections at every gate.
- Full lists, all at once, copy-paste-able. No "top picks", no samples.
- Loose awareness classification. Don't force every ad into a precise bucket.
- Never verify numbers Joey pasted — his data is real (see memory:
  dont-verify-user-written-claims).
- No compliance/claims commentary. Ever.
- No copywriting. The run ends at the plan.
