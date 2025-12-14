#!/usr/bin/env python3
"""
Add accessibility improvements to HTML files:
- Skip to main content links
- Main landmarks where missing
- Fix missing titles and empty links
"""

import re
from pathlib import Path


def add_skip_link(html_content: str) -> str:
    """Add skip to main content link right after opening body tag."""
    
    # Check if skip link already exists
    if 'skip-link' in html_content or 'skip to main' in html_content.lower():
        return html_content
    
    # Find the opening body tag and insert skip link after it
    pattern = r'(<body[^>]*>)'
    replacement = r'\1\n  <a href="#main-content" class="skip-link">Skip to main content</a>'
    
    new_content = re.sub(pattern, replacement, html_content, count=1, flags=re.IGNORECASE)
    
    return new_content


def add_main_landmark(html_content: str) -> str:
    """Add main landmark if missing."""
    
    # Check if main landmark already exists
    if re.search(r'<main[\s>]', html_content, re.IGNORECASE):
        return html_content
    
    # Look for common content wrapper patterns to wrap in <main>
    # Pattern 1: Look for content div/section after header/nav
    pattern1 = r'(</(?:header|nav)>\s*)((?:<div|<section)[^>]*class="[^"]*content[^"]*"[^>]*>)'
    if re.search(pattern1, html_content, re.IGNORECASE):
        html_content = re.sub(
            pattern1,
            r'\1<main id="main-content">\n  \2',
            html_content,
            count=1,
            flags=re.IGNORECASE
        )
        # Find the closing tag and add </main> before footer or end of body
        pattern_close = r'(</(?:div|section)>\s*)(</body>|<footer)'
        html_content = re.sub(
            pattern_close,
            r'\1</main>\n\2',
            html_content,
            count=1,
            flags=re.IGNORECASE
        )
    else:
        # Pattern 2: If no clear content div, wrap everything between header and footer
        pattern2 = r'(</(?:header|nav)>\s*)(.+?)(\s*<footer)'
        if re.search(pattern2, html_content, re.DOTALL | re.IGNORECASE):
            html_content = re.sub(
                pattern2,
                r'\1<main id="main-content">\n\2\n</main>\3',
                html_content,
                count=1,
                flags=re.DOTALL | re.IGNORECASE
            )
        else:
            # Pattern 3: Just add main with ID for skip link target
            # Find first content after body and before footer
            pattern3 = r'(<body[^>]*>\s*(?:<a[^>]*skip[^>]*>.*?</a>\s*)?)'
            html_content = re.sub(
                pattern3,
                r'\1\n<div id="main-content"></div>',
                html_content,
                count=1,
                flags=re.IGNORECASE
            )
    
    return html_content


def fix_empty_links(html_content: str) -> str:
    """Fix links with href='#' by making them buttons or removing href."""
    
    # Find links with href="#" that are not skip links
    pattern = r'<a\s+([^>]*)href=["\'](#)["\']([^>]*)>'
    
    def replace_empty_link(match):
        before_href = match.group(1)
        after_href = match.group(3)
        
        # If it has onclick or is a button-like element, convert to button
        if 'onclick' in before_href.lower() or 'button' in before_href.lower():
            return f'<button {before_href}{after_href} type="button">'
        # Otherwise, remove the href to make it non-interactive
        return f'<span {before_href}{after_href}>'
    
    html_content = re.sub(pattern, replace_empty_link, html_content, flags=re.IGNORECASE)
    
    return html_content


def add_title_if_missing(html_content: str, filepath: Path) -> str:
    """Add title tag if missing."""
    
    # Check if title exists and is not empty
    if re.search(r'<title>\s*\S+.*?</title>', html_content, re.IGNORECASE):
        return html_content
    
    # Generate title from filename
    filename = filepath.stem
    if filename == 'index':
        title = "Itzik Ben Shabat - 3D Computer Vision Research"
    elif filename == 'about':
        title = "About - Itzik Ben Shabat"
    elif filename == 'contact':
        title = "Contact - Itzik Ben Shabat"
    elif filename == 'publications':
        title = "Publications - Itzik Ben Shabat"
    elif filename == 'blog':
        title = "Research Blog - Itzik Ben Shabat"
    else:
        # Convert filename to readable title
        title = filename.replace('-', ' ').title() + " - Itzik Ben Shabat"
    
    # If title tag exists but is empty, replace it
    if re.search(r'<title>\s*</title>', html_content, re.IGNORECASE):
        html_content = re.sub(
            r'<title>\s*</title>',
            f'<title>{title}</title>',
            html_content,
            count=1,
            flags=re.IGNORECASE
        )
    else:
        # Add title tag in head
        html_content = re.sub(
            r'(<head[^>]*>)',
            f'\\1\n  <title>{title}</title>',
            html_content,
            count=1,
            flags=re.IGNORECASE
        )
    
    return html_content


def process_file(filepath: Path) -> tuple[bool, list[str]]:
    """Process a single HTML file to add accessibility improvements."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    html_content = original_content
    changes = []
    
    # Add skip link
    new_content = add_skip_link(html_content)
    if new_content != html_content:
        changes.append("Added skip link")
        html_content = new_content
    
    # Add main landmark
    new_content = add_main_landmark(html_content)
    if new_content != html_content:
        changes.append("Added main landmark")
        html_content = new_content
    
    # Fix empty links
    new_content = fix_empty_links(html_content)
    if new_content != html_content:
        changes.append("Fixed empty links")
        html_content = new_content
    
    # Add title if missing
    new_content = add_title_if_missing(html_content, filepath)
    if new_content != html_content:
        changes.append("Added title tag")
        html_content = new_content
    
    # Write back if changed
    if html_content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        return True, changes
    
    return False, []


def main():
    """Main function."""
    print("=" * 70)
    print("ADDING ACCESSIBILITY IMPROVEMENTS")
    print("=" * 70)
    print()
    
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
    
    print(f"Processing {len(html_files)} HTML files...\n")
    
    # Process all files
    modified_count = 0
    change_summary = {
        'skip_link': 0,
        'main_landmark': 0,
        'empty_links': 0,
        'title': 0
    }
    
    for html_file in sorted(html_files):
        modified, changes = process_file(html_file)
        if modified:
            modified_count += 1
            print(f"✓ {html_file}")
            for change in changes:
                print(f"  • {change}")
                if 'skip link' in change.lower():
                    change_summary['skip_link'] += 1
                if 'main landmark' in change.lower():
                    change_summary['main_landmark'] += 1
                if 'empty links' in change.lower():
                    change_summary['empty_links'] += 1
                if 'title' in change.lower():
                    change_summary['title'] += 1
    
    print(f"\n{'=' * 70}")
    print("SUMMARY")
    print(f"{'=' * 70}")
    print(f"Total files processed: {len(html_files)}")
    print(f"Files modified: {modified_count}")
    print(f"Files unchanged: {len(html_files) - modified_count}")
    print()
    print("Changes made:")
    print(f"  • Skip links added: {change_summary['skip_link']}")
    print(f"  • Main landmarks added: {change_summary['main_landmark']}")
    print(f"  • Empty links fixed: {change_summary['empty_links']}")
    print(f"  • Titles added: {change_summary['title']}")
    print()
    print("✅ Accessibility improvements complete!")
    print("   Run check_accessibility.py to verify")


if __name__ == "__main__":
    main()
