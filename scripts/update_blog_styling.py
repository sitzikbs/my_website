#!/usr/bin/env python3
"""
Update blog post HTML files with proper styling and relative paths
"""

from pathlib import Path
import re

def update_blog_post_html(filepath):
    """Update a blog post HTML file with proper styling"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title and date from existing content
    title_match = re.search(r'<h1>(.*?)</h1>', content, re.DOTALL)
    title = title_match.group(1).strip() if title_match else "Blog Post"
    
    date_match = re.search(r'<time datetime="([^"]+)">', content)
    date = date_match.group(1) if date_match else "2024-01-01"
    
    # Extract the post content (everything in post-content div)
    content_match = re.search(r'<div class="post-content">(.*?)</div>\s*</article>', content, re.DOTALL)
    if not content_match:
        print(f"Could not find post content in {filepath}")
        return False
    
    post_content = content_match.group(1).strip()
    
    # New HTML template with updated styling
    new_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Itzik Ben-Shabat</title>
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
                <h1>{title}</h1>
                <div class="post-meta">
                    <time datetime="{date}">{date}</time>
                    <span class="author">By Itzik Ben-Shabat</span>
                </div>
            </header>
            <div class="post-content">
                {post_content}
            </div>
        </article>
    </main>
    <script src="../../js/main.js"></script>
</body>
</html>"""
    
    # Write updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    print(f"Updated: {filepath.name}")
    return True

def main():
    posts_dir = Path('blog/posts')
    
    # Update all 2024-01-01 prefixed files (the ones we fetched)
    updated = 0
    for filepath in posts_dir.glob('2024-01-01-*.html'):
        if update_blog_post_html(filepath):
            updated += 1
    
    print(f"\n✓ Updated {updated} blog posts with proper styling")

if __name__ == "__main__":
    main()
