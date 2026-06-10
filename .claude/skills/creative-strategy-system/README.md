# Creative Strategy System — Kit (v2)

This is the thing a workshop participant uploads into their Claude Code. It teaches Claude the entire
creative-strategy flywheel, scaffolds their workspace, and walks them from a first real win to building
out the whole system — manually, hybrid, or fully automated. Works on plain Claude Code; better with a
Genesis API key (trained bots) or the Exodus app (done-for-you).

**v2** folds in a full pass of operator feedback: it's a *scaffold the user owns and edits* (not gospel),
it's **strategy-first** (choose what to make before making it), it offers two paths after onboarding
(execute fast / build the system), and it carries a thick set of operating rules — lead with conviction,
do only what's asked, never lecture compliance, full clickable links, never freehand copy (prime first),
list everything at once, and bake every edit back into the primers.

## What's in here
- **`SKILL.md`** — the master skill (the orchestrator). This is what Claude reads and runs: onboard →
  scaffold → first win → build outward.
- **`knowledge/`** — everything the skill leans on:
  - `00-canonical-walkthrough.md` — **the canonical system** (the complete teaching walkthrough; the
    master skill is grounded in this — Strategy Map, Production Plan, Allocation Mix, chad logic,
    per-node tools, the after-session skill, CAST-as-scripts).
  - `00-full-system-reference.md` — the deep 16-part compendium (extra reference).
  - `01-node-types-and-build.md` — the 7 node types + where each lives/runs.
  - `02-cast-video-grammar.md` — the CAST video framework.
  - `folder-scaffold.md` — the full annotated workspace structure.
  - `genesis-exodus-keys.md` — the Genesis & Exodus key-fork wiring.
  - `kie-render-reference.md` — banked KIE render reference (one key = statics + video; endpoints, the
    User-Agent/upload gotchas, the disappearing-screenshot rule, the ultra-real prompt template).
  - `tool-registry.md` — a real tool behind every node (simple → pro).
  - `frameworks/` — the focused tools: hook-quality, editing-rules, segments, iterations, STORMING/
    SCRAWLS/Copy Blocks.
- **`templates/`** — starter local bots (hook / writing / editing) copied into the user's `bots/` for
  the no-key path.

## How a participant uses it
1. Drop this folder into a project and open it in Claude Code (or install `SKILL.md` as a skill).
2. Say what they want ("help me make a hook from my winning ad"). The skill onboards, scaffolds, and
   routes them to a first win.
3. Build outward one node at a time from the Task Menu.

## How to test it SILOED (do this before shipping)
The kit must stand on its own — a customer has only this folder, none of your setup. To verify:
1. Copy ONLY this folder to a fresh empty directory on a clean path.
2. Open it in a Claude Code session with your global memory / other skills / MCP **off** (cleanest: a
   separate config/home or a throwaway container).
3. Act like a customer with nothing — no keys, no primers. Confirm the skill alone can onboard →
   scaffold → reach a first win **without reaching for anything that isn't in this folder or that it
   creates.** Any time Claude pulls "from your head"/your files, that's a gap to close in the kit.

## The bonus (later)
The **bot-builder** is a separate skill we build together — the factory that makes new bots/skills with
the user. `SKILL.md` has the stub.
