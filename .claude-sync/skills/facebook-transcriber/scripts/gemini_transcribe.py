#!/usr/bin/env python3
"""Transcribe any audio/video URL or local file using the Gemini API.

Usage:
    python3 gemini_transcribe.py <url-or-file> [language]

- URL input: strips bytestart/byteend params (Facebook DASH segment ranges),
  downloads with curl, then transcribes.
- Local file input: transcribes directly.
- Converts to 16kHz mono MP3 via ffmpeg first (small + universally accepted).
- Files under ~18MB are sent inline (base64); larger files go through the
  Gemini Files API with resumable upload.

Requires: GEMINI_API_KEY env var, ffmpeg, curl. No Python packages needed.
All HTTP goes through curl (avoids macOS Python SSL cert issues).
Prints the transcript to stdout. Exits non-zero with an ERROR: line on failure.
"""
import base64
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.parse

MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
API_KEY = os.environ.get("GEMINI_API_KEY", "")
BASE = "https://generativelanguage.googleapis.com"
INLINE_LIMIT = 18 * 1024 * 1024


def die(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def strip_range_params(url):
    """Remove bytestart/byteend so we get the full stream, not one segment."""
    parts = urllib.parse.urlsplit(url)
    query = [(k, v) for k, v in urllib.parse.parse_qsl(parts.query, keep_blank_values=True)
             if k not in ("bytestart", "byteend")]
    return urllib.parse.urlunsplit(parts._replace(query=urllib.parse.urlencode(query)))


def api_post(url, payload, retries=3):
    # Payload can exceed ARG_MAX with inline audio, so pass it via a temp file
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(payload, f)
        body_file = f.name
    try:
        for attempt in range(retries):
            r = run(["curl", "-s", "-w", "\n%{http_code}", "-X", "POST", url,
                     "-H", "Content-Type: application/json",
                     "--data-binary", f"@{body_file}", "--max-time", "600"])
            out, _, code = r.stdout.rpartition("\n")
            if code == "200":
                return json.loads(out)
            if code in ("429", "500", "502", "503") and attempt < retries - 1:
                time.sleep(10 * (attempt + 1))
                continue
            die(f"Gemini API HTTP {code or 'no response'}: {out[:500]}")
    finally:
        os.unlink(body_file)


def upload_to_files_api(path, size):
    start = run([
        "curl", "-s", "-i", "-X", "POST",
        f"{BASE}/upload/v1beta/files?key={API_KEY}",
        "-H", "X-Goog-Upload-Protocol: resumable",
        "-H", "X-Goog-Upload-Command: start",
        "-H", f"X-Goog-Upload-Header-Content-Length: {size}",
        "-H", "X-Goog-Upload-Header-Content-Type: audio/mp3",
        "-H", "Content-Type: application/json",
        "-d", json.dumps({"file": {"displayName": os.path.basename(path)}}),
    ])
    m = re.search(r"x-goog-upload-url:\s*(\S+)", start.stdout, re.IGNORECASE)
    if not m:
        die(f"Files API did not return an upload URL. Response head: {start.stdout[:300]}")
    upload_url = m.group(1)

    fin = run([
        "curl", "-s", "-X", "POST", upload_url,
        "-H", "X-Goog-Upload-Command: upload, finalize",
        "-H", "X-Goog-Upload-Offset: 0",
        "-H", f"Content-Length: {size}",
        "--data-binary", f"@{path}",
    ])
    try:
        info = json.loads(fin.stdout)["file"]
    except (json.JSONDecodeError, KeyError):
        die(f"Upload finalize failed: {fin.stdout[:300]}")

    # Poll until the file is processed and ACTIVE
    for _ in range(60):
        if info.get("state") == "ACTIVE":
            return info["uri"]
        time.sleep(2)
        poll = run(["curl", "-s", f"{info['uri']}?key={API_KEY}"])
        try:
            info = json.loads(poll.stdout)
        except json.JSONDecodeError:
            continue
    die("Uploaded file never became ACTIVE on Gemini Files API")


def main():
    if not API_KEY:
        die("GEMINI_API_KEY is not set (it lives in ~/.zshrc — run: source ~/.zshrc)")
    if len(sys.argv) < 2:
        die("usage: gemini_transcribe.py <url-or-file> [language]")

    src = sys.argv[1]
    language = sys.argv[2] if len(sys.argv) > 2 else "the original language"
    tmpdir = tempfile.mkdtemp(prefix="gemini_tx_")
    raw = os.path.join(tmpdir, "raw_media")
    mp3 = os.path.join(tmpdir, "audio.mp3")

    if re.match(r"^https?://", src):
        url = strip_range_params(src)
        dl = run(["curl", "-sL", "--fail", "-o", raw, url])
        if dl.returncode != 0 or not os.path.exists(raw) or os.path.getsize(raw) == 0:
            die("Download failed — the stream URL may have expired (Facebook URLs are short-lived). Re-capture it.")
    else:
        if not os.path.exists(src):
            die(f"File not found: {src}")
        raw = src

    conv = run(["ffmpeg", "-y", "-i", raw, "-vn", "-ac", "1", "-ar", "16000", "-b:a", "48k", mp3])
    if conv.returncode != 0:
        die(f"ffmpeg conversion failed: {conv.stderr[-400:]}")

    size = os.path.getsize(mp3)
    prompt = (f"Transcribe this audio verbatim in {language}. Output ONLY the spoken words as plain text "
              f"paragraphs — no timestamps, no speaker labels, no commentary. If there is no speech "
              f"(music only), output exactly: NO_SPEECH_DETECTED")

    if size <= INLINE_LIMIT:
        with open(mp3, "rb") as f:
            audio_part = {"inlineData": {"mimeType": "audio/mp3",
                                         "data": base64.b64encode(f.read()).decode()}}
    else:
        audio_part = {"fileData": {"mimeType": "audio/mp3", "fileUri": upload_to_files_api(mp3, size)}}

    result = api_post(
        f"{BASE}/v1beta/models/{MODEL}:generateContent?key={API_KEY}",
        {"contents": [{"parts": [audio_part, {"text": prompt}]}],
         "generationConfig": {"temperature": 0.0, "maxOutputTokens": 65536}},
    )
    try:
        text = "".join(p.get("text", "") for p in result["candidates"][0]["content"]["parts"]).strip()
    except (KeyError, IndexError):
        die(f"Unexpected Gemini response: {json.dumps(result)[:500]}")
    print(text)


if __name__ == "__main__":
    main()
