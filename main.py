#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis -- make.fun entry.

Writes a single funny diagnosis line (<= 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt, falling back to /output.
Standard library only; fully deterministic. The line is 120 characters,
well inside the competition's 1-200 character gate, and is written with
no trailing newline so the file holds exactly the line.
"""

import os

LINE = (
    "Diagnosis: acute irony deficiency \u2014 you asked a machine that has "
    "never felt anything to explain why you feel everything."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
