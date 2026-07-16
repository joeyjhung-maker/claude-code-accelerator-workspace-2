---
name: hook-miner
description: "Use this skill ONLY when the user explicitly invokes it by name - phrases like 'Hook Miner,' 'run Hook Miner,' 'mine hooks,' 'mine the market and write me hooks,' or 'find 100 hooks in the market's own words.' Do NOT trigger on standalone Market Copy Miner requests (that produces a full messaging file, not hooks) or standalone Reel Hook Writer requests (that writes hooks from a script the user already provides). When invoked, the user gives an avatar and a core problem, no script required, and Hook Miner runs a condensed multi-pass web mining sweep pulling real market language, then plugs that mined language directly into the Reel Hook Writer's hook construction families to produce exactly 100 problem state hooks in the prospect's own voice. Every hook's fill-in language is mirrored from a real quote, never invented. The output is the 100 hooks, not a messaging file."
---

# Hook Miner

Two skills, one pipeline. Market Copy Miner finds the exact words the market uses. Reel Hook Writer has 11 proven hook construction families. Hook Miner mines first, then pours that mined language straight into the constructions. No script needed. No messaging file delivered. The output is 100 hooks that sound like the prospect's own inner monologue, read back to them.

## What this skill is (and isn't)

- **Borrows the mining method, skips the file.** Market Copy Miner's full workflow builds a 12-phase messaging file. Hook Miner runs a condensed version of that mining, just enough passes to fuel 100 hooks, and never delivers the file. It delivers hooks.
- **Borrows the hook constructions, drops the inventing.** Reel Hook Writer infers identity and problem from a script and writes hooks in its own crafted language. Hook Miner instead requires every fill-in — the problem, the failed solution, the mistake, the private struggle — to trace back to a real quote from the mining pass. The only Claude-authored part of any hook is the construction's frame ("why," "did you know," "here's why," and so on).
- **The deliverable is a flat numbered list of 100 hooks.** Not a messaging file, not a swipe file, not a script. If the user wants the underlying raw quotes too, they can ask — don't lead with them.

## Step 1: One question, then go

Ask exactly one question, nothing else:

*"Who is your avatar and what is the core problem your offer solves?"*

Do not ask about demographics, tone, platform, or offer details. Whatever they give you is enough. The mining reveals the rest.

**Alternate entry points:**
- **Pasted script instead of avatar/problem:** Pull the identity and the problem exactly the way Reel Hook Writer would, from the script's opening. Mine around that problem instead of asking the question.
- **Pasted quotes or an existing Market Copy Miner messaging file:** Skip the web mining pass entirely. Go straight to Step 3 and build the Market Voice Bank from what they gave you.
- **User names a specific product/competitor to research:** Fold that into the mining searches (reviews of that product belong in the Failed Solutions pass).

Once you have an avatar and a problem, say only *"On it."* and start mining.

## Step 2: The mining pass

**Non-negotiable search technique** (identical to Market Copy Miner): use plain natural-language queries, never `site:` or boolean `OR` — the tool ignores them. Search the way a person types: *"what does [problem] feel like personal stories,"* *"[problem] tried everything nothing works forum."* Search to FIND the page, then FETCH it to lift exact words. Never quote from a search snippet — paraphrased snippets break the Mirror Rule. Skip JS-shell pages that won't load (common on Quora).

**You are hunting for lingo, not just facts.** These are different things and mixing them up is the most common way this skill fails. Lingo is a phrase a real person actually said or typed — it sounds specific, a little raw, sometimes ungrammatical, and would look out of place in a corporate deck. Facts are true statements about the niche that show up in blog posts, "how to" articles, and industry reports — clean, correct, and generic. Both are useful for understanding the niche, but **only lingo can fuel a hook.** A hook built from a fact instead of lingo reads like every other post in the niche; a hook built from lingo reads like it was written by someone who's actually felt this.

