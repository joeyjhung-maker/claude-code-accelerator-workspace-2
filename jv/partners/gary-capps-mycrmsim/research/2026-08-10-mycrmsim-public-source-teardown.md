# myCRMSIM — public-source teardown (2026-08-10)

Pulled from public sources only. **Nothing here is cleared for reuse in copy** — it's their own marketing claims, not proof Joey has approved to repeat. Confirm with Gary before quoting any number.

Sources: [mycrmsim.com/about](https://mycrmsim.com/about), [mycrmsim.com/pricing](https://mycrmsim.com/pricing), [YouTube — Gary Capps on Scaling SaaS, Automating SMS & Staying Fit at 50, Ep 58 #ghl](https://www.youtube.com/watch?v=xogubnYKocs), [LinkedIn](https://www.linkedin.com/in/garycapps/) (blocked — login wall, nothing pulled), [Apple Podcasts interview](https://podcasts.apple.com/us/podcast/my-interview-with-gary-capps-founder-of-mycrmsim/id1492600749?i=1000717770663) (fetch failed — page didn't return usable content).

## What myCRMSIM is
Connects a business's own phone + SIM card directly to their CRM, so SMS/iMessage/WhatsApp/RCS go out looking like a real human texting — not a bulk campaign. The pitch is entirely against the traditional SMS-API model (Twilio, A2P 10DLC registration):
- No A2P 10DLC registration (weeks of approval, campaign rejection risk) — the core wedge.
- Fixed monthly cost per line/SIM instead of usage-based billing.
- 4 channels: SMS (Android, unlimited), iMessage (iPhone, 50 unique contacts/day, "3–6x higher engagement," blue bubble), WhatsApp (any phone, unlimited, 3B+ users), RCS (Android, unlimited, rich media).
- Built-in AI agents inside the CRM that auto-qualify leads, book appointments, run follow-up sequences off inbound replies — positioned as no-code automation on top of the messaging layer.
- CRM integrations: GoHighLevel (appears to be the primary/home ecosystem — YouTube tag is `#ghl`), HubSpot, Salesforce, Zoho, Make, Zapier.

## Who it's for (their own segmentation, from pricing page)
- **Messaging businesses / agencies** — resell unlimited messaging to their own clients, "full margin control." This reads as the core ICP — an agency/reseller audience, not end-consumer.
- Sales teams (faster lead follow-up)
- Customer support teams (unlimited conversations, fixed cost)
- Marketing teams (campaign deliverability, avoiding spam filters)

This is the same shape of audience as BotBuilders (`jv/partners/matt-leitz-botbuilders/`) — people selling tools/services to businesses, GHL-adjacent, agency-owner mindset. Worth flagging to Joey before locking an angle: **overlap risk between Gary's audience and BotBuilders' audience** if both JV legs run book/ROYA pitches into a similar list at the same time.

## Pricing (public, as of 2026-08-10)
- SMS: $970/year ($80.83/mo) or presumably a monthly option — up to 10 sub-accounts, unlimited SMS via own SIM.
- iMessage / WhatsApp / RCS: $290/line/year ($24.17/line/mo), $29/mo for 1–10 lines, drops to $15.83/line/mo at 11+ lines.
- 30-day money-back guarantee, stated on both /about and /pricing.
- Comparison table positions against Twilio, WhatsApp API, Google RCS API, Apple Messages for Business — cost-at-scale and setup-time (5 min vs weeks) are the two hammered wedges.

## Proof claims (public, unverified/uncleared)
- "10,000+ business owners," "30+ countries served," "hundreds of members" in their Facebook group.
- "Cut their SMS costs by 90%" (homepage CTA line — exact wording, not independently confirmed).
- Named reviewers with titles (Joseph Robertson – ops manager, nationalbrokersgroup.net; Ahmed – CEO, Rocket Launch Media; John Bellamy – Founder, Chat To Clients; several more names with no title shown) — 5.0 rating displayed, but the actual review text wasn't visible in the page pull.

## Gary Capps — founder
- Background: Engineering, Digital Marketing, AWS (per team page).
- Founder quote: "We're not just saving businesses money — we're giving them back the ability to actually reach their clients' customers. That's the real mission."
- Founded 2023, HQ Australia.
- YouTube (Ep 58 of "Marketing Funnelz with Nipun Syal," 3 months old at time of pull): episode description reads "He removed AI from customer support — and his churn dropped" — a real story beat worth chasing if it's true and Gary confirms it (potential hook material, needs verification, not to be used until confirmed).
- LinkedIn profile didn't load (auth wall) — no bio pulled. Podcast episode page also didn't return content — needs a different fetch method or Joey to share the audio/transcript directly if it matters.

## Voice, from the site copy
Direct, problem-agitate-solve, plain B2B SaaS register — not hype-heavy. Repeated structure: "Stop waiting. Stop paying. Start messaging." / "Say Goodbye to Expensive Third-Party Services." Leans on specificity (registration timelines, dollar comparisons) over adjectives. No jargon beyond category terms (A2P, 10DLC, blue bubble) that the target ICP (agency owners already in the CRM/GHL space) would already know.

## Case studies — CLEARED (his own published proof, mycrmsim.com/case-studies)
Per Joey (2026-08-10): proof Gary is already running in his own marketing is cleared for our use. All of the below is verbatim/paraphrased from his live case-studies page — his own named customers, his own numbers.

**Site-wide aggregate stats (headline banner):** 6x reply-rate increase · 90% conversion rate · $1K/month average savings · 5 min average setup.

**Directly DBR-relevant (closest to Flexxable's own mechanism):**
- **Kristy Goodwin — Attn Seekr (real estate, regional Australia):** helps agents turn big databases into leads. "One client saw 86 appraisals, 7 listings, and $125K in GCI in around 100 days." This is a near-identical DBR story to Flexxable's own pitch — strong hero-number candidate.
- **Jayme Richardson (gym niche):** saved $1,000/month that used to go to a VA just managing Twilio/A2P setup. Client accounts now stood up "within the hour instead of days" — "bringing in results for gym owner clients almost immediately with database reactivations."
- **Kelvin Holliday — Productivity Hub:** 90% conversion rate and +30% MRR using his own "10×10 sales strategy" combined with myCRMSIM, for client onboarding.

**International / can't-get-a-number angle (validates shark #3):**
- **Jon Jamati — DDC Coaching (NZ):** was stuck on email/Facebook Messenger because NZ text-messaging restrictions blocked him from SMS entirely. Now closes leads automatically via SMS. Direct quote: "Text messaging restrictions in NZ had me stuck with email and Facebook Messenger. Now I'm closing leads automatically through SMS. Game changer."
- **Jackson Chen — ACR 365 (gym niche, Saaspreneur award winner):** 250+ subaccounts, zero physical phones on-site, including clients in New Zealand "where they can't even get numbers to do SMS from."
- **Jeremy Adelaide (early customer #2, pre-launch):** runs Vietnamese eSIMs from Australia, no roaming fees, $10/month at the time. "7 minutes from unboxing a phone to sending an SMS."
- **Sukumar Gudalore — Whiz Rock:** sends AU → NZ using a local number, zero roaming fees.

**Deliverability / blue-bubble angle (validates shark #2):**
- **Georgios Roros — Volume Up (roofing/home services):** switched green-bubble SMS to iMessage, 4-5x higher response rates on follow-ups, $1,500/month saved vs Twilio.
- **Jonathan Ferrell (lead gen):** client's reply rate went from 5% (Twilio green bubble) to 30%+ (myCRMSIM iMessage) — same ads, same leads, 6x increase. Quote: "If you're still using green bubble texts, you're leaving money on the table."

**Cost/setup-speed angle (validates shark #1):**
- **Daniel Sharifi — Score Media (construction/earthworks lead gen):** switched to RCS, eliminated Twilio cost entirely, near-zero manual follow-up work.
- **Jackson Chen — ACR 365 (WhatsApp):** 20 WhatsApp devices connected, centralized team communication and automated lead follow-up.

## Pricing history note
A 2-year-old YouTube video ("Unlimited SMS for $10/Month? Gary Capps Explains myCRMSIM," Ryan Builds Stuff on GHL) shows an original ~$10/month price point — this matches Jeremy Adelaide's early-customer case study above. **Current live pricing is $970/yr (~$80.83/mo) for SMS, $290/line/yr for iMessage/WhatsApp/RCS** — the $10/mo figure is historical/launch pricing, not current. Don't use it as a live price claim.

## Gary's own positioning (from podcast search results)
Across multiple podcast appearances (The Lead King, Pivot 2 Thrive Ep. 109, The HighLevel Experience, Qualified/CloseBot), Gary is consistently described as: an Australian entrepreneur and six-figure agency owner himself before building myCRMSIM; known in the GoHighLevel community for "generosity, consistency, and solving a very specific problem exceptionally well"; positions through free education (database reactivation strategies, compliance/opt-in guidance, "text like a human not a bot") rather than aggressive marketing. Full transcripts weren't fetchable (podcast pages only return episode-announcement text, not transcripts) — if a specific quote or number matters, the audio itself would need to be pulled.

## The "restricted countries" angle — market context (2026-08-10)
Joey's read: lots of Flexxable members in NZ believe they can't run DBR there. Confirmed true by two of Gary's own case studies (Jon Jamati/DDC Coaching and Jackson Chen/ACR 365, both above) — NZ carrier restrictions blocked standard SMS for them, myCRMSIM's own-device/SIM model (not carrier-registered bulk traffic) got them sending anyway.

This isn't NZ-only — it's a growing pattern worth widening the webinar's net around, per general industry sources (not Gary/myCRMSIM-specific, general market research):
- **Australia** just stood up a government-run Sender ID Register (ACMA), live **1 July 2026** — brand new, a month old at time of writing.
- **US/Canada**: unregistered A2P long-code traffic has been blocked by every major carrier since Feb 2025; Canada's CASL is one of the strictest anti-spam regimes globally.
- **India**: requires DLT (entity + sender-ID) registration before any A2P SMS.
- **Vietnam, Thailand, Bangladesh, Rwanda, Uganda, Japan**: standard A2P channels don't support inbound replies at all — which would kill a DBR play specifically, since the model depends on the lead replying.

**Caution:** Gary's case studies only directly confirm the fix works in NZ, and for AU→NZ / Vietnam-eSIM-in-Australia cross-border sending. The mechanism (own device + SIM instead of carrier-registered bulk traffic) should logically sidestep most of the above, but that's inference, not a confirmed case study — don't claim it's proven everywhere without Gary confirming which markets he's actually seen it work in.

Sources (general market research, not myCRMSIM-specific): [SMS Regulations by Country: Global Compliance Guide 2026](https://www.telerivet.com/blog/sms-compliance-by-country-global-guide?hs_amp=true), [10DLC Registration & Compliance Guide 2026](https://textbolt.com/blog/10dlc-compliance/), [SMS compliance in 2026](https://telnyx.com/resources/sms-compliance), [International SMS Compliance Guide — Telnyx](https://developers.telnyx.com/docs/messaging/messages/international-sms-compliance), [What Is A2P 10DLC and How to Get Registered in 2026](https://www.quo.com/blog/what-is-a2p-10dlc/), [10DLC Compliance Guide 2026](https://messageiq.io/blogs/10dlc-registration-sms-compliance/), [A2P 10DLC Compliance in 2026 — Apten](https://www.apten.ai/blog/a2p-dlc-compliance-2026).

## Open — needs Gary or Joey, not inferable from the public site
- Deal direction: which leg runs first (myCRMSIM → our list, or IAA book/ROYA → Gary's list, or both)?
- Actual list size / audience makeup Gary would send to (his Facebook community, email list, YouTube, or all three?)
- Any proof Gary has personally cleared for us to use (the "90%" stat, the churn story, specific customer names)
- Approval process — who signs off before anything goes to his list
- His personal voice on his own channels (this teardown is his company's SaaS site copy, not necessarily how Gary himself talks/writes)
