#!/usr/bin/env python3
"""
Consolidate blog images: Remove duplicates, keep highest resolution originals.
"""

import shutil
import subprocess
from pathlib import Path
import re
from collections import defaultdict

BLOG_IMAGES_DIR = Path("assets/images/blog")
BACKUP_DIR = Path("backup/homedir/sites/itzikbs.com/wp-content/uploads")
TEMP_BACKUP_DIR = Path("temp_image_backup")

def get_dimensions(img_path):
    """Get image dimensions using identify."""
    try:
        result = subprocess.run(['identify', '-format', '%w %h', str(img_path)],
                              capture_output=True, text=True, check=True, timeout=5)
        w, h = result.stdout.strip().split()
        return int(w), int(h)
    except:
        return None, None

def find_in_backup(filename):
    """Find original file in backup archive."""
    # Strip WordPress suffixes
    original_name = re.sub(r'-\d+x\d+(\.[^.]+)$', r'\1', filename)
    original_name = re.sub(r'-scaled(\.[^.]+)$', r'\1', original_name)
    
    for img_path in BACKUP_DIR.rglob(original_name):
        # Skip WordPress variants in backup
        if re.search(r'-\d+x\d+\.(jpg|jpeg|png)', img_path.name):
            continue
        if '-scaled' in img_path.name and original_name in img_path.name:
            continue
        return img_path
    return None

def get_base_name(filename):
    """Get base name without WordPress suffixes, but keep numbered variants (-1, -2)."""
    # First check if it has numbered variant (-1, -2, etc) before the extension
    match = re.match(r'(.+?)(-\d+)?(-scaled)?(-\d+x\d+)?(\.[^.]+)$', filename)
    if match:
        base = match.group(1)
        numbered = match.group(2) or ''
        ext = match.group(5)
        return base + numbered + ext
    return filename

def get_variant_type(filename):
    """Identify what type of variant this is."""
    if filename.endswith('.old'):
        return 'backup'
    if '.webp' in filename:
        return 'webp'
    if re.search(r'-\d+x\d+\.(jpg|jpeg|png|gif)$', filename):
        return 'wordpress_size'
    if re.search(r'-scaled\.(jpg|jpeg|png|gif)$', filename):
        return 'scaled'
    return 'original'

# Step 1: Remove .old backup files
print("="*70)
print("STEP 1: Removing .old backup files")
print("="*70)
old_files = list(BLOG_IMAGES_DIR.glob("*.old"))
for f in old_files:
    f.unlink()
    print(f"Removed: {f.name}")
print(f"✓ Removed {len(old_files)} .old backup files\n")

# Step 2: Delete WebP files from source
print("="*70)
print("STEP 2: Removing WebP files (belong in _site/)")
print("="*70)
webp_files = list(BLOG_IMAGES_DIR.glob("*.webp"))
for f in webp_files:
    f.unlink()
    print(f"Removed: {f.name}")
print(f"✓ Removed {len(webp_files)} WebP files\n")

# Step 3: Group images and consolidate to highest resolution
print("="*70)
print("STEP 3: Consolidating image variants")
print("="*70)

# Create backup directory
TEMP_BACKUP_DIR.mkdir(exist_ok=True)

# Group images by base name
image_groups = defaultdict(list)
for img in BLOG_IMAGES_DIR.glob("*"):
    if img.suffix.lower() not in ['.jpg', '.jpeg', '.png', '.gif']:
        continue
    base_name = get_base_name(img.name)
    variant_type = get_variant_type(img.name)
    
    if variant_type != 'backup' and variant_type != 'webp':
        image_groups[base_name].append(img)

consolidated = 0
deleted = 0

for base_name, variants in sorted(image_groups.items()):
    if len(variants) <= 1:
        continue  # No duplicates
    
    print(f"\nProcessing: {base_name}")
    
    # Get dimensions for each variant
    variant_info = []
    for v in variants:
        w, h = get_dimensions(v)
        if w and h:
            variant_info.append({
                'path': v,
                'width': w,
                'height': h,
                'pixels': w * h,
                'name': v.name
            })
            print(f"  - {v.name}: {w}x{h}")
    
    if not variant_info:
        continue
    
    # Sort by pixel count (highest first)
    variant_info.sort(key=lambda x: x['pixels'], reverse=True)
    
    # Keep the highest resolution
    best = variant_info[0]
    
    # If best isn't the base name, rename it
    target_path = BLOG_IMAGES_DIR / base_name
    if best['path'] != target_path:
        print(f"  ✓ Keeping: {best['name']} ({best['width']}x{best['height']})")
        # Backup to temp
        shutil.copy2(best['path'], TEMP_BACKUP_DIR / best['path'].name)
        # Rename to base name
        best['path'].rename(target_path)
        print(f"  → Renamed to: {base_name}")
        consolidated += 1
    else:
        print(f"  ✓ Already named correctly: {base_name} ({best['width']}x{best['height']})")
    
    # Delete other variants
    for v in variant_info[1:]:
        if v['path'].exists():  # Check if not already renamed
            shutil.copy2(v['path'], TEMP_BACKUP_DIR / v['path'].name)
            v['path'].unlink()
            print(f"  ✗ Deleted: {v['name']} ({v['width']}x{v['height']})")
            deleted += 1

