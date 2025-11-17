# Content Management Guide

This guide explains how to add and update content on your website without needing any special tools or WordPress.

## Quick Reference

- **Add Publications:** Edit `data/publications.json`
- **Add Blog Posts:** Create HTML file + update `data/blog.json`
- **Update News:** Edit `data/news.json`
- **Update Bio/About:** Edit `index.html`
- **Update Contact Info:** Edit `contact.html` and footer in all HTML files

---

## Adding Publications

Publications are managed through `data/publications.json`. This file contains an array of publication objects.

### Step 1: Edit the JSON file

Open `data/publications.json` and add your publication:

```json
{
  "title": "Your Paper Title Here",
  "authors": "First Author, Second Author, Third Author",
  "venue": "Conference Name (Acronym) or Journal Name",
  "year": "2024",
  "abstract": "A brief description or abstract of your paper (optional)",
  "links": {
    "paper": "https://arxiv.org/pdf/your-paper.pdf",
    "code": "https://github.com/username/repo",
    "project": "https://yourproject.com",
    "video": "https://youtube.com/watch?v=...",
    "slides": "https://slides.com/your-slides"
  }
}
```

### Tips:
- Add publications in reverse chronological order (newest first)
- All fields except `links` are required
- You can omit any link that doesn't exist
- Use real URLs for links (no placeholders)

### Example:

```json
[
  {
    "title": "Neural 3D Reconstruction with Deep Learning",
    "authors": "Jane Smith, John Doe, Alice Johnson",
    "venue": "CVPR 2024",
    "year": "2024",
    "abstract": "We present a novel approach to 3D reconstruction using deep neural networks...",
    "links": {
      "paper": "https://arxiv.org/pdf/2401.12345.pdf",
      "code": "https://github.com/username/neural-3d",
      "project": "https://neural3d.github.io"
    }
  }
]
```

---

## Adding Blog Posts

Adding a blog post is a two-step process:

### Step 1: Create the HTML file

1. Copy `blog/blog-post-template.html`
2. Rename it with a URL-friendly name (e.g., `my-new-post.html`)
3. Edit the content:
   - Replace `[Your Blog Post Title]` with your title
   - Replace `[Month Day, Year]` with the publication date
   - Replace `[Brief description]` in the meta tag
   - Fill in your content

**Example filename:** `understanding-transformers.html`

### Step 2: Add metadata to blog.json

Open `data/blog.json` and add an entry:

```json
{
  "title": "Understanding Transformers",
  "slug": "understanding-transformers",
  "date": "December 1, 2024",
  "excerpt": "A comprehensive guide to transformer architecture and its applications.",
  "image": "images/blog/transformers.jpg"
}
```

**Notes:**
- The `slug` must match your HTML filename (without .html)
- Add entries at the top for newest posts
- `image` is optional (leave empty string if no image)
- Place blog images in `images/blog/` folder

### Blog Post Writing Tips:

**Use headings for structure:**
```html
<h2>Main Section</h2>
<h3>Subsection</h3>
```

**Add code blocks:**
```html
<pre><code>def hello_world():
    print("Hello, World!")
</code></pre>
```

**Add inline code:**
```html
Use <code>inline code</code> for variables
```

**Add images:**
```html
<img src="../images/blog/my-image.jpg" alt="Description" style="max-width: 100%; height: auto;">
```

**Add lists:**
```html
<ul>
  <li>Point one</li>
  <li>Point two</li>
</ul>
```

---

## Updating News

Edit `data/news.json` to add news items:

```json
[
  {
    "date": "December 2024",
    "content": "New paper accepted at ICCV 2025"
  },
  {
    "date": "November 2024",
    "content": "Gave invited talk at MIT"
  }
]
```

**Tips:**
- Add newest items first
- Only the 5 most recent items display on homepage
- Keep descriptions concise
- Date format is flexible (be consistent)

---

## Updating Personal Information

### Homepage Bio

Edit `index.html`:

**Update name and title:**
```html
<h1>Your Name</h1>
<p class="subtitle">Your Title • Your Role • Your Field</p>
```

**Update bio text:**
```html
<div class="about-content">
    <p>Your bio paragraph here...</p>
    <p>Additional information...</p>
</div>
```

**Update research interests:**
```html
<ul class="interests-list">
    <li>Research Area 1</li>
    <li>Research Area 2</li>
    <li>Research Area 3</li>
    <li>Research Area 4</li>
</ul>
```

### Contact Information

Edit `contact.html`:

**Update email:**
```html
<p><a href="mailto:your.real.email@university.edu">your.real.email@university.edu</a></p>
```

**Update location:**
```html
<p>Department Name<br>
University Name<br>
City, State, Country</p>
```

### Social Media Links

Update in **all HTML files** (look for the footer section):

