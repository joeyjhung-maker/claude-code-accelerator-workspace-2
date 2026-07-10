#!/usr/bin/env python3
"""Render a static ad image through KIE (GPT-Image / Nano Banana).

The copy side has run_mario.py / run_hookbot.py; this is the same idea for
STATICS. One KIE key renders images and video — this script does images.

Two modes:
  * text-to-image (default)   — model `google/nano-banana`, prompt only.
  * edit / reference-guided   — pass --ref <local-or-url>; model flips to
                                `google/nano-banana-edit` and the reference is
                                uploaded (if local) then handed to the model as
                                image_urls. Reference images are the #1 quality
                                lever for native SCRAWLS renders — use one when
                                you have it.

Endpoints + gotchas are banked in
`.claude/skills/creative-strategy-system/knowledge/kie-render-reference.md`:
  - createTask  POST https://api.kie.ai/api/v1/jobs/createTask
  - poll        GET  https://api.kie.ai/api/v1/jobs/recordInfo?taskId=...
  - upload      POST https://kieai.redpandaai.co/api/file-base64-upload
  - A browser User-Agent is REQUIRED on EVERY call (KIE's WAF 403s Python's UA),
    including the final image download.

Usage:
  python3 scripts/run_image.py "<prompt>" --out creatives/flexxable/foo.png
  python3 scripts/run_image.py "<prompt>" --ref creatives/refs/burnout.png \
      --aspect 4:5 --out creatives/flexxable/foo.png
  --model overrides the model id. --dry-run prints the payload, no API call.

Key from clients/.env (KIE_API_KEY). Format 4:5 or 1:1 only (feed-native).
"""

import argparse
import base64
import json
import ssl
import sys
import time
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ENV_FILE = REPO / "clients" / ".env"
CREATE_URL = "https://api.kie.ai/api/v1/jobs/createTask"
POLL_URL = "https://api.kie.ai/api/v1/jobs/recordInfo"
UPLOAD_URL = "https://kieai.redpandaai.co/api/file-base64-upload"
UA = "Mozilla/5.0"  # KIE's WAF 403s Python's default UA — mimic a browser.
T2I_MODEL = "google/nano-banana"
EDIT_MODEL = "google/nano-banana-edit"

# curl reaches this host fine without cert verification; urllib otherwise
# throws CERTIFICATE_VERIFY_FAILED. Mirror curl's behaviour.
_CTX = ssl.create_default_context()
_CTX.check_hostname = False
_CTX.verify_mode = ssl.CERT_NONE


def load_env(path):
    env = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


def post_json(url, payload, token):
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
            "User-Agent": UA,
        },
    )
    with urllib.request.urlopen(req, context=_CTX) as resp:
        return json.loads(resp.read().decode())


def get_json(url, token):
    req = urllib.request.Request(
        url, headers={"Authorization": f"Bearer {token}", "User-Agent": UA}
    )
    with urllib.request.urlopen(req, context=_CTX) as resp:
        return json.loads(resp.read().decode())


def upload_ref(local_path, token):
    """Upload a local reference image → return a public downloadUrl KIE can pull."""
    p = Path(local_path)
    b64 = base64.b64encode(p.read_bytes()).decode()
    ext = p.suffix.lstrip(".").lower() or "png"
    payload = {
        "base64Data": f"data:image/{ext};base64,{b64}",
        "uploadPath": "images/refs",
        "fileName": p.name,
    }
    out = post_json(UPLOAD_URL, payload, token)
    url = (out.get("data") or {}).get("downloadUrl")
    if not url:
        sys.exit(f"Reference upload failed: {json.dumps(out)[:400]}")
    print(f">>> reference uploaded: {url}", file=sys.stderr)
    return url


def download(url, out_path):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, context=_CTX) as resp:
        data = resp.read()
    Path(out_path).write_bytes(data)
    return len(data)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt", help="the render prompt")
    ap.add_argument("--out", required=True, help="where to save the .png")
    ap.add_argument("--ref", help="reference image (local path or URL) — flips to edit model")
    ap.add_argument("--aspect", default="4:5", help="4:5 (default) or 1:1 — feed-native only")
    ap.add_argument("--model", help="override the model id")
    ap.add_argument("--timeout", type=int, default=300, help="poll timeout seconds")
    ap.add_argument("--dry-run", action="store_true", help="print payload, no API call")
    args = ap.parse_args()

    if args.aspect not in ("4:5", "1:1"):
        print(f"!! warning: {args.aspect} isn't feed-native (use 4:5 or 1:1)", file=sys.stderr)

    model = args.model or (EDIT_MODEL if args.ref else T2I_MODEL)
    payload = {
        "model": model,
        "input": {
            "prompt": args.prompt,
            "output_format": "png",
            "image_size": args.aspect,
        },
    }

    if args.dry_run:
        if args.ref:
            payload["input"]["image_urls"] = ["<uploaded-ref-url>"]
        print(json.dumps(payload, indent=2))
        return

    env = load_env(ENV_FILE)
    token = env.get("KIE_API_KEY")
    if not token:
        sys.exit(f"KIE_API_KEY missing from {ENV_FILE}")

    if args.ref:
        ref_url = args.ref if args.ref.startswith("http") else upload_ref(args.ref, token)
        payload["input"]["image_urls"] = [ref_url]

    print(f">>> createTask ({model}, {args.aspect})...", file=sys.stderr)
    created = post_json(CREATE_URL, payload, token)
    task_id = (created.get("data") or {}).get("taskId") or created.get("taskId")
    if not task_id:
        sys.exit(f"createTask returned no taskId: {json.dumps(created)[:400]}")
    print(f">>> taskId {task_id} — polling...", file=sys.stderr)

    deadline = time.time() + args.timeout
    while time.time() < deadline:
        time.sleep(5)
        info = get_json(f"{POLL_URL}?taskId={task_id}", token)
        data = info.get("data") or {}
        state = data.get("state")
        if state == "success":
            result = data.get("resultJson")
            result = json.loads(result) if isinstance(result, str) else (result or {})
            urls = result.get("resultUrls") or []
            if not urls:
                sys.exit(f"success but no resultUrls: {json.dumps(data)[:400]}")
            n = download(urls[0], args.out)
            print(f">>> saved {n} bytes -> {args.out}", file=sys.stderr)
            print(args.out)
            return
        if state in ("fail", "failed"):
            sys.exit(f"render failed: {json.dumps(data)[:400]}")
        print(f"    state={state}...", file=sys.stderr)

    sys.exit(f"timed out after {args.timeout}s (taskId {task_id})")


if __name__ == "__main__":
    main()