print(f"\n✓ Consolidated {consolidated} image groups, deleted {deleted} lower-res variants\n")

# Step 4: Handle orphaned -scaled files
print("="*70)
print("STEP 4: Processing orphaned -scaled files")
print("="*70)

scaled_orphans = []
for img in BLOG_IMAGES_DIR.glob("*-scaled.*"):
    base_candidate = re.sub(r'-scaled(\.[^.]+)$', r'\1', img.name)
    if not (BLOG_IMAGES_DIR / base_candidate).exists():
        scaled_orphans.append(img)

renamed_from_backup = 0
kept_scaled = 0

for orphan in scaled_orphans:
    base_name = re.sub(r'-scaled(\.[^.]+)$', r'\1', orphan.name)
    backup_file = find_in_backup(base_name)
    
    if backup_file:
        backup_w, backup_h = get_dimensions(backup_file)
        orphan_w, orphan_h = get_dimensions(orphan)
        
        print(f"\n{orphan.name}:")
        print(f"  Local -scaled: {orphan_w}x{orphan_h}")
        print(f"  Backup original: {backup_w}x{backup_h}")
        
        if backup_w and backup_h and backup_w * backup_h > orphan_w * orphan_h:
            # Use backup version
            shutil.copy2(orphan, TEMP_BACKUP_DIR / orphan.name)
            shutil.copy2(backup_file, BLOG_IMAGES_DIR / base_name)
            orphan.unlink()
            print(f"  ✓ Replaced with backup, renamed to: {base_name}")
            renamed_from_backup += 1
        else:
            # Keep -scaled but rename to base
            shutil.copy2(orphan, TEMP_BACKUP_DIR / orphan.name)
            orphan.rename(BLOG_IMAGES_DIR / base_name)
            print(f"  ✓ Renamed to: {base_name}")
            kept_scaled += 1
    else:
        # No backup found, just rename
        shutil.copy2(orphan, TEMP_BACKUP_DIR / orphan.name)
        orphan.rename(BLOG_IMAGES_DIR / base_name)
        print(f"\n{orphan.name}: No backup found, renamed to: {base_name}")
        kept_scaled += 1

print(f"\n✓ Processed {len(scaled_orphans)} orphaned -scaled files")
print(f"  - Replaced from backup: {renamed_from_backup}")
print(f"  - Renamed from -scaled: {kept_scaled}\n")

# Step 5: Compare with backup and upgrade
print("="*70)
print("STEP 5: Comparing with backup for upgrades")
print("="*70)

upgraded = 0
already_good = 0
not_in_backup = 0

for local_img in sorted(BLOG_IMAGES_DIR.glob("*")):
    if local_img.suffix.lower() not in ['.jpg', '.jpeg', '.png', '.gif']:
        continue
    if '_old' in local_img.name or '_new' in local_img.name:
        continue
    
    local_w, local_h = get_dimensions(local_img)
    if not local_w:
        continue
    
    backup_img = find_in_backup(local_img.name)
    if not backup_img:
        not_in_backup += 1
        continue
    
    backup_w, backup_h = get_dimensions(backup_img)
    if not backup_w:
        continue
    
    if backup_w * backup_h > local_w * local_h * 1.05:
        shutil.copy2(local_img, TEMP_BACKUP_DIR / (local_img.name + '.pre-upgrade'))
        shutil.copy2(backup_img, local_img)
        upgraded += 1
        print(f"✓ {local_img.name}: {local_w}x{local_h} → {backup_w}x{backup_h}")
    else:
        already_good += 1

print(f"\n✓ Upgraded: {upgraded}")
print(f"  Already optimal: {already_good}")
print(f"  Not in backup: {not_in_backup}\n")

# Step 6: Check for broken references
print("="*70)
print("STEP 6: Checking blog posts for invalid image references")
print("="*70)

posts_dir = Path("blog/posts-md")
broken_refs = []

for post in posts_dir.glob("*.md"):
    content = post.read_text()
    
    # Find image references with -scaled or -WIDTHxHEIGHT
    scaled_refs = re.findall(r'[\'"]([^"\']*?-scaled\.[^"\']+)[\'"]', content)
    sized_refs = re.findall(r'[\'"]([^"\']*?-\d+x\d+\.[^"\']+)[\'"]', content)
    
    for ref in scaled_refs + sized_refs:
        if 'blog' in ref:
            broken_refs.append((post.name, ref))
            print(f"⚠ {post.name}: {ref}")

if broken_refs:
    print(f"\n⚠ Found {len(broken_refs)} references to variant filenames")
    print("  These should be updated to reference base filenames")
else:
    print("✓ No broken references found")

print("\n" + "="*70)
print("CLEANUP COMPLETE")
print("="*70)
print(f"Backups saved to: {TEMP_BACKUP_DIR}/")
print(f"Total files cleaned: {len(old_files) + len(webp_files) + deleted}")
print(f"Total upgrades: {consolidated + renamed_from_backup + upgraded}")
