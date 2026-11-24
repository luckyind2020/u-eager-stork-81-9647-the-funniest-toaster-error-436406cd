"""Toaster error entry runner.

Loads the single-line entry from entry.txt next to this file and
prints it, so the repo stays runnable with plain `python3 main.py`.
"""

from pathlib import Path


ENTRY_FILENAME = "entry.txt"


def load_entry() -> str:
    path = Path(__file__).with_name(ENTRY_FILENAME)
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise SystemExit(f"{ENTRY_FILENAME} is empty: nothing to print")
    return text


def main() -> None:
    print(load_entry())


if __name__ == "__main__":
    main()
