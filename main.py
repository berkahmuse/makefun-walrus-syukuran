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


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
