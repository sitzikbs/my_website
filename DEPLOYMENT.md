# Deployment Guide

This guide covers deploying your Eleventy (11ty) static site to production.

## Prerequisites

Before deploying:
1. **Build locally:** Run `npm run build` to ensure the site builds without errors
2. **Test locally:** Run `npm run serve` and test at http://localhost:8000
3. **Commit changes:** Ensure all changes are committed to git
4. **Update data:** Verify `data/publications.json`, `data/news.json`, etc. are current
5. **Check assets:** Ensure all images and assets are properly placed in `assets/`
6. **HTML validation:** Automated HTML validation runs on pull requests via GitHub Actions

---

## 📦 Build Configuration

This site uses **Eleventy (11ty) static site generator** with automated build process:

- **Build command:** `npm run build`
- **Output directory:** `_site/`
- **Node version:** 18 or later (LTS recommended)

The build process runs:
1. CSS minification (`csso`)
2. JavaScript minification (`terser`)
3. 11ty static site generation
4. All assets copied to `_site/`

---

## ⭐ Cloudflare Pages (Recommended)

Cloudflare Pages is the **recommended platform** for this 11ty site. It provides:
- Automatic builds on git push
- Edge network (fast global delivery)
- Free SSL/HTTPS
- Unlimited bandwidth
- Preview deployments for branches

### Setup Steps:

1. **Sign up** at [pages.cloudflare.com](https://pages.cloudflare.com)

2. **Create a project:**
   - Click "Create a project"
   - Connect your GitHub account
   - Select your repository

3. **Configure build settings:**
   - **Framework preset:** Eleventy
   - **Build command:** `npm run build`
   - **Build output directory:** `_site`
   - **Root directory:** (leave empty)

4. **Environment variables:**
   - Add: `NODE_VERSION` = `18`

5. **Deploy:**
   - Click "Save and Deploy"
   - Wait for first build (usually 1-2 minutes)

6. **Custom domain:**
   - Go to "Custom domains" tab
   - Add your domain (e.g., itzikbs.com)
   - Update DNS records as instructed
   - SSL certificate will be automatically provisioned

### Automatic Deployments

After setup, Cloudflare Pages will:
- **Automatically build and deploy** when you push to `main` branch
- Create **preview deployments** for other branches/PRs
- Provide unique URLs for testing before merging

---

## Alternative Platforms

### Netlify

Excellent alternative with similar features:

1. Sign up at [netlify.com](https://www.netlify.com)
2. Click "Add new site" → "Import an existing project"
3. Connect GitHub and select repository
4. Build settings:
   - **Build command:** `npm run build`
   - **Publish directory:** `_site`
   - **Node version:** 18 (in environment variables)
5. Deploy

**Features:**
- Free SSL certificates
- Automatic deployments
- Form handling with `netlify` attribute
- Serverless functions support

### Vercel

Another popular option:

1. Sign up at [vercel.com](https://vercel.com)
2. Import repository from GitHub
3. Framework: Select "Other" or "11ty"
4. Build settings:
   - **Build Command:** `npm run build`
   - **Output Directory:** `_site`
5. Deploy

---

## GitHub Pages (Not Recommended for 11ty)

GitHub Pages **doesn't natively support build processes**. Options:

**Option A:** Build locally and commit `_site/`
- Not recommended (bloats repository with build artifacts)

**Option B:** Use GitHub Actions
- Requires workflow configuration
- More complex setup

**Recommendation:** Use Cloudflare Pages or Netlify instead for automatic builds.

---

## Post-Deployment Checklist

After deploying:

- [ ] **Test live site:** Verify all pages load correctly
- [ ] **Check HTTPS:** Ensure SSL certificate is active
- [ ] **Test forms:** If using contact forms, verify they work
- [ ] **Verify analytics:** Check Google Analytics 4 (ID: G-EJRL17R9NE) is tracking
- [ ] **Test links:** Verify internal and external links work
- [ ] **Mobile testing:** Test on mobile devices
- [ ] **Performance:** Run Lighthouse audit
- [ ] **SEO setup:**
  - [ ] Add property to Google Search Console
  - [ ] Submit sitemap.xml (`https://yourdomain.com/sitemap.xml`)
  - [ ] Verify robots.txt is accessible

---

## Updating Content

### Blog Posts

1. Create new Markdown file in `blog/posts-md/`:
   ```bash
   # Format: YYYY-MM-DD-title.md
   touch blog/posts-md/2026-01-15-my-new-post.md
   ```

2. Add frontmatter and content:
   ```yaml
   ---
   title: "My New Post"
   date: 2026-01-15
   excerpt: "Brief description"
   image: "/assets/images/blog/image.jpg"
   ---
   
   Post content here...
   ```

3. Commit and push:
   ```bash
   git add blog/posts-md/2026-01-15-my-new-post.md
   git commit -m "feat: add new blog post"
   git push
   ```

4. Site will automatically rebuild and deploy!

### Publications

1. Edit `data/publications.json`
2. Add new publication entry
3. Commit and push - site rebuilds automatically

### News Items

1. Edit `data/news.json`
2. Add new news entry
3. Commit and push

---

## Build Troubleshooting

### Build Fails

1. **Check logs** in hosting platform dashboard
2. **Test locally:** Run `npm run build` and fix any errors
3. **Verify Node version:** Ensure environment uses Node 18+
4. **Check dependencies:** Run `npm install` locally

### Site Not Updating

1. **Verify deployment succeeded** in hosting dashboard
2. **Clear browser cache** (Ctrl+Shift+R or Cmd+Shift+R)
3. **Check CDN cache** - may take a few minutes to propagate
4. **Verify commit was pushed** to correct branch

### Missing Assets

1. **Check file paths** are correct (relative from site root)
2. **Verify files exist** in `assets/` directory
3. **Check .eleventy.js** passthrough copy configuration
4. **Rebuild:** Sometimes `npm run build` again fixes it

---

## Performance Optimization

The site is already optimized with:
- ✅ WebP images with responsive sizes
- ✅ CSS minification
- ✅ JavaScript minification
- ✅ Lazy loading images
- ✅ Google Fonts optimization

For further optimization:
- Enable **Cloudflare CDN caching** (automatic with Cloudflare Pages)
- Use **Cloudflare Analytics** for detailed metrics
- Monitor **Core Web Vitals** in Google Search Console

---

## Security

Ensure these security measures:
- ✅ HTTPS/SSL enabled (automatic with modern hosts)
- ✅ Security headers configured
- ✅ Dependencies updated: Run `npm audit` regularly
- ✅ Secrets in environment variables (never commit)

---

## Support & Resources

- **11ty Documentation:** https://www.11ty.dev/docs/
- **Cloudflare Pages Docs:** https://developers.cloudflare.com/pages/
- **Netlify Docs:** https://docs.netlify.com/
- **Repository:** https://github.com/sitzikbs/my_website
