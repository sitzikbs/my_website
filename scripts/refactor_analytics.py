#!/usr/bin/env python3
"""
Replace embedded Google Analytics code with external script reference.
This makes the codebase more maintainable by centralizing GA configuration.
"""

import re
from pathlib import Path


# Pattern to match the entire embedded GA4 code block
# Made more flexible to handle whitespace and quote variations
GA4_EMBEDDED_PATTERN = re.compile(
    r'\s*<!-- Google Analytics 4 -->\s*'
    r'<script async src="https://www\.googletagmanager\.com/gtag/js\?id=G-EJRL17R9NE"></script>\s*'
    r'<script>\s*'
    r'window\.dataLayer = window\.dataLayer \|\| \[\];\s*'
    r'function gtag\(\)\s*\{\s*dataLayer\.push\(arguments\);\s*\}\s*'
    r"gtag\('js',\s*new Date\(\)\);\s*"
    r"gtag\('config',\s*'G-EJRL17R9NE',\s*\{\s*"
    r"['\"]anonymize_ip['\"]:\s*true,\s*"
    r"['\"]cookie_flags['\"]:\s*'SameSite=None;Secure'\s*"
    r'\}\);\s*'
    r'</script>',
    re.MULTILINE | re.DOTALL
)

# Replacement: simple script tag reference
GA4_SCRIPT_TAG = '  <script src="js/analytics.js"></script>\n'


def replace_embedded_ga4(filepath: Path) -> bool:
    """
    Replace embedded GA4 code with external script reference.
    
    Args:
        filepath: Path to the HTML file
        
    Returns:
        True if file was modified, False otherwise
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Check if embedded GA4 code exists
    if not GA4_EMBEDDED_PATTERN.search(html_content):
        return False
    
    # Replace with external script reference
    new_content = GA4_EMBEDDED_PATTERN.sub(GA4_SCRIPT_TAG, html_content)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✓ {filepath}")
    return True


def main():
    """Main function."""
    print("Refactoring Google Analytics to use external script...\n")
    
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
        if replace_embedded_ga4(html_file):
            modified_count += 1
    
    print(f"\n{'=' * 60}")
    print("SUMMARY")
    print(f"{'=' * 60}")
    print(f"Total files processed: {len(html_files)}")
    print(f"Files modified: {modified_count}")
    print(f"Files unchanged: {len(html_files) - modified_count}")
    print()
    print("✅ Refactoring complete!")
    print("   All HTML files now use: <script src=\"js/analytics.js\"></script>")
    print("   Update GA4 settings in one place: js/analytics.js")


if __name__ == "__main__":
    main()
