# 11ty Migration Plan

**Goal**: Migrate from static HTML with duplicated templates to 11ty static site generator with Markdown blog posts and reusable templates.

**Timeline**: ~5-7 hours total, spread across multiple branches
**Date Started**: 2026-01-02

---

## Migration Phases

### Phase 1: Setup & Foundation (Issue #20)
**Branch**: `feat/11ty-setup`
**Time Estimate**: 1-2 hours

**Tasks**:
- [ ] Install 11ty: `npm install --save-dev @11ty/eleventy`
- [ ] Create `.eleventy.js` config file
- [ ] Set up input/output directories
- [ ] Create `_includes/` directory for templates
- [ ] Create base layout template (`_includes/layouts/base.njk`)
- [ ] Create navigation partial (`_includes/partials/nav.njk`)
- [ ] Create footer partial (`_includes/partials/footer.njk`)
- [ ] Configure passthrough copy for assets (css/, js/, assets/, etc.)
- [ ] Add build scripts to package.json
- [ ] Test basic build

**Validation Checklist**:
- [ ] `npm run build` works without errors
- [ ] Output directory (_site/) is created
- [ ] CSS/JS/images are copied correctly
- [ ] Basic layout renders

**Deliverables**:
- Working 11ty configuration
- Base templates (layout, nav, footer)
- Build command that generates static HTML

---

### Phase 2: Migrate Homepage & Core Pages (Issue #21)
**Branch**: `feat/11ty-core-pages`
**Time Estimate**: 1-2 hours
**Depends On**: Phase 1

**Tasks**:
- [ ] Convert index.html to index.njk (or keep as .html with frontmatter)
- [ ] Use base layout in homepage
- [ ] Keep data loading JavaScript for publications/news/podcast
- [ ] Convert about.html to use base layout
- [ ] Convert publications.html to use base layout
- [ ] Convert podcast.html to use base layout
- [ ] Convert blog.html (index) to use base layout
- [ ] Convert code.html to use base layout
- [ ] Convert contact.html to use base layout
- [ ] Test all navigation links work
- [ ] Verify dynamic content (publications, news) still loads

**Validation Checklist**:
- [ ] All 7 core pages render correctly
- [ ] Navigation shows on all pages with correct active states
- [ ] Footer shows on all pages
- [ ] All links work (internal and external)
- [ ] Dynamic content (publications, news, podcast) loads via JS
- [ ] Styling is identical to current site

**Deliverables**:
- All core pages using base template
- Single source of truth for nav/footer
- No duplicated HTML structure

---

### Phase 3: Create Blog Post Template (Issue #22)
**Branch**: `feat/11ty-blog-template`
**Time Estimate**: 1 hour
**Depends On**: Phase 2

**Tasks**:
- [ ] Create blog post layout (`_includes/layouts/blog-post.njk`)
- [ ] Design blog post frontmatter schema (title, date, author, excerpt, image)
- [ ] Add blog hero section to template
- [ ] Configure markdown processing
- [ ] Add syntax highlighting for code blocks (if needed)
- [ ] Create blog post collection in 11ty config
- [ ] Test with 1-2 sample posts

**Blog Post Frontmatter Schema**:
```yaml
---
title: "Post Title"
date: 2021-03-10
author: Itzik Ben-Shabat
excerpt: "Brief description"
image: /assets/images/blog/post-image.jpg
tags: [research, 3d-vision]
---
```

**Validation Checklist**:
- [ ] Sample Markdown posts render correctly
- [ ] Blog hero section displays with title, date, author
- [ ] Navigation and footer show correctly
- [ ] Markdown formatting works (bold, links, images, code)
- [ ] Blog post styling matches current design

**Deliverables**:
- Blog post template
- Markdown configuration
- Documentation for writing new posts

---

### Phase 4: Migrate Blog Posts to Markdown (Issue #23)
**Branch**: `feat/11ty-migrate-blog-posts`
**Time Estimate**: 2-3 hours
**Depends On**: Phase 3

**Strategy**: Migrate in batches for easier validation

**Batch 1: Recent Posts (2024-2025)** - ~10 posts
- [ ] Convert HTML to Markdown
- [ ] Extract frontmatter from HTML
- [ ] Verify images/links work
- [ ] Test rendering

**Batch 2: 2022-2023 Posts** - ~20 posts
- [ ] Convert HTML to Markdown
- [ ] Extract frontmatter
- [ ] Verify rendering

**Batch 3: 2020-2021 Posts** - ~20 posts
- [ ] Convert HTML to Markdown
- [ ] Extract frontmatter
- [ ] Verify rendering