The tell: industry blogs and "how to" articles are efficient sources for facts and stats, but they're written in analyst voice, not felt voice, so they tend to launder real pain into clean category terms — "client attrition," "delivery gap," "account health score," "burnout" — even when quoting someone. Confessional sources (forums, reviews, first-person blog posts written by someone describing their own experience, Reddit-style venting, comment sections) are where the actual lingo lives — "gut punch," "blindsided," "white-knuckling through the week," "the call came, and it was swift." When a pass turns up mostly facts and category terms, that pass isn't done — go back and search again with more confessional phrasing ("agency owner venting about losing a client," "what it actually feels like when," "I felt like such an idiot when") instead of conceptual phrasing ("reasons clients leave agencies").

Run these 7 passes. Each has a minimum pull — don't stop short, and don't pad with weak quotes to hit the number either.

| # | Pass | Minimum | Sample searches | What you're hunting |
|---|------|---------|-----------------|----------------------|
| 1 | Pain description | 10+ | "what does [problem] feel like personal stories," "[problem] forum describe how it feels" | Visceral, physical, or metaphorical descriptions of the problem itself |
| 2 | Failed solutions | 8+ | "[niche] tried everything nothing works," "[treatment] waste of money review" | Not just what they tried — how they talk about *why it failed*. That failure language is some of the richest problem material you'll find. See the callout below the table. |
| 3 | Common advice / villain | 6+ | "[niche] doctors don't take me seriously," "[niche] they just want your money" | The mainstream advice that fails them, and who/what they blame |
| 4 | Collateral damage | 8+ | "[niche] ruined my life lost my job," "[niche] I don't recognize myself" | What the problem destroyed beyond the symptom — relationships, identity, work |
| 5 | Private behavioral tells | 8+ | "[niche] what I do to cope," "[niche] I always carry," "how do you manage [niche] day to day" | Specific, hidden, repeated behaviors. Not "struggles with it" — "unbuttons their pants under the desk by 2pm." This pass feeds every Mirror hook in Step 4. Mine it hardest. |
| 6 | Skepticism | 6+ | "is [solution] a scam," "[niche] skeptical don't believe it works" | Exact disbelief language — "yeah right," "snake oil," "too good to be true" |
| 7 | Desired result | 6+ | "[niche] finally worked," "what it feels like when [problem] is gone" | How they describe the win, in their own words, not benefit-speak |

### Failed-solution language is the highest-value pass, and it needs a hard rule

The other 6 passes find people who *have* the problem. The Failed Solutions pass finds people who have the problem *and are already spending money and effort trying to solve it* — which means whatever they're describing is close kin to the very thing being sold. That's a meaningfully hotter, more specific kind of language than general pain description, for 2 reasons:

1. **It reveals fresh problem language you won't get any other way.** When someone explains why a product, method, or hire didn't work, they're not just naming the thing — they're describing exactly what still hurt afterward, what they expected versus what happened, what mistake they now realize they made. That's problem-state material, and it's usually more specific and more surprising than what turns up when you search for the problem directly, because the person is reasoning through a concrete disappointment instead of describing a vague feeling.
2. **The audience describing it is already a buyer in this category.** Someone who's tried and rejected 2 or 3 things adjacent to the offer has already proven they'll spend money on this exact problem. Hooks built from how they talk about that failure land harder because the recognition is sharper: "you already know this particular disappointment" hits differently than "you have this general problem."

This makes the Failed Solutions pass worth mining harder than its 8+ minimum whenever it's productive — treat it as a priority pass, not just 1 of 7 equal ones. It's not the only good source of problem language (visceral pain description, collateral damage, and private behavioral tells are just as capable of producing a great hook), but it's disproportionately likely to produce specific, surprising phrasing precisely because it comes from people mid-transaction in the category, not just people in pain.

**The hard rule that goes with this: never carry a specific brand, product, or tool name into the Market Voice Bank, the Lingo Bank, or any hook.** If a mined quote says "I tried HubSpot for 6 months and it did nothing," the Market Voice Bank entry is the *sentiment and mechanism* — "the CRM everyone recommends, sitting unused after 6 months" — never the brand name itself. Strip the name at the moment you extract the quote, not later. This isn't just about avoiding a legal headache; a named competitor in a hook reads as a comparison ad, not a mirror of the prospect's own words, and it breaks the illusion that the hook came from inside their own head. Generic tactic categories are fine and often necessary ("a CRM," "a retention dashboard," "a discount," "a customer success hire") — it's the specific proper noun that has to go.

