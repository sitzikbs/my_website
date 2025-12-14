#!/usr/bin/env python3
"""
Check and report heading hierarchy issues in HTML files.
Ensures proper semantic structure: one h1 per page, proper nesting.
"""

import re
from pathlib import Path
from typing import List, Dict, Tuple


def extract_headings(html_content: str, filepath: Path) -> List[Dict]:
    """Extract all heading tags and their levels from HTML content."""
    # Match heading tags with their content
    pattern = r'<h([1-6])[^>]*>(.*?)</h\1>'
    matches = re.findall(pattern, html_content, re.DOTALL | re.IGNORECASE)
    
    headings = []
    for level, content in matches:
        # Clean up content (remove HTML tags, extra whitespace)
        clean_content = re.sub(r'<[^>]+>', '', content)
        clean_content = ' '.join(clean_content.split()).strip()
        
        if clean_content:  # Only include non-empty headings
            headings.append({
                'level': int(level),
                'text': clean_content[:80]  # Truncate long headings
            })
    
    return headings


def check_hierarchy(headings: List[Dict]) -> List[str]:
    """Check for heading hierarchy issues."""
    issues = []
    
    if not headings:
        issues.append("No headings found")
        return issues
    
    # Check for h1
    h1_count = sum(1 for h in headings if h['level'] == 1)
    
    if h1_count == 0:
        issues.append("⚠️  No h1 found")
    elif h1_count > 1:
        issues.append(f"⚠️  Multiple h1 tags ({h1_count} found) - should have exactly one")
    
    # Check for heading level skips
    prev_level = 0
    for i, heading in enumerate(headings):
        level = heading['level']
        
        # Check if we skip levels (e.g., h1 -> h3)
        if prev_level > 0 and level > prev_level + 1:
            issues.append(
                f"⚠️  Heading level skip at position {i+1}: "
                f"h{prev_level} -> h{level} ('{heading['text']}')"
            )
        
        prev_level = level
    
    return issues


def analyze_file(html_file: Path) -> Tuple[List[Dict], List[str]]:
    """Analyze a single HTML file for heading hierarchy."""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    headings = extract_headings(content, html_file)
    issues = check_hierarchy(headings)
    
    return headings, issues


def main():
    """Main function."""
    print("Analyzing heading hierarchy in HTML files...\n")
    
    # Find all HTML files
    html_files = []
    
    # Root HTML files (exclude css-demo.html and templates)
    for html_file in Path('.').glob('*.html'):
        if html_file.name not in ['css-demo.html']:
            html_files.append(html_file)
    
    # Blog post HTML files
    blog_dir = Path('blog/posts')
    if blog_dir.exists():
        html_files.extend(blog_dir.glob('*.html'))
    
    print(f"Found {len(html_files)} HTML files to analyze\n")
    print("="*80)
    
    # Track statistics
    total_issues = 0
    files_with_issues = 0
    perfect_files = []
    
    # Analyze each file
    for html_file in sorted(html_files):
        headings, issues = analyze_file(html_file)
        
        if issues:
            files_with_issues += 1
            total_issues += len(issues)
            
            print(f"\n📄 {html_file}")
            print(f"   Headings: {len(headings)}")
            
            # Show heading structure
            if headings:
                print(f"   Structure:")
                for h in headings[:5]:  # Show first 5 headings
                    indent = "  " * (h['level'] - 1)
                    print(f"     {indent}h{h['level']}: {h['text']}")
                if len(headings) > 5:
                    print(f"     ... ({len(headings) - 5} more)")
            
            # Show issues
            print(f"\n   Issues:")
            for issue in issues:
                print(f"     {issue}")
            print("-" * 80)
        else:
            perfect_files.append(html_file)
    
    # Summary
    print(f"\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    print(f"Total files analyzed: {len(html_files)}")
    print(f"Files with issues: {files_with_issues}")
    print(f"Files with perfect hierarchy: {len(perfect_files)}")
    print(f"Total issues found: {total_issues}")
    
    if perfect_files and len(perfect_files) <= 10:
        print(f"\n✅ Perfect files:")
        for f in perfect_files:
            print(f"   {f}")
    
    print(f"\n💡 Recommendations:")
    print(f"   - Each page should have exactly ONE h1 tag (page title)")
    print(f"   - Headings should not skip levels (h1 -> h2 -> h3, not h1 -> h3)")
    print(f"   - Use h2 for main sections, h3 for subsections, etc.")


if __name__ == '__main__':
    main()
