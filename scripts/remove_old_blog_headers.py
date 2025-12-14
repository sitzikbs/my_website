#!/usr/bin/env python3
"""
Remove old post-header elements that are duplicates of the new hero headers.
"""

import re
from pathlib import Path

def remove_old_header(html_path: Path) -> bool:
    """Remove old post-header from a blog post."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if there's a hero header (we only remove old header if new one exists)
    if 'class="blog-hero"' not in content:
        return False
    
    # Remove old post-header
    old_header_pattern = r'\s*<header class="post-header">.*?</header>\s*'
    if not re.search(old_header_pattern, content, re.DOTALL):
        return False
    
    content = re.sub(old_header_pattern, '\n', content, flags=re.DOTALL, count=1)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Process all blog posts."""
    print("Removing duplicate old headers from blog posts...")
    
    blog_dir = Path("blog/posts")
    modified_count = 0
    total_count = 0
    
    for html_path in blog_dir.glob("*.html"):
        total_count += 1
        
        if remove_old_header(html_path):
            print(f"  ✓ {html_path.name}")
            modified_count += 1
    
    print(f"\n✅ Removed old headers from {modified_count}/{total_count} blog posts")

if __name__ == "__main__":
    main()
