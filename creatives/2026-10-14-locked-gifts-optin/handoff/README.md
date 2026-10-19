# Locked Gifts opt-in: two variants for a split test

Dan approved both. They replace the hero on https://docs.flexxable.com/locked-gifts and run 50/50.

## What's here
- `variant-a-dark.html`: dark, yellow accent.
- `variant-b-light.html`: light, blue button, yellow highlights.
- `img/`: Dan hero photo (`dan-its-locked.jpg`, replaces `optin-dan.jpg`) plus the four locked-gift product shots from b2bgifts.ai.
- `preview-a-dark.png`, `preview-b-light.png`: full-page desktop screenshots.

These are static design files: inline styles, Google Fonts, no JavaScript. Every link and button is `href="#"`. Treat them as the visual spec. Restyle or refactor as you like, but keep the copy and the order.

## Wiring to do (it's all already on the live page)
- **"Get the free guide now"** opens the existing sign-up popup. Same form, same `/locked-gifts/optin` call, same redirect to `/locked-gifts/part-1`. On the live page that's `id="open"`.
- **The photo** opens the popup too, like `id="peek"` does on the live page.
- **The existing tracking** (UTMs, `lg_vid`, `/locked-gifts/t` beacons) should stay as it is.
- **Record which variant each visitor saw** (a / b) on the page-view beacon and the opt-in, so conversion can be compared by variant. Keep the same visitor on the same variant when they come back.
- **Footer and consent links** (Privacy Policy, Terms, Disclaimer) need real URLs.
- **Cookie consent**, if the Meta pixel or any other tracking cookie runs on this page (UK/EU).

## Page order (both variants)
Logo → audience line → headline → subhead → Dan photo with three locked gifts pinned to it (photo + gifts open the popup) → "every one arrives locked" pill → 4 benefit bullets → **350M+ Leads free-gift box** (Dan wants this prominent) → button → consent line → footer.

## Notes
- Copy is final. Joey and Dan signed it off, so please don't reword it.
- On B, the audience line ("FOR AGENCIES, CONSULTANTS, B2B SALES PEEPS:") is left-aligned on purpose. On phones it's the only left-aligned line, so ask Joey if it looks off.
- Checked at 375px and 1440px wide: no sideways scroll.
- Text sizes change with screen width on purpose (the `clamp()` font sizes: bullets 18→23px, gift line 18→22px, subhead 22→30px). Keep them fluid; don't swap them for fixed sizes.
- Live design canvas (comments welcome): https://claude.ai/artifact/B2f33A2X6Adcr4f3rcgAGQ
