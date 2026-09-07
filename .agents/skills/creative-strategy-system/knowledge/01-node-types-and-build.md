# NODE SPECIFICATION — Creative Strategy System

**Purpose.** This file teaches a Claude Code instance the canonical parts of a creative-strategy system and where each one lives, runs, and gets built. When the user wants to stand up their own system, use this to scaffold the project, place each node in the right home, and pick the right tool for their level. Default to **local-first**: everything lives in one project folder the user opens in Claude Code. Graduate a single node to a cloud service ONLY when it must (a) run unattended/scheduled, (b) hold scale beyond local files, or (c) be served to other people.

---

## 1. The seven node types (canonical · MECE · sorted by FUNCTION, not file format)

Every node in the system is exactly one of these. The discriminator is what role it plays in the circuit — multiple types are plain markdown, so file format is NOT the cut.

| Type | Function test (the discriminator) | Role |
|---|---|---|
| **Code** | Deterministic — runs the same every time | Mechanical work: scrape, score, pull, format, orchestrate |
| **Bot** | Transforms input → output using a model | Active instruction (prompt/skill) that writes, edits, classifies, ideates |
| **Knowledge** | Read/injected; never acts on its own | Passive reference: primers, swipe banks, frameworks, docs |
| **Database** | Queried/filtered/accumulated by row | Structured store: hypotheses, seed bank, coverage matrix, saved rules |
| **Connection** | A wire/credential to an outside service | MCP socket + API key |
| **Surface** | A screen a human sees and acts in | Visual instrument: maps, canvases, dashboards |
| **Human** | Judgment / the optional gate | Selection and taste (not a build artifact) |

**Boundary rules (resolve these explicitly when classifying a node):**
- **Bot vs Knowledge** — both markdown. Bot *produces output*; Knowledge *gets read into a bot*. A skill file = Bot. A primer = Knowledge.
- **Knowledge vs Database** — Knowledge is read **whole/injected**; a Database is **queried for rows**. A primer = Knowledge; a tagged ad-coverage table = Database.
- **Surface vs Human** — Surface is the screen; Human is the judgment. Either can exist without the other (a voice-note gate has no surface; a read-only dashboard has no gate).
- **Connection vs Code** — Connection is the wire+key; Code is the logic that uses it. They compose (Python pulling a Meta report = Code using a Connection).

---

## 2. Where each node lives, runs, and gets built

`SIMPLE` = the default to scaffold first (local, in-repo). `PRO` = graduate target. `WHEN` = the only reason to graduate.

### Code
- **Lives:** `*.py` in the repo (`/code` or `/scripts`).
- **Runs:** on demand inside Claude Code (it executes the shell). Recurring → local `cron` or Claude Code scheduling.
- **SIMPLE:** local scripts, run on request.
- **PRO:** trigger.dev · Modal · Railway · GitHub Actions.
- **WHEN:** must run unattended/scheduled or serve others. Not required to build.

### Bot
- **Lives:** `*.md` in the repo (`.claude/skills/<name>/SKILL.md`, or `/bots/<name>.md`).
- **Runs:** inside the user's own Claude Code (the model executes the prompt). Scriptable via the Anthropic API.
- **SIMPLE:** markdown prompt/skill files, invoked locally.
- **PRO:** a hosted, stateless bot server (2-step prime→instruct protocol).
- **WHEN:** only to let OTHER people use the trained bots. Never needed for self-use.

### Knowledge
- **Lives:** `*.md` in the repo (`/knowledge`, `/primers`) OR an Obsidian vault on disk.
- **Runs:** n/a — read/injected into Bots.
- **SIMPLE:** local markdown folder or Obsidian vault; Claude Code reads it directly.
- **PRO:** same, git-versioned.
- **WHEN:** effectively never. Local markdown is correct long-term.

### Database (+ optional RAG)
- **Lives:** a store the repo or app reads.
- **SIMPLE ladder:** flat files (markdown/CSV/JSON) → **SQLite** (one local file) → **Airtable / Google Sheets** (visual, non-dev friendly).
- **PRO:** **Convex** (reactive, app-backing) · **Supabase** (Postgres + API, friendly middle) · Postgres.
- **RAG:** prefer **none** at small scale — let Claude Code grep/read the markdown (context beats retrieval until the corpus exceeds the window). When needed: local vector store (**LanceDB · Chroma · sqlite-vec**) or managed (**Supabase pgvector · Turbopuffer · Pinecone**).
- **WHEN:** a Surface needs live data, multiple users, or scale beyond local files.

