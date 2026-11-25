#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single original sentence pitching a ridiculous invention that
fixes a tiny everyday annoyance to ``entry.txt``.

Standard library only.
"""

import os
import sys

ENTRY = (
    "The Guilt Microwave ends the forgotten-lunch beep by eating one "
    "spoonful of your food for every minute you ignore it, so dinner "
    "arrives hot, on time, and mysteriously smaller."
)


def main() -> int:
    """Write the entry sentence to entry.txt and exit 0 on success."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
