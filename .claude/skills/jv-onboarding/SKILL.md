---
name: jv-onboarding
description: Stand up a new JV partner folder. Use when Joey says "new JV partner", "onboard [name]", "set up a jv partner", "add a partner", or names a JV deal that doesn't have a folder in jv/partners/ yet. Scaffolds partner.md + research/ + copy/sell-their-offer/ + copy/sell-our-offer/ from the template, runs a short intake, and adds the partner to jv/JV-map.md. Setup only — no copywriting happens here, that's /storm, /brief, /produce.
---

# /jv-onboarding — stand up a new JV partner, mini-client style

Every JV partner is treated as its own mini-client (`jv/JV-map.md`: "don't
blend avatars or angles across partners"). This skill exists so that setup
step is never skipped or half-done under time pressure — it's the same
shape every time: `partner.md`, `research/`, `copy/sell-their-offer/`,
`copy/sell-our-offer/`.

**This is scaffolding + intake only.** No hooks, no angles, no copy. Once
the folder exists and `partner.md` has enough filled in, hand off to
`/storm` → `/brief` → `/produce` for the actual work.

## The run

### 1. Get the name and business
Ask if not already given: partner's name + business/brand name.
Build the folder slug the same way existing partners are named —
`firstname-lastname-businessname`, lowercase, hyphenated, no spaces
(e.g. `ryan-magdanz-leadbase`, `matt-leitz-botbuilders`). Check
`jv/partners/` isn't already using that slug before creating it.

### 2. Scaffold the folder
Create `jv/partners/{slug}/` with:
- `partner.md` — copied from `jv/partners/_partner-template.md`, title line
  changed to `# JV Partner: {Name} — {Business}`. Leave every section as
  the template's prompt text until intake fills it in.
- `research/_about-research.md` — one line: "Drop anything here: sales page
  screenshots, VSL transcripts, testimonials, competitor swipes, notes from
  a call with {Name}. Claude synthesizes this into `partner.md` once
  there's enough to work with."
- `copy/sell-their-offer/_about.md` — "Copy that sends the Flexxable
  audience into {Business}. Build once `partner.md` has the offer and proof
  filled in."
- `copy/sell-our-offer/_about.md` — "Copy that sends {Name}'s audience into
  the IAA book or ROYA. Build once `partner.md` has the audience avatar
  filled in."

### 3. Run a short intake
Ask Joey (don't guess, don't invent — same rule as everywhere else):
- Who they are — one or two lines, what they're known for, what they sell.
- **Deal direction** — which leg is happening first: selling their offer to
  our audience, selling our offer (book/ROYA) to their audience, or both?
- Their offer: product/service, price if known, sales page link, proof
  that's actually cleared to use.
- Their audience: niche, sophistication, pain points — enough to judge fit
  for whichever offer is going their way.
- Voice/approval: how they sound, who signs off before anything ships to
  their list.

Fill in whatever Joey gives you. Anything he doesn't have yet stays marked
**"TBD — ask Joey"** or **"unknown — ask [partner]'s team"** rather than
invented — match how `matt-leitz-botbuilders/partner.md` handles open
items. Don't block folder creation on a complete intake; partial is fine,
this gets filled in over time same as every other partner file.

### 4. Register in the map
Add one bullet to `jv/JV-map.md` under `## Partners`, above the "Next
partner — add when ready" line:
`- {Name} — {Business}: [jv/partners/{slug}/](partners/{slug}/partner.md)`

### 5. Point at the standing rules, don't re-explain them
Tell Joey the folder's live, and remind him (briefly, don't re-paste the
whole thing) that the JV ladder rules in `jv/JV-map.md` ("Hard rules
learned") and `jv/partner-voice-template.md` apply the moment copy starts —
this skill doesn't re-litigate those, it just gets the partner ready for
them.

Related: [[JV Partnerships Map]]
