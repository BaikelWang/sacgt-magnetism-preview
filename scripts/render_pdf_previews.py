#!/usr/bin/env python3
"""Render PDF figures to PNG previews for GitHub display.

Usage:
    python scripts/render_pdf_previews.py assets/figures/main
"""
from pathlib import Path
import argparse
import fitz

def render_folder(folder: Path, scale: float = 2.0):
    for pdf in sorted(folder.glob("*.pdf")):
        doc = fitz.open(pdf)
        page = doc[0]
        pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
        out = pdf.with_suffix(".png")
        pix.save(out)
        print(f"wrote {out}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder", type=Path)
    ap.add_argument("--scale", type=float, default=2.0)
    args = ap.parse_args()
    render_folder(args.folder, args.scale)

if __name__ == "__main__":
    main()
