#!/usr/bin/env python3
"""
Upgrade WordPress images that were downloaded at low resolution but have
higher resolution versions available.
"""

import json
import subprocess
from pathlib import Path

BLOG_DIR = Path("assets/images/blog")
IMAGE_MAPPING_FILE = Path("data/image-mapping.json")

# Images to upgrade based on image-mapping.json analysis
IMAGES_TO_UPGRADE = {
    "IMG_20190619_194012.jpg": {
        "current": 300,
        "target": 1124,
        "path": "2019/06"
    },
    "boya_by_m1_microphone.jpg": {
        "current": 300,
        "target": 1000,
        "path": "2020/09"
    },
    "nyu_v2_1.png": {
        "current": 300,
        "target": 875,
        "path": "2019/04"
    },
}

def get_image_dimensions(image_path):
    """Get dimensions of an image file."""
    try:
        result = subprocess.run(
            ["identify", "-format", "%wx%h", str(image_path)],
            capture_output=True,
            text=True,
            check=True
        )
        width, height = map(int, result.stdout.strip().split('x'))
        return width, height
    except Exception:
        return None, None

def copy_from_backup(filename, wp_path):
    """Try to copy from Windows backup."""
    backup_path = f"/mnt/c/Users/sitzi/Downloads/itzikbs.com/itzikbs.com/wp-content/uploads/{wp_path}/{filename}"
    dest_path = BLOG_DIR / filename
    
    try:
        result = subprocess.run(
            ["cp", backup_path, str(dest_path)],
            capture_output=True,
            check=True
        )
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("Upgrading WordPress images to full resolution...")
    print("=" * 80)
    
    upgraded = 0
    skipped = 0
    failed = 0
    
    for filename, info in IMAGES_TO_UPGRADE.items():
        image_path = BLOG_DIR / filename
        
        if not image_path.exists():
            print(f"⏭️  {filename}: File not found, skipping")
            skipped += 1
            continue
        
        # Check current dimensions
        width, height = get_image_dimensions(image_path)
        if not width:
            print(f"⚠️  {filename}: Cannot read dimensions, skipping")
            skipped += 1
            continue
        
        if width >= info["target"]:
            print(f"✓  {filename}: Already at target resolution ({width}x{height})")
            skipped += 1
            continue
        
        print(f"📥 {filename}: Current {width}x{height}, upgrading to ~{info['target']}px...")
        
        # Try to copy from backup
        if copy_from_backup(filename, info["path"]):
            new_width, new_height = get_image_dimensions(image_path)
            if new_width and new_width > width:
                print(f"  ✅ Upgraded to {new_width}x{new_height}")
                upgraded += 1
            else:
                print(f"  ⚠️  Copy successful but not higher resolution")
                failed += 1
        else:
            print(f"  ❌ Failed to copy from backup")
            failed += 1
    
    print("\n" + "=" * 80)
    print(f"Summary: {upgraded} upgraded, {skipped} skipped, {failed} failed")
    
    if failed > 0:
        print("\nNote: Failed images may not be in the Windows backup.")
        print("The original files might have been uploaded at low resolution only.")

if __name__ == "__main__":
    main()
