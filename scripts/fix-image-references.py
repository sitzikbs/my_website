#!/usr/bin/env python3
"""
Fix blog post references to -scaled and -WIDTHxHEIGHT image filenames.
"""

from pathlib import Path
import re

posts_dir = Path("blog/posts-md")

# Patterns to fix
patterns = [
    (r'/assets/images/blog/IMG_8508-scaled\.jpg', '/assets/images/blog/IMG_8508.jpg'),
    (r'/assets/images/blog/IMG_8418-scaled\.jpg', '/assets/images/blog/IMG_8418.jpg'),
    (r'/assets/images/blog/IMG_8505-scaled\.jpg', '/assets/images/blog/IMG_8505.jpg'),
    (r'/assets/images/blog/IMG_8421-1-scaled\.jpg', '/assets/images/blog/IMG_8421-1.jpg'),
    (r'/assets/images/blog/IMG_8432-1-scaled\.jpg', '/assets/images/blog/IMG_8432-1.jpg'),
    (r'/assets/images/blog/IMG_8435-1-scaled\.jpg', '/assets/images/blog/2020-08-IMG_8435-1.jpg'),
    (r'20220619_134527-scaled\.jpg', '20220619_134527.jpg'),
    (r'../../assets/images/blog/IMG_8505-scaled\.jpg', '../../assets/images/blog/IMG_8505.jpg'),
    (r'../../assets/images/blog/IMG_8421-1-scaled\.jpg', '../../assets/images/blog/IMG_8421-1.jpg'),
    (r'IMG_20170503_134915-ANIMATION-300x225\.gif', 'IMG_20170503_134915-ANIMATION.gif'),
]

total_replacements = 0

for post in posts_dir.glob("*.md"):
    content = post.read_text()
    modified = content
    post_replacements = 0
    
    for pattern, replacement in patterns:
        new_content = re.sub(pattern, replacement, modified)
        count = len(re.findall(pattern, modified))
        if count > 0:
            print(f"{post.name}: {count} × {pattern} → {replacement}")
            post_replacements += count
        modified = new_content
    
    if post_replacements > 0:
        post.write_text(modified)
        total_replacements += post_replacements
        print(f"  ✓ Updated {post.name} ({post_replacements} replacements)\n")

print(f"{'='*70}")
print(f"Total replacements: {total_replacements}")
