#!/usr/bin/env python3
"""
Replace WordPress URLs in markdown files with local paths.
"""

import re
import os

def replace_wordpress_urls(content):
    """Replace WordPress URLs with local paths in markdown content."""
    
    # Pattern 1: Direct WordPress URLs in links (PDFs, ZIPs, images)
    # Example: https://www.itzikbs.com/wp-content/uploads/2017/08/Poster-raz-and-dan.pdf
    content = re.sub(
        r'https://www\.itzikbs\.com/wp-content/uploads/\d{4}/\d{2}/([^"\'?\s>]+)',
        r'/assets/images/blog/\1',
        content
    )
    
    # Pattern 2: CDN URLs with i[0-3].wp.com
    # Example: https://i2.wp.com/www.itzikbs.com/wp-content/uploads/2020/08/IMG_8418-scaled.jpg?ssl=1
    content = re.sub(
        r'https://i[0-3]\.wp\.com/www\.itzikbs\.com/wp-content/uploads/\d{4}/\d{2}/([^"\'?\s>]+)',
        r'/assets/images/blog/\1',
        content
    )
    
    # Pattern 3: Clean up remaining query parameters that were left behind
    # Example: /assets/images/blog/image.jpg?fit=800%2C534&ssl=1
    content = re.sub(
        r'(/assets/images/blog/[^"\'?\s>]+)\?[^"\'<>\s]+',
        r'\1',
        content
    )
    
    return content

def process_markdown_file(file_path):
    """Process a single markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file has WordPress URLs
    if 'itzikbs.com/wp-content' not in content and 'wp.com' not in content:
        return False
    
    new_content = replace_wordpress_urls(content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    
    return False

def main():
    """Process all markdown files in blog/posts-md/."""
    md_dir = 'blog/posts-md'
    
    if not os.path.exists(md_dir):
        print(f"Directory {md_dir} not found!")
        return
    
    updated = 0
    skipped = 0
    
    for filename in sorted(os.listdir(md_dir)):
        if not filename.endswith('.md'):
            continue
        
        file_path = os.path.join(md_dir, filename)
        
        if process_markdown_file(file_path):
            print(f"✓ Updated: {filename}")
            updated += 1
        else:
            skipped += 1
    
    print()
    print("="*80)
    print(f"Complete: {updated} files updated, {skipped} files skipped")
    print("="*80)

if __name__ == "__main__":
    main()
