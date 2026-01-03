#!/usr/bin/env python3
"""
Fix the image mapping issue by:
1. Downloading all date-specific versions of images
2. Saving them with date prefixes to keep them unique
3. Updating blog-index.json to point to the correct version for each post
"""

import json
import urllib.request
import ssl
import os
import re

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

def is_valid_image(file_path):
    """Check if file is a valid image."""
    if not os.path.exists(file_path):
        return False
    try:
        with open(file_path, 'rb') as f:
            header = f.read(16)
            if len(header) < 2:
                return False
            if header.startswith(b'<!DO') or header.startswith(b'<htm'):
                return False
            return (header[:2] == b'\xff\xd8' or  # JPEG
                    header[:8] == b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a' or  # PNG
                    header[:3] == b'GIF' or  # GIF
                    (header[:4] == b'RIFF' and header[8:12] == b'WEBP'))  # WebP
    except:
        return False

def download(url, path):
    """Download file from URL."""
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        request = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0'
        })
        with urllib.request.urlopen(request, context=ssl_context, timeout=30) as response:
            content = response.read()
        temp = path + '.tmp'
        with open(temp, 'wb') as f:
            f.write(content)
        if is_valid_image(temp):
            os.rename(temp, path)
            return True, len(content)
        os.remove(temp)
        return False, "Invalid"
    except Exception as e:
        return False, str(e)

def extract_date_and_filename(url):
    """Extract date and filename from WordPress URL."""
    # Pattern: /YYYY/MM/filename.ext
    match = re.search(r'/(\d{4})/(\d{2})/([^/?]+\.(jpg|jpeg|png|gif|webp))', url, re.IGNORECASE)
    if match:
        year = match.group(1)
        month = match.group(2)
        filename = match.group(3)
        return year, month, filename
    return None, None, None

def main():
    # Load current blog-index.json
    with open('data/blog-index.json', 'r') as f:
        data = json.load(f)
    
    # Get original URLs from main branch
    import subprocess
    result = subprocess.run(['git', 'show', 'main:data/blog-index.json'], 
                          capture_output=True, text=True)
    original_data = json.loads(result.stdout)
    
    # Create a map of post ID to original image URL
    original_urls = {}
    for post in original_data.get('posts', []):
        if 'image' in post and ('itzikbs.com' in post['image'] or 'wp.com' in post['image']):
            original_urls[post['id']] = post['image']
    
    print(f"Found {len(original_urls)} posts with WordPress URLs")
    print()
    
    downloaded = 0
    skipped = 0
    failed = 0
    
    # Process each post
    for post in data.get('posts', []):
        post_id = post['id']
        
        if post_id not in original_urls:
            continue
        
        original_url = original_urls[post_id]
        year, month, filename = extract_date_and_filename(original_url)
        
        if not year or not month or not filename:
            print(f"⚠️  {post_id}: Could not parse URL: {original_url}")
            failed += 1
            continue
        
        # Create date-prefixed filename: YYYY-MM-original-filename.ext
        name, ext = os.path.splitext(filename)
        date_prefixed_filename = f"{year}-{month}-{filename}"
        local_path = f"assets/images/blog/{date_prefixed_filename}"
        
        print(f"📄 {post_id}: {date_prefixed_filename}...", end=' ')
        
        # Skip if already exists
        if is_valid_image(local_path):
            print(f"✓ Exists")
            post['image'] = f"/assets/images/blog/{date_prefixed_filename}"
            skipped += 1
            continue
        
        # Download the specific date version
        result, info = download(original_url, local_path)
        if result:
            print(f"✅ {info:,} bytes")
            post['image'] = f"/assets/images/blog/{date_prefixed_filename}"
            downloaded += 1
        else:
            print(f"❌ {info}")
            # Keep the generic version as fallback
            failed += 1
    
    # Write updated blog-index.json
    with open('data/blog-index.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print()
    print("="*80)
    print(f"Complete: {downloaded} downloaded, {skipped} skipped, {failed} failed")
    print("="*80)

if __name__ == "__main__":
    main()
