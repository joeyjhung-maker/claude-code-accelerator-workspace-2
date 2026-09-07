# KIE Render Reference (bank this — stop re-hunting endpoints)

One KIE key renders **statics AND video**. Don't fetch docs / web-search for endpoints every time — it's
all here. (Hard-won during a live render session; this is the thing to read before any render.)

## What one KIE key covers
- **Images:** gpt-image · nano-banana / Flux · Midjourney
- **Video:** Veo 3.1 · Kling 3.0 · Runway · Sora · Hailuo
- Veo endpoint: `https://api.kie.ai/api/v1/veo/generate` · docs: https://docs.kie.ai/veo3-api/generate-veo-3-video
- **Higgsfield is NOT on KIE** — it's a separate key, only for stylized video. KIE's Veo/Kling/Runway
  cover standard cinematic/UGC video.

## The gotchas (so calls stop 403/404-ing)
- **Browser User-Agent is REQUIRED on EVERY call** — upload, createTask, recordInfo, AND the final image
  download. KIE's WAF 403s Python's default UA. Send `User-Agent: Mozilla/5.0`.
- **Upload host:** `https://kieai.redpandaai.co/api/file-base64-upload` (NOT `api.kie.ai/...` → 404).
  Body: `{base64Data:"data:image/png;base64,…", uploadPath, fileName}` → returns `data.downloadUrl`.
- **Generate:** `POST https://api.kie.ai/api/v1/jobs/createTask`, Bearer auth, model
  `google/nano-banana-edit`, `input:{prompt, image_urls:[url], output_format:"png", aspect_ratio:"4:5"}`
  → `taskId`. (KIE pulls the reference from a URL — local files must be uploaded first, hence the upload
  step above.)
- **Poll:** `GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId=…` until `state=success`; the output URL
  is inside `data.resultJson → resultUrls`.
- **All wired in** `code/kie_render.py`: `python3 code/kie_render.py "<image>" "<prompt>" 4:5 <name>`.

## The disappearing-screenshot rule
Pasted screenshots only live in a macOS temp folder
(`/var/folders/.../TemporaryItems/NSIRD_screencaptureui_*/Screenshot….png`) that **self-purges within
seconds**, and the clipboard usually holds TIFF, not PNG — so "read the temp file later" and "pull from
clipboard" both fail. **Always save the reference to a stable path FIRST** (Cmd+Shift+4 → Desktop, or
`creative/refs/`), then render. If it's only in temp, an atomic find-and-copy of the newest
`Screenshot*.png` in `/var/folders` works **only with the sandbox disabled** — and it's a race against
the purge. Don't rely on it.

## Prompt craft — make it REAL and keep it STRONG
Image models default to making people pretty; fight that. Bake these into EVERY native render prompt:
- **Stack ultra-realism, don't say it once.** "ultra-realistic, photorealistic, real skin texture,
  visible pores, blemishes, slight redness, shot on an iPhone front camera, harsh indoor light, NOT AI,
  NOT rendered, NOT smooth, NOT airbrushed."
- **Force it to USE the reference, hard.** "Match the EXACT face shape, swelling and puffiness in the
  reference image. Keep the heavy water retention, bloated cheeks and swollen under-eyes — do NOT slim,
  beautify, or make him handsome."
- **Keep the angle STRONG — no holds barred.** "If anything, exaggerate the puffiness. Make him look
  unwell and swollen, not flattering." Don't let the model soften the visceral point.
- **Native / shareable cues.** "Looks like a real candid photo a regular guy posted to Facebook —
  boring, unflattering, true-to-life. NOT an ad, NOT a model, NOT a studio shot."
- **Negatives.** no smoothing, no symmetry, no glam, no studio lighting, no retouch, no perfect skin.
- **A named camera sells "a real person took this"** — "shot on an iPhone 13 front camera" /
  "point-and-shoot with direct flash" / "Canon 5D 50mm".
- **Reference image = the #1 quality lever.** Always upload one and tell the model to match it. Easiest
  source: Google Images **"reddit" + the topic** (or Pinterest / the Wild-sourcing folder).

### Strong native render — fill-in template
```
Ultra-realistic, photorealistic candid iPhone front-camera selfie of [SUBJECT]. Match the EXACT face
shape, swelling and puffiness of the reference image — keep the [puffy under-eyes / bloated cheeks /
soft jaw], do NOT slim or beautify. Real skin texture, visible pores, blemishes, slight redness, light
stubble. [Setting] under harsh overhead light, flat low-effort phone photo. Looks like a real unflattering
photo a regular guy posted to Facebook. NOT an ad, NOT a model, NOT studio, NOT smooth, NOT airbrushed,
NOT AI-looking. 4:5.
```

