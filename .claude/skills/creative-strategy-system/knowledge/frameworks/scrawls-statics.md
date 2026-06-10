# Statics — the complete process (SCRAWLS + the format bots)

How to generate a high volume of winning static ad concepts. There are **two categories** of static
ads, and the process for each is different. (Image gen: we use **GPT-Image** and **Nano Banana Pro**.)

> **Why statics matter:** cheaper to produce, faster to test, and when they hit they scale as hard as
> video. The problem is most people have no real *process* — they guess, or reuse the same 3 styles.
> This is the process.

---

## The fork — two categories

| Category | Who's scrolling | Feel | Process |
|---|---|---|---|
| **1 · Unaware / Problem-aware** | doesn't know the product (or the problem) | **native, in-feed** — looks like a real post, a little shocking/weird, "what the f*** am I looking at?" | **SCRAWLS** (deep ideation) |
| **2 · Solution / Product-aware** | knows they want a solution / the category | cleaner, more direct — proof, comparison, offer | **the format bots** (run product through proven formats) |
| *(Most-aware)* | knows your brand, wants a discount | simplest | skip — just a promo |

*Context nuance:* for **info products** you often *don't* go hard on mass-market unaware curiosity (you
want friction/exclusion for good leads). For **e-com** (lower-ticket), cast wide. Decide how hard to
lean into Category 1 accordingly.

> **In the kit's three static types — this is the clean mapping:**
> - **Native = SCRAWLS, only.** The deep ideation that finds weird/real/visceral in-feed images. No
>   fixed template — the image itself is the idea.
> - **Templated = a per-format bot.** One bot per proven layout (Before-After, Infographic, Comparison,
>   Holding Sign, Native News…). Run your product through it.
> - **Branded = the same, product-forward bots** (Hero, Branded, Product-Breakdown-forward…).
>
> So: native ⇒ run SCRAWLS. Templated/branded ⇒ pick the format bot and feed it your product. Don't run
> SCRAWLS for templated/branded, and don't expect a format bot to do native.

---

## Category 2 (the easy one) — the format bots

Have a set of proven static formats and **run your product through each one**. Pick a format → feed it
your product info or ad copy (Build-a-Buyer / Copy Blocks / Offer Brief / sales copy) → it returns a
concept (headline · visual direction · layout · color) → drop into GPT-Image / Nano Banana Pro. Test a
few types, find what works for your brand, iterate.

**The 30+ formats (Genesis/Exodus ships trained bots for these; build your own in the kit):**
Headline + Image · Side-by-Side / Before-After · Infographic · Product Breakdown · Animation ·
Comparison · Scientific Study · Collage · Holding Sign · Native News · Note From Founder · Testimonial ·
Lo-Fi · Bold Typography · Meme · Hero · Comment/Review · Handwritten/Note · Screenshot/Chat/Notification ·
Breaking/Authority · Carousel/Story · Branded · Statistic · Post-It Note · Happy Avatar ·
Problem-Solution · Writing On Body · Multi-Testimonial · Receipt · Step-By-Step · Sales/Promo Offer ·
Cost of Inaction · UGC · Quiz/Interactive.

---

## Category 1 (the real magic) — SCRAWLS

