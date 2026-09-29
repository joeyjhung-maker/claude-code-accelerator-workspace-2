# Skill Observations

Running backlog of corrections and repeated patterns worth turning into a skill change. Logged by task-observer, actioned via /save-as-skill (new skills) or /upskill (existing-skill fixes).

Status key: OPEN = not yet actioned | ACTIONED (YYYY-MM-DD) — what changed | DECLINED (YYYY-MM-DD) — why

Related: [[Promotion]] [[Memory Loop]]

---

### Observation 1: Global npm installs need sudo on this machine — prefer npx

**Status:** OPEN
**Date:** 2026-08-13
**Skill:** Cross-cutting (hit during the CLI update, then again in defuddle)
**Issue:** `/usr/local/lib/node_modules` is root-owned, so any `npm install -g` fails with EACCES and needs a sudo password Claude can't supply. This came up twice in one day: updating the Claude Code CLI, then installing defuddle. Each time it cost a detour before landing on the workaround.
**Suggested fix:** Default to `npx --yes <tool>` for any Node CLI rather than a global install. Only escalate to `sudo npm install -g` (run by Joey in his own terminal) when a tool genuinely can't run via npx. Worth a line in the Script if it bites a third time.

---

### Observation 2: `copy_lint.py` reports a false clean on any file using `---` as a section break

**Status:** OPEN
**Date:** 2026-08-13
**Skill:** `scripts/copy_lint.py` (used by /produce and every judge pass)
**Issue:** `body_lines()` splits the file on `\n---\n` and lints only `parts[1]` — it assumes `---` means frontmatter delimiters. A 9-section long-form ad that uses `---` as its section breaks therefore linted as **"1 FAIL, 0 FLAG"** when the real count was 65 FAIL / 2 FLAG. The gate passed silently on a draft it should have stopped. Only caught it because the number looked implausibly good against a draft that had failed 72 times ten minutes earlier.
**Suggested fix:** Treat `---` as frontmatter only when it appears in the first few lines of the file (or only when the file OPENS with `---`). Otherwise lint the whole body. Until it's fixed, any long-form/multi-section draft has to be linted with the breaks stripped: `sed 's/^---$/SECTIONBREAK/'`.

---

### Observation 3: `copy_lint.py` and the copy-rubric pass both missed long run-on sentences — only caught on Joey's read

**Status:** OPEN
**Date:** 2026-08-28
**Skill:** `scripts/copy_lint.py` + `rubrics/copy-rubric.md` (used by /produce and every judge pass)
**Issue:** Produced 7 Most-Aware static-ad copy pieces, ran `copy_lint.py` on all of them, all came back clean (0 FAIL / 0 FLAG or trivial flags only). Joey then flagged one on read: "sentences are too long" — e.g. "The book itself is the full blueprint for landing performance-based AI clients who pay you 30-50% of the revenue you generate, with no upfront cost to them." (26 words, 3 clauses, one period). `copy_lint.py`'s "two+ full sentences on one line" rule only fires when a line has multiple SENTENCES (multiple end-stops) — a single long compound/run-on sentence with one final period passes clean no matter how many clauses it stacks with commas, "and," or "who." The copy-rubric's taste pass (graded before this went to Joey) didn't catch it either — nothing in either gate explicitly checks clause-count or word-count per sentence against the Script's house rule ("Short punchy paragraphs. One idea per line. Each sentence earns its own line.").
**Suggested fix:** Add a mechanical check to `copy_lint.py` — flag any line/sentence over ~15-18 words or containing 2+ comma-joined independent clauses, since that's almost always "one idea per line" being violated even when it's grammatically one sentence. Until fixed, the judge pass needs an explicit manual step: read each sentence and ask "is this one idea?" — not just check for multiple sentences per line.
**Also noted:** the same production run showed `copy_lint.py` scanning a saved copy-file's ANNOTATION PROSE (the write-up above the `## Hook` section) as if it were ad copy, because that prose sits between the frontmatter `---` and the first section `---` — same root cause as Observation 2. Fix: lint only the isolated `## Body` section content, not the whole markdown file, until Observation 2 is fixed upstream.

---

### Observation 4: `copy_lint.py` throws a false FAIL on abbreviations like "Inc." — the opposite failure mode from Observations 2/3

