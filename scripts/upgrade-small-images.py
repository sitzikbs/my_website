#!/usr/bin/env python3
"""
Find and upgrade small images in the blog to higher resolution versions.
For Twitter/X images, attempts to download the original full-size version.
"""

import os
import json
import subprocess
from pathlib import Path

# Base paths
BLOG_DIR = Path("assets/images/blog")
IMAGE_MAPPING_FILE = Path("data/image-mapping.json")

# Twitter image patterns - these can often be upgraded
TWITTER_PATTERNS = ["GQ", "FV"]  # Common Twitter image ID prefixes

def get_image_dimensions(image_path):
    """Get dimensions of an image file."""
    try:
        result = subprocess.run(
            ["identify", "-format", "%wx%h", str(image_path)],
            capture_output=True,
            text=True,
            check=True
        )
        width, height = map(int, result.stdout.strip().split('x'))
        return width, height
    except Exception as e:
        print(f"Error getting dimensions for {image_path}: {e}")
        return None, None

def find_small_images(max_width=500):
    """Find images that are smaller than the desired width."""
    small_images = []
    
    for image_file in BLOG_DIR.glob("*.jpg"):
        width, height = get_image_dimensions(image_file)
        if width and width < max_width:
            small_images.append({
                "file": image_file.name,
                "path": str(image_file),
                "width": width,
                "height": height
            })
    
    return sorted(small_images, key=lambda x: x["width"])

def find_original_url(image_name):
    """Find the original WordPress URL for an image."""
    try:
        with open(IMAGE_MAPPING_FILE) as f:
            mappings = json.load(f)
        
        target_path = f"assets/images/blog/{image_name}"
        
        # Find URLs that map to this image
        urls = [url for url, path in mappings.items() if path == target_path]
        
        # Sort by quality - prefer larger sizes
        def get_size_hint(url):
            if "?w=" in url:
                try:
                    return int(url.split("?w=")[1].split("&")[0])
                except:
                    pass
            if "resize=" in url:
                try:
                    dims = url.split("resize=")[1].split("&")[0]
                    return int(dims.split("%2C")[0])
                except:
                    pass
            return 0
        
        urls.sort(key=get_size_hint, reverse=True)
        return urls
    except Exception as e:
        print(f"Error finding URLs for {image_name}: {e}")
        return []

def main():
    print("Finding small images in blog directory...")
    small_images = find_small_images(max_width=500)
    
    print(f"\nFound {len(small_images)} images smaller than 500px wide:")
    print("-" * 80)
    
    for img in small_images:
        print(f"{img['file']:50} {img['width']}x{img['height']}")
        urls = find_original_url(img['file'])
        if urls:
            print(f"  Original URLs found: {len(urls)}")
            for url in urls[:2]:  # Show top 2
                print(f"    {url}")
        else:
            print(f"  No URL mapping found")
        print()

if __name__ == "__main__":
    main()
