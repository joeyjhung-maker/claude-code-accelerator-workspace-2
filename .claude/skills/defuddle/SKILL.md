---
name: defuddle
description: Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to save tokens. Use instead of WebFetch when the user provides a URL to read or analyze, for online documentation, articles, blog posts, or any standard web page. Do NOT use for URLs ending in .md — those are already markdown, use WebFetch directly.
---

# Defuddle

Use Defuddle CLI to extract clean readable content from web pages. Prefer over WebFetch for standard web pages — it removes navigation, ads, and clutter, reducing token usage.

**Run it with `npx --yes defuddle`, not a global install.** This machine's `/usr/local/lib/node_modules` is root-owned, so `npm install -g` fails with EACCES and needs sudo. `npx` sidesteps that entirely and is confirmed working here.

**Why this matters in this vault:** WebFetch answers a prompt against a page via a small model — it returns a *summary*. Defuddle returns the page's actual text. For anything feeding `swipes/`, `/storm`, `hook-miner`, or `mechanism-finder`, verbatim market language is the whole point, so a summary is the wrong output. Use defuddle when capturing source material; WebFetch is fine when you only need a question answered.

## Usage

Always use `--md` for markdown output:

```bash
npx --yes defuddle parse <url> --md
```

Save to file:

```bash
npx --yes defuddle parse <url> --md -o content.md
```

Extract specific metadata:

```bash
npx --yes defuddle parse <url> -p title
npx --yes defuddle parse <url> -p description
npx --yes defuddle parse <url> -p domain
```

## Output formats

| Flag | Format |
|------|--------|
| `--md` | Markdown (default choice) |
| `--json` | JSON with both HTML and markdown |
| (none) | HTML |
| `-p <name>` | Specific metadata property |
