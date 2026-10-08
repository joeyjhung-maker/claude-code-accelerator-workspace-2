# Workflow: Pull a transcript from a video link (Zoom, Wistia, Vimeo)

Related: [[Promotion]] [[2026-09-25-dan-copy-correction-loop]]

Run four times in the Topa LinkedIn campaign (Sept to Oct 2026): one Zoom recording, one Wistia call, two Vimeo videos. Each platform needed a different method. This page is so the next pull takes one pass.

## When to use this
Joey sends a link to a recorded call or video and wants it reviewed, summarised, or turned into copy. YouTube and Facebook links have their own skills (`youtube-transcriber`, `facebook-transcriber`); this is for everything else.

## The steps
1. **Try the built-in browser first.** Open the link and read the page text.
2. **Use the method for the platform:**
   - **Zoom share link.** The recording page has an "Audio Transcript" panel. Decline the cookie banner, then read the page text. It comes back complete, with speaker names and timestamps.
   - **Wistia.** Reading the page text returns nothing, because the player keeps its content in a shadow DOM. Click the chapters/transcript icon in the player controls, then walk the shadow roots with a text TreeWalker (skip `style` and `script` nodes). The whole transcript is one long string with "Chapter <title>" markers and NO speaker labels. Find the chapter by searching the string, then slice by character position.
   - **Vimeo.** The built-in browser hits a Cloudflare "Verify you are human" check, which Claude must not complete. Use Joey's Chrome (Claude in Chrome): open the link in a new tab there, since his browser has already passed the check. Click the "Transcript" button under the video so the caption file loads. Do NOT scrape the transcript panel: it only renders about three rows at a time and scrolling it by script is unreliable. Instead, read `performance.getEntriesByType('resource')`, find the `captions.vimeo.com/captions/<id>.vtt` entry, fetch it inside the page and strip the cue numbers and timestamps.
3. **Get long text out of the page.** JavaScript return values get cut off at a few hundred characters, and any return value containing a URL with a query string is blocked. So: never return raw URLs (return host + path if needed), and for the transcript itself, write it into the page (`<main><pre>…</pre></main>` replacing the body) and read it back with the page-text tool, which returns the whole thing.
4. **Close any tab opened in Joey's Chrome** once the text is saved.
5. **Save it as source material**, in the relevant client or campaign `source/` folder, named `YYYY-MM-DD-who-what.md`. Header: the link, the date pulled, the length, whether there are speaker labels, and any obvious transcription errors (e.g. "Toca" = Topa, "royal" = ROYA, "school" = Skool). Then a short **key facts for copy** block (numbers, quotes, what is and isn't live), then the transcript verbatim. Raw material: never edit it afterwards.
6. **Check it before using it.** Compare every number and quote in the key-facts block against the transcript text, and flag anything that conflicts with copy already written or sent.

## If it's blocked
- If every browser and shell action fails with a "no verdict" safety-check error, that's a temporary outage on the checking service. Stop retrying, tell Joey, and try again a few minutes later.
- If the page needs a login or passcode, ask Joey. Don't try to get round it.
- Fallbacks to offer: the video owner downloads the caption file (Vimeo: Settings → Distribution → Subtitles → download the .vtt), or the Zoom cloud recording's own transcript.

## What good looks like
`clients/flexxable/campaigns/2026-09-topa-linkedin-automation/source/2026-10-linkedin-signals-dan-johnny-walkthrough.md` — full transcript, key facts on top, two conflicts with existing copy flagged the same day.
