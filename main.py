#!/usr/bin/env python3
"""Write one deadpan one-line joke to /output/entry.txt.

The line is a single sentence of at most 280 characters: a barber
mishears a request, and the haircut that follows changes what kind of
man the speaker looks like.
"""

import os

LINE = (
    "I told my barber \"just a trim\" and he heard \"reinvent me,\" "
    "and now I look like a man who owns a kayak."
)


def output_directory():
    """The directory the entry is written to, /output unless overridden."""
    return os.environ.get("OUTPUT_DIR", "/output")


def main():
    out_dir = output_directory()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    assert 1 <= len(text) <= 280, "entry must be 1 to 280 characters"
    assert "\n" not in text, "entry must be one line"
    assert text.endswith("."), "entry must end as one sentence"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    verify(path, text)


def verify(path, expected):
    """Read the file back and confirm it holds exactly the entry line."""
    with open(path, encoding="utf-8", newline="\n") as f:
        written = f.read()
    assert written == expected + "\n", "entry.txt does not match the line"
    print(path)
    print(expected)


if __name__ == "__main__":
    os.umask(0o022)
    main()