**Status:** OPEN
**Date:** 2026-09-05
**Skill:** `scripts/copy_lint.py` (used by /produce and every judge pass)
**Issue:** The "two+ full sentences on one line" check splits on `(?<=[.!?])\s+` — any period followed by whitespace counts as a sentence end. On the BotBuilders JV email rewrites, this fired on genuinely single sentences that happen to contain an abbreviation: "They just hit #710 on the Inc. 5000 list of America's fastest-growing private companies in America." reads as two sentences to the regex because "Inc." ends in a period. Hit this twice in one session (Email 1 and Email 4 of the same JV sequence) — both had to be manually verified as false positives rather than rewritten.
**Suggested fix:** Add a short abbreviation exception list to the split regex (Inc., vs., etc., Mr., Mrs., Dr., U.S., a.m., p.m.) so a period immediately after one of these doesn't count as a sentence boundary. Until fixed, any FAIL on a line containing an abbreviation needs a by-eye check before rewriting it — don't trust the count blindly.

---

### Observation 5: `faith-thread` drafted only from the Second Brain wiki note, not the raw source it summarises — Joey called the posts flat

**Status:** ACTIONED (2026-09-05) — SKILL.md step 2 rewritten to require reading the raw source before drafting
**Date:** 2026-09-05
**Skill:** `faith-thread`
**Issue:** Ran `/faith-thread Biblical Meditation`, drafted 5 options straight from `Second Brain/wiki/biblical-meditation.md`. Joey rejected all of them: "you are writing posts from these summarised notes and they miss all the nuance and depth of the full raw sources." Checked the wiki note's own `sources:` frontmatter and read the raw files it was built from (`Prophet School - Session 12 - August 26.md` + two YT transcript notes) — they contain the actual vivid, quotable, specific language (the front-door/kitchen demonstration, the magnifying-glass image, "Pentecostalism is loud: it's a cover-up for disconnection," "a man who starved to death locked inside a supermarket") that the wiki note had compressed into flat one-line paraphrases ("Confidence in prayer is developed through proximity" with none of the surrounding contrast that makes it land). The wiki is a *good* index — it's just not the thing to draft the actual post text from.
**Fix applied:** `faith-thread/SKILL.md` step 2 now splits into (a) use the wiki note to confirm the topic exists and find its cross-references, then (b) look up that note's `sources:` frontmatter, locate the matching file(s) under `Second Brain/raw-sources/`, and read those in full — draft the actual post language from the raw source's specific quotes, images, and demonstrations, not from the wiki's paraphrase.

---

### Observation 6: `faith-thread` defaulted to `structure-bank.md` devices instead of the account's real voice — rejected a third time, plus a same-day reading-level rule reversed

**Status:** ACTIONED (2026-09-05) — SKILL.md step 3 now leads with the personal-processing register; the grade-2 reading-level lock from earlier the same day was reversed
**Date:** 2026-09-05
**Skill:** `faith-thread`
**Issue:** Even after fixing Observation 5 (raw source over wiki paraphrase), Joey rejected the redraft too: "its the way you are writing and explaining the concepts." He pointed at his real Google Sheets archive. Reading the actual 190-post archive (not `structure-bank.md`'s mined evidence, not `threads-voice.md`'s summary of it) showed the real gap: most real posts are first-person realisation/processing ("The more I pray, the more I realise this...", "I used to pray for God to change my situation. Sometimes he did. But then...", "Something that took me far too long to learn:") — not the named rhetorical devices (Definition Flip, Cleared Suspect, Counter-Intuitive Method) the skill was defaulting to for every draft. Those devices are real and evidenced, but they're a mined slice of high-rate outliers, not the baseline voice. `threads-voice.md` already listed the real recurring openers ("The more I…", "I used to…", "Something I…") but the skill never drew on them — it went straight to `structure-bank.md` every time.

**Compounding finding, same session:** a `~grade 2` reading-level rule had just been locked (from one narrow example) earlier the same day. Checking it against the real archive showed actual posts run grade 2.3–14.3, averaging ~5-6 — the grade-2 rule was a one-example overgeneralization that would have kept pulling drafts away from the real voice. Reversed before it did more damage. General lesson for both: **a rule locked from a single example, or a summary file (wiki note, structure-bank, voice-file summary) built from a mined/curated slice, needs checking against the full raw underlying data before being trusted as "the pattern"** — this is the same root issue as Observation 5, recurring at a different layer (voice register and reading level, not source material).

