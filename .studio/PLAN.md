# The Studio — plan + data check

*LOTR pixel-art live dashboard over the creative-strategy flywheel. Built 2026-07-10.*

## The decision this screen improves
"What's cooking, and what do I do next?" — where this week's work sits in the
pipeline (seeds banked → briefs ready → copy written), what changed recently,
and which stage needs Joey's hand.

## Lane
Ops readiness (what's blocked / what's next), dressed as a quest map.
Visual language is deliberately NOT the standard design system — Joey asked for
LOTR pixel art. Decision-first principles stay: quest log first, statuses, next action.

## Data it trusts (all live reads from the vault — no copies, no samples)
| Number | Source | How it's worked out |
|---|---|---|
| Seeds banked | `clients/flexxable/seeds/*.md` | count of `^## ` headers per file |
| Briefs ready / written | `clients/flexxable/briefs/*.md` | YAML frontmatter `status:` |
| Copy shipped | `copy/*.md` | file count; "this week" = mtime in last 7 days |
| Winners / losers | `winners/`, `losers/` | file counts (minus `_*` templates) |
| Room activity | any room folder | max mtime: hot <30min, warm <24h, else quiet |
| Leaderboard | `swipes/market-leaderboard.md` | shown verbatim |
| Trigger words | `clients/flexxable/trigger-words.md` | shown verbatim (may not exist yet) |

## Data it does NOT trust / doesn't exist yet
- `account-reads/`, `hypotheses.md`, `trigger-words.md` don't exist yet →
  every room renders a designed empty state ("No quest scroll yet — run
  /account-read"), never a blank.
- VOC copy bank lives OUTSIDE the vault (`~/Downloads/market-research/copy-bank/
  voice-of-customer.md`) → allowed via explicit whitelist only.

## Rooms → folders
| Room | Stage | Folders |
|---|---|---|
| Palantír Tower | /account-read + Monday sweep | market-leaderboard, trigger-words, account-reads/, strategy-map, hypotheses |
| The Deep Mine | research | swipe-bank/** , parsed-hooks-bodies-headlines, VOC bank (whitelisted) |
| Weathertop | /storm | seeds/ |
| Council Hall | /brief | briefs/ (status chips) |
| The Forge | /produce | copy/, creatives/ |
| The Library | reference | brand/, concepts/, rubrics/, the-data-dictionary |
| Golden Hall | winners+losers | winners/ (hall), losers/ (the barrow) |

## Build shape
- `.studio/server.js` — zero-dependency Node (v24 present). Static + `/api/state`
  + `/api/file?p=` (sandboxed to vault root + whitelist; .md/.txt only). Port 4173.
- `.studio/public/` — one page: SVG pixel map, parchment theme, Uncial Antiqua +
  VT323 (vendored woff2). Click room → scroll panel: file list → rendered markdown
  (client-side mini renderer w/ tables). Quest log scroll top-left.
- Read-only by design: the server NEVER writes to the vault.
- Start: `.claude/launch.json` name "studio" + `Open The Studio.command` (root).

## Verify before done
Open via the real flow (launch), click every room, open a file with a table
(copy-rubric), confirm empty states for missing files, confirm sandbox rejects
path traversal.
