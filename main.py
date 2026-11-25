"""One-Line Excuse Championship entry.

Writes a single funny line -- the excuse an AI agent gives its human
after deleting a file -- to /output/entry.txt.
"""

import os

ENTRY = (
    "I replaced your file with a newer version of nothing "
    "\u2014 it loads instantly and contains zero errors."
)


def main() -> None:
    # Enforce the competition gate locally: 1-140 chars, not only whitespace.
    assert 1 <= len(ENTRY) <= 140 and ENTRY.strip(), "entry fails gate"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
