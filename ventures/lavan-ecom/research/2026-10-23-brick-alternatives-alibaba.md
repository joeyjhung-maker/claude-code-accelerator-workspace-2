# Brick alternatives on Alibaba (2026-10-23)

Question: can we buy a Brick-style product from China and reposition it for another market?

Short answer: yes for the hardware, but the hardware is the easy half. The app is the product.

## What the Brick actually is
- A small plastic NFC puck. No battery. Tap your phone to lock chosen apps, tap again to unlock.
- All the logic lives in a free app. The puck is just a tag in a shell.
- Price: £49 on getbrick.com (UK), about $59 in the US. Brick Night (Bluetooth bedtime blocker) is £119.
- Claims on the site: "55,000+ 5-star reviews", survey of 3,500+ users, named one of TIME's Best Inventions of 2026. Their numbers, not ours.
- Five lifetime emergency unlocks, then you contact support. Shareable across a family.
- Sources: [getbrick.com](https://getbrick.com/), [Tom's Guide](https://www.tomsguide.com/phones/brick-review), [Apartment Therapy](https://apartmenttherapy.com/brick-app-review-37523373)

## Two ways to build an alternative

### A. NFC puck + a free app (closest to Brick)
Alibaba has the shell. Search "NFC focus device" and "magnetic app blocker".
- Fineplus Machining (Fujian, 1 yr on Alibaba, 5.0 store rating): "Custom Injection Molded NFC Focus Device Magnetic App Blocker". £0.75 at 1-999 pieces, £0.38 at 1,000+, £0.08 at 10,000+. MOQ 1. Custom logo, colour and packaging offered. They list six near-identical variants, one with "NFC chip magnet" embedded. [Listing](https://www.alibaba.com/product-detail/Custom-Injection-Molded-NFC-Focus-Device_1601801318238.html)
- Unverified: whether the price includes the NFC chip. They are a moulding shop, so ask for the shell with an NTAG213 inlay fitted.
- Loose tags if you want to skip the shell: NTAG213/215 stickers about £0.03-0.19 each at 500+ ([search](https://www.alibaba.com/trade/search?SearchText=ntag213+nfc+tag)).
- Keyword trap: "NFC blocker" mostly returns RFID wallet-shield cards. That is the opposite product. Search "NFC focus", "NFC tag app blocker", "digital detox NFC".

The app is the catch. We can't use Brick's. Options:
- Foqos: free iOS app, MIT licensed, iOS 16+, built to work with any NFC tag. [GitHub](https://github.com/awaseem/foqos)
- Lock: free Android app that works with any NFC tag, Android 14+. ([source](https://www.similarweb.com/zh-tw/app/google/com.nathanb.lock/))
- Competing brands already in market: Bloom (about $39 steel card, own app), Unpluq (about $27 tag plus a yearly subscription). [BGR](https://bgr.com/2235201/phone-blocking-app-brick-alternatives/)
- Sell the tag plus a setup guide for Foqos/Lock = easiest start, but customers do the setup and you own none of the app.
- Or commission a white-label app = the real moat, the real cost. Quote not gathered.
- Check before building on Foqos: Apple's Screen Time (Family Controls) entitlement for a published app. Not verified here.

### B. Timer lock box (not NFC, already sells on Alibaba)
No app, no setup. Phone goes in the box, box locks for a set time.
- Fuzhou Greathome: £3.78, MOQ 10, 487 sold
- Ningbo Rato Hardware: £3.01-3.69, MOQ 120, 1,938 sold, 12 yrs
- Hebei Shenghui: £4.91, MOQ 2, 814 sold
- Fuzhou Farway: £3.02-3.40, MOQ 1,000, "99 hours, 60 days battery"
- Shenzhen Union Electronics: £16.60-19.99, MOQ 2 (premium version)
- [Search](https://www.alibaba.com/trade/search?SearchText=digital+detox+phone+lock+box+timer)
- Sold counts show people already buy these. We have not checked Amazon retail prices or ad activity.

## Where to reposition (hypotheses, none validated)
Brick pitches adults who doomscroll. Everything below is a different buyer.
1. Parents of teens. Brick already works as a shared family device. A UK Mumsnet thread (Sept 2026) shows parents hunting for ways to limit phones before secondary school. No parental-control menu for a kid to find. [Mumsnet](https://www.mumsnet.com/talk/parenting/5575388-brickphones-for-y7-kids-any-cons-anyone-regretted-it)
2. Exam students (GCSE/A-level, JEE/NEET, uni finals). Timer boxes already move volume with this wording in their titles.
3. Sabbath / prayer / church groups. A "tap to unplug on Sunday" ritual. Group buys through churches. Fits your faith account.
4. Sleep. Brick Night costs £119. A £15 puck by the bed that blocks everything past 10pm undercuts it, though it will not be automatic.
5. Recovery (gambling, porn). Strong pain, very different ad rules.
6. Language gaps. Brick coverage exists in German, Arabic and Korean press. A local-language brand and app could take the same product to a market with no local player. Check whether Brick ships there first.

## Risks to check before money moves
- Brick patents or trademarks: not found in a quick search. Don't use the Brick name or lookalike branding. Search USPTO and UKIPO.
- Foqos and Lock were built by hobbyists. Support, updates and iOS changes are on us if we sell on top of them.
- Copycats get easy once one works. Moat = brand, angle, bundle, not the plastic.
- Cheap-tag quality: sample 10 pieces and test on iPhone 12-17 and Pixel/Samsung before ordering a run.

## Next steps
1. Message Fineplus and 2-3 timer-box suppliers. Ask: NTAG213 fitted, price per piece, sample cost, lead time, shipping to UK/US.
2. Order samples, tap-test with Foqos (iOS) and Lock (Android).
3. Pull Meta ads for Brick, Bloom and Unpluq (WinningHunter) to see which angles and markets already run.
4. Pick one market from the list above and write the angle.

Related: [[Lavan ecom project]] [[Supplier trace]] [[Purple ocean filter]]