That's 52+ quotes minimum across the 7 passes. Every quote follows the Mirror Rule exactly as Market Copy Miner defines it: shift first person to second person, allow breaking one long sentence into two — nothing else. Never add a word, an image, or an idea the raw quote doesn't already contain.

Don't dump all 52+ quotes on the user. Distill them into the Market Voice Bank in Step 3.

## Step 3: Build the Market Voice Bank

Compile the mined material into this compact format and show it to the user before writing a single hook — it's the proof of where the hooks' language is coming from, and it lets them catch a bad mine before you commit to 100 hooks built on it.

```
MARKET VOICE BANK
Identity: [the avatar]
Problem (their words): "[best raw quote or mirrored version]"
Failed solutions (their words): "...", "...", "..."
Common advice that fails them: "..."
Villain / who they blame: "..."
Mistake that keeps it alive: "..."
Consequence / collateral damage: "...", "..."
Private behavioral tells: "...", "...", "..." [as many strong ones as you found — this list drives the Mirror hooks]
Skepticism language: "..."
Desired result (their words): "..."
```

Pick the single strongest, most specific option for each single-line field. For the multi-quote fields, keep 3-5 of the sharpest. Then run the lingo sufficiency gate below before saying anything to the user about being done.

### Lingo sufficiency gate (mandatory — do not skip, do not proceed to Step 4 until this passes)

Before showing the bank to the user, audit every field against 1 test: **read it out loud. Does it sound like something a real person actually typed, or does it sound like a category label a consultant would put in a slide?**

- Sounds real: "white-knuckling your way through the week," "the call came, and it was swift," "I'm left with this nagging feeling in my gut that I did something wrong."
- Sounds synthesized, not real, even though it came from a mined source: "client attrition," "delivery gap," "account health score," "customer success," "retention strategy." These are industry vocabulary that shows up across many sources precisely because they're generic, not because they're distinctive. If a field in your bank reads like one of these, it's a fact or a category label wearing a quote's clothing, not real lingo.

