#!/usr/bin/env python3
"""
Replace the placeholder GA4 Measurement ID with the actual one in all HTML files.
This script finds and replaces all instances of G-XXXXXXXXXX with the real ID.
"""

import re
from pathlib import Path


# The placeholder ID used initially
PLACEHOLDER_ID = "G-XXXXXXXXXX"

# The actual GA4 Measurement ID from the WordPress site
ACTUAL_ID = "G-EJRL17R9NE"


def replace_ga4_id(filepath: Path) -> bool:
    """
    Replace placeholder GA4 ID with actual ID in a single HTML file.
    
    Args:
        filepath: Path to the HTML file
        
    Returns:
        True if file was modified, False otherwise
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Check if placeholder exists
    if PLACEHOLDER_ID not in html_content:
        return False
    
    # Replace all instances of placeholder with actual ID
    new_content = html_content.replace(PLACEHOLDER_ID, ACTUAL_ID)
    
    # Count replacements
    replacements = html_content.count(PLACEHOLDER_ID)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✓ {filepath}: Replaced {replacements} instance(s)")
    return True


def main():
    """Main function."""
    print(f"Replacing GA4 Measurement ID in HTML files...")
    print(f"Placeholder: {PLACEHOLDER_ID}")
    print(f"Actual ID:   {ACTUAL_ID}\n")
    
    # Find all HTML files
    html_files = []
    
    # Root HTML files
    for html_file in Path('.').glob('*.html'):
        if html_file.name not in ['css-demo.html']:
            html_files.append(html_file)
    
    # Blog post HTML files
    blog_dir = Path('blog/posts')
    if blog_dir.exists():
        html_files.extend(blog_dir.glob('*.html'))
    
    print(f"Found {len(html_files)} HTML files to process\n")
    
    # Process each file
    modified_count = 0
    for html_file in sorted(html_files):
        if replace_ga4_id(html_file):
            modified_count += 1
    
    print(f"\n{'=' * 60}")
    print("SUMMARY")
    print(f"{'=' * 60}")
    print(f"Total files processed: {len(html_files)}")
    print(f"Files modified: {modified_count}")
    print(f"Files unchanged: {len(html_files) - modified_count}")
    print()
    print("✅ GA4 Measurement ID replacement complete!")
    print(f"   All instances of {PLACEHOLDER_ID} have been replaced with {ACTUAL_ID}")


if __name__ == "__main__":
    main()
