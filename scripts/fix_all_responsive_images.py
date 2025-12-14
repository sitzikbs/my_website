#!/usr/bin/env python3
"""
Fix all blog post images to use proper responsive image structure.
For images with 800px: use min-width:800px for 800px, max-width:799px for 400px, max-width:399px for 200px
For images without 800px: use min-width:400px for 400px, max-width:399px for 200px
"""

import re
from pathlib import Path
from collections import defaultdict

def find_available_sizes(img_base_name, blog_dir):
    """Find which WebP sizes are available for an image"""
    sizes = {}
    for size in [800, 400, 200]:
        webp_path = blog_dir / f"{img_base_name}-{size}.webp"
        if webp_path.exists():
            sizes[size] = str(webp_path.relative_to(blog_dir.parent.parent))
    return sizes

def fix_picture_tags(html_path):
    """Fix responsive image structure in a blog post"""
    
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    blog_dir = Path('assets/images/blog')
    modified = False
    
    # Pattern to match picture tags with WebP sources
    # Captures the entire picture block
    picture_pattern = r'<picture>\s*(?:<source[^>]*>[\s\n]*)+<img[^>]*>'
    
    def replace_picture(match):
        nonlocal modified
        picture_block = match.group(0)
        
        # Extract image base name from the source tags
        webp_match = re.search(r'srcset="../../assets/images/blog/([^"]+?)-(?:200|400|800)\.webp"', picture_block)
        if not webp_match:
            return picture_block
        
        img_base = webp_match.group(1)
        
        # Find available sizes
        sizes = find_available_sizes(img_base, blog_dir)
        
        if not sizes:
            return picture_block
        
        # Extract the img tag
        img_match = re.search(r'<img[^>]*>', picture_block)
        if not img_match:
            return picture_block
        
        img_tag = img_match.group(0)
        
        # Build new picture tag based on available sizes
        new_sources = []
        
        if 800 in sizes and 400 in sizes and 200 in sizes:
            # All three sizes available
            new_sources = [
                f'  <source srcset="../../assets/images/blog/{img_base}-800.webp" type="image/webp" media="(min-width: 800px)">',
                f'  <source srcset="../../assets/images/blog/{img_base}-400.webp" type="image/webp" media="(max-width: 799px)">',
                f'  <source srcset="../../assets/images/blog/{img_base}-200.webp" type="image/webp" media="(max-width: 399px)">'
            ]
        elif 400 in sizes and 200 in sizes:
            # Only 400 and 200 available (original < 800px)
            new_sources = [
                f'  <source srcset="../../assets/images/blog/{img_base}-400.webp" type="image/webp" media="(min-width: 400px)">',
                f'  <source srcset="../../assets/images/blog/{img_base}-200.webp" type="image/webp" media="(max-width: 399px)">'
            ]
        elif 200 in sizes:
            # Only 200 available (very small original)
            new_sources = [
                f'  <source srcset="../../assets/images/blog/{img_base}-200.webp" type="image/webp">'
            ]
        else:
            return picture_block
        
        new_picture = '<picture>\n' + '\n'.join(new_sources) + '\n  ' + img_tag + '\n</picture>'
        
        if new_picture != picture_block:
            modified = True
            return new_picture
        
        return picture_block
    
    new_content = re.sub(picture_pattern, replace_picture, content, flags=re.MULTILINE)
    
    if modified:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    
    return False

def main():
    posts_dir = Path('blog/posts')
    fixed_count = 0
    
    for html_file in sorted(posts_dir.glob('*.html')):
        if fix_picture_tags(html_file):
            print(f"✓ Fixed {html_file.name}")
            fixed_count += 1
    
    print(f"\nFixed {fixed_count} blog posts")

if __name__ == '__main__':
    main()
