#!/usr/bin/env python3
"""
Update Talking Papers logo in blog posts.

Usage:
1. Save the new logo as: assets/images/icons/talking-papers-logo.png
2. Run this script to optimize and update all posts
"""

import subprocess
from pathlib import Path
import json

# Paths
SOURCE_LOGO = Path("assets/images/icons/talking-papers-logo.png")
DEST_DIR = Path("assets/images/icons")
WEBP_LOGO = DEST_DIR / "talking-papers-logo.webp"

def optimize_logo():
    """Convert PNG logo to optimized WebP."""
    if not SOURCE_LOGO.exists():
        print(f"❌ Logo not found: {SOURCE_LOGO}")
        print("Please save the logo image to this location first.")
        return False
    
    # Create directory if needed
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    
    # Convert to WebP with optimization
    try:
        subprocess.run([
            "cwebp",
            "-q", "90",  # Quality
            "-m", "6",   # Max compression
            str(SOURCE_LOGO),
            "-o", str(WEBP_LOGO)
        ], check=True)
        print(f"✓ Converted logo to WebP: {WEBP_LOGO}")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to convert to WebP. Is cwebp installed?")
        return False
    except FileNotFoundError:
        print("❌ cwebp not found. Installing...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "webp"], check=True)
        return optimize_logo()

def update_blog_posts():
    """Update all Talking Papers posts to use new logo."""
    # Load blog index to find Talking Papers posts
    with open("data/blog-index.json", 'r') as f:
        blog_index = json.load(f)
    
    talking_papers_posts = []
    for post in blog_index['posts']:
        if "Talking Papers Podcast" in post.get('categories', []):
            content_path = post.get('content', '').lstrip('/')
            if content_path:
                talking_papers_posts.append(Path(content_path))
    
    print(f"\nFound {len(talking_papers_posts)} Talking Papers episodes")
    
    # Old logo path
    old_logo = "../../assets/images/publications/Talking_papers_cover-400.webp"
    new_logo = "../../assets/images/icons/talking-papers-logo.webp"
    
    updated_count = 0
    for post_path in talking_papers_posts:
        if not post_path.exists():
            continue
        
        with open(post_path, 'r') as f:
            content = f.read()
        
        if old_logo in content:
            content = content.replace(old_logo, new_logo)
            with open(post_path, 'w') as f:
                f.write(content)
            print(f"  ✓ {post_path.name}")
            updated_count += 1
    
    print(f"\n✅ Updated {updated_count} blog posts with new logo")

def main():
    print("Updating Talking Papers logo...")
    
    if optimize_logo():
        update_blog_posts()
    else:
        print("\nPlease:")
        print(f"1. Save the new logo to: {SOURCE_LOGO}")
        print("2. Run this script again")

if __name__ == "__main__":
    main()
