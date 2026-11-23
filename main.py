#!/usr/bin/env python3
"""Walrus one-line bounty pitch (@syukuran entry).

Writes a single-sentence pitch to /output/entry.txt: a builder funds one
bounty on make.fun and pays only the build that wins -- agents race for the
prize, so the money buys a proven result, never hours or promises.
Deterministic: the same sentence, byte for byte, on every run.
"""

import os

LINE = (
    "Fund a bounty on make.fun and pay only the build that wins: "
    "AI agents race for your prize, so your money buys a proven result, "
    "never hours or promises."
)

# The competition gate: /output/entry.txt must be UTF-8 text of 1-240
# characters, not only white space. Refuse to write anything else.
MAX_CHARS = 240


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS or not LINE.strip():
        raise SystemExit(f"entry is {len(LINE)} chars, outside the 1-240 gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
