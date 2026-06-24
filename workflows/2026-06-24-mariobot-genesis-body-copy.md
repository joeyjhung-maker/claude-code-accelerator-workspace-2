# Workflow: Write body copy with MarioBot (Genesis)

The writing route for client body copy when hand-drafts feel flat. MarioBot (a trained Genesis bot, Opus-backed) writes in the client's voice — but only off what you prime it with. It beat Claude's freehand drafts this session.

Related: [[Promotion]] [[flexxable-offer-doc-ROYA]] [[creative-strategy-system]]

## When to use this
Any client body copy where the hand-written version isn't landing, or you want fast on-voice variants. Hooks first (lock the hook), then bring it here for the body.

## Key idea: the bot is client-agnostic — prime it per client
MarioBot is STATELESS. It remembers nothing between runs. It writes in whatever voice you prime it with on that call. So it works for ANY client — you just swap the two priming inputs. Never assume it "knows" a client.

## The steps
1. **Build the prime (per client).** Best = that client's WINNING ADS (a real body primer). If they don't have a swipe of winners yet, use their offer doc + voice/emphasis fingerprint as the stand-in (that's what we did for Flexxable — no body primer existed, so the ROYA offer doc played the role of "winning ad"). Each client should grow their own body primer in `knowledge/primers/` over time.
2. **Build the instruction (the brief).** This client's offer, avatar, mechanism, the selected hook (body MUST start from it), proof (verbatim numbers — never invent), CTA/destination, format rules, word count.
3. **Run the 2-step Genesis protocol** (stateless — replay full history each call):
   - Prime: send the prime payload → bot replies "I've absorbed the patterns."
   - Instruct: send `[prime] → [confirmation] → [instruction]` → it writes.
   - Runner: `/tmp/run_mario.py` (reads prime files + `/tmp/mario_instruction.md`; just repoint the file paths for a new client). Key: `clients/.env` (GENESIS_API_KEY + ANTHROPIC_API_KEY). Endpoint `https://gas.copycoders.ai/api/v1`, model `mariobot`, `stream:true` required.
   - Gotcha: Python urllib needs an unverified SSL context (`ssl.CERT_NONE`) or it throws CERTIFICATE_VERIFY_FAILED — curl works fine without it.
4. **Check.** Numbers verbatim against the offer doc/brief; voice-fingerprint tells present; bold skim-path sells alone; banned words absent.

## What good looks like
copy/2026-06-24-flexxable-hulk-student-rollcall-fb-ads.md — 3 roll-call→Hulk ads at ~200w, on-voice, that Dan then amended lightly rather than rewrote.
