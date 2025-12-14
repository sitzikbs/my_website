#!/usr/bin/env python3
"""
Comprehensive accessibility audit for HTML files.
Checks WCAG 2.1 AA compliance for common issues.
"""

import re
from pathlib import Path
from collections import defaultdict
from html.parser import HTMLParser


class AccessibilityChecker(HTMLParser):
    """Parse HTML and check for accessibility issues."""
    
    def __init__(self):
        super().__init__()
        self.issues = []
        self.images = []
        self.links = []
        self.headings = []
        self.forms = []
        self.in_nav = False
        self.has_skip_link = False
        self.has_main_landmark = False
        self.has_h1 = False
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        # Check images for alt text
        if tag == 'img':
            alt = attrs_dict.get('alt')
            src = attrs_dict.get('src', 'unknown')
            if alt is None:
                self.issues.append(f"Missing alt attribute on image: {src}")
            elif alt == '':
                # Empty alt is OK for decorative images, but note it
                pass
            self.images.append((src, alt))
        
        # Check links
        if tag == 'a':
            href = attrs_dict.get('href')
            if href and href == '#':
                self.issues.append("Empty link (href='#') - should have meaningful destination")
        
        # Check headings
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.headings.append(tag)
            if tag == 'h1':
                self.has_h1 = True
        
        # Check for skip link
        if tag == 'a' and attrs_dict.get('href') == '#main-content':
            self.has_skip_link = True
        
        # Check for main landmark
        if tag == 'main':
            self.has_main_landmark = True
        
        # Check nav
        if tag == 'nav':
            self.in_nav = True
        
        # Check form inputs
        if tag == 'input':
            input_type = attrs_dict.get('type', 'text')
            label_id = attrs_dict.get('id')
            aria_label = attrs_dict.get('aria-label')
            if input_type not in ['hidden', 'submit', 'button'] and not label_id and not aria_label:
                self.issues.append(f"Input field missing id or aria-label: type={input_type}")
    
    def handle_endtag(self, tag):
        if tag == 'nav':
            self.in_nav = False


def check_file(filepath: Path) -> dict:
    """Check a single HTML file for accessibility issues."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    checker = AccessibilityChecker()
    try:
        checker.feed(html_content)
    except Exception as e:
        return {
            'file': filepath,
            'error': f"Parse error: {e}",
            'issues': []
        }
    
    # Additional checks
    issues = checker.issues.copy()
    
    # Check for lang attribute
    if not re.search(r'<html[^>]*\slang=', html_content, re.IGNORECASE):
        issues.append("Missing lang attribute on <html> tag")
    
    # Check for page title
    if not re.search(r'<title>.*?</title>', html_content, re.IGNORECASE):
        issues.append("Missing or empty <title> tag")
    
    # Check for viewport meta tag (mobile accessibility)
    if not re.search(r'<meta[^>]*name=["\']viewport["\']', html_content, re.IGNORECASE):
        issues.append("Missing viewport meta tag for mobile accessibility")
    
    # Check for skip link
    if not checker.has_skip_link:
        issues.append("Missing skip to main content link (recommended for keyboard navigation)")
    
    # Check for main landmark
    if not checker.has_main_landmark:
        issues.append("Missing <main> landmark (helps screen readers)")
    
    # Check for h1
    if not checker.has_h1:
        issues.append("Missing h1 heading (every page should have one)")
    
    return {
        'file': filepath,
        'issues': issues,
        'images': len(checker.images),
        'images_without_alt': len([img for img in checker.images if img[1] is None]),
        'headings': len(checker.headings),
        'has_h1': checker.has_h1
    }


def main():
    """Main function."""
    print("=" * 70)
    print("ACCESSIBILITY AUDIT - WCAG 2.1 AA")
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
    
    print(f"Checking {len(html_files)} HTML files...\n")
    
    # Check all files
    all_results = []
    total_issues = 0
    files_with_issues = 0
    
    for html_file in sorted(html_files):
        result = check_file(html_file)
        all_results.append(result)
        
        if result.get('issues'):
            total_issues += len(result['issues'])
            files_with_issues += 1
    
    # Summary statistics
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total files checked: {len(html_files)}")
    print(f"Files with issues: {files_with_issues}")
    print(f"Files passed: {len(html_files) - files_with_issues}")
    print(f"Total issues found: {total_issues}")
    print()
    
    # Issue breakdown
    if total_issues > 0:
        print("=" * 70)
        print("ISSUE BREAKDOWN")
        print("=" * 70)
        
        issue_counts = defaultdict(int)
        for result in all_results:
            for issue in result.get('issues', []):
                # Generalize issue for counting
                if 'alt' in issue.lower():
                    issue_counts['Missing alt attributes'] += 1
                elif 'skip' in issue.lower():
                    issue_counts['Missing skip link'] += 1
                elif 'main' in issue.lower() and 'landmark' in issue.lower():
                    issue_counts['Missing main landmark'] += 1
                elif 'h1' in issue.lower():
                    issue_counts['Missing h1'] += 1
                elif 'lang' in issue.lower():
                    issue_counts['Missing lang attribute'] += 1
                else:
                    issue_counts[issue] += 1
        
        for issue, count in sorted(issue_counts.items(), key=lambda x: -x[1]):
            print(f"  • {issue}: {count} occurrence(s)")
        print()
    
    # Files with most issues
    if files_with_issues > 0:
        print("=" * 70)
        print("TOP 10 FILES WITH MOST ISSUES")
        print("=" * 70)
        
        sorted_results = sorted(all_results, key=lambda x: len(x.get('issues', [])), reverse=True)
        for result in sorted_results[:10]:
            if result.get('issues'):
                print(f"\n{result['file']} ({len(result['issues'])} issues):")
                for issue in result['issues'][:5]:  # Show first 5 issues
                    print(f"  • {issue}")
                if len(result['issues']) > 5:
                    print(f"  ... and {len(result['issues']) - 5} more")
    
    print()
    print("=" * 70)
    if total_issues == 0:
        print("✅ ALL CHECKS PASSED!")
    else:
        print(f"⚠️  Found {total_issues} accessibility issues across {files_with_issues} files")
        print("\nRecommended actions:")
        print("  1. Add skip to main content links")
        print("  2. Ensure all images have alt text")
        print("  3. Add <main> landmark to pages")
        print("  4. Verify color contrast ratios (use browser dev tools)")
        print("  5. Test keyboard navigation manually")
    print("=" * 70)


if __name__ == "__main__":
    main()
