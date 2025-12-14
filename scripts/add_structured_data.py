#!/usr/bin/env python3
"""
Add Schema.org structured data (JSON-LD) to HTML files.
"""

import json
import re
from pathlib import Path
from typing import Dict, Optional
from datetime import datetime


def generate_person_schema() -> str:
    """Generate Person schema for homepage."""
    schema = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Itzik Ben-Shabat",
        "url": "https://www.itzikbs.com",
        "image": "https://www.itzikbs.com/assets/images/profile/Itzik_Ben_Shabat_portrait.jpg",
        "jobTitle": "Research Scientist",
        "worksFor": {
            "@type": "Organization",
            "name": "Australian National University"
        },
        "alumniOf": [
            {
                "@type": "Organization",
                "name": "Technion - Israel Institute of Technology"
            }
        ],
        "sameAs": [
            "https://github.com/sitzikbs",
            "https://twitter.com/sitzikbs",
            "https://www.linkedin.com/in/yizhak-itzik-ben-shabat-67b3b1b7/"
        ]
    }
    
    return json.dumps(schema, indent=2)


def extract_blog_date(html_content: str, filepath: Path) -> Optional[str]:
    """Extract publication date from blog post filename or content."""
    # Try to extract from filename (format: YYYY-MM-DD-title.html)
    match = re.search(r'(\d{4})-(\d{2})-(\d{2})', filepath.name)
    if match:
        year, month, day = match.groups()
        return f"{year}-{month}-{day}"
    
    # Try to extract from content
    date_match = re.search(r'<time[^>]*datetime="([^"]+)"', html_content)
    if date_match:
        return date_match.group(1)
    
    return None


def generate_blog_post_schema(html_content: str, filepath: Path) -> str:
    """Generate BlogPosting schema for blog posts."""
    # Extract title
    title_match = re.search(r'<h1[^>]*>([^<]+)</h1>', html_content)
    title = title_match.group(1).strip() if title_match else filepath.stem.replace('-', ' ').title()
    
    # Extract date
    date_published = extract_blog_date(html_content, filepath)
    
    # Extract first paragraph as description
    desc_match = re.search(r'<p[^>]*>([^<]+)</p>', html_content)
    description = desc_match.group(1).strip() if desc_match else ""
    if len(description) > 200:
        description = description[:197] + "..."
    
    url = f"https://www.itzikbs.com/blog/posts/{filepath.name}"
    
    schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": title,
        "url": url,
        "author": {
            "@type": "Person",
            "name": "Itzik Ben-Shabat",
            "url": "https://www.itzikbs.com"
        },
        "publisher": {
            "@type": "Person",
            "name": "Itzik Ben-Shabat"
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": url
        }
    }
    
    if date_published:
        schema["datePublished"] = date_published
        schema["dateModified"] = date_published
    
    if description:
        schema["description"] = description
    
    return json.dumps(schema, indent=2)


def generate_website_schema(page_type: str) -> str:
    """Generate WebSite or WebPage schema for other pages."""
    schema = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "Itzik Ben-Shabat",
        "url": "https://www.itzikbs.com",
        "author": {
            "@type": "Person",
            "name": "Itzik Ben-Shabat"
        }
    }
    
    return json.dumps(schema, indent=2)


def add_structured_data(html_file: Path) -> bool:
    """Add Schema.org structured data to an HTML file."""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has structured data
    if 'application/ld+json' in content or '@context' in content:
        print(f"  ⏭️  Skipping {html_file} (already has structured data)")
        return False
    
    # Determine schema type based on file
    if html_file.name == 'index.html':
        schema_json = generate_person_schema()
    elif html_file.parent.name == 'posts':
        schema_json = generate_blog_post_schema(content, html_file)
    else:
        schema_json = generate_website_schema(html_file.stem)
    
    # Create script tag
    script_tag = f'''
  <!-- Structured Data (Schema.org) -->
  <script type="application/ld+json">
  {schema_json}
  </script>'''
    
    # Find insertion point (before </head>)
    pattern = r'(</head>)'
    
    def insert_schema(match):
        return script_tag + '\n' + match.group(1)
    
    new_content, count = re.subn(pattern, insert_schema, content, count=1)
    
    if count == 0:
        print(f"  ⚠️  Warning: Could not find </head> in {html_file}")
        return False
    
    # Write back
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✓ Added structured data to {html_file}")
    return True


def main():
    """Main function."""
    print("Adding Schema.org structured data to HTML files...\n")
    
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
        if add_structured_data(html_file):
            modified_count += 1
    
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Total files processed: {len(html_files)}")
    print(f"Files modified: {modified_count}")
    print(f"Files skipped: {len(html_files) - modified_count}")
    print(f"\n💡 Note: You may want to update social media URLs in index.html")
    print(f"   and verify dates in blog post structured data.")


if __name__ == '__main__':
    main()
