# Genesis & Exodus — the key forks (full wiring)

Three tiers of power. The system works on all three; the keys make it better.
- **Plain Claude Code** — local prompt-bots in `bots/`. You can do every node manually.
- **Genesis API key** — the trained server bots (pro-grade output) + deep-build calls.
- **Exodus app/key** — the done-for-you pipeline (runs the majority of the flywheel for you).

Detect at onboarding: read `.env` for `GENESIS_API_KEY` and `EXODUS_API_KEY`. Route accordingly.
Always confirm `ANTHROPIC_API_KEY` exists — Genesis needs it as the provider key.

---

## GENESIS — the trained bots

**Endpoint & auth.** Base URL admin-provided, e.g. `https://gas.copycoders.ai/api/v1`.
Every call needs BOTH headers:
```
Authorization: Bearer $GENESIS_API_KEY
X-Provider-Key: $ANTHROPIC_API_KEY      # the key that actually runs the model
```
- **List bots:** `GET $GENESIS_BASE_URL/models` → live roster with IDs + descriptions (new bots get
  added; always check live).
- **Call a bot:** `POST $GENESIS_BASE_URL/chat/completions`
  ```json
  { "model": "<bot-id>", "messages": [ … ], "stream": true }
  ```
  `stream: true` is **required**. Wait 1–2s between protocol steps. Sequential calls only on one key.

**The 2-step protocol (every bot is stateless — replay the whole history each call):**
1. **Prime** — send the full primer (winning ads). Bot replies "I've absorbed the patterns."
2. **Instruct** — send as a conversation: `[primer] → [bot's confirmation] → [your instruction]`.
3. **(Hooks only) Double-pass** — same conversation, push to Level 3: 10 hooks → sharpen → 10 more.

**Bot roster (most-used):**

| Stage | Bot ID | Does |
|---|---|---|
| Analysis | `media-buying-analysis-1` | Ads Manager CSV → spend/CPA/CTR/ROAS, star ads, budget issues |
| Analysis | `cash-analysisvariation-bot` | Deep read of top 5–10 ads — why they work, variation openings |
| Analysis | `comment-intel-1` | Ad comments → audience language, objections, buying signals |
| Ideation | `insight-vectors-bot` | Hidden patterns inside winners (Internal Vectors — I seeds) |
| Ideation | `75-ads-template-bot` | Extract a winning ad into a mad-lib template (Templates — T seeds) |
| Copy · hooks | `ad-hook-bot-1` | Hooks via 2-step + mandatory double-pass (20 total) |
| Copy · body+headlines | `mariobot` | 700–1500w body, headlines in the SAME conversation |
| Copy · swipes | `swiping-master-bot` | Faithful competitor swipe, run parallel to ad-hook-bot-1 |
| Video script | `infeed-vsl-bot` | In-feed VSL/video-script style (if available) |

**Parallelization (multiple Anthropic keys):** up to 3 briefs at once (one key each); body-1 / body-2
parallel; headlines wait for their body (same convo); swipe path parallel to hook path; sequential on
one key.

**Creative — images & video:** not on the Genesis server. One `KIE_API_KEY` covers BOTH — statics
(GPT-Image + Nano Banana Pro) and video (Veo / Kling / Sora). Higgsfield is a separate key, stylized
video only. Full render reference: `knowledge/kie-render-reference.md`.

**No Genesis key?** Use `bots/hook-bot.md`, `bots/writing-bot.md`, etc. on plain Claude. Still good —
just not the trained models. Recommend Genesis for serious volume/quality.

---

## EXODUS — the done-for-you pipeline

Exodus runs most of the flywheel for the operator. If they have it, route to the `exodus` CLI instead
of building the heavy nodes by hand.

**API (raw):** `EXODUS_API_URL=https://good-cod-360.convex.site`, `Authorization: Bearer $EXODUS_API_KEY`
(e.g. `GET /api/v2/swipe-library` → scraped competitor ads). **Pipeline keys it needs in `.env`:**
Anthropic + KIE (renders); ElevenLabs for video/Pixar.

**Command surface (what's reliable):**

| Capability | Command | Notes |
|---|---|---|
| Build primer | `exodus primer --file <winning-ads.md> --yes` | async; 4-primer split (body unaware/problem · body solution/product · hooks · headlines), built from their winning ads |
| Primer steering | `exodus primer steering` | set always-use / don't-use per primer |
| Write ads (workhorse) | `exodus genesis run --brief <brief.md>` | the reliable path; also the swipe path |
| From a reel/post | `exodus genesis --reel "<url>"` | canonical `/reel/<id>/` or `/p/<id>/` |
| Static images | `exodus image --ad "<copy>"` | infers native; copy-derived bundles Reptile/SCRAWLS |
| Templated statics | `exodus image --type template` | `--realism realistic`, `--mode manual --quantities` |
| Poll a long run | `exodus read-doc <runId>` | fire runs with `--no-wait`, then poll |

**The faithful swipe recipe** (use this, not `mirror`): `exodus genesis run --brief` with a brief that
has ① a numbered **beat-map** of the source ad (each beat's function), ② a **mechanism-swap** to the
brand's mechanism, ③ a **brand guard** ("do NOT mention <competitor/ingredients>"), ④ the **full source
ad** pasted at the bottom.

**Gotchas to know (so you don't misread a run):**
- Runs are long + server-side → `--no-wait` then poll `read-doc`. The "no documents yet" message
  contains the word **"failed"** — do NOT grep for "failed" to detect failure.
- Genesis VPS is ~1-concurrent — don't fire many at once (they queue/stall).
- KIE drops ~1–2 renders per batch (429) — re-fire.
- After any `exodus update`, `chmod +x node_modules/.bin/exodus`.
- `mirror` modes are unreliable (modular can ship the wrong brand) — prefer the brief recipe.

**What Exodus does for you (the speed-up):** categorizes winning ads into primer slots, writes briefs,
pulls from multiple brands, auto-generates reptile triggers + templates, runs the writing/static
pipelines. A good majority of the manual build — not 100%, but most of it.

---

## The routing rule (for the skill)

For any node the user wants:
- **Has Exodus?** → is there an `exodus` command for it? Use it (done-for-you). Else fall through.
- **Has Genesis key?** → route writing/analysis to the trained bots via the 2-step protocol.
- **Neither?** → use the local `bots/` on plain Claude Code.

Always be honest about the tier: plain = you can do it; Genesis = pro bots; Exodus = it does it for you.
