#!/usr/bin/env python3
"""
Generate sitemap.xml for the website
"""

import os
from datetime import datetime
from pathlib import Path
import subprocess

BASE_URL = "https://itzikbs.com"
OUTPUT_FILE = "sitemap.xml"

# Page priorities
PRIORITIES = {
    "index.html": "1.0",
    "publications.html": "0.8",
    "blog.html": "0.8",
    "about.html": "0.8",
    "podcast.html": "0.8",
    "code.html": "0.7",
    "contact.html": "0.7",
}

def get_html_files():
    """Get all HTML files in the project"""
    html_files = []
    
    # Root HTML files
    for file in Path(".").glob("*.html"):
        if not file.name.startswith('.'):
            html_files.append(str(file))
    
    # Blog posts
    blog_posts_dir = Path("blog/posts")
    if blog_posts_dir.exists():
        for file in blog_posts_dir.glob("*.html"):
            html_files.append(str(file))
    
    return html_files

def get_last_modified(file_path):
    """Get last modified date of file from git or filesystem"""
    try:
        # Try to get last commit date from git
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%cI', file_path],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0 and result.stdout.strip():
            # Parse ISO format and return just the date
            date_str = result.stdout.strip()
            return date_str.split('T')[0]
    except Exception:
        pass
    
    # Fallback to file modification time
    return datetime.fromtimestamp(
        os.path.getmtime(file_path)
    ).strftime("%Y-%m-%d")

def generate_sitemap():
    """Generate sitemap.xml"""
    files = get_html_files()
    
    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    for file in sorted(files):
        url = f"{BASE_URL}/{file}"
        lastmod = get_last_modified(file)
        priority = PRIORITIES.get(file, "0.5")
        
        # Blog posts get priority 0.6
        if "blog/posts/" in file:
            priority = "0.6"
        
        xml.append("  <url>")
        xml.append(f"    <loc>{url}</loc>")
        xml.append(f"    <lastmod>{lastmod}</lastmod>")
        xml.append(f"    <priority>{priority}</priority>")
        xml.append("  </url>")
    
    xml.append("</urlset>")
    
    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(xml))
    
    print(f"✅ Sitemap generated: {OUTPUT_FILE}")
    print(f"📊 Total URLs: {len(files)}")
    print(f"\nSitemap includes:")
    
    # Count by category
    root_pages = [f for f in files if "/" not in f]
    blog_posts = [f for f in files if "blog/posts/" in f]
    
    print(f"  - {len(root_pages)} root pages")
    print(f"  - {len(blog_posts)} blog posts")

if __name__ == "__main__":
    generate_sitemap()
