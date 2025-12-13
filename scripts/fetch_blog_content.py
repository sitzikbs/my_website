#!/usr/bin/env python3
"""
Fetch blog post content from the WordPress site using the sitemap
"""

import json
import requests
from bs4 import BeautifulSoup
import re
from pathlib import Path

# Key blog posts to fetch (most recent and important ones)
PRIORITY_POSTS = [
    "https://www.itzikbs.com/cvpr2024",
    "https://www.itzikbs.com/3dpaintbrush",
    "https://www.itzikbs.com/career_update_2024",
    "https://www.itzikbs.com/wacv2024",
    "https://www.itzikbs.com/cvpr-2023",
    "https://www.itzikbs.com/cvpr-2022",
    "https://www.itzikbs.com/the-talking-papers-podcast",
    "https://www.itzikbs.com/the-story-behind-the-ikea-assembly-dataset-paper",
    "https://www.itzikbs.com/surface-fitting-for-3d-point-cloud-deepfit",
    "https://www.itzikbs.com/how-to-stand-out-academically-during-covid-19",
    "https://www.itzikbs.com/cvpr-2019",
    "https://www.itzikbs.com/phd-guide-advisor-hunt",
    "https://www.itzikbs.com/why-i-left-social-media-and-what-brought-me-back"
]

