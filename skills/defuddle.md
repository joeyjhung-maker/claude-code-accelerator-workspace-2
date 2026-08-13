# defuddle

No command — Claude reaches for it when reading a web page.

Use it when you want the *actual words* off a page, not a summary of them.

WebFetch runs a page through a small model and hands back a summary. Defuddle strips the nav, ads, and clutter and returns the real text. For swipe capture and market-language mining, the difference matters — a summary launders out the exact phrasing that makes a swipe worth keeping.

Feeds `swipes/`, `/storm`, `hook-miner`, and `mechanism-finder`.

Runs via `npx --yes defuddle` (no global install — this machine's npm global folder is root-owned and would need sudo).

From [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills). MIT.

Actual runtime file: `.claude/skills/defuddle/SKILL.md`
