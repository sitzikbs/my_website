#!/usr/bin/env python3
"""
Compare all blog images with backup archive and identify upgrades.
This script scans blog posts, checks current image dimensions, 
and looks for higher resolution versions in the backup.
"""

import subprocess
import json
from pathlib import Path
import re

BACKUP_ARCHIVE = "/mnt/c/Users/sitzi/Downloads/download_havrakon_1767420934_64223.tar.gz"
BLOG_IMAGES_DIR = Path("assets/images/blog")
IMAGE_MAPPING_FILE = Path("data/image-mapping.json")

def get_image_dimensions(image_path):
    """Get dimensions of a local image file."""
    try:
        result = subprocess.run(
            ['identify', '-format', '%wx%h', str(image_path)],
            capture_output=True,
            text=True,
            check=True
        )
        dims = result.stdout.strip()
        if 'x' in dims:
            w, h = dims.split('x')
            return int(w), int(h)
    except:
        pass
    return None, None

def build_archive_index():
    """Build an index of all files in the archive (once)."""
    print("Building archive index (this may take a minute)...")
    try:
        cmd = f'tar -tzf "{BACKUP_ARCHIVE}" 2>/dev/null | grep -E "\\.(jpg|jpeg|png|gif)$"'
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=120
        )
        
        # Build a dictionary: filename -> full path
        archive_index = {}
        for line in result.stdout.strip().split('\n'):
            if line:
                filename = line.split('/')[-1]
                # Skip size variants, keep only originals
                if not any(x in filename for x in ['-1024x', '-768x', '-300x', '-150x']):
                    # If multiple paths exist, prefer the one without size suffix
                    if filename not in archive_index or len(line) < len(archive_index[filename]):
                        archive_index[filename] = line
        
        print(f"Found {len(archive_index)} images in archive\n")
        return archive_index
    except Exception as e:
        print(f"Error building archive index: {e}")
        return {}

def get_archive_image_dimensions(archive_path):
    """Extract and check dimensions of an image from the archive."""
    if not archive_path:
        return None, None
    
    try:
        # Extract to stdout and pipe to identify
        cmd = f'tar -xzOf "{BACKUP_ARCHIVE}" "{archive_path}" 2>/dev/null | identify -format "%wx%h" - 2>/dev/null'
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        dims = result.stdout.strip()
        if dims and 'x' in dims:
            w, h = dims.split('x')
            return int(w), int(h)
    except:
        pass
    return None, None

def main():
    print("Scanning blog images for potential upgrades...")
    print("=" * 70)
    
    # Build archive index once
    archive_index = build_archive_index()
    if not archive_index:
        print("Failed to build archive index")
        return
    
    # Get all images in blog directory
    image_files = sorted([f for f in BLOG_IMAGES_DIR.glob("*") 
                         if f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif']])
    
    upgradeable = []
    checked = 0
    
    print(f"Comparing {len(image_files)} local images with backup...")
    print()
    
    for img_path in image_files:
        filename = img_path.name
        
        # Skip if it's a generated or processed variant
        if any(x in filename for x in ['_old', '_new', '-scaled', '-1024x', '-768x', '-300x', '-150x']):
            continue
        
        checked += 1
        if checked % 20 == 0:
            print(f"Progress: {checked}/{len(image_files)} images checked, {len(upgradeable)} upgrades found so far...")
        
        # Get current dimensions
        current_w, current_h = get_image_dimensions(img_path)
        if not current_w:
            continue
        
        # Look for the file in backup using index
        archive_path = archive_index.get(filename)
        if not archive_path:
            continue
        
        # Get backup dimensions
        backup_w, backup_h = get_archive_image_dimensions(archive_path)
        if not backup_w:
            continue
        
        # Compare
        current_pixels = current_w * current_h
        backup_pixels = backup_w * backup_h
        
        if backup_pixels > current_pixels * 1.1:  # At least 10% more pixels
            ratio = backup_pixels / current_pixels
            upgradeable.append({
                'filename': filename,
                'current': f"{current_w}x{current_h}",
                'backup': f"{backup_w}x{backup_h}",
                'archive_path': archive_path,
                'improvement': f"{ratio:.1f}x"
            })
    
    print(f"\nCompleted scanning {checked} images.")
    print("=" * 70)
    print(f"\nFound {len(upgradeable)} images that can be upgraded:\n")
    
    for img in upgradeable:
        print(f"📷 {img['filename']}")
        print(f"   Current: {img['current']} → Backup: {img['backup']} ({img['improvement']} larger)")
        print(f"   Archive: {img['archive_path']}")
        print()
    
    # Save results to file
    if upgradeable:
        output_file = Path("upgradeable-images.json")
        with open(output_file, 'w') as f:
            json.dump(upgradeable, f, indent=2)
        print(f"Results saved to {output_file}")
        print(f"\nTo upgrade these images, run: python3 scripts/apply-image-upgrades.py")

if __name__ == "__main__":
    main()
