#!/usr/bin/env python3
"""Simple script to apply date corrections from mapping file."""

import json
import re
import shutil
from pathlib import Path

# Load mapping
SCRIPT_DIR = Path(__file__).parent
MAPPING_FILE = SCRIPT_DIR / "wordpress-dates-mapping.json"
BLOG_DIR = SCRIPT_DIR.parent / "blog" / "posts-md"
BLOG_INDEX_FILE = SCRIPT_DIR.parent / "data" / "blog-index.json"

with open(MAPPING_FILE, 'r') as f:
    mapping = json.load(f)

# Filter posts that need updates
posts_to_update = {k: v for k, v in mapping.items() if v.get('needs_update', False)}

print(f"Found {len(posts_to_update)} posts to update\n")

# Update each file
for slug, post_data in posts_to_update.items():
    old_file = BLOG_DIR / Path(post_data['file_path']).name
    old_date = post_data['current_date']
    new_date = post_data['wordpress_date']
    
    if not old_file.exists():
        print(f"⚠️  File not found: {old_file.name}")
        continue
    
    print(f"Updating: {old_file.name}")
    print(f"  Date: {old_date} → {new_date}")
    
    # Read and update content
    with open(old_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update date in frontmatter
    updated_content = re.sub(
        r'^date:\s*["\']?\d{4}-\d{2}-\d{2}["\']?',
        f'date: "{new_date}"',
        content,
        flags=re.MULTILINE
    )
    
    # Create new filename
    slug_part = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', old_file.stem)
    new_filename = f"{new_date}-{slug_part}.md"
    new_file = BLOG_DIR / new_filename
    
    # Write to new file
    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    # Remove old file if different
    if new_file != old_file:
        old_file.unlink()
        print(f"  Renamed to: {new_filename}")
    else:
        print(f"  Updated (no rename needed)")

# Update blog-index.json
print(f"\nUpdating {BLOG_INDEX_FILE}...")

with open(BLOG_INDEX_FILE, 'r', encoding='utf-8') as f:
    blog_index = json.load(f)

updated_count = 0
if 'posts' in blog_index:
    for post in blog_index['posts']:
        post_id = post.get('id', '')
        if post_id in posts_to_update:
            old_date = post['date']
            new_date = posts_to_update[post_id]['wordpress_date']
            post['date'] = new_date
            updated_count += 1
            print(f"  Updated {post_id}: {old_date} → {new_date}")

with open(BLOG_INDEX_FILE, 'w', encoding='utf-8') as f:
    json.dump(blog_index, f, indent=2, ensure_ascii=False)

print(f"\n✓ Successfully updated {len(posts_to_update)} markdown files!")
print(f"✓ Updated {updated_count} entries in blog-index.json!")
