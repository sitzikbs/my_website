# SEO Implementation Guide

This document outlines the SEO features implemented on this website and how to maintain them.

## Overview

This website implements comprehensive SEO best practices to ensure maximum visibility in search engines and social media platforms.

## Core SEO Features

### 1. Meta Tags

Every page includes essential meta tags configured in the base template (`_includes/layouts/base.njk`):

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{{ description }}">
<meta name="author" content="Itzik Ben-Shabat">
```

**How to set for individual pages:**
```yaml
---
title: Your Page Title
description: Your page description (recommended 150-160 characters)
---
```

### 2. Open Graph Tags (Social Media)

Implemented for Facebook, LinkedIn, and other platforms:

```html
<meta property="og:type" content="website">
<meta property="og:url" content="{{ canonicalUrl }}{{ page.url }}">
<meta property="og:title" content="{{ title }}">
<meta property="og:description" content="{{ description }}">
<meta property="og:image" content="https://www.itzikbs.com/assets/images/profile/Itzik_Ben_Shabat_portrait.jpg">
<meta property="og:site_name" content="Itzik Ben-Shabat">
```

### 3. Twitter Card Tags

Optimized for Twitter sharing:

```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:url" content="{{ canonicalUrl }}{{ page.url }}">
<meta name="twitter:title" content="{{ title }}">
<meta name="twitter:description" content="{{ description }}">
<meta name="twitter:image" content="https://www.itzikbs.com/assets/images/profile/Itzik_Ben_Shabat_portrait.jpg">
```

### 4. Canonical URLs

Every page has a canonical URL to prevent duplicate content issues:

```html
<link rel="canonical" href="{{ canonicalUrl }}{{ page.url }}">
```

**Setting custom canonical URL:**
```yaml
---
canonicalUrl: https://www.itzikbs.com/custom-path/
---
```

### 5. Structured Data (Schema.org)

#### Person Schema (Homepage)

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Itzik Ben-Shabat",
  "url": "https://www.itzikbs.com",
  "image": "https://www.itzikbs.com/assets/images/profile/Itzik_Ben_Shabat_portrait.jpg",
  "jobTitle": "Research Scientist",
  "worksFor": {
    "@type": "Organization",
    "name": "Roblox"
  },
  "alumniOf": [{
    "@type": "Organization",
    "name": "Technion - Israel Institute of Technology"
  }],
  "sameAs": [
    "https://github.com/sitzikbs",
    "https://twitter.com/sitzikbs",
    "https://www.linkedin.com/in/yizhak-itzik-ben-shabat-67b3b1b7/"
  ]
}
```

#### BlogPosting Schema (Blog Posts)

Automatically added to all blog posts via `blog-post.njk` layout:

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{{ title }}",
  "datePublished": "{{ date }}",
  "author": {
    "@type": "Person",
    "name": "{{ author }}",
    "url": "https://www.itzikbs.com"
  },
  "publisher": {
    "@type": "Person",
    "name": "Itzik Ben-Shabat"
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.itzikbs.com{{ page.url }}"
  }
}
```

**Adding custom schema to a page:**
```yaml
---
customSchema: |
  {
    "@context": "https://schema.org",
    "@type": "YourType",
    "property": "value"
  }
---
```

### 6. Sitemap

XML sitemap located at `/sitemap.xml` includes:
- All main pages
- Blog posts
- Publications
- Proper priority values (0.6 to 1.0)
- Last modification dates

**Generating sitemap:**
```bash
python3 scripts/generate_sitemap.py
```

### 7. Robots.txt

Located at `/robots.txt`, properly configured to:
- Allow all search engines
- Block sensitive directories (scripts, reports, .git)
- Reference sitemap location
- Set crawl delay to 1 second

## Page-Specific SEO

### Homepage
- **Priority**: 1.0 (highest)
- **Schema**: Person
- **Title**: "Itzik Ben-Shabat - 3D Computer Vision Research"
- **Description**: General professional summary

### About Page
- **Priority**: 0.8
- **Title**: "About - Itzik Ben-Shabat"
- **Description**: Background and experience

### Publications Page
- **Priority**: 0.8
- **Schema**: Consider adding ScholarlyArticle for individual publications
- **Title**: "Publications - Itzik Ben-Shabat"

### Blog Posts
- **Priority**: 0.6
- **Schema**: BlogPosting (automatic)
- **Title**: From frontmatter
- **Description**: From frontmatter or first paragraph

### Contact Page
- **Priority**: 0.7
- **Title**: "Contact - Itzik Ben-Shabat"

## Heading Hierarchy

All pages follow proper heading hierarchy:

```
h1: Page title (one per page)
├── h2: Main sections
│   ├── h3: Subsections
│   │   └── h4: Sub-subsections
```

**Verify heading hierarchy:**
```bash
python3 scripts/check_heading_hierarchy.py
```

## Image SEO

All images should:
1. Have descriptive alt text
2. Use appropriate file names (descriptive, lowercase, hyphens)
3. Be optimized for web (compressed)
4. Include width and height attributes
5. Use lazy loading (`loading="lazy"`)

**Example:**
```html
<img src="/assets/images/research-paper.jpg" 
     alt="3D point cloud visualization showing surface normals" 
     width="800" 
     height="600" 
     loading="lazy">
