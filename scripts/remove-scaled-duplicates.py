#!/usr/bin/env python3
"""
Remove WordPress -scaled duplicates if the original file exists.
"""

from pathlib import Path
import re

BLOG_IMAGES_DIR = Path("assets/images/blog")

scaled_pattern = re.compile(r'-scaled(\.[^.]+)$')

removed = 0
kept = 0

for img in sorted(BLOG_IMAGES_DIR.glob("*-scaled.*")):
    # Get the base filename without -scaled
    base_name = scaled_pattern.sub(r'\1', img.name)
    base_path = img.parent / base_name
    
    if base_path.exists():
        print(f"Removing: {img.name} (original {base_name} exists)")
        img.unlink()
        removed += 1
    else:
        print(f"WARNING: {img.name} has no base file {base_name}")
        kept += 1

print(f"\n{'='*70}")
print(f"Removed: {removed} -scaled duplicates")
print(f"Kept: {kept} -scaled files without originals")
