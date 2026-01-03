#!/usr/bin/env python3
"""
Convert hardcoded <picture> elements in markdown files to {% responsiveImage %} shortcode.
"""

import re
from pathlib import Path

def extract_image_info(picture_element):
    """Extract src and alt from picture element."""
    # Find the img tag within picture
    img_match = re.search(r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"[^>]*>', picture_element, re.DOTALL)
    if not img_match:
        # Try alt after src
        img_match = re.search(r'<img[^>]*alt="([^"]*)"[^>]*src="([^"]*)"[^>]*>', picture_element, re.DOTALL)
        if img_match:
            alt, src = img_match.groups()
        else:
            return None, None
    else:
        src, alt = img_match.groups()
    
    return src, alt

def convert_picture_to_shortcode(content):
    """Convert all <picture> elements to {% responsiveImage %} shortcode."""
    
    # Find all picture elements (multiline)
    picture_pattern = r'<picture>.*?</picture>'
    
    def replace_picture(match):
        picture_element = match.group(0)
        src, alt = extract_image_info(picture_element)
        
        if not src:
            print(f"Warning: Could not extract src from: {picture_element[:100]}")
            return picture_element
        
        # Clean up the src path - remove -1024x380, -scaled, etc suffixes before extension
        # Example: Capture-1024x380.jpg -> Capture.jpg
        src_cleaned = re.sub(r'-\d+x\d+(\.\w+)$', r'\1', src)
        src_cleaned = re.sub(r'-scaled(\.\w+)$', r'\1', src_cleaned)
        
        # Also remove any size variants like -400, -200 from WebP files
        src_cleaned = re.sub(r'-\d+(\.\webp)$', r'.jpg', src_cleaned)
        src_cleaned = re.sub(r'\.webp$', '.jpg', src_cleaned)
        
        # Escape double quotes in alt text
        alt_escaped = alt.replace('"', '\\"')
        
        return f'{{% responsiveImage "{src_cleaned}", "{alt_escaped}" %}}'
    
    # Replace all picture elements
    converted = re.sub(picture_pattern, replace_picture, content, flags=re.DOTALL)
    
    return converted

def main():
    posts_dir = Path("blog/posts-md")
    
    if not posts_dir.exists():
        print(f"Error: {posts_dir} does not exist")
        return
    
    md_files = list(posts_dir.glob("*.md"))
    print(f"Found {len(md_files)} markdown files")
    
    converted_count = 0
    picture_count = 0
    
    for md_file in md_files:
        content = md_file.read_text(encoding='utf-8')
        
        # Count pictures in this file
        pictures_in_file = len(re.findall(r'<picture>', content))
        
        if pictures_in_file > 0:
            print(f"\nProcessing {md_file.name} ({pictures_in_file} pictures)")
            new_content = convert_picture_to_shortcode(content)
            
            if new_content != content:
                md_file.write_text(new_content, encoding='utf-8')
                converted_count += 1
                picture_count += pictures_in_file
                print(f"  ✓ Converted {pictures_in_file} picture elements")
    
    print(f"\n{'='*60}")
    print(f"Conversion complete!")
    print(f"Files modified: {converted_count}")
    print(f"Picture elements converted: {picture_count}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