**Batch 4: Pre-2020 Posts** - ~24 posts
- [ ] Convert HTML to Markdown
- [ ] Extract frontmatter
- [ ] Verify rendering

**Conversion Script**:
Create Python/Node script to automate:
- Extract title, date from HTML
- Convert HTML body to Markdown
- Create .md files with frontmatter
- Preserve image paths

**Validation Checklist**:
- [ ] All 74 blog posts render correctly
- [ ] Images display properly
- [ ] Links work (internal and external)
- [ ] Dates are correct
- [ ] Blog index page lists all posts
- [ ] Individual post URLs preserved (or redirects set up)

**Deliverables**:
- All blog posts as Markdown files
- Conversion script (for future reference)
- Updated blog index page

---

### Phase 5: Update Blog Index & Collections (Issue #24)
**Branch**: `feat/11ty-blog-collections`
**Time Estimate**: 1 hour
**Depends On**: Phase 4

**Tasks**:
- [ ] Update blog.html to use 11ty collections
- [ ] Generate blog cards from collection data
- [ ] Implement pagination (if needed)
- [ ] Add filtering/search functionality
- [ ] Sort posts by date (newest first)
- [ ] Preserve existing blog grid layout
- [ ] Test with all migrated posts

**Validation Checklist**:
- [ ] Blog index shows all posts
- [ ] Posts are sorted by date (newest first)
- [ ] Blog cards have correct images, titles, excerpts
- [ ] Clicking cards navigates to correct posts
- [ ] Blog layout matches current design

**Deliverables**:
- Dynamic blog index using collections
- Proper sorting and filtering

---

### Phase 6: Cleanup & Optimization (Issue #25)
**Branch**: `feat/11ty-cleanup`
**Time Estimate**: 1 hour
**Depends On**: Phase 5

**Tasks**:
- [ ] Remove old HTML blog post files (blog/posts/*.html)
- [ ] Update .gitignore for _site/ directory
- [ ] Remove duplicate navigation/footer code
- [ ] Verify sitemap generation works with 11ty
- [ ] Update README.md with 11ty instructions
- [ ] Create CONTRIBUTING.md for adding new blog posts
- [ ] Test full build from scratch
- [ ] Verify all 81 URLs still work
- [ ] Check favicon, analytics, SEO tags preserved

**Validation Checklist**:
- [ ] Site builds completely from scratch
- [ ] All 81 pages accessible
- [ ] No broken links
- [ ] Sitemap.xml generated correctly
- [ ] SEO tags intact on all pages
- [ ] Performance is same or better
- [ ] README updated with new workflow

**Deliverables**:
- Clean codebase without duplication
- Updated documentation
- Build process validated

---

## Rollback Plan

**If anything goes wrong**:
1. Each phase is in separate branch
2. Main branch remains untouched until validation
3. Can revert to any previous branch
4. Current working site always available

**Rollback Commands**:
```bash
# If on a broken branch
git checkout main

# If merged but need to revert
git revert <commit-hash>

# Nuclear option (restore to before migration)
git reset --hard <commit-before-migration>
```

---

## Testing Checklist (Before Each Merge)

- [ ] Run `npm run build` successfully
- [ ] All pages render without errors
- [ ] Navigation works on all pages
- [ ] Footer appears on all pages
- [ ] All links functional (internal/external)
- [ ] Images load correctly
- [ ] Dynamic content (publications, news) works
- [ ] Blog posts display correctly
- [ ] SEO tags present (title, meta description)
- [ ] Analytics tracking present
- [ ] Favicon displays
- [ ] Responsive design intact
- [ ] No console errors in browser

---

## Success Criteria

**Migration is complete when**:
1. ✅ All 7 core pages use base template
2. ✅ All 74 blog posts are Markdown
3. ✅ Blog post template works for new posts
4. ✅ No duplicated HTML (nav/footer)
5. ✅ Site builds with `npm run build`
6. ✅ All URLs work (or redirects in place)
7. ✅ Documentation updated
8. ✅ Ready for deployment

**Benefits Achieved**:
- ✅ Single source for nav/footer changes
- ✅ Write blog posts in Markdown (much easier!)
- ✅ Maintainable codebase
- ✅ Template-based architecture
- ✅ Still static HTML output (deployment unchanged)

---

## Next Steps After Migration

1. Deploy to production with new build process
2. Write new blog posts in Markdown
3. Consider adding:
   - RSS feed generation
   - Blog post tags/categories
   - Related posts
   - Reading time estimates

---

**Document Created**: 2026-01-02
**Status**: Planning
**Next Action**: Create Issue #20 for Phase 1
