#!/usr/bin/env python3
"""
Fix blog posts by re-extracting titles and excerpts from WordPress
Updates both the JSON and the HTML files
"""

import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path
import time

def extract_title_and_excerpt_from_wordpress(url):
    """Extract the actual post title and excerpt from WordPress"""
    try:
        response = requests.get(url, timeout=15, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Try to find the post title (not the site header)
        title = None
        
        # Look for post title in elementor content area first
        post_content = soup.select_one('.elementor-widget-theme-post-title')
        if post_content:
            title_elem = post_content.find(['h1', 'h2'])
            if title_elem:
                title = title_elem.get_text(strip=True)
        
        # Try article heading
        if not title:
            article = soup.find('article')
            if article:
                # Find h1/h2 that's NOT the site header
                for heading in article.find_all(['h1', 'h2']):
                    heading_text = heading.get_text(strip=True)
                    if heading_text and heading_text != "Yizhak Ben-Shabat (Itzik), PhD":
                        title = heading_text
                        break
        
        # Fallback to page title
        if not title:
            title_tag = soup.find('title')
            if title_tag:
                title = title_tag.get_text(strip=True)
                title = title.replace(' - Yizhak Ben-Shabat (Itzik), PhD', '').strip()
        
        # Extract excerpt from first paragraph
        excerpt = ""
        content_area = soup.select_one('.elementor-widget-theme-post-content')
        if content_area:
            paragraphs = content_area.find_all('p', recursive=True)
            for p in paragraphs:
                text = p.get_text(strip=True)
                if len(text) > 50:
                    excerpt = text[:300] + "..." if len(text) > 300 else text
                    break
        
        return title, excerpt
        
    except Exception as e:
        print(f"  Error: {e}")
        return None, None

def update_html_file(filepath, new_title):
    """Update the title in an HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the h1 title
        content = content.replace(
            '<h1>Yizhak Ben-Shabat (Itzik), PhD</h1>',
            f'<h1>{new_title}</h1>'
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"  Error updating HTML: {e}")
        return False

def main():
    # Load blog index
    index_path = Path('data/blog-index.json')
    with open(index_path, 'r', encoding='utf-8') as f:
        blog_index = json.load(f)
    
    fixed = 0
    failed = 0
    
    for i, post in enumerate(blog_index['posts'], 1):
        # Check if title needs fixing
        if post['title'] == "Yizhak Ben-Shabat (Itzik), PhD" or not post['excerpt']:
            slug = post['id']
            url = f"https://www.itzikbs.com/{slug}"
            
            print(f"[{i}/{len(blog_index['posts'])}] Fixing: {slug}")
            
            # Extract from WordPress
            title, excerpt = extract_title_and_excerpt_from_wordpress(url)
            
            if title and title != "Yizhak Ben-Shabat (Itzik), PhD":
                # Update JSON
                post['title'] = title
                if excerpt:
                    post['excerpt'] = excerpt
                
                # Update HTML file
                content_path = post['content'].lstrip('/')
                html_path = Path(content_path)
                if html_path.exists():
                    update_html_file(html_path, title)
                
                print(f"  ✓ {title[:60]}...")
                fixed += 1
                
                # Save progress after each update
                with open(index_path, 'w', encoding='utf-8') as f:
                    json.dump(blog_index, f, indent=4, ensure_ascii=False)
                
                time.sleep(1)  # Be nice to the server
            else:
                print(f"  ✗ Could not extract title")
                failed += 1
    
    print(f"\n{'='*60}")
    print(f"✓ Fixed {fixed} posts")
    print(f"✗ Failed {failed} posts")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
