#!/usr/bin/env python3
"""
Fix PhD advisor hunt post images to include all responsive sizes.
"""

import re
from pathlib import Path

# The images that need fixing
IMAGES = [
    'PhD-advisor-hunt-illustration',
    'phd-survival-kit',
    'research-group-size',
    'money',
    'red-flags',
    'ultimate-check-list',
    'Find_an_Advisor',
    'PhD_Mindmap'
]

def fix_image_tags(html_path):
    """Add missing 400px and 800px WebP sources to picture tags"""
    
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    for img_name in IMAGES:
        # Pattern to match picture tags with only 200px source
        pattern = rf'(<picture>\s*<source srcset="../../assets/images/blog/{img_name}-200\.webp" type="image/webp" media="\(max-width: 399px\)">\s*<img)'
        
        # Replacement with all three sizes
        replacement = (
            f'<picture>\n'
            f'  <source srcset="../../assets/images/blog/{img_name}-800.webp" type="image/webp" media="(min-width: 800px)">\n'
            f'  <source srcset="../../assets/images/blog/{img_name}-400.webp" type="image/webp" media="(max-width: 799px)">\n'
            f'  <source srcset="../../assets/images/blog/{img_name}-200.webp" type="image/webp" media="(max-width: 399px)">\n'
            f'  <img'
        )
        
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            modified = True
            print(f"✓ Fixed {img_name}")
    
    if modified:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    html_path = Path('blog/posts/2025-02-17-phd-guide-advisor-hunt.html')
    
    if not html_path.exists():
        print(f"Error: {html_path} not found")
        return
    
    if fix_image_tags(html_path):
        print(f"\n✓ Updated {html_path}")
    else:
        print(f"No changes needed for {html_path}")

if __name__ == '__main__':
    main()
