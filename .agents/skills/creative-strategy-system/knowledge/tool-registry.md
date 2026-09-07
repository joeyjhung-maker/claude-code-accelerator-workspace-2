# Tool Registry — a real tool behind every node

For each node type and each stage, the **simple default** (start here, local-first) and the **pro**
option (graduate only when scheduled/unattended, at scale, or serving others). Add a tool only when the
node that needs it comes online — never wire everything on day one.

## By node type
| Node | Simple (start) | Pro (graduate) | Graduate when |
|---|---|---|---|
| **Code** | local Python, run on demand in Claude Code | trigger.dev · Modal · Railway · GitHub Actions | must run unattended/scheduled |
| **Bot** | markdown in `bots/`, run in your Claude Code | hosted bot server (e.g. Genesis) | to let *others* use your bots |
| **Knowledge** | local markdown / Obsidian vault | git-versioned | ~never |
| **Database** | files (md/CSV/JSON) → SQLite → Airtable/Sheets | Supabase · Convex | a Surface needs live data / scale |
| **RAG** | let Claude Code grep/read the markdown | LanceDB · Chroma · sqlite-vec · Supabase pgvector | corpus exceeds context |
| **Connection** | `.env` keys / MCP servers | — | — |
| **Surface** | one self-contained HTML file (`file://`) | Vite/React on Netlify/Vercel + DB | live data / sharing |

## By stage (the connections you reach for)
- **Analysis:** Meta Marketing API (pull report + comments). KPIs you define.
- **Ideation / STORMING:** **scrapecreators.com** (paste an ad link → text+media for swipes) · Meta Ad
  Library / **Hookd** / **Get Hooked** (swipe libraries) · **Apify** (scrape reviews/comments) · Meta API
  (organic comments) · template bots · the matrix gap finder (fed by the Strategy Map) · inside-vectors bot.
- **Copy:** none required (primers = Knowledge, bots run locally). Genesis bots optional.
- **Editing:** **Wispr Flow** (voice steer — types what you say) · the canvas (a writing bot; run in
  **Poe** / Claude Code / Genesis server) · steer-prompts (markdown buttons) · the after-session skill.
- **Creative — images:** **KIE.ai** (gpt-image + nano-banana pro — *primary*) · **Higgsfield** (stylized) ·
  Midjourney / fal.ai (optional). **Video:** the same one **KIE** key also does video (**Veo · Kling ·
  Sora**) · **Higgsfield** (stylized, separate key). **Avatars (talking person):** **HeyGen · Hedra.**
  **Ship:** Meta API. (Render endpoints + craft: `kie-render-reference.md`.)
- **Voice-note dumps / transcription:** Whisper. **Finish doc:** Google Docs API.

## The required minimum
Just **the Meta connection** to read what's working and ship. Everything else is muscle you add one node
at a time. Most of the system is markdown + Python + HTML in one folder, run from Claude Code.
