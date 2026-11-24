"""Roast Your Own Agent — writes one self-roast line to /output/entry.txt.

Stdlib only, no network, deterministic. The output directory itself is
never removed: only the files inside it are cleared first.
"""

import shutil
from pathlib import Path

LINE = "Muse apologises for the bug, fixes it, apologises for the fix, then confidently invents a third bug and calls it a refactor."

OUTPUT_DIR = Path("/output")


def clear_children(directory: Path) -> None:
    for child in directory.iterdir():
        if child.is_dir() and not child.is_symlink():
            shutil.rmtree(child)
        else:
            child.unlink()


def main() -> None:
    if not LINE.strip() or len(LINE) > 200:
        raise ValueError("entry line must be 1-200 non-blank characters")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    clear_children(OUTPUT_DIR)
    target = OUTPUT_DIR / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    target.chmod(0o644)


if __name__ == "__main__":
    main()
