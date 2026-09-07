---
name: faith-thread
description: Draft Threads post options for Joey's personal faith account (@joeyhung_), grounded in his Second Brain theology wiki. Use when Joey says "thread", "faith thread", "write me a thread on X", "/faith-thread", or asks for Threads post options on a theological topic or concept. Produces 5 draft options (3 short, 2 long) using the account's own non-testimony structures, checked against the account's voice rules and reject list before he sees them. Never writes personal testimony or story content — that's Joey's to add himself.
---

# /faith-thread — Second Brain wiki becomes Threads draft options

The whole point of this skill: stop re-explaining "go read my Second Brain" every
time. One call, five grounded drafts, done.

**Hard boundary — no testimony, ever.** Never touch `threads/testimony-bank.md`.
Never write a personal story, event, or first-person claim about Joey's life. That's
his to write himself. This skill draws content **only** from the Second Brain wiki
(doctrine/teaching) and shapes it with the **non-testimony** structures below. If a
topic can't be written without a personal story, say so and stop — don't reach for
testimony bank as a workaround.

**Never quote scripture or doctrine from memory.** Every claim in a draft has to
trace to an actual note in `/Users/joey/Documents/Second Brain/wiki/` (a separate
Obsidian vault — read-only, never edit anything there) or to something Joey states
in the session. If you can't point to the line it came from, don't write it.

## The run

### 1. Get the topic
- **Joey names one** (a concept, a teacher, a verse, a phrase) → search the wiki for
  the matching note(s). `ls "/Users/joey/Documents/Second Brain/wiki/"` then grep/read
  by filename or content match.
- **No topic given** → skim the wiki folder and surface **3–5 real note titles** for
  Joey to pick from. **Repeating a topic already drafted is fine — Joey wants that.**
  Reinforcing what's already been taught is a deliberate part of his content strategy,
  not something to route around. Mix fresh notes and previously-used ones freely; a
  quick check of `threads/posts/` for what's run before is useful context to mention,
  not a filter to exclude by. Never invent a topic that isn't an actual note in the
  wiki.
- If the wiki has nothing on the named topic, say so and ask — don't draft from
  general theological knowledge as a fallback.

### 2. The wiki finds the topic. The raw source is what you draft from.

**Never draft directly off a wiki note.** The wiki is a compressed, paraphrased
summary — that's its job, and it's good at that job, but it strips out the specific
quotes, images, and demonstrations that make a post actually land. Confirmed
2026-09-05: drafted straight from `biblical-meditation.md`'s one-line paraphrase
("Confidence in prayer is developed through proximity"); Joey rejected the whole
batch as flat. The wiki note's own sources had the real material — a front-door/
kitchen demonstration, a magnifying-glass image, a loud-vs-connected contrast — none
of which survived into the summary.

**2a. Read the matched wiki note in full** — same as before, this confirms the topic
is real and surfaces cross-referenced concepts (`[[other-note]]` links) worth
checking too.

**2b. Read its raw source(s).** Every wiki note has a `sources:` line in its
frontmatter listing the file(s) it was built from. Locate those files under
`/Users/joey/Documents/Second Brain/raw-sources/` (search by filename — the folder
structure varies by teacher/series, e.g. WASP sources sit under
`raw-sources/Prophetic Notion Export/Prophetic/WASP/`) and **read them in full**,
not just the section the wiki note cited. This is where the actual post language
comes from: specific quotes, metaphors, demonstrations, contrasts. Note which raw
file each drafted line traces to — it gets cited alongside the wiki note in the
saved draft.

If a `sources:` entry can't be found on disk (renamed, moved, or the wiki note
predates this rule and cites something too vague to trace), say so and fall back to
the wiki note — don't silently skip this step.

### 3. Pick from three families — vary across ALL of them, not just within one

Three shapes are all legitimate and evidenced. Draft across all three in a batch —
**don't fill a 5-post batch with several posts from the same family**, even if
they're technically different named structures. Confirmed 2026-09-05: three drafts
that each opened with a personal realisation ("The more I…", "I used to…",
"Something I…") got rejected as too similar even though they were three different
structure-bank entries in theory — the opener SHAPE was the same three times.

