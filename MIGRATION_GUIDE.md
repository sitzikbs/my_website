# WordPress Content Migration Guide

**Date**: 2025-11-17  
**Purpose**: Step-by-step guide for migrating WordPress content to static site  
**Status**: Ready for use

---

## Overview

This guide provides detailed instructions for extracting content from WordPress and populating the static site structure. The repository is now ready with:

- ✅ Directory structure created
- ✅ Example data files with schema
- ✅ Placeholder blog posts showing structure
- ✅ JSON schemas for publications and blog index

---

## Prerequisites

Before starting, ensure you have:

- [ ] Access to WordPress admin panel at https://itzikbs.com/wp-admin
- [ ] FTP/SFTP access to WordPress server (for media files)
- [ ] WordPress export plugin (optional but recommended)
- [ ] Text editor for editing JSON files
- [ ] Image optimization tools (TinyPNG, ImageOptim, etc.)

---

## Migration Process

### Step 1: Export Blog Posts from WordPress

#### Method A: Using WordPress Export Tool

1. Log into WordPress admin
2. Go to **Tools → Export**
3. Select **Posts** and click **Download Export File**
4. Save the XML file to your computer
5. Use an XML-to-Markdown/HTML converter:
   - [WordPress to Hugo](https://github.com/SchumacherFM/wordpress-to-hugo-exporter)
   - [wordpress-export-to-markdown](https://github.com/lonekorean/wordpress-export-to-markdown)
   - [exitwp](https://github.com/thomasf/exitwp)

#### Method B: Using WP-CLI

```bash
# SSH into WordPress server
ssh user@itzikbs.com

# Export all posts
wp post list --post_type=post --format=json > posts-export.json

# Export full content
wp export --post_type=post --dir=./exports/
```

#### What to Extract per Post

For each blog post, you need:
- Title
- Publication date
- Last modified date
- Author name
- Full content (HTML)
- Excerpt/summary
- Categories
- Tags
- Featured image URL
- All embedded images
- SEO metadata (if available)

---

### Step 2: Convert Blog Posts to HTML

For each WordPress post:

1. **Create new HTML file** in `blog/posts/`:
   ```
   blog/posts/YYYY-MM-DD-post-slug.html
   ```
   Example: `blog/posts/2024-03-15-my-first-post.html`

2. **Copy the template** from `blog/posts/2024-11-15-example-blog-post.html`

3. **Replace placeholder content**:
   - Update `<title>` tag
   - Update meta tags (description, keywords, og tags)
   - Replace post title in `<h1>`
   - Update date in `<time>` tag
   - Update categories and tags
   - Replace post content in `.post-content`

4. **Convert WordPress content**:
   - Remove WordPress shortcodes or convert to HTML
   - Update image paths to point to new location
   - Fix internal links
   - Preserve code blocks with proper syntax
   - Convert embedded videos to HTML5 or iframe

---

### Step 3: Update Blog Index (blog-index.json)

After creating each blog post HTML file:

1. Open `data/blog-index.json`
2. Add a new entry to the `posts` array:

```json
{
  "id": "2024-03-15-my-first-post",
  "title": "My First Post Title",
  "date": "2024-03-15",
  "updated": "2024-03-15",
  "author": "Itzik Ben-Shabat",
  "excerpt": "Brief 2-3 sentence summary of the post...",
  "content": "/blog/posts/2024-03-15-my-first-post.html",
  "categories": ["Category1", "Category2"],
  "tags": ["tag1", "tag2", "tag3"],
  "image": "/assets/images/blog/2024-03-15-featured.jpg",
  "readingTime": 5,
  "featured": false,
  "status": "published"
}
```

3. Update the `categories` array if you added new categories
4. Update the `tags` array with any new tags

---

### Step 4: Download Blog Images

#### Method A: Manual Download from WordPress

1. Go to WordPress admin → **Media Library**
2. Filter by used in posts
3. Download each image
4. Save to appropriate directory:
   - Featured images: `assets/images/blog/YYYY-MM-DD-post-slug-featured.jpg`
   - Inline images: `assets/images/blog/YYYY-MM-DD-post-slug-image-1.jpg`

#### Method B: Bulk Download via SFTP

```bash
# Download entire uploads directory
sftp user@itzikbs.com
get -r /wp-content/uploads/ ./wordpress-media/
```

#### Organize Downloaded Images

```
assets/images/blog/
├── 2024-11-15-example-featured.jpg
├── 2024-11-15-example-img-1.jpg
├── 2024-11-15-example-img-2.jpg
├── 2024-10-20-another-featured.jpg
└── ...
```

#### Optimize Images

Before adding to repository:

```bash
# Using ImageMagick
mogrify -resize 1600x1600\> -quality 85 assets/images/blog/*.jpg

# Or use online tools:
# - TinyPNG.com
# - Squoosh.app
# - ImageOptim (Mac)
```

---

### Step 5: Export Publications Data

#### From WordPress

If publications are in WordPress:

1. Go to WordPress admin
2. Navigate to Publications (or custom post type)
3. Export each publication's data:
   - Title
   - Authors list
   - Venue name
   - Publication year and month
   - Abstract
   - All links (paper PDF, code, project page, video, DOI)
   - BibTeX citation
   - Thumbnail image URL
   - Awards/recognition

#### Update publications.json

1. Open `data/publications.json`
2. Replace example publications with real data:

```json
{
  "id": "unique-slug-2024",
  "title": "Actual Publication Title",
  "authors": [
    "Itzik Ben-Shabat",
    "Co-author Name"
  ],
  "venue": "Conference or Journal Name",
  "venueType": "conference",
  "year": 2024,
  "month": "June",
  "abstract": "Full abstract text here...",
  "keywords": ["keyword1", "keyword2"],
  "links": {
    "paper": "/assets/documents/papers/paper-2024.pdf",
    "project": "https://project-url.com",
    "code": "https://github.com/username/repo",
    "video": "https://youtube.com/watch?v=...",
    "doi": "https://doi.org/...",
    "arxiv": "https://arxiv.org/abs/..."
  },
  "image": "/assets/images/publications/pub-2024-thumb.jpg",
  "bibtex": "@inproceedings{citationkey2024,\n  title={...},\n  author={...},\n  booktitle={...},\n  year={2024}\n}",
  "featured": true,
  "awards": ["Best Paper Award"],
  "tags": ["tag1", "tag2"]
}
```

---

### Step 6: Download Publication Assets

#### Publication PDFs

1. Download all paper PDFs from WordPress
2. Rename consistently: `paper-slug.pdf`, `paper-slug-supplementary.pdf`
3. Save to: `assets/documents/papers/`

#### Publication Images

1. Download thumbnail/teaser images
2. Rename: `pub-slug-thumb.jpg`, `pub-slug-fig1.png`
3. Save to: `assets/images/publications/`
4. Optimize images before adding

---

### Step 7: Extract About/Bio Content

1. Find bio text on WordPress site (usually Homepage or About page)
2. Copy the full bio text
3. Create `data/about.json`:

```json
{
  "name": "Itzik Ben-Shabat",
  "title": "Research Scientist / PhD Student / etc.",
  "affiliation": "Institution Name",
  "shortBio": "2-3 sentence bio for homepage...",
  "fullBio": "Extended bio with multiple paragraphs...",
  "research_interests": [
    "Computer Vision",
    "3D Reconstruction",
    "Deep Learning"
  ],
  "contact": {
    "email": "email@example.com",
    "office": "Office location (if applicable)"
  },
  "social": {
    "github": "https://github.com/sitzikbs",
    "linkedin": "https://linkedin.com/in/...",
    "scholar": "https://scholar.google.com/citations?user=...",
    "twitter": "https://twitter.com/..."
  },
  "cv": "/assets/documents/cv/cv-current.pdf"
}
```

---

### Step 8: Download CV and Other Documents

1. Download current CV from WordPress
2. Save to: `assets/documents/cv/cv-current.pdf`
3. Download any other documents (research statements, etc.)
4. Save to appropriate subdirectories in `assets/documents/`

---

### Step 9: Download Profile/Header Images

1. Download profile photo/headshot
2. Create multiple sizes:
   - Large: 800x800px → `profile-large.jpg`
   - Medium: 400x400px → `profile-medium.jpg`
   - Thumbnail: 200x200px → `profile-thumb.jpg`
3. Save to: `assets/images/profile/`

---

### Step 10: Update Image References

After downloading all images:

1. **In blog posts**: Update all `<img>` src attributes to new paths
2. **In blog-index.json**: Update image paths
3. **In publications.json**: Update image and PDF paths
4. **Verify all paths are correct**

Example path updates:
- Old: `https://itzikbs.com/wp-content/uploads/2024/03/image.jpg`
- New: `/assets/images/blog/2024-03-15-post-slug-image.jpg`

---

### Step 11: Download Icons and General Assets

1. Site logo: Save to `assets/images/general/logo.png`
2. Favicon: Save to `assets/images/general/favicon.ico`
3. Social media icons: Save to `assets/images/icons/`
4. Background images: Save to `assets/images/general/`

---

## Validation Checklist

After completing migration, verify:

- [ ] All blog posts exported and converted to HTML
- [ ] Blog index (blog-index.json) updated with all posts
- [ ] All blog images downloaded and optimized
- [ ] All image paths in blog posts updated
- [ ] Publications data (publications.json) complete
- [ ] All publication PDFs downloaded
- [ ] All publication images downloaded
- [ ] About/bio content extracted
- [ ] Profile images downloaded
- [ ] CV and documents downloaded
- [ ] All internal links working
- [ ] No broken image references
- [ ] JSON files are valid (no syntax errors)

---

## Testing

### Validate JSON Files

```bash
# Check publications.json
cat data/publications.json | python3 -m json.tool > /dev/null
echo "publications.json is valid"

# Check blog-index.json
cat data/blog-index.json | python3 -m json.tool > /dev/null
echo "blog-index.json is valid"
```

### Check for Broken Links

```bash
# Find all image references in blog posts
grep -r "src=" blog/posts/ | grep -o 'src="[^"]*"'

# Verify image files exist
find assets/images/ -type f
```

---

## Common Issues and Solutions

### Issue: WordPress Shortcodes in Content

**Problem**: WordPress shortcodes like `[gallery]`, `[video]` appear in exported content

**Solution**: 
- Convert gallery shortcodes to HTML image grids
- Convert video shortcodes to HTML5 `<video>` or iframe embeds
- Replace custom shortcodes with equivalent HTML

### Issue: Internal Links Point to Old URLs

**Problem**: Links still point to itzikbs.com/old-structure

**Solution**:
- Find and replace old domain with relative paths
- Update internal post links to new structure
- Create redirect map for old URLs

### Issue: Large Image File Sizes

**Problem**: Original images are too large (>1MB each)

**Solution**:
- Compress all images before adding to repo
- Use WebP format with JPG fallback
- Generate responsive image sizes

### Issue: Code Blocks Not Formatted

**Problem**: Code blocks from WordPress lost formatting

**Solution**:
- Wrap code in `<pre><code>` tags
- Add language class for syntax highlighting
- Preserve indentation and line breaks

---

## Tools and Resources

### WordPress Export Tools
- **WordPress built-in**: Tools → Export
- **WP-CLI**: Command-line WordPress management
- **All-in-One WP Migration**: Plugin for complete site export

### Content Conversion Tools
- **wordpress-export-to-markdown**: https://github.com/lonekorean/wordpress-export-to-markdown
- **Jekyll Exporter**: WordPress plugin for Jekyll export
- **HTML to Markdown**: https://github.com/mixmark-io/turndown

### Image Optimization
- **TinyPNG**: https://tinypng.com/
- **Squoosh**: https://squoosh.app/
- **ImageOptim** (Mac): https://imageoptim.com/
- **ImageMagick**: Command-line image processing

### Validation Tools
- **JSONLint**: https://jsonlint.com/
- **HTML Validator**: https://validator.w3.org/
- **Link Checker**: https://validator.w3.org/checklink

---

## Next Steps After Migration

Once all content is migrated:

1. Review all pages for correct formatting
2. Test all links (internal and external)
3. Verify images load correctly
4. Check responsive design on mobile
5. Run accessibility audit
6. Set up redirects from old WordPress URLs
7. Deploy to hosting platform
8. Update DNS to point to new site
9. Monitor for any issues

---

## Support

If you encounter issues during migration:

1. Check this guide for solutions
2. Refer to `/audit` directory documentation
3. Review example files for correct structure
4. Validate JSON syntax
5. Open an issue in the repository

---

**Last Updated**: 2025-11-17  
**Version**: 1.0  
**Status**: Ready for use
