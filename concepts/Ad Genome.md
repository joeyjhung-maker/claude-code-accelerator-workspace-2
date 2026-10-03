# Ad Genome

The thinking model for taking an ad apart, and for listing everything in it that can be tested.

Every ad is a stack of six layers. The bottom layers are the most fundamental. The top layers are the most subtle.

![[ad-genome-pyramid.png]]

| | Layer | The question it answers |
|---|---|---|
| 6 | **Copy beats** | What gets said, in what order, line by line? |
| 5 | **Actors, styles, looks** | Who's on screen, and what does it look like? |
| 4 | **Conceits** | What is the ad pretending to be? |
| 3 | **Concepts, angles, formats** | What's the claim, why should they care, and what's the skeleton? |
| 2 | **5 awareness levels** | How much do they already know? |
| 1 | **Segments + sub-segments** | Who is this for? |

Read it bottom up. Layer 1 decides everything above it.

Source: Genesis, "5 Workflows That Make Winning Ads" (slide 40). Saved 2026-10-03.
Related: [[The Lock]] [[creative-coverage]] [[concepts-and-angles]] [[hooks]] [[multiply]] [[timeline-ad]] [[cs-client-onboarding-DRAFT]]

---

## What each layer is, and what you test there

**1. Segments + sub-segments.** Who it's for.
- Three parts: the outcome they want, who they are, and why they're here (the facet).
- Test: a new outcome, a sub-outcome, a new demographic, a new facet.
- Biggest lever. A new segment is a new pocket of buyers.
- Lives in: `/segments`, the client's strategy map.

**2. Awareness.** What they already know.
- Unaware, problem-aware, solution-aware, product-aware, most-aware.
- Test: the same segment at a different level.
- Most accounts sit in the middle. The two ends are usually empty.
- Lives in: `/brief` (Awareness field), `brand/creative-coverage.md`.

**3. Concepts, angles, formats.** The message and its skeleton.
- Concept: the claim about the world.
- Angle: the frame that makes them care (whistleblower, discovery, confession).
- Format: the beat order (timeline, listicle, comparison, story).
- Test: hold the concept and rotate angles. Hold the angle and rotate concepts. Keep both and change the format.
- Lives in: `brand/concepts-and-angles.md`, `/timeline-ad`.

**4. Conceits.** What the ad pretends to be.
- A podcast clip. A street interview. A customer call. An apology letter.
- A conceit changes the shape of the script.
- Test: the same message, staged as a different kind of media.

**5. Actors, styles, looks.** Who and how it looks.
- Actor: real or invented, expert or peer, and what they look like.
- Style: the filter. Raw iPhone, claymation, Notes app.
- A style changes the picture and leaves the script alone.
- Test: new creator, new style. The cheapest swap there is.

**6. Copy beats.** The words.
- The hook, the lines, the proof, the call to action.
- Test: new hooks on a frozen body. One reworded beat.
- Lives in: `brand/hooks.md`, `rubrics/hook-rubric.md`.

---

## How the layers behave

- **Lower layers are bigger bets.** A new segment or a new awareness level can open a whole new front. It also costs more to prove.
- **Upper layers are cheaper swaps.** A new style or a new hook is fast and low risk. The win is usually smaller.
- **Change one layer at a time.** Change two and a miss teaches you nothing.
- **A winner is one path through all six.** One segment, one message, one treatment, proven with spend.
- **A gap is an empty slot at any layer.** No unaware ads. No statics. Nobody talking to men over 55.

---

## The diagrams

Five diagrams from the same deck. All saved in `concepts/_assets/`.

### 1. The genome (top of this note)
The six layers, most fundamental at the bottom.
**Use it for:** dissecting any ad, and listing what can be tested.

### 2. One winning ad is one path
![[ad-genome-one-winning-ad-path.jpg]]

Each layer is a row of options. A winning ad is one box lit up in every row, joined into a single path.
**Use it for:** explaining what a "winner" is. And for seeing that every unlit box next to the path is a test one swap away.

### 3. Horizontal vs vertical
![[ad-genome-horizontal-vs-vertical.jpg]]

Start from a winning ad. Go sideways for new segments and personas. Go up for new styles, formats and conceits.
**Use it for:** deciding which direction the next batch goes. Vertical first. Horizontal once the current segments are squeezed.