**Fix applied:** `faith-thread/SKILL.md` step 3 restructured to try the personal-processing register (pulling from `threads-voice.md`'s recurring-openers list, shaped around the raw source content) first, and treat `structure-bank.md` devices as a secondary option only when a note's content is a clean paradox/list/distinction. `threads-voice.md` gained a "Default voice register" section with the real quoted examples and a testimony-line caveat (generic "I used to…" framing is fine; an invented specific dated event is not). The grade-2 reading-level rule was reversed to no fixed target.

---

### Observation 7: `faith-thread` fix from Observation 6 overcorrected — 3 of 5 drafts used the same "realisation" opener shape under different structure-bank names

**Status:** ACTIONED (2026-09-05) — SKILL.md step 3 now requires variety across three families, capped at one personal-processing post per batch
**Date:** 2026-09-05
**Skill:** `faith-thread`
**Issue:** Observation 6's fix told the skill to default to the personal-processing register. Applied literally, that meant labelling three different drafts as three different structure-bank devices while all three actually opened with the same shape ("The more I…", "I used to…", "Something I…" — all realisation-openers). Joey: "options 1,2,3 are too similar in that they ALL start with a realisation. We only need 1 option for this." The fix for Observation 6 was correct about the register existing, but didn't say anything about capping how often it's used per batch — "vary the shape" was in the instructions but wasn't specific enough to catch three structurally-identical openers hiding under different names.

Joey then supplied 4 more real posts from his own archive, unprompted, as models for structures the skill didn't have at all: a "problem illumination" post (name a felt problem, reframe it as training, explain why, 8.43% eng), a "never/don't" warning post (permission clause + urgency + scripture citation + casual aside, 8.85% eng, 13 reposts), a "you know you've truly X when Y" diagnostic with two branching outcomes (**14.53% eng — the highest confirmed rate in the account so far**), and a Bible-story typology post (Moses' staff, 7.58% eng). None of these were in `structure-bank.md` despite being real, evidenced, high-performing posts from his own archive — the mining pass that built the bank simply missed them.

**Fix applied:** Added these four as structures #20-23 in `structure-bank.md` (Part 1, evidenced from Joey's own archive with real engagement numbers). `faith-thread/SKILL.md` step 3 rewritten around three families — personal-processing (Family A, capped at one per batch), Joey's newly-mined structures #20-23 (Family B, first-class not fallback), and the original mined devices (Family C, used only when content calls for one) — with an explicit instruction to vary across families, not just across named structures within one family.

---

### Observation 8: The old Skool judge optimized technical cleanliness and flattened Mariobot's selling voice

**Status:** ACTIONED (2026-09-08) — added a Dan-specific light judge and removed the legacy style-contract/lint gate from the Dan Skool route
**Date:** 2026-09-08
**Skill:** `produce-skool` + `scripts/run_mario.py`
**Issue:** Joey repeatedly found that raw general-model copy and his own edits sold harder than the output from the full Mariobot production setup. The bottleneck was not missing notes. The generation prompt was over-constrained by a legacy style contract, then the judge optimized for compliance, lint cleanliness, and a visible scorecard. This selected against the cheeky lines, concrete micro-scenes, uneven rhythm, and purposeful roughness that make Dan's copy feel human. The process was protecting rules instead of protecting the sale.
**Fix applied:** Added `rubrics/dan-skool-chatgpt-rubric.md`, added `run_mario.py --no-style-contract`, and rewrote both copies of `produce-skool` so truth and the brief remain hard gates while the style judge makes only one to three high-impact edits. Mechanical lint and the old copy rubric are no longer automatic gates for Dan Skool drafts.

---

### Observation 9: The light judge preserved voice but missed the emotional bridge

**Status:** ACTIONED (2026-09-08) — added the resistance-then-disarm check to the Dan Skool judge
**Date:** 2026-09-08
**Skill:** `produce-skool`
**Issue:** The mobile-follow-up draft correctly explained that calling is more powerful than email or LinkedIn, but it stopped at rational advice. Joey's edit named why readers avoid the call (“need some cojones”) and immediately made it feel safer by explaining that the gift has already opened the door. He also restored a functional headline and Dan sign-off despite requesting an informal FYI note.
**Fix applied:** The Dan judge now checks whether practical advice names the reader's emotional resistance and disarms it with the mechanism. It also no longer interprets “informal FYI” as an automatic instruction to remove the headline and sign-off.

---

### Observation 10: Product teases need a transferable principle, not a use-case tour