```html
<div class="social-links">
    <a href="mailto:your.email@domain.com" aria-label="Email">
        <i class="fas fa-envelope"></i>
    </a>
    <a href="https://scholar.google.com/citations?user=YOUR_ID" aria-label="Google Scholar">
        <i class="fas fa-graduation-cap"></i>
    </a>
    <a href="https://github.com/yourusername" aria-label="GitHub">
        <i class="fab fa-github"></i>
    </a>
    <a href="https://linkedin.com/in/yourprofile" aria-label="LinkedIn">
        <i class="fab fa-linkedin"></i>
    </a>
    <a href="https://twitter.com/yourusername" aria-label="Twitter">
        <i class="fab fa-twitter"></i>
    </a>
</div>
```

**Pro tip:** Use find-and-replace to update social links in all files at once.

---

## Adding Images

### Profile Picture

1. Save your photo as `images/profile.jpg`
2. Recommended size: 400x400px or larger (square)
3. It will automatically appear on homepage

### Blog Images

1. Create folder: `images/blog/` (if it doesn't exist)
2. Save images with descriptive names: `my-topic-image.jpg`
3. Reference in blog posts: `../images/blog/my-topic-image.jpg`
4. Optimize images before uploading (compress to reduce file size)

### Publication Images

1. Save in `images/publications/`
2. To display in publications, edit `js/publications-loader.js` to include image field

---

## Customizing Styles

### Changing Colors

Edit `css/style.css` and modify the color variables at the top:

```css
:root {
    --primary-color: #2c3e50;      /* Main dark color */
    --secondary-color: #3498db;     /* Accent/link color */
    --text-color: #333;             /* Body text */
    --text-light: #666;             /* Secondary text */
    --bg-color: #ffffff;            /* Background */
    --bg-light: #f8f9fa;           /* Alternate background */
}
```

### Changing Fonts

Add to `css/style.css`:

```css
body {
    font-family: 'Your Font', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
```

If using Google Fonts, add to `<head>` in all HTML files:

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Your+Font&display=swap">
```

---

## Testing Your Changes

### Test Locally

Before deploying, test your changes:

1. **Start local server:**
   ```bash
   # Python 3
   python -m http.server 8000
   
   # Python 2
   python -m SimpleHTTPServer 8000
   
   # Node.js (if you have it)
   npx http-server
   ```

2. **Open in browser:** http://localhost:8000

3. **Test everything:**
   - Click all navigation links
   - Check all pages load
   - Verify your new content appears
   - Test on mobile (resize browser window)
   - Check console for errors (F12)

### Common Issues

**JSON errors:**
- Make sure commas are correct between items
- Last item in array shouldn't have comma after it
- All quotes must be double quotes `"`
- Validate JSON at https://jsonlint.com

**Images not loading:**
- Check file path is correct
- Check file extension matches (.jpg vs .JPG)
- Ensure image file exists in the right folder

**Content not updating:**
- Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Check JSON syntax is valid
- Look for JavaScript errors in console (F12)

---

## Publishing Changes

### If using Git/GitHub:

```bash
# Stage changes
git add .

# Commit with message
git commit -m "Add new publication / blog post / etc"

# Push to GitHub
git push
```

If using GitHub Pages, Netlify, or Vercel, your site will update automatically!

### If using traditional hosting:

1. Upload changed files via FTP/SFTP
2. Only upload files you modified
3. Clear CDN cache if applicable

---

## Content Best Practices

### Writing Tips

- **Keep it simple:** Clear, concise language
- **Use headings:** Break up content into sections
- **Add images:** Visual content is engaging
- **Be consistent:** Use same format for dates, titles, etc.
- **Proofread:** Check for typos and errors

### SEO Tips

- **Title tags:** Make descriptive and unique for each page
- **Meta descriptions:** Summarize page content
- **Alt text:** Describe images for accessibility
- **Internal links:** Link between related pages
- **Update regularly:** Fresh content helps rankings

### Accessibility

- Use descriptive link text (not "click here")
- Add alt text to all images
- Use proper heading hierarchy (h1 → h2 → h3)
- Ensure good color contrast
- Test with keyboard navigation

---

## Need Help?

**Common tasks:**
- Publication not showing? Check JSON syntax
- Blog post not appearing? Verify slug matches filename
- Changes not visible? Clear browser cache
- Page broken? Check browser console for errors

**Validation tools:**
- JSON: https://jsonlint.com
- HTML: https://validator.w3.org
- Links: https://validator.w3.org/checklink

**File structure:**
```
my_website/
├── index.html (homepage)
├── publications.html
├── blog.html
├── contact.html
├── css/
│   └── style.css
├── js/
│   └── (JavaScript files)
├── data/
│   ├── publications.json (edit this!)
│   ├── blog.json (edit this!)
│   └── news.json (edit this!)
├── blog/
│   └── (your blog post HTML files)
└── images/
    ├── profile.jpg (your photo)
    └── blog/ (blog images)
```

Happy content creating! 🎉
