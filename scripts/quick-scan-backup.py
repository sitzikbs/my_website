#!/usr/bin/env python3
"""
Quick scan: Find images in backup that might be better quality.
Just checks if the file exists in backup, doesn't verify dimensions.
"""

import subprocess
from pathlib import Path

BACKUP_ARCHIVE = "/mnt/c/Users/sitzi/Downloads/download_havrakon_1767420934_64223.tar.gz"
BLOG_IMAGES_DIR = Path("assets/images/blog")

print("Building archive index...")
cmd = f'tar -tzf "{BACKUP_ARCHIVE}" 2>/dev/null | grep -E "wp-content/uploads/.*\\.(jpg|jpeg|png|gif)$"'
result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=120)

# Build index
archive_index = {}
for line in result.stdout.strip().split('\n'):
    if line:
        filename = line.split('/')[-1]
        # Skip size variants
        if not any(x in filename for x in ['-1024x', '-768x', '-300x', '-150x', '-600x']):
            if filename not in archive_index:
                archive_index[filename] = line

print(f"Found {len(archive_index)} original images in archive\n")

# Check local images
print("Checking local images...\n")
candidates = []

for img_path in sorted(BLOG_IMAGES_DIR.glob("*")):
    if img_path.suffix.lower() not in ['.jpg', '.jpeg', '.png', '.gif']:
        continue
    
    filename = img_path.name
    
    # Skip variants
    if any(x in filename for x in ['_old', '_new', '-scaled']):
        continue
    
    if filename in archive_index:
        candidates.append({
            'filename': filename,
            'archive_path': archive_index[filename],
            'local_size': img_path.stat().st_size
        })

print(f"Found {len(candidates)} images that exist in both local and backup\n")
print("Images to check (likely have originals in backup):")
print("=" * 70)

for c in candidates[:30]:  # Show first 30
    size_kb = c['local_size'] / 1024
    print(f"{c['filename']:50} ({size_kb:6.1f} KB)")

if len(candidates) > 30:
    print(f"\n... and {len(candidates) - 30} more")

print(f"\n\nTotal: {len(candidates)} images found in backup")
print("\nTo extract all originals, run:")
print("python3 scripts/extract-all-backup-images.py")
