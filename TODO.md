# Website TODO & Project Status

## Overview
Personal website built with Eleventy (11ty) static site generator. Successfully migrated from WordPress to a modern, lightweight static site with all content preserved.

## 🎯 Current Status (January 2026)
- **Phase 1-8:** ✅ COMPLETE (Setup through SEO & Accessibility)
- **11ty Migration:** ✅ COMPLETE (74 blog posts migrated to Markdown)
- **Repository Cleanup:** ✅ COMPLETE (Issue #35)
- **Phase 9-10:** ⏳ IN PROGRESS (Deployment, Testing, Security)

**Latest Achievements:** 
- ✅ 11ty build system fully operational (builds in ~1.3 seconds)
- ✅ All 74 blog posts migrated to Markdown with proper frontmatter
- ✅ Asset optimization: 78.3% size reduction (489 images → WebP)
- ✅ CSS/JS minification and build automation
- ✅ SEO complete: Schema.org, Open Graph, sitemap.xml, robots.txt
- ✅ Google Analytics 4 integrated (ID: G-EJRL17R9NE)
- ✅ Repository cleaned for production launch

---

## 📦 Build Commands

- **Development:** `npm run dev` - Start 11ty dev server with hot reload
- **Build site:** `npm run build` - Full build (CSS minify + JS minify + 11ty build)
- **Build CSS only:** `npm run build:css` - Minify CSS
- **Build JS only:** `npm run build:js` - Minify JavaScript
- **Build 11ty only:** `npm run build:11ty` - Generate static site
- **Watch CSS:** `npm run watch:css` - Auto-rebuild CSS on changes
- **Serve built site:** `npm run serve` - Serve _site/ directory on port 8000
- **Generate sitemap:** `npm run build:sitemap` - Run sitemap generator

---

## ⏳ Outstanding Tasks

### Phase 9: Deployment (NEXT PRIORITY)

#### 9.1 Cloudflare Pages Deployment
- [ ] Connect GitHub repository to Cloudflare Pages
- [ ] Configure build settings:
  - Build command: `npm run build`
  - Output directory: `_site`
  - Environment: `NODE_VERSION = 18`
- [ ] Enable automatic deployments from main branch
- [ ] Set up custom domain (itzikbs.com)
- [ ] Verify HTTPS/SSL configuration
- [ ] Test deployment and verify site functionality

#### 9.2 Post-Deployment Verification
- [ ] Verify Google Analytics 4 tracking (ID: G-EJRL17R9NE)
- [ ] Submit sitemap.xml to Google Search Console
- [ ] Monitor indexation status
- [ ] Test all pages and functionality live

---

### Phase 10: Testing & Security

#### 10.1 Performance Testing
- [ ] Run Lighthouse audits (aim for 90+ performance score)
- [ ] Test page load speeds
- [ ] Verify Core Web Vitals (LCP, FID, CLS)
- [ ] Cross-browser testing: Chrome, Firefox, Safari, Edge
- [ ] Mobile device testing

#### 10.2 Accessibility Testing (WCAG 2.1 AA)
- [ ] Verify color contrast (4.5:1 for normal text)
- [ ] Test keyboard navigation support
- [ ] Verify focus indicators visible
- [ ] Test with screen reader (NVDA, JAWS, or VoiceOver)

#### 10.3 Security Audit
- [ ] Run security checks:
  - [ ] Mozilla Observatory: https://observatory.mozilla.org
  - [ ] Security Headers: https://securityheaders.com
  - [ ] SSL Labs: https://www.ssllabs.com/ssltest/
- [ ] Implement Content Security Policy (CSP)
- [ ] Configure security headers (X-Frame-Options, etc.)
- [ ] Add Subresource Integrity (SRI) for CDN resources
- [ ] Verify HTTPS/HSTS configuration
- [ ] Audit npm dependencies: `npm audit`

#### 10.4 Functionality Testing
- [ ] Test all internal links
- [ ] Test all external links
- [ ] Verify navigation works on all pages
- [ ] Verify all publications load correctly
- [ ] Verify all blog posts display properly
- [ ] Test responsive images at different screen sizes

---

## 📝 Content Management

### Adding New Blog Posts
1. Create new Markdown file in `blog/posts-md/` with format: `YYYY-MM-DD-title.md`
2. Add frontmatter:
   ```yaml
   ---
   title: "Post Title"
   date: YYYY-MM-DD
   excerpt: "Brief description"
   image: "/assets/images/blog/image.jpg"
   ---
   ```
3. Write content in Markdown
4. Run `npm run build` to generate HTML
5. Commit and push to deploy

### Adding Publications
1. Edit `data/publications.json`
2. Add publication entry with all details
3. Rebuild site: `npm run build`
4. Commit and push

---

## 🗂️ Project Structure

```
/
├── _includes/          # 11ty templates (layouts, partials)
├── _site/             # Built site (git ignored)
├── assets/            # Images, videos, documents
├── blog/              # Blog posts (Markdown in posts-md/)
├── css/               # Stylesheets
├── data/              # JSON data files
├── docs/              # Project documentation
├── js/                # JavaScript files
├── scripts/           # Python utility scripts
├── .eleventy.js       # 11ty configuration
├── package.json       # Dependencies and build scripts
└── *.html             # Page templates (index, about, etc.)
```

---

## 📚 Documentation

See `docs/` directory for detailed documentation:
- **DESIGN_SYSTEM.md** - CSS architecture and design patterns
- **CLOUDFLARE_DEPLOYMENT.md** - Deployment instructions
- **PERFORMANCE_SEO_PLAN.md** - Optimization guide
- **PERFORMANCE_SUMMARY.md** - Performance metrics

---

## 🔗 Useful Links

- **Live Site:** https://itzikbs.com
- **Repository:** https://github.com/sitzikbs/my_website
- **11ty Documentation:** https://www.11ty.dev/docs/
- **Cloudflare Pages:** https://pages.cloudflare.com
