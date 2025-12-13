#!/usr/bin/env python3
"""
Comprehensive blog post fetcher with correct dates and metadata
Fetches all posts from WordPress sitemap with proper dates, titles, and categories
"""

import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path
import xml.etree.ElementTree as ET
import time

def get_all_post_urls_from_sitemap():
    """Extract all blog post URLs with dates from WordPress sitemap"""
    sitemap_url = "https://www.itzikbs.com/post-sitemap.xml"
    
    print(f"Fetching sitemap from {sitemap_url}")
    response = requests.get(sitemap_url)
    response.raise_for_status()
    
    # Parse XML sitemap
    root = ET.fromstring(response.content)
    
    # Define namespace
    ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    posts = []
    for url_elem in root.findall('sm:url', ns):
        loc = url_elem.find('sm:loc', ns).text
        lastmod = url_elem.find('sm:lastmod', ns)
        
        if lastmod is not None:
            # Parse date (format: 2017-01-30T21:23:42+00:00)
            date_str = lastmod.text
            try:
                # Split on 'T' to separate date from time, then split on '+' to remove timezone
                date_part = date_str.split('T')[0]
                date = date_part  # Already in YYYY-MM-DD format
            except Exception:
                date = '2024-01-01'
        else:
            date = '2024-01-01'
        
        posts.append({
            'url': loc,
            'date': date
        })
    
    print(f"Found {len(posts)} posts in sitemap")
    return posts

