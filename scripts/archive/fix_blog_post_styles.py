#!/usr/bin/env python3
"""
Fix blog post styling issues:
1. Remove duplicate CSS
2. Remove top padding from .blog-post
"""

import re
from pathlib import Path

def fix_blog_post(html_path: Path) -> bool:
    """Fix styling in a blog post."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # Fix 1: Remove duplicate hero styles (keep only the first occurrence)
    # Find all occurrences of the hero header styles block
    hero_pattern = r'        \.blog-hero-content \{[^}]+\}.*?(?=\n        /\*|</style>)'
    matches = list(re.finditer(hero_pattern, content, re.DOTALL))
    
    if len(matches) > 1:
        # Remove duplicates (keep first, remove rest)
        for match in reversed(matches[1:]):
            content = content[:match.start()] + content[match.end():]
        modified = True
        print(f"  Removed {len(matches)-1} duplicate style blocks from {html_path.name}")
    
    # Fix 2: Change .blog-post padding from "2rem 1.5rem" to "0 1.5rem"
    blog_post_pattern = r'(\.blog-post \{[^}]*padding:\s*)2rem(\s+1\.5rem;)'
    if re.search(blog_post_pattern, content):
        content = re.sub(blog_post_pattern, r'\g<1>0\g<2>', content)
        modified = True
    
    if modified:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    """Process all blog posts."""
    print("Fixing blog post styles...")
    
    blog_dir = Path("blog/posts")
    modified_count = 0
    
    for html_path in sorted(blog_dir.glob("*.html")):
        if fix_blog_post(html_path):
            print(f"  ✓ {html_path.name}")
            modified_count += 1
    
    print(f"\n✅ Fixed {modified_count} blog posts")

if __name__ == "__main__":
    main()
