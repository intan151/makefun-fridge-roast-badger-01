#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line (<= 200 chars) about a smart fridge to
/output/entry.txt, deterministically.
"""

ENTRY = (
    "My smart fridge pushed a firmware update at 3 a.m., rebooted for "
    "twenty minutes, then proudly announced the milk expired \u2014 three "
    "days after it watched me drink it."
)


def main() -> None:
    import os

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Self-check gate: the written entry must be byte-identical to ENTRY,
    # 1-200 chars, non-whitespace. Fails loudly instead of shipping a
    # drifted or invalid line.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt drifted from ENTRY"
    assert 1 <= len(written) <= 200, "entry must be 1-200 characters"
    assert written.strip(), "entry must not be only whitespace"
    print(ENTRY)


if __name__ == "__main__":
    main()
