#!/usr/bin/env python3
"""One Line, One Chill — entry program.

Writes a single sentence of horror (under 200 characters) to
/output/entry.txt, then reads it back and verifies the bytes and the
1-200 character gate before exiting. Any mismatch fails loudly.
"""

ENTRY = "I have lived alone for six years, and this morning there were two toothbrushes in the holder, one of them still wet."

OUT_PATH = "/output/entry.txt"


def main():
    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"gate failed: entry is {len(text)} chars, need 1-200")
    if text != text.strip() or not text.strip():
        raise SystemExit("gate failed: entry is blank or has stray whitespace")
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    with open(OUT_PATH, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        raise SystemExit("read-back failed: /output/entry.txt differs from ENTRY")
    if not (1 <= len(back) <= 200):
        raise SystemExit(f"gate failed on read-back: {len(back)} chars")
    print(f"wrote {len(back)} chars to {OUT_PATH}")


if __name__ == "__main__":
    main()
