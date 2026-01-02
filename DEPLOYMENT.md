# Deployment Guide

This guide will help you deploy your new static website to various hosting platforms.

## Prerequisites

Before deploying, make sure to:
1. **Build the site:** Run `npm run build` to generate the `_site` directory
2. Replace `assets/images/profile/` images with your actual profile pictures
3. Update personal information in the 11ty templates (`_includes/layouts/`)
4. Update social media links in templates
5. Add your publications to `data/publications.json`
6. Add blog posts as Markdown files in `blog/posts-md/`
7. Update `data/news.json` with your news

## Deployment Options

**Important:** After the 11ty migration, your site requires a build step. See the note about Cloudflare Pages below for the recommended deployment approach.

### 1. GitHub Pages (Free)

GitHub Pages is perfect for static websites and integrates directly with your repository.

**Steps:**
1. Go to your repository on GitHub
2. Click on "Settings"
3. Scroll down to "Pages" in the left sidebar
4. Under "Source", select the branch you want to deploy (usually `main`)
5. Select `/` (root) as the folder
6. Click "Save"
7. Wait a few minutes for deployment

**Note for 11ty sites:** You'll need to either:
- **Option A:** Build locally and commit `_site/` folder, then set GitHub Pages to serve from `_site/`
- **Option B:** Use GitHub Actions to auto-build (requires workflow configuration)
- **Recommended:** Use Cloudflare Pages instead for automatic builds

Your site will be available at: `https://[username].github.io/[repository-name]`

**Custom Domain:**
- Add a file named `CNAME` to the root with your domain name
- Configure your domain's DNS settings to point to GitHub Pages

### 2. Netlify (Free, Very Easy)

Netlify offers continuous deployment and excellent features.

