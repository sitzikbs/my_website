#!/usr/bin/env python3
"""
Analyze all WordPress URLs in the repository.
Find which images need to be downloaded and which already exist locally.
"""

import json
import os
import re
from pathlib import Path
from urllib.parse import urlparse, unquote

def extract_wordpress_urls(file_path):
    """Extract all WordPress URLs from a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern for WordPress URLs
    patterns = [
        r'https?://(?:www\.)?itzikbs\.com/wp-content/[^"\s]+',
        r'https?://i[0-3]\.wp\.com/[^"\s]+',
    ]
    
    urls = set()
    for pattern in patterns:
        urls.update(re.findall(pattern, content))
    
    return urls

def get_local_path_from_url(url):
    """Convert WordPress URL to local path."""
    # Remove query parameters
    url_no_query = url.split('?')[0]
    
    # Extract filename
    parsed = urlparse(url_no_query)
    path_parts = parsed.path.split('/')
    
    # Find the uploads folder and extract year/month/filename
    if 'uploads' in path_parts:
        idx = path_parts.index('uploads')
        # uploads/YYYY/MM/filename.ext
        remaining = path_parts[idx+1:]
        if len(remaining) >= 3:  # year/month/file
            filename = remaining[-1]
            return f"assets/images/blog/{filename}"
        elif len(remaining) >= 1:
            filename = remaining[-1]
            return f"assets/images/blog/{filename}"
    
    # Fallback: just use filename
    filename = path_parts[-1]
    return f"assets/images/blog/{filename}"

def main():
    print("=" * 80)
    print("WordPress URL Analysis")
    print("=" * 80)
    
    # Files to check
    files_to_check = [
        'data/blog-index.json',
        'data/blog.json',
    ]
    
    # Add all markdown blog posts
    blog_posts_dir = Path('blog/posts-md')
    if blog_posts_dir.exists():
        files_to_check.extend([str(f) for f in blog_posts_dir.glob('*.md')])
    
    all_urls = set()
    file_url_map = {}
    
    for file_path in files_to_check:
        if not os.path.exists(file_path):
            continue
        
        urls = extract_wordpress_urls(file_path)
        if urls:
            file_url_map[file_path] = urls
            all_urls.update(urls)
    
    print(f"\nTotal unique WordPress URLs found: {len(all_urls)}")
    print(f"Files containing WordPress URLs: {len(file_url_map)}")
    
    # Categorize URLs
    cdn_urls = [u for u in all_urls if 'wp.com' in u]
    direct_urls = [u for u in all_urls if 'itzikbs.com/wp-content' in u]
    
    print(f"\nURL Breakdown:")
    print(f"  CDN URLs (i[0-3].wp.com): {len(cdn_urls)}")
    print(f"  Direct WordPress URLs: {len(direct_urls)}")
    
    # Check which files already exist locally
    existing_files = []
    missing_files = []
    url_to_local = {}
    
    for url in all_urls:
        local_path = get_local_path_from_url(url)
        url_to_local[url] = local_path
        
        if os.path.exists(local_path):
            # Check if it's a real image or HTML
            with open(local_path, 'rb') as f:
                header = f.read(100)
            
            is_image = (
                header[:2] == b'\xff\xd8' or  # JPEG
                header[:4] == b'\x89PNG' or   # PNG
                header[:4] == b'GIF8' or      # GIF
                (header[:4] == b'RIFF' and header[8:12] == b'WEBP')  # WebP
            )
            
            if is_image:
                existing_files.append((url, local_path))
            else:
                missing_files.append((url, local_path, "corrupted"))
        else:
            missing_files.append((url, local_path, "missing"))
    
    print(f"\nFile Status:")
    print(f"  Existing valid images: {len(existing_files)}")
    print(f"  Missing or corrupted: {len(missing_files)}")
    
    if missing_files:
        print(f"\n{'='*80}")
        print(f"Missing/Corrupted Files ({len(missing_files)}):")
        print(f"{'='*80}")
        
        for url, local_path, status in sorted(missing_files, key=lambda x: x[1]):
            print(f"\n  {status.upper()}: {local_path}")
            print(f"    URL: {url}")
    
    # Save URLs to download
    urls_to_download = {url: local_path for url, local_path, _ in missing_files}
    
    with open('urls-to-download.json', 'w') as f:
        json.dump(urls_to_download, f, indent=2)
    
    print(f"\n{'='*80}")
    print(f"Saved {len(urls_to_download)} URLs to download in: urls-to-download.json")
    print(f"{'='*80}")

if __name__ == '__main__':
    main()
