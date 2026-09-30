#!/usr/bin/env python3
"""Render a short video clip through KIE (image-to-video or text-to-video).

  python3 scripts/run_video.py "<motion prompt>" --image key.png --out clip.mp4
  python3 scripts/run_video.py "<prompt>" --out clip.mp4 --model veo-3-1 --duration 6 --aspect 9:16

Same plumbing as run_image.py (see kie-render-reference.md): browser User-Agent on every
call, local images uploaded to KIE's file host first, createTask -> poll recordInfo.
Prints the credit balance before and after so every clip's cost is visible.
Key from clients/.env (KIE_API_KEY).
"""
import argparse, json, sys, time, urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_image import load_env, post_json, get_json, upload_ref, download, ENV_FILE, CREATE_URL, POLL_URL, UA, _CTX  # noqa: E402

CREDIT_URL = "https://api.kie.ai/api/v1/chat/credit"


def credits(token):
    try:
        return get_json(CREDIT_URL, token).get("data")
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt")
    ap.add_argument("--out", required=True)
    ap.add_argument("--image", help="start frame (local path or URL) -> image-to-video")
    ap.add_argument("--model", default="veo-3-1")
    ap.add_argument("--duration", type=int, default=6)
    ap.add_argument("--aspect", default="9:16")
    ap.add_argument("--resolution", default="1080p")
    ap.add_argument("--extra", default="{}", help="JSON merged into input{} for model-specific params")
    ap.add_argument("--task", help="resume polling an existing taskId instead of creating a new one")
    args = ap.parse_args()

    token = load_env(ENV_FILE)["KIE_API_KEY"]
    if args.task:
        return poll(args.task, token, args.out)
    before = credits(token)
    inp = {"prompt": args.prompt, "aspect_ratio": args.aspect, "duration": args.duration, "resolution": args.resolution}
    if args.image:
        url = args.image if args.image.startswith("http") else upload_ref(args.image, token)
        inp["image_urls"] = [url]
        inp["generation_type"] = "FIRST_AND_LAST_FRAMES_2_VIDEO"
    inp.update(json.loads(args.extra))
    payload = {"model": args.model, "input": inp}
    print(f">>> createTask {args.model} {args.duration}s {args.aspect} {args.resolution} (credits before: {before})", file=sys.stderr)
    out = post_json(CREATE_URL, payload, token)
    tid = (out.get("data") or {}).get("taskId")
    if not tid:
        sys.exit(f"createTask failed: {json.dumps(out)[:500]}")
    # log the id straight away so a dropped connection never loses a paid render (resume with --task)
    print(f">>> taskId {tid}", file=sys.stderr, flush=True)
    poll(tid, token, args.out)


def poll(tid, token, out_path):
    t0 = time.time()
    while True:
        time.sleep(8)
        try:
            rec = get_json(f"{POLL_URL}?taskId={tid}", token).get("data") or {}
        except Exception as e:  # network blips / sleep: keep polling
            print(f"... poll error ({e}); retrying", file=sys.stderr, flush=True)
            if time.time() - t0 > 1800:
                sys.exit(f"timed out, taskId {tid}")
            continue
        state = rec.get("state")
        if state == "success":
            res = json.loads(rec.get("resultJson") or "{}")
            d = res.get("data") or {}
            urls = res.get("resultUrls") or d.get("result_urls") or d.get("origin_urls") or []
            if not urls:
                sys.exit(f"no result url: {json.dumps(rec)[:500]}")
            n = download(urls[0], out_path)
            print(f">>> saved {n} bytes -> {out_path} in {time.time()-t0:.0f}s, {rec.get('creditsConsumed')} credits (balance now: {credits(token)})", file=sys.stderr)
            print(out_path)
            return
        if state in ("fail", "failed", "error"):
            sys.exit(f"render failed: {json.dumps(rec)[:600]}")
        if time.time() - t0 > 1800:
            sys.exit(f"timed out, taskId {tid}")


if __name__ == "__main__":
    main()