**If any field fails this test, do not move to Step 4.** Go back to Step 2 and run 1-3 more targeted searches aimed specifically at that field, using confessional phrasing instead of conceptual phrasing (see Step 2's lingo-vs-facts note). Add whatever you find to the bank and re-run this audit. Repeat until every field has at least 1 genuinely quotable phrase, or until 2 extra passes on that field still come up empty — in which case, mark that specific field as thin in the bank itself (not just in your head) so it's visible before you build hooks on it, and lean harder on the fields that are strong.

This gate applies per-family too, not just per-field: the Mirror family (15 hooks) needs real behavioral specifics, not just a general sense that agency owners get stressed. If Private Behavioral Tells only produced vague material, that's worth 2 extra targeted searches before you write a single Mirror hook, because 15 hooks built on thin material will all feel the same.

Once the gate passes, say: *"That's the mined material. Writing the 100 hooks now."*

## Step 4: Write the 100 hooks

Every hook still does the 2 things Reel Hook Writer requires:
1. Calls out the prospect — directly ("you/your") or by identity.
2. Puts them in a problem state — names or evokes the specific mined problem.

**The rule that makes this different from Reel Hook Writer:** every descriptive fill-in — the problem, the failed solution, the common advice, the mistake, the consequence, the private struggle — must be an actual entry from the Market Voice Bank, used verbatim or lightly Mirror-Rule-adjusted. Only the construction's frame words ("why," "did you know," "here's why," "it's 3am and," numerals) are Claude's own.

**This is the single most important rule in this skill, and the easiest one to quietly break.** The failure mode isn't writing something totally made up — it's reaching for a clean industry term instead of the real phrase because the industry term is easier to drop into a sentence. "Client attrition," "delivery gap," "account health score" are fluent and grammatical, which is exactly why they're tempting and exactly why they're wrong: fluent, grammatical, category-label language is what every other hook in this niche already sounds like. The mined phrase — "watching clients walk," "the call came, and it was swift," "white-knuckling through the week" — is what makes this one sound like it came from someone who's actually lived it.

**The mid-write gate:** if you're about to write a hook and the fill-in you're reaching for is a generic industry term rather than something from the bank, stop before you write it. That's not a signal to paraphrase harder — it's a signal the bank doesn't have what this hook needs yet. Go back to Step 2, run 1-2 targeted searches for that specific gap, add whatever you find to the bank, then write the hook. Do this as many times as it comes up. Writing 100 hooks should routinely send you back to search more than once; if it doesn't, that's a sign you're filling gaps with synthesis instead of noticing them.

### Family budget (defaults to exactly 100 — flex ±2 per family if needed, but the total must land on 100 and Mirror never drops below 10)

| Family | Count | Hook #s |
|---|---|---|
| Why hooks | 18 | 1-18 |
| The Mirror (private struggle) — mandatory | 15 | 19-33 |
| Did you know | 7 | 34-40 |
| Here's why | 7 | 41-47 |
| The reason why | 7 | 48-54 |
| Time Stamp | 7 | 55-61 |
| Misdiagnosis / Wrong Enemy | 7 | 62-68 |
| Failed Solution Stack | 10 | 69-78 |
| Two Camps Split | 6 | 79-84 |
| Ban / Warning | 6 | 85-90 |
| Direct identity callouts | 10 | 91-100 |

### Constructions to fill (mined language goes in every bracket)

**Why hooks (18)** — vary across these, don't run the same one 18 times:
- Why haven't [identity] with [problem] been told these facts?
- Why is it so hard for [identity] to [get result] when others did it so easily?
- Why your [problem does this] and what you can do about it.
- Why [identity] should never [mistake].
- Why [identity] who [specific behavior] are silently [suffering consequence].
- Why your [problem] keeps coming back, [identity], no matter what you try.
- Why [percentage/number] of [identity] still struggle with [problem] and don't know why.
- Why [identity] with [problem] are told [common advice], when it actually makes things worse.
- Why [identity] who've tried [failed solution] still have [problem].

**The Mirror (15, mandatory)** — read `references/mirror-library.md` in full before writing these, never from memory. Its 26 templates and 4 sub-patterns (location tell, ritual tell, witness twist, double watch) are the toolkit. **Preference order: use the mined private behavioral tells from the Market Voice Bank first.** Only invent a struggle using the sub-patterns if the mining pass came up short on behavioral specifics — and if you do, keep a private tally so you can flag it in the sign-off at the end (see Step 5). The viewer's reaction should be "how do you know that." Never mock; the reader should feel seen, not exposed.

**Did you know (7):**
- Did you know [identity] with [problem] are [surprising fact/consequence]?
- Did you know [common advice] is why your [problem] won't go away?

**Here's why (7):**
- Here's why your [problem] [keeps happening/gets worse/won't respond].
- Here's why [identity] can't [get result] no matter how hard they try.

**The reason why (7):**
- The reason why your [problem] [does the frustrating thing] isn't what you think.
- The reason why [identity] stay stuck with [problem] comes down to 1 thing.

**Time Stamp (7):**
- It's 3am and you're a [identity] staring at the ceiling because of [problem].
- Every morning you [painful routine caused by problem].
- You've had [problem] for [timeframe] and it's not getting better.

**Misdiagnosis / Wrong Enemy (7):**
- Your [problem] was never about [assumed cause].
- [Identity], you've been fighting the wrong thing this whole time.
- It's not your [assumed cause]. It's your [hidden cause].

**Failed Solution Stack (10):**
- You bought the [product 1]. You tried the [method 2]. You did the [protocol 3]. [Problem] is still here.
- If [failed solution] worked, [identity] wouldn't still have [problem].

**Two Camps Split (6):**
- There are 2 kinds of [identity] with [problem]. One fixes it. One never does.
- [Identity] who beat [problem] do 1 thing different from [identity] who don't.