### Connection
- **Lives:** API keys in `.env` at repo root, OR MCP servers in Claude Code settings.
- **Runs:** invoked by Code or via MCP from Claude Code.
- **SIMPLE:** `.env` keys + MCP servers, added one at a time as each node needs them.
- **Registry (add as needed):**
  - **Meta Marketing API** — REQUIRED. Read performance + comments (Analysis); push/ship (Creative).
  - **Apify** — scrape reviews, comments, ad library (Strategy/Ideation research).
  - **Whisper** — transcribe voice-note dumps.
  - **Meta Ad Library** / **Hookd AI / Get Hooked** — swipes.
  - **Image gen:** KIE.ai (gpt-image, nano-banana) · fal.ai · OpenAI Images · Midjourney.
  - **Video / avatar gen:** Higgsfield · Runway · Kling · Veo · HeyGen · Hedra (CAST Actor/Style).
  - **Voice:** Wispr Flow (edit steer) · ElevenLabs (VO).
  - **Docs:** Google Docs API (finish step).

### Surface
- **Lives:** a single self-contained `*.html` (inline CSS/JS) in `/surfaces`.
- **Runs:** opened locally via `file://` in a browser. Claude Code authors/edits the file.
- **SIMPLE:** one HTML file (pattern: a faceted instrument like a segment map or editing canvas).
- **PRO:** Vite/React app hosted on Netlify/Vercel; reads live data from Convex/Supabase.
- **WHEN:** needs live DB data or sharing.

### Human
- **Lives:** n/a. The user. Gates are optional (bypassable).
- **Acts via:** a Surface, a voice note (Wispr), or a yes/no.

---

## 3. Recommended project structure (scaffold this)

```
creative-strategy-system/
├── .env                       # Connection keys (Meta, image/video gen, etc.)
├── .claude/
│   └── skills/                # Bots (each = a SKILL.md)
│       ├── hook-bot/
│       ├── writing-bot/
│       ├── editing-bot/
│       └── classifier-bot/
├── code/                      # Code (Python scripts)
│   ├── pull_meta_report.py
│   ├── score_ads.py
│   ├── scrape_reviews.py
│   └── orchestrate.py
├── knowledge/                 # Knowledge (markdown; or point at an Obsidian vault)
│   ├── primers/
│   │   ├── payload/           # awareness × length primers
│   │   └── conceit/           # format/vehicle primers
│   ├── swipe-bank/
│   └── frameworks/            # STORMING, SCRAWLS, CASHED, CAST, Copy Blocks
├── data/                      # Database (start as files/SQLite)
│   ├── seed-bank.md
│   ├── hypotheses.sqlite
│   └── coverage.json
└── surfaces/                  # Surface (single-file HTML instruments)
    ├── segment-studio.html
    └── editing-canvas.html
```

---

## 4. Build heuristics (decision rules for the assistant)

1. **Classify before building.** For any node the user names, identify which of the 7 types it is using the function test + boundary rules. State it.
2. **Local-first by default.** Place every node in the repo with its SIMPLE tool. Do not introduce a cloud service unless a graduation trigger (unattended/scheduled · scale · serve-others) is explicitly present.
3. **Meta API is the only required Connection.** Add others only when the node that needs them is being built.
4. **Prefer files over a database, and grep over RAG,** until size forces the upgrade. Call out the upgrade trigger rather than pre-building.
5. **A Surface is one HTML file** until it needs live data or sharing.
6. **Bots are markdown the user runs in their own Claude Code.** Only mention a server in the context of serving others.
7. **Everything runs from Claude Code pointed at the one project folder.** That folder IS the system.

---

## 5. One-line model

**Claude Code + one repo = the workshop.** The system is almost entirely local markdown (Bots + Knowledge) + Python (Code) + HTML (Surfaces) + a few keys (Connections), with small Databases as files. Cloud services (bot server, Convex/Supabase, trigger.dev) are the graduation path you take only when you stop building for yourself and start running on autopilot or for others.
