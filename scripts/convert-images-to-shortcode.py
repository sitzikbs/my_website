#!/usr/bin/env python3
"""
Convert blog post images to Eleventy responsive image shortcode.

This script:
1. Parses all markdown files in blog/posts-md/
2. Finds <img> tags and <picture> elements
3. Replaces them with {% responsiveImage %} shortcode syntax
4. Preserves alt text and handles relative paths
"""

import re
from pathlib import Path


def extract_img_info(img_tag):
    """Extract src and alt from img tag.
    
    Args:
        img_tag: HTML img tag string
        
    Returns:
        tuple: (src, alt) or (None, None) if parsing fails
    """
    # Extract src
    src_match = re.search(r'src=["\']([^"\']+)["\']', img_tag)
    src = src_match.group(1) if src_match else None
    
    # Extract alt
    alt_match = re.search(r'alt=["\']([^"\']*)["\']', img_tag)
    alt = alt_match.group(1) if alt_match else ""
    
    return src, alt


def convert_picture_to_shortcode(picture_block):
    """Convert <picture> block to shortcode.
    
    Args:
        picture_block: HTML picture element with sources and img
        
    Returns:
        str: Nunjucks shortcode or original block if conversion fails
    """
    # Extract img tag from picture block
    img_match = re.search(r'<img[^>]+>', picture_block, re.DOTALL)
    if not img_match:
        return picture_block
    
    img_tag = img_match.group(0)
    src, alt = extract_img_info(img_tag)
    
    if not src:
        return picture_block
    
    # Clean up path - remove ../../ and get clean relative path from root
    clean_src = src.replace('../../', '')
    
    # Don't convert if it's already pointing to a webp or sized variant
    # (these files no longer exist)
    if '-200.webp' in src or '-400.webp' in src or '-800.webp' in src:
        # Get the base image name without webp suffix
        base_name = re.sub(r'-\d+\.webp$', '', src.split('/')[-1])
        # Reconstruct path with original extension
        path_parts = src.split('/')[:-1]
        # Try to find the original file
        clean_src = f"{'/'.join(path_parts[2:])}/{base_name}.jpg"  # Assume jpg, could be png
    
    # Generate shortcode
    shortcode = f'{{% responsiveImage "{clean_src}", "{alt}" %}}'
    
    return shortcode


def convert_img_to_shortcode(img_tag):
    """Convert standalone <img> tag to shortcode.
    
    Args:
        img_tag: HTML img tag string
        
    Returns:
        str: Nunjucks shortcode or original tag if conversion fails
    """
    src, alt = extract_img_info(img_tag)
    
    if not src:
        return img_tag
    
    # Skip LaTeX images (WordPress formula renderer)
    if 'latex.php' in src or 's0.wp.com' in src:
        return img_tag
    
    # Clean up path
    clean_src = src.replace('../../', '')
    
    # Don't convert external images
    if src.startswith('http'):
        return img_tag
    
    # Generate shortcode
    shortcode = f'{{% responsiveImage "{clean_src}", "{alt}" %}}'
    
    return shortcode


def process_markdown_file(file_path):
    """Process a single markdown file.
    
    Args:
        file_path: Path to markdown file
        
    Returns:
        tuple: (modified_content, changes_made)
    """
    content = file_path.read_text(encoding='utf-8')
    original_content = content
    changes = 0
    
    # First, replace <picture> elements (more complex)
    # Match picture blocks that may span multiple lines
    picture_pattern = r'<picture>.*?</picture>'
    
    def replace_picture(match):
        nonlocal changes
        result = convert_picture_to_shortcode(match.group(0))
        if result != match.group(0):
            changes += 1
        return result
    
    content = re.sub(picture_pattern, replace_picture, content, flags=re.DOTALL)
    
    # Then replace standalone <img> tags that aren't inside picture elements
    # Be careful not to match img tags we just created in shortcodes
    img_pattern = r'<img\s+[^>]*>'
    
    def replace_img(match):
        nonlocal changes
        img_tag = match.group(0)
        # Skip if it's a LaTeX image
        if 'latex.php' in img_tag or 's0.wp.com' in img_tag:
            return img_tag
        result = convert_img_to_shortcode(img_tag)
        if result != img_tag:
            changes += 1
        return result
    
    # Only replace img tags that aren't already part of picture elements
    # Since we already replaced pictures, any remaining img tags are standalone
    content = re.sub(img_pattern, replace_img, content, flags=re.DOTALL)
    
    return content, changes


def main():
    """Main function to process all blog markdown files."""
    posts_dir = Path('blog/posts-md')
    
    if not posts_dir.exists():
        print(f"❌ Directory not found: {posts_dir}")
        return
    
    markdown_files = sorted(posts_dir.glob('*.md'))
    total_files = len(markdown_files)
    total_changes = 0
    modified_files = []
    
    print(f"🔍 Found {total_files} markdown files to process\n")
    
    for md_file in markdown_files:
        new_content, changes = process_markdown_file(md_file)
        
        if changes > 0:
            md_file.write_text(new_content, encoding='utf-8')
            total_changes += changes
            modified_files.append((md_file.name, changes))
            print(f"✅ {md_file.name}: {changes} images converted")
        else:
            print(f"⏭️  {md_file.name}: No changes needed")
    
    print("\n" + "=" * 70)
    print("📊 CONVERSION SUMMARY")
    print("=" * 70)
    print(f"Total files processed: {total_files}")
    print(f"Files modified: {len(modified_files)}")
    print(f"Total image conversions: {total_changes}")
    
    if modified_files:
        print("\n📝 Modified files:")
        for filename, changes in modified_files[:10]:
            print(f"  {filename}: {changes} conversions")
        if len(modified_files) > 10:
            print(f"  ... and {len(modified_files) - 10} more files")


if __name__ == "__main__":
    main()
