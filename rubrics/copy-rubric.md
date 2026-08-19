# Copy Rubric — the Judge's scorecard

*This is the grading half of the two-brain trick (Standards Ladder, Day 2). The writer (mariobot) drafts the floor. This rubric is what a sharper editor model grades the draft against BEFORE I ever read it. Fails get rewritten, not shown.*

**Status: SEED.** These rules are lifted from Mario's MarioJudge living log and email-engine standards as a starting scaffold. They are good DR fundamentals, but they are HIS taste, not yet mine. Amend, delete, and add as my own reactions come in. Every time I say "no, like THIS," bank it here and date it.

Scope: hooks, body copy, headlines.
Related: [[voice]] [[Promotion]] [[winners]] [[losers]]

---

## How to grade
For each draft, score every rule below as PASS / FAIL.
Any FAIL → rewrite that line and re-grade. Only a clean pass reaches me.
When in doubt on a taste call (not a mechanical one), flag it for me rather than guessing.

**The judge's output is a rule-by-rule PASS/FAIL scorecard — never a prose summary.** A narrative "judge pass" ("fixed a dash, kept the good bits") waved 12 mechanical fails through on 2026-07-06. Run `scripts/copy_lint.py` on the draft FIRST (it catches the mechanical STRUCTURE rules), rewrite every FAIL, then grade the taste rules as an explicit tick-list. If the scorecard isn't shown, the grading didn't happen. (Banked 2026-07-06)

**Provenance rule (applies to everything below).** Grade and auto-fix AI-WRITTEN copy hard. But anything *I* wrote, do not "correct" — at most FLAG it and let me decide. My lines are my call. The judge polices the machine's output, not mine.

---

## STRUCTURE (mechanical — these are pass/fail, candidates for a linter later)

- **One sentence per line.** Shatter the paragraph. Never cluster two on a line. A wall of grey makes the eye quit before it reads a word. **Exception: headlines.** A headline stays one flowing line even when long — don't break it across lines. (2026-06-10)
- **No walls of text.** Short punchy paragraphs. One idea per line. If it reads like an essay, it failed.
- **Break up the triplets.** Doublet is the default. A survivor earns its own line. Three items stacked on one line is a strong AI tell — kill it.
- **Flow can beat staccato — don't chop one thought into period-fragments.** "One sentence per line" bans stacking two *sentences* on a line. It does NOT mean manufacture choppy fragments. When it's a single thought, a flowing line with a connector reads more human than the clipped version. Prefer "Every gap and every crack where the leads slip through" over "Every gap. Every crack where the leads slip through." Prefer "From slow follow-ups to cold leads gathering dust…" over three clipped fragments. Fake-choppy is an AI tell as loud as the wall of text. (Banked 2026-07-02)
- **Don't manufacture fragment-lists for rhythm — commas and flow beat a stack of clipped fragments.** When several beats belong to ONE thought, join them into a flowing line with commas; don't split them into separate period-fragments for cadence. Joey killed six of these in the "build a life, not a cage" email and rewrote each with commas: "Coffee. Quiet house. Maybe 20 minutes of work." → "Coffee, a quiet house, and maybe 20 minutes of actual work." "Some days I use it. Some days I don't." → "Some days I use it, some days I don't." "Lachie came from finance. Zero tech experience. Zero business experience." → "Lachie came from finance with zero tech experience and zero biz skills behind him." Even the brand slogan took commas: "ONE offer, ONE client at a time, ONE person." This is the general form of the flow-over-staccato rule: a comma'd sentence reads human; a stack of fragments reads like a machine performing punch. (Banked 2026-07-06)
- **No filler "fake-punchy" fragments.** A short/one-word line must EARN its place by doing a job — new info, a turn, a concrete image, soft proof. If it only exists for rhythm, cut it or replace it with one that works. Joey deleted "Cool.", "Not in theory.", and "Same business. Same screen." on sight — rhythmic padding that admires itself and moves nothing. Punch comes from the line doing work, not from adding full stops. (Banked 2026-07-02)
- **Even a kept short line should read like natural speech, not a clipped telegram.** Clipping to bare words is NOT punch. Joey turned my "Tedious… but doable." into "It's tedious… but totally doable." Same beat, but spoken-natural beats stripped-down. When you keep a short concession/turn, write it the way Dan would actually say it out loud. (Banked 2026-07-02)
- **Ellipsis is for trailing between beats, not glue inside one clause.** Don't drop a "…" in the middle of a single tight phrase. Joey killed the ellipsis in "close convos too early… or miss the ones it should've closed" → "…too early or miss the ones…". Reserve "…" for a line that genuinely trails off into the next. (Banked 2026-07-02)
- **Dashes are provenance-based, not character-based.** If AI wrote a dash (any kind), remove it. If *I* wrote a dash, leave it alone — never tell me to remove my own. Don't flag my dashes. (Amended 2026-06-10)

## VOICE / REGISTER

