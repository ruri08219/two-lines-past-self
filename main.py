"""Two Lines to Your Past Self — make.fun entry.

Writes the two-line warning to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = (
    "Don't click deploy at 4:47 p.m. on the Friday before launch.\n"
    "That one click takes the checkout page down for nine hours, and the apology email you write that night is still the first thing anyone finds when they search your name."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
