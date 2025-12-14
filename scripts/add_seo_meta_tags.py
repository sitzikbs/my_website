#!/usr/bin/env python3
"""
Add SEO meta tags (Open Graph, Twitter Cards, etc.) to HTML files.
"""

import re
from pathlib import Path
from typing import Dict, Optional


def extract_page_info(html_content: str, filepath: Path) -> Dict[str, str]:
    """Extract page information for meta tags."""
    # Extract title
    title_match = re.search(r'<title>([^<]+)</title>', html_content)
    title = title_match.group(1) if title_match else "Itzik Ben-Shabat"
    
    # Extract description from meta tag if exists
    desc_match = re.search(r'<meta\s+content="([^"]+)"\s+name="description"', html_content)
    description = desc_match.group(1) if desc_match else "Personal website and blog"
    
    # Determine page type and URL
    filename = filepath.stem
    if filename == 'index':
        url = "https://www.itzikbs.com/"
        og_type = "website"
    elif filepath.parent.name == 'posts':
        url = f"https://www.itzikbs.com/blog/posts/{filename}.html"
        og_type = "article"
    else:
        url = f"https://www.itzikbs.com/{filename}.html"
        og_type = "website"
    
    # Default image
    image = "https://www.itzikbs.com/assets/images/profile/Itzik_Ben_Shabat_portrait.jpg"
    
    return {
        'title': title,
        'description': description,
        'url': url,
        'type': og_type,
        'image': image
    }


def generate_meta_tags(page_info: Dict[str, str]) -> str:
    """Generate meta tags HTML."""
    return f'''
  <!-- SEO Meta Tags -->
  <meta name="description" content="{page_info['description']}">
  <meta name="author" content="Itzik Ben-Shabat">
  <link rel="canonical" href="{page_info['url']}">
  
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="{page_info['type']}">
  <meta property="og:url" content="{page_info['url']}">
  <meta property="og:title" content="{page_info['title']}">
  <meta property="og:description" content="{page_info['description']}">
  <meta property="og:image" content="{page_info['image']}">
  <meta property="og:site_name" content="Itzik Ben-Shabat">
  
  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="{page_info['url']}">
  <meta name="twitter:title" content="{page_info['title']}">
  <meta name="twitter:description" content="{page_info['description']}">
  <meta name="twitter:image" content="{page_info['image']}">'''


def add_meta_tags(html_file: Path) -> bool:
    """Add SEO meta tags to an HTML file."""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has Open Graph tags
    if 'og:title' in content:
        print(f"  ⏭️  Skipping {html_file} (already has meta tags)")
        return False
    
    # Extract page info
    page_info = extract_page_info(content, html_file)
    
    # Generate meta tags
    meta_tags = generate_meta_tags(page_info)
    
    # Find insertion point (after the last preconnect/resource hint link or after viewport)
    # Try after the Google Fonts stylesheet link
    pattern = r'(<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]+>)'
    
    def insert_meta(match):
        return match.group(1) + '\n' + meta_tags
    
    new_content, count = re.subn(pattern, insert_meta, content, count=1)
    
    if count == 0:
        # Try after viewport meta
        pattern = r'(<meta\s+name="viewport"[^>]+>)'
        new_content, count = re.subn(pattern, insert_meta, content, count=1)
    
    if count == 0:
        # Try after charset
        pattern = r'(<meta\s+charset="[^"]+"\s*/>)'
        new_content, count = re.subn(pattern, insert_meta, content, count=1)
    
    if count == 0:
        print(f"  ⚠️  Warning: Could not find insertion point in {html_file}")
        return False
    
    # Write back
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✓ Added SEO meta tags to {html_file}")
    return True


def main():
    """Main function."""
    print("Adding SEO meta tags to HTML files...\n")
    
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
        if add_meta_tags(html_file):
            modified_count += 1
    
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Total files processed: {len(html_files)}")
    print(f"Files modified: {modified_count}")
    print(f"Files skipped: {len(html_files) - modified_count}")


if __name__ == '__main__':
    main()
