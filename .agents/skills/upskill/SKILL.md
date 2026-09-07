---
name: upskill
description: Periodic maintenance for your skills library. Scans your installed skills, flags stale or unused ones, finds near-duplicates that should merge, and proposes a leaner set. Run every few weeks so the library does not bloat into the 80-skill problem. Maintenance, not daily.
---

# Upskill

Keeps the library lean so it stays fast and usable. The opposite of installing everything you see.

## When to run
Every few weeks, or when see-your-setup flags skill bloat. Not a daily skill.

## Process
1. List every installed skill and, where you can tell, when it last fired.
2. Check skills/observations.md for OPEN entries against existing skills (not "new skill candidate" ones — those are save-as-skill's job). Fold each into the proposal below as a targeted fix, not a rewrite.
3. Flag three groups: stale (never or rarely used), duplicate (two skills doing nearly the same job), and bloated (one skill trying to do three things).
4. Propose the moves: remove the stale, merge the duplicates into one, split the bloated, apply the observation fixes. One line of reasoning each.
5. The operator approves. Apply only what they approve. Mark actioned observations `ACTIONED (YYYY-MM-DD) — [what changed]`; mark declined ones `DECLINED (YYYY-MM-DD) — [why]`.
6. Report the new count and what changed.

## Rules
- Lean beats complete. Five sharp skills beat forty installed.
- Never remove a skill without approval. Propose, do not delete.
