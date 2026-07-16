---
name: youtube-transcriber
description: Transcribe YouTube videos. Use when the user provides a YouTube URL and wants the transcript, summary, or to extract key points from a video.
user-invocable: true
---

# YouTube Transcriber

Fetch and return the full transcript of a YouTube video, then offer analysis.

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

    # Try to list transcripts and pick the best one
    try:
        transcript_list = api.list_transcripts(video_id)
        try:
            transcript = transcript_list.find_manually_created_transcript(['en'])
        except:
            try:
                transcript = transcript_list.find_generated_transcript(['en'])
            except:
                # Fall back to any available language, translated to English
                transcript = next(iter(transcript_list)).translate('en')
        data = transcript.fetch()
    except Exception:
        # Simple fetch fallback
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

## Step 3 — Present Results

1. Display the **full transcript** in a clean readable format (no timestamps unless requested)
2. After the transcript, offer the user these options:
   - **Summary** — bullet-point key takeaways
   - **Key quotes** — most impactful lines
   - **Hook/Angle extraction** — for ad or content inspiration
   - **Full analysis** — structure, messaging, CTA

## Error Handling

- If transcripts are disabled: inform the user and suggest using `yt-dlp` to download audio and transcribe locally
- If the video is private/unavailable: tell the user
- If no English transcript: try to translate from available language and note this

## yt-dlp Fallback (if transcript API fails)

```bash
yt-dlp --write-auto-sub --sub-lang en --skip-download --output "/tmp/yt_%(id)s" "VIDEO_URL"
cat /tmp/yt_VIDEO_ID.en.vtt 2>/dev/null | grep -v "^WEBVTT" | grep -v "^$" | grep -v "[0-9]\{2\}:[0-9]\{2\}" | sort -u
```
