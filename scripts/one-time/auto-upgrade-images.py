#!/usr/bin/env python3
"""
Simple upgrade: Replace local images with backup versions if backup is larger.
"""

import shutil
import subprocess
from pathlib import Path
import re

BACKUP_DIR = Path("backup/homedir/sites/itzikbs.com/wp-content/uploads")
BLOG_IMAGES_DIR = Path("assets/images/blog")

def get_dimensions(img_path):
    try:
        result = subprocess.run(['identify', '-format', '%w %h', str(img_path)],
                              capture_output=True, text=True, check=True, timeout=5)
        w, h = result.stdout.strip().split()
        return int(w), int(h)
    except:
        return None, None

def find_in_backup(filename):
    # Strip WordPress size suffix if present
    original_name = re.sub(r'-\d+x\d+(\.[^.]+)$', r'\1', filename)
    
    for img_path in BACKUP_DIR.rglob(original_name):
        # Skip WordPress variants in backup
        if re.search(r'-\d+x\d+\.(jpg|jpeg|png)', img_path.name):
            continue
        return img_path
    return None

print("Upgrading images from backup...")
upgraded = 0
skipped = 0
notfound = 0

for local_img in sorted(BLOG_IMAGES_DIR.glob("*")):
    if local_img.suffix.lower() not in ['.jpg', '.jpeg', '.png', '.gif']:
        continue
    if '_old' in local_img.name or '_new' in local_img.name:
        continue
    
    # Get local dimensions
    local_w, local_h = get_dimensions(local_img)
    if not local_w:
        continue
    
    # Find in backup
    backup_img = find_in_backup(local_img.name)
    if not backup_img:
        notfound += 1
        continue
    
    # Get backup dimensions
    backup_w, backup_h = get_dimensions(backup_img)
    if not backup_w:
        continue
    
    # Compare
    if backup_w * backup_h > local_w * local_h * 1.05:  # 5% threshold
        # Backup old version
        shutil.copy2(local_img, str(local_img) + '.old')
        # Copy new version
        shutil.copy2(backup_img, local_img)
        upgraded += 1
        print(f"✓ {local_img.name}: {local_w}x{local_h} → {backup_w}x{backup_h}")
    else:
        skipped += 1

print(f"\n{'='*70}")
print(f"Upgraded: {upgraded}")
print(f"Already good: {skipped}")
print(f"Not in backup: {notfound}")