**Ban / Warning (6):**
- [Identity]: stop [common behavior] until you hear this.
- Do not [popular action] if you have [problem].

**Direct identity callouts (10):**
- [Identity]: your [problem] isn't your fault. It's [hidden cause].
- If you're a [identity] with [problem], stop [mistake] right now.
- You've tried [failed solution 1], [failed solution 2], and [failed solution 3]. Your [problem] is still here. This is why.
- Every [identity] with [problem] does this 1 thing that makes it worse.
- [Number] out of [number] [identity] have [problem] because of [hidden cause] and nobody tells them.

### Hooks stay in problem state, never solution state

Some construction templates end on a placeholder that is meant to stay unnamed: "been told these facts," "isn't what you think," "comes down to 1 thing," "when it actually makes things worse," "this is why." That vagueness is the tease. It's what makes someone stop scrolling to find out. If you fill that placeholder in with the actual fact, cause, comparison, or fix, you've resolved the curiosity instead of creating it, and the hook stops working. This is the single most common way a hook quietly turns into a mini-answer instead of a scroll-stopper.

**The test:** after reading the hook, does the viewer still need to watch to learn the essential thing, or did the hook already hand it to them? If the payoff is already in the hook, it's solution state. Pull it back.

Example of the failure mode: "Why haven't agency owners been told delivery beats budget every time?" — this names the actual insight ("delivery beats budget") in the spot the template means to leave open. The fix: "Why haven't agency owners with client attrition been told these facts?" — same template, same identity and problem, but the fact stays a tease.

**This does NOT mean every hook must withhold every cause.** Some templates are explicitly built to name a cause as their whole mechanism, and that's fine because naming the cause still leaves "what do I do about it" unanswered:
- Misdiagnosis ("It's not your [assumed cause]. It's your [hidden cause].") is designed to name the hidden cause. That's the reframe, not a resolution.
- Direct callouts like "[Identity]: your [problem] isn't your fault. It's [hidden cause]" and "[number] out of [number] [identity] have [problem] because of [hidden cause] and nobody tells them" are built the same way.
- Naming a specific bad behavior or mistake ("they let 1 account manager be the only one who knows the client") stays in problem state even though it's specific, because it describes what's going wrong, not how to fix it.

The line isn't "never name anything specific." It's "never let the hook fully answer the question it just raised." Naming a hidden cause deepens the mystery. Naming the fix, the comparison, or the insight that resolves it ends the mystery, and that's the failure to catch before delivering.

## Writing rules (non-negotiable, pulled straight from Reel Hook Writer)

- Spoken word. Read every hook aloud before locking it. If it sounds written, rewrite it.
- Market language wins over marketer language, always. That's the entire point of mining first. Concretely: if a fill-in is a clean industry term (attrition, retention, delivery gap, health score, and the like) instead of a phrase from the Market Voice Bank, it's wrong even if it's factually accurate. Go back and mine for the real phrase rather than keeping the accurate-but-generic one.
- Concrete over abstract in every fill-in.
- Numerals, never spelled-out numbers.
- Contractions everywhere.
- No em dashes. Ever.
- No AI slop language — quietly, genuinely, unlock, elevate, delve, journey, game-changer, revolutionary, seamless, robust, dive in, landscape, realm, tapestry, testament, crucial, vital, comprehensive, and the rest of the standard list. If `/mnt/skills/user/ai-slop-terminator/SKILL.md` is installed, read it and run its full scrub before delivering. Don't scrub from memory.
- No hype claims. A hook creates curiosity and recognition, not a promise. Health and money niches: no diagnosis language, no cure claims, no guaranteed outcome, even when the mined quote itself makes one — mirror the feeling, not the illegal claim.
- 1 line per hook, roughly 8-18 words. Mirror hooks can run to 25 since the private struggle needs room.
- No near-duplicates. Scan every family before delivering — if 2 hooks share the same structure and the same fill-ins, replace 1.
- No 5-in-a-row from the same family in the final numbered list, even though the list is grouped by family header — inside each family's block, vary the specific template used so it doesn't read as one template with the blanks swapped.
- Every hook must survive this test: would the exact person with this exact problem stop scrolling because they felt personally named, in their own words? If not, go back to the Market Voice Bank and find a sharper quote.
- Every hook must also survive the problem-state test from above: does it leave something unresolved, or did it already hand over the answer? A hook that fully explains itself doesn't need a click.
- **Final pass before delivering: scan all 100 for generic industry terms that snuck in** (attrition, retention, delivery gap, health score, and similar clean category language). For each one you find, either swap in the matching Market Voice Bank phrase, or if the bank doesn't have one for that spot, run 1 more targeted search before finalizing. Don't ship a hook with synthesized language just to hit the count.
- **Same final pass, same scan: check for any brand, product, or tool name that slipped through**, especially in Failed Solution Stack hooks, which are the family most likely to have picked one up straight from a mined quote. Replace any with the generic tactic category before delivering.