def extract_post_content(url):
    """Fetch and extract content from a WordPress post"""
    try:
        print(f"Fetching: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title - look for the actual post title, not site title
        title_tag = (
            soup.find('h1', class_=lambda x: x and 'entry-title' in str(x)) or
            soup.find('h1', class_=lambda x: x and 'post-title' in str(x)) or
            soup.find('h1', class_=lambda x: x and 'title' in str(x) and 'site' not in str(x).lower()) or
            soup.find('meta', property='og:title')
        )
        
        if title_tag:
            if title_tag.name == 'meta':
                title = title_tag.get('content', url.split('/')[-1].replace('-', ' ').title())
            else:
                title = title_tag.get_text(strip=True)
                # Filter out site titles
                if title in ['Yizhak Ben-Shabat (Itzik), PhD', 'Itzik Ben-Shabat']:
                    # Try to get from page title
                    page_title = soup.find('title')
                    if page_title:
                        title = page_title.get_text(strip=True).split('–')[0].strip()
        else:
            title = url.split('/')[-1].replace('-', ' ').title()
        
        # Extract date
        date_tag = soup.find('time', class_='entry-date') or soup.find('time')
        date = date_tag.get('datetime', '2024-01-01') if date_tag else '2024-01-01'
        
        # Extract main content
        # WordPress with Elementor uses specific structure
        content_div = soup.find('div', class_=lambda x: x and 'elementor-widget-theme-post-content' in str(x))
        
        # Fallback to other selectors
        if not content_div:
            for selector in [
                {'name': 'div', 'class_': 'entry-content'},
                {'name': 'article'},
                {'name': 'div', 'class_': 'post-content'},
                {'name': 'main'},
            ]:
                content_div = soup.find(**selector)
                if content_div:
                    break
        
        if not content_div:
            print(f"  Could not find content div for {url}")
            return None
        
        # For Elementor, get the widget container
        if 'elementor' in str(content_div.get('class', [])):
            content_div = content_div.find('div', class_='elementor-widget-container')
            if not content_div:
                print(f"  Could not find elementor widget container for {url}")
                return None
            
        # Clean up content
        for tag in content_div.find_all(['script', 'style', 'iframe', 'noscript']):
            tag.decompose()
            
        # Remove WordPress-specific elements
        for tag in content_div.find_all(class_=['sharedaddy', 'jp-relatedposts', 'wpcnt']):
            tag.decompose()
            
        # Fix image URLs to be absolute
        for img in content_div.find_all('img'):
            if img.get('src') and not img['src'].startswith('http'):
                img['src'] = 'https://www.itzikbs.com' + img['src']
            # Add loading lazy
            img['loading'] = 'lazy'
                
        # Fix links to be absolute
        for link in content_div.find_all('a'):
            if link.get('href') and not link['href'].startswith('http') and not link['href'].startswith('#'):
                if link['href'].startswith('/'):
                    link['href'] = 'https://www.itzikbs.com' + link['href']
                    
        content_html = str(content_div)
        
        # Generate excerpt from first paragraph
        first_p = content_div.find('p')
        excerpt = ''
        if first_p:
            excerpt_text = first_p.get_text(strip=True)
            if len(excerpt_text) > 200:
                excerpt = excerpt_text[:197] + '...'
            else:
                excerpt = excerpt_text
        
        # Determine category
        categories = ['Research']  # Default
        url_lower = url.lower()
        if any(x in url_lower for x in ['personal', 'guide', 'social', 'pronounce']):
            categories = ['Personal']
        elif any(x in url_lower for x in ['cvpr', 'wacv', 'conference', 'iccv', 'eccv']):
            categories = ['Research', 'Conference']
            
        return {
            'url': url,
            'title': title,
            'date': date.split('T')[0] if 'T' in date else date[:10],
            'excerpt': excerpt,
            'content_html': content_html,
            'categories': categories
        }
        
    except Exception as e:
        print(f"  Error fetching {url}: {e}")
        return None

def create_blog_post_file(post_data):
    """Create an HTML file for a blog post"""
    
    slug = post_data['url'].split('/')[-1]
    if not slug:
        slug = 'post'
        
    filename = f"{post_data['date']}-{slug}.html"
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
                    <time datetime="{post_data['date']}">{post_data['date']}</time>
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
    
    print(f"  Created: {filepath}")
    return filename

def update_blog_index(posts_data):
    """Update the blog index JSON file"""
    
    index_path = Path('data/blog-index.json')
    
    # Load existing index
    with open(index_path, 'r', encoding='utf-8') as f:
        index_data = json.load(f)
    
    existing_ids = {p['id'] for p in index_data['posts']}
    
    # Add new posts
    for post_data, filename in posts_data:
        slug = post_data['url'].split('/')[-1]
        post_id = slug
        
        if post_id not in existing_ids:
            new_entry = {
                "id": post_id,
                "title": post_data['title'],
                "date": post_data['date'],
                "updated": post_data['date'],
                "author": "Itzik Ben-Shabat",
                "excerpt": post_data['excerpt'],
                "content": f"/blog/posts/{filename}",
                "categories": post_data['categories'],
                "tags": []
            }
            index_data['posts'].append(new_entry)
            print(f"  Added to index: {post_data['title']}")
        else:
            # Update existing entry
            for entry in index_data['posts']:
                if entry['id'] == post_id:
                    entry['excerpt'] = post_data['excerpt']
                    entry['content'] = f"/blog/posts/{filename}"
                    entry['categories'] = post_data['categories']
                    print(f"  Updated in index: {post_data['title']}")
                    break
    
    # Sort by date (newest first)
    index_data['posts'].sort(key=lambda x: x['date'], reverse=True)
    
    # Save updated index
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=4, ensure_ascii=False)
    
    print(f"\nUpdated blog-index.json with {len(posts_data)} posts")

def main():
    print("Fetching blog posts from WordPress site...\n")
    
    posts_data = []
    
    for url in PRIORITY_POSTS:
        post_data = extract_post_content(url)
        if post_data:
            filename = create_blog_post_file(post_data)
            posts_data.append((post_data, filename))
            print(f"  ✓ Success\n")
        else:
            print(f"  ✗ Failed\n")
    
    if posts_data:
        update_blog_index(posts_data)
        print(f"\n✓ Successfully processed {len(posts_data)} blog posts")
    else:
        print("\n✗ No posts were successfully fetched")

if __name__ == "__main__":
    main()
