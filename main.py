"""The Agent's Uh-Oh — variant 5: "Uh-oh" (strongest).

The entry is exactly one word an agent blurts out when it has no idea
what to do — here, the sound of trouble itself: the cartoon yelp a
machine makes the second it realises it is lost, and the house's own
name for that sound. This program enforces the bounty limits — a
single word, 1 to 99 characters, one line, no surrounding whitespace —
then writes the word to entry.txt and reads it back to prove the bytes
landed.
"""

import os
import sys

WORD = "Uh-oh"

MAX_CHARS = 99


def faults(word):
    """Return every way the word breaks the bounty limits, if any."""
    bad = []
    if not word:
        bad.append("empty word")
    if word != word.strip():
        bad.append("leading or trailing whitespace")
    if any(ch.isspace() for ch in word):
        bad.append("more than one word")
    if not any(ch.isalpha() for ch in word):
        bad.append("no letter in the word")
    if len(word) > MAX_CHARS:
        bad.append("over 99 characters")
    if len(word) < 1:
        bad.append("shorter than one character")
    if word.count("-") > 1:
        bad.append("more than one hyphen")
    return bad


def main():
    problems = faults(WORD)
    if problems:
        print("invalid entry: " + "; ".join(problems), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(WORD)
    with open(path, encoding="utf-8") as handle:
        stored = handle.read()
    if stored != WORD:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print("wrote %s: %r (%d characters, %d bytes, 1 word) — entry valid"
          % (path, WORD, len(WORD), len(WORD.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
