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
   - Edit the HTML files to update your bio, contact info, etc.
   - Replace `images/profile.jpg` with your profile picture
   - Update social media links in all HTML files

3. **Add your data:**
   - Edit `data/publications.json` to add your publications
   - Edit `data/blog.json` to add blog post metadata
   - Edit `data/news.json` to add news items

4. **View locally:**
   - Open `index.html` in your web browser
   - Or use a local server:
     ```bash
     python -m http.server 8000
     # Then visit http://localhost:8000
     ```

5. **Deploy:**
   - Deploy to GitHub Pages, Netlify, Vercel, or any static hosting service
   - Just upload all files to your hosting provider

## Adding Content

### Adding a Publication

Edit `data/publications.json`:

```json
{
  "title": "Your Paper Title",
  "authors": "Author 1, Author 2, Author 3",
  "venue": "Conference Name (Acronym)",
  "year": "2024",
  "abstract": "Brief description of your paper",
  "links": {
    "paper": "https://link-to-paper.pdf",
    "code": "https://github.com/username/repo",
    "project": "https://project-page-url.com"
  }
}
```

### Adding a Blog Post

1. **Create the HTML file** in the `blog/` directory:
   - Copy an existing blog post as a template
   - Name it with a slug, e.g., `my-new-post.html`
   - Update the content

2. **Add metadata** to `data/blog.json`:
   ```json
   {
     "title": "My New Blog Post",
     "slug": "my-new-post",
     "date": "December 1, 2024",
     "excerpt": "A brief description of the post",
     "image": "images/blog/my-post-image.jpg"
   }
   ```

### Adding News Items

Edit `data/news.json`:

```json
{
  "date": "November 2024",
  "content": "Your news update here"
}
```

## Customization

### Colors and Styling

Edit `css/style.css` and modify the CSS variables at the top:

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

### Navigation

Update the navigation links in all HTML files. Each page has this structure:

```html
<ul class="nav-menu">
    <li><a href="index.html">About</a></li>
    <li><a href="publications.html">Publications</a></li>
    <li><a href="blog.html">Blog</a></li>
    <li><a href="contact.html">Contact</a></li>
</ul>
```

### Social Links

Update social media links in the footer of each HTML file:

```html
<div class="social-links">
    <a href="mailto:your.email@example.com" aria-label="Email">...</a>
    <a href="https://scholar.google.com/..." aria-label="Google Scholar">...</a>
    <a href="https://github.com/yourusername" aria-label="GitHub">...</a>
    <!-- etc -->
</div>
```

### Contact Form

The contact form is currently set up for demonstration. To make it functional, integrate with a form service:

**Option 1: Formspree** (Recommended - free tier available)
1. Sign up at [formspree.io](https://formspree.io)
2. Create a form and get your form ID
3. Edit `js/contact.js` and uncomment the Formspree integration code
4. Replace `YOUR_FORM_ID` with your actual form ID

**Option 2: Netlify Forms** (if hosting on Netlify)
1. Add `netlify` attribute to the form tag in `contact.html`
2. Netlify will automatically handle form submissions

**Option 3: Custom Backend**
- Implement your own backend API endpoint
- Update the form submission code in `js/contact.js`

## Deployment

### GitHub Pages

1. Go to your repository settings
2. Navigate to "Pages" section
3. Select the branch to deploy (usually `main` or `master`)
4. Select `/` (root) as the folder
5. Save and wait for deployment

Your site will be available at: `https://yourusername.github.io/repository-name`

### Netlify

1. Sign up at [netlify.com](https://www.netlify.com)
2. Click "Add new site" → "Import an existing project"
3. Connect your GitHub repository
4. Click "Deploy site" (no build command needed!)

### Vercel

1. Sign up at [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repository
4. Click "Deploy" (no configuration needed!)

### Custom Domain

After deploying, you can add a custom domain:
- **GitHub Pages**: Add a `CNAME` file with your domain
- **Netlify/Vercel**: Use their domain settings interface

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## License

Feel free to use this template for your own website. No attribution required.

## Credits

Built with:
- Pure HTML5, CSS3, and JavaScript
- Font Awesome icons
- No frameworks or build tools required! 
