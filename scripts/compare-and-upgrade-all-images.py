#!/usr/bin/env python3
"""
Compare all blog post images with backup archive and upgrade to highest resolution.
Systematically checks every image in every blog post.
"""

import os
import re
import subprocess
import tarfile
from pathlib import Path
from collections import defaultdict

# Configuration
BLOG_DIR = Path("assets/images/blog")
BACKUP_PATH = "/mnt/c/Users/sitzi/Downloads/download_havrakon_1767420934_64223.tar.gz"
TEMP_DIR = Path("/tmp/image_comparison")

def get_image_dimensions(image_path):
    """Get dimensions of an image file."""
    try:
        result = subprocess.run(
            ['identify', '-format', '%w %h', str(image_path)],
            capture_output=True,
            text=True,
            check=True
        )
        width, height = map(int, result.stdout.strip().split())
        return width, height
    except:
        return None, None

def find_in_archive(archive_path, filename):
    """Find all matching files in the archive."""
    print(f"  Searching archive for: {filename}")
    try:
        result = subprocess.run(
            ['tar', '-tzf', archive_path],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        lines = result.stdout.split('\n')
        # Look for the original file (without size suffixes)
        base_name = filename.rsplit('.', 1)[0]
        ext = filename.rsplit('.', 1)[1] if '.' in filename else ''
        
        matches = []
        for line in lines:
            if not line:
                continue
            # Find exact filename match
            if line.endswith('/' + filename):
                matches.append(line)
            # Also check for the file without size suffix
            elif f'/{base_name}.{ext}' in line and not any(
                size_marker in line.split('/')[-1]
                for size_marker in ['-150x150', '-300x', '-768x', '-1024x', '-scaled']
            ):
                matches.append(line)
        
        return matches
    except Exception as e:
        print(f"  Error searching archive: {e}")
        return []

def extract_from_archive(archive_path, file_path, output_path):
    """Extract a specific file from the archive."""
    try:
        print(f"  Extracting: {file_path}")
        result = subprocess.run(
            ['tar', '-xzOf', archive_path, file_path],
            capture_output=True,
            timeout=60,
            check=True
        )
        
        with open(output_path, 'wb') as f:
            f.write(result.stdout)
        
        return output_path.exists()
    except Exception as e:
        print(f"  Extraction failed: {e}")
        return False

def get_all_blog_images():
    """Get all images referenced in blog posts."""
    images = set()
    
    # Scan all markdown files
    blog_posts_dir = Path("blog/posts-md")
    for md_file in blog_posts_dir.glob("*.md"):
        try:
            content = md_file.read_text()
            # Find all image references
            # Pattern 1: {% responsiveImage "path", "" %}
            for match in re.finditer(r'{%\s*responsiveImage\s+"([^"]+)"', content):
                img_path = match.group(1)
                # Extract just the filename
                filename = img_path.split('/')[-1]
                if filename:
                    images.add(filename)
            
            # Pattern 2: Regular img src="/assets/images/blog/..."
            for match in re.finditer(r'src="[^"]*assets/images/blog/([^"]+)"', content):
                filename = match.group(1).split('/')[-1]
                if filename:
                    images.add(filename)
                    
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
    
    return sorted(images)

def main():
    print("=" * 80)
    print("COMPREHENSIVE BLOG IMAGE COMPARISON AND UPGRADE")
    print("=" * 80)
    print()
    
    # Create temp directory
    TEMP_DIR.mkdir(exist_ok=True)
    
    # Get all images used in blog posts
    print("📋 Scanning all blog posts for images...")
    all_images = get_all_blog_images()
    print(f"Found {len(all_images)} unique images referenced in blog posts")
    print()
    
    # Track upgrades
    upgrades_needed = []
    upgrades_successful = []
    upgrades_failed = []
    no_upgrade_needed = []
    
    for i, filename in enumerate(all_images, 1):
        print(f"[{i}/{len(all_images)}] Checking: {filename}")
        
        current_path = BLOG_DIR / filename
        
        # Get current dimensions
        if not current_path.exists():
            print(f"  ⚠️  File not found locally, skipping")
            print()
            continue
        
        current_width, current_height = get_image_dimensions(current_path)
        if current_width is None:
            print(f"  ⚠️  Could not determine dimensions, skipping")
            print()
            continue
        
        print(f"  Current: {current_width}x{current_height}")
        
        # Search in archive
        matches = find_in_archive(BACKUP_PATH, filename)
        
        if not matches:
            print(f"  ℹ️  Not found in backup archive")
            no_upgrade_needed.append((filename, "Not in backup"))
            print()
            continue
        
        # Try to extract and compare
        best_match = None
        best_width = current_width
        best_height = current_height
        
        for match in matches:
            temp_file = TEMP_DIR / f"temp_{filename}"
            if extract_from_archive(BACKUP_PATH, match, temp_file):
                width, height = get_image_dimensions(temp_file)
                if width and width > best_width:
                    best_match = match
                    best_width = width
                    best_height = height
                    print(f"  Archive: {width}x{height} ✓ Better quality!")
                temp_file.unlink()
        
        if best_match and best_width > current_width:
            upgrades_needed.append((filename, best_match, current_width, best_width))
            print(f"  ✅ UPGRADE AVAILABLE: {current_width}x{current_height} → {best_width}x{best_height}")
        else:
            no_upgrade_needed.append((filename, f"Current is best ({current_width}x{current_height})"))
            print(f"  ✓ Current version is already best quality")
        
        print()
    
    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total images checked: {len(all_images)}")
    print(f"Upgrades available: {len(upgrades_needed)}")
    print(f"Already optimal: {len(no_upgrade_needed)}")
    print()
    
    if upgrades_needed:
        print("📥 IMAGES THAT CAN BE UPGRADED:")
        print("-" * 80)
        for filename, archive_path, old_size, new_size in upgrades_needed:
            print(f"  {filename}")
            print(f"    {old_size}px → {new_size}px")
            print(f"    Archive: {archive_path}")
        print()
        
        # Ask if user wants to upgrade
        print("Would you like to upgrade these images? (yes/no): ", end='')
        response = input().strip().lower()
        
        if response in ['yes', 'y']:
            print()
            print("=" * 80)
            print("UPGRADING IMAGES")
            print("=" * 80)
            print()
            
            for i, (filename, archive_path, old_size, new_size) in enumerate(upgrades_needed, 1):
                print(f"[{i}/{len(upgrades_needed)}] Upgrading: {filename}")
                
                current_path = BLOG_DIR / filename
                backup_path = BLOG_DIR / (filename + '.backup')
                temp_file = TEMP_DIR / filename
                
                # Extract
                if extract_from_archive(BACKUP_PATH, archive_path, temp_file):
                    # Verify it's better
                    width, height = get_image_dimensions(temp_file)
                    if width and width > old_size:
                        # Backup current
                        if current_path.exists():
                            current_path.rename(backup_path)
                        # Replace with new
                        temp_file.rename(current_path)
                        print(f"  ✅ Upgraded successfully: {old_size}px → {width}px")
                        upgrades_successful.append(filename)
                    else:
                        print(f"  ❌ Verification failed")
                        upgrades_failed.append(filename)
                        temp_file.unlink()
                else:
                    print(f"  ❌ Extraction failed")
                    upgrades_failed.append(filename)
                
                print()
            
            print("=" * 80)
            print("UPGRADE COMPLETE")
            print("=" * 80)
            print(f"Successfully upgraded: {len(upgrades_successful)}")
            print(f"Failed: {len(upgrades_failed)}")
            print()
            
            if upgrades_successful:
                print("✓ Upgraded images:")
                for f in upgrades_successful:
                    print(f"  - {f}")
                print()
                print("Note: Original files backed up with .backup extension")
                print("Run 'npm run build' to regenerate responsive image versions")

if __name__ == "__main__":
    main()
