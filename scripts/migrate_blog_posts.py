#!/usr/bin/env python3
"""Migrate blog posts from HTML to Markdown while preserving URLs"""

import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime

def extract_blog_metadata(html_content, filename):
    """Extract metadata from HTML blog post"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract title from h1.blog-hero-title
    title_elem = soup.find('h1', class_='blog-hero-title')
    title = title_elem.get_text().strip() if title_elem else "Untitled"
    
    # Extract date from time element
    time_elem = soup.find('time', class_='blog-hero-date')
    date_str = None
    if time_elem and time_elem.get('datetime'):
        date_str = time_elem.get('datetime')
    
    # If no date in HTML, extract from filename
    if not date_str:
        match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
        if match:
            date_str = match.group(1)
    
    # Extract author (default to Itzik)
    author_elem = soup.find('a', class_='blog-hero-author')
    author = author_elem.get_text().strip() if author_elem else "Itzik Ben-Shabat"
    
    return {
        'title': title,
        'date': date_str,
        'author': author
    }

def extract_blog_content(html_content):
    """Extract main blog content"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the post-content div
    content_div = soup.find('div', class_='post-content')
    if not content_div:
        # Try article.blog-post
        article = soup.find('article', class_='blog-post')
        if article:
            content_div = article.find('div', class_='post-content')
    
    if not content_div:
        print("  ⚠️  Could not find post-content")
        return ""
    
    # Convert HTML to simplified HTML (we'll keep it as HTML for now)
    # Remove jp-relatedposts div if present
    for related in content_div.find_all('div', id='jp-relatedposts'):
        related.decompose()
    
    # Remove elementor wrapper if present
    for elem in content_div.find_all('div', class_=lambda x: x and 'elementor' in x):
        # Unwrap elementor divs but keep content
        elem.unwrap()
    
    return str(content_div)

def html_to_markdown_simple(html):
    """Convert HTML content to Markdown (simplified)"""
    # For now, we'll keep HTML in the markdown files
    # 11ty can render HTML within markdown
    return html

def migrate_post(html_file, output_dir):
    """Migrate a single blog post"""
    filename = html_file.name
    print(f"Migrating: {filename}")
    
    try:
        # Read HTML
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Extract metadata
        metadata = extract_blog_metadata(html_content, filename)
        
        # Extract content
        content = extract_blog_content(html_content)
        
        if not content:
            print(f"  ❌ Failed: No content found")
            return False
        
        # Create markdown filename (same as HTML but .md)
        md_filename = filename.replace('.html', '.md')
        md_filepath = output_dir / md_filename
        
        # Create frontmatter
        frontmatter = f"""---
layout: layouts/blog-post.njk
title: "{metadata['title']}"
date: {metadata['date']}
author: {metadata['author']}
permalink: "/blog/posts/{filename}"
---

"""
        
        # Write markdown file
        with open(md_filepath, 'w', encoding='utf-8') as f:
            f.write(frontmatter)
            f.write(content)
        
        print(f"  ✅ Created: {md_filename}")
        return True
        
    except Exception as e:
        print(f"  ❌ Error: {str(e)}")
        return False

def main():
    # Paths
    posts_dir = Path('blog/posts')
    output_dir = Path('blog/posts-md')
    
    # Create output directory
    output_dir.mkdir(exist_ok=True)
    
    # Get all HTML files
    html_files = sorted(posts_dir.glob('*.html'))
    
    print(f"Found {len(html_files)} blog posts to migrate\n")
    
    success_count = 0
    fail_count = 0
    
    for html_file in html_files:
        if migrate_post(html_file, output_dir):
            success_count += 1
        else:
            fail_count += 1
        print()
    
    print(f"\n{'='*50}")
    print(f"Migration Complete!")
    print(f"✅ Success: {success_count}")
    print(f"❌ Failed: {fail_count}")
    print(f"{'='*50}")

if __name__ == '__main__':
    main()
