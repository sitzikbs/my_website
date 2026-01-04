#!/usr/bin/env python3
"""
Clean up duplicate images in assets/images/blog/.
Remove old non-date-prefixed versions that have been replaced by date-prefixed ones.
Keep files that are actively referenced in blog-index.json.
"""

import os
import json

def main():
    # Load blog-index.json to see what's actually used
    with open('data/blog-index.json', 'r') as f:
        data = json.load(f)
    
    # Extract all referenced image files
    used_images = set()
    for post in data.get('posts', []):
        if 'image' in post:
            # Extract just the filename from the path
            img_path = post['image']
            if img_path.startswith('/assets/images/blog/'):
                filename = img_path.replace('/assets/images/blog/', '')
                used_images.add(filename)
    
    print(f"Found {len(used_images)} images referenced in blog-index.json")
    print()
    
    # List all images in the directory
    blog_dir = 'assets/images/blog'
    all_files = set()
    for filename in os.listdir(blog_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # Skip webp versions - those are generated
            all_files.add(filename)
    
    print(f"Found {len(all_files)} image files in {blog_dir}")
    print()
    
    # Find files not referenced
    unused = all_files - used_images
    
    # Filter to only files that might be duplicates
    # These are non-date-prefixed files where date-prefixed versions exist
    duplicates_to_remove = []
    for filename in sorted(unused):
        # Skip if it's already date-prefixed
        if filename[:4].isdigit() and filename[4] == '-':
            continue
        
        # Check if date-prefixed versions of this file exist
        base_name = filename
        has_dated_version = any(img.endswith(base_name) and img.startswith(('202', '201')) 
                               for img in used_images)
        
        if has_dated_version:
            duplicates_to_remove.append(filename)
            print(f"🗑️  {filename} (has date-prefixed versions)")
    
    print()
    print("="*80)
    print(f"Found {len(duplicates_to_remove)} duplicate files to remove")
    print("="*80)
    print()
    
    if duplicates_to_remove:
        response = input(f"Remove {len(duplicates_to_remove)} duplicate files? (yes/no): ")
        if response.lower() == 'yes':
            for filename in duplicates_to_remove:
                filepath = os.path.join(blog_dir, filename)
                os.remove(filepath)
                print(f"✓ Removed: {filename}")
            print()
            print(f"✅ Removed {len(duplicates_to_remove)} duplicate files")
        else:
            print("Cancelled - no files removed")
    else:
        print("No duplicate files found to remove")

if __name__ == "__main__":
    main()
