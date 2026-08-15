# Play: mining Threads for data and post structures

*First run 2026-08-15. Status: RUN ONCE — banked early because these are tool facts that cost real time and money to discover, not a process still being guessed at. Update after run two.*

Two jobs: (1) pull Joey's own posts + metrics, (2) scrape other people's posts to mine structures.
System spec: [[threads-growth-system-map]]. Output: [[structure-bank]].

---

## Job 1 — Joey's own posts: use the Threads API, not the website

- **The website is useless for this.** Both the profile feed and the Insights list hang after ~4 posts — the lazy-load spinner spins forever and no further page arrives. Scrolling harder does not fix it.
- **The API returns everything.** 403 posts in 6 pages, no problem.
- **No App Review needed** for your own account. Dev mode + adding yourself as a Threads Tester (and accepting the invite in Threads → Settings → Website permissions) is enough.
- **Metrics go back much further than the web UI implies.** The web view defaults to 30 days; the API served real numbers back to Nov 2025.
- Token is long-lived (60 days) straight from the User Token Generator — no short-lived exchange step, and **no app secret required** (it's only used for the OAuth flow, which the generator bypasses). Refresh with `GET /refresh_access_token` before it lapses or the whole setup has to be rebuilt.
- Credentials live in `.env` (gitignored). Homebrew Python has no SSL cert store — **use `curl` for the fetching**, Python only for parsing local files.

## Job 2 — Other people's posts: Apify

Actor: `automation-lab/threads-scraper`. Modes: `profile` (follower counts), `posts` (by username), `search` (by keyword).

### Three gotchas that each cost a run

**1. Threads search only matches short, natural terms.**
`sobriety` → results. `sobriety recovery one year` → **zero**. `money` → results. `money mindset wealth` → **zero**.
Ten constructed descriptive phrases returned 0 posts across the board and looked exactly like the scraper was broken. It wasn't. Use single words or real idioms people actually type.

**2. Do not scrape famous people.**
Verified on 15 big names: Hormozi 4.9M followers / **median 170 likes**. Dan Martell 3M / **52**. Daily Stoic 3.5M / **31**. The Budget Nista 682K / **19**. Dan Koe 1.76M / **420**.
Those follower counts are Instagram imports, not Threads audiences. Only Adam Grant (median 1,901) and Jeff Nippard (median 1,820) actually perform here.
**Scrape Threads-native accounts instead** — people who built the audience on this platform. A 3,222-like post on 2,233 followers (@natemlambo) is worth more than anything Hormozi posts.

**3. The sync endpoint times out at 300 seconds.**
`run-sync-get-dataset-items` returns HTTP 408 on anything over ~6 queries — but **the run keeps going server-side**. Don't re-run and pay twice. Start the run async, poll `/actor-runs/{id}`, then fetch the dataset. Aborting a run still lets you salvage everything collected so far.

### Cost
~$0.02 start fee per run plus roughly $0.003/post. A 10-query search at 30 posts each runs about $1. The free tier is $5/month. Set a hard spend limit in Apify billing.

---

## Analysis rules

**Rank by engagement rate, not views.** Joey's biggest post by views (354,177) has a **0.05% engagement rate** — it was pushed to an audience that didn't care, and it alone is 55% of his lifetime views. Sorted by views it tops every list and teaches nothing. His genuinely best posts sit at 11–17% on 500–2,000 views.

**Normalise by follower count.** Likes-per-follower points somewhere completely different from raw likes, and it's the only version that identifies structures a small account can actually reproduce.

**Pull a median sample, not just top performers.** Top-only analysis teaches you what *all* posts share (line breaks, short sentences), not what wins. The gap between top and median is the finding.

**Expect a dirty corpus.** Keyword search surfaces impersonation accounts farming engagement (fake Stallone, fake Tyler Perry, fake Eminem), large non-English clusters, and one-word hashtag posts. Filter on: non-Latin script ratio, impersonation keywords in the username, and posts under six words.

## Next run — do differently
- Skip keyword search for account discovery; it surfaces whoever ranks, which is how the fake celebrities got in. Target named accounts directly.
- Build the seed list from Threads-native practitioners, then verify with `profile` mode before spending on `posts`.
- Profile-check authors *as* they're harvested, so follower counts aren't missing from the final file.

Related: [[Promotion]] [[threads-growth-system-map]] [[structure-bank]] [[2026-08-15-unglamorous-absolute-threads]]
