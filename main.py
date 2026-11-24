"""Write one original out-of-office one-liner to entry.txt.

Deterministic: the same line, byte for byte, on every run. No randomness,
no network, no clock, no input files.

The line: a plausible one-line out-of-office reply with a twist — the
emails unionized and demanded the holiday, so the human obeyed. It reads
like something a real person would actually set, has a voice of its own,
and uses every word: setup (out of office), surprise (unionized emails),
punchline (so I obeyed).
"""

import os

LINE = "I'm out of office \u2014 my emails unionized and demanded I take a holiday, so I obeyed."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
