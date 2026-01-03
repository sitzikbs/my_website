#!/usr/bin/env python3
"""
Replace all WordPress URLs in blog-index.json with local paths.
Only replaces URLs where the local file actually exists.
"""

import json
import re
import os

def get_local_filename(url):
    """Extract filename from WordPress URL (ignores date path)."""
    match = re.search(r'/([^/]+\.(jpg|png|jpeg|gif|webp))', url, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

def main():
    # Load blog-index.json
    with open('data/blog-index.json', 'r') as f:
        data = json.load(f)
    
    replaced = 0
    missing = 0
    already_local = 0
    
    for entry in data.get('posts', []):
        if 'image' not in entry:
            continue
        
        img_url = entry['image']
        
        # Skip if already using local path
        if img_url.startswith('/assets/') or not ('itzikbs.com' in img_url or 'wp.com' in img_url):
            already_local += 1
            continue
        
        # Extract filename
        filename = get_local_filename(img_url)
        if not filename:
            print(f"⚠️  Could not extract filename from: {img_url}")
            continue
        
        # Check if file exists locally
        local_path = f"assets/images/blog/{filename}"
        if not os.path.exists(local_path):
            print(f"❌ Missing local file: {filename} (from {entry['id']})")
            missing += 1
            continue
        
        # Replace with local path
        new_path = f"/assets/images/blog/{filename}"
        entry['image'] = new_path
        replaced += 1
        print(f"✓ {entry['id']}: {filename}")
    
    # Write back to file
    with open('data/blog-index.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print()
    print("="*80)
    print(f"Complete: {replaced} URLs replaced, {already_local} already local, {missing} missing files")
    print("="*80)

if __name__ == "__main__":
    main()
