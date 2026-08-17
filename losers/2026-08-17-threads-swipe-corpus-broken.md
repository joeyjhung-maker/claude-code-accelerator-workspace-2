# Died: the Threads swipe corpus — scraped wide instead of deep

*Diagnosed 2026-08-17 after Joey flagged the swipes were "all wrong and generated bad outputs".
He was right. Three structural breaks, one root cause.*

**What died:** `threads/swipe-file-1k-plus.csv` (80 posts) and the 565-post scrape behind it.
**What survives:** [[structure-bank]] Part 1 (#1–10). Those came from Joey's own 403-post archive
with real metrics. **Only Part 2 (#11–17) is affected.** Do not throw out the good half.

---

## Break 1 — no follower data, so nothing could be normalised

[[threads-growth-system-map]] line 31 sets the method: *"Normalise engagement per follower. A
300-like post from a 1K account is a better model than a 10K-like post from a 500K account."*

**528 of 530 scraped authors have no follower count.** The Apify `posts` mode does not return one —
only `profile` mode does, and that was run on a different, barely-overlapping set of 79 accounts
(15 populated, 2 of which overlap the post authors).

So the central normalisation step could never execute. The swipe file's own name is the tell:
`1k-plus` implies a follower floor that was only ever applied to **9 of 80 rows**.

## Break 2 — those 9 rows are the accounts we documented as poison

The 9 rows with real follower counts: adamgrant (2.8M), jeffnippard (4.1M), markmanson (2.2M).

[[2026-08-15-threads-data-mining]] says in bold: **"Do not scrape famous people."** With receipts —
Hormozi 4.9M followers / median 170 likes. Daily Stoic 3.5M / 31.

The one filter that did run selected for exactly what the play forbids. **4 of those 9 posts had
under 0.1% likes-per-follower** — they flopped for their size, and got banked as models.

## Break 3 — the fatal one: 1.07 posts per author

565 posts across **530 distinct authors**.

The method requires *top and median per account* — the map says the **delta between them is the
finding**, because top-only analysis just teaches you what all posts have in common.

With roughly one post per author there is no median. **The delta is not computable.** The corpus
was structurally incapable of answering the question it was built to answer.

## Plus the noise nobody filtered

- **213 of 565 posts (38%) are photo, video or carousel.** The image is doing the work; the text
  teaches nothing. "Leaning out and stuff, shoutout MacroFactor" — 4,225 likes on six words and a
  physique photo — is in the swipe file.
- **89 replies** — context-free fragments of conversations we can't see.
- **48 posts under six words.**
- 5 duplicate postIds across files.

---

## Root cause

**Broad keyword search across strangers, when the method needed deep sampling of a known few.**

Keyword search returns one post each from hundreds of accounts. That shape can never produce a
per-account median or a follower-normalised rate. The scrape design and the analysis design were
never compatible — and the mismatch was invisible until someone tried to use the output.

The corpus-health note at the bottom of the structure bank caught the *symptoms* (impersonation
accounts, non-English clusters, photos doing the work) and even said "treat these as leads, not
laws." What it missed is that the sampling shape itself was wrong.

---

## The fix — go deep, not wide

Do not re-run the broad search. Re-scrape **20 accounts properly** instead of 530 accounts badly.
The seed list already exists in `threads/seed-accounts-candidates.md`.

1. **`profile` mode over the 20 seeds** → follower counts. One cheap call.
2. **`posts` mode per username**, 30–50 posts each → ~600–1,000 posts with a real per-account
   distribution.
3. **Filter before analysis:** `mediaType == text`, drop `isReply`, drop under 6 words, dedupe on
   `postId`.
4. **Then compute the delta** — each account's top decile against its own median. That comparison
   is the whole point and has never once been run.

Same post volume, radically better data, and **cheaper** — 20 accounts instead of 530, well inside
the $10/month Apify ceiling.

## The lesson that generalises

**Check that the sampling shape can answer the question before you spend the credits.**

"Get lots of examples" is not a sampling design. The analysis needed a within-account comparison,
so the scrape had to be within-account. Nobody checked that the two matched, and the corpus looked
fine — 565 posts, real engagement numbers, plausible authors — right up until it was used.

Related: [[structure-bank]] [[threads-growth-system-map]] [[2026-08-15-threads-data-mining]] [[threads-README]]
