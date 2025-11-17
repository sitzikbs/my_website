# Personal Website - Itzik Ben-Shabat

A modern, lightweight personal website built with pure HTML, CSS, and JavaScript. This site showcases research publications, blog posts, and professional information without relying on WordPress or other heavy content management systems.

## 🌐 Live Website

Visit the live site at: [https://itzikbs.com/](https://itzikbs.com/)

## 📁 Project Structure

```
my_website/
├── css/                    # All stylesheets
│   ├── reset.css          # Browser normalization
│   ├── variables.css      # CSS custom properties
│   ├── base.css           # Global styles
│   ├── layout.css         # Layout utilities
│   ├── components.css     # Component styles
│   └── responsive.css     # Media queries
├── js/                     # JavaScript files
│   ├── navigation.js      # Navigation functionality
│   ├── publications.js    # Publications rendering
│   └── blog.js            # Blog functionality
├── assets/                 # Static assets
│   ├── images/            # Image files
│   ├── fonts/             # Custom fonts
│   └── icons/             # Icon files
├── blog/                   # Blog posts
│   ├── index.html         # Blog listing page
│   └── posts/             # Individual blog posts
├── publications/           # Publications section
│   └── index.html         # Publications page
├── data/                   # JSON data files
│   ├── publications.json  # Publications data
│   └── blog-index.json    # Blog post metadata
├── index.html             # Homepage
├── package.json           # Project metadata
└── README.md              # This file
```

## 🚀 Getting Started

### Prerequisites

- A modern web browser (Chrome, Firefox, Safari, or Edge)
- Python 3 (for local development server) or any other HTTP server

### Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sitzikbs/my_website.git
   cd my_website
   ```

2. **Start a local development server:**
   ```bash
   npm run dev
   # or
   python3 -m http.server 8000
   ```

3. **Open your browser:**
   Navigate to `http://localhost:8000`

### Alternative Servers

You can use any HTTP server of your choice:
- **Node.js:** `npx http-server`
- **PHP:** `php -S localhost:8000`
- **Ruby:** `ruby -run -ehttpd . -p8000`

## ✍️ Adding New Content

### Adding a New Blog Post

1. **Create a new HTML file** in the `blog/posts/` directory:
   ```
   blog/posts/YYYY-MM-DD-post-title.html
   ```

2. **Use the blog post template** with proper structure:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Post Title - Itzik Ben-Shabat</title>
       <link rel="stylesheet" href="../../css/base.css">
   </head>
   <body>
       <!-- Navigation -->
       <!-- Post content -->
   </body>
   </html>
   ```

3. **Update blog index** in `data/blog-index.json`:
   ```json
   {
     "id": "post-slug",
     "title": "Post Title",
     "date": "2024-01-01",
     "excerpt": "Brief description...",
     "tags": ["tag1", "tag2"],
     "image": "path/to/image.jpg"
   }
   ```

### Adding a New Publication

1. **Add publication data** to `data/publications.json`:
   ```json
   {
     "id": "unique-id",
     "title": "Publication Title",
     "authors": ["Author 1", "Author 2"],
     "venue": "Conference/Journal Name",
     "year": 2024,
     "abstract": "Abstract text...",
     "links": {
       "paper": "url-to-pdf",
       "project": "url-to-project-page",
       "code": "url-to-github",
       "video": "url-to-video"
     },
     "image": "assets/images/publications/thumbnail.jpg",
     "bibtex": "BibTeX citation...",
     "featured": true
   }
   ```

2. **Add images** to `assets/images/publications/`

3. The publication will automatically appear on the publications page

### Adding Images

1. Place images in appropriate subdirectories:
   - Blog images: `assets/images/blog/`
   - Publication images: `assets/images/publications/`
   - Profile/general images: `assets/images/`

2. Optimize images before adding:
   - Compress images (use tools like TinyPNG, ImageOptim)
   - Use appropriate formats (WebP with JPG/PNG fallbacks)
   - Consider responsive image sizes

## 🚢 Deployment

### GitHub Pages

1. Push your changes to the `main` branch
2. Go to repository Settings > Pages
3. Select `main` branch as source
4. Your site will be available at `https://[username].github.io/my_website/`

### Netlify

1. Connect your GitHub repository to Netlify
2. Set build command: (leave empty for static site)
3. Set publish directory: `/`
4. Deploy!

### Custom Domain

1. Add your custom domain in hosting platform settings
2. Update DNS records:
   ```
   Type: A
   Name: @
   Value: [hosting provider IP]
   
   Type: CNAME
   Name: www
   Value: [hosting provider domain]
   ```

3. Enable HTTPS/SSL (usually automatic)

## 🎨 Design System

### Colors
- Primary: `#333333`
- Secondary: `#666666`
- Accent: `#0066cc`
- Background: `#ffffff`
- Text: `#1a1a1a`

### Typography
- Headings: System font stack
- Body: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, sans-serif

### Responsive Breakpoints
- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: 1024px - 1440px
- Large Desktop: > 1440px

## 🧪 Testing

### Before Deployment
- [ ] Test all internal links
- [ ] Test all external links
- [ ] Verify responsive design on multiple devices
- [ ] Check cross-browser compatibility
- [ ] Run Lighthouse audit (aim for 90+ score)
- [ ] Validate HTML (W3C Validator)
- [ ] Check accessibility (WAVE, axe DevTools)

## 🤝 Contributing

This is a personal website, but suggestions and bug reports are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add some improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📧 Contact

- Website: [https://itzikbs.com/](https://itzikbs.com/)
- GitHub: [@sitzikbs](https://github.com/sitzikbs)

## 🙏 Acknowledgments

- Design inspiration from [Vincent Sitzmann's website](https://www.vincentsitzmann.com/)
- Built with semantic HTML5, modern CSS3, and vanilla JavaScript

---

**Status:** In Development
**Last Updated:** 2025-11-17
