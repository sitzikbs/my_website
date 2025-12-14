#!/usr/bin/env python3
"""
Add centered hero header with portrait/logo to blog posts.
Similar to Vincent Sitzmann's blog design.
"""

import json
import re
from pathlib import Path
from typing import Dict, List

# Talking Papers podcast logo
PODCAST_LOGO = "../../assets/images/publications/Talking_papers_cover-400.webp"
# Author portrait
AUTHOR_PORTRAIT = "../../assets/images/profile/Itzik_Ben_Shabat_portrait.jpg"
AUTHOR_NAME = "Itzik Ben-Shabat"

def load_blog_index() -> Dict:
    """Load blog index to get post metadata."""
    blog_index_path = Path("data/blog-index.json")
    with open(blog_index_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def is_talking_papers(categories: List[str]) -> bool:
    """Check if post is a Talking Papers episode."""
    return "Talking Papers Podcast" in categories

def add_hero_header(html_path: Path, post_data: Dict) -> bool:
    """
    Add hero header to a blog post.
    
    Returns True if modified, False otherwise.
    """
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if hero header already exists
    if 'class="blog-hero"' in content:
        return False
    
    # Determine which image to use
    is_podcast = is_talking_papers(post_data.get('categories', []))
    image_src = PODCAST_LOGO if is_podcast else AUTHOR_PORTRAIT
    image_alt = "Talking Papers Podcast Logo" if is_podcast else AUTHOR_NAME
    
    # Extract the title and date
    title = post_data.get('title', 'Blog Post')
    date = post_data.get('date', '')
    
    # Format date nicely
    if date:
        from datetime import datetime
        try:
            date_obj = datetime.strptime(date, '%Y-%m-%d')
            formatted_date = date_obj.strftime('%B %d, %Y')
        except:
            formatted_date = date
    else:
        formatted_date = ''
    
    # Create hero header HTML
    hero_html = f'''  <div class="blog-hero">
    <div class="blog-hero-content">
      <img src="{image_src}" alt="{image_alt}" class="blog-hero-avatar">
      <div class="blog-hero-byline">
        <a href="../../index.html" class="blog-hero-author">{AUTHOR_NAME}</a>
        <time class="blog-hero-date" datetime="{date}">{formatted_date}</time>
      </div>
      <h1 class="blog-hero-title">{title}</h1>
    </div>
  </div>
  
'''
    
    # Find where to insert the hero header
    # Look for <article class="blog-post"> tag
    article_pattern = r'(<article class="blog-post">)\s*'
    
    if not re.search(article_pattern, content):
        print(f"  ⚠️  Could not find <article class=\"blog-post\"> in {html_path.name}")
        return False
    
    # Insert hero header right after the opening article tag
    content = re.sub(article_pattern, r'\1\n' + hero_html, content, count=1)
    modified = True
    
    if not modified:
        print(f"  ⚠️  Could not find insertion point in {html_path.name}")
        return False
    
    # Remove old post-header if it exists (we're replacing it with hero)
    old_header_pattern = r'\s*<header class="post-header">.*?</header>\s*'
    if re.search(old_header_pattern, content, re.DOTALL):
        content = re.sub(old_header_pattern, '\n', content, flags=re.DOTALL, count=1)
    
    # Write back
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def add_hero_styles(html_path: Path) -> bool:
    """Add CSS styles for hero header to a blog post."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if styles already exist
    if '.blog-hero' in content:
        return False
    
    # Find the style tag
    style_pattern = r'(<style>)'
    if not re.search(style_pattern, content):
        print(f"  ⚠️  No <style> tag found in {html_path.name}")
        return False
    
    hero_styles = '''<style>
        /* Hero Header Styles */
        .blog-hero {
            max-width: 900px;
            margin: 3rem auto 1.5rem;
            padding: 0 1.5rem;
            text-align: center;
        }
        
        .blog-hero-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 1rem;
        }
        
        .blog-hero-avatar {
            width: 96px;
            height: 96px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid var(--border-color);
        }
        
        .blog-hero-byline {
            display: flex;
            flex-direction: column;
            gap: 0.25rem;
            font-size: 0.95rem;
            color: var(--text-light);
        }
        
        .blog-hero-author {
            color: var(--primary-color);
            text-decoration: none;
            font-weight: 500;
        }
        
        .blog-hero-author:hover {
            text-decoration: underline;
        }
        
        .blog-hero-date {
            font-size: 0.9rem;
        }
        
        .blog-hero-title {
            font-size: 2.5rem;
            margin: 1rem 0 0 0;
            color: var(--primary-color);
            line-height: 1.2;
            max-width: 800px;
        }
        
        @media (max-width: 768px) {
            .blog-hero {
                margin: 2rem auto 1rem;
            }
            
            .blog-hero-avatar {
                width: 77px;
                height: 77px;
            }
            
            .blog-hero-title {
                font-size: 1.75rem;
            }
        }
        
'''
    
    # Insert hero styles at the beginning of the style tag
    content = re.sub(style_pattern, hero_styles, content)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Process all blog posts."""
    print("Adding hero headers to blog posts...")
    
    # Load blog index
    blog_index = load_blog_index()
    posts = blog_index.get('posts', [])
    
    blog_dir = Path("blog/posts")
    
    modified_count = 0
    total_count = 0
    
    for post in posts:
        # Get the HTML file path from the content field
        content_path = post.get('content', '')
        if not content_path:
            continue
        
        # Convert to actual file path
        html_path = Path(content_path.lstrip('/'))
        
        if not html_path.exists():
            print(f"  ⚠️  File not found: {html_path}")
            continue
        
        total_count += 1
        
        # Add hero header first
        header_added = add_hero_header(html_path, post)
        
        # Then add styles if header was added
        styles_added = False
        if header_added:
            styles_added = add_hero_styles(html_path)
        
        if styles_added or header_added:
            is_podcast = is_talking_papers(post.get('categories', []))
            icon = "🎙️" if is_podcast else "✍️"
            print(f"  {icon} {html_path.name}")
            modified_count += 1
    
    print(f"\n✅ Modified {modified_count}/{total_count} blog posts")

if __name__ == "__main__":
    main()
