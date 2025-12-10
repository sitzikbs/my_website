#!/usr/bin/env python3
"""
Fix titles in blog-index.json by extracting from the HTML files
"""

import json
from pathlib import Path
from bs4 import BeautifulSoup

def extract_title_from_html(html_path):
    """Extract the actual title from a blog post HTML file"""
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        
        # Try to find h1 in post-header
        h1 = soup.select_one('.post-header h1')
        if h1:
            return h1.get_text(strip=True)
        
        # Fallback to any h1
        h1 = soup.find('h1')
        if h1:
            return h1.get_text(strip=True)
        
        return None
    except Exception as e:
        print(f"Error reading {html_path}: {e}")
        return None

def main():
    # Load blog index
    index_path = Path('data/blog-index.json')
    with open(index_path, 'r', encoding='utf-8') as f:
        blog_index = json.load(f)
    
    fixed = 0
    for post in blog_index['posts']:
        # Check if title is the generic one
        if post['title'] == "Yizhak Ben-Shabat (Itzik), PhD":
            # Extract filename from content path
            content_path = post['content'].lstrip('/')
            html_path = Path(content_path)
            
            if html_path.exists():
                title = extract_title_from_html(html_path)
                if title and title != "Yizhak Ben-Shabat (Itzik), PhD":
                    print(f"Fixing: {post['id']}")
                    print(f"  Old: {post['title']}")
                    print(f"  New: {title}")
                    post['title'] = title
                    fixed += 1
    
    # Save updated index
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(blog_index, f, indent=4, ensure_ascii=False)
    
    print(f"\n✓ Fixed {fixed} titles")

if __name__ == "__main__":
    main()
