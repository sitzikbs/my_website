#!/usr/bin/env python3
"""
Update blog hero CSS styles in all blog posts.
"""

import re
from pathlib import Path

def update_hero_styles(html_path: Path) -> bool:
    """Update hero header CSS in a blog post."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if hero styles exist
    if '.blog-hero {' not in content:
        return False
    
    # Updated CSS with larger avatar and reduced bottom margin
    new_css = '''        /* Hero Header Styles */
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
    
    # Replace the hero styles section
    pattern = r'        /\* Hero Header Styles \*/.*?        \n'
    if not re.search(pattern, content, re.DOTALL):
        return False
    
    content = re.sub(pattern, new_css, content, flags=re.DOTALL, count=1)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Process all blog posts."""
    print("Updating blog hero CSS styles...")
    
    blog_dir = Path("blog/posts")
    modified_count = 0
    
    for html_path in blog_dir.glob("*.html"):
        if update_hero_styles(html_path):
            print(f"  ✓ {html_path.name}")
            modified_count += 1
    
    print(f"\n✅ Updated CSS in {modified_count} blog posts")

if __name__ == "__main__":
    main()
