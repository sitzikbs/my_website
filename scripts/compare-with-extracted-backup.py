#!/usr/bin/env python3
"""
Compare blog images with extracted backup and upgrade to higher resolution versions.
"""

import subprocess
import shutil
from pathlib import Path

BACKUP_DIR = Path("backup/homedir/sites/itzikbs.com/wp-content/uploads")
BLOG_IMAGES_DIR = Path("assets/images/blog")

def get_image_dimensions(image_path):
    """Get dimensions of an image file."""
    try:
        result = subprocess.run(
            ['identify', '-format', '%w %h', str(image_path)],
            capture_output=True,
            text=True,
            check=True,
            timeout=5
        )
        w, h = result.stdout.strip().split()
        return int(w), int(h)
    except:
        return None, None

def find_original_in_backup(filename, backup_dir):
    """Find the original (non-resized) version of an image in backup."""
    import re
    
    # If the local filename has a WordPress size suffix (e.g., image-300x225.jpg),
    # strip it to find the original (e.g., image.jpg)
    original_name = re.sub(r'-\d+x\d+(\.[^.]+)$', r'\1', filename)
    
    # Look for the original filename in backup
    for img_path in backup_dir.rglob(original_name):
        # Skip WordPress auto-generated size variants in backup
        if any(x in str(img_path) for x in ['-1024x', '-768x', '-600x', '-300x', '-150x']):
            continue
        return img_path
    return None

def main():
    if not BACKUP_DIR.exists():
        print(f"Error: Backup directory not found at {BACKUP_DIR}")
        print("Please extract the backup first!")
        return
    
    print("Comparing blog images with backup...")
    print("=" * 70)
    
    upgradeable = []
    checked = 0
    total = 0
    
    # Get all images
    image_files = sorted([f for f in BLOG_IMAGES_DIR.glob("*") 
                         if f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif']])
    
    for img_path in image_files:
        filename = img_path.name
        
        # Skip temp/variant files
        if any(x in filename for x in ['_old', '_new', '-scaled']):
            continue
        
        total += 1
        
        # Get current dimensions
        current_w, current_h = get_image_dimensions(img_path)
        if not current_w:
            continue
        
        # Find in backup
        backup_path = find_original_in_backup(filename, BACKUP_DIR)
        if not backup_path:
            continue
        
        checked += 1
        if checked % 50 == 0:
            print(f"Progress: {checked} images found in backup, {len(upgradeable)} upgrades identified...")
        
        # Get backup dimensions
        backup_w, backup_h = get_image_dimensions(backup_path)
        if not backup_w:
            continue
        
        # Compare
        current_pixels = current_w * current_h
        backup_pixels = backup_w * backup_h
        
        if backup_pixels > current_pixels * 1.05:  # At least 5% more pixels
            ratio = backup_pixels / current_pixels
            upgradeable.append({
                'filename': filename,
                'current': (current_w, current_h),
                'backup': (backup_w, backup_h),
                'backup_path': backup_path,
                'local_path': img_path,
                'ratio': ratio
            })
    
    print(f"\nScanned {total} local images")
    print(f"Found {checked} images in backup")
    print(f"Identified {len(upgradeable)} images that can be upgraded")
    print("=" * 70)
    
    if not upgradeable:
        print("\n✅ All images are already at their best resolution!")
        return
    
    # Categorize upgrades
    tiny = [img for img in upgradeable if img['current'][0] < 400]
    small = [img for img in upgradeable if 400 <= img['current'][0] < 800]
    medium = [img for img in upgradeable if 800 <= img['current'][0] < 1200]
    large = [img for img in upgradeable if img['current'][0] >= 1200]
    
    print(f"\n📊 Upgrade Summary:")
    print(f"  - {len(tiny)} tiny images (< 400px wide)")
    print(f"  - {len(small)} small images (400-800px)")
    print(f"  - {len(medium)} medium images (800-1200px)")
    print(f"  - {len(large)} large images (>= 1200px)")
    
    print(f"\nTop 20 largest improvements:\n")
    
    for img in sorted(upgradeable, key=lambda x: x['ratio'], reverse=True)[:20]:
        curr = img['current']
        back = img['backup']
        print(f"📷 {img['filename']}")
        print(f"   Current: {curr[0]}x{curr[1]} → Backup: {back[0]}x{back[1]} ({img['ratio']:.1f}x larger)")
    
    if len(upgradeable) > 20:
        print(f"\n... and {len(upgradeable) - 20} more")
    
    # Ask to proceed
    print(f"\n\nUpgrade {len(upgradeable)} images? (y/n): ", end="")
    response = input().strip().lower()
    
    if response != 'y':
        print("Cancelled.")
        return
    
    # Perform upgrades
    print("\nUpgrading images...")
    upgraded = 0
    
    for img in upgradeable:
        try:
            # Backup current
            backup_name = img['local_path'].with_suffix(img['local_path'].suffix + '.old')
            shutil.copy2(img['local_path'], backup_name)
            
            # Copy new version
            shutil.copy2(img['backup_path'], img['local_path'])
            
            # Verify
            new_w, new_h = get_image_dimensions(img['local_path'])
            if new_w == img['backup'][0] and new_h == img['backup'][1]:
                upgraded += 1
                print(f"✓ {img['filename']}: {img['current'][0]}x{img['current'][1]} → {new_w}x{new_h}")
            else:
                # Restore if verification failed
                shutil.copy2(backup_name, img['local_path'])
                print(f"✗ {img['filename']}: Verification failed, restored original")
        except Exception as e:
            print(f"✗ {img['filename']}: Error - {e}")
    
    print(f"\n{'=' * 70}")
    print(f"Successfully upgraded {upgraded}/{len(upgradeable)} images")
    print("\nNext steps:")
    print("1. Rebuild site: npm run build")
    print("2. Test locally: python3 -m http.server 8080 --directory _site")
    print("3. Commit: git add assets/images/blog/ && git commit -m 'fix: upgrade blog images to higher resolution'")
    print("4. Push: git push")

if __name__ == "__main__":
    main()
