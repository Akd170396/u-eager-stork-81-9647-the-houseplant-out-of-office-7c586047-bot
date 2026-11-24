"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default ./output/entry.txt for local runs).
Stdlib only. Deterministic: the same bytes on every run.
"""

import os
import sys

ENTRY = "Out of office: last watered in March. Your email is now a raisin \u2014 I\u2019ll reply when someone remembers I\u2019m alive."


def validate(text):
    """Gate: UTF-8 text of 1 to 120 characters, not only white space."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 120):
        raise ValueError("entry must be 1 to 120 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    with open(path, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != ENTRY:
        raise SystemExit("read-back mismatch: entry.txt does not match ENTRY")
    return 0


if __name__ == "__main__":
    sys.exit(main())
