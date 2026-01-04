#!/usr/bin/env python3
"""
Clean up generated image variants, keeping only source images.
Remove:
- .webp files (will be regenerated)
- -scaled versions (WordPress artifacts)
- Size variants like -200, -400, -800 (will be regenerated)
Keep:
- Original source images referenced in blog-index.json and markdown
"""

import os
import re
import json

def is_generated_variant(filename):
    """Check if file is a generated variant that can be removed."""
    # WebP files - these are generated
    if filename.endswith('.webp'):
        return True
    
    # Files with -scaled in the name (WordPress artifacts)
    if '-scaled' in filename and not filename.startswith(('2017-', '2018-', '2019-', '2020-', '2021-', '2022-', '2023-', '2024-', '2025-')):
        return True
    
    # Size variants like -200.jpg, -400.jpg, -800.jpg, -1200.jpg, -300x169.jpg
    if re.search(r'-\d+(x\d+)?\.(jpg|jpeg|png|gif)$', filename):
        return True
    
    return False

def main():
    blog_dir = 'assets/images/blog'
    
    # Count what we have
    all_files = [f for f in os.listdir(blog_dir) if os.path.isfile(os.path.join(blog_dir, f))]
    variants = [f for f in all_files if is_generated_variant(f)]
    
    print(f"Total files: {len(all_files)}")
    print(f"Generated variants to remove: {len(variants)}")
    print(f"Source images to keep: {len(all_files) - len(variants)}")
    print()
    
    # Show breakdown
    webp = [f for f in variants if f.endswith('.webp')]
    scaled = [f for f in variants if '-scaled' in f and not f.endswith('.webp')]
    size_variants = [f for f in variants if re.search(r'-\d+(x\d+)?\.(jpg|jpeg|png|gif)$', f)]
    
    print(f"Breakdown:")
    print(f"  WebP files: {len(webp)}")
    print(f"  -scaled versions: {len(scaled)}")
    print(f"  Size variants: {len(size_variants)}")
    print()
    
    response = input(f"Remove {len(variants)} generated variants? (yes/no): ")
    if response.lower() == 'yes':
        removed = 0
        for filename in variants:
            filepath = os.path.join(blog_dir, filename)
            try:
                os.remove(filepath)
                removed += 1
            except Exception as e:
                print(f"⚠️  Failed to remove {filename}: {e}")
        
        print(f"\n✅ Removed {removed} generated variant files")
        print(f"📁 {len(all_files) - removed} source images remain")
    else:
        print("Cancelled - no files removed")

if __name__ == "__main__":
    main()
