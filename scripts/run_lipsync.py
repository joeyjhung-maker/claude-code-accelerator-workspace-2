#!/usr/bin/env python3
"""Lip-sync a character image to an audio line through KIE (Kling AI Avatar Pro by default).

  python3 scripts/run_lipsync.py --image face.png --audio line.mp3 --out talk.mp4 "<performance prompt>"

Uploads both files to KIE's file host, logs the taskId immediately, then polls with the same
resilient loop as run_video.py (resume a dropped job with: run_video.py x --task <id> --out talk.mp4).
"""
import argparse, base64, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_image import load_env, post_json, upload_ref, ENV_FILE, CREATE_URL, UPLOAD_URL  # noqa: E402
from run_video import poll, credits  # noqa: E402


def upload_audio(path, token):
    p = Path(path); ext = p.suffix.lstrip('.').lower()
    mime = {'mp3': 'audio/mpeg', 'wav': 'audio/wav', 'm4a': 'audio/mp4', 'aac': 'audio/aac'}.get(ext, 'audio/mpeg')
    out = post_json(UPLOAD_URL, {"base64Data": f"data:{mime};base64,{base64.b64encode(p.read_bytes()).decode()}",
                                 "uploadPath": "audio/refs", "fileName": p.name}, token)
    url = (out.get("data") or {}).get("downloadUrl")
    if not url:
        sys.exit(f"audio upload failed: {json.dumps(out)[:400]}")
    print(f">>> audio uploaded: {url}", file=sys.stderr, flush=True)
    return url


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt")
    ap.add_argument("--image", required=True)
    ap.add_argument("--audio", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default="kling/ai-avatar-pro")
    args = ap.parse_args()
    token = load_env(ENV_FILE)["KIE_API_KEY"]
    img = args.image if args.image.startswith("http") else upload_ref(args.image, token)
    aud = args.audio if args.audio.startswith("http") else upload_audio(args.audio, token)
    print(f">>> createTask {args.model} (credits before: {credits(token)})", file=sys.stderr, flush=True)
    out = post_json(CREATE_URL, {"model": args.model, "input": {"image_url": img, "audio_url": aud, "prompt": args.prompt}}, token)
    tid = (out.get("data") or {}).get("taskId")
    if not tid:
        sys.exit(f"createTask failed: {json.dumps(out)[:500]}")
    print(f">>> taskId {tid}", file=sys.stderr, flush=True)
    poll(tid, token, args.out)


if __name__ == "__main__":
    main()
