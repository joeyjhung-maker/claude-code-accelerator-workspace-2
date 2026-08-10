# Workflow: Vet a third-party AI tool before adopting it

Related: [[Promotion]] [[Memory Loop]]

Ran this same play five times in one session (claude-mem, OmniRoute, headroom, claude-code-setup, task-observer) — three passes, two adopted. Worth systematizing before it happens a sixth time on autopilot.

## When to use this
Joey drops a GitHub URL (or names a tool) and asks what it is, or whether we should use it.

## The steps
1. Pull repo metadata via `gh repo view` — stars, license, push activity, topics. Cheap signal on legitimacy and how alive it is before reading a word of prose.
2. Read the README for what it actually does and how it installs.
3. Check for red flags: global side effects outside the project (edits to `~/.claude.json` or similar), credential/BYOK exposure, self-admitted ToS risk, MITM-style proxying of LLM traffic, promotional language outweighing substance.
4. Ask whether it solves a problem *this* workspace actually has, not just a generic dev-tooling problem. Most don't — say so plainly and move on.
5. If it's a genuine fit, don't install wholesale. Trim it to the vault's existing conventions (file locations, naming, single-operator scale) and wire it into what already exists instead of standing up a parallel system.

## What good looks like
task-observer: pulled the real skill file, cut the multi-session concurrency machinery it didn't need, redirected its output to `skills/observations.md`, and wired it into `save-as-skill`/`upskill`/`reflect` instead of becoming a fifth competing pipeline.
