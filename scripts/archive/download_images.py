#!/usr/bin/env python3
"""
Download all WordPress CDN images locally for optimization.
Scans HTML files for i0.wp.com URLs and downloads them to assets/images/
"""

import os
import re
import json
import requests
from pathlib import Path
from urllib.parse import urlparse, unquote
from collections import defaultdict

# Configuration
WORDPRESS_CDN = "i0.wp.com"
OUTPUT_DIR = Path("assets/images")
MAPPING_FILE = Path("data/image-mapping.json")

# Image categories
CATEGORIES = {
    "profile": OUTPUT_DIR / "profile",
    "publications": OUTPUT_DIR / "publications",
    "blog": OUTPUT_DIR / "blog",
    "general": OUTPUT_DIR / "general",
}

def ensure_directories():
    """Create output directories if they don't exist"""
    for directory in CATEGORIES.values():
        directory.mkdir(parents=True, exist_ok=True)
    MAPPING_FILE.parent.mkdir(parents=True, exist_ok=True)

def find_html_files():
    """Find all HTML files in the project"""
    html_files = []
    
    # Root HTML files
    for file in Path(".").glob("*.html"):
        html_files.append(file)
    
    # Blog posts
    blog_posts_dir = Path("blog/posts")
    if blog_posts_dir.exists():
        for file in blog_posts_dir.glob("*.html"):
            html_files.append(file)
    
    return html_files

def extract_wordpress_images(html_content):
    """Extract all WordPress CDN image URLs from HTML"""
    # Pattern to match i0.wp.com URLs in src and srcset attributes
    patterns = [
        r'src=["\']([^"\']*' + WORDPRESS_CDN + r'[^"\']*)["\']',
        r'srcset=["\']([^"\']*' + WORDPRESS_CDN + r'[^"\']*)["\']',
    ]
    
    urls = set()
    for pattern in patterns:
        matches = re.finditer(pattern, html_content)
        for match in matches:
            url_string = match.group(1)
            # Extract individual URLs from srcset (can contain multiple URLs)
            for part in url_string.split(','):
                url = part.strip().split()[0]  # Remove size descriptor (e.g., "800w")
                if WORDPRESS_CDN in url:
                    urls.add(url)
    
    return list(urls)

def categorize_image(url, filename):
    """Determine the category for an image based on URL/filename"""
    url_lower = url.lower()
    filename_lower = filename.lower()
    
    if "portrait" in filename_lower or "profile" in filename_lower or "itzik" in filename_lower:
        return "profile"
    elif "publication" in url_lower or "paper" in url_lower or "teaser" in filename_lower:
        return "publications"
    elif "blog" in url_lower or "wp-content/uploads" in url_lower:
        # Most WordPress uploads are blog-related
        return "blog"
    else:
        return "general"

def download_image(url, category, mapping):
    """Download a single image and save to appropriate directory"""
    try:
        # Parse URL to get filename
        parsed = urlparse(url)
        path_parts = Path(unquote(parsed.path)).parts
        
        # Get original filename
        original_filename = path_parts[-1] if path_parts else "unknown.jpg"
        
        # Clean filename (remove query parameters)
        base_filename = original_filename.split('?')[0]
        
        # Determine category
        img_category = categorize_image(url, base_filename)
        output_path = CATEGORIES[img_category] / base_filename
        
        # Skip if already downloaded
        if output_path.exists():
            print(f"⏭️  Skipping (exists): {base_filename}")
            mapping[url] = str(output_path)
            return True
        
        # Download image
        print(f"⬇️  Downloading: {url}")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # Save image
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        # Get image size
        size_kb = len(response.content) / 1024
        print(f"✅ Saved to: {output_path} ({size_kb:.1f} KB)")
        
        # Update mapping
        mapping[url] = str(output_path)
        
        return True
        
    except Exception as e:
        print(f"❌ Error downloading {url}: {e}")
        return False

def generate_report(mapping):
    """Generate a report of downloaded images"""
    stats = defaultdict(lambda: {"count": 0, "total_size": 0})
    
    for url, local_path in mapping.items():
        path = Path(local_path)
        if path.exists():
            category = path.parent.name
            size = path.stat().st_size
            stats[category]["count"] += 1
            stats[category]["total_size"] += size
    
    print("\n" + "="*60)
    print("📊 DOWNLOAD REPORT")
    print("="*60)
    
    total_images = 0
    total_size = 0
    
    for category, data in sorted(stats.items()):
        count = data["count"]
        size_mb = data["total_size"] / (1024 * 1024)
        total_images += count
        total_size += data["total_size"]
        print(f"{category:15} {count:3} images  {size_mb:6.2f} MB")
    
    print("-"*60)
    total_mb = total_size / (1024 * 1024)
    print(f"{'TOTAL':15} {total_images:3} images  {total_mb:6.2f} MB")
    print("="*60)

def main():
    """Main execution"""
    print("🖼️  WordPress Image Download Script")
    print("="*60)
    
    # Setup
    ensure_directories()
    
    # Find all HTML files
    html_files = find_html_files()
    print(f"📄 Found {len(html_files)} HTML files to scan\n")
    
    # Extract all WordPress image URLs
    all_urls = set()
    for html_file in html_files:
        print(f"Scanning: {html_file}")
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            urls = extract_wordpress_images(content)
            all_urls.update(urls)
            if urls:
                print(f"  Found {len(urls)} WordPress images")
    
    print(f"\n📌 Total unique WordPress images found: {len(all_urls)}\n")
    
    if not all_urls:
        print("✅ No WordPress CDN images found!")
        return
    
    # Download images
    mapping = {}
    success_count = 0
    
    for i, url in enumerate(sorted(all_urls), 1):
        print(f"\n[{i}/{len(all_urls)}]")
        if download_image(url, "general", mapping):
            success_count += 1
    
    # Save mapping
    with open(MAPPING_FILE, 'w') as f:
        json.dump(mapping, f, indent=2)
    
    print(f"\n💾 Mapping saved to: {MAPPING_FILE}")
    
    # Generate report
    generate_report(mapping)
    
    print(f"\n✅ Successfully downloaded {success_count}/{len(all_urls)} images")
    print(f"❌ Failed to download {len(all_urls) - success_count} images\n")

if __name__ == "__main__":
    main()
