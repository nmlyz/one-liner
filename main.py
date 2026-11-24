"""Write one deadpan one-line joke to a text file."""

import os
from pathlib import Path


def build_line() -> str:
    """Assemble the joke from its parts, in order."""
    speaker = 'I told my barber "just a trim"'
    misheard = 'and he heard "reinvent me,"'
    consequence = "and now I look like a man who owns a kayak."
    return " ".join([speaker, misheard, consequence])


OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def output_path() -> Path:
    """Resolve where the joke is written (OUTPUT_DIR overrides the default)."""
    return Path(os.environ.get("OUTPUT_DIR", DEFAULT_OUTPUT_DIR)) / OUTPUT_FILENAME


def write_entry(line: str) -> Path:
    """Write the line plus a trailing newline, creating the directory if needed."""
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(line + "\n", encoding="utf-8")
    return path


def main() -> None:
    write_entry(build_line())


if __name__ == "__main__":
    main()