**Family A — Personal-processing register.** Someone thinking out loud and landing
on a realisation. Pull from `threads-voice.md`'s recurring openers (`The more I…`,
`I used to…`, `Something I…`, `When you understand…`), shaped around the raw
source's teaching content. Use **at most one per batch** — this was the
over-used family that triggered the 2026-09-05 correction.

**Family B — Joey's own newly-mined structures (#20-23).** Supplied directly by
Joey 2026-09-05 from his real archive, including the single highest engagement
rate found in the account so far (#22, 14.53%). Treat these as first-class, not
fallback:
- **#20 Problem Illumination** — name a felt problem, reframe it, explain the
  mechanism/why, close with the stakes.
- **#21 Warning Command** — Never/Don't + a permission clause + urgency + a
  scripture citation + a casual aside + a restated closing warning.
- **#22 Diagnostic with Branching Outcomes** — "You know you've truly X when Y."
  Two branching outcomes, both answered with the same calm. Highest-evidence
  structure in the bank — reach for this one whenever the note supports a clean
  internal-state definition.
- **#23 Narrative Parallel (Typology)** — narrate a concrete Bible scene with real
  dialogue/detail, let an object's transformation carry the metaphor, extract one
  principle, close with a contemporary rally line. Only use when the wiki note or
  raw source actually contains the Bible narrative in enough detail to narrate
  concretely — don't reach for a Bible story from memory to force this structure.

**Family C — Original mined structure-bank devices**, used only when a note's
content genuinely calls for one (a clean paradox fits #4, a hard list fits #3 or
#9, a sharp two-line distinction fits #19) — not as a default lens:

**Eligible:** #1 Unglamorous Absolute · #2 Definition Flip · #3 Absurdly Simple List ·
#4 Counter-Intuitive Method · #5 Reversed Posture · #6 Research Reveal · #8 Blunt
Command · #9 Stacked Directive · #13 Compressed Aphorism · #15 Trait Redefinition ·
#16 Open Question · #18 Optimal-Decision Release · #19 Cleared Suspect

**Never use, any family:** #7 Scene Testimony, #10 Confession-to-Principle, #11
Milestone Number, #12 Rock-Bottom List Promise, #14 Unresolved Confession (all
require a personal story) — and #17 Pre-empted Critic (flagged do-not-use in the
bank itself).

### 4. Draft five — 3 short, 2 long
- **No fixed reading-level target.** A grade-2 rule was tried and reversed
  2026-09-05 — the real archive runs grade 2.3 to 14.3, averaging ~5-6. Don't
  simplify vocabulary to hit a number; use the account's own words ("proximity,"
  "meditation") where they fit. Readability follows from the voice register in step
  3, not from a separate pass.
- **3 short** — roughly 100–250 characters. Aphoristic weight, matches the account's
  246-char median. Best fit: #2, #13, #15, #16, #19.
- **2 long** — pushed toward the cap, roughly 400–500 characters, single post.
  Best fit: #1, #3, #6, #9, #18. Only split into a cliffhanger thread (per
  `threads-voice.md`'s split rule) if the content genuinely can't fit at 500 —
  don't default to splitting.
- Apply every rule in `threads/threads-voice.md`: line break between ideas, God/He/
  Him/His/Father/Lord always capitalised, British spelling, sincere register (no
  irony, no hedging), declaratives not qualifiers.
- **Always count actual characters** on the drafted text and state ONE POST (with
  count) for every option — never estimate, never hand over undercounted copy.
- **Default to the tighter cut.** Confirmed rewrite pattern (see the Rewrite log in
  `threads-voice.md`): Joey consistently trims qualifying or mirrored clauses down to
  a flatter, shorter line. If a draft has a clause like "is the only one that
  actually…" or a mirrored abstract second half, write the cut version, not the
  fuller one — check `threads-voice.md`'s Rewrite log for the latest state of this
  rule before drafting.
