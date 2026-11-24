"""Two Lines to Your Past Self — make.fun entry.

Writes the two-line warning to /output/entry.txt.
Standard library only.
"""

import os

# Gate: /output/entry.txt must be UTF-8 text of 1 to 280 characters.
MAX_CHARS = 280

ENTRY = (
    "Don't click deploy at 4:47 p.m. on the Friday before launch.\n"
    "That one click takes the checkout page down for nine hours, and the apology email you write that night is still the first thing anyone finds when they search your name."
)


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(ENTRY)}")
    if ENTRY.count("\n") != 1:
        raise ValueError("entry must be exactly two lines")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back: the file on disk must be byte-identical to the entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise ValueError("read-back mismatch: /output/entry.txt != ENTRY")


if __name__ == "__main__":
    main()
