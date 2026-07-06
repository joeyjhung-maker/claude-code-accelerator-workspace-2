#!/usr/bin/env python3
"""Mechanical linter for the copy-rubric's STRUCTURE rules.

The rubric (rubrics/copy-rubric.md) marks its STRUCTURE section as "mechanical
— pass/fail, candidates for a linter later". This is that linter. It exists
because a judge model grading by feel missed these exact fails on 2026-07-06.

It checks ONLY the mechanical rules. Taste rules (mind movies, additive
framing, proof matching) stay with the judge pass. Provenance still applies:
run this on AI drafts and fix the FAILs; on Joey's own copy, output is
flag-only information, never a correction.

Usage:  python3 scripts/copy_lint.py <file.md> [more files...]
Lints the copy body (between the first and second `---` if present, else the
whole file), skipping markdown headers/meta lines. Exit 1 if any FAIL.
"""

import re
import sys
from pathlib import Path

BANNED_WORDS = ["leverage", "solution", "deliverable", "onboarding"]
SIGNPOSTS = ["here's the thing", "here's the magic", "and here's the"]


def body_lines(text):
    parts = text.split("\n---\n")
    body = parts[1] if len(parts) >= 3 else text
    offset = parts[0].count("\n") + 2 if len(parts) >= 3 else 0
    for i, line in enumerate(body.splitlines(), start=offset + 1):
        s = line.strip()
        if not s or s.startswith(("#", "*", "|", ">", "-", "Related:", "Date:")):
            continue
        yield i, s


def segments(line):
    """Split a line into sentence-ish segments. Ellipsis is NOT a terminator."""
    s = line.replace("...", "<ELL>").replace("…", "<ELL>")
    s = re.sub(r"(\d)\.(\d)", r"\1<DOT>\2", s)          # $14.40
    s = re.sub(r"\b([A-Za-z])\.([A-Za-z])\.", r"\1<DOT>\2<DOT>", s)  # A.I.
    parts = [p.strip() for p in re.split(r"(?<=[.!?])\s+", s) if p.strip()]
    return [p.replace("<ELL>", "…").replace("<DOT>", ".") for p in parts]


def is_spec(seg):
    """Price/spec fragments ("$14.40." / "167 pages.") are allowed."""
    return bool(re.search(r"\d", seg))


def lint_file(path):
    fails, flags = [], []
    for n, line in body_lines(Path(path).read_text()):
        low = line.lower()

        for w in BANNED_WORDS:
            if re.search(rf"\b{w}\b", low):
                fails.append((n, f'banned word "{w}"', line))
        for sp in SIGNPOSTS:
            if sp in low:
                fails.append((n, f'canned signpost "{sp}"', line))
        if re.search(r"[—–]", line):
            flags.append((n, "em/en dash — kill if AI wrote it, keep if Joey did", line))

        segs = segments(line)
        wordy = [s for s in segs if not re.match(r"^[.!?…]*$", s)]
        fulls = [s for s in wordy if len(s.split()) >= 4]
        frags = [s for s in wordy if len(s.split()) <= 3 and not is_spec(s)]

        if len(fulls) >= 2:
            fails.append((n, "two+ full sentences on one line", line))
        if len(wordy) >= 3 and len(frags) >= 2:
            fails.append((n, "fragment stack (fake-punchy staccato)", line))
        elif len(wordy) == 2 and len(frags) >= 1:
            flags.append((n, "short fragment pair — must earn its line", line))
        if sum(1 for s in wordy if s.startswith("No ")) >= 2:
            fails.append((n, '"No X. No Y." pattern — join with commas or rewrite', line))

    return fails, flags


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    any_fail = False
    for path in sys.argv[1:]:
        fails, flags = lint_file(path)
        print(f"\n== {path}: {len(fails)} FAIL, {len(flags)} FLAG ==")
        for n, rule, line in fails:
            print(f"  FAIL line {n}: {rule}\n        > {line}")
        for n, rule, line in flags:
            print(f"  flag line {n}: {rule}\n        > {line}")
        any_fail |= bool(fails)
    sys.exit(1 if any_fail else 0)


if __name__ == "__main__":
    main()
