# Skill Observations

Running backlog of corrections and repeated patterns worth turning into a skill change. Logged by task-observer, actioned via /save-as-skill (new skills) or /upskill (existing-skill fixes).

Status key: OPEN = not yet actioned | ACTIONED (YYYY-MM-DD) — what changed | DECLINED (YYYY-MM-DD) — why

Related: [[Promotion]] [[Memory Loop]]

---

### Observation 1: Global npm installs need sudo on this machine — prefer npx

**Status:** OPEN
**Date:** 2026-08-13
**Skill:** Cross-cutting (hit during the CLI update, then again in defuddle)
**Issue:** `/usr/local/lib/node_modules` is root-owned, so any `npm install -g` fails with EACCES and needs a sudo password Claude can't supply. This came up twice in one day: updating the Claude Code CLI, then installing defuddle. Each time it cost a detour before landing on the workaround.
**Suggested fix:** Default to `npx --yes <tool>` for any Node CLI rather than a global install. Only escalate to `sudo npm install -g` (run by Joey in his own terminal) when a tool genuinely can't run via npx. Worth a line in the Script if it bites a third time.