**Steps:**
1. Sign up at [netlify.com](https://www.netlify.com)
2. Click "Add new site" → "Import an existing project"
3. Connect your GitHub account
4. Select your repository
5. Deploy settings:
   - **Build command:** `npm run build`
   - **Publish directory:** `_site`
6. Click "Deploy site"

Your site will be live in seconds with a custom Netlify URL. You can add a custom domain later.

**Features:**
- Automatic deployments on git push
- Free SSL certificates
- Contact form handling (add `netlify` attribute to form)
- Instant rollbacks

### 3. Vercel (Free, Fast)

Vercel is another excellent option with great performance.

**Steps:**
1. Sign up at [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repository
4. Framework Preset: Select "Other" or "11ty"
5. Build settings:
   - **Build Command:** `npm run build`
   - **Output Directory:** `_site`
6. Click "Deploy"

Your site will be deployed with a Vercel URL. Add a custom domain in settings.

### 4. Cloudflare Pages (Recommended) ⭐

**This site uses Eleventy (11ty) static site generator.** Cloudflare Pages is the recommended deployment option for automatic builds.

**Steps:**
1. Sign up at [pages.cloudflare.com](https://pages.cloudflare.com)
2. Click "Create a project"
3. Connect your GitHub account
4. Select your repository
5. Build settings:
   - **Framework preset:** Eleventy
   - **Build command:** `npm run build`
   - **Build output directory:** `_site`
   - **Root directory:** (leave empty)
   - **Environment variables:** 
     - `NODE_VERSION` = `18` (or latest LTS)
6. Click "Save and Deploy"

**Benefits:**
- ✅ Automatic deployments on every push to main
- ✅ Branch preview deployments (test before merging!)
- ✅ Free SSL, unlimited bandwidth
- ✅ Global CDN for fast loading worldwide
- ✅ Build logs for debugging
- ✅ Instant rollbacks if needed

**Custom Domain:**
1. Go to your Cloudflare Pages project
2. Navigate to "Custom domains"
3. Add your domain (e.g., itzikbs.com)
4. Follow DNS configuration instructions
5. SSL certificate automatically provisioned

**Deployment Workflow:**
```bash
# Make changes to templates, blog posts, or data
git add .
git commit -m "Add new blog post"
git push origin main

# Cloudflare automatically:
# 1. Detects push
# 2. Runs npm install
# 3. Runs npm run build (11ty builds your site)
# 4. Deploys _site/ folder to CDN
# 5. Site live in ~1-2 minutes!
```

**Local Development:**
```bash
# Install dependencies
npm install

# Run dev server with hot reload
npm run serve
# Site available at http://localhost:8080

# Build for production
npm run build
# Output in _site/ directory
```

### 5. Traditional Web Hosting

For traditional hosting (shared hosting, VPS, etc.):

1. **Export your files:**
   ```bash
   # Create a zip of all files (excluding .git)
   zip -r website.zip . -x "*.git*" "*.DS_Store" "node_modules/*"
   ```

2. **Upload via FTP/SFTP:**
   - Use FileZilla, Cyberduck, or your hosting provider's file manager
   - Upload all files to your `public_html` or `www` directory

3. **Configure:**
   - Ensure your hosting supports static files (it should!)
   - Set your index page to `index.html`

## Post-Deployment Checklist

After deploying, verify:

- [ ] All pages load correctly
- [ ] Navigation works on all pages
- [ ] Images display properly
- [ ] Links work (internal and external)
- [ ] Contact form is configured (if using a service)
- [ ] Mobile responsiveness works
- [ ] Social media links point to correct profiles
- [ ] Custom domain is configured (if applicable)
- [ ] SSL/HTTPS is enabled
- [ ] Test all interactive elements

## Configure Contact Form

The contact form needs a backend service to work. Choose one:

### Option 1: Formspree (Recommended)

1. Sign up at [formspree.io](https://formspree.io)
2. Create a new form
3. Get your form endpoint URL
4. Edit `js/contact.js`:
   - Uncomment the Formspree integration code (lines ~40-50)
   - Replace `YOUR_FORM_ID` with your actual form ID
5. Commit and push changes

### Option 2: Netlify Forms

If hosting on Netlify:
1. Edit `contact.html`
2. Add `netlify` attribute to the `<form>` tag:
   ```html
   <form id="contact-form" class="contact-form" netlify>
   ```
3. Add a hidden input for spam protection:
   ```html
   <input type="hidden" name="form-name" value="contact-form">
   ```
4. Deploy - Netlify automatically handles submissions

### Option 3: Custom Backend

If you have your own backend:
1. Create an API endpoint to handle form submissions
2. Edit `js/contact.js` to post to your endpoint
3. Handle CORS if needed

## Performance Optimization

After deployment, consider:

1. **Enable Compression:** Most hosting platforms do this automatically
2. **Use a CDN:** Cloudflare, etc. (often included with hosts)
3. **Optimize Images:** 
   - Use WebP format where possible
   - Compress images before uploading
   - Use appropriate sizes
4. **Add Caching Headers:** Configure via hosting platform

## SEO Configuration

1. **Update meta tags** in each HTML file:
   ```html
   <meta name="description" content="Your actual description">
   <meta name="keywords" content="your, keywords, here">
   <meta name="author" content="Your Name">
   ```

2. **Create a sitemap.xml:**
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
     <url>
       <loc>https://yourdomain.com/</loc>
       <priority>1.0</priority>
     </url>
     <url>
       <loc>https://yourdomain.com/publications.html</loc>
       <priority>0.8</priority>
     </url>
     <!-- Add more pages -->
   </urlset>
   ```

3. **Add robots.txt:**
   ```
   User-agent: *
   Allow: /
   
   Sitemap: https://yourdomain.com/sitemap.xml
   ```

4. **Submit to search engines:**
   - Google Search Console
   - Bing Webmaster Tools

## Analytics (Optional)

Add Google Analytics or other analytics:

1. Sign up for Google Analytics
2. Get your tracking code
3. Add before `</head>` in all HTML files:
   ```html
   <!-- Google Analytics -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'GA_MEASUREMENT_ID');
   </script>
   ```

## Maintenance

**Regular Updates:**
- Add new publications to `data/publications.json`
- Add blog posts by creating HTML files and updating `data/blog.json`
- Update news in `data/news.json`
- Keep your profile and bio up to date

**Version Control:**
- Always commit changes to git
- Use meaningful commit messages
- Deployments will happen automatically (with Netlify/Vercel/etc.)

## Troubleshooting

**Pages not loading:**
- Check that all file paths are correct (case-sensitive on Linux servers)
- Verify index.html exists in root

**Images not showing:**
- Check image paths are relative (not absolute)
- Ensure images are in the correct directory
- Check image file extensions match

**CSS/JS not loading:**
- Verify paths in HTML are correct
- Check browser console for errors
- Clear browser cache

**Contact form not working:**
- Ensure you've configured a form handler (Formspree, etc.)
- Check browser console for JavaScript errors
- Verify CORS settings if using custom backend

## Support

If you encounter issues:
1. Check browser console for errors (F12)
2. Verify all file paths are correct
3. Test locally first: `python -m http.server 8000`
4. Check hosting platform's documentation
5. Review the README.md for configuration details

Happy deploying! 🚀
