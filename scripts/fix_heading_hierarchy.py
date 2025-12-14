#!/usr/bin/env python3
"""
Fix heading hierarchy issues in HTML files.
Changes h3 "Related" sections and blog post structure headings to h2.
"""

import re
from pathlib import Path


def fix_headings(html_content: str, filepath: Path) -> tuple[str, int]:
    """Fix heading hierarchy issues in HTML content."""
    changes = 0
    
    # Fix 1: Change <h3>Related</h3> to <h2>Related</h2>
    new_content = re.sub(
        r'<h3([^>]*)>\s*<em>Related</em>\s*</h3>',
        r'<h2\1><em>Related</em></h2>',
        html_content,
        flags=re.IGNORECASE
    )
    if new_content != html_content:
        changes += 1
        html_content = new_content
    
    # Fix 2: Change blog post structure h3 tags to h2 (AUTHORS, ABSTRACT, etc.)
    structure_headings = [
        'AUTHORS?',
        'ABSTRACT',
        'RELATED (WORKS?|PAPERS?)',
        'LINKS AND RESOURCES',
        'CONTACT',
        'SUBSCRIBE AND FOLLOW',
    ]
    
    for heading_pattern in structure_headings:
        pattern = rf'<h3([^>]*)>(\s*(?:<br\s*/?>)?)\s*{heading_pattern}\s*</h3>'
        replacement = r'<h2\1>\2' + heading_pattern.replace('?', '') + r'</h2>'
        
        new_content = re.sub(pattern, replacement, html_content, flags=re.IGNORECASE)
        if new_content != html_content:
            changes += 1
            html_content = new_content
    
    # Fix 3: More specific patterns for common issues
    # Fix "Day X" headers (should be h2, not h4)
    new_content = re.sub(
        r'<h4([^>]*)>\s*Day\s+\d+[:\s]*</h4>',
        lambda m: f'<h2{m.group(1)}>Day {m.group(0).split("Day")[1].strip().rstrip("</h4>")}:</h2>',
        html_content,
        flags=re.IGNORECASE
    )
    if new_content != html_content:
        changes += 1
        html_content = new_content
    
    # Fix 4: Statistics, Awards, etc. in CVPR posts
    conference_headings = ['Statistics', 'Awards', 'Workshops', 'Favorite Posters']
    for heading in conference_headings:
        pattern = rf'<h3([^>]*)>\s*{heading}\s*</h3>'
        replacement = rf'<h2\1>{heading}</h2>'
        new_content = re.sub(pattern, replacement, html_content, flags=re.IGNORECASE)
        if new_content != html_content:
            changes += 1
            html_content = new_content
    
    return html_content, changes


def main():
    """Main function."""
    print("Fixing heading hierarchy in HTML files...\n")
    
    # Find all HTML files
    html_files = []
    
    # Blog post HTML files (where most issues are)
    blog_dir = Path('blog/posts')
    if blog_dir.exists():
        html_files.extend(blog_dir.glob('*.html'))
    
    print(f"Found {len(html_files)} HTML files to fix\n")
    
    # Fix each file
    total_changes = 0
    files_modified = 0
    
    for html_file in sorted(html_files):
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, changes = fix_headings(content, html_file)
        
        if changes > 0:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            files_modified += 1
            total_changes += changes
            print(f"✓ Fixed {html_file} ({changes} changes)")
    
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Files processed: {len(html_files)}")
    print(f"Files modified: {files_modified}")
    print(f"Total changes: {total_changes}")
    print(f"\n💡 Run check_heading_hierarchy.py again to verify fixes")


if __name__ == '__main__':
    main()
