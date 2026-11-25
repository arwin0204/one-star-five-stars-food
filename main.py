#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun bounty entry.

Writes a single-sentence, one-star review of planet Earth by an alien
tourist that still slips in a genuine compliment about the food.

Deterministic: no network, no randomness, no reads outside this repo.
Output goes only to the grader's output directory (argv[1], or the
MAKEFUN_OUTPUT_DIR env var, or /output), never into this repository.
"""

import os
import sys

ENTRY = (
    "One star: Earth makes me pay to sleep, leaks sky-water without "
    "warning, and its gravity will not let me leave — but the tacos "
    "were so good I nearly defected to your species."
)


def main() -> int:
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "MAKEFUN_OUTPUT_DIR", "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