**SCRAWLS = Swipes · Copy-derived · Reptile triggers · Audience language · Wild sourcing · Loopback ·
Source.** Seven sources → **80–200 raw concepts**. Pulling from many sources (like STORMING for copy)
spreads your coverage across the whole board (Battleship — don't cluster your shots). Two flywheels:
the process trains your visual judgment, and diverse sources keep the account healthy (no local-maximum
trap).

### S — Swipe mining (competitors only)
What static formats are competitors *spending* on. Meta Ad Library (active ads, your country) by brand
**and** by keyword ("grounding sheets," "joint pain"); AdSpy if you have it. For each: note the format,
note longevity (= it's working), save the link. → a swipe file of 20–50 winning formats. **S = competitors
only; your own ads go in L.**

### C — Copy-derived (from your ad text)
Feed your full ad copy (hook + body) to the bot → ~10–15 concepts. They'll be boring at first — **push
hard**: "option B, weirder," "C, turn up the dial," "D, adjacent/associative," "E, completely unrelated
objects," "more visceral," "what objects from their daily life?" Run **2–3 passes** (passes 2–3 are where
it gets real). → 20–30 concepts. *Images need NOT connect logically to the product — disconnected often
wins. The job is stop-the-scroll + a visceral reaction.*
> **Prompt:** *"For the following ad, please break down individual ideas, sentiments, emotions, feelings,
> symbols or anything else that could then be turned into a powerful static ad. Ideally we're looking for
> something very native for in-feed ads — what someone would actually post on FB. Offer general ideas,
> then specific suggestions of where to find them. Be thorough."*

### R — Reptile triggers (primal psychology)
Run the ad through **13 primal triggers** → visceral gut-punch concepts. The bot self-censors — push it:
*"A tasteful reptile trigger is a failed reptile trigger. Take each literally. Sexual means sexual.
Primal Fear means actual death."* Runs: ①all 13 · ②push A–E with enforcement · ③identity / sense-of-self
/ core wound · ④adjacent objects only (zero product link). ~20% usable; **pick the ones that make you
uncomfortable.**
**The 13:** Ultra-Real (candid iPhone, not polished) · Bizarre (pure pattern interrupt) · Voyeur (texts,
screenshots, something private) · Suffering/Pain · Gory/Visceral · Sexual · Primal Fear (death, danger) ·
Inside Joke (only your niche gets it) · Old/Vintage · Victory Lap (aspirational outcome) ·
Selfie/Demographic · Uncanny Object · Wildcard.

### A — Audience language (customer words → images)
Mine comments, testimonials, group posts for **visual language** — objects, scenes, moments. "White-
knuckling the toilet seat" → hands gripping a toilet seat. "Hiking boots haven't moved in 3 years" →
dusty boots by a door. A mentioned object (heating pad, pill organizer, knee brace) **is** the image.
Translate: physical struggle → show literally · emotion/state → animation (avoids AI-face uncanny
valley) · relationship shift → show the relationship. → 10–20 of the most authentic concepts.
> **Prompt:** *"For the following comments from ads, please generate ideas for new static ads — native
> in-feed, what someone would actually post on FB. Pay attention to emotions, symbols, objects, or any
> other ideas. Be thorough."*

### W — Wild sourcing (leave the ad ecosystem)
Hunt **real, native, UGC** images from the wild — NOT ads, NOT stock. Reddit (pain subs r/ChronicPain,
identity subs r/Menopause, adjacent r/Earthing — sort top, high-engagement image posts), niche FB groups,
Google Images ("senior hiking," "joint pain morning"). Save 30–60 native-looking reference images. **These
become your style references at render time — they massively raise quality.**

### L — Loopback (your own winners only)
Pull your top images (by ROAS/CPA/spend). For each, list the elements (subject · angle · quality/style ·
lighting/mood · text style · emotion), rank by importance, then **expand each** (bloodshot eye → eye bags,
dilated pupils, yellow eyes) and **stack vectors** (vintage + pain + body part = sepia photo of swollen
joints). The flywheel: winners feed back → more winners. **L = your account only.** Skip on a cold start.
> **Prompt:** *"Please analyze all of these existing ad images and identify any patterns or themes that
> emerge. Cluster into themes and 'types.' Then offer suggestions for NEW ideas based on these."*

### S — Source (your own brain)
After S→L, ideas are firing — write them ALL down. Your instincts sharpen every cycle; eventually your
own brain is one of the most valuable sources. (The flywheel: SCRAWLS trains your judgment, your judgment
improves SCRAWLS.)

---

## Generating the actual images

You should now have **80–200 raw concepts**. Scan, pick the **15–20 that hit hardest** (does it stop you?
visceral reaction? different from last batch? trust your gut).

**For every pick, find a real reference image** (Google Images, your Wild-Sourcing folder, Reddit, swiped
ads). *This matters a lot — image models work far better with a reference than text alone. Always find one
first.*

Then render. **We use GPT-Image and Nano Banana Pro** (Midjourney optional for top quality):
- **GPT-Image** — fast, good. Detailed text prompt (subject · style · mood · angle · lighting · text
  overlays · format). Add **"native to Facebook feed, NOT polished, NOT an ad"** to *every* prompt.
  3–4 variations per concept.
- **Nano Banana Pro** — best for text-heavy formats + screenshots; accepts reference images directly.
  *"Recreate this style as a 1:1 square static for [product]. [concept details]."* Great for Notes-app
  screenshots, texts, tweets, writing-on-body.
- *(Midjourney — best overall; RAW mode, stylize 0, 1:1 or 4:5; reverse-engineer 5 prompts from your
  reference.)*

Per concept: 3–4 images across tools → 15–20 concepts × 3–4 ≈ **60–80 images** → pick **12–16 testable
creatives** to run.

---

## Testing structure & the flywheel
Lock **1–2 hooks + 1–2 headlines**, then test many **images** against them (the image is the variable you
test in volume). Find a winner → run it back through **Loopback** → extract the vectors → 10–20 variations
→ test → feed new winners back into L. It never stops.

## The hard rules
- Images **need not be logical** — disconnected often wins.
- **Push every bot relentlessly** — first output is boring; passes 2–3 are where it gets real.
- **~20% hit rate is normal** — 100 concepts → test 15–20 → 3–4 winners.
- **Reference images make output 10× better** — always find one first.
- **Format: 1:1 or 4:5. Never anything else.**
- Must look **native to the feed** — "what the f*** am I looking at," not a polished ad.
- **Variety over volume** — spread across sources/categories; don't make 10 of the same.
- **S = competitors, L = your account. Never blend them.**
- Trust your instincts more every cycle.
