# Blog Directory

This directory contains all blog posts and the blog index page.

## Structure

```
blog/
├── index.html           # Blog listing page (to be created)
└── posts/              # Individual blog post files
    ├── 2024-11-15-example-blog-post.html
    ├── 2024-10-20-another-example-post.html
    └── [more posts...]
```

## Blog Post Format

### File Naming Convention

All blog posts should follow this naming pattern:
```
YYYY-MM-DD-post-slug.html
```

Examples:
- `2024-03-15-my-first-post.html`
- `2024-12-20-understanding-point-clouds.html`
- `2023-08-10-conference-report.html`

### Blog Post Template

Each blog post should use this HTML structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Post excerpt/description">
    <meta name="keywords" content="tag1, tag2, tag3">
    <meta name="author" content="Itzik Ben-Shabat">
    <meta property="og:title" content="Post Title">
    <meta property="og:description" content="Post description">
    <meta property="og:type" content="article">
    <meta property="article:published_time" content="YYYY-MM-DD">
    <title>Post Title - Itzik Ben-Shabat</title>
</head>
<body>
    <article class="blog-post">
        <header class="post-header">
            <h1>Post Title</h1>
            <div class="post-meta">
                <time datetime="YYYY-MM-DD">Month DD, YYYY</time>
                <span class="reading-time">X min read</span>
            </div>
            <div class="post-categories">
                <span class="category">Category 1</span>
            </div>
            <div class="post-tags">
                <span class="tag">#tag1</span>
                <span class="tag">#tag2</span>
            </div>
        </header>
        
        <div class="featured-image">
            <img src="/assets/images/blog/YYYY-MM-DD-slug-featured.jpg" 
                 alt="Descriptive alt text"
                 loading="lazy">
        </div>
        
        <div class="post-content">
            <!-- Main content here -->
        </div>
        
        <footer class="post-footer">
            <!-- Navigation, sharing, etc. -->
        </footer>
    </article>
</body>
</html>
```

## Blog Index

The `data/blog-index.json` file contains metadata for all posts. When adding a new post:

1. Create the HTML file in `posts/`
2. Update `data/blog-index.json` with post metadata
3. The blog index page will automatically list the new post

## Content Elements

Blog posts can include:

### Text Formatting
- Headings (h2, h3 for sections and subsections)
- Paragraphs
- **Bold** and *italic* text
- Blockquotes
- Lists (ordered and unordered)

### Code Blocks
```html
<pre><code class="language-python">
def example():
    print("Code here")
</code></pre>
```

### Images
```html
<figure>
    <img src="/assets/images/blog/image.jpg" 
         alt="Description"
         loading="lazy">
    <figcaption>Image caption</figcaption>
</figure>
```

### Links
```html
<a href="https://example.com" target="_blank" rel="noopener noreferrer">
    External Link
</a>

<a href="/publications/">Internal Link</a>
```

### Tables
```html
<table>
    <thead>
        <tr>
            <th>Header 1</th>
            <th>Header 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Data 1</td>
            <td>Data 2</td>
        </tr>
    </tbody>
</table>
```

## WordPress Migration

### Export Blog Posts

1. **Using WordPress Export Tool:**
   - Go to Tools → Export in WordPress admin
   - Select "Posts"
   - Download XML file
   - Use converter tool to transform to HTML

2. **Using WP-CLI:**
   ```bash
   wp post list --post_type=post --format=json > posts.json
   wp export --post_type=post
   ```

### Convert Posts

For each WordPress post:

1. **Create HTML file** following naming convention
2. **Copy template** from example post
3. **Replace content:**
   - Update title and meta tags
   - Copy post content
   - Update image paths
   - Convert WordPress shortcodes to HTML
   - Fix internal links

4. **Update blog-index.json:**
   - Add post metadata entry
   - Update categories and tags

5. **Add images:**
   - Download featured image
   - Download inline images
   - Save to `assets/images/blog/`
   - Update image paths in HTML

### Content Conversion Checklist

For each post, ensure:
- [ ] Title and meta tags updated
- [ ] Publication date correct
- [ ] Categories and tags added
- [ ] Featured image downloaded and referenced
- [ ] All inline images downloaded
- [ ] Image paths updated
- [ ] Code blocks properly formatted
- [ ] Links verified (internal and external)
- [ ] WordPress shortcodes converted
- [ ] Entry added to blog-index.json

## Categories and Tags

Organize posts with consistent categories and tags:

### Suggested Categories
- Tutorial
- Research
- Conference Report
- Project Update
- Technical Deep Dive
- Opinion

### Tagging Guidelines
- Use lowercase
- Use hyphens for multi-word tags (e.g., `computer-vision`)
- Be specific but not too narrow
- Aim for 3-5 tags per post
- Reuse existing tags when possible

## Current Status

- ✅ Blog directory structure created
- ✅ Example blog posts provided
- ✅ Template structure defined
- ⏳ **Awaiting WordPress blog post migration**

## Next Steps

1. Export all blog posts from WordPress
2. Convert each post to HTML format
3. Download all blog images
4. Update blog-index.json with all posts
5. Create blog/index.html page to list all posts
6. Test all posts display correctly

See [MIGRATION_GUIDE.md](../MIGRATION_GUIDE.md) for detailed migration instructions.
