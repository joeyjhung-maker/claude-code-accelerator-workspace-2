---
name: landing-page-analysis
description: Analyze landing pages and conversion pages. Use when reviewing competitor landing pages, analyzing the destination behind ad CTAs, auditing offer pages, studying funnel structure, or evaluating any page designed to convert visitors. Takes a screenshot and produces a structured marketing analysis of the page's offer, layout, and conversion strategy.
---

# Landing Page Analysis

Visit a landing page, capture it, and analyze the conversion strategy like a CRO specialist.

## Workflow

### Step 0: Load Chrome tools (once per session, one ToolSearch call)

```
ToolSearch query: "select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp"
```

### Step 1: Visit and screenshot the page

1. `tabs_context_mcp` to connect to the browser; `tabs_create_mcp` for a fresh tab.
2. `navigate` to the URL.
3. Wait 2–3 seconds for lazy content and hero images to render.
4. If a cookie banner or popup blocks the page, dismiss it (`computer` with `left_click` on the dismiss/accept button).
5. Screenshot the viewport (`computer` with action `screenshot`), then scroll down (`computer` with action `scroll`) and screenshot again — repeat until you've captured the full page, typically 3–6 screenshots.

### Step 2: Capture the page content

Call `get_page_text` for the full page text, and `read_page` for structure (form fields, CTAs, links). This is more reliable than reading text off screenshots.

**Fallback if Chrome isn't connected:** use `WebFetch` on the URL for text/structure and note in the output that visual analysis (Section 6) is limited because no screenshot was available.

### Step 3: Analyze

Use the screenshots + page text to produce the analysis. Follow the prompt structure in `references/prompts.md`.

## Output Format

1. **Message Match** — Does the page continue the ad's promise/angle/vocabulary? Graded strong/partial/broken.
2. **Above the Fold + 5-Second Test** — What is this? What's in it for me? What do I do next?
3. **Awareness Stage Fit** — Which stage the copy targets, and whether depth matches traffic temperature.
4. **The Offer** — Type, value equation (dream outcome × likelihood ÷ time × effort), risk reversal, price framing, Rule of One check.
5. **Social Proof Audit** — Strength-graded (specific+named vs generic), and proximity to claims/CTAs.
6. **Objection Map** — Which objections are handled by which elements, and which likely objection is unhandled.
7. **Copy Strategy** — Tone, pain vs aspiration lead, specificity, unique mechanism, story coherence.
8. **CTA & Friction Audit** — Every CTA, form fields, steps to convert, real vs manufactured urgency.
9. **Visual Design** — Layout, hierarchy, imagery, mobile signals.
10. **Funnel Position & Backend Inference** — TOFU/MOFU/BOFU, likely next step, what the funnel shape implies about economics.
11. **What Works / Weaknesses** — Tied to the frameworks; each weakness paired with its fix.
12. **Swipe Notes** — Section-by-section outline reusable for another offer.

**Context tip:** if the analysis was triggered from an ad (via ad-creative-analysis or ads-analyst), pass the ad's hook/angle into the prompt — Section 1 (Message Match) depends on it.

## Integration

Typically used after **meta-ads-library** extracts CTA URLs from ads. The pipeline:
1. Extract ads + CTA URLs (meta-ads-library)
2. Analyze the creative (ad-creative-analysis)
3. Visit + analyze the landing page (this skill)
4. Compile full ad-to-conversion report

## Reference

See `references/prompts.md` for the full analysis prompt.
