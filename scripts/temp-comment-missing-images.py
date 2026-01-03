#!/usr/bin/env python3
"""
Temporarily comment out missing image references that are causing build failures.
These images were likely removed during the cleanup process and need to be recovered
from WordPress backup.
"""

import os
import re
from pathlib import Path

# List of missing images identified from build errors
MISSING_IMAGES = [
    "samsunggalaxy_buds-1.jpg",
    "neewer_camera_sling_bag-1.jpg",
    "Edfp1jGUcAAhM2w-1.jpg",
    "fv_34-300x225.png",
    "Shaked_Dinosaur_costume_1-200x300.jpg",
    "knit-lion-costume-2-200x300.jpg",
    "decoder_original_vs_reconstruction-01.png",
    "20220619_134527-scaled.jpg",
    "GDCbsbOWYAAGhsf-1.jpeg",
    "GQYNemQaIAUTC8O-1.jpg",
    "IMG-20240618-WA00121-1.jpg",
    "GQh5m-la8AAEP_B-1.jpg",
    "example-inline-image.jpg",
    "segmentation_example.jpg",
    "pose_example.jpg",
]

def comment_out_image_references(file_path, missing_images):
    """Comment out references to missing images in a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes = []
    
    for img in missing_images:
        # Pattern to match image tags with this filename
        # Match either <img>, <figure> with responsiveImage shortcode, or standalone responsiveImage
        patterns = [
            # Match figure blocks with responsiveImage shortcode
            rf'(<figure[^>]*>)\s*({{%\s*responsiveImage\s*["\'][^"\']*{re.escape(img)}["\'][^%]*%}})\s*(</figure>)',
            # Match div blocks with images
            rf'(<div[^>]*>)\s*(<figure[^>]*>)?\s*({{%\s*responsiveImage\s*["\'][^"\']*{re.escape(img)}["\'][^%]*%}})\s*(</figure>)?\s*(</div>)',
            # Match standalone responsiveImage shortcodes
            rf'({{%\s*responsiveImage\s*["\'][^"\']*{re.escape(img)}["\'][^%]*%}})',
        ]
        
        for pattern in patterns:
            if re.search(pattern, content, re.IGNORECASE | re.DOTALL):
                # Wrap in comment
                content = re.sub(
                    pattern,
                    lambda m: f'{{% raw %}}\\n<!-- TODO: Restore missing image {img} -->\\n{{% endraw %}}',
                    content,
                    flags=re.IGNORECASE | re.DOTALL
                )
                changes.append(img)
                break
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    return []

def main():
    blog_dir = Path("blog/posts-md")
    total_changes = 0
    files_modified = 0
    
    print(f"🔍 Searching for missing image references in {blog_dir}")
    
    for md_file in blog_dir.glob("*.md"):
        changes = comment_out_image_references(md_file, MISSING_IMAGES)
        if changes:
            files_modified += 1
            total_changes += len(changes)
            print(f"✓ {md_file.name}: Commented out {len(changes)} images")
            for img in changes:
                print(f"  - {img}")
    
    print(f"\\n📊 SUMMARY")
    print(f"Files modified: {files_modified}")
    print(f"Image references commented out: {total_changes}")

if __name__ == "__main__":
    main()