### 4. The segment cube
![[segments-odf-cube.jpg]]

Three axes: outcomes, demographics, facets. One small cube is one segment.
**Use it for:** layer 1. Finding segments nobody is talking to. Facets (why they're here) are the axis most accounts ignore.

### 5. The map, from brand to the one-second line
![[segments-map-brand-to-one-second-line.jpg]]

A tree for one brand. Brand → outcomes → sub-outcomes → who and why → the line they recognise themselves in within a second.
One column is one persona: same product, same proof, new door.
**Use it for:** laying out a client's segments on one page, and picking the first bet. The highlighted column is the example bet: a facet no competitor is running.

---

## How to dissect an ad (about a minute)

Go bottom up. Say one line per layer.

1. **Who is it for?** Outcome, person, and the reason they're here.
2. **What do they already know?** Listen to the first line. Does it name a problem, a solution, or the product?
3. **What's the claim, and what's the frame?** Then name the skeleton.
4. **What is it pretending to be?**
5. **Who's on screen, and what's the look?**
6. **What's the hook, and what are the beats?** Note the words that carry the weight.

Then two more lines:

7. **Why does it work?** Usually one layer is doing the heavy lifting. Name it.
8. **What would I test next?** One swap, one layer, and why.

### Worked example

The RYZE blue-collar 30-day ad from the timeline training. Script only, so layer 5 is partly unknown.

| Layer | This ad |
|---|---|
| 1. Segment | Blue-collar men in their 40s. Outcome: energy and a smaller gut. Facet: drinks energy drinks to get through a shift |
| 2. Awareness | Problem-aware. He knows he's tired and soft. He doesn't know about the product |
| 3. Concept / angle / format | Concept: mushrooms fix energy and gut together. Angle: watch what happens over 30 days. Format: timeline |
| 4. Conceit | A narrated story about one man. No interview, no podcast |
| 5. Actor / style | Actor: "a blue-collar man in his 40s", a peer. Style: not known from the script |
| 6. Copy beats | Frame and tease → day one, nothing happens → things that stop → an ingredient per result → the shirt fits → "there he is" → the cheap-version comparison → one cup → proof → offer |

- **Why it works:** layer 3. The timeline lets small claims build, so the big one at the end is already believed.
- **What I'd test next:** layer 1. Same script, swap "blue-collar man" for a nurse on nights. The moments change with her. Everything else stays.

---

## Using it in an interview

Two questions are likely: "what's your testing process?" and "talk me through this ad."

### "Talk me through this ad"

Use the dissection above. Bottom up, one line per layer, then why it works and what you'd test next.

Ending on the next test is the point. It shows you read ads as things to act on.

### "What's your testing process?"

**Ask first.** The honest answer depends on the account.
- What are you optimising for right now?
- What's your split between iteration and net new?
- Where's new-customer cost against target?

**Then give the frame.** Something like this, in your own words:

> I read every ad as six layers.
> Who it's for. What they already know. The message and its skeleton. What it's pretending to be. Who's on screen and how it looks. Then the words.
>
> My first job in an account is to tag the winners on those layers.
> That shows me the patterns. It also shows me the gaps: the segments, the awareness levels and the formats nobody's running.
>
> Then I test one layer at a time.
> Top layers first, because they're cheap. A new style or a new creator on a script that's already proven.
> Bottom layers next, because that's where the big wins are. A new segment. An unaware ad.
>
> Every ad goes out with a one-line hypothesis.
> So a win is a predicted win, and a miss still teaches us something.
>
> I judge top-of-funnel ads on new-customer cost, and I check which ads brought the customers who stayed.

**What makes this a good answer.**
- Most candidates say "I look at spend and ROAS, do research, and come up with ideas."
- This shows a map, an order of operations, and a way to learn from misses.

**Keep it honest.** Use a real example from your own work when you have one. Don't quote a result that isn't yours.

---

## Where the rest lives

- The five ways to swap a layer: `/multiply`
- The moves ranked by difficulty (Bankers, Bridges, Bets): Second Brain wiki, `bankers-bridges-bets`
- The finer version of layers 3 to 5: Second Brain wiki, `ad-grammar-structure-conceit-actor`
- Reading a new account: [[cs-client-onboarding-DRAFT]], stage 2
