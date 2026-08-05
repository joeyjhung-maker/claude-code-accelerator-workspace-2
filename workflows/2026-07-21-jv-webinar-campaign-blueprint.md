# JV Webinar Campaign — reusable blueprint (v0.1, WORKING DRAFT)

*The repeatable shape of a JV webinar launch (our side: we host the expert to a partner's list). Built from the first full run — Bill McIntosh × Buildy × Dan/Flexxable, Jul 2026. **Status: work in progress.** It ran, it worked, but it's not battle-tested across partners yet. Refine after every run; once it's run cleanly 2–3 times, it graduates from draft to locked play.*

Related: [[partner-voice-template]] [[2026-07-21-clarity-first-webinar-reorder-wrong-for-warm-jv]] [[hooks]] [[copy-rubric]] [[always-use-mariobot-to-write]]

---

## 0. Intake — gather these BEFORE writing anything
- **Partner's voice sample** (their own emails/videos) → drives [[partner-voice-template]] rule #3.
- **Partner's audience:** who they are + their ONE unanswered pain = the BRIDGE. (Buildy: they can build AI but can't get paid → "the money's in the offer, not the build.")
- **The offer + price/stack** being sold on the webinar (or mark TBD — but the close can't finish without it).
- **Approved proof** — verified numbers/names only. Pick a **hero number** for the title + hooks (Buildy run: $222,600 commission from a $1.03M campaign — "not too big, not too small, feels doable").
- **Dates:** webinar day + the send calendar (pins the "tomorrow/tonight/Tuesday" references).
- **Two decisions up front:**
  1. **Mechanism: hide or reveal?** Default here = hide on Day 1–2 reg emails (curiosity), reveal ON the webinar.
  2. **Structure: curiosity-led or clarity-first?** Warm/owned/JV list run by experienced webinar operators → curiosity-led, defer to their playbook. Cold paid traffic → clarity-first can help. See [[2026-07-21-clarity-first-webinar-reorder-wrong-for-warm-jv]].

## 1. The webinar deck skeleton
1. **Title slide** — number-led hero (big pool → the cut, e.g. "$1.03M in sales… and Dan Banked $222,600 as a Pure Commission Split") + subtitle = the process promise + presenters + date.
2. **Partner intro (~3 slides)** — meet the audience where they are → name the gap → introduce + vouch the expert with the hero number → tease the two things they'll learn → "here's [expert]."
3. **Expert cold-open** — disarm the skeptic (anti-hype, "I was in your shoes"), then plain-ish setup.
4. **The business case** — why the opportunity exists + why it's UNCONTESTED (the "same pie" logic: everyone fights over new leads; nobody wants the old). This was the missing piece on the first run — don't skip it.
5. **Mechanism + the pitch** — reveal the how + the risk-free offer ("we don't get paid unless you do").
6. **Proof** — a wall of relatable wins + the big number.
7. **The offer suite / stack.**
8. **The close** — Travis's "2 roads" (old grind vs risk-free path) → milestone roadmap (land the meeting → demo → easy-yes offer → get paid → they ask for more) → "ready to get started?" → early-bird → [offer stack + price] → join CTA → Q&A ("I'll stay on as long as humanly possible").

## 2. The 8-email registration sequence (each email's JOB)
*All in Partner Voice, mechanism hidden Day 1–2, short graded SLs.*
- **Day 1 · E1 — Reframe.** The old-model pain (chasing clients, upfront fees, fulfillment hell) → the new way (partner, get paid on results, AI does delivery). Reveal the expert only AFTER the argument.
- **Day 1 · E2 — Curiosity gap.** Open ONE loop the webinar closes (e.g. "the one reason these deals close on the spot"). Short, same-day 2nd send.
- **Day 2 · E3 — Expert origin / belief.** The expert's story, told to land the bridge to THIS audience (build vs get-paid). Story-led open.
- **Day 2 · E4 — Proof wall.** Relatable "people like you" wins. Hook-first, not proof-first (house rule); strip any mechanism from the testimonials.
- **Day 2 · E5 — Tomorrow push.** Outcome recap + hammer "we go live tomorrow." <200 words.
- **Day 3 · E6 — 6hr (fuller).** Open "we go live TODAY," recap what they'll walk away with, tease the open loops, push LIVE-over-replay.
- **Day 3 · E7 — 1hr (short).** One-line reminder + urgency.
- **Day 3 · E8 — 10min (short).** Pure "we're starting, come in."

## 3. Production pipeline (every asset)
Brief → **mariobot** writes ([[always-use-mariobot-to-write]]) → `copy_lint.py` (mechanical) → judge against [[copy-rubric]] (taste) → save to `copy/`. Subject lines: grade against [[hooks]] at partner intensity, **≤8 words** default.

## 4. Exemplars from run #1 (copy these)
- Emails: `copy/2026-07-21-flexxable-buildy-jv-webinar-reg-day*` (all 8).
- Close slides: `copy/2026-07-21-flexxable-buildy-webinar-CLOSE-slides-MARIOBOT.md`.
- Voice + subject-line craft: [[partner-voice-template]], [[hooks]].

## 5. Refine log (update after each partner run)
- **2026-07-21 — Buildy (run #1):** first full run. Worked. Open questions that slowed it: the offer/price for the close wasn't locked (close left with [TBD] placeholders); structure debate (curiosity vs clarity) cost a detour — now pre-decided in §0. Partner Voice + ≤8-word SLs were the standout wins. Next run: lock the offer BEFORE building the close; confirm dates before writing Day 3.
- **2026-08-05 — Matt Leitz/BotBuilders (run #2):** confirms the blueprint compresses for a lighter/earlier-stage partner — 2 reg emails + a 3-email same-day "Webby Live" sequence + 2-day close, not the full 8-email run, and it still works. Sharpened the §0 "hide or reveal" default: when asked to punch up copy for curiosity, the concrete move is stripping fully-worked mechanism detail (the worked dollar math, the step-by-step "how") and replacing it with named-but-unexplained teases — name "2 and 20" without the worked example, name "a system" without the SMS/CRM specifics, reference "a single question" without stating it. Reveal stays exclusively for the live event, including in urgency/reminder emails.