- **Street-smart is the register.** Grade for "real," not "articulate." Casual, direct, British-inflected. Like Dan texting a mate who happens to be a business owner.
- **Don't neuter the profanity.** It is texture, not vulgarity. Never scrub it clean.
- **No corporate / agency language.** Banned: leverage, solution, deliverable, onboarding. (From the Script.)
- **Kill the canned signpost.** No "and here's the magic," no "but here's the thing." Let the line land on its own — when AI wrote it. For signposts *I* wrote (e.g. "In short:"), FLAG it and let me decide — sometimes I keep it, sometimes I replace. Don't auto-fix my lines. (Amended 2026-06-10)
- **Sounds like AI bullshit? Cut it.** If I would never write it, it fails — no matter how smooth it reads.
- **PARTNER VOICE — when writing FROM a JV partner to THEIR list, write in the partner's voice, not the client's.** For JV sends (e.g. Bill McIntosh promoting Dan/Flexxable to the Buildy list), the sender is a trusted host vouching for a friend in THIRD person ("my friend Dan," "Dan's story"). Grade for: (1) ZERO client-insider jargon — the partner's audience doesn't know Sleeping Beauty Android, Prince Charming, Offer of the Century, Coffee Dates, Profit Partner, Androids, DBR; translate to plain language (sales meetings, deals, the system, take a cut); (2) the partner's OWN register, not the client's tics — Bill is warm/neutral, NOT Dan's "peeps/mate/bloke" British-Aussie slang; (3) understated, not hypey — curiosity from specificity + paradox, never volume/"secret"/"game-changer"; (4) personal endorsement used genuinely ("it's rare I put my name on something"); (5) a bridge to the partner's specific audience pain (Buildy: can build with AI, can't get paid → "the money's in the offer, not the build"). Full guide: [[partner-voice-template]]. (Banked 2026-07-21 — Joey flagged the Bill emails as the right partner tone and asked to make it reusable.)
- **Kill the manufactured cadence — flowing sentences over neat parallelism.** AI fakes voice with three tells: the clipped three-beat fragment close ("You deliver the leads. You get paid. Job done."), the tidy antithesis / two-part flip ("They're not worthless. They're just untouched." / "not X, it's Y"), and the "Not because X… it's Y" reassurance stitch. All three read as clever-machine, not a person talking. Real people — and especially a given sender like Ryan — write flowing, conversational sentences. Keep the MEANING (e.g. respecting that they're good at their job) but say it the way they'd actually say it, folded into a normal sentence, not a balanced reversal. Match the sender's real register from their past emails, not a punchy-copywriter default. (Banked 2026-07-03 — Joey flagged three of these in a mariobot email-3 draft that had drifted into a staccato Ryan doesn't use.)

## CLARITY

- **No vague pronouns.** Name the actual noun, every single time. Hunt every it / this / that. Keep a pronoun only when its antecedent is in the same breath and unmistakable.
- **Never leave the WHY vague.** Cash every claim out into a concrete reader payoff. Tell them WHY they get it / why it matters.
- **Serve the reader, not yourself.** Every line is for THEM. A line that admires its own cleverness is dead weight, no matter how good it sounds. When a line performs MY wit, swap it for what the reader actually GETS.

## PERSUASION

