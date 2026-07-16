---
name: youtube-transcriber-notes
description: Transcribe a YouTube video and convert it into structured personal learning notes for retention and action — not summaries, not marketing material.
user-invocable: true
---

# YouTube Transcriber → Learning Notes

Fetch the full transcript of a YouTube video and convert it into structured, personal study notes designed for retention, future review, and real-world application.

## Step 1 — Extract the Video ID

Parse the YouTube URL provided by the user. Extract the video ID from formats like:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/shorts/VIDEO_ID`

## Step 2 — Fetch the Transcript

Use the Bash tool to run this Python script, replacing `VIDEO_ID` with the actual ID:

```bash
python3 - <<'EOF'
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

video_id = "VIDEO_ID"

try:
    api = YouTubeTranscriptApi()

    try:
        transcript_list = api.list_transcripts(video_id)
        try:
            transcript = transcript_list.find_manually_created_transcript(['en'])
        except:
            try:
                transcript = transcript_list.find_generated_transcript(['en'])
            except:
                transcript = next(iter(transcript_list)).translate('en')
        data = transcript.fetch()
    except Exception:
        data = api.fetch(video_id)

    full_text = " ".join([entry.text for entry in data])
    print(full_text)

except TranscriptsDisabled:
    print("ERROR: Transcripts are disabled for this video.")
except NoTranscriptFound:
    print("ERROR: No transcript found for this video.")
except Exception as e:
    print(f"ERROR: {e}")
EOF
```

## Step 3 — Analyse the Transcript

Before writing notes, identify:
- The **core subject** and overarching theme
- The **main concepts or arguments** (aim for 5–12 distinct ideas worth noting)
- Any **named frameworks, models, terms, or distinctions** introduced
- **Examples, stories, or case studies** that illustrate the concepts
- **Actionable implications** — what someone could actually *do* with this

Do NOT summarise. Do NOT write for an audience. These notes are for the person who just watched the video to help them retain, revisit, and act.

## Step 4 — Write the Learning Notes

Format the notes using the structure below. Adapt section names to fit the content — these are guidelines, not a rigid template.

---

### Notes Header

```
# [Title — describe the subject, not the video]

**Source:** [YouTube URL or video title if known]
```

---

### Core Concept Sections

Each major concept gets its own numbered section:

```
## 1. [Concept Name]
**[Key scripture / quote / source reference if applicable]**

- Bullet points covering the key ideas in this section
- Use plain language — write it as if explaining to yourself
- Capture the *why* behind each idea, not just the what

**Key insight:** [One sentence that distills the most important takeaway from this section]

**Action:** [Only include if there's something directly actionable. Skip if not.]
```

---

### Tables for Distinctions

When the content introduces a comparison or contrast between two things (e.g. two types, two stages, two words), use a table:

```
| Term A | Term B |
|--------|--------|
| Definition | Definition |
| Implication | Implication |
```

---

### Summary Section

After all concept sections, write a concise summary list:

```
## Summary — [The Core Laws / Principles / Framework]

1. First principle
2. Second principle
...
```

---

### Questions to Sit With

End with 3–6 honest, personal questions that arise from the content. These should be questions the viewer might need to ask themselves — not rhetorical, not soft:

```
## Questions to Sit With

- [Direct personal question]
- [Direct personal question]
- ...
```

---

## Formatting Rules

- Use `**Key insight:**` callouts to flag the most important single idea per section
- Use `**Action:**` only when there is a concrete, real-world thing to do — not vague intentions
- Use bold sparingly — only for genuinely important terms or distinctions
- No filler phrases like "In this section we explore..." or "The speaker argues..."
- Write in second person ("you") for actionable parts; third person or neutral for concept explanations
- Keep sentences short. Dense content should breathe.
- Do NOT end with a list of options or ask what the user wants next — just deliver the notes.

---

## Error Handling

- If transcripts are disabled: inform the user and suggest using `yt-dlp` to download audio
- If the video is private/unavailable: tell the user
- If no English transcript exists: translate from available language and note this at the top of the notes

## yt-dlp Fallback (if transcript API fails)

```bash
yt-dlp --write-auto-sub --sub-lang en --skip-download --output "/tmp/yt_%(id)s" "VIDEO_URL"
cat /tmp/yt_VIDEO_ID.en.vtt 2>/dev/null | grep -v "^WEBVTT" | grep -v "^$" | grep -v "[0-9]\{2\}:[0-9]\{2\}" | sort -u
```
