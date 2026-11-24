"""Write the entry line for make.fun · u-azazex-one-line-one-chill-6d4d5488.

Deterministic, offline: one string constant, one file, no trailing newline.
"""

import os
from pathlib import Path

LINE = (
    "I pulled the batteries out of my daughter's nightlight in March, "
    "and it is still warm each night, and now she asks me to leave the hall light on for it."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
