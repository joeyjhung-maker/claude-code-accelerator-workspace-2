# Workflow: "Make me an image like this" means a prompt, not a mockup

*Status: first instance, not yet a locked play. Watch for a repeat before treating this as settled.*

Related: [[Promotion]] [[b2b-leads-lab-project]]

## When to use this
Joey pastes a reference image (a competitor infographic, a swipe, a poster) and asks Claude to produce something like it.

## What happened
Asked to reproduce a Royalty Ronin-style Skool About-page infographic for B2B Leads Lab. Built a full HTML/CSS "case file" mockup — real copy, real proof numbers, custom layout, no invented facts. Rejected outright: "Your image sucks balls. Give me a prompt so I can do this in ChatGPT." The actual want was never a webpage rendering of the idea — it was a real illustrated image, and Claude's own image output isn't the tool for that. Redid it as a single ChatGPT image-gen prompt (with the same real content) sized to the actual platform slot, and that's what shipped.

## The steps (proposed)
1. Confirm what the deliverable actually is: a real image asset (goes to an image-gen prompt), or an interactive/webpage thing (goes to an HTML artifact). Reference-image requests are almost always the former.
2. Pull the exact dimensions/aspect ratio the image needs to fill (the platform's upload slot, ad spec, etc.) before writing the prompt — measure it from a screenshot if there's no documented spec.
3. Write one dense, structured image-gen prompt: style/palette/mood, exact text blocks to render verbatim, layout description section by section. Ground every number and claim in verified facts, same as any other copy.
4. Don't build an HTML/CSS comp as a stand-in "so you can see the structure first" unless Joey specifically asks for a webpage or interactive mockup.

## What good looks like
`creatives/flexxable/b2b-leads-lab-about-page-chatgpt-prompt.md` — one prompt block, 1920x1080 (matched to the real Skool About-page slot), real Money Bags campaign numbers, no invented stats.
