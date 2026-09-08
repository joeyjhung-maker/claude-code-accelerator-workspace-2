# CLAUDE.md

*This is "the Script": the doc Claude reads first, every session. The file stays named CLAUDE.md (that is the filename Claude Code loads); we call it the Script in the workshop. Keep it thin: who you are, how you work, where things live. Detail goes in the folders, not here.*

## Who I am
Marketing director for coaching brands. My work is ad copy, hooks, and the strategy underneath — building paid creative that converts for coaches and infoproduct sellers.

## How I work
- Show me an example before writing. I work from swipes and past winners, not blank prompts.
- Hook first. Body copy only after the hook survives a stress test.
- For anything client-facing: decide the shape, build it, then check it. For throwaways, fast and loose is fine.
- When a move works twice, we promote it into memory. When something breaks, we fix the rule, not just today's output.
- Use my voice and my swipes, not the model's average.
- For Dan Skool copy: run Mariobot without the legacy style contract, then use `rubrics/dan-skool-chatgpt-rubric.md` as the light judge. Preserve personality, prioritize selling power, make only 1–3 high-impact edits, and surface only hard factual uncertainties—not minor nitpicks.
- Use Fable subagents when you need more intelligence. Everyday sessions run on Opus; spawn a Fable subagent (Agent tool, model: fable) for the genuinely hard calls — deep strategy, the Lock, a gnarly build. Don't spawn one for routine work; each spawn starts cold and costs more than it saves.
- Start of session: `git pull` first (this is a two-machine setup — desktop and laptop — so the local copy may be behind), then check the most recent note in daily/ and open with what's still outstanding, instead of waiting to be told.
- End of session: log a short entry to today's daily note automatically — what got made, what's still open. This is separate from promotion (see below); it happens every session, promotion only happens when something's actually worth keeping.
- If asked about past work that isn't in memory or daily notes, search past session transcripts before saying you don't know.
- When a correction reveals a skill got something wrong, or the same manual move happens a second time, log it to skills/observations.md (task-observer) instead of letting it evaporate.

## Where my stuff lives (open when relevant)
Reference (feeds the work):
- Memory map: memory-map.md
- Concept notes: concepts/
- Voice rules: brand/voice.md
- Hook craft (8 vicious-hook principles): brand/hooks.md
- Swipes to model, by mechanism: swipes/
- What worked and why: winners/
- What died and why: losers/
- Repeatable plays: workflows/
- A specific client's context and rules: clients/{name}/client.md (one folder per client: primers/, strategy-map.md, seeds/, briefs/, winning-ads.md)
- JV partner deals (separate from core Flexxable work): jv/JV-map.md
- Human-readable skill guide: skills/Skills.md

Production (what I make):
- Written work (hooks, headlines, long-form): copy/
- Visual work (statics, video): creatives/

Flow:
- Unsorted drop zone: inbox/
- Daily notes: daily/
- Finished or retired work: archive/
- The Studio (live pixel-map dashboard of the pipeline, read-only): double-click "Open The Studio.command", or ask Claude to start the studio (.studio/, port 4173)

What to promote into memory vs ignore: the-data-dictionary.md (read it; it is the rule for what compounds).
When creating a durable note, include a short `Related:` line with useful Obsidian links, for example `Related: [[Promotion]] [[Workbench vs Memory]]`.
The real Claude Code skill instructions live in `.claude/skills/`. Obsidian hides dot folders, so use `skills/Skills.md` when you want to see the skill map.

## Rules that bite
- Short punchy paragraphs. One idea per line. Each sentence earns its own line. If it reads like an essay, rewrite it.
- No corporate or agency language. Ban: "leverage," "solution," "deliverable," "onboarding." Write like Dan is texting a mate who happens to be a business owner. Casual, direct, Australian-inflected.
- Never open copy with student proof or testimonials. And don't default to pain-first either — pain is white noise now. Lead with curiosity, novelty, a promise, or a world-level hook; use pain as the AMPLIFIER once you've earned attention. Proof comes after trust. (Ask me and I'll tell you when I want pain-led variations for a specific ad.)
- Never write in blocks of text. Wall of text = instant delete.
- Never invent a client result, number, or quote. If it is not in the client file, ask me.
- If you are unsure what good looks like, ask for an example before guessing.
- SAVE work into copy/ or creatives/. PROMOTE the lesson (why it won or died) into winners/, losers/, brand/, or workflows/. Two moves, not one. Never delete from archive/.
- At the end of a session, ask me what is worth promoting into memory and where it goes. That is how the workspace compounds.
