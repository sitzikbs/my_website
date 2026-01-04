# Website TODO & Project Status

## Overview
Personal website built with Eleventy (11ty) static site generator. Successfully migrated from WordPress to a modern, lightweight static site with all content preserved.

## 🎯 Current Status (January 2026)
- **All Phases:** ✅ COMPLETE (Setup, Migration, Deployment, Security)
- **Repository Cleanup:** ✅ COMPLETE (Issues #35, #52)

**Site Status:** 
- ✅ Live at https://itzikbs.com
- ✅ 11ty build system fully operational (builds in ~1.3 seconds)
- ✅ All 74 blog posts migrated from WordPress to Markdown
- ✅ Asset optimization: 78.3% size reduction (489 images → WebP)
- ✅ CSS/JS minification and build automation
- ✅ SEO complete: Schema.org, Open Graph, sitemap.xml, robots.txt
- ✅ Google Analytics 4 integrated (ID: G-EJRL17R9NE)
- ✅ Security audit complete (see [docs/SECURITY_AUDIT.md](docs/SECURITY_AUDIT.md))
- ✅ Repository organized: one-time scripts archived, temporary files removed

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

## ⏳ Maintenance Tasks

### Content Updates
- [ ] Monitor and update publications.json as new papers are published
- [ ] Add new blog posts as needed
- [ ] Keep CV/documents up to date

### Periodic Checks
- [ ] Run accessibility checks: `uv run python scripts/check_accessibility.py`
- [ ] Run heading hierarchy checks: `uv run python scripts/check_heading_hierarchy.py`
- [ ] Validate data files: `uv run python scripts/validate-content.py`
- [ ] Check for broken links
- [ ] Review Google Analytics for insights
- [ ] Monitor Google Search Console for SEO issues
- [ ] Update npm dependencies periodically: `npm audit` and `npm update`

### Performance Monitoring
- [ ] Periodic Lighthouse audits
- [ ] Monitor Core Web Vitals in Search Console
- [ ] Check page load times

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
├── data/              # JSON data files (+ archive/ for historical data)
├── docs/              # Project documentation
├── js/                # JavaScript files
├── scripts/           # Python utility scripts
│   ├── archive/       # 11ty migration scripts (completed)
│   └── one-time/      # WordPress migration scripts (completed)
├── .eleventy.js       # 11ty configuration
├── package.json       # Dependencies and build scripts
└── *.html             # Page templates (index, about, etc.)
```

---

## 📚 Documentation

See `docs/` directory for detailed documentation:
- **CLOUDFLARE_DEPLOYMENT.md** - Deployment instructions
- **DESIGN_SYSTEM.md** - CSS architecture and design patterns
- **PERFORMANCE_SEO_PLAN.md** - Optimization guide
- **PERFORMANCE_SUMMARY.md** - Performance metrics
- **SECURITY_AUDIT.md** - Security implementation and audit results

---

## 🔗 Useful Links

- **Live Site:** https://itzikbs.com
- **Repository:** https://github.com/sitzikbs/my_website
- **11ty Documentation:** https://www.11ty.dev/docs/
- **Cloudflare Pages:** https://pages.cloudflare.com
