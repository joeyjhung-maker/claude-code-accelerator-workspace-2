# Workflow: Design mockup to PNG

Related: [[Promotion]]

First run 2026-10-14 (Locked Gifts opt-in for the CTO and Dan).

## When to use this
A page redesign that needs showing to someone: the CTO gets the live canvas, Dan gets PNGs.

## The steps
1. Look at the live page first (copy, image, button). Rebuild what's there. Offer extra sections instead of building them.
2. Mock it up in Claude Design (Artifact quickstart, intent "design"). Two directions, side by side, each with a colour picker.
3. Use the real photo. Edit the photo itself with Pillow when the callout needs to change (see [[2026-10-14-photo-callout-points-at-mechanism]]).
4. Before every change, re-read the canvas. Joey edits it by hand between rounds.
5. Export: read the latest artboards, then run `scripts/design_canvas_to_png.py` (headless Chrome, 2x, trims the empty space under the footer). Check the footer isn't clipped.
6. Save the PNGs and the photo to `creatives/YYYY-MM-DD-<name>/`. The canvas link stays private until Joey shares it.

## What good looks like
`creatives/2026-10-14-locked-gifts-optin/` and the canvas https://claude.ai/artifact/B2f33A2X6Adcr4f3rcgAGQ
