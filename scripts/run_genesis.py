#!/usr/bin/env python3
"""General Genesis runner — call ANY bot with the stateless N-turn protocol.

run_mario.py (body, 2-step, prepends the style contract) and run_hookbot.py
(hooks, 3-step double-pass) are purpose-built. This one is the generic tool for
any other bot on the roster (75-ads-template-bot, insight-vectors-bot, etc.):

  1. PRIME  — send the primer file(s). Bot replies it's absorbed the patterns.
  2..N. TURN — replay the full history + each --turn instruction, in order.

Every bot is stateless, so we replay [primer -> confirmation -> turn1 -> reply1
-> turn2 ...] each call. stream:true required, both headers, a beat between.

Usage:
  python3 scripts/run_genesis.py --bot 75-ads-template-bot \
      --primer path/to/winning-ad.md \
      --turn path/to/turn1.md --turn path/to/turn2.md \
      --out path/to/output.md
  --dry-run prints the payloads. A --turn value that is an existing file path is
  read as a file; otherwise it is sent as a literal string.
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


def load_env(path):
    env = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


def call_bot(bot, messages, env):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    body = json.dumps({"model": bot, "messages": messages, "stream": True})
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


def resolve(val):
    p = Path(val)
    return p.read_text() if p.exists() else val


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bot", required=True, help="bot id from the roster")
    ap.add_argument("--primer", action="append", required=True,
                    help="primer file (winning ad/hooks); repeatable")
    ap.add_argument("--turn", action="append", required=True,
                    help="instruction (file path or literal); repeatable, in order")
    ap.add_argument("--out", help="write the FINAL reply here as well as stdout")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    primer = "\n\n---\n\n".join(Path(p).read_text() for p in args.primer)
    prime_msg = (
        "You are about to work on direct-response copy. First, absorb the voice, "
        "structure and patterns of the winning material below. Reply only that "
        "you've absorbed the patterns.\n\n" + primer
    )
    turns = [resolve(t) for t in args.turn]

    if args.dry_run:
        print("=== PRIME ===\n" + prime_msg)
        for i, t in enumerate(turns, 1):
            print(f"\n=== TURN {i} ===\n" + t)
        return

    env = load_env(ENV_FILE)
    for key in ("GENESIS_API_KEY", "ANTHROPIC_API_KEY"):
        if key not in env:
            sys.exit(f"{key} missing from {ENV_FILE}")

    print(">>> priming...", file=sys.stderr)
    confirmation = call_bot(args.bot, [{"role": "user", "content": prime_msg}], env)
    history = [
        {"role": "user", "content": prime_msg},
        {"role": "assistant", "content": confirmation},
    ]
    final = confirmation
    for i, t in enumerate(turns, 1):
        time.sleep(2)
        print(f">>> turn {i}...", file=sys.stderr)
        history.append({"role": "user", "content": t})
        final = call_bot(args.bot, history, env)
        history.append({"role": "assistant", "content": final})

    if args.out:
        Path(args.out).write_text(final + "\n")
        print(f">>> Final reply written to {args.out}", file=sys.stderr)
    print(final)


if __name__ == "__main__":
    main()
