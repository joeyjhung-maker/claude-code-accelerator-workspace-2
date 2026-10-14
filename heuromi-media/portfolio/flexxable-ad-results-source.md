# Flexxable ad results: the numbers behind the CV, and how they were measured

*Saved 2026-10-14 so the method isn't lost again. The original analysis was done in a Claude session on 2026-10-05, reading Meta Ads Manager (Flexxable Growth account, 837452716631540) read-only in Joey's Chrome.*

Related: [[2026-10-05-cv-intro-options-MARIOBOT]]

## The CV claim and what backs it

> My 16 concepts since June have produced 540+ purchases at about 20% lower cost per purchase than the rest of the account.

| Period | Joey's ads | Everything else |
|---|---|---|
| June | £19,780, 209 purchases, £94.64 | £5,058, 41 purchases, £123.37 |
| July | £9,715, 112 purchases, £86.74 | £14,244, 117 purchases, £121.74 |
| 1 Aug to 4 Oct | £23,408, 223 purchases, £104.97 | £36,853, 292 purchases, £126.21 |
| **Total** | **£52,903, 544 purchases, £97.25** | **£56,155, 450 purchases, £124.79** |

22% cheaper overall; Joey's ads beat the rest in every period.

## How it was measured (use the same method to update it)

- **Cold traffic only, like for like.** June: Joey's ad sets against the other ad sets in the TESTING campaign. July: ad-level, campaign total minus Joey's identified ads. 1 Aug onwards: inside the "2026-06-30 | Scaling | Best Ads | Broad" ad set, the only one spending then.
- **Excluded:** the Retargeting campaign, June's separate SCALING campaign (£6,580, 54 purchases), and £1,207 of June spend that couldn't be attributed.
- **Joey's ads were identified by name** from the concept docs in his Drive folder (https://drive.google.com/drive/folders/1Sdqbi_3lU5OsJiK_deKjCOHuo_1NdxpN), one concept a week from 8 June to 28 September.
- A whole-account comparison (all sales campaigns, retargeting included) gives a smaller gap, because retargeting runs at about £62 per purchase. Don't mix the two methods.

## Joey's concepts (as matched in Ads Manager)

June ad sets: Renting AI Employees, Agency Owner Paid Like Employees, Concept 2024 Book, Performance AI (incl. "9-5ers paycheck").
From August, in the scaling ad set (1 Aug to 4 Oct):

| Concept | Spend | Purchases | Cost per purchase |
|---|---|---|---|
| Make Money With AI System | £4,378 | 41 | £106.77 |
| Renting Androids / Performance Employees | £4,278 | 40 | £106.96 |
| Old Agency Models | £3,446 | 33 | £104.43 |
| No Ad Spend ("Weird Campaign") | £2,865 | 32 | £89.52 |
| Sales Bros Are Dead | £2,623 | 21 | £124.89 |
| Whiskey Bottle | £1,895 | 11 | £172.24 |
| BOFU Ads | £1,327 | 15 | £88.44 |
| Bogged Down By Delivery | £856 | 11 | £77.80 |
| Biz Op Mass Market | £845 | 10 | £84.52 |
| 1 vs 10 Clients | £640 | 9 | £71.13 |
| 48 Hour Android | £256 | 0 | no sales |

Not yet spending as of 4 Oct: Retainer Lie, Against Building, Hedge Fund (for 9-5ers).

## Other checked claims

- **"6 of the account's top 10 ads by spend"**: Joey's ads ranked 5th to 10th (1 Aug onwards); the top four are older ads that aren't his. Re-checked 2026-10-14: positions 5 to 7 for 1 Aug to 14 Oct are his.
- **"4 of my 5 biggest concepts beat the account's average cost per purchase"**: holds.
- **"Account's top spender in June"** (Agency Owner Paid Like Employees, £4,391 in June): confirmed 2026-10-14.
- Ads Manager screenshots from 2026-10-14 are in ~/Downloads/cs-job-scout/proof/.

## Re-pulled 2026-10-14 (1 Jun to 14 Oct), with screenshots

A simpler, screenshot-able version of the same cold-traffic method: TESTING campaign only (id 120237498924300609), ad level, one ad-name filter for all of Joey's concepts (Agency Owner Paid, Weird Campaign, Renting AI, Renting Android, Performance AI, Performance Employee, Whiskey, Whiseky, Old Agency, Make Money With AI, BOFU, Concept 2024, 9-5ers, Sales Bros, Bogged, Biz Op, 1 vs 10, 48 Hour, Retainer Lie, Against Building).

- Joey's ads: £52,396.81, 543 purchases, £96.50
- All TESTING ads: £115,832.60, 1,058 purchases, £109.48
- Everything else: £63,435.79, 515 purchases, £123.18 → Joey's 22% cheaper; 45% of spend, 51% of purchases
- Same filter to 4 Oct gives £50,371 / 506 (the 5 Oct analysis found £52,903 / 544 by ad-set and date matching; the name filter is slightly conservative).
- Since 1 Aug (to 14 Oct) Joey's ads are 5th, 6th and 7th by spend; "6 of the top 10" was true at 4 Oct only.

Screenshots and the proof PDF (headline stats, ROAS note, every number with its Ads Manager screenshot, links to each ad in Drive): heuromi-media/portfolio/meta-results-proof/.
