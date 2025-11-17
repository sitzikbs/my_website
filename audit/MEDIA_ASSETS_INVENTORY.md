# Media Assets Inventory

**Document Purpose**: Complete catalog of all media files from WordPress site  
**Date**: 2025-11-17  
**Status**: 📝 Ready for Data Collection

---

## Overview

This document provides a comprehensive inventory of all media assets (images, videos, documents, etc.) hosted on the WordPress website that need to be migrated.

---

## Media Statistics

### Summary
- **Total Media Files**: [#]
- **Total Size**: [GB/MB]
- **Images**: [#] files ([size])
- **PDFs**: [#] files ([size])
- **Videos**: [#] files ([size])
- **Other Documents**: [#] files ([size])

### By Year
- 2024: [#] files ([size])
- 2023: [#] files ([size])
- 2022: [#] files ([size])
- [etc.]

---

## WordPress Media Library Structure

Document the current organization:

```
/wp-content/uploads/
├── 2024/
│   ├── 01/
│   ├── 02/
│   ├── 03/
│   └── ...
├── 2023/
│   └── ...
└── [year]/
    └── [month]/
```

**WordPress Generated Sizes**:
- Original: [typical dimensions]
- Large: [dimensions]
- Medium: [dimensions]  
- Thumbnail: [dimensions]
- Custom sizes: [any custom image sizes]

---

## Images Inventory

### Profile & Personal Images

| Filename | Current Path | Dimensions | Format | Size | Usage | Alt Text | Download Priority |
|----------|--------------|------------|--------|------|-------|----------|-------------------|
| profile-photo.jpg | /uploads/2024/01/ | 800x800 | JPG | 150KB | Homepage, About | [alt] | High |
| profile-photo-large.jpg | /uploads/2024/01/ | 1200x1200 | JPG | 300KB | High-res profile | [alt] | High |
| headshot.png | /uploads/2023/05/ | 600x600 | PNG | 200KB | Contact page | [alt] | High |

**Total Profile Images**: [#]  
**Total Size**: [size]

---

### Publication Images

#### Thumbnails/Teasers

| Filename | Publication | Current Path | Dimensions | Format | Size | Alt Text | Priority |
|----------|-------------|--------------|------------|--------|------|----------|----------|
| pub-2024-teaser.jpg | [Pub Title] | /uploads/2024/03/ | 1200x600 | JPG | 250KB | [alt] | High |
| pub-2023-thumb.png | [Pub Title] | /uploads/2023/09/ | 800x400 | PNG | 180KB | [alt] | High |

**Total Publication Images**: [#]  
**Total Size**: [size]

#### Full Figures/Diagrams

| Filename | Publication | Figure # | Current Path | Dimensions | Format | Size | Description |
|----------|-------------|----------|--------------|------------|--------|------|-------------|
| figure-1.png | [Pub Title] | Fig. 1 | /uploads/2024/03/ | 2000x1500 | PNG | 1.5MB | [Description] |
| diagram-2.svg | [Pub Title] | Fig. 2 | /uploads/2024/03/ | vector | SVG | 50KB | [Description] |

**Total Figure Images**: [#]  
**Total Size**: [size]

---

### Blog Post Images

#### Featured Images

| Post Title | Filename | Current Path | Dimensions | Format | Size | Alt Text | Priority |
|------------|----------|--------------|------------|--------|------|----------|----------|
| [Post 1] | post-1-featured.jpg | /uploads/2024/05/ | 1200x800 | JPG | 300KB | [alt] | Medium |
| [Post 2] | post-2-hero.jpg | /uploads/2024/04/ | 1600x900 | JPG | 450KB | [alt] | Medium |

**Total Featured Images**: [#]  
**Total Size**: [size]

#### Embedded Images

| Post Title | Filename | Current Path | Dimensions | Format | Size | Usage in Post | Priority |
|------------|----------|--------------|------------|--------|------|---------------|----------|
| [Post 1] | screenshot-1.png | /uploads/2024/05/ | 800x600 | PNG | 200KB | Code example | Medium |
| [Post 1] | diagram.svg | /uploads/2024/05/ | vector | SVG | 30KB | Explanation | Medium |

**Total Embedded Images**: [#]  
**Total Size**: [size]

---

### General Site Images

| Filename | Purpose | Current Path | Dimensions | Format | Size | Alt Text | Priority |
|----------|---------|--------------|------------|--------|------|----------|----------|
| logo.png | Site logo | /uploads/2024/01/ | 200x200 | PNG | 20KB | Site logo | High |
| favicon.ico | Browser icon | /root/ | 32x32 | ICO | 5KB | Site icon | High |
| hero-bg.jpg | Homepage background | /uploads/2024/01/ | 1920x1080 | JPG | 500KB | Background | Medium |
| placeholder.png | Default image | /uploads/2023/01/ | 400x300 | PNG | 50KB | Placeholder | Low |

**Total General Images**: [#]  
**Total Size**: [size]

---

### Icons & Graphics

| Filename | Type | Current Path | Dimensions | Format | Size | Usage | Priority |
|----------|------|--------------|------------|--------|------|-------|----------|
| icon-github.svg | Social icon | /uploads/2024/01/ | vector | SVG | 2KB | Footer | Low |
| icon-linkedin.svg | Social icon | /uploads/2024/01/ | vector | SVG | 2KB | Footer | Low |
| icon-email.svg | Contact icon | /uploads/2024/01/ | vector | SVG | 2KB | Contact | Low |

**Total Icons**: [#]  
**Total Size**: [size]

---

## Documents & PDFs

### Publications/Papers

| Filename | Publication | Current Path | Pages | Size | Language | Priority |
|----------|-------------|--------------|-------|------|----------|----------|
| paper-2024.pdf | [Pub Title] | /uploads/2024/03/ | 12 | 5MB | English | High |
| supplementary-2024.pdf | [Pub Title] | /uploads/2024/03/ | 8 | 2MB | English | High |

**Total Paper PDFs**: [#]  
**Total Size**: [size]

---

### CV/Resume

| Filename | Version | Current Path | Pages | Size | Last Updated | Priority |
|----------|---------|--------------|-------|------|--------------|----------|
| cv-current.pdf | Current | /uploads/2024/11/ | 4 | 500KB | 2024-11-01 | High |
| cv-2023.pdf | Archive | /uploads/2023/12/ | 3 | 400KB | 2023-12-15 | Low |
| resume.pdf | Short version | /uploads/2024/11/ | 2 | 300KB | 2024-11-01 | Medium |

**Total CV/Resume Files**: [#]  
**Total Size**: [size]

---

### Other Documents

| Filename | Type | Purpose | Current Path | Size | Format | Priority |
|----------|------|---------|--------------|------|--------|----------|
| research-statement.pdf | Document | Job applications | /uploads/2024/08/ | 800KB | PDF | Medium |
| dataset-info.pdf | Data | Dataset documentation | /uploads/2023/05/ | 1MB | PDF | Low |

**Total Other Documents**: [#]  
**Total Size**: [size]

---

## Video Files

### Locally Hosted Videos

| Filename | Associated Content | Current Path | Duration | Resolution | Format | Size | Priority |
|----------|-------------------|--------------|----------|------------|--------|------|----------|
| demo-video.mp4 | [Publication] | /uploads/2024/03/ | 2:30 | 1920x1080 | MP4 | 50MB | Low |
| tutorial.webm | [Blog Post] | /uploads/2024/05/ | 5:00 | 1280x720 | WebM | 30MB | Low |

**Total Local Videos**: [#]  
**Total Size**: [size]

**Note**: Consider whether to keep locally or use external hosting (YouTube/Vimeo)

---

### Embedded External Videos

| Video Title | Platform | Video ID | Associated Content | Duration | Priority |
|-------------|----------|----------|-------------------|----------|----------|
| [Video Title] | YouTube | [ID] | [Publication] | 3:45 | - |
| [Video Title] | Vimeo | [ID] | [Blog Post] | 2:15 | - |

**Total Embedded Videos**: [#]

**Action**: Verify all video links still work

---

## Audio Files

| Filename | Type | Current Path | Duration | Format | Size | Usage | Priority |
|----------|------|--------------|----------|--------|------|-------|----------|
| [audio file] | [type] | /uploads/... | [dur] | MP3 | [size] | [usage] | [priority] |

**Total Audio Files**: [#]  
**Total Size**: [size]

---

## Other Media Types

### Archives/Zips

| Filename | Contents | Current Path | Size | Usage | Priority |
|----------|----------|--------------|------|-------|----------|
| dataset.zip | Research data | /uploads/2023/07/ | 100MB | Download link | Medium |
| code-samples.zip | Code examples | /uploads/2024/02/ | 5MB | Tutorial | Low |

**Total Archive Files**: [#]  
**Total Size**: [size]

---

### Presentations

| Filename | Event/Purpose | Current Path | Format | Size | Date | Priority |
|----------|---------------|--------------|--------|------|------|----------|
| presentation-2024.pdf | Conference talk | /uploads/2024/06/ | PDF | 10MB | 2024-06-15 | Medium |
| slides.pptx | Workshop | /uploads/2024/03/ | PPTX | 15MB | 2024-03-20 | Low |

**Total Presentation Files**: [#]  
**Total Size**: [size]

---

## Media Organization Plan

### Current Structure Issues

Document any organizational problems:
- [ ] Duplicate files: [List duplicates]
- [ ] Inconsistent naming: [Examples]
- [ ] Multiple versions: [Note versions]
- [ ] Unused files: [List unused media]
- [ ] Missing alt text: [Count]
- [ ] Oversized files: [List files > 1MB]

---

### Proposed New Structure

```
/assets/
├── images/
│   ├── profile/
│   │   ├── profile-main.jpg
│   │   ├── profile-large.jpg
│   │   └── headshot.jpg
│   ├── publications/
│   │   ├── [publication-id]-thumb.jpg
│   │   ├── [publication-id]-fig1.png
│   │   └── [publication-id]-fig2.png
│   ├── blog/
│   │   ├── 2024/
│   │   │   ├── [post-slug]-featured.jpg
│   │   │   ├── [post-slug]-img1.jpg
│   │   │   └── [post-slug]-img2.png
│   │   └── 2023/
│   │       └── ...
│   ├── general/
│   │   ├── logo.png
│   │   ├── hero-background.jpg
│   │   └── placeholder.png
│   └── icons/
│       ├── github.svg
│       ├── linkedin.svg
│       └── email.svg
├── documents/
│   ├── cv/
│   │   ├── cv-current.pdf
│   │   └── resume-short.pdf
│   ├── papers/
│   │   ├── [publication-id]-paper.pdf
│   │   └── [publication-id]-supplementary.pdf
│   └── other/
│       └── ...
├── videos/
│   ├── [video-name].mp4
│   └── [video-name].webm
└── downloads/
    ├── datasets/
    │   └── dataset.zip
    └── code/
        └── code-samples.zip
```

---

## File Naming Conventions

### Images
- **Profile**: `profile-[variant].jpg` (e.g., `profile-main.jpg`, `profile-large.jpg`)
- **Publications**: `[pub-id]-[type]-[number].ext` (e.g., `pub-2024-cvpr-thumb.jpg`, `pub-2024-cvpr-fig1.png`)
- **Blog**: `[YYYY-MM-DD]-[post-slug]-[type].ext` (e.g., `2024-03-15-my-post-featured.jpg`)
- **General**: Descriptive name (e.g., `logo.png`, `hero-background.jpg`)

### Documents
- **Papers**: `[pub-id]-paper.pdf`, `[pub-id]-supplementary.pdf`
- **CV**: `cv-[date].pdf` or `cv-current.pdf`

### Videos
- **Descriptive names**: `[publication-id]-demo.mp4`, `[topic]-tutorial.mp4`

---

## Image Optimization Plan

### Pre-Migration Optimization

For each image, optimize before migration:

1. **Resize if oversized**
   - Max width for publication images: 1200px
   - Max width for blog images: 1600px
   - Profile images: As needed

2. **Compress**
   - JPG: Quality 85%
   - PNG: Use tools like TinyPNG
   - Consider WebP format with fallbacks

3. **Convert formats if beneficial**
   - Large PNGs → JPG (if no transparency needed)
   - Simple graphics → SVG (if possible)
   - Photos → WebP + JPG fallback

4. **Generate responsive sizes**
   - Original (full size)
   - Large (1200px)
   - Medium (800px)
   - Thumbnail (400px)

### Optimization Tools

- [ ] TinyPNG/TinyJPG (online)
- [ ] ImageOptim (Mac)
- [ ] Squoosh (online/CLI)
- [ ] Sharp (Node.js library)
- [ ] ImageMagick (CLI)

---

## Media Download Checklist

### Download Methods

#### Option 1: Direct SFTP/FTP Download
```bash
# Connect to WordPress server
sftp user@itzikbs.com

# Download entire uploads directory
get -r /wp-content/uploads/ ./wordpress-media/
```

#### Option 2: WordPress Plugin
- Use "All-in-One WP Migration" or similar
- Export media library
- Download backup file

#### Option 3: WP-CLI
```bash
# List all media files
wp post list --post_type=attachment --format=json > media-list.json

# Download specific files via scripts
```

#### Option 4: Database + Files
```bash
# Export media metadata from database
wp db export media.sql --tables=wp_posts,wp_postmeta

# Then download files via FTP/SFTP
```

---

### Download Checklist

- [ ] All profile/personal images downloaded
- [ ] All publication images downloaded
- [ ] All blog post images downloaded
- [ ] All site graphics/logos downloaded
- [ ] All icons downloaded
- [ ] All PDF documents downloaded
- [ ] All video files downloaded (or links verified)
- [ ] All downloadable files (zips, datasets) downloaded
- [ ] All presentation files downloaded
- [ ] WordPress generated image sizes handled

---

## Media Migration Steps

### 1. Pre-Migration

- [ ] Complete this inventory
- [ ] Download all media files
- [ ] Create new directory structure
- [ ] Identify duplicate files
- [ ] Identify unused files
- [ ] List files needing optimization

### 2. Processing

- [ ] Rename files according to new convention
- [ ] Organize into new directory structure
- [ ] Optimize all images
- [ ] Generate responsive image sizes
- [ ] Convert formats where beneficial
- [ ] Create WebP versions with fallbacks

### 3. Post-Migration

- [ ] Verify all files copied correctly
- [ ] Update file paths in content
- [ ] Update file paths in JSON data
- [ ] Test all image loading
- [ ] Test all download links
- [ ] Verify all videos play
- [ ] Check alt text for all images
- [ ] Remove unused files

---

## Alt Text Audit

For accessibility, ensure all images have appropriate alt text:

### Images Missing Alt Text
| Filename | Current Location | Suggested Alt Text | Priority |
|----------|------------------|-------------------|----------|
| [file] | [path] | [suggested alt text] | [priority] |

### Images with Poor Alt Text
| Filename | Current Alt Text | Improved Alt Text | Priority |
|----------|------------------|-------------------|----------|
| [file] | [current] | [improved] | [priority] |

**Total Images Needing Alt Text**: [#]

---

## File Size Analysis

### Large Files (> 1MB)

| Filename | Size | Type | Can Be Reduced? | Target Size | Priority |
|----------|------|------|-----------------|-------------|----------|
| [file] | 5MB | JPG | Yes | 500KB | High |
| [file] | 10MB | PDF | Maybe | 5MB | Medium |

**Total Large Files**: [#]  
**Potential Size Reduction**: [MB saved]

---

## External Media Links

### Images Hosted Externally

| Image | External URL | Used In | Reliability | Action Needed |
|-------|--------------|---------|-------------|---------------|
| [img] | [URL] | [location] | High/Low | Download/Keep link |

### Video Platforms

| Video | Platform | URL | Embed Code | Used In | Action |
|-------|----------|-----|------------|---------|--------|
| [video] | YouTube | [URL] | [embed] | [location] | Verify/Update |

---

## Copyright & Licensing

### Third-Party Media

List any media not created by site owner:

| Filename | Source | License | Attribution Required | Usage Rights |
|----------|--------|---------|---------------------|--------------|
| [file] | [source] | [license] | Yes/No | [rights] |

### Original Media

- [ ] All original content - No attribution needed
- [ ] Mixed - Some third-party content (documented above)

---

## Backup Plan

### WordPress Media Backup

1. **Full Backup**
   - Date: [Date of backup]
   - Location: [Where backup stored]
   - Size: [Backup size]
   - Method: [How backed up]

2. **Verification**
   - [ ] Backup completed successfully
   - [ ] File count matches
   - [ ] File sizes verified
   - [ ] Backup tested (sample restore)

---

## Post-Migration URL Updates

### Internal References

Document all places where media URLs need updating:

1. **HTML files**: [Count] references
2. **CSS files**: [Count] background images
3. **JSON data files**: [Count] image paths
4. **JavaScript files**: [Count] image references

### Find & Replace Pattern

```bash
# Old WordPress URLs
https://itzikbs.com/wp-content/uploads/YYYY/MM/filename.ext

# New static URLs
/assets/images/[category]/filename.ext
```

---

## Testing Checklist

After migration, verify:

- [ ] All images display correctly
- [ ] All download links work
- [ ] All videos play/embed correctly
- [ ] Responsive images load appropriately
- [ ] No broken image links (404s)
- [ ] Image lazy loading works
- [ ] Alt text present for all images
- [ ] File sizes reasonable (< 500KB for most)
- [ ] WebP formats with fallbacks working

---

**Status**: 📝 Template Ready - Awaiting Data Collection  
**Next Step**: Access WordPress media library and begin cataloging all files  
**Estimated Time**: [Time estimate based on media count]