**Status:** ACTIONED (2026-09-08) — added a philosophy-first product-tease pattern to the Dan judge
**Date:** 2026-09-08
**Skill:** `produce-skool`
**Issue:** The LinkedIn-first draft explained lumpy-mail and non-lumpy-mail paths separately, which made the second half feel like a feature/use-case tour. Joey collapsed both into one philosophy (“warm up leads before the pitch”), a two-step method readers can use now, and a tease that the upcoming tool automates Step 1. He also replaced an implied performance claim with “My hunch,” keeping the anticipation without pretending the lift is proven.
**Fix applied:** The judge now prefers principle → steps → immediate manual action → automated-step tease, and requires confident uncertainty for unproven expected outcomes.

---

### Observation 11: Swipe adaptation copied the label but missed the section's argumentative function

**Status:** ACTIONED (2026-09-08) — added an argument-function check to the Dan judge
**Date:** 2026-09-08
**Skill:** `produce-skool`
**Issue:** In the fishing swipe adaptation, `WHERE` was mapped literally to niche and Dream 100 targeting. Travis's original section actually uses `WHERE` to pain-dig the crowded alternatives, discredit their fees and platform control, and position a different channel as the better fishing hole. The adapted nouns were relevant, but the persuasion sequence had disappeared.
**Fix applied:** The Dan judge now requires swipe adaptations to map the rhetorical job of every section—pain, enemy, contrast, proof, or payoff—before translating surface labels into the client's market.

---

### Observation 12: The Dan light judge missed clipped negation contrasts that read as AI slop

**Status:** OPEN
**Date:** 2026-09-11
**Skill:** `produce-skool`
**Issue:** A shortened Skool draft passed the light judge with several adjacent contrast fragments: a claim followed by “Not because…,” “Not the most technically impressive… / The thing that…,” and “One X. Not a Y.” Joey flagged the clusters as obvious AI-slop tells. The judge currently protects purposeful fragments but does not distinguish human roughness from templated negation/reversal beats, especially when several appear in one post.
**Suggested fix:** Add a repetition-level check to the Dan judge: scan for clustered `Not X / Y`, `X. Not Y.`, and `Not because / But because` constructions. Preserve a single earned contrast if it sounds natural, but cut or rewrite repeated instances before showing the draft.

---

### Observation 13: Video-analysis skills have no caption fallback when Gemini is unavailable

**Status:** OPEN
**Date:** 2026-09-14
**Skill:** `ad-creative-analysis` + `facebook-transcriber`
**Issue:** Both skills depend on `GEMINI_API_KEY`. When the key was missing even after loading the normal shell config, the documented path stopped despite the Instagram reel having clean burned-in captions that could recover the full script. The workaround was manual: download the reel, sample it at 2 fps, crop the caption band, tile the frames by time, and reconstruct the incremental captions.
**Suggested fix:** Add a documented no-key fallback for captioned videos: use ffmpeg to sample and crop the subtitle band into timed contact sheets, then reconstruct the transcript from the incremental captions. Check for the key before attempting the Gemini route so the fallback starts immediately.

---

### Observation 14: Genesis streaming helpers can fail without producing a usable artifact

**Status:** OPEN
**Date:** 2026-09-14
**Skill:** `genesis-bots`
**Issue:** The bundled Node streaming helper exited successfully without invoking its CLI entry point, leaving no output. The Python fallback printed its model/provider preflight but then left a zero-byte destination file without a completion or error message. A direct streaming request to the same Genesis endpoint succeeded and produced the full Message Isolator report, so the bot and credentials were healthy; the failure was in the helper path or its session handling.
**Suggested fix:** Normalize the Node entry-point paths before comparing `import.meta.url` with `process.argv[1]`, and make both helpers treat a missing/empty stream as a non-zero failure with a clear diagnostic. Add an end-to-end smoke test that asserts the destination file contains content before reporting success.

---

### Observation 15: `produce-skool` started writing before source gathering was closed

**Status:** OPEN
**Date:** 2026-09-20
**Skill:** `produce-skool` + `brief-skool`
**Issue:** A request to “go through” an initial resource bundle and pull notes/key points also mentioned the eventual post. The workflow treated that as permission to lock a brief and produce immediately, but Joey was still feeding a much larger product-update source set and explicitly did not want copy yet. This created a premature draft based on an incomplete, pre-release picture.
**Suggested fix:** Add a research-close gate before briefing or producing from a user-supplied source bundle: if the user frames the current action as gathering/pulling notes, stay in research mode and ask or wait for an explicit “that's everything / now write” signal before creating copy, even when the eventual deliverable has already been named.

---