```

## Performance Optimization

SEO is closely tied to performance:
- ✅ Minified CSS and JavaScript
- ✅ WebP images with fallbacks
- ✅ Resource hints (preconnect, dns-prefetch)
- ✅ Google Analytics with async loading

## Social Media Optimization

### Preview Testing Tools:
- **Facebook/LinkedIn**: [Sharing Debugger](https://developers.facebook.com/tools/debug/)
- **Twitter**: [Card Validator](https://cards-dev.twitter.com/validator)
- **Google**: [Rich Results Test](https://search.google.com/test/rich-results)

### Image Requirements:
- **Minimum size**: 1200x630px
- **Aspect ratio**: 1.91:1 (Open Graph)
- **Format**: JPG or PNG
- **Max size**: Under 8MB

## Maintenance Checklist

### When Adding New Pages:
- [ ] Add unique title and description in frontmatter
- [ ] Verify heading hierarchy (h1, then h2, etc.)
- [ ] Add to sitemap (regenerate with script)
- [ ] Check all images have alt text
- [ ] Test social media previews
- [ ] Verify canonical URL

### Monthly:
- [ ] Regenerate sitemap with updated dates
- [ ] Check for broken links
- [ ] Review Google Search Console for issues
- [ ] Update schema markup if needed

### When Publishing Blog Posts:
- [ ] Set title and description
- [ ] Add publication date
- [ ] Include featured image with alt text
- [ ] Verify BlogPosting schema renders correctly
- [ ] Share on social media and test preview

## Testing and Validation

### Automated Tools:
```bash
# Check heading hierarchy
python3 scripts/check_heading_hierarchy.py

# Generate sitemap
python3 scripts/generate_sitemap.py

# Check accessibility (includes SEO checks)
python3 scripts/check_accessibility.py
```

### Manual Testing:
1. **Google Search Console**: Monitor indexing and search performance
2. **Schema Validator**: Test structured data
3. **Page Speed Insights**: Check performance metrics
4. **Social Media Validators**: Test Open Graph and Twitter Cards

## Best Practices

### Title Tags:
- Keep under 60 characters
- Include primary keyword
- Make it unique and descriptive
- Format: "Page Title - Itzik Ben-Shabat"

### Meta Descriptions:
- Keep between 150-160 characters
- Include call-to-action
- Accurately describe page content
- Include relevant keywords naturally

### URLs:
- Use lowercase
- Use hyphens (not underscores)
- Keep short and descriptive
- Include relevant keywords

### Content:
- Use semantic HTML
- Write for humans first, search engines second
- Include relevant keywords naturally
- Keep content fresh and updated
- Use descriptive link text (avoid "click here")

## Resources

- [Google Search Central](https://developers.google.com/search)
- [Schema.org Documentation](https://schema.org/)
- [Open Graph Protocol](https://ogp.me/)
- [Twitter Cards Documentation](https://developer.twitter.com/en/docs/twitter-for-websites/cards)
- [Moz SEO Learning Center](https://moz.com/learn/seo)

## Questions?

For questions about SEO implementation, refer to:
- This documentation
- Base template: `_includes/layouts/base.njk`
- Blog post template: `_includes/layouts/blog-post.njk`
- Scripts directory: `/scripts/`
