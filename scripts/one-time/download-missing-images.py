#!/usr/bin/env python3
"""
Download all missing WordPress images from Cloudflare cache.
"""

import json
import os
import urllib.request
import ssl
from pathlib import Path
import time

# Create SSL context that doesn't verify certificates
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

def download_image(url, output_path):
    """Download image from URL, trying multiple variants."""
    
    # Remove query parameters for cleaner URL
    clean_url = url.split('?')[0]
    
    # Try multiple URL patterns
    urls_to_try = [
        clean_url,
        clean_url.replace('https://www.itzikbs.com/', 'https://itzikbs.com/'),
    ]
    
    # Add CDN variants if not already a CDN URL
    if 'wp.com' not in clean_url:
        for i in range(4):
            cdn_url = f"https://i{i}.wp.com/{clean_url.replace('https://', '').replace('http://', '')}"
            urls_to_try.append(cdn_url)
    
    for try_url in urls_to_try:
        try:
            req = urllib.request.Request(try_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, context=ssl_context, timeout=30) as response:
                content = response.read()
                
                # Verify it's an actual image or file (not HTML)
                is_valid = (
                    content[:2] == b'\xff\xd8' or  # JPEG
                    content[:4] == b'\x89PNG' or   # PNG
                    content[:4] == b'GIF8' or      # GIF
                    (content[:4] == b'RIFF' and b'WEBP' in content[:20]) or  # WebP
                    content[:2] == b'PK' or  # ZIP
                    content[:4] == b'%PDF'   # PDF
                )
                
                if is_valid or len(content) > 1000:  # Assume large files are valid
                    # Ensure directory exists
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    
                    with open(output_path, 'wb') as f:
                        f.write(content)
                    return True, len(content), try_url
                    
        except Exception as e:
            continue
    
    return False, 0, None

def main():
    # Load URLs to download
    with open('urls-to-download.json', 'r') as f:
        urls_to_download = json.load(f)
    
    print(f"Downloading {len(urls_to_download)} files...")
    print("=" * 80)
    
    # Group by unique filenames to avoid downloading same file multiple times
    file_to_urls = {}
    for url, local_path in urls_to_download.items():
        if local_path not in file_to_urls:
            file_to_urls[local_path] = []
        file_to_urls[local_path].append(url)
    
    print(f"Unique files to download: {len(file_to_urls)}")
    print("=" * 80)
    
    successful = []
    failed = []
    
    for i, (local_path, urls) in enumerate(file_to_urls.items(), 1):
        print(f"\n[{i}/{len(file_to_urls)}] {local_path}")
        
        # Try the first URL for this file
        url = urls[0]
        print(f"  Trying: {url[:80]}...")
        
        success, size, used_url = download_image(url, local_path)
        
        if success:
            print(f"  ✅ Downloaded {size:,} bytes from:")
            print(f"     {used_url}")
            successful.append(local_path)
        else:
            print(f"  ❌ Failed to download")
            failed.append((local_path, urls))
        
        # Small delay to be nice to the server
        time.sleep(0.1)
    
    print("\n" + "=" * 80)
    print(f"\nSummary:")
    print(f"  Successfully downloaded: {len(successful)}")
    print(f"  Failed: {len(failed)}")
    
    if failed:
        print(f"\n⚠️  Failed files:")
        for local_path, urls in failed:
            print(f"    {local_path}")
            print(f"      Tried: {urls[0][:80]}")

if __name__ == '__main__':
    main()
