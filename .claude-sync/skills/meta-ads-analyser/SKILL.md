---
name: meta-ads-analyser
description: Analyze extracted Meta ad creatives and generate a professional strategy report. Use after /meta_ads_extractor to produce a clean, organized analysis document with inline videos/images grouped by funnel/landing page.
---

# Meta Ads Analyser

Generate a professional ad strategy analysis report from extracted Meta ad creatives.

## Prerequisites

- Extracted ad assets from `/meta_ads_extractor` (images, videos, landing page screenshots)
- Ad creative analysis (hooks, scripts, emotions, CTAs, strengths/weaknesses)
- Landing page analysis (headlines, strategies, conversion flows)

## Input

Assets folder from extraction, typically at:
```
~/clawd/output/meta-ads/{advertiser-slug}/
├── {slug}-video-01.mp4
├── {slug}-video-02.mp4
├── {slug}-image-01.jpg
├── {slug}-image-02.jpg
├── landing-{page-name}.jpg
└── ...
```

## Analysis Process

### 1. Analyze Each Creative

For each ad creative, identify:
- **Aspect Ratio** — Dimensions and ratio (1:1, 4:5, 9:16, 16:9)
- **Duration** — For videos, length in seconds
- **Hook** — Opening line/visual that stops the scroll, classified by type (call-out, contrarian, proof-first, curiosity gap, bold claim, demonstration, story open)
- **Awareness Stage** — Who the ad targets: unaware / problem-aware / solution-aware / product-aware / most-aware (inferred from whether it leads with story, pain, mechanism, proof, or offer)
- **Angle & Mechanism** — The desire/pain slice the ad enters through; any named unique method/system
- **Script/Copy** — Key messaging and value proposition
- **Visual Flow** — Sequence of scenes/elements (for video); native/lo-fi vs produced
- **Emotion** — Primary emotional trigger (curiosity, fear, aspiration, etc.)
- **Proof & Objections** — Proof elements used; objections pre-empted
- **CTA** — Call to action and friction level
- **Strengths** — What works well
- **Weaknesses/Gaps** — What could be improved

Use vision model for images, Gemini for video analysis. For deeper per-creative breakdowns, use the full prompts in the **ad-creative-analysis** skill (`references/prompts.md`) — they share this framework.

**Get dimensions with:**
```bash
# Images (macOS)
sips -g pixelWidth -g pixelHeight image.jpg

# Videos
ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 video.mp4
```

**Common aspect ratios:**
| Ratio | Use Case |
|-------|----------|
| 1:1 | Feed (universal) |
| 4:5 | Feed (recommended) |
| 9:16 | Stories/Reels |
| 16:9 | Landscape video |

### 2. Analyze Landing Pages

For each landing page, identify:
- **Headline** — Primary value proposition
- **Strategy** — Key conversion elements (social proof, urgency, etc.)
- **Conversion Flow** — Path from landing to purchase/signup
- **Strengths** — What converts well
- **Gaps** — Missing elements or friction points

### 3. Map Funnels

Group ads by their destination landing page. Each funnel = landing page + all ads driving to it.

Typical funnel types:
- **TOFU (Top of Funnel)** — Awareness, lead magnets, quizzes, free content
- **BOFU (Bottom of Funnel)** — Direct offer, application, purchase

### 4. Identify Strategy Patterns

Look for:
- **Angle map** — every distinct angle/mechanism across the ads; which angles get the most variants (advertisers iterate on winners — variant count is a proxy for performance)
- **Longevity signals** — if ad start dates are available, flag the longest-running ads as likely verified winners
- **Awareness coverage** — which stages they target and with which formats; concentration reveals where their volume comes from
- Credibility stacking (logos, credentials, social proof)
- Price anchoring
- Native creative (ads that don't look like ads)
- Identity-driven copy
- Testing patterns — distinguish true tests (one variable changed: hook swap on same body) from different concepts
- **Whitespace** — credible angles, stages, or formats they're NOT running (the openings for competing against them)

## Output Format

Generate a self-contained HTML report using the template structure below.

### Report Structure

```
1. Header
   - Advertiser name
   - Stats (# ads, # funnels, date)

2. Strategy Overview (TOP)
   - High-level acquisition strategy
   - Funnel flow visualization
   - Creative testing patterns
   - Key takeaways (actionable insights)

3. Funnel Sections (one per landing page)
   - Funnel header (name, URL)
   - Landing page card (screenshot + analysis)
   - Ad cards grid (media + analysis for each)
   
4. Footer
   - Source attribution
   - Date generated
```

### Styling Guidelines

- **Clean, doc-like design** — white background, simple typography
- **No dark gradients or heavy styling** — should feel like a PDF/Notion doc
- **Inline media** — videos and images embedded and playable
- **Mobile-friendly** — responsive grid for ad cards
- **Badges for quick scanning** — TOFU/BOFU, Video/Image, Variant, Top performer, Aspect ratio (1:1, 4:5, 9:16)

### Ad Card Format

Each ad card should display:
```
[Media: video/image]
[Badges: Type | Funnel Stage | Aspect Ratio | Duration (if video)]
[Title]
[Analysis fields: Hook, Script, Emotion, Strengths, Gaps]
```

**Include aspect ratio badge** on every ad card so patterns are visible at a glance (e.g., "all TOFU ads are 4:5, BOFU ads are 1:1").

See `templates/report-template.html` for the full HTML/CSS template.

## Delivery

1. Generate HTML file in the assets folder:
   ```
   ~/clawd/output/meta-ads/{advertiser-slug}/{slug}-analysis.html
   ```

2. Zip the entire folder (HTML + all media assets)

3. Send via Telegram with caption explaining contents

**Important:** The HTML uses relative paths to media files. Always deliver as a zip so the recipient can open it locally with all assets.

## Example Workflow

```
User: Analyze the EricPartaker ads we extracted

1. Read assets folder: ~/clawd/output/meta-ads/ericpartaker/
2. Analyze each video with Gemini / image with vision
3. Analyze landing page screenshots
4. Map ads to landing pages (identify 3 funnels)
5. Identify strategy patterns
6. Generate HTML report
7. Zip folder
8. Send to user
```

## Integration

This skill is designed to follow `/meta_ads_extractor`:

```
/meta_ads_extractor → downloads assets
/meta_ads_analyser → generates strategy report
```

Can also integrate with:
- **ad-creative-analysis** — detailed individual ad breakdowns
- **landing-page-analysis** — deeper landing page audits
