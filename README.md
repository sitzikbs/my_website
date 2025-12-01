# Personal Website

A clean, responsive, static website built with pure HTML, CSS, and JavaScript. No WordPress dependency required!

## Features

- 🎨 Clean, modern design inspired by academic/researcher websites
- 📱 Fully responsive (mobile, tablet, desktop)
- 🚀 Fast loading - pure static HTML/CSS/JS
- 📝 Easy content management via JSON files
- 📚 Publications page
- ✍️ Blog with individual post pages
- 📧 Contact page with form
- 🎯 No build process required - just edit and deploy

## Structure

```
├── index.html              # Homepage with bio and recent work
├── publications.html       # Full publications list
├── blog.html              # Blog posts grid
├── contact.html           # Contact information and form
├── css/
│   └── style.css          # All styles (includes responsive design)
├── js/
│   ├── main.js            # Navigation and general functionality
│   ├── data-loader.js     # Loads data for homepage
│   ├── publications-loader.js  # Loads publications
│   ├── blog-loader.js     # Loads blog posts
│   └── contact.js         # Contact form handling
├── data/
│   ├── publications.json  # Publications data
│   ├── blog.json         # Blog posts metadata
│   └── news.json         # News/updates
├── blog/
│   └── [post-name].html  # Individual blog post pages
└── images/
    └── profile.jpg       # Profile picture (add your own)
```

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/my_website.git
   cd my_website
   ```

2. **Customize the content:**
   - Edit `index.html` for your bio and introduction.
   - Update `data/publications.json` with your papers.
   - Add blog posts to `data/blog.json` and create HTML files in `blog/`.
   - Replace `images/profile.jpg` with your photo.

3. **Run locally:**
   Since it's a static site, you can just open `index.html` in your browser.
   
   For a better experience (and to avoid CORS issues with JSON loading), use a simple local server:
   
   ```bash
   # Python 3
   python3 -m http.server
   
   # Node.js
   npx serve
   ```

## Customization

### Colors and Fonts
Edit `css/style.css` to change the CSS variables at the top of the file:

```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --accent-color: #e74c3c;
    /* ... */
}
```

### Adding Blog Posts
1. Create a new HTML file in `blog/` (copy an existing one as a template).
2. Add an entry to `data/blog.json`:
   ```json
   {
       "title": "My New Post",
       "date": "2024-03-20",
       "excerpt": "Short summary...",
       "url": "blog/my-new-post.html",
       "tags": ["research", "update"]
   }
   ```

## Deployment

You can deploy this site for free on:
- **GitHub Pages**: Go to Settings > Pages > Source: Main branch.
- **Netlify**: Drag and drop the folder.
- **Vercel**: Import the repository.
