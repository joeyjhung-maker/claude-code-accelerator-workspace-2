---
name: create-skill
description: Helps you build a new Claude skill by asking the right questions and generating a properly formatted Skill.md file with correct YAML frontmatter.
---

# Create Skill

Your job is to interview the user and generate a production-ready `Skill.md` file for a new Claude skill.

## Trigger

Invoked when the user runs `/create-skill` or describes a task they want to turn into a reusable skill.

## Behavior

Work through the interview **one section at a time**. Ask each section's questions together, wait for the answer, reflect back what you heard, then move to the next. Do not dump all questions at once.

After all sections are complete, generate the finished `Skill.md` and ask the user where to save it. Default save path: `.claude/skills/{skill-name}/Skill.md`.

---

## Interview Sections

### Section 1: Identity

Ask:
- What do you want to call this skill? (this becomes the slug, e.g. `write-linkedin-post`)
- In one sentence, what does this skill do? (this becomes the YAML `description` field — it's what Claude uses to decide when to trigger the skill, so make it specific)

### Section 2: Purpose & Role

Ask:
- What is Claude's role when this skill is active? (e.g. "You are a LinkedIn ghostwriter writing in Joey's voice")
- What problem does this skill solve, and why does it need to be a skill rather than a one-off prompt?

### Section 3: Trigger & Usage

Ask:
- How will you invoke it? (e.g. `/write-linkedin-post`, or a keyword prefix like `Agency:`)
- Are there any arguments or options the user can pass? (e.g. a topic, a URL, a mode like "firefighting" or "optimiser")
- Should this skill ask clarifying questions before starting, or just execute?

### Section 4: Inputs

Ask:
- What information does this skill need to do its job?
- Where does that information come from — files it should read, user-provided details, context files in the project?
- Is anything optional vs. required?

### Section 5: Output

Ask:
- What does the finished output look like? (a file, a draft in chat, a structured document, a JSON blob?)
- Where should it be saved, if anywhere?
- Any specific format, length, or structure requirements?

### Section 6: Rules & Constraints

Ask:
- Are there any hard rules this skill must follow? (e.g. voice rules, things to avoid, must-include elements)
- Are there any files it should always read before starting? (e.g. voice-dna.json, icp.json, business-profile.json)
- Any error cases or edge cases to handle?

### Section 7: Examples (Optional)

Ask:
- Do you have an example of good output for this skill? (even rough notes help)
- Is there a bad example — output this skill should never produce?

---

## Output

Once all sections are complete, generate the `Skill.md` using this structure:

```
---
name: {skill-name}
description: {one-sentence description — specific enough for Claude to know when to trigger it}
---

# {Skill Title}

{1–2 sentence summary of what this skill does and the role Claude takes on.}

## Trigger

{When and how this skill is invoked. Include slash command, keyword prefix, or any variants.}

## Before You Start

{List any files Claude should read before executing. e.g. voice-dna.json, icp.json, business-profile.json}

## Inputs

{What information is needed. Mark each as required or optional. Note where it comes from.}

## Workflow

{Step-by-step of what Claude does. Number the steps. Be explicit about decisions and outputs at each stage.}

## Output

{What the finished output looks like. Format, length, where it's saved.}

## Rules

{Hard constraints. Things Claude must always do. Things Claude must never do.}

## Examples

{Good output example and/or bad output example, if provided.}
```

Omit any section the user didn't provide content for. Do not add placeholder text — only include what was confirmed in the interview.

---

## After Generating

1. Show the completed `Skill.md` in full in the chat.
2. Ask: "Where should I save this? Default is `.claude/skills/{skill-name}/Skill.md`"
3. Write the file to the confirmed path.
4. Confirm it's saved and ready to use.
