#!/usr/bin/env python3
"""Run mariobot (Genesis) with the 2-step stateless protocol.

Replaces the old throwaway /tmp/run_mario.py, which got wiped between sessions
and led to the pipeline being rebuilt from memory (thin primes, forgotten rules).

What it does, per workflows/2026-06-24-mariobot-genesis-body-copy.md:
  1. PRIME  — send the primer file(s) (winning ads), bot absorbs the patterns.
  2. INSTRUCT — replay [primer -> confirmation -> instruction] and get the draft.

The style contract (rubrics/mariobot-style-contract.md) is prepended to the
instruction automatically, so the WRITER sees the hard rules — the judge is
the backstop, not the only line of defence.

Usage:
  python3 scripts/run_mario.py \
      --primer clients/flexxable-primers/iaa-jv-body.md \
      --instruction /path/to/brief.md \
      --out jv/partners/.../draft.md          # optional; prints to stdout too
  Add --dry-run to inspect the exact payloads without calling the API.

Keys come from clients/.env (GENESIS_API_KEY + ANTHROPIC_API_KEY).
Endpoint needs BOTH headers (Authorization: Bearer genesis-key, X-Provider-Key:
anthropic-key), stream:true is required, and sequential calls only on one key.
"""

import argparse
import json
import re
import ssl
import sys
import time
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ENV_FILE = REPO / "clients" / ".env"
CONTRACT_FILE = REPO / "rubrics" / "mariobot-style-contract.md"
BASE_URL = "https://gas.copycoders.ai/api/v1"
BOT = "mariobot"


def load_env(path):
    env = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


def style_contract():
    text = CONTRACT_FILE.read_text()
    m = re.search(
        r"\(verbatim block starts here\)\n(.*?)\n\(verbatim block ends here\)",
        text,
        re.DOTALL,
    )
    if not m:
        sys.exit(f"Could not find the verbatim block in {CONTRACT_FILE}")
    return m.group(1).strip()


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
                    help="primer file (winning ads); repeatable")
    ap.add_argument("--instruction", required=True, help="the brief file")
    ap.add_argument("--out", help="write the draft here as well as stdout")
    ap.add_argument("--dry-run", action="store_true",
                    help="print payloads, no API call")
    args = ap.parse_args()

    primer = "\n\n---\n\n".join(Path(p).read_text() for p in args.primer)
    prime_msg = (
        "You are about to write direct-response copy. First, absorb the voice "
        "and patterns of these winning ads. Reply only that you've absorbed "
        "the patterns.\n\n" + primer
    )
    instruction = (
        "Before you write, these are the hard rules. They override any "
        "structural pattern in the sample ads you absorbed.\n\n"
        + style_contract()
        + "\n\n---\n\nNow the brief:\n\n"
        + Path(args.instruction).read_text()
    )

    if args.dry_run:
        print("=== STEP 1: PRIME ===\n")
        print(prime_msg)
        print("\n=== STEP 2: INSTRUCT (after replaying prime + confirmation) ===\n")
        print(instruction)
        return

    env = load_env(ENV_FILE)
    for key in ("GENESIS_API_KEY", "ANTHROPIC_API_KEY"):
        if key not in env:
            sys.exit(f"{key} missing from {ENV_FILE}")

    print(">>> Step 1: priming...", file=sys.stderr)
    confirmation = call_bot([{"role": "user", "content": prime_msg}], env)

    time.sleep(2)  # the server wants a beat between protocol steps

    print(">>> Step 2: instructing...", file=sys.stderr)
    draft = call_bot(
        [
            {"role": "user", "content": prime_msg},
            {"role": "assistant", "content": confirmation},
            {"role": "user", "content": instruction},
        ],
        env,
    )

    if args.out:
        Path(args.out).write_text(draft + "\n")
        print(f">>> Draft written to {args.out}", file=sys.stderr)
    print(draft)


if __name__ == "__main__":
    main()
