# RYZE timeline ad: the lifelong coffee drinker, three weeks (spec, v05, the "you" flip)

Date: 2026-10-07
Related: [[research]] [[TIMELINE_CoffeeLifer_Hypothetical_21Day_VIDEO_v01]] [[2026-10-03-video-ad-rules]]

*Spec ad for the Heuromi portfolio. Voiceover video, one piece. The frame is third person, then the body flips to "you" from Day 1, the way RYZE's own ads do. Mariobot wrote the flip. Markers in [brackets] are on-screen text. The first line has to be on screen at frame 0.*

---

A woman who never started a day without coffee replaced her first cup with RYZE Mushroom Coffee for three weeks.

The change was so quiet she almost missed it.

But wait until you hear what came out of her mouth on the last morning.

[DAY 1]

One spoon, hot water, ten seconds.

You take a sip and it's not your coffee.

It's earthy, a little odd, and there's no jolt behind it.

You think you've wasted your money.

You dump in your usual creamer and finish the cup out of stubbornness.

Nothing happens.

The only change so far is what's not in the cup, about half the caffeine you normally drink.

That's when things start to get interesting.

[DAY 3]

You reach for the bag before the coffee maker.

The taste has stopped being odd, and with your creamer it just tastes like your morning.

It's still real coffee, organic arabica, just with something extra in it.

You don't really think about it.

[WEEK 2]

Three o'clock comes and goes on a Tuesday and you only notice afterwards.

No second coffee.

Cordyceps, one of the six mushrooms in the blend, supports your body's natural energy production.

Friday evening you open the fridge and the Red Bull is still sitting in the door.

You're not sure when you stopped reaching for it.

This is the part you were waiting for.

[DAY 21]

You're sitting in the kitchen before anyone else is up.

Same mug, same chair, still your favorite ten minutes of the day.

This week your husband said you seem like your old self.

He couldn't say what was different.

And you go, "Same six hours of sleep I always get."

"It just doesn't feel like six."

Reishi supports calm, and mornings feel like they belong to you again.

You never quit coffee, because this is coffee.

The 3pm Red Bull and the wired feeling at night both came from one oversized caffeine hit in the morning.

All you did was change the size of that hit, one spoon, once a day, for 21 days.

Six mushrooms, 2,000mg per cup, organic and grown in the USA.

No sugar, 20 calories.

219,573 reviews and a 4.8 star average.

About 90 cents a cup.

Right now, your first bag is 40% off with a 30-day money-back guarantee.

Click below and try your first cup.

---

## Judge tick-list (v05, 2026-10-07)

- PASS: copy_lint, 0 fails.
- PASS: length. 384 words in one piece. The model ad is 378.
- PASS: the flip. Frame is word for word. No "she" or "her" left after Day 1. Every moment and the order are unchanged.
- NOTE: mariobot dropped "She didn't give anything up." It said the same thing as the next line.
- PASS: ceiling, momentum, proportion, moments, as v04.
- PASS: compliance. "Supports" only, no banned phrases, every number traces to research.md.
- FLAG: in "you", the seal now tells the viewer where her own 3pm Red Bull and wired nights come from. It is still a line about regular coffee, not RYZE, but it is more direct than it was in "she".
- FLAG: "your husband" assumes she has one. The model makes the same kind of assumption ("kids handled").
- OPEN: line 2 of the frame is still the one Joey picked. The hook rubric flagged it as tame (see v04). Alternatives below.

## Line 2 alternatives

(mariobot), lines 1 and 3 unchanged

- 2A: She almost sent the bag back after the first sip. (FAIL: not in the script, invented.)
- 2B: The first cup tasted so wrong she only finished it out of stubbornness.
- 2C: Day one, she was sure she'd wasted her money.
- 2D: She dumped in creamer just to get through the first cup.
- 2E: Her husband said she seemed like her old self and couldn't explain why. (FLAG: gives away the last stage.)
- 2F: The Red Bull in her fridge door went untouched and she never noticed when she stopped reaching for it. (FLAG: gives away week 2.)

2B and 2C fix the three fails at once: they are the charged true thing, they make a stranger react, and no other mushroom coffee ad would say them. Both set up the "But" in line 3.
