---
name: Fix WordPress Image Links
about: Replace old WordPress CDN URLs with local asset paths
title: 'Fix broken WordPress image links in blog posts'
labels: bug, content, high-priority
assignees: ''

---

## 🐛 Issue Description

Blog posts still contain references to old WordPress image URLs (`http://www.itzikbs.com/wp-content/uploads/...`) instead of local asset paths. This causes:

1. **Mixed content warnings** (HTTP images on HTTPS pages)
2. **Dependency on old hosting** (images may break if old site goes down)
3. **Performance issues** (external requests instead of local assets)
4. **Broken images** if old WordPress site is taken down

## 📍 Affected Pages

Found on blog index page, likely affecting many individual blog posts:
- `http://www.itzikbs.com/wp-content/uploads/2017/11/built_in_option.jpg`
- `http://www.itzikbs.com/wp-content/uploads/2017/02/TensorFlow-Logo-300x54.png`
- `http://www.itzikbs.com/wp-content/uploads/2017/06/netVLAD_Architecture-1024x197.png`
- `http://www.itzikbs.com/wp-content/uploads/2016/12/Capture-1024x380.jpg`

## 🔍 Investigation Needed

1. **Check blog post markdown files** (`blog/posts-md/*.md`)
   - Search for: `http://www.itzikbs.com/wp-content/uploads/`
   - Search for: `http://i0.wp.com/` (WordPress CDN)

2. **Check JSON data files**
   - `data/blog.json`
   - `data/blog-index.json`
   - Look for old URLs in excerpts, content, or image paths

3. **Verify images exist locally**
   - Check if images are in `/assets/images/blog/`
   - Cross-reference with `data/image-mapping.json` if it exists

## ✅ Solution

Replace all old WordPress URLs with local paths:

**From:**
```
http://www.itzikbs.com/wp-content/uploads/2017/11/built_in_option.jpg
```

**To:**
```
/assets/images/blog/built_in_option.jpg
```

Or appropriate WebP version:
```
/assets/images/blog/built_in_option.webp
```

## 🛠️ Implementation Steps

1. **Search and identify** all occurrences:
   ```bash
   grep -r "http://www.itzikbs.com/wp-content" blog/posts-md/
   grep -r "http://i0.wp.com" blog/posts-md/
   grep -r "http://www.itzikbs.com/wp-content" data/
   ```

2. **Create a script** to:
   - Find all WordPress URLs in markdown files
   - Extract image filenames
   - Check if image exists in `/assets/images/blog/`
   - Replace URLs with local paths
   - Prefer WebP versions if available

3. **Manual verification**:
   - Build site and test affected blog posts
   - Verify all images load correctly
   - Check responsive images work

4. **Test thoroughly**:
   - Test blog index page
   - Test individual blog posts
   - Check browser console for errors

## 📊 Impact

**High Priority** - Affects multiple blog posts and could break images if old WordPress hosting is discontinued.

**Estimated affected posts:** Unknown (needs grep search)

## 🔗 Related Files

- `blog/posts-md/*.md` - Blog post markdown files
- `data/blog.json` - Blog data
- `data/blog-index.json` - Blog index data
- `assets/images/blog/` - Local image directory
- `data/image-mapping.json` - Image conversion tracking (if exists)

## 🎯 Acceptance Criteria

- [ ] No HTTP image URLs in blog posts
- [ ] All images use local paths (`/assets/images/blog/...`)
- [ ] No mixed content warnings in browser console
- [ ] All blog post images display correctly
- [ ] WebP versions used where available
- [ ] Responsive images working properly

---

**Browser auto-upgrades HTTP→HTTPS currently**, so images still work, but this is a temporary fix. Need to resolve before old hosting is shut down.
