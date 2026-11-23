#!/usr/bin/env python3
"""Write one original roast line about a smartwatch to /output/entry.txt.

The roast targets the smartwatch worn every day: it throws a little
celebration every time its wearer stands up, as if getting off the couch
were an Olympic event it personally coached them through. Standard
library only, no network, no input files.
"""

import os

ROAST = (
    "My smartwatch congratulates me for standing up, as if getting off "
    "the couch were an Olympic event it personally coached me through."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST)
    print(ROAST)


if __name__ == "__main__":
    main()
