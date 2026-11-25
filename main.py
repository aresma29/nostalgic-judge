"""Print the nostalgic one-line entry stored in entry.txt.

The entry file is resolved relative to this script, so the program
works from any working directory on a read-only filesystem.
"""

from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    print(entry_path.read_text(encoding="utf-8").strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
