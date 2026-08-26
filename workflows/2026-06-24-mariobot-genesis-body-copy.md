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
   - Runner: `scripts/run_mario.py --primer <primer.md> --instruction <brief.md>` (durable, in-repo — the old `/tmp` runner kept getting wiped, and each session rebuilt the prime from memory, which is how thin primes happened). It auto-prepends `rubrics/mariobot-style-contract.md` to the instruction so the WRITER sees the hard rules, not just the judge. Key: `clients/.env` (GENESIS_API_KEY + ANTHROPIC_API_KEY). Endpoint `https://gas.copycoders.ai/api/v1`, model `mariobot`, `stream:true` required, BOTH headers (`Authorization: Bearer` + `X-Provider-Key`). `--dry-run` prints the exact payloads.
   - Gotcha: Python urllib needs an unverified SSL context (`ssl.CERT_NONE`) or it throws CERTIFICATE_VERIFY_FAILED — curl works fine without it. (The runner handles this.)
   - Primers live in `clients/flexxable-primers/` (e.g. `iaa-jv-body.md` for IAA-book ads to JV lists). Never re-type a prime by hand.
4. **Check — two layers, in order.**
   - **Linter first:** `python3 scripts/copy_lint.py <draft.md>` — mechanical STRUCTURE rules (multi-sentence lines, fragment stacks, "No X. No Y.", banned words, signposts, dashes). Every FAIL gets rewritten before the judge pass. (Added 2026-07-06 after a judge-by-feel pass waved through 12 mechanical fails.)
   - **Judge pass second:** grade the taste rules from `rubrics/copy-rubric.md` as an explicit PASS/FAIL scorecard per rule — not a prose summary. Numbers verbatim against the offer doc/brief AND proof TYPE matched to the claim; voice-fingerprint tells present; additive framing when it's a JV list; only a clean pass reaches Joey.

5. **On a REVISION turn, re-run the whole judge pass. It does not inherit the last turn's fixes.** (Added 2026-08-13.) When you send a second `--turn` asking the bot to revise its own draft, it re-writes from its own turn-1 output — not from the corrected version you edited by hand after the judge pass. So every fix that lived only in your edit gets silently reverted. On the long-form IAA swipe, turn 2 re-broke five rules turn 1 had already been cleaned of: the treadmill metaphor Joey killed weeks earlier, a "No X. No Y." fragment stack, "167 pages", the Chesky quote, and US "skeptical" for British "sceptical". Two ways to handle it, use both: put the already-fixed items into the revision brief as explicit "keep it this way" lines, and re-run linter + full scorecard on the new turn as if it were a fresh draft. Never diff-only.

6. **A strict structural swipe ("match line for line, don't deviate") needs explicit per-line word
   caps in the brief, or the bot drifts long.** (Added 2026-08-26.) Asking mariobot to swipe a
   winning ad's exact structure without a length constraint reliably produces expanded lines — extra
   clauses, added explanation, sometimes whole new beats. Happened twice on the same session: a
   short banner-ad swipe first (top banner went from 6 words to 12+), then a long-form 14-line swipe
   (every line 2-4x longer than source). Both times, adding an explicit word-count cap per line/block
   in the instruction — matched to the source's actual word count — fixed it on the next pass. State
   the cap as a number, not "keep it short."

## What good looks like
copy/2026-06-24-flexxable-hulk-student-rollcall-fb-ads.md — 3 roll-call→Hulk ads at ~200w, on-voice, that Dan then amended lightly rather than rewrote.