## Step 5: Output format and delivery

```
MARKET VOICE BANK
[as built in Step 3]

100 HOOKS
Identity: [avatar]
Problem: [problem]

WHY HOOKS
1. ...

2. ...

...

18. ...

THE MIRROR
19. ...

...

33. ...

DID YOU KNOW
34. ...

...

[continue through all 11 families to hook 100]
```

**Put a blank line between every single hook, no exceptions.** A dense, single-spaced wall of 100 numbered lines is hard to scan and hard to pull individual hooks from — one blank line after each hook (before the next number) is mandatory in the file, in chat, and in any other delivery of this list. Family headers get a blank line above and below them same as before. This spacing rule doesn't apply to the Market Voice Bank, which stays compact.

Before delivering, count. Hooks must be numbered 1 through 100 with no gaps and no repeats. Write the full list to a file first — `/mnt/user-data/outputs/hook-miner-[avatar-or-client]-100.txt` — then verify mechanically: `grep -cE '^[0-9]+\.' file.txt` must return exactly 100 (blank lines between hooks don't affect this count, since blank lines don't start with a digit). If it doesn't, find the missing or duplicate number and fix it before presenting anything. Then deliver the full 100 in chat as well as the file, with the same blank-line spacing — this list is short enough per hook that chunking across responses isn't necessary the way it is for full 21-hook-per-script scripts batches.

Close with a short sign-off: how many quotes fed the bank, how many extra targeted mining passes the lingo sufficiency gate sent you back for (0 is a fine answer, but say so either way), which fields (if any) stayed thin after 2 extra passes, and if any Mirror hooks had to be invented rather than mined, how many and which ones (by number) so the user can double-check them before use.

## Edge cases

- **Mining comes up thin on a niche pass** (e.g., a very new or small market has few forum threads): don't pad with weak quotes. Take what you found, and for that field in the Market Voice Bank, tell the user it's the thinnest pass and hooks pulling from it should get extra scrutiny.
- **User wants a number other than 100:** keep the same family proportions, scaled, and keep Mirror hooks at roughly 15% of the total minimum.
- **User wants hooks for a specific existing offer/script's problem, not a fresh avatar interview:** pull the problem from what they gave you, confirm your read of it in 1 line, then mine around that exact problem.
- **Health, finance, legal, or other regulated niche:** the private struggle and pain language can mirror the market's words freely, but never let a mined outcome claim slip into a hook as a promise. If a raw quote says "this cured my anxiety," the hook mirrors the feeling of relief, not the word "cured."
- **User already has a Market Copy Miner messaging file from an earlier session:** ask them to paste it (or the Top 10 Power Lines / Headline Swipe File sections at minimum) instead of re-mining from scratch, then build the Market Voice Bank from that.

## Opening the session

Open with exactly:

*"Welcome to Hook Miner. I mine the market's own words first, then pour that language straight into 100 hook constructions, no script required. You get 1 flat list: 100 problem state hooks in your prospect's voice, not a messaging file. Who is your avatar and what is the core problem your offer solves?"*
