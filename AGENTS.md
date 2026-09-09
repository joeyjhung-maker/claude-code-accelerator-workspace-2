# AGENTS.md

*This is the Codex-CLI equivalent of CLAUDE.md ("the Script"). CLAUDE.md is what Claude Code reads in this repo; AGENTS.md is what Codex reads. Keep both in sync when the rules change — this file translates the same rules into things a plain file-reading/writing agent can follow without Claude Code's skills, subagents, or MCP tools.*

## Who I am
Marketing director for coaching brands. My work is ad copy, hooks, and the strategy underneath — building paid creative that converts for coaches and infoproduct sellers.

## How to work here
- Before writing anything, go read an example first — a real swipe or a past winner, not a blank prompt. Pull from `swipes/`, `winners/`, or a client's `winning-ads.md`.
- Hook first. Write and stress-test the hook before writing body copy.
- Never invent a client result, number, or quote. If it's not in the client file under `clients/{name}/`, ask instead of guessing.
- Follow the "Rules that bite" section below on every piece of copy, no exceptions.
- Before showing me finished copy, self-check it against `rubrics/copy-rubric.md` and note where it might fail, rather than presenting it as done.
- **Dan Skool/Mariobot route (2026-09-08):** Generate Dan's Skool drafts without the legacy style contract (`run_mario.py --no-style-contract`), then judge with `rubrics/dan-skool-chatgpt-rubric.md`. The judge prioritizes selling power and Dan's voice, preserves Mariobot's personality, makes only 1–3 high-impact edits, and mentions only hard factual uncertainties—not minor nitpicks. Do not apply the old copy-rubric/lint rewrite process to these drafts.
- Read `the-data-dictionary.md` before deciding what's worth writing back into `winners/`, `losers/`, `brand/`, or `workflows/` — that file is the rule for what compounds.
- **Read the relevant playbook before running a stage.** This repo's process (storm → brief → produce → reflect) is written out as plain markdown "skills" for Claude Code at `.claude/skills/{name}/SKILL.md`. You don't have Claude Code's slash-command system, but the files are just instructions — open the one that matches what I'm asking for and follow it step by step:
  - `.claude/skills/storm/SKILL.md` — generate raw ideas/seeds, no copywriting yet
  - `.claude/skills/brief/SKILL.md` — lock the DNA of an ad (segment, awareness, mechanism, hook angle) before any copy exists
  - `.claude/skills/produce/SKILL.md` — the only stage that actually writes copy, from a locked brief
  - `.claude/skills/reflect/SKILL.md` — end-of-session promotion of what worked/died into memory
  - Same pattern for the Skool-specific variants (`storm-skool`, `brief-skool`, `produce-skool`).
- **No persistent memory across sessions.** Claude Code keeps an auto-memory file outside this repo (`~/.claude/projects/.../memory/`) that you can't see. Anything durable that should survive between sessions with you needs to live in this repo instead — in `brand/voice.md`, a client's `client.md`, or this AGENTS.md file. If you learn something that should stick, say so explicitly so it gets written into one of those files rather than assumed remembered.
- Start of session: check the most recent file in `daily/` for what was still outstanding before starting new work.
- End of session: log a short entry to today's daily note (`daily/YYYY-MM-DD.md`) — what got made, what's still open.
- **Concurrent Git ownership:** Claude Code and Codex may work against this repo at the same time. Never run `git add -A`, `git add .`, or `git commit -a`. When committing, stage only the specific files Codex created or modified in the current session, named explicitly. Leave every other modified or untracked file untouched. If ownership of an unstaged file is uncertain, ask Joey before staging it.

## Where things live
Reference (feeds the work):
- Concept notes: `concepts/`
- Voice rules: `brand/voice.md`
- Hook craft: `brand/hooks.md`
- Swipes to model, by mechanism: `swipes/`
- What worked and why: `winners/`
- What died and why: `losers/`
- Repeatable plays: `workflows/`
- A specific client's context and rules: `clients/{name}/client.md` (plus `primers/`, `strategy-map.md`, `seeds/`, `briefs/`, `winning-ads.md`)
- JV partner deals: `jv/JV-map.md`
- Copy-quality rubric: `rubrics/copy-rubric.md`

Production (what gets made):
- Written work (hooks, headlines, long-form): `copy/`
- Visual work (statics, video): `creatives/`

Flow:
- Unsorted drop zone: `inbox/`
- Daily notes: `daily/`
- Finished or retired work: `archive/` (never delete from here)

## Rules that bite
- Short punchy paragraphs. One idea per line. Each sentence earns its own line. If it reads like an essay, rewrite it.
- No corporate or agency language. Banned words: "leverage," "solution," "deliverable," "onboarding." Write like texting a mate who happens to be a business owner. Casual, direct, Australian-inflected.
- Never open copy with student proof or testimonials. Don't default to pain-first either — lead with curiosity, novelty, a promise, or a world-level hook; use pain as the amplifier once attention is earned, not the opener.
- Never write in blocks of text. A wall of text is an instant delete.
- Never invent a client result, number, or quote. If it's not in the client file, ask.
- If unsure what good looks like, ask for an example before guessing.
- Two moves when copy is done: save the work into `copy/` or `creatives/`, and separately promote the lesson (why it won or died) into `winners/`, `losers/`, `brand/`, or `workflows/`. Don't skip the second move.

Related: [[CLAUDE.md]]