### Observation 16: Product-release copy described the lifecycle instead of dramatizing the new delta

**Status:** OPEN
**Date:** 2026-09-20
**Skill:** `produce-skool`
**Issue:** The Wingman 2.0 release draft used a generic prospect → demo → setup → optimisation sequence. Joey flagged that the same broad lifecycle had already been used when Wingman first launched, so it did not make Version 2.0 feel new. The copy was accurate but failed the release's real job: make the reader feel the product has materially changed.
**Suggested fix:** Add a product-release check to the Dan judge: compare the proposed explanation with prior launch positioning and replace generic category/lifecycle language with one concrete new capability chain that could not have been written about the old version. For Wingman 2.0, a proof → pre-launch validation → post-launch improvement sequence (The Wall → Gauntlet → A/B testing) communicates the delta without becoming a feature list.

---

### Observation 17: Proof posts can over-narrate the testimonial instead of extracting the commercial lesson

**Status:** OPEN
**Date:** 2026-09-20
**Skill:** `produce-skool`
**Issue:** The first Pierre proof-post draft spent too much space explaining that both Pierre and his client called the result small, reproducing both reactions and then interpreting their understatement. Joey asked for a completely different version with less narration. The screenshot already carries the voices; the post should add a useful strategic meaning rather than retell what the attached image says.
**Suggested fix:** Add a proof-post check to the Dan judge: when the testimonial screenshot is attached, quote only when a phrase carries the hook or mechanism. Otherwise extract one transferable commercial lesson from the verified result and let the image supply the play-by-play.

---

### Observation 18: Early-result proof posts should map the full commercial optionality

**Status:** OPEN
**Date:** 2026-09-20
**Skill:** `produce-skool`
**Issue:** The second Pierre draft improved on testimonial narration but reduced the value of a positive 100-lead test to immediate commission and reusable credibility. Joey pointed out that the result also creates confidence to scale the original campaign, access to the client's fresh leads, and a path to stack more Androids inside the same account. Focusing on only the next pitch made the opportunity feel much smaller than it is.
**Suggested fix:** Add an early-result check to the Dan judge: after a successful test, map every evidence-backed expansion path before choosing the post's argument—scale the same campaign, expand into fresh demand, add adjacent products inside the account, and reuse the proof in new-business conversations. The post need not list every path, but it should not accidentally collapse a land-and-expand result into testimonial value alone.

---

### Observation 19: Gated lead-magnet teasers must not publish the payload

**Status:** ACTIONED (2026-09-20) — added an information-gap check to the Dan Skool judge
**Date:** 2026-09-20
**Skill:** `produce-skool`
**Issue:** A teaser correctly established the cost of mailing the wrong prospect, then listed all five labels from the gated scorecard. Joey removed the list: the post had given away the very mechanism people were meant to comment to access. The old instruction to “preview enough to feel concrete” was too permissive for a compact checklist asset.
**Suggested fix:** For gated assets, teach the stakes and name the asset, but keep its framework steps, checklist labels, answers, and mechanism behind the gate. Tease the number or depth of the asset without making the teaser independently usable as a substitute.

---

### Observation 20: The Dan judge still confuses one-sentence-per-line with tiny sentences

**Status:** ACTIONED (2026-09-24) — added a final rhythm scan to the Dan Skool judge
**Date:** 2026-09-24
**Skill:** `produce-skool`
**Issue:** The bad-market mindset post passed through the judge with repeated runs of two-to-five-word lines even though the client voice notes already required varied sentence lengths. The judge made the raw Mariobot draft worse by splitting related ideas into isolated beats.
**Suggested fix:** After the mechanical one-sentence-per-line pass, flag any run of three or more sentences under roughly six words and combine related thoughts unless the run is a deliberate closing crescendo.

---

### Observation 21: Genesis helpers silently swallow streamed provider errors

**Status:** OPEN
**Date:** 2026-09-25
**Skill:** `genesis-bots`
**Issue:** `run_mario.py` received HTTP 200 and an initial empty assistant chunk, followed by a streamed provider-error event explaining that the Anthropic key was not workspace-scoped. The parser ignored the error event, exited zero and returned an empty draft, making a credential-scope problem look like Mariobot produced nothing.
**Suggested fix:** Parse SSE error objects explicitly, print the provider message, exit non-zero when no content is returned, and document that Genesis BYOK calls require a workspace-scoped Anthropic key unless the workspace ID header is supplied.

---

### Observation 22: Explicit bot names must override the default writer route

