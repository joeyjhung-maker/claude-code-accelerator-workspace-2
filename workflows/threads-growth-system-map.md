# Threads Growth System — V1 Map

**Status:** awaiting go. Nothing built yet.
**Account:** [@joeyhung_](https://www.threads.com/@joeyhung_) — 1,173 followers as of 15 Aug 2026
**Context target:** 5,000 followers by 15 Nov 2026 (not something V1 measures — see Out of scope)
**Apify ceiling:** $10/month

---

## V1 is two deliverables. Nothing else.

### A — The post archive
Every post Joey has published, full copy, with its metrics attached.

- Source: **Threads API** (live and authenticated — this is unblocked right now)
- Reconciled against the Notion archive to catch anything the API can't reach
- Columns: date · full post text · lane · views · likes · replies · reposts · quotes · media type · single vs thread · permalink
- **Must be appendable** — Joey adds future posts and tracks performance in the same place

Known issues going in:
- Notion mixes drafts and published posts with no marker. The API is the source of truth for what actually ran; Notion is only a cross-check.
- Green highlighting in Notion does not survive extraction. Real metrics replace it.
- April 26 and July 26 are missing from Notion.
- Unknown how far back Threads Insights serves data. This caps how deep the metrics go, and we won't know until we pull.

### B — The viral structure bank
A bank of post structures that perform, drawn from scraped high-engagement Threads posts.

- Source: **Apify**, 20 seed accounts, 1K–50K followers, both lanes
- Pull **top and median** samples — the delta between them is the finding. Top-only analysis just teaches you what all posts have in common.
- Normalise engagement **per follower**. A 300-like post from a 1K account is a better model than a 10K-like post from a 500K account.
- Analysis by dimension split: sub-agents each seeing one dimension across the corpus, blind to the rest — opening line · shape and whitespace · skeleton · what obliges a reply · landing line · specificity markers · stance/POV · length band. Each reports top-vs-median frequency and the gap.
- Bank entries record **structure**: skeleton, the mechanism, lane fit, evidence delta.
- **Raw scraped posts are also stored**, in a separate reference file, so Joey can look at the source examples behind any structure. Private research reference — the structures are what we write from, and copy we publish is always original.

---

## Explicitly out of scope for V1

- Writing or structuring Joey's posts
- Reply strategy — Joey handles this himself
- Cadence planning, lane ratios, production scheduling
- The fortnightly measurement loop
- Anything touching the 5K follower target

Parked, not deleted. Revisit after V1 is in hand.

---

## Infrastructure

| Piece | Tool | Status |
|---|---|---|
| Own posts + metrics | Threads API (dev mode) | **Live — Deliverable A unblocked** |
| Corpus scraping | Apify | **Not configured — blocks Deliverable B** |
| Token refresh | Script, 60-day expiry | Not built |

Permissions live: `threads_basic`, `threads_manage_insights`, `threads_manage_replies`, `threads_content_publish`.
`threads_profile_discovery` added but parked — needs App Review (2–4 weeks, Tech Provider verification). Apify covers it instead.

Token expires ~14 Oct 2026. Refresh script is small but load-bearing; if the token lapses the Meta console setup has to be redone from scratch.

---

## Open

- Where the archive lives — Google Sheet or local file
- 20 seed accounts — Claude hunts once the Apify key lands, Joey narrows