def extract_post_metadata(url):
    """Extract title, content, categories from a WordPress post"""
    try:
        response = requests.get(url, timeout=15, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title - try multiple selectors
        title = None
        title_selectors = [
            'h1.entry-title',
            'h1.elementor-heading-title',
            'article h1',
            'h1'
        ]
        
        for selector in title_selectors:
            title_elem = soup.select_one(selector)
            if title_elem:
                title = title_elem.get_text(strip=True)
                break
        
        if not title:
            title = soup.find('title').get_text(strip=True) if soup.find('title') else "Untitled Post"
            # Remove site name from title if present
            title = title.replace(' - Yizhak Ben-Shabat (Itzik), PhD', '').strip()
        
        # Extract categories - try multiple approaches
        categories = []
        
        # Try Elementor category widget
        category_widget = soup.select('.elementor-widget-post-info .elementor-icon-list-item')
        for item in category_widget:
            cat_link = item.find('a')
            if cat_link and '/category/' in cat_link.get('href', ''):
                cat_name = cat_link.get_text(strip=True)
                if cat_name.lower() in ['research', 'personal']:
                    categories.append(cat_name.capitalize())
        
        # Try WordPress category classes
        if not categories:
            post_elem = soup.find('article')
            if post_elem:
                classes = post_elem.get('class', [])
                for cls in classes:
                    if cls.startswith('category-'):
                        cat_name = cls.replace('category-', '').replace('-', ' ').title()
                        if 'research' in cat_name.lower():
                            categories.append('Research')
                        elif 'personal' in cat_name.lower():
                            categories.append('Personal')
        
        # Default to Research if no category found
        if not categories:
            # Check content for clues
            content_text = soup.get_text().lower()
            if 'talking papers' in content_text or 'podcast' in content_text:
                categories = ['Talking Papers Podcast']
            elif any(word in content_text for word in ['conference', 'paper', 'cvpr', 'publication', 'research']):
                categories = ['Research']
            else:
                categories = ['Personal']
        
        # Extract content
        content = None
        content_selectors = [
            '.elementor-widget-theme-post-content',
            'article .entry-content',
            '.post-content',
            'article'
        ]
        
        for selector in content_selectors:
            content_elem = soup.select_one(selector)
            if content_elem:
                content = str(content_elem)
                break
        
        if not content:
            content = "<p>Content extraction failed</p>"
        
        # Extract excerpt
        excerpt = ""
        paragraphs = soup.select('article p')
        for p in paragraphs:
            text = p.get_text(strip=True)
            if len(text) > 50:
                excerpt = text[:300] + "..." if len(text) > 300 else text
                break
        
        return {
            'title': title,
            'content_html': content,
            'categories': categories,
            'excerpt': excerpt
        }
        
    except Exception as e:
        print(f"Error extracting post from {url}: {e}")
        return None

def create_blog_post_file(post_data, date, slug):
    """Create HTML file for blog post with proper styling"""
    
    filename = f"{date}-{slug}.html"
    filepath = Path('blog/posts') / filename
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{post_data['title']} - Itzik Ben-Shabat</title>
    <link rel="stylesheet" href="../../css/style.css?v=5">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        /* Blog post specific styles */
        .blog-post {{ 
            max-width: 900px; 
            margin: 0 auto; 
            padding: 2rem 1.5rem; 
        }}
        
        .post-header {{ 
            margin-bottom: 3rem; 
            border-bottom: 2px solid var(--border-color); 
            padding-bottom: 1.5rem; 
        }}
        
        .post-header h1 {{ 
            font-size: 2.5rem; 
            margin-bottom: 1rem; 
            color: var(--primary-color); 
            line-height: 1.2;
        }}
        
        .post-meta {{ 
            color: var(--text-light); 
            font-size: 0.95rem; 
        }}
        
        .post-meta time {{ 
            margin-right: 1rem; 
        }}
        
        /* Content styling */
        .post-content {{ 
            line-height: 1.8; 
            font-size: 1.05rem;
        }}
        
        .post-content h2,
        .post-content h3.wp-block-heading {{
            margin-top: 2.5rem; 
            margin-bottom: 1.25rem; 
            color: var(--primary-color);
            font-weight: 600;
        }}
        
        .post-content h2 {{
            font-size: 1.75rem;
        }}
        
        .post-content h3,
        .post-content h3.wp-block-heading {{ 
            font-size: 1.4rem;
        }}
        
        .post-content p {{ 
            margin-bottom: 1.25rem; 
        }}
        
        .post-content strong {{
            color: var(--primary-color);
            font-weight: 600;
        }}
        
        /* Images and figures */
        .post-content img {{ 
            max-width: 100%; 
            height: auto; 
            display: block;
            margin: 2rem auto;
            border-radius: 8px;
            box-shadow: var(--shadow);
        }}
        
        .post-content figure {{
            margin: 2rem 0;
            text-align: center;
        }}
        
        .post-content .wp-block-image,
        .post-content .wp-block-gallery {{
            margin: 2rem 0;
        }}
        
        .post-content .wp-block-image.aligncenter,
        .post-content figure.aligncenter {{
            text-align: center;
        }}
        
        .post-content .wp-block-gallery {{
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            justify-content: center;
        }}
        
        .post-content .wp-block-gallery figure {{
            flex: 1 1 300px;
            max-width: 450px;
            margin: 0;
        }}
        
        /* Lists */
        .post-content ul, 
        .post-content ol,
        .post-content .wp-block-list {{ 
            margin-bottom: 1.5rem; 
            padding-left: 2rem; 
        }}
        
        .post-content li {{ 
            margin-bottom: 0.75rem;
            line-height: 1.7;
        }}
        
        .post-content ul {{
            list-style-type: disc;
        }}
        
        /* Links */
        .post-content a {{ 
            color: var(--secondary-color); 
            text-decoration: none; 
            border-bottom: 1px solid transparent;
            transition: var(--transition);
        }}
        
        .post-content a:hover {{ 
            border-bottom-color: var(--secondary-color);
        }}
        
        /* Code blocks */
        .post-content blockquote {{ 
            border-left: 4px solid var(--secondary-color); 
            padding-left: 1.5rem; 
            margin: 2rem 0; 
            font-style: italic; 
            color: var(--text-color);
            background-color: var(--bg-light);
            padding: 1rem 1.5rem;
            border-radius: var(--radius);
        }}
        
        .post-content code {{ 
            background-color: var(--bg-light); 
            padding: 0.2rem 0.5rem; 
            border-radius: 4px; 
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }}
        
        .post-content pre {{ 
            background-color: #1f2937; 
            color: #f9fafb; 
            padding: 1.5rem; 
            border-radius: var(--radius); 
            overflow-x: auto;
            margin: 2rem 0;
        }}
        
        .post-content pre code {{
            background-color: transparent;
            padding: 0;
        }}
        
        /* WordPress specific cleanup */
        .elementor-widget-container {{
            width: 100%;
        }}
        
        @media (max-width: 768px) {{
            .post-header h1 {{
                font-size: 2rem;
            }}
            
            .blog-post {{
                padding: 1rem;
            }}
            
            .post-content {{
                font-size: 1rem;
            }}
        }}
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="nav-brand">
                <a href="../../index.html">Itzik Ben-Shabat</a>
            </div>
            <button class="nav-toggle" aria-label="Toggle navigation">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-menu">
                <li><a href="../../index.html">About</a></li>
                <li><a href="../../publications.html">Publications</a></li>
                <li><a href="../../blog.html">Blog</a></li>
                <li><a href="../../contact.html">Contact</a></li>
            </ul>
        </div>
    </nav>
    <main>
        <article class="blog-post">
            <header class="post-header">
                <h1>{post_data['title']}</h1>
                <div class="post-meta">
                    <time datetime="{date}">{date}</time>
                    <span class="author">By Itzik Ben-Shabat</span>
                </div>
            </header>
            <div class="post-content">
                {post_data['content_html']}
            </div>
        </article>
    </main>
    <script src="../../js/main.js"></script>
</body>
</html>"""
    
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return filename

def main():
    # Get all posts from sitemap
    posts = get_all_post_urls_from_sitemap()
    
    # Load existing blog index if it exists to resume
    index_path = Path('data/blog-index.json')
    if index_path.exists():
        with open(index_path, 'r', encoding='utf-8') as f:
            blog_index = json.load(f)
        existing_ids = {post['id'] for post in blog_index.get('posts', [])}
        print(f"Found {len(existing_ids)} existing posts, will skip those")
    else:
        blog_index = {
            "posts": [],
            "categories": [
                {
                    "name": "Research",
                    "slug": "research",
                    "description": "Research updates and insights"
                },
                {
                    "name": "Personal",
                    "slug": "personal",
                    "description": "Personal updates and reflections"
                },
                {
                    "name": "Talking Papers Podcast",
                    "slug": "talking-papers-podcast",
                    "description": "Episodes from the Talking Papers Podcast"
                }
            ],
            "tags": []
        }
        existing_ids = set()
    
    successful = 0
    failed = 0
    skipped = 0
    
    for i, post_info in enumerate(posts, 1):
        url = post_info['url']
        date = post_info['date']
        
        # Extract slug from URL
        slug = url.rstrip('/').split('/')[-1]
        
        # Skip certain pages
        skip_slugs = ['reaserch-blog', 'recommended-courses']
        if slug in skip_slugs:
            print(f"[{i}/{len(posts)}] Skipping non-post: {slug}")
            skipped += 1
            continue
        
        # Skip if already processed
        if slug in existing_ids:
            print(f"[{i}/{len(posts)}] Already exists: {slug}")
            skipped += 1
            continue
        
        print(f"\n[{i}/{len(posts)}] Processing: {slug}")
        
        # Extract post metadata with retry
        max_retries = 3
        post_data = None
        for retry in range(max_retries):
            try:
                post_data = extract_post_metadata(url)
                if post_data:
                    break
            except Exception as e:
                print(f"  Retry {retry + 1}/{max_retries}: {e}")
                if retry < max_retries - 1:
                    time.sleep(3)
        
        if not post_data:
            print(f"  ✗ Failed after {max_retries} attempts")
            failed += 1
            # Save progress even on failure
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(blog_index, f, indent=4, ensure_ascii=False)
            continue
        
        # Create blog post file
        try:
            filename = create_blog_post_file(post_data, date, slug)
            
            # Add to index
            blog_index['posts'].append({
                'id': slug,
                'title': post_data['title'],
                'date': date,
                'updated': date,
                'author': 'Itzik Ben-Shabat',
                'excerpt': post_data['excerpt'],
                'content': f'/blog/posts/{filename}',
                'categories': post_data['categories'],
                'tags': []
            })
            
            successful += 1
            print(f"  ✓ Created: {filename}")
            
            # Save progress after each successful post
            blog_index['posts'].sort(key=lambda x: x['date'], reverse=True)
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(blog_index, f, indent=4, ensure_ascii=False)
            
            # Be nice to the server - longer delay to avoid rate limits
            time.sleep(2)
            
        except Exception as e:
            print(f"  ✗ Failed to create post: {e}")
            failed += 1
            # Save progress even on failure
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(blog_index, f, indent=4, ensure_ascii=False)
    
    print(f"\n{'='*60}")
    print(f"✓ Successfully created {successful} blog posts")
    print(f"✗ Failed: {failed}")
    print(f"⊘ Skipped: {skipped}")
    print(f"✓ Total in index: {len(blog_index['posts'])} posts")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
