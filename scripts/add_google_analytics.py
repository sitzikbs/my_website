#!/usr/bin/env python3
"""
Add Google Analytics 4 (GA4) tracking code to all HTML files.
The tracking code will be added right after the opening <head> tag.
"""

import re
from pathlib import Path


# GA4 Measurement ID from the original WordPress site (using MonsterInsights plugin)
GA4_MEASUREMENT_ID = "G-EJRL17R9NE"


def get_ga4_code(measurement_id: str) -> str:
    """Generate GA4 tracking code."""
    return f'''
  <!-- Google Analytics 4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={measurement_id}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{measurement_id}', {{
      'anonymize_ip': true,
      'cookie_flags': 'SameSite=None;Secure'
    }});
  </script>'''


def add_ga4_tracking(html_content: str, filepath: Path) -> bool:
    """Add GA4 tracking code to HTML content."""
    
    # Check if already has Google Analytics
    if 'googletagmanager.com/gtag' in html_content or 'gtag(' in html_content:
        print(f"  ⏭️  Skipping {filepath} (already has GA4 tracking)")
        return False
    
    ga4_code = get_ga4_code(GA4_MEASUREMENT_ID)
    
    # Find insertion point (after opening <head> tag)
    # Look for <head> with possible attributes
    pattern = r'(<head[^>]*>)'
    
    def insert_ga4(match):
        return match.group(1) + ga4_code
    
    new_content, count = re.subn(pattern, insert_ga4, html_content, count=1, flags=re.IGNORECASE)
    
    if count == 0:
        print(f"  ⚠️  Warning: Could not find <head> in {filepath}")
        return False
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✓ Added GA4 tracking to {filepath}")
    return True


def main():
    """Main function."""
    print("Adding Google Analytics 4 tracking code to HTML files...\n")
    print(f"Using Measurement ID: {GA4_MEASUREMENT_ID}")
    print(f"⚠️  NOTE: Update GA4_MEASUREMENT_ID in this script with your actual ID!\n")
    
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
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if add_ga4_tracking(content, html_file):
            modified_count += 1
    
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Total files processed: {len(html_files)}")
    print(f"Files modified: {modified_count}")
    print(f"Files skipped: {len(html_files) - modified_count}")
    print(f"\n💡 Next steps:")
    print(f"   1. Update GA4_MEASUREMENT_ID in this script with your actual ID")
    print(f"   2. Run this script again to update all files")
    print(f"   3. Set up your Google Analytics property at https://analytics.google.com")
    print(f"   4. Verify tracking is working in GA4 Real-time reports")


if __name__ == '__main__':
    main()