- **Structure #5's "waiting on" mirror is unconfirmed for this account.** Cut or
  fully rewritten both times it's been drafted so far. Prefer #4 Counter-Intuitive
  Method or #2 Definition Flip for a passive-to-active reveal idea instead — check
  the Rewrite log for the current state of this before defaulting to #5.
- **Quote verified scripture in the post, not just the source-line footnote.** If the
  wiki note contains the exact scripture text and it's directly relevant, include it
  in the post body with a citation: `"[quote]" - [Book Ch:V]`. Don't sanitize a
  verified quote out of the draft — that's over-caution, not the actual rule.
- **Name over pronoun.** When introducing God/Jesus/the Father in a line, prefer the
  actual name over "Him"/"He" where it reads naturally — matches
  [[name-the-specific-noun]] elsewhere in this workspace.

### 5. Check against the reject list before showing Joey
From `threads/threads-voice.md` and `threads/README.md`:
- No shaming, no manufactured antagonist/dunking
- No invented spiritual experience (moot here — no testimony at all)
- No scripture or doctrine quoted from memory — must trace to the raw source (or the
  wiki note if the raw source couldn't be located, per step 2b's fallback)
- No guaranteed outcomes or prosperity promises
- No stacked abstract triplet (three abstract benefits in a row)
- No corporate/marketing register

Build a rubric table, one row per rule, one column per draft (A–E) — same format as
`threads/posts/2026-08-17-unconventional-mistake-drafts.md`. Flag anything uncertain
(a doctrinal framing that's an interpretation rather than a direct quote) rather than
silently asserting it.

### 6. Save and hand off
Save to `threads/posts/YYYY-MM-DD-{slug}.md`:
- Header + `*Drafted [date]. Status: UNPOSTED — awaiting Joey's pick.*`
- `*Wiki note: `{note-file}.md` · Raw source(s): `{raw-file-1}.md`, `{raw-file-2}.md`*`
- Each option: structure name + number, character count, the post text, one line on
  why it works / what raw-source line or image it pulls from
- The rubric table
- A `Related:` line linking `[[threads-README]] [[threads-voice]] [[structure-bank]]`

**Stop there.** Present the five options in chat and the saved path. Do not pick one
for him, do not rewrite into the LOCKED format, do not touch
`data/threads-archive.csv` — those are separate, later, manual steps.

### 7. When Joey reports his pick — bank it, don't just move on
Whenever Joey comes back with what he actually went with (verbatim or edited), diff
it against the draft it came from and log it to the **Rewrite log** section at the
top of `threads/threads-voice.md`:
- **Edited** → note exactly what was cut, swapped, or added, dated. This is the voice
  correcting the draft — the file's own words for it.
- **Posted verbatim** → log the confirmation too. Not every entry is a correction;
  an unchanged post validates that structure/phrasing choice.
- **A pattern repeats across two or more logged instances** → promote it from a
  logged instance to a standing rule in the log's own "apply going forward" note, and
  actually apply it in the next batch of drafts. Don't wait for a third correction of
  the same thing.

This is the same discipline the copy-rubric judge runs for Flexxable work — corrections
get banked so the next draft is better, not just noted and dropped.

## Rules that bite here
- **No testimony, period.** Never read `testimony-bank.md`, never write a personal
  story or first-person life claim. Joey adds that himself if he wants it.
- **Wiki or nothing.** Every theological claim traces to a specific note in Second
  Brain. No topic in the wiki → say so, don't draft from memory.
- **Wiki finds it, raw source writes it.** The wiki note confirms the topic exists;
  the actual post language comes from the raw source(s) in its `sources:` frontmatter
  (step 2b). Drafting straight off the wiki's paraphrase reads flat — confirmed
  2026-09-05.
- **No-topic ≠ invent one.** Suggest real note titles Joey hasn't drafted from yet,
  never a topic that isn't an actual note.
- **5 drafts, 3 short + 2 long, varied structures** — not five of the same shape.
- **Character count is mechanical, not a guess.** Count the actual drafted text.
- **Stops at options.** No locking, no posting, no archive logging — Joey's call,
  separately.

Related: [[threads-README]] [[threads-voice]] [[structure-bank]] [[testimony-bank]]