**Status:** OPEN
**Date:** 2026-09-25
**Skill:** `produce` + `genesis-bots`
**Issue:** A request for “marciobot” was automatically routed to Mariobot because `/produce` treats Mariobot as the mandatory default writer. Joey had explicitly named Marcio Narrative Ads Bot, so the near-identical bot names caused the wrong workflow to start.
**Suggested fix:** Before applying `/produce`'s default writer rule, check whether the user named a Genesis bot explicitly. Treat close bot-name spellings as distinct, verify the live slug, and route through `genesis-bots` when a non-Mariobot writer was requested.

---

### Observation 23: A full-draft bot route must not bypass the hook-first gate

**Status:** OPEN
**Date:** 2026-09-25
**Skill:** `produce` + `genesis-bots` + `creative-strategy-system`
**Issue:** Marcio’s full-ad pass was judged for factual accuracy and mechanical copy quality, but its opening reached Joey without a separate vicious-hook gate. “Ten clients gave me ten bosses” carried contrast but no sharp emotional pain in the first line, so it passed the broad scorecard while still failing the actual scroll-stop standard.
**Suggested fix:** Any bot that outputs a full ad must still be stopped at hooks first. Grade the opening independently for a first-line emotional wound, a charged word, a lived moment and the flinch test, then wait for hook selection before accepting or editing the body.

---

### Observation 24: Hook amplification must preserve the ad's POV and genre

**Status:** OPEN
**Date:** 2026-09-25
**Skill:** `produce` + `creative-strategy-system`
**Issue:** The vicious-hook pass improved pain but transformed a first-person chronological story about the narrator into ten second-person reader accusations. The hooks matched the offer argument while breaking the creative's narrative contract.
**Suggested fix:** Add POV and genre to the hook gate before intensity grading. A story ad stays in the narrator's established pronouns and causal sequence; amplification can sharpen the opening but cannot turn it into advice, diagnosis, accusation or a different ad format.

---

### Observation 25: Dan Skool drafts can hide removable filler inside contrast beats

**Status:** OPEN
**Date:** 2026-09-26
**Skill:** `produce-skool`
**Issue:** A ROYA draft inserted a canned “not because X… but because Y” explanation followed by tiny reaction lines (“So ya just… don't. Fair enough.”). Joey deleted the entire section without weakening the argument. The passage created artificial rhythm and performed empathy without adding a fact, belief, desire or necessary transition.
**Suggested fix:** Add a deletion pass to the Dan judge: test every multi-line contrast beat by removing it. If the logic and desire still land, cut it. Scrutinise “not X, but Y” constructions especially when X is a negative label the reader never raised and the next lines are disposable fragments. Keep ROYA's broader plain-language tendency observational until more Joey-written samples establish a real room-specific pattern.

---

### Observation 26: Campaign workflows reduce CAP to a finished-copy checklist

**Status:** OPEN
**Date:** 2026-09-28
**Skill:** `storm` + `brief` + `produce` and Skool variants
**Issue:** The workspace treated Child/Adult/Parent mainly as three checks inside one finished piece, and misrouted proof toward Adult. Joey clarified that CAP also governs campaign sequencing: Child outcome/dopamine first, Adult mechanism/process second, Parent proof/objections last; a short T1 may intentionally be pure Child.
**Suggested fix:** Add a CAP-position field or campaign-stage check to ideation and briefing workflows. Judge a piece against its intended CAP job rather than requiring every asset to contain all three, while retaining Child → Adult → Parent as the default sequence for full pieces and campaigns.

---

### Observation 27: Winner variations drifted off the winner's core concept

**Status:** OPEN
**Date:** 2026-09-28
**Skill:** `produce` + `creative-strategy-system` (variation / iteration path)
**Issue:** The 2026-09-25 Marcio variation of the Hedge Fund winner produced 10 hooks, 9 of which dropped the "copied the hedge fund managers' model" concept and ran on the one-vs-ten payoff instead. Joey rejected all of them: a variation that loses the winner's concept isn't a variation. Message Isolator later showed that line is the ad's ONLY carrier of the mechanism, so it is FROZEN twice over.
**Suggested fix:** Before varying any winner, run Genesis `message-isolator` first and treat its FROZEN column as a hard constraint on every downstream writer (Cash Rewriter, Segment/Mech Swapper, Marcio, mariobot). Change one lever at a time (`cash-analysisvariation-bot` → `cash-rewriter-bot`); never let a hook pass re-pick the concept.
