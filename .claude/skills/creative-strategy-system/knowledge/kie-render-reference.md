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

## Model selection — text-heavy vs photo (banked 2026-07-10)
Which model matters as much as the prompt:
- **Text-heavy statics (screenshots, Notes app, texts, comments, search bars) → `nano-banana-2` (Pro).**
  The base model `google/nano-banana` garbles fine text — it duplicated a word ("chest chest tight") and
  invented junk UI labels ("Pladls / Blutn / Srams") on a Notes-app render. Re-running the exact same
  prompt on `nano-banana-2` came back clean and legible. Don't waste a render firing screenshot concepts
  at the base model.
- **`nano-banana-2` ignores `image_size` and defaults to 1:1.** 1:1 is feed-native so it's fine; if you
  specifically need 4:5 portrait, the param name differs for this model — sort it before relying on it.
- Wired in `scripts/run_image.py`: `--model nano-banana-2` flips to Pro; default is base for photo work.
  `python3 scripts/run_image.py "<prompt>" --model nano-banana-2 --out <path.png>`.

## Plain-English explainer
We turn a winning ad's message into native-looking static images. Feed a real reference photo + a prompt
into an image model (KIE / nano-banana). Two things make or break it: **(a)** get the reference onto a
real file first (pasted screenshots vanish), and **(b)** write the prompt to force ultra-realism, match
the reference exactly, and keep the visceral angle strong. Render 4:5, native-to-feed, ~20% hit rate,
keep the winners → Loopback.
