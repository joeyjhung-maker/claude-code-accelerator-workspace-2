# B2B Leads Lab — DFY Beta onboarding sequence (SHIPPED, live)

*2026-08-26. Written as Dan Wardrope, drafted via mariobot on `clients/flexxable-primers/b2b-leads-lab-body.md`, judged against `rubrics/copy-rubric.md` before reaching Joey. Sequence: waitlist signup → Email 1 (application) → Google Form (live) → Dan shortlists → Email 2 ("you're in").*

Related: [[b2b-leads-lab-project]] [[copy-rubric]] [[2026-08-25-b2b-leads-lab-dfy-beta-waitlist-landing-page-FINAL]]

**Full funnel, as it stands 2026-08-26:** landing page signup → Email 1 (application) →
Google Form (live) → Dan reviews and shortlists → Email 2 ("you're in") to the 10, OR the
rejection email below to everyone else.

## Live assets
- **Google Form (live):** https://docs.google.com/forms/d/e/1FAIpQLSd62Tm0yb9hodCjAGeHhmW_vbYuDdoJEhcY4ywJh_SEX0YHhw/viewform
- **Response sheet (in the B2B Gifts Drive folder):** https://docs.google.com/spreadsheets/d/16jtpECGku8urmVPIKr6IFcSU20Z3eUhBuXn-KaZSwH0/edit — note: once the Form's Responses tab is linked to this spreadsheet, Forms creates its own tab (usually "Form Responses 1") with headers pulled from the actual question text, separate from the pre-built header row. That's expected.

## Judge notes
- Original mariobot draft for Email 1 opened "Yo, you're in" — a real accuracy problem, not just a
  voice miss: this email fires BEFORE shortlisting, so telling someone they're "in" contradicts
  the entire point of the vetting step. Rewritten to the established "Hey, it's Dan here…" opener
  and corrected to confirm only that they're on the waitlist.
- Email 2 (the original draft, written before the vetting step was added) used the banned word
  "onboard" ("ready to onboard you") — hard rule violation (Script bans leverage/solution/
  deliverable/onboarding). Fixed to "bring you into the beta." Also caught "DFY fulfilment beta"
  leaking internal shorthand the reader was never introduced to — trimmed to "the fulfilment
  beta."
- Both emails: 0 FAIL on `scripts/copy_lint.py`. No invented facts — Sept 15 date is hedged
  ("aiming," "around," "the target, not a blood oath") per the established honest-beta framing.

---

## Email 1 — Waitlist confirmation + application

**Fires:** immediately on waitlist signup from the landing page.

**Subject line:** You're on the list - one quick thing

Hey, it's Dan here…

Thanks for putting your name down for the fulfilment beta.

Quick heads up on how this works…

There are only 10 beta spots.

And they're not first-come-first-served.

I'm hand-picking the 10 from the applications that come in.

Not to be precious about it… it's actually better for YOU this way.

Getting picked for something you're not ready for is probably worse than a 2-minute form.

So there's a short application.

Takes about 2 minutes, nothing crazy.

Just enough so I can figure out who's the right fit and who'll actually get results from this.

[Fill Out The Application](https://docs.google.com/forms/d/e/1FAIpQLSd62Tm0yb9hodCjAGeHhmW_vbYuDdoJEhcY4ywJh_SEX0YHhw/viewform)

Once I've gone through the responses, I'll let ya know if you're one of the 10.

Rooting for ya,

Dan

---

## Application form (13 questions, live)

Full field-by-field spec with exact copy: `b2b-beta-application-form.md` (scratchpad, superseded
by the live form itself — the live link above is the source of truth now).

Screening order: contact info → UK/budget/volume disqualifiers → niche/service/client-status →
readiness (Dream 100 list started) → motivation (open text) → beta-honesty acknowledgment.

---

## Email 2 — "You're in" (sent only to the shortlisted 10, after Dan reviews applications)

**Subject line:** You're in - here's what to knock out while you wait

Hey, it's Dan here…

Just wanted to say welcome… and thanks for putting your name down for the fulfilment beta.

This isn't one of those "thanks for signing up!" autoresponders that goes nowhere.

We're actually building this thing out right now, and you're gonna be one of the first people through the door.

We're aiming to start fulfilling shipments around the 15th of September.

That's the target, not a blood oath… first time running the beta so I wanna make sure everything's dialled in before we start posting bottles on your behalf.

But that doesn't mean you should just sit around waiting.

There's a few things you can get sorted NOW so you're ready to rock the second we flip the switch:

**1.** Go through the B2B Leads Masterclass in the Skool classroom… the whole thing, not just the bits that look fun.

**2.** Start building your Dream 100 list - follow Step 3 in the SOP doc. This is the part most people skip and then wonder why their first batch goes out to randoms who were never gonna buy.

**3.** Sign up for Topa if you haven't already: https://b2bgifts.ai/

**4.** Start working on your leads and your letter now. When we bring you into the beta, I want you locked and loaded… not scrambling to figure out who you're even sending to.

I'll shoot you another email as soon as we're ready to bring you in.

Until then, get stuck into that checklist.

Rooting for ya,
Dan

---

## Email 3 — Rejection / not selected

**Fires:** manually, sent by Dan to applicants who don't make the shortlisted 10.

**Subject: your beta application**

Hey,

Wanted to send this personally because you took the time to apply, and that deserves a straight answer from me.

You didn't make the 10 this round.

Not because your application was weak or your business isn't a fit.

We only had 10 spots because this is the first time Jonathan's team is running fulfilment this way, and that's genuinely all they can handle while we figure out what works and what doesn't.

Narrowing it down to 10 when the constraint is just capacity… it's a rough cut no matter how you slice it.

So I don't want you reading this as some kind of verdict on you or where your business is at, because it isn't that.

Now the bit that actually matters…

Everything inside B2B Leads Lab still works exactly the same whether you're in the beta or not.

The masterclass, building your Dream 100 list, writing the letter, buying a bottle and sending it yourself… that's the SAME system we're using.

The only difference with the beta is someone else handles the physical sending part for you.

That's it.

So if you've been waiting on this to get started… don't.

Grab a bottle, write the letter, send it to someone on your Dream 100 and see what happens.

The system doesn't need the beta to work.

And look, if this first run proves out and we expand capacity down the line, you'll be one of the first to hear about it.

I'm not gonna promise you a spot or a date because I genuinely don't know yet… but I'll keep you posted either way.

Rooting for ya,
Dan

*Judge note: deliberately doesn't promise a guaranteed next round or a specific date — not
confirmed. Redirects straight into the DIY path rather than leaving the reader stuck. Original
mariobot draft included "A LOT of people applied" — cut as an unverifiable claim about future
application volume this template can't actually know at send time.*

---

## Still open
- Whether a "No" on UK/budget/volume questions should branch the Google Form to an early exit
  message, or just get filtered manually when Dan reviews responses — not decided.
- The actual landing-page signup mechanism that triggers Email 1 isn't built yet — that's
  Jonathan's/Joey's 27 Aug deadline (Key Dates item 2). This whole sequence needs to be handed to
  Jonathan so he can wire it into the real page/autoresponder build.