## Model selection — text-heavy vs photo (banked 2026-07-10, corrected 2026-09-01)
Which model matters as much as the prompt:
- **Text-heavy statics (screenshots, Notes app, texts, comments, search bars) → `nano-banana-2` (Pro).**
  The base model `google/nano-banana` garbles fine text — it duplicated a word ("chest chest tight") and
  invented junk UI labels ("Pladls / Blutn / Srams") on a Notes-app render. Re-running the exact same
  prompt on `nano-banana-2` came back clean and legible. Don't waste a render firing screenshot concepts
  at the base model.
- **Real model slug is `nano-banana-2` — no `google/` prefix.** Unlike base nano-banana, which IS
  `google/nano-banana`. `google/nano-banana-2` 422s ("model name not supported"). Confirmed against
  docs.kie.ai 2026-09-01 after the prefixed version failed live.
- **Param schema for `nano-banana-2` differs from base nano-banana too**: `aspect_ratio` (not
  `image_size`), reference images go in `image_input` (not `image_urls`). All three model families wired
  in this workspace now use different param names — see the schema table in `scripts/run_image.py`
  (`MODEL_SCHEMAS`) rather than re-deriving them by trial and error.
- Wired in `scripts/run_image.py`: `--nano-banana-2` flips to Pro with the correct schema; default is
  base nano-banana for photo work. `python3 scripts/run_image.py "<prompt>" --nano-banana-2 --out <path.png>`.

## gpt-image-2 — tested 2026-09-01, does NOT fix the small-text garbling
Same KIE key also serves OpenAI's model as `gpt-image-2-text-to-image` / `gpt-image-2-image-to-image`
(reference-guided uses `input_urls`, param is `aspect_ratio`). **Note: the i2i variant's docs list `4:5`
as an allowed `aspect_ratio` but it 422s live ("not within the range of allowed options") — use `auto`
or another value from the list and let KIE pick, don't trust the doc's list at face value.**

Ran a head-to-head against `nano-banana-2` on a real garbled specimen (a book-cover thumbnail whose
foreword line had come out as "AUTHOR OF MAKE 'EM BOG TO BUY FROM YOU" in production, should read
"BEG"). Same prompt, same reference image, both models:
- **Large-print text (the main subtitle band) — both models nailed it exactly**, no difference.
- **Small-print text (the foreword line) — `nano-banana-2` came back near-perfect** (one letter off:
  "BOG" for "BEG"). **`gpt-image-2` fabricated a different phrase entirely**: "AUTHOR OF MAKE TEN KGS TO
  BUY FROM YOU" — not a typo, a different sentence.

**Conclusion: gpt-image is not a fix for this failure mode, and on this test it's worse than what's
already in the pipeline.** The garbling is a small-text-at-scale limit that seems to hit every model in
this family, not a nano-banana-specific weakness. Don't burn more render credits chasing a model-swap
fix for tiny text — the reliable fix is to stop asking the image model to render small
headline/proof/foreword-scale text at all: render the base visual clean, then overlay that text
separately (Canva or similar) so it's never regenerated pixel-by-pixel. Large hero text (a headline,
a book title) is fine to bake in — both models render that correctly and consistently.

## Iterative edits — one fix per pass, not several (banked 2026-08-24)
A 9-render saga on a Flexxable static taught this the hard way: asking one edit pass to
fix multiple things at once (pose + text legibility + add a person) reliably fails —
each pass satisfies some instructions and silently drops or corrupts others (wrong
composition, garbled text reappearing, an added element vanishing). **Chain edits one
targeted fix at a time**, using the best prior output as the next `--ref`, and re-check
the WHOLE frame after each pass — "keep everything else unchanged" does not reliably
hold; a pass aimed at fixing text can quietly drift the room, add accessories, etc.
`--ref` + `--model nano-banana-2` together IS supported (undocumented elsewhere) — but
stacking the reference constraint with the text-quality model seems to raise the odds of
deviating from the reference vs. `--ref` alone. If a real reference photo is available
and 1-2 verbal-description attempts haven't matched it, stop re-describing and pass the
actual photo via `--ref` immediately rather than continuing to iterate blind.

## Plain-English explainer
We turn a winning ad's message into native-looking static images. Feed a real reference photo + a prompt
into an image model (KIE / nano-banana). Two things make or break it: **(a)** get the reference onto a
real file first (pasted screenshots vanish), and **(b)** write the prompt to force ultra-realism, match
the reference exactly, and keep the visceral angle strong. Render 4:5, native-to-feed, ~20% hit rate,
keep the winners → Loopback.
