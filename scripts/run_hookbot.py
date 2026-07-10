#!/usr/bin/env python3
"""Run ad-hook-bot-1 (Genesis) with the 3-step stateless hook protocol.

Sibling of run_mario.py, but for HOOKS. The difference is the mandatory
double-pass: hooks need a third call that sharpens the best of the first 10 to
Level 3 and generates 10 more, for 20 total (per the hook-bot template and
knowledge/frameworks/hook-quality.md).

  1. PRIME     — send the hook primer (winning hooks). Bot absorbs the patterns.
  2. INSTRUCT  — replay [primer -> confirmation -> brief]. Bot returns ~10 hooks.
  3. DOUBLEPASS- replay the whole history + "take your strongest, sharpen each to
                 Level 3 viciousness, generate 10 MORE. Output all 20, numbered."

Usage:
  python3 scripts/run_hookbot.py \
      --primer clients/flexxable/primers/hooks.md \
      --instruction /path/to/brief.md \
      --out jv/.../hooks.md         # optional; also prints to stdout
  --dry-run prints the payloads without calling the API.

Keys from clients/.env (GENESIS_API_KEY + ANTHROPIC_API_KEY). Both headers,
stream:true required, sequential calls only, a beat between steps.
"""

import argparse
import json
import ssl
import sys
import time
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ENV_FILE = REPO / "clients" / ".env"
BASE_URL = "https://gas.copycoders.ai/api/v1"
BOT = "ad-hook-bot-1"

DOUBLEPASS = (
    "Now the double-pass. Take your strongest 2-3 hooks from above, sharpen each "
    "to Level 3 viciousness (go harder for the throat, protect the charged word, "
    "keep it spoken-natural for a Reel), then generate 10 MORE using Transfer / "
    "Reframe / Promote. Output ALL 20 hooks as one numbered list, one line each. "
    "No preamble, no commentary."
)


def load_env(path):
    env = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


def call_bot(messages, env):
    # Python urllib fails CERTIFICATE_VERIFY_FAILED against this host; curl is
    # fine without it, so we mirror curl's behaviour.
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    body = json.dumps({"model": BOT, "messages": messages, "stream": True})
    req = urllib.request.Request(
        f"{BASE_URL}/chat/completions",
        data=body.encode(),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {env['GENESIS_API_KEY']}",
            "X-Provider-Key": env["ANTHROPIC_API_KEY"],
        },
    )
    chunks = []
    with urllib.request.urlopen(req, context=ctx) as resp:
        for raw in resp:
            line = raw.decode("utf-8", "replace").strip()
            if not line.startswith("data:"):
                continue
            data = line[5:].strip()
            if data == "[DONE]":
                break
            try:
                delta = json.loads(data)["choices"][0]["delta"]
            except (json.JSONDecodeError, KeyError, IndexError):
                continue
            piece = delta.get("content")
            if piece:
                chunks.append(piece)
                sys.stderr.write(piece)
                sys.stderr.flush()
    sys.stderr.write("\n")
    return "".join(chunks)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--primer", action="append", required=True,
                    help="hook primer file (winning hooks); repeatable")
    ap.add_argument("--instruction", required=True, help="the brief file")
    ap.add_argument("--out", help="write the hooks here as well as stdout")
    ap.add_argument("--dry-run", action="store_true",
                    help="print payloads, no API call")
    args = ap.parse_args()

    primer = "\n\n---\n\n".join(Path(p).read_text() for p in args.primer)
    prime_msg = (
        "You are about to generate direct-response hooks. First, absorb the "
        "voice, rhythm and hook patterns of these winning hooks. Reply only that "
        "you've absorbed the patterns.\n\n" + primer
    )
    instruction = Path(args.instruction).read_text()

    if args.dry_run:
        print("=== STEP 1: PRIME ===\n")
        print(prime_msg)
        print("\n=== STEP 2: INSTRUCT ===\n")
        print(instruction)
        print("\n=== STEP 3: DOUBLE-PASS ===\n")
        print(DOUBLEPASS)
        return

    env = load_env(ENV_FILE)
    for key in ("GENESIS_API_KEY", "ANTHROPIC_API_KEY"):
        if key not in env:
            sys.exit(f"{key} missing from {ENV_FILE}")

    print(">>> Step 1: priming...", file=sys.stderr)
    confirmation = call_bot([{"role": "user", "content": prime_msg}], env)
    time.sleep(2)

    print(">>> Step 2: instructing (first pass)...", file=sys.stderr)
    history = [
        {"role": "user", "content": prime_msg},
        {"role": "assistant", "content": confirmation},
        {"role": "user", "content": instruction},
    ]
    first = call_bot(history, env)
    time.sleep(2)

    print(">>> Step 3: double-pass...", file=sys.stderr)
    history += [
        {"role": "assistant", "content": first},
        {"role": "user", "content": DOUBLEPASS},
    ]
    final = call_bot(history, env)

    if args.out:
        Path(args.out).write_text(final + "\n")
        print(f">>> Hooks written to {args.out}", file=sys.stderr)
    print(final)


if __name__ == "__main__":
    main()
