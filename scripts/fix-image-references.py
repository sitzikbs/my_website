#!/usr/bin/env python3
"""
Fix image references in shortcodes to point to actual existing files.

Converts references to sized variants (e.g., -1024x380.jpg) to base filenames.
"""

import re
from pathlib import Path


def get_actual_image_path(referenced_path):
    """Find the actual image file that exists.
    
    Args:
        referenced_path: Path from shortcode (may reference non-existent variant)
        
    Returns:
        str: Corrected path to existing file, or original if not found
    """
    # Extract just the filename
    parts = referenced_path.split('/')
    filename = parts[-1]
    directory = '/'.join(parts[:-1])
    
    # Remove size suffixes like -1024x380, -300x169, etc.
    base_filename = re.sub(r'-\d+x\d+\.', '.', filename)
    
    # Check if base file exists
    base_path = Path(f"{directory}/{base_filename}")
    if base_path.exists():
        return f"{directory}/{base_filename}"
    
    # If not, try without any date prefix or variant
    # Extract just the core name
    core_name = re.sub(r'^\d{4}-\d{2}(-\d{2})?-', '', base_filename)
    core_path = Path(f"{directory}/{core_name}")
    if core_path.exists():
        return f"{directory}/{core_name}"
    
    # Return original if we can't find a match
    print(f"⚠️  Could not find image for: {referenced_path}")
    return referenced_path


def fix_shortcode_references(content):
    """Fix all responsiveImage shortcode references in content.
    
    Args:
        content: Markdown file content
        
    Returns:
        tuple: (fixed_content, num_fixes)
    """
    fixes = 0
    
    # Pattern to match responsiveImage shortcodes
    pattern = r'\{%\s*responsiveImage\s+"([^"]+)",\s*"([^"]*)"\s*%\}'
    
    def replace_shortcode(match):
        nonlocal fixes
        path = match.group(1)
        alt = match.group(2)
        
        # Check if the referenced file exists
        if not Path(path).exists():
            corrected_path = get_actual_image_path(path)
            if corrected_path != path:
                fixes += 1
                print(f"  Fixed: {path} → {corrected_path}")
                return f'{{% responsiveImage "{corrected_path}", "{alt}" %}}'
        
        return match.group(0)
    
    fixed_content = re.sub(pattern, replace_shortcode, content)
    return fixed_content, fixes


def main():
    """Main function to process all blog markdown files."""
    posts_dir = Path('blog/posts-md')
    
    if not posts_dir.exists():
        print(f"❌ Directory not found: {posts_dir}")
        return
    
    markdown_files = sorted(posts_dir.glob('*.md'))
    total_fixes = 0
    fixed_files = []
    
    print(f"🔍 Processing {len(markdown_files)} markdown files\n")
    
    for md_file in markdown_files:
        content = md_file.read_text(encoding='utf-8')
        fixed_content, fixes = fix_shortcode_references(content)
        
        if fixes > 0:
            md_file.write_text(fixed_content, encoding='utf-8')
            total_fixes += fixes
            fixed_files.append((md_file.name, fixes))
            print(f"✅ {md_file.name}: {fixes} references fixed\n")
    
    print("=" * 70)
    print("📊 FIX SUMMARY")
    print("=" * 70)
    print(f"Total files processed: {len(markdown_files)}")
    print(f"Files fixed: {len(fixed_files)}")
    print(f"Total references fixed: {total_fixes}")


if __name__ == "__main__":
    main()
