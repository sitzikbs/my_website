#!/usr/bin/env python3
"""
Download ALL blog images from WordPress URLs and replace them with local paths.
Tries ORIGINAL (non-scaled) versions first as requested.
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
            # Check for valid image formats
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

def get_original_filename(url):
    """Extract original filename, removing -scaled suffix."""
    # Extract filename from URL
    match = re.search(r'/([^/]+)\.(jpg|jpeg|png|gif|webp)', url, re.IGNORECASE)
    if match:
        filename = match.group(1)
        ext = match.group(2)
        # Remove -scaled, -1, -2, etc. suffixes to get original
        original = re.sub(r'-scaled$', '', filename)
        return f"{original}.{ext}"
    return None

def get_local_path(filename):
    """Get local path for a filename."""
    return f"assets/images/blog/{filename}"

def try_download_original(url, local_path):
    """Try to download original (non-scaled) version first, then fallback to scaled."""
    # First, try the URL as-is (might already be original)
    if download(url, local_path)[0]:
        return True, "original URL"
    
    # Try removing query parameters and downloading original filename
    clean_url = url.split('?')[0]
    
    # If it has -scaled in it, try without -scaled
    if '-scaled' in clean_url:
        original_url = clean_url.replace('-scaled', '')
        if download(original_url, local_path)[0]:
            return True, f"original (non-scaled): {original_url}"
    
    # Try with CDN format
    if 'wp-content' in url:
        # Try i0.wp.com CDN
        cdn_url = f"https://i0.wp.com/www.itzikbs.com{clean_url.split('itzikbs.com')[1]}?ssl=1"
        if download(cdn_url, local_path)[0]:
            return True, f"CDN: {cdn_url}"
        
        # Try with fit parameter for high-res
        cdn_url_fit = f"https://i0.wp.com/www.itzikbs.com{clean_url.split('itzikbs.com')[1]}?fit=2560%2C2560&ssl=1"
        if download(cdn_url_fit, local_path)[0]:
            return True, f"CDN with fit: {cdn_url_fit}"
    
    # Last resort: try the original URL with parameters
    if download(url, local_path)[0]:
        return True, "with params"
    
    return False, "all attempts failed"

def main():
    # Load blog-index.json
    with open('data/blog-index.json', 'r') as f:
        blog_data = json.load(f)
    
    # Find all WordPress URLs
    wordpress_images = []
    for entry in blog_data.get('posts', []):
        if 'image' in entry:
            img_url = entry['image']
            if 'itzikbs.com/wp-content' in img_url or 'wp.com/' in img_url:
                wordpress_images.append((entry['id'], img_url))
    
    print(f"Found {len(wordpress_images)} blog entries with WordPress image URLs")
    print()
    
    successful = 0
    failed = 0
    skipped = 0
    
    for i, (entry_id, url) in enumerate(wordpress_images, 1):
        # Extract filename
        filename = get_original_filename(url)
        if not filename:
            print(f"[{i}/{len(wordpress_images)}] {entry_id}: ❌ Could not extract filename from {url}")
            failed += 1
            continue
        
        local_path = get_local_path(filename)
        
        print(f"[{i}/{len(wordpress_images)}] {filename}...", end=' ')
        
        # Skip if already exists and valid
        if is_valid_image(local_path):
            print(f"✓ Already exists")
            skipped += 1
            continue
        
        # Try to download (original first, then fallbacks)
        result, info = try_download_original(url, local_path)
        if result:
            size = os.path.getsize(local_path)
            print(f"✅ {size:,} bytes ({info})")
            successful += 1
        else:
            print(f"❌ Failed: {info}")
            failed += 1
    
    print()
    print("="*80)
    print(f"Complete: {successful} downloaded, {skipped} skipped, {failed} failed")
    print("="*80)
    print()
    print("Next step: Replace WordPress URLs in blog-index.json with local paths")

if __name__ == "__main__":
    main()
