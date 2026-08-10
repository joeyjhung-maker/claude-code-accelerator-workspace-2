# task-observer

No command — this one runs quietly in the background of any session using a skill.

Use it when a correction you gave Claude should stick permanently, or when you notice yourself doing the same manual thing for the second time.

It doesn't touch winners/losers/brand/clients (that's [[reflect]] and [[remember-this]]) and it doesn't write a new skill file itself (that's [[save-as-skill]]). It just notices and logs, so the pattern doesn't evaporate when the session ends.

Backlog lives at `skills/observations.md`. New-skill candidates get picked up by `/save-as-skill`. Existing-skill fixes get picked up during `/upskill`.

Adapted from Eoghan Henn's "One Skill to Rule Them All" (rebelytics.com, CC BY 4.0), trimmed down — the original is built for teams with parallel sessions writing to a shared log; this workspace is one operator, so the concurrency machinery got cut.

Actual runtime file: `.claude/skills/task-observer/SKILL.md`
