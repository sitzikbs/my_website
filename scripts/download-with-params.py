#!/usr/bin/env python3
"""
Download images using the ACTUAL URLs from blog-index.json (with query parameters intact).
The previous script was stripping query parameters which caused downloads to fail.
"""

import json
import urllib.request
import urllib.error
import ssl
import os
from pathlib import Path
import re

# Create SSL context that doesn't verify certificates
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

def is_valid_image(file_path):
    """Check if file is a valid image by reading its signature."""
    if not os.path.exists(file_path):
        return False
    
    try:
        with open(file_path, 'rb') as f:
            header = f.read(16)
            if len(header) < 4:
                return False
            
            # Check for HTML (common for 404 pages)
            if header.startswith(b'<!DO') or header.startswith(b'<htm') or header.startswith(b'<HTM'):
                return False
            
            # JPEG
            if header[:2] == b'\xff\xd8':
                return True
            # PNG
            if header[:8] == b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a':
                return True
            # GIF
            if header[:3] == b'GIF':
                return True
            # WebP
            if header[:4] == b'RIFF' and header[8:12] == b'WEBP':
                return True
            return False
            
    except Exception as e:
        return False

def get_local_path_from_url(url):
    """Extract local file path from WordPress URL."""
    # Extract the filename from wp-content/uploads path
    match = re.search(r'/wp-content/uploads/\d{4}/\d{2}/([^?]+)', url)
    if match:
        filename = match.group(1)
        return f"assets/images/blog/{filename}"
    
    # Handle i0-3.wp.com URLs
    match = re.search(r'i[0-3]\.wp\.com/[^/]+/wp-content/uploads/\d{4}/\d{2}/([^?]+)', url)
    if match:
        filename = match.group(1)
        return f"assets/images/blog/{filename}"
    
    return None

def download_image(url, local_path):
    """Download an image from URL to local path."""
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        # Try to download - DON'T strip query parameters!
        request = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        with urllib.request.urlopen(request, context=ssl_context, timeout=30) as response:
            content = response.read()
            
            # Save to temp file first
            temp_path = local_path + '.tmp'
            with open(temp_path, 'wb') as f:
                f.write(content)
            
            # Verify it's valid
            if is_valid_image(temp_path):
                os.rename(temp_path, local_path)
                return True, len(content)
            else:
                os.remove(temp_path)
                return False, "Not a valid image"
                
    except Exception as e:
        return False, str(e)

def main():
    """Download missing images from URLs in blog-index.json."""
    
    # Load blog-index.json
    with open('data/blog-index.json', 'r') as f:
        content = f.read()
    
    # Find all WordPress URLs (keep query parameters!)
    wp_urls = set()
    
    # Pattern for i[0-3].wp.com URLs
    wp_urls.update(re.findall(r'https://i[0-3]\.wp\.com/[^"]+', content))
    
    # Pattern for direct WordPress URLs
    wp_urls.update(re.findall(r'https://www\.itzikbs\.com/wp-content/[^"]+', content))
    
    print(f"Found {len(wp_urls)} WordPress URLs in blog-index.json")
    print()
    
    # Group by local filename to avoid duplicate downloads
    url_by_file = {}
    for url in wp_urls:
        local_path = get_local_path_from_url(url)
        if local_path:
            if local_path not in url_by_file:
                url_by_file[local_path] = []
            url_by_file[local_path].append(url)
    
    print(f"Unique files to download: {len(url_by_file)}")
    print()
    
    successful = 0
    failed = 0
    skipped = 0
    
    for i, (local_path, urls) in enumerate(sorted(url_by_file.items()), 1):
        filename = os.path.basename(local_path)
        print(f"[{i}/{len(url_by_file)}] {filename}...", end=' ')
        
        # Skip if already exists and valid
        if is_valid_image(local_path):
            print(f"✓ Already exists")
            skipped += 1
            continue
        
        # Try the first URL (they all point to same file, just different sizes)
        # Use the one with highest resolution
        best_url = urls[0]
        for url in urls:
            if 'fit=2560' in url or 'ssl=1' in url and '?' in url:
                best_url = url
                break
        
        result, info = download_image(best_url, local_path)
        if result:
            print(f"✅ {info:,} bytes")
            successful += 1
        else:
            print(f"❌ {info}")
            failed += 1
    
    print()
    print("="*80)
    print(f"Download complete: {successful} downloaded, {skipped} skipped, {failed} failed")
    print("="*80)

if __name__ == "__main__":
    main()
