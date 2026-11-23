#!/usr/bin/env python3
"""Entry for make.fun 'The joke about the demo'.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt. Deterministic: the same text on every run.
"""

import os
from pathlib import Path

JOKE = "My agent fixed the crashed demo by reverting me to the version before I had opinions."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
