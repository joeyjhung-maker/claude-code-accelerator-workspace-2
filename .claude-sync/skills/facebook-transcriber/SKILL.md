---
name: facebook-transcriber
description: Transcribe Facebook videos, reels, and video ads. Use when the user provides a Facebook/Meta video URL (facebook.com/watch, /reel/, /videos/, fb.watch) and wants a transcript, summary, or the script/hook extracted. Also works for any local audio/video file or direct media URL the user wants transcribed.
user-invocable: true
---

# Facebook Video Transcriber

Get a transcript from a Facebook video with zero manual DevTools work. Two paths: try `yt-dlp` first (fast when it works), fall back to sniffing the audio stream URL via the Chrome extension (reliable).

The transcription engine is `scripts/gemini_transcribe.py` — it downloads, converts, and transcribes via the Gemini API in one command. It accepts either a URL or a local file path.

**Requirements:** `GEMINI_API_KEY` (in `~/.zshrc`), ffmpeg, curl. No OpenAI/Whisper needed.

## Path A — yt-dlp (try first, ~30 seconds)

```bash
source ~/.zshrc 2>/dev/null
yt-dlp -f "bestaudio/best" --cookies-from-browser chrome -o "/tmp/fb_media.%(ext)s" "FACEBOOK_URL" 2>&1 | tail -5
```

- If it succeeds: find the downloaded file (`ls -t /tmp/fb_media.*`) and jump to **Transcribe**.
- If it errors (common on Facebook posts — parsing failures, login walls): go to Path B. Do not retry Path A more than once.

## Path B — Chrome network sniffing (reliable fallback)

Facebook serves video via DASH: separate video-only and audio-only `.mp4` chunk streams. You need the **audio** stream URL. Its path contains `m412` (video streams contain `m366`), and its `efg` query param contains `dash_ln_heaac`.

### Step 1: Load Chrome tools (one ToolSearch call)

```
ToolSearch query: "select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_network_requests,mcp__claude-in-chrome__tabs_create_mcp"
```

### Step 2: Open the video and play it

1. `tabs_context_mcp` to connect; create a tab if needed with `tabs_create_mcp`.
2. `navigate` to the Facebook URL.
3. Take a screenshot (`computer` with action `screenshot`). If a login wall or "See more on Facebook" dialog blocks the video, close it (click the X) or tell the user to log in.
4. Click the video's play button (`computer` with action `left_click` on the player). Wait ~5 seconds so several chunks load.

### Step 3: Pull the audio URL from network requests

Call `read_network_requests` and search the results for URLs containing `m412` OR `dash_ln_heaac`. Take any one matching URL — the script strips the `bytestart`/`byteend` segment params automatically to fetch the full stream.

If no match: play the video for a few more seconds and call `read_network_requests` again.

## Transcribe

```bash
source ~/.zshrc 2>/dev/null
python3 ~/.claude/skills/facebook-transcriber/scripts/gemini_transcribe.py "AUDIO_URL_OR_FILE" English
```

- Use the language the video is actually in if known; omit the second arg to auto-detect.
- The script prints the transcript to stdout, or `ERROR: ...` to stderr on failure.

## Error branches

| Symptom | Meaning | Action |
|---|---|---|
| `NO_SPEECH_DETECTED` | Text-overlay reel with music only | Tell the user there's no voiceover; offer to read the on-screen text from a screenshot instead |
| `Download failed — stream URL may have expired` | Facebook CDN URLs are short-lived | Re-capture the URL via Path B (don't reuse an old URL) |
| `GEMINI_API_KEY is not set` | Env not loaded | Prefix the command with `source ~/.zshrc` |
| Gemini HTTP 429 | Rate limit (script already retried 3×) | Wait a minute, run the script again |

## Present results

Show the full transcript in clean paragraphs. Then offer: summary, key quotes, or hook/angle extraction for ad research.
