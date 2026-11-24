#!/usr/bin/env python3
"""One Line, One Chill — a single line of horror.

Writes exactly one line of horror text to /output/entry.txt, then reads
the file back and verifies it matches the intended line exactly.
"""

import sys

LINE = (
    "I have lived alone for six years, and this morning there were "
    "two toothbrushes in the holder, one of them still wet."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)

    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()

    if written != LINE:
        print("error: written content does not match the line", file=sys.stderr)
        return 1
    if not 1 <= len(written) <= 200:
        print("error: line length out of range (1-200)", file=sys.stderr)
        return 1
    if not written.endswith("."):
        print("error: line does not end with a period", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
