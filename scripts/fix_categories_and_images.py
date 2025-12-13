#!/usr/bin/env python3
"""
Fix categories and extract featured images from WordPress posts
Only posts under /category/talking-tapers-podcast should be labeled as Podcast
"""

import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path
import time

def extract_category_and_image_from_wordpress(url):
    """Extract the actual category and featured image from WordPress"""
    try:
        response = requests.get(url, timeout=15, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract category from the URL in breadcrumbs or category links
        categories = []
        is_podcast = False
        
        # Check if URL or page links contain the podcast category
        page_html = response.text.lower()
        if '/category/talking-tapers-podcast' in page_html or 'talking-tapers-podcast' in url:
            categories = ['Talking Papers Podcast']
            is_podcast = True
        else:
            # Try to find category links
            category_links = soup.select('a[href*="/category/"]')
            for link in category_links:
                href = link.get('href', '').lower()
                if 'research' in href or 'reaserch' in href:
                    categories = ['Research']
                    break
                elif 'personal' in href:
                    categories = ['Personal']
                    break
            
            # If no category found, check article classes
            if not categories:
                article = soup.find('article')
                if article:
                    classes = article.get('class', [])
                    for cls in classes:
                        if 'research' in cls.lower():
                            categories = ['Research']
                            break
                        elif 'personal' in cls.lower():
                            categories = ['Personal']
                            break
            
            # Default based on content
            if not categories:
                content_text = soup.get_text().lower()
                if any(word in content_text for word in ['conference', 'paper', 'cvpr', 'iccv', 'neurips', 'publication']):
                    categories = ['Research']
                else:
                    categories = ['Personal']
        
        # Extract featured image
        image_url = None
        
        # Try multiple selectors for featured image
        image_selectors = [
            'meta[property="og:image"]',
            'article img',
            '.wp-post-image',
            '.elementor-widget-image img',
            '.entry-content img'
        ]
        
        for selector in image_selectors:
            if selector.startswith('meta'):
                img_tag = soup.select_one(selector)
                if img_tag:
                    image_url = img_tag.get('content')
                    if image_url and image_url.startswith('http'):
                        break
            else:
                img_tag = soup.select_one(selector)
                if img_tag:
                    image_url = img_tag.get('src')
                    if image_url and image_url.startswith('http'):
                        # Skip very small images (likely icons)
                        width = img_tag.get('width')
                        if width and int(width) < 100:
                            continue
                        break
        
        return categories, image_url
        
    except Exception as e:
        print(f"  Error: {e}")
        return None, None

def main():
    # Load blog index
    index_path = Path('data/blog-index.json')
    with open(index_path, 'r', encoding='utf-8') as f:
        blog_index = json.load(f)
    
    fixed_categories = 0
    added_images = 0
    
    for i, post in enumerate(blog_index['posts'], 1):
        slug = post['id']
        url = f"https://www.itzikbs.com/{slug}"
        
        print(f"[{i}/{len(blog_index['posts'])}] Processing: {slug}")
        
        # Extract from WordPress
        categories, image_url = extract_category_and_image_from_wordpress(url)
        
        if categories:
            old_categories = post.get('categories', [])
            if old_categories != categories:
                post['categories'] = categories
                print(f"  ✓ Category: {old_categories} → {categories}")
                fixed_categories += 1
        
        if image_url:
            if not post.get('image') or post['image'] != image_url:
                post['image'] = image_url
                print(f"  ✓ Image: {image_url[:60]}...")
                added_images += 1
        
        # Save progress after every 10 updates
        if i % 10 == 0:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(blog_index, f, indent=4, ensure_ascii=False)
        
        time.sleep(0.5)  # Be nice to the server
    
    # Final save
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(blog_index, f, indent=4, ensure_ascii=False)
    
    print(f"\n{'='*60}")
    print(f"✓ Fixed {fixed_categories} categories")
    print(f"✓ Added {added_images} images")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
