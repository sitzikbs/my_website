#!/usr/bin/env python3
"""
Remove WordPress-generated image size variants (duplicates with -WIDTHxHEIGHT suffix).
Keep only the base filename versions.
"""

from pathlib import Path
import re

BLOG_IMAGES_DIR = Path("assets/images/blog")

def main():
    print("Scanning for WordPress-generated size variants...")
    print("=" * 70)
    
    # Find all WordPress size variants (files with -300x225 style suffixes)
    wordpress_variants = []
    
    for img_path in sorted(BLOG_IMAGES_DIR.glob("*")):
        if img_path.suffix.lower() not in ['.jpg', '.jpeg', '.png', '.gif']:
            continue
        
        # Check if filename has WordPress size suffix pattern
        if re.search(r'-\d+x\d+\.(jpg|jpeg|png|gif)$', img_path.name, re.IGNORECASE):
            # Get the base filename (without size suffix)
            base_name = re.sub(r'-\d+x\d+(\.[^.]+)$', r'\1', img_path.name)
            base_path = BLOG_IMAGES_DIR / base_name
            
            # Check if the base file exists
            if base_path.exists():
                wordpress_variants.append((img_path, base_path))
            else:
                # Base doesn't exist - this variant might be the only version
                print(f"⚠️  {img_path.name} - no base file '{base_name}' found, keeping variant")
    
    print(f"\nFound {len(wordpress_variants)} WordPress-generated variants with base files\n")
    
    if not wordpress_variants:
        print("✅ No WordPress variant duplicates found!")
        return
    
    # Show samples
    print("Sample duplicates (showing first 10):")
    for variant_path, base_path in wordpress_variants[:10]:
        print(f"  Remove: {variant_path.name}")
        print(f"  Keep:   {base_path.name}")
        print()
    
    if len(wordpress_variants) > 10:
        print(f"... and {len(wordpress_variants) - 10} more\n")
    
    print(f"\nRemove {len(wordpress_variants)} WordPress variant duplicates? (y/n): ", end="")
    response = input().strip().lower()
    
    if response != 'y':
        print("Cancelled.")
        return
    
    # Remove variants
    removed = 0
    for variant_path, base_path in wordpress_variants:
        try:
            variant_path.unlink()
            removed += 1
            print(f"✓ Removed {variant_path.name}")
        except Exception as e:
            print(f"✗ Failed to remove {variant_path.name}: {e}")
    
    print(f"\n{'=' * 70}")
    print(f"Removed {removed}/{len(wordpress_variants)} WordPress variant duplicates")
    print("\nNext step: Run compare-with-extracted-backup.py to find real upgrades")

if __name__ == "__main__":
    main()
