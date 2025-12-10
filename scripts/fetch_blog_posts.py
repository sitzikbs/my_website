import json
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# List of posts to fetch
posts_to_fetch = [
    {
        "title": "Highlights and Insights from CVPR 2024",
        "url": "https://www.itzikbs.com/cvpr2024",
        "date": "2024-06-18",
        "categories": ["Research", "Conference"]
    },
    {
        "title": "Personal update! I will be joining...",
        "url": "https://www.itzikbs.com/career_update_2024",
        "date": "2024-06-16",
        "categories": ["Personal", "Career"]
    },
    {
        "title": "WACV 2024 : Waikoloa Hawaii",
        "url": "https://www.itzikbs.com/wacv2024",
        "date": "2024-01-10",
        "categories": ["Research", "Conference"]
    },
    {
        "title": "CVPR 2023",
        "url": "https://www.itzikbs.com/cvpr-2023",
        "date": "2023-06-18",
        "categories": ["Research", "Conference"]
    },
    {
        "title": "CVPR 2022",
        "url": "https://www.itzikbs.com/cvpr-2022",
        "date": "2022-06-20",
        "categories": ["Research", "Conference"]
    }
]

def fetch_and_save_posts():
    blog_index_path = 'data/blog-index.json'
    with open(blog_index_path, 'r') as f:
        index_data = json.load(f)
    
    existing_ids = [p['id'] for p in index_data['posts']]
    
    for post_info in posts_to_fetch:
        print(f"Processing: {post_info['title']}")
        
        # Generate ID and filename
        slug = post_info['url'].split('/')[-1]
        if not slug: slug = "post"
        post_id = slug
        filename = f"{post_info['date']}-{slug}.html"
        filepath = f"blog/posts/{filename}"
        
        # Fetch content
        try:
            response = requests.get(post_info['url'])
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Try to find the main content
                # Adjust selector based on typical WordPress structure
                content_div = soup.find('div', class_='entry-content')
                if not content_div:
                    content_div = soup.find('article')
                
                if content_div:
                    # Clean up content
                    for tag in content_div.find_all(['script', 'style', 'iframe']):
                        tag.decompose()
                    
                    # Fix images to be absolute or download them (skipping download for now, using absolute)
                    for img in content_div.find_all('img'):
                        if img.get('src') and not img['src'].startswith('http'):
                            img['src'] = 'https://www.itzikbs.com' + img['src']
                            
                    content_html = str(content_div)
                    
                    # Create HTML file
                    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{post_info['title']} - Itzik Ben-Shabat</title>
    <link rel="stylesheet" href="/css/base.css">
    <link rel="stylesheet" href="/css/layout.css">
    <link rel="stylesheet" href="/css/components.css">
    <link rel="stylesheet" href="/css/responsive.css">
    <style>
        .blog-post {{ max-width: 800px; margin: 0 auto; padding: 2rem; }}
        .post-header {{ margin-bottom: 2rem; border-bottom: 1px solid #eee; padding-bottom: 1rem; }}
        .post-content img {{ max-width: 100%; height: auto; margin: 1rem 0; }}
        .post-content p {{ margin-bottom: 1rem; }}
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="nav-brand">
                <a href="/index.html">Itzik Ben-Shabat</a>
            </div>
            <ul class="nav-menu">
                <li><a href="/index.html">Home</a></li>
                <li><a href="/publications.html">Publications</a></li>
                <li><a href="/blog.html">Blog</a></li>
                <li><a href="/contact.html">Contact</a></li>
            </ul>
        </div>
    </nav>
    <main>
        <article class="blog-post">
            <header class="post-header">
                <h1>{post_info['title']}</h1>
                <div class="post-meta">
                    <time datetime="{post_info['date']}">{post_info['date']}</time>
                    <span class="author">By Itzik Ben-Shabat</span>
                </div>
            </header>
            <div class="post-content">
                {content_html}
            </div>
        </article>
    </main>
</body>
</html>"""
                    
                    with open(filepath, 'w') as f:
                        f.write(full_html)
                    
                    # Generate excerpt
                    excerpt = content_div.get_text()[:150] + "..."
                    
                    # Add to index if not exists
                    if post_id not in existing_ids:
                        new_entry = {
                            "id": post_id,
                            "title": post_info['title'],
                            "date": post_info['date'],
                            "updated": post_info['date'],
                            "author": "Itzik Ben-Shabat",
                            "excerpt": excerpt.strip(),
                            "content": f"/blog/posts/{filename}",
                            "categories": post_info['categories'],
                            "tags": []
                        }
                        index_data['posts'].append(new_entry)
                        existing_ids.append(post_id)
                        print(f"Added to index: {post_info['title']}")
                    else:
                        print(f"Updated content for: {post_info['title']}")
                        
                else:
                    print(f"Could not find content for {post_info['title']}")
            else:
                print(f"Failed to fetch {post_info['url']}")
        except Exception as e:
            print(f"Error processing {post_info['title']}: {e}")

    # Sort posts by date
    index_data['posts'].sort(key=lambda x: x['date'], reverse=True)
    
    with open(blog_index_path, 'w') as f:
        json.dump(index_data, f, indent=4)
    print("Updated blog-index.json")

if __name__ == "__main__":
    fetch_and_save_posts()
