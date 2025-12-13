import os
import json

def wrap_blog_posts():
    index_path = 'data/blog-index.json'
    if not os.path.exists(index_path):
        print("No blog index found.")
        return
        
    with open(index_path, 'r') as f:
        data = json.load(f)
        
    template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Itzik Ben-Shabat</title>
    <link rel="stylesheet" href="/css/base.css">
    <link rel="stylesheet" href="/css/layout.css">
    <link rel="stylesheet" href="/css/components.css">
    <link rel="stylesheet" href="/css/responsive.css">
    <style>
        .blog-post {{ max-width: 800px; margin: 0 auto; padding: 2rem; }}
        .post-header {{ margin-bottom: 2rem; border-bottom: 1px solid #eee; padding-bottom: 1rem; }}
        .post-content img {{ max-width: 100%; height: auto; }}
    </style>
</head>
<body>
    <nav class="main-nav">
        <div class="container">
            <a href="/" class="logo">Itzik Ben-Shabat</a>
            <ul class="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/publications.html">Publications</a></li>
                <li><a href="/blog/index.html">Blog</a></li>
            </ul>
        </div>
    </nav>
    <main>
        <article class="blog-post">
            <header class="post-header">
                <h1>{title}</h1>
                <div class="post-meta">
                    <time datetime="{date}">{date}</time>
                    <span class="author">By {author}</span>
                </div>
            </header>
            <div class="post-content">
                {content}
            </div>
        </article>
    </main>
</body>
</html>"""

    for post in data['posts']:
        # Check if it's one of the new posts (starts with 2025 or 2024-07)
        # Or just check if the file content doesn't start with <!DOCTYPE html>
        
        # The path in json is /blog/posts/..., we need relative path
        rel_path = post['content'].lstrip('/')
        if not os.path.exists(rel_path):
            print(f"File not found: {rel_path}")
            continue
            
        with open(rel_path, 'r') as f:
            content = f.read()
            
        if content.strip().startswith('<!DOCTYPE html>'):
            print(f"Skipping {rel_path} (already formatted)")
            continue
            
        print(f"Wrapping {rel_path}...")
        wrapped_content = template.format(
            title=post['title'],
            date=post['date'],
            author=post['author'],
            content=content
        )
        
        with open(rel_path, 'w') as f:
            f.write(wrapped_content)

if __name__ == "__main__":
    wrap_blog_posts()
