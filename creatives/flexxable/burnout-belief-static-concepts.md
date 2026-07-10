# BURNOUT belief-validation — static concepts (SCRAWLS: C + A + R·Voyeur)

Ad: [copy/2026-07-10-flexxable-iaa-burnout-belief-fb-ad.md](../../copy/2026-07-10-flexxable-iaa-burnout-belief-fb-ad.md)
Category: **1 · native SCRAWLS** (awareness = unaware). Info-product → native but
*qualifying* (a burnt agency owner recognises himself), not mass-market shock.
Constant to test against: hook 1 + one headline. Image is the variable. Format 4:5.
Overlay text is pulled from the ad's already-judged lines; any new micro-copy gets a
lint pass before render.

Legend: **V** = Voyeur/confession · **U** = Ultra-Real/Suffering · **C** = Copy-derived/symbolic

---

## Voyeur / confession — the format that IS the angle ("can't say it out loud")
1. **[V] iPhone Notes screenshot** — a note titled *"things I can't say out loud"*, body = the hook verbatim. No face. Nano-Banana (screenshot). The confession you type and never post.
2. **[V] Half-typed text, never sent** — an iMessage draft to "Wife"/a mate: *"some days I don't even want to—"* typing dots, unsent. The thing you delete before sending.
3. **[V] Two-column Notes list** — left *"What everyone sees"* (best month, laptop, six figures) / right *"What it actually is"* (3am, chest tight, haven't sat at the table in weeks). The contradiction, literal. ⭐
4. **[V] Screen-time screenshot** — *"214 pickups today. First pickup: 3:04 AM."* Data as confession. No face.
5. **[V] Bank push + Google search stacked** — a payment notification *"You received £8,420"* directly above a search bar: *"why do i feel nothing when i make money".* The split, in one glance. No face. ⭐
6. **[V] Fake "must be nice" comment** — a win post with the top comment *"must be nice 🙄"*; poster's face cropped out. Nails the exact social trap the ad names. ⭐

## Ultra-Real / Suffering — candid, native, unflattering
7. **[U] Car in the driveway, night** — guy in the driver's seat outside his own lit house, hands still on the wheel. Overlay: *"too exhausted to walk inside."* Reddit ref. ⭐
8. **[U] Lunch at the desk** — overhead iPhone shot: sad sandwich beside a laptop of dashboards, a kid's drawing at the edge. Overlay: *"my kid asked why I don't sit at the table anymore."*
9. **[U] 3am ceiling** — POV in bed, phone glow on face, clock 3:07. Overlay: *"best month I'd ever had. Couldn't sleep."*
10. **[U] Bathroom mirror, pre-work** — tired guy, phone in hand, harsh light. Overlay: *"checking my phone before I even had a piss."* Native, unflattering.
11. **[U] Stripe graph at night** — revenue line up, shot candidly (phone over laptop, screen reflection). Overlay: *"best month ever. Felt absolutely nothing."*

## Copy-derived / symbolic — pattern interrupt (higher risk, mark as gambit)
12. **[C] The leash** — a dog lead wrapped around the wrist of a hand typing on a laptop (*"the money was the leash"*). Associative, weird. Gambit.
13. **[C] Packed calendar wall** — every slot full incl. weekends, one tiny handwritten *"breathe?"*. Overlay: *"next quarter is never calmer, is it?"*
14. **[C] Envy flip** — candid of a guy staring at someone's retirement/holiday post. Overlay: *"I was jealous of my dad's retirement."*
15. **[C] Invoice + scrawl** — a printed big-number invoice with a handwritten line across it: *"and I still couldn't sleep."* Nods to the house `rob-invoice-80k-static.png` style (Loopback-adjacent).

---

## Picks to test first (⭐)
Filtered on: carries the angle · stops the scroll · reference is gettable · info-product-qualifying.
- **#3** (what everyone sees / what it is) — cleanest belief-validation contradiction; text-only render, no face, fireable now.
- **#5** (payment + "why do I feel nothing") — visceral split; text-only, fireable now.
- **#6** ("must be nice" comment) — nails "can't say it out loud"; text-only.
- **#7** (car in driveway) — strongest Ultra-Real image; needs a Reddit reference photo for quality.
- **#1** (Notes confession) — format = angle; text-only.

**Render order:** #3 + #5 first (text-heavy → nano-banana text-to-image, no reference hunt),
then #7 once we pull a candid reference. ~20% hit rate: from these we expect 1 clear winner → Loopback.

---

## Render log (2026-07-10) — via `scripts/run_image.py` (KIE)
Learning banked: base model `google/nano-banana` garbles fine screenshot text
(duplicated words, junk UI labels). **Text-heavy statics → render on `nano-banana-2`
(Pro).** Pro also rendered 1:1 not 4:5 — 1:1 is feed-native, fine; exact 4:5 flag TBD.

- **#3 v1** `burnout-static-c3-notes-v1.png` — base model. REJECT: "chest chest tight", garbled tab bar.
- **#3 v2** `burnout-static-c3-notes-v2.png` — nano-banana-2. **KEEPER.** Clean Notes screenshot, low red battery at 3:07 reinforces the burnout.
- **#5 v1** `burnout-static-c5-payment-search-v1.png` — nano-banana-2. **KEEPER.** Lock screen: Stripe £8,420 received + Google search "why do i feel nothing when i make money" (reddit autocomplete).
- **#6 v1** `burnout-static-c6-mustbenice-comment-v1.png` — nano-banana-2. **KEEPER.** FB win post + top comment "must be nice 🙄".

**First test set = #3v2 + #5 + #6** against the locked hook. Next: pull a Reddit ref for #7 (car in driveway).
