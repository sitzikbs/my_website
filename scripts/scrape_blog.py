import requests
from bs4 import BeautifulSoup
import json
import re
import os
from datetime import datetime

def scrape_blog():
    url = "https://www.itzikbs.com/"
    print(f"Fetching {url}...")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch page: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find "Recent Posts" section
    recent_posts_header = soup.find(lambda tag: tag.name in ['h1', 'h2', 'h3'] and "Recent Posts" in tag.text)
    
    if not recent_posts_header:
        print("Could not find 'Recent Posts' header.")
        return

    # The posts are likely in the section following the header
    header_section = recent_posts_header.find_parent('section')
    if not header_section:
        header_section = recent_posts_header.find_parent(class_='elementor-section')
        
    if not header_section:
        print("Could not find section for Recent Posts.")
        return

    # Get subsequent sections or columns?
    # Based on previous experience, it might be in the same section or next ones.
    # Let's look for links inside the section or following sections.
    
    # Actually, looking at the fetch_webpage output for home page:
    # ## Recent Posts
    # ### [Title](url)
    # Date
    # Excerpt...
    
    # So they seem to be in h3 tags with links.
    
    posts = []
    
    # Find all h3 tags with links that are after the header
    # Or just search in the whole page but filter by location?
    # Let's search in the siblings of the header's container.
    
    # Let's try to find all 'article' tags or similar if they exist.
    # Or just look for h3 tags with links.
    
    all_h3s = soup.find_all('h3')
    for h3 in all_h3s:
        link = h3.find('a')
        if not link:
            continue
            
        title = link.get_text(strip=True)
        post_url = link.get('href')
        
        # Check if this is likely a blog post
        # The URL usually contains the slug
        if "itzikbs.com" not in post_url and not post_url.startswith('/'):
            continue
            
        # Skip "KEEP IN TOUCH" or other widgets
        if "KEEP IN TOUCH" in title:
            continue
            
        print(f"Found post: {title}")
        
        # Fetch the post content
        print(f"Fetching post content from {post_url}...")
        post_response = requests.get(post_url)
        if post_response.status_code != 200:
            print(f"Failed to fetch post: {post_response.status_code}")
            continue
            
        post_soup = BeautifulSoup(post_response.content, 'html.parser')
        
        # Extract content
        # Usually in 'entry-content' or 'elementor-widget-text-editor'
        content_div = post_soup.find('div', class_='entry-content')
        if not content_div:
            # Try elementor section
            content_div = post_soup.find('div', class_='elementor-section-wrap')
            
        if content_div:
            # Remove scripts, styles
            for script in content_div(["script", "style"]):
                script.decompose()
            content_html = str(content_div)
        else:
            content_html = "<p>Could not extract content.</p>"
            
        # Extract Date
        # Look for date in the post page or the home page snippet
        # On home page snippet, date was under the title.
        # On post page, usually meta tag or time tag.
        date_str = "2025-01-01" # Default
        
        time_tag = post_soup.find('time')
        if time_tag:
            if time_tag.has_attr('datetime'):
                date_str = time_tag['datetime'].split('T')[0]
            else:
                # Parse text like "October 14, 2025"
                try:
                    date_obj = datetime.strptime(time_tag.get_text(strip=True), "%B %d, %Y")
                    date_str = date_obj.strftime("%Y-%m-%d")
                except:
                    pass
        
        # Generate slug
        slug = post_url.strip('/').split('/')[-1]
        if not slug:
            slug = "post-" + date_str
            
        filename = f"{date_str}-{slug}.html"
        filepath = os.path.join('blog/posts', filename)
        
        # Save HTML content
        with open(filepath, 'w') as f:
            f.write(content_html)
            
        posts.append({
            "id": slug,
            "title": title,
            "date": date_str,
            "updated": date_str,
            "author": "Itzik Ben-Shabat",
            "excerpt": "", # Could extract from home page or first paragraph
            "content": f"/blog/posts/{filename}",
            "categories": [],
            "tags": []
        })

    # Update blog-index.json
    index_path = 'data/blog-index.json'
    if os.path.exists(index_path):
        with open(index_path, 'r') as f:
            data = json.load(f)
    else:
        data = {"posts": []}
        
    # Merge posts (avoid duplicates by id)
    existing_ids = {p['id'] for p in data['posts']}
    for post in posts:
        if post['id'] not in existing_ids:
            data['posts'].insert(0, post) # Add new posts at the beginning
            
    with open(index_path, 'w') as f:
        json.dump(data, f, indent=4)
        
    print(f"Saved {len(posts)} posts to {index_path}")

if __name__ == "__main__":
    scrape_blog()