- **Show it, don't summarize it.** Don't name a quality and expect the reader to buy it. Stage the evidence and let them land on the conclusion themselves. Replace every abstract summary with the symptom shown.
- **NEVER write a stacked abstract triplet. Hard rule, zero exceptions.** Three abstractions in a row — "More certainty. Higher close rates. You're the pro in the room." — is a dead AI tell and an automatic FAIL. Don't write it in the first place. If three benefits want to stack: show ONE as a concrete scene, or cut to one line. (Hardened to a NEVER 2026-06-30 at Joey's instruction.)
- **A benefit needs its WHY in the same breath.** Don't state a recommendation or feature and move on — attach the reason it pays off for the reader, right there. "Tells you which to PITCH" is weak alone; "which to PITCH… because they'll have the HIGHEST chance of closing" lands. (Banked 2026-06-30)
- **Convert flat negatives into a felt fear.** "No more guessing. No more pitching a bot they don't need" is a generic absence. Make it second-person and name the sting: "you'll never look like an ass pitching a bot they don't need." Stakes the reader can FEEL beat the neutral benefit. (Banked 2026-06-30)
- **Prefer the direct-address question over the instruction.** When setting up a tactic, don't command ("Now picture this on a Loom… You walk them through…"). Pull the yes with a question + a hunch: "Here's my HUNCH… what do ya think would happen if you shot a Loom with this? I bet you'd blow their socks off." Engages instead of lecturing. (Banked 2026-06-30 — matches the voice doc's "direct-address questions pull the yes.")
- **Name the blue ocean when the tactic is novel.** If nobody else is doing the move, say so — "No one is doing this… you've just shown them the keys to the kingdom." The first-mover edge is part of the sell. (Banked 2026-06-30)
- **Anchor a new feature to the product it actually lives in — as its OWN beat, not crammed mid-sentence.** Name its home, but give the placement its own clean line, ideally near the CTA as the bridge into "click the link." Joey pulled "we built the 'Campaign Analyser' inside the Hulk" apart into "we built the 'Campaign Analyser'." + a standalone "The Campaign Analyser is in The Hulk now." right before the CTA. The Pain Signal Auditor lives inside **Sales Wingman**; the Campaign Analyser lives inside **the Hulk** (live-campaign optimisation). Get the placement right AND give it room. (Banked 2026-06-30, refined 2026-07-02)
- **Show the tangible artifact, not just the action.** Name the concrete thing the reader GETS, not only what the tool "does." Joey added "Spits out a huge report breaking down every component." "It analyses your convos" is abstract; "spits out a huge report" is a deliverable they can picture holding. Give the mechanism an output they can see. (Banked 2026-07-02)
- **Land on the ambition, not just the metric.** Close the benefit stack on the reader's bigger-picture ceiling — scale, bigger clients, killing the fear — not only the immediate number. Joey added "take on big clients and launch without worrying if your campaigns will bomb… scale up faster and easier than ever before" AFTER "more commission." Elevate from the feature-benefit to the dream before the CTA. (Banked 2026-07-02)
- **At the problem→solution pivot, flip to the ASPIRATION with concrete numbers — don't restate the pain.** At the turn from problem to fix, don't linger on a negative re-statement of the problem ("that churn caps your agency… you're stuck on a treadmill"). Pivot on the positive ceiling, with a specific number ladder. Joey replaced my treadmill line with "Protecting against this churn is what will allow you to scale to 20k, 40k, 60k+ months." The dream-with-numbers ($20k/$40k/$60k months) pulls harder than the trapped metaphor. (Banked 2026-07-03, Ryan email 3.)
- **For a JV partner's audience, never dunk on their existing model.** When selling into a partner's list (e.g. Ryan's PPL / lead-gen operators), the offer is an ADDITION that makes their core business STRONGER — never a replacement that implies their model is broken. Kill "escape the grind," "your ads suck," "stop doing X." Frame every line as "on top of what you already do," and SHOW the synergy — the new thing makes their existing service convert better (the Androids work the leads their lead gen already generates). The partner's audience is the partner's livelihood; insulting it insults them. This is the sharper, general form of the "name the complement" note. (Banked 2026-07-03 — Joey killed a squeeze rewrite that opened "stop living and dying by ad spend… that treadmill gets OLD fast.")
- **Get the MECHANISM mechanically right — don't hand-wave HOW it works.** A vague "how" is worse than no how. "The Androids are demoing LIVE on the map" was fuzzy and not quite true; the real move is "the Hulk builds all the androids in one click, so you demo each one LIVE on the coffee date, one after the other." Name the actual product action that produces the benefit. If you're unsure how the mechanism works, ASK — never paper over it with a smooth-sounding vague line. (Banked 2026-07-02)
- **Even a throwaway/transition line must do work.** Don't drop a flat filler reaction ("Cool.") to bridge two beats. Make the bridge carry something — soft social proof, momentum, a turn. "A bunch of you loved it!" bridges AND banks light proof. A line that only fills space is a delete. (Banked 2026-07-02)
- **Make mind movies.** A replacement for a "telling" line isn't enough if it's flat — it has to be VISUALLY strong, so the reader pictures the scene playing out. Paint the concrete moment (the face lighting up, the penny dropping), not just a literal restatement. (2026-06-10)
- **Replace, never just delete.** When a flagged line fails, don't leave a hole — swap in something that keeps the line's JOB. A cut superlative still needs a reason in its place. (2026-06-10)
- **Calibrated hedges.** A naked superlative reads as hype and the guard goes up. A small hedge on the biggest claims ("probably," "considered a top 0.1%") makes them believable. The voice still runs at a 10 — only the claim gets the hedge.
- **Lead with the human, not the machine/mechanism.** The mechanism is body proof, never the hook. (Matches Script: never open with student proof or testimonials.)
- **Don't default to a pain-first hook. Pain is the amplifier, not the opener.** AI defaults every hook to pain ("I used to crush mornings, now I'm just surviving them") and it's become white noise Meta dislikes too. Lead with curiosity, novelty, a weird tangible thing, a promise, or an identity challenge — then use pain AFTER you've earned attention and want to twist the knife. A hook that opens on suffering is a FAIL unless Joey asked for a pain-led variation on this specific ad. When he does, grade the pain version on its own merits. (Lesson 11, banked 2026-07-10.)
- **Never invent a result, number, or quote.** If it's not in the client file, FAIL and ask. (Hard rule from the Script.)
- **Rob Brown → "Rob" only. Never use his surname in copy.** Locked rule. Every other named proof (Scott, Jack, Michael, Lachie, etc.) keeps first name only anyway — Rob Brown was the one outlier still carrying a surname. Fix on sight in any draft. (Banked 2026-07-09.)
- **Proof TYPE must match the claim.** A real number attached to the wrong kind of claim still FAILS. A "6-figure commission checks" hook can't be backed by Rob Brown's $341,042 *profit* or Jack's $15,000 *install fee* — it needs a commission number ($222,600 commission, Scott's $27k deal, Katarrey's $4,250). Right numbers, wrong proof type = Joey has to fix it by hand. Match the category, not just the magnitude. (Banked 2026-07-06 — the no-ad-spend WINNER edit.)
- **Check live dates against the calendar.** Any "Wednesday, Sept 17th"-style date: verify the weekday actually matches the date. Flag mismatches and placeholders (`Xpm`, `EST` in summer = EDT). Numbers must also stay consistent across pieces in the same campaign. (Banked 2026-06-10 — caught a Wed/Thu error on the Hulk Reveal email.)

### Substance gates (from the 37 Rapid-Fire tips, banked 2026-07-10)
*Three fast pass/fail tests. Run them on the HOOK first, then the lead. A fail here isn't a line to polish — it's a line that says nothing yet.*

- **The Product Swap Test.** Could this hook sell a different product? If a mattress, a coffee, a supplement, and an app could all run your exact line, it's not specific enough — FAIL. "I used to crush mornings, now I'm just surviving them" fits fifty products. Find the angle only THIS product can own. (Lesson 2 / 36.)
- **The Step-Back Bullshit Detector.** Strip the adjectives and dramatic wrapping, say the bare claim out loud. If the bare idea is a platitude the reader already believes ("you are what you eat," "your body can heal itself," "there's a gene") — FAIL, no matter how good the language sounds. The writing can't rescue an idea that isn't worth writing about. Test: interrupt someone at dinner and say ONLY the bare claim. If they'd say "yeah, I know" or "so what?", it's dead. (Lesson 2.)
- **One curiosity thread, not three.** One open loop the reader has to close — not three competing ones. Three threads dilute; the reader can't hold them and picks none. Pick the single most magnetic question and starve the rest. (Lesson 7.)

### Hook intensity — too polite is a FAIL (Lesson 1 + 22, banked 2026-07-10)
*The hook's job is to stop the scroll against the reader's will. Discomfort is the signal you're at the right level — not cleverness, not beauty.*

- **The flinch test.** Read the hook aloud. If it doesn't make you (or a non-marketer) visibly react — wince, laugh, say "damn" — it's too tame. FAIL. Most people write 3–4 levels too polite and dial back way too early. "Your shower water contains chemicals" is flat; "most people's shower water is so toxic it'd kill a goldfish" is the level.
- **Escalate first, dial back second — never the reverse.** Find the version that makes YOU uncomfortable (life-or-death, social stakes, identity confrontation), THEN decide how far to pull back for compliance. You can't find the ceiling by starting at the floor.
- **Compliance is a spectrum, not a wall.** Aim for a 7/10 aggression. Write 1–2 points ABOVE the comfort line and let it get pulled back — writing at a 4 when a 5 is fine is killing yourself for nothing. This is a judge-flag, not an auto-cut: flag the risk level, don't neuter on sight.
- **Third-person the scary claim.** Don't point the knife straight at the reader ("YOUR liver is shutting down"). Let them observe it: "most guys have no idea their liver is 18 months from shutting down." Same fear, no feeling of being attacked, softer compliance profile.
- **Empathy, not accusation, on the tender stuff.** She FEELS like a burden — she doesn't say she IS one. The small shift turns an attack into empathy. (The softener move.)

**Vicious-hook checklist — grade every hook against the 8 principles ([[hooks]]).** Full craft in `brand/hooks.md`; these are the pass/fail gates:
- **Relevance in the first line.** Something relevant to the reader in the first 10–20 words (pain/condition call-out, belief call-out, or general intrigue). If line 1 is throat-clearing, FAIL.
- **Protect the charged word.** The detonating word IS the hook — "sexless" not "unfulfilling," "killing" not "hurting," "panties" not "pajamas." If a softer/clinical synonym crept in, FAIL and restore the charged word.
- **Caveman / Germanic language.** Short, blunt, five-year-old-simple. Fabrics→cloth, excessive→too much, insomnia→sleeplessness, perspire→sweat. Latinate/clinical word where a Germanic one exists = FAIL.
- **Consequence before mechanism.** Lead with the wound, not the scalpel. A hook that opens on HOW it works ("silver releases ions…", "this spikes cortisol") before WHY they should care = FAIL — flip it, mechanism is body copy.
- **Reads like information, not an ad.** Story, news, confession, or promised insight — the payoff is catharsis/intrigue/insight, never a pitch. If it reads like an ad, dead on arrival.
- **Push to the edge of reality.** Comfortable and plausible = not on the edge. The best hooks make the reader think "there's no way…" and then need to find out. (Banked 2026-07-10, Lesson: vicious hooks.)

---

## HULK CAMPAIGN — locked CTA model (2026-06-30)
*Every Hulk email closes on this exact shape. Grade the CTA against it.*

1. `Click the link below…`
2. `Then send over the word "KEYWORD" to our FB Messenger` — theme-matched to the email's CORE PROMISE, which can be the OUTCOME, not just the feature name. Feature-themed ("AUDIT", "MAP") or outcome-themed ("SCALE") both work; pick whichever the email is really selling. Joey swapped "ANALYSE" → "SCALE" once the email built to a scale-up ambition. (Refined 2026-07-02)
3. `==> [benefit-framed line]` — SHORT and pain/outcome-framed, sits RIGHT AFTER the keyword. NOT a feature recap. Joey cut "See exactly where your prospects are bleeding revenue… and watch the Androids plug every gap LIVE" down to "Sell to their PAIN the easy way." Keep the ==> line a crisp promise, not a description of the tool. (Tightened 2026-07-02)
4. The soft what-happens-next → routes to joining ROYA: "We'll have a quick chat, then get ya the deets to join us inside ROYA…"
5. A fresh, specific proof in parens at the very end: `(Erik just signed a $10k TRIAL project)` — provenance: Joey's own, never flag or verify.
6. `-Dan`

## THE LIVING LOG — banked, dated, permanent
*Every entry = the raw reaction I had once, then the rule it hardened into. Add here as we go. I never give the same note twice.*

| Date | I reacted | Banked as a rule |
|---|---|---|
| 2026-06-10 | (seeded from Mario's PDF — rules above) | Starting scaffold, to be amended to my voice |
| 2026-06-10 | "I still want the headline in one long sentence" | Headlines stay one flowing line, even when long. Shortening into beats is fine; breaking across lines is not. |
| 2026-06-10 | "Small dash is my style, compare - vs – . Long dash no." | Short hyphen `-` allowed. Only long em/en dashes `— –` banned. |
| 2026-06-10 | "We don't just delete it, we replace it with something that fits" | When cutting a flagged line, swap in a replacement that keeps its job. Never leave a hole. |
| 2026-06-10 | "Create mind movies so people can picture what's going on" | Show = paint a vivid visual scene the reader can SEE, not a flat literal restatement. |
| 2026-06-10 | "For the dash — I can do it, you cannot. If AI wrote it remove it. If I wrote it, don't tell me to remove it." | Dashes are provenance-based: kill AI dashes, leave mine. |
| 2026-06-10 | "In short: flag it if I've done it. Sometimes I keep, sometimes I replace. Tell me and I decide." | Don't auto-fix MY lines. Flag and let me choose. The judge polices the machine's output, not mine. |
| 2026-06-30 | Deleted "More certainty. Higher close rates. You're the pro in the room." | Kill the stacked abstract benefit-list — show one as a scene or cut it. |
| 2026-06-30 | Added "because they'll have the HIGHEST chance of closing" to the PITCH line | A benefit needs its WHY in the same breath. |
| 2026-06-30 | "No more pitching a bot they don't need" → "you'll never look like an ass pitching a bot they don't need" | Convert flat negatives into a second-person felt fear. |
| 2026-06-30 | Rewrote the declarative Loom block as "Here's my HUNCH… what do ya think would happen if…? I bet you'd blow their socks off" | Prefer the direct-address question + hunch over the instruction. |
| 2026-06-30 | Added "No one is doing this… keys to the kingdom" | Name the blue ocean when the tactic is novel. |
| 2026-06-30 | Added "available now inside Sales Wingman" + reordered the CTA, proof in parens | Anchor a feature to its real product home; lock the Hulk CTA model (see above). |
| 2026-07-02 | Deleted "Cool.", "Not in theory.", "Same business. Same screen." | No filler fake-punchy fragments — a short line must do a job or die. |
| 2026-07-02 | Rejoined my chopped fragments into "Every gap and every crack…" / "From slow follow-ups to cold leads…" | Flow beats staccato; don't shatter one thought into period-fragments. |
| 2026-07-02 | "Cool." → "A bunch of you loved it!" | Even a transition line must carry something (soft proof / momentum). |
| 2026-07-02 | "Androids demoing LIVE on the map" → "the Hulk builds them in one click, so you demo each one LIVE on the coffee date" | Get the mechanism mechanically right; don't hand-wave the HOW. |
| 2026-07-02 | Long ==> recap → "Sell to their PAIN the easy way" | The ==> CTA line is a short pain/outcome promise, not a feature recap. |
| 2026-07-02 | "Tedious… but doable." → "It's tedious… but totally doable." | Kept short lines should read spoken-natural, not clipped to bare words. |
| 2026-07-02 | Killed the ellipsis in "too early… or miss…" → "too early or miss…" | Ellipsis trails between beats; don't glue it inside one clause. |
| 2026-07-02 | Pulled "inside the Hulk" out of the build line into a standalone "The Campaign Analyser is in The Hulk now." before the CTA | Anchor the feature's home as its own beat near the CTA, not mid-sentence. |
| 2026-07-02 | Added "Spits out a huge report breaking down every component." | Show the tangible artifact the reader gets, not just the action. |
| 2026-07-02 | Added "take on big clients… scale up faster… without worrying if campaigns bomb" | Land on the ambition/ceiling, not just the immediate metric. |
| 2026-07-02 | Keyword "ANALYSE" → "SCALE" | CTA keyword themes to the core promise (outcome ok), not always the feature name. |
| 2026-07-02 | Cut "Right, I'm just gonna say it" before the excitement claim | Cut filler preamble — open straight on the claim, not a run-up to it. |
| 2026-07-02 | Added "I've made a 10,000x ROI at LEAST" from Dan's old system, before revealing the new AI one (JV/Ryan campaign) | A quantified personal result from the messenger, used to set up "imagine what's possible now" escalation, beats a vague comparison ("makes the old stuff look like X"). Note the hedge — "AT LEAST" — was already attached in the same breath. |
| 2026-07-02 | Cut "makes everything we were doing back then look like finger painting" for "takes it to the next level" (JV/Ryan campaign) | Plain over clever — even a vivid metaphor gets cut if a direct line says the same thing straighter. |
| 2026-07-02 | Cut "Just paid it. Done." for "...without batting an eyelid" folded into the main sentence (JV/Ryan campaign) | Don't tack a short fragment pair onto the end of a sentence for punch — fold the payoff into one flowing sentence with an idiom instead. |
| 2026-07-02 | Added "(or continue scaling no ad spend AI campaigns if you prefer)" next to the PPL-conversion tease (JV/Ryan campaign) | When teasing a new revenue mechanism to an audience with an existing model, name the optional/flexible path explicitly — reinforces complement, not replace. |
| 2026-07-02 | Split "grinding for every new lead" and "clients throwing money at them" into two lines with an ellipsis at the pivot (JV/Ryan campaign) | For a strong before/after contrast, break it into two lines with an ellipsis cliffhanger at the turn, not one flowing sentence straight through. |
| 2026-07-02 | Replaced the "it's not X, it's Y" problem restatement with "By the end of this training you will know how to…" (JV/Ryan campaign) | For webinar-registration copy specifically, cash the pain out into a concrete promise of what the reader walks away KNOWING, not another restatement of the problem. |
| 2026-07-02 | Added "===> Yes Ryan! I want to learn how to run No Ad Spend Campaigns" as the CTA (JV/Ryan campaign) | Webinar-registration CTAs get an explicit I-statement button line — same benefit-framed-CTA principle as the locked Hulk CTA model above, adapted for registration instead of FB-messenger-keyword. |
| 2026-07-02 | Added "DATE/TIME: Thursday, July 9th 3pm EST / 8pm UK" directly under the CTA (JV/Ryan campaign) | Repeat the critical event logistics right where the reader is about to click, not just earlier in the body. |
| 2026-07-03 | Killed a JV squeeze rewrite that opened "stop living and dying by ad spend / that treadmill gets OLD fast" | For a JV partner's audience, never dunk on their existing model — frame the offer as an ADDITION that makes their core biz stronger, and show the synergy. |
| 2026-07-03 | Flagged "You get paid. Job done." / "not worthless, just untouched" / "Not because you're doing anything wrong…" in a reg email | Kill manufactured AI cadence (3-beat fragment closes, tidy antithesis flips, "not because X" stitches). Write flowing conversational sentences that match the sender's real register. |
| 2026-07-03 | Replaced my "churn caps your agency… stuck on a treadmill" with "Protecting against this churn is what will allow you to scale to 20k, 40k, 60k+ months" | At the problem→solution pivot, flip to the aspirational ceiling with a concrete number ladder — don't restate the pain negatively. |
| 2026-07-03 | "They stay, they're happy, and they buy more." → "And when they're happy, they stay, and they buy more!" | Convert a flat trait-list into a CAUSAL line (when X → Y). Cause-and-effect reads more human than a comma-list. |
| 2026-07-03 | "And you earn a cut of every extra sale…" → "This is a SUPER smart way to earn a cut…" | Editorialize the tactic in the sender's voice (their enthusiasm / opinion), not a flat feature statement. |
| 2026-07-03 | `"The lead quality isn't good enough"` → `"…" they say.` | Attribute a quoted objection/complaint ("they say") so it lands as a real thing people say, not a floating quote. |
| 2026-07-03 | CTA "Yes Ryan! I want to learn…" → "Make your clients more STICKY while earning more" (+ an "if you want X… you need to come along" bridge) | The CTA button can be an outcome promise matched to THIS email's angle, not always the generic campaign I-statement. Precede it with an "if you want [outcome], you need to [act]" benefit bridge. |
| 2026-07-06 | Killed six fragment-lists in the "build a life, not a cage" email → rewrote each with commas ("Coffee. Quiet house. Maybe 20 minutes." → "Coffee, a quiet house, and maybe 20 minutes of actual work.") | Don't manufacture fragment-lists for rhythm — join beats of one thought with commas and let it flow. General form of the flow-over-staccato rule. |
| 2026-07-06 | Swapped Rob Brown's profit + Jack's install fee out of the "6-figure commission checks" ad for the $222,600 commission, Scott $27k, Katarrey $4,250 | Proof TYPE must match the claim — a commission hook needs commission proof, not profit or fee numbers. |
| 2026-07-06 | A prose "judge pass" signed off two mariobot drafts that `copy_lint.py` then failed 21 times between them | The judge outputs a rule-by-rule PASS/FAIL scorecard, never a narrative. Linter first (mechanical rules), scorecard second (taste rules). |
| 2026-07-09 | "Rob Brown made $341,042…" → "Rob made $341,042…" | Never use Rob Brown's surname in copy — first name only, matching every other named proof point. |
| 2026-07-10 | `copy_lint.py` failed a fine spoken hook (question + answer) and a headline during a /produce run | The linter's STRUCTURE rules are BODY-scoped. Hooks and headlines are single units — a Q+A hook or a short headline is not a "two sentences on a line" / "fragment stack" fail. Treat a lint FAIL on a hook/headline as a flag to eyeball, not an auto-rewrite. (Fix later: teach copy_lint line-type context so it stops crying wolf on hooks/headlines.) |
| 2026-07-10 | mariobot wrote the IAA business as "AI-powered lead generation… it finds them new leads" | **Mechanism check:** IAA is OLD/dead-lead REACTIVATION over SMS → new sales, not new-lead generation. Grade every Flexxable draft's mechanism against this. See [[iaa-mechanism-old-leads]]. |
| 2026-07-10 | Hooks claimed "my company replaced my team with AI" / "I failed IT in school, now I make more than my desk job" — untrue for Dan | **Dan-truth check:** first-person claims must be true to Dan (no redundancy/desk-job/failed-IT backstory). Reframe escape-9-5 / not-technical angles as second-person. See [[dan-truth-constraint]]. |
| 2026-07-10 | Mined the 37 Rapid-Fire A-lister tips for judge gates | Added three substance gates above: Product Swap Test, Step-Back Bullshit Detector, One curiosity thread. Run on the hook before the taste rules — they catch a hook that says nothing before we polish the way it says it. |
| 2026-07-21 | "Really liking how these Bill emails are coming out… very nice tone for partner emails as they don't have Dan's full lingo" | **PARTNER VOICE** — for JV partner sends, write in the partner's voice (third-person vouch, zero client jargon, partner's own register, understated). Banked as a rubric rule (VOICE section) + reusable guide [[partner-voice-template]]. |
| 2026-07-21 | Joey inserted a SECOND pain layer ("he still had to run the ads… one bad day wiping out a month's profit") after the first fix, before AI resolves it | **Don't resolve the arc too early — stack a second layer of tension before the solution.** When a story fixes the problem too fast, the payoff is weak. Add the remaining problem after the first fix, then let the real answer land. Full breakdown: [[2026-07-21-partner-voice-jv-emails]]. |
| 2026-07-21 | Joey changed "more than TEN retainer clients" → "3 retainer clients" | **Dial numbers DOWN for believability.** A smaller, credible multiple beats an impressive-but-suspicious one — even when the bigger number is technically supported. Overclaiming raises the guard. |
| 2026-07-21 | "Why are you writing like this: It's not another tool. / It's not another course. / It's not 'just hustle harder.'" | **Lint-fix must FLOW, not CHOP.** When `copy_lint.py` flags "two sentences on one line," the fix is NOT to reflexively split each onto its own line — that manufactures the exact staccato fragment-stack the rubric bans. If splitting creates clipped fragments, JOIN with commas / restructure into one breathing line instead. (Recurring miss this session — the mechanical split was creating AI-tell cadence in the emails.) |

<!-- Next time a draft makes me wince, add a row:
| YYYY-MM-DD | "the thing I said once" | the permanent rule |
-->

---

## DAN — SKOOL COMMUNITY POSTS (added 2026-08-19)

*Built by diffing my draft against Joey's rewrite of the B2B Gifts sales-call post. This is a
DIFFERENT register from ad copy. Dan in his own room is looser, warmer and more spoken than Dan in
a Meta ad. Grade Skool posts against this section, not the ad rules above, wherever the two clash.*

### Register
- **Dan is AUSSIE, not British.** Correcting the standing "British-inflected" note — that's the
  residue of him living in the UK. His background is Australian and he says so in copy
  ("Maybe it's because of my Aussie background?"). Aussie casual, not London casual.
- **Spoken contractions are mandatory.** ya, 'em, gonna. "To show ya…" not "To show you." "Nobody
  has ever done this to 'em" not "to them."
- **Conversational filler earns its place here.** "You know…" on its own line is a spoken beat, not
  padding. The no-filler-fragments rule from the ad section does NOT apply to Dan's spoken asides.
- **Double exclamation marks on the punchline.** "you will be disappointed!!" "I was never really
  good at it!" One "!" is flat for him.
- **CAPS for emphasis, roughly one word every few lines.** CLOSE, EASY, SIMPLE, WAY, WITHOUT,
  LITERALLY, ONE. Not shouting — vocal stress written down.
- **Scare quotes signal irony and distance.** "pitch", "persuasion", "me". Dan uses them to hold a
  word at arm's length. Keep them.
- **Sign off with his name.** Dan.

### Structure
- **THE ELLIPSIS LADDER IS A DAN DEVICE — exempt from the fragment-stack FAIL.** I joined three
  beats into one comma'd flowing line per the flow-over-staccato rule. Joey split them back out:
  > It happens when they open the box…
  > When they read the letter…
  > And when they realise nobody has ever done this to 'em before.
  Three lines, each trailing on "…", building to an "And". This is spoken cadence, not manufactured
  staccato. **Test to tell them apart:** if the beats trail INTO each other and a person would pause
  between them out loud, it's a ladder — keep it. If they're clipped full stops performing punch
  ("Two people chatting. One of them agrees. Done."), it's still a FAIL. The ellipsis is the tell.
- **Ellipsis is Dan's main connector — it replaces commas AND full stops.** The ad rule ("ellipsis
  only for trailing between beats, never glue inside a clause") is relaxed for him. He even runs
  ellipsis-separated lists: "media buying… copywriting… POS systems… insurance… SaaS…"
- **P.S. is a structural element, not an afterthought.** Dan uses it to widen the market after the
  main post has done its job. Expect one.

### Persuasion
- **Lead with a weakness before the flex.** The strongest thing Joey added was Dan admitting he was
  never good at closing, and pinning it on his Aussie discomfort with hard selling — then handing
  the reader an out: "maybe you can relate." Confession first, proof second. A Dan post that only
  flexes is missing its best beat.
- **ASK FOR THE SPECIFIC PROOF. Don't write around the gap.** My draft had zero numbers because I
  had no facts, and I wrote elegantly around the hole. Joey dropped in *"We've closed 5 adventure
  park clients now"* and it carries the whole post. **New standing rule: when a post needs proof I
  don't have, stop and ask for the number and the niche before drafting, rather than producing a
  version that works without them.** The vague version is not a safe default, it's a weak one.
- **The engagement ask should SEGMENT, not just ask.** My CTA was one flat question. Joey's splits
  the room and makes them self-identify:
  > Where are ya at…
  > Do ya crush sales already…
  > Or does this get you excited… now that you will be able to land clients WITHOUT having to do much selling?
  That's the handraiser mechanic from [[naps-nurture-and-picks]] — it sorts the list while it
  engages. Default to a two-camp question on any Skool post meant to drive comments.

### Positioning
- **"Don't make it about X" → NAME X and DEMOTE it. Don't scrub it.** Dan's brief said be careful
  not to make this an "AI Automation" B2B group. I scrubbed every mention. Joey named it in the P.S.
  and reduced it to one item on a list: *"AI Automation is just ONE example. You could sell media
  buying… copywriting… pitch your startup idea to investors… POS systems… insurance… SaaS…"*
  **Scrubbing leaves the reader's existing assumption intact. Demoting actually corrects it.** This
  is the better read of a "don't position it as X" instruction and it generalises beyond this post.
- **Widen the market at the end, never at the top.** The post earns attention on one concrete story
  (adventure parks), then the P.S. tells everyone else it applies to them too.

Related: [[dan-truth-constraint]] [[naps-nurture-and-picks]] [[b2b-gifts-project]]

### Dan Skool posts — round 2 corrections (2026-08-19, same post)

- **SHOW THE CHANGE BEFORE YOU NAME IT. This was my biggest miss on the whole piece.** Both my draft
  and mariobot's went straight from the mechanism ("I started sending lumpy mail") to the conclusion
  ("the close is the EASY bit"). Nothing in between. Joey inserted the evidence:
  > Because these leads weren't ANYTHING like what I was used to.
  > They were HAPPY we got in touch with 'em.
  > They were EXCITED to get on a call.
  Only THEN does the close-is-easy line land. **A mechanism claim needs the felt difference dramatised
  between the cause and the payoff.** Without it the reader is asked to take the conclusion on trust.
  Ask on every draft: have I shown WHAT CHANGED, or have I only asserted that something did?
- **Two beats, not three.** That block is a doublet (HAPPY / EXCITED). Dan's anaphora runs in pairs.
  A third would have tipped it into the stacked-triplet FAIL.
- **LEADING ellipsis is a Dan device too.** Not just trailing. A line that OPENS on "…" continues the
  previous breath: "…I realised something kinda embarrassing." / "…and when it came to the close…
  that was the EASY bit." Reads as one long spoken thought broken across lines.
- **Proof lands better as a consequence clause than as its own boast.** Joey changed my
  *"We've closed 5 adventure park clients now - you won't believe how SIMPLE it's been"* into
  *"Which has meant we've closed 5 adventure park clients now with many more in the pipeline."*
  Hanging the number off "which has meant" makes it the RESULT of the argument instead of a brag
  interrupting it. This also dissolves the never-open-with-proof tension — subordinated proof can sit
  anywhere.
- **Name what the asset proves in the handoff line.** "To show ya…" became "To show ya how easy it
  is…". Tell the reader what to watch FOR, not just that something is coming.
- **When causality runs backwards, restructure the thought — don't word-swap.** I offered to change
  "Then" to "So". Joey rebuilt the beat instead: *"So I'm THRILLED we figured out a way to make the
  close irrelevant. / It all started by sending lumpy mail…"* Outcome, then origin, both pointing
  forwards. Reach for the restructure before the connector swap.
- **A direct reader-bridge can be beaten by a scene.** I preserved "maybe you can relate" because the
  new opener had no invitation in it. Joey cut it and let the HAPPY/EXCITED block do that job instead.
  Showing the reader something recognisable pulls harder than asking them if they recognise it.
