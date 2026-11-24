"""Out-of-office one-liner for the make.fun bounty.

Writes a single deterministic out-of-office line to ``entry.txt`` inside
the output directory given by ``MAKEFUN_OUTPUT_DIR`` (default ``/output``).
The line is fixed text, so the output is identical on every run.
The output file is exactly the 83-character line plus one trailing
newline, written with an explicit ``newline`` so the line ending does
not depend on the platform running the program.
"""

import os

LINE = (
    "I'm out of office \u2014 my emails unionized and demanded "
    "I take a holiday, so I obeyed."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
