---
name: task-observer
description: Passive noticer that runs alongside any session using a skill. Watches for corrections that reveal a skill is wrong or incomplete, and for repeated manual patterns that should become a new skill. Logs candidates to skills/observations.md for later review — never edits a skill directly and never touches content memory (winners/losers/brand/clients, that stays reflect's and remember-this's job). Adapted from Eoghan Henn's "One Skill to Rule Them All" (rebelytics.com), trimmed for a single-operator workspace.
---

# Task Observer

Skills improve from friction noticed during real work, not from sitting down to "improve a skill." This formalizes that noticing so it survives past the session it happened in.

**Scope, on purpose:** this skill only watches skill/process behavior — whether an existing `.Codex/skills/*/SKILL.md` got something wrong, or whether a repeated manual move should become a new one. It does not decide what's a winning hook, a dead angle, or a voice rule — that's [[reflect]] and [[remember-this]]. It does not write skill files itself — that's [[save-as-skill]]. This is the layer underneath both: it notices, they act.

## When to observe

Whenever a skill is in use this session — running `/produce`, `/brief`, `/storm`, any of them. Not active for casual chat or a quick factual question with no skill involved.

## What to log

**A skill got it wrong or missed something:**
- Joey corrects output a skill produced, and the correction isn't a one-off (it would apply again next time)
- a skill's rule gets violated or ignored in a way that suggests the rule needs to be sharper or structural, not just repeated
- a gap: something a skill should have handled but didn't cover

**A new skill candidate:**
- the same multi-step move happens for the second time in a session or across recent sessions
- Joey describes a process he "always does this way" that nothing currently captures

**Do not log:** a true one-off that won't recur; anything already covered by an existing skill rule; a client-specific preference that belongs in `clients/{name}.md` via remember-this instead.

## How to log

Append to `skills/observations.md` (create it from the template below if it doesn't exist yet). Do this quietly, in the moment or by the end of the session — don't hold it in your head and hope you remember at close-out.

```markdown
### Observation [N]: [short title]

**Status:** OPEN
**Date:** [YYYY-MM-DD]
**Skill:** [existing skill name, or "New skill candidate: [working name]"]
**Issue:** [what happened, specific enough to make sense weeks later]
**Suggested fix:** [concrete change — name the section for an existing skill, or scope for a new one]
```

Keep the Principle general — no client names or specifics in the title/suggested-fix if it's the kind of note that might outlive this client relationship. If it's genuinely client-bound, it probably belongs in `clients/{name}.md` instead, not here.

## Surfacing

At the end of a session, if anything new got logged, say so in one line — count and skill names, nothing more. Don't offer an "act now or later" choice every time; the default is log-and-defer.

Act in-session only when: Joey explicitly asks ("update the produce skill", "act on that observation"), or a skill is producing visibly wrong output right now and fixing the rule is faster than working around it.

Otherwise, observations sit as a backlog:
- **New-skill candidates** get picked up by `/save-as-skill` — that skill's own trigger ("noticed the same move twice or three times") is exactly what accumulates here.
- **Existing-skill fixes** get picked up during `/upskill`'s periodic pass, or whenever Joey wants to work through the backlog directly.

## Rules

- Notice and log. Never edit a skill file directly outside the two triggers above.
- Never touches winners/, losers/, brand/, clients/, or workflows/ — wrong folder, wrong job.
- Short entries, in plain language. This is a backlog, not a report.
- If `skills/observations.md` doesn't exist yet, create it with this header:

```markdown
# Skill Observations

Running backlog of corrections and repeated patterns worth turning into a skill change. Logged by task-observer, actioned via /save-as-skill (new skills) or /upskill (existing-skill fixes).

Status key: OPEN = not yet actioned | ACTIONED (YYYY-MM-DD) — what changed | DECLINED (YYYY-MM-DD) — why

Related: [[Promotion]] [[Memory Loop]]

---
```
