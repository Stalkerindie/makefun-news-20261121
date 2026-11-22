#!/usr/bin/env python3
"""make.fun entry: Sum up 21 November's world news in one image.

Writes the entry image to /output/entry.png (or $MAKEFUN_OUTPUT_DIR).
No network, no randomness: it copies the image bundled in this repo.
The image is a JPEG (the rules tell PNG and JPEG apart by first bytes
and the output name stays entry.png either way).
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "entry.jpg")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    sys.exit(main())
