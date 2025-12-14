#!/usr/bin/env python3
"""
Add resource hints to HTML files for performance optimization:
- preconnect to Google Fonts
- dns-prefetch to Google Fonts
- Font stylesheet link with proper attributes
"""

import os
import re
from pathlib import Path


# Resource hints to add
RESOURCE_HINTS = '''<!-- Resource Hints for Performance -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="dns-prefetch" href="https://fonts.googleapis.com">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap">'''


def add_resource_hints_to_html(html_file: Path) -> bool:
    """
    Add resource hints to an HTML file's <head> section.
    
    Returns:
        bool: True if file was modified, False otherwise
    """
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has resource hints
    if 'preconnect' in content and 'fonts.googleapis.com' in content:
        print(f"  Skipping {html_file} (already has resource hints)")
        return False
    
    # Find the <head> section and add hints after charset meta
    # Look for charset or viewport meta tag as insertion point
    pattern = r'(<meta\s+charset="[^"]+"\s*/>|<meta\s+content="[^"]+"\s+name="viewport"\s*/>)'
    
    def insert_hints(match):
        return match.group(1) + '\n' + RESOURCE_HINTS
    
    # Try to insert after charset/viewport
    new_content, count = re.subn(pattern, insert_hints, content, count=1)
    
    if count == 0:
        # If no charset/viewport found, try to insert after <head>
        new_content = content.replace('<head>', '<head>\n' + RESOURCE_HINTS)
        if new_content == content:
            print(f"  Warning: Could not find insertion point in {html_file}")
            return False
    
    # Write back
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✓ Added resource hints to {html_file}")
    return True


def main():
    """Main function to add resource hints to all HTML files."""
    print("Adding resource hints to HTML files...\n")
    
    # Find all HTML files
    html_files = []
    
    # Root HTML files
    for html_file in Path('.').glob('*.html'):
        html_files.append(html_file)
    
    # Blog post HTML files
    blog_dir = Path('blog/posts')
    if blog_dir.exists():
        html_files.extend(blog_dir.glob('*.html'))
    
    print(f"Found {len(html_files)} HTML files to process\n")
    
    # Process each file
    modified_count = 0
    for html_file in sorted(html_files):
        if add_resource_hints_to_html(html_file):
            modified_count += 1
    
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Total files processed: {len(html_files)}")
    print(f"Files modified: {modified_count}")
    print(f"Files skipped: {len(html_files) - modified_count}")


if __name__ == '__main__':
    main()
