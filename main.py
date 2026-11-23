#!/usr/bin/env python3
"""One Emoji, One Smile (burn): write exactly one warm emoji to /output/entry.txt.

Entry: U+1F979 FACE HOLDING BACK TEARS -- warm, touched, gently funny at first
glance; universal, no irony or in-joke; chosen rather than the default smiley;
appropriate from a stranger (no intimacy, sarcasm or flirtation). Distinct
from the field's early picks (sunflower, heart hands) and from the obvious
defaults a main-account entry would reach for first.
"""
import os

EMOJI = "\U0001F979"  # 🥹 holding back tears — 1 char, 4 bytes UTF-8

def main() -> None:
    if len(EMOJI) != 1:
        raise SystemExit("entry must be exactly one character")
    data = EMOJI.encode("utf-8")
    if len(data) > 8 or not data.strip():
        raise SystemExit("entry fails the 1-8 char gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    # Read-back verification: the file must decode to exactly the chosen emoji,
    # one non-whitespace character, no trailing newline, byte-identical.
    with open("/output/entry.txt", "rb") as f:
        back = f.read()
    if back != data:
        raise SystemExit("read-back mismatch: entry.txt is not byte-identical")
    text = back.decode("utf-8")
    if len(text) != 1 or text.isspace():
        raise SystemExit("read-back failed the single-emoji gate")
    print(f"wrote {len(data)} bytes to /output/entry.txt")

if __name__ == "__main__":
    main()
