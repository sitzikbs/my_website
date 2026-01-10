# Manual Test Plan - Rich Results Validation

## Overview

This document provides step-by-step instructions for manually testing all structured data on the website using Google's Rich Results Test tool.

---

## Prerequisites

- [ ] Site has been built: `npm run build`
- [ ] All files are in `_site/` directory
- [ ] Access to: https://search.google.com/test/rich-results
- [ ] Access to: https://validator.schema.org/ (backup validator)

---

## Test 1: Blog Post - Article Rich Results ✅ (Expected to Pass)

### Purpose
Verify that blog posts generate Article/BlogPosting rich results with all required fields.

### Test Steps

1. **Select a blog post to test**
   ```bash
   # Choose a recent post
   cat _site/blog/posts/2024-06-26-cvpr2024.html
   ```

2. **Copy entire HTML content**
   - Select all content (Ctrl+A / Cmd+A)
   - Copy to clipboard (Ctrl+C / Cmd+C)

3. **Open Google Rich Results Test**
   - Navigate to: https://search.google.com/test/rich-results
   - Click the "CODE" tab

4. **Paste HTML and test**
   - Paste the entire HTML content
   - Click "TEST CODE" button
   - Wait for analysis to complete (10-30 seconds)

### Expected Results

✅ **PASS Criteria:**
- Message: "Page is eligible for rich results"
- Detected item: "Article" or "BlogPosting"
- Preview shows:
  - Article headline
  - Publication date
  - Author name (Itzik Ben-Shabat)
  - Featured image (if present)
  - Publisher information

✅ **Required Fields Present:**
- `headline` ✓
- `datePublished` ✓
- `author` (Person with name) ✓

✅ **Recommended Fields Present:**
- `image` ✓
- `publisher` ✓
- `dateModified` ✓

### If Test Fails

❌ **No rich results detected:**
- Run schema validator: `uv run python scripts/validate_schema.py _site/blog/posts/2024-06-26-cvpr2024.html`
- Check if `<script type="application/ld+json">` tag is present in HTML
- Verify JSON is valid (no syntax errors)

❌ **Missing required fields:**
- Check blog post front matter has all required fields
- Rebuild: `npm run build`
- Test again

### Additional Blog Posts to Test

Test at least 2-3 more blog posts to ensure consistency:
- [ ] `_site/blog/posts/2024-06-16-career_update_2024.html`
- [ ] `_site/blog/posts/2023-07-19-cvpr-2023.html`
- [ ] `_site/blog/posts/2022-01-15-the-talking-papers-podcast.html`

---

## Test 2: About Page - Person Rich Results ⚠️ (May Pass)

### Purpose
Verify that the About page generates Person rich results. Profile/about pages have better eligibility than homepages.

### Test Steps

1. **Get About page HTML**
   ```bash
   cat _site/about/index.html
   ```

2. **Copy entire HTML content**
   - Select all content (Ctrl+A / Cmd+A)
   - Copy to clipboard (Ctrl+C / Cmd+C)

3. **Open Google Rich Results Test**
   - Navigate to: https://search.google.com/test/rich-results
   - Click the "CODE" tab

4. **Paste HTML and test**
   - Paste the entire HTML content
   - Click "TEST CODE" button
   - Wait for analysis to complete

### Expected Results - Scenario A (Ideal)

✅ **PASS Criteria:**
- Message: "Page is eligible for rich results"
- Detected item: "Person"
- Preview shows:
  - Name: "Itzik Ben-Shabat"
  - Alternate name: "Yizhak Ben-Shabat"
  - Job title: "Research Scientist"
  - Organization: "Roblox"
  - Profile photo
  - Social media links

✅ **Schema Structure:**
- ProfilePage contains:
  - `mainEntity` → Person with all details
  - Full Person schema nested inside ProfilePage

### Expected Results - Scenario B (Also Valid)

⚠️ **Valid but not eligible:**
- Message: "No rich results detected" or "Valid schema but not eligible"
- Schema.org validator shows valid Person schema
- This is acceptable - the data is still valuable for:
  - Knowledge Graph
  - Entity recognition
  - Search understanding

### Verification Steps

1. **Verify Person schema exists**
   ```bash
   uv run python scripts/extract_schema.py _site/about/index.html
   ```
   
   Should show Person entity with:
   - name, alternateName
   - description
   - image (ImageObject)
   - jobTitle, worksFor
   - alumniOf
   - knowsAbout
   - sameAs (social profiles)

2. **Validate with Schema.org**
   - Copy JSON-LD output from above command
   - Go to: https://validator.schema.org/
   - Paste and validate
   - Should show no errors

### If Test Shows "No Rich Results"

✓ **This is acceptable!** Person rich results on about pages are:
- Valid structured data ✓
- May or may not show rich results (Google's discretion)
- Still valuable for Knowledge Graph and entity recognition
- Not a failure of implementation

### If Test Fails Completely

❌ **Schema errors:**
- Run: `uv run python scripts/validate_schema.py _site/about/index.html`
- Check for JSON syntax errors
- Verify Person schema is nested inside ProfilePage.mainEntity

❌ **Missing fields:**
- Verify all fields present in about.html front matter
- Rebuild: `npm run build`
- Test again

---

## Test 3: Homepage - Person + WebSite Schema ℹ️ (Not Expected to Show Rich Results)

### Purpose
Verify that homepage has valid Person and WebSite schemas, even though they won't show as rich results.

### Test Steps

1. **Get Homepage HTML**
   ```bash
   cat _site/index.html
   ```

2. **Copy entire HTML content**
   - Select all content
   - Copy to clipboard

3. **Open Google Rich Results Test**
   - Navigate to: https://search.google.com/test/rich-results
   - Click "CODE" tab
   - Paste HTML
   - Click "TEST CODE"

### Expected Results

⚠️ **Expected: "No rich results detected"**

This is **CORRECT** and **EXPECTED**. Homepages typically don't show Person rich results.

### Verification Steps

1. **Verify schemas are valid**
   ```bash
   uv run python scripts/validate_schema.py _site/index.html
   ```
   
   Should show:
   - ✓ Person schema: All required fields present
   - ✓ WebSite schema: All required fields present
   - 0 errors

2. **Verify schemas exist**
   ```bash
   uv run python scripts/extract_schema.py _site/index.html
   ```
   
   Should show @graph with:
   - Person entity (with all fields)
   - WebSite entity

3. **Validate with Schema.org**
   - Copy JSON-LD from extract command
   - Test at: https://validator.schema.org/
   - Should validate with no errors

### Success Criteria

✅ **PASS if:**
- Google test shows "No rich results detected" (expected)
- Local validation shows 0 errors
- Schema.org validator shows valid schemas
- Both Person and WebSite schemas present in @graph

❌ **FAIL if:**
- Local validation shows errors
- Schema.org validator shows syntax errors
- Schemas are missing from HTML

### Why This is Acceptable

The homepage Person schema is **valid and valuable** even without rich results:
- ✓ Helps Google understand site ownership
- ✓ Enables Knowledge Graph eligibility
- ✓ Improves entity recognition across the web
- ✓ Enhances social media sharing
- ✓ Future-proofing for when Google expands support

---

## Test 4: Breadcrumb Navigation - All Sub-Pages 🔵 (Expected to Pass)

### Purpose
Verify that breadcrumb structured data is present on all sub-pages and may enable breadcrumb rich results in search.

### Pages to Test

Test breadcrumbs on at least one page from each type:
- [ ] Publications: `_site/publications/index.html`
- [ ] Blog Index: `_site/blog/index.html`
- [ ] Podcast: `_site/podcast/index.html`
- [ ] Code: `_site/code/index.html`
- [ ] Contact: `_site/contact/index.html`
- [ ] About: `_site/about/index.html` (already tested above)

### Test Steps (For Each Page)

1. **Get page HTML**
   ```bash
   # Example for publications
   cat _site/publications/index.html
   ```

2. **Copy and test in Google Rich Results Test**
   - Navigate to: https://search.google.com/test/rich-results
   - Click "CODE" tab
   - Paste HTML
   - Click "TEST CODE"

### Expected Results

✅ **PASS if shows:**
- "Breadcrumb" rich result detected
- Preview shows navigation path: Home → [Page Name]
- Or: "Valid schema but may not show rich results" (also acceptable)

⚠️ **ACCEPTABLE if shows:**
- Primary schema (Blog, CollectionPage, PodcastSeries, etc.)
- Breadcrumb in "Other valid schema" section
- "No rich results detected" but schema validates locally

### Verification Steps

1. **Verify BreadcrumbList exists**
   ```bash
   # Example for publications
   uv run python scripts/extract_schema.py _site/publications/index.html | grep -A 15 "BreadcrumbList"
   ```

2. **Validate all breadcrumbs at once**
   ```bash
   uv run python scripts/validate_schema.py _site/
   ```
   
   Should show:
   - ✓ BreadcrumbList on all sub-pages
   - 0 errors

### Success Criteria

✅ **PASS if:**
- BreadcrumbList schema present on all sub-pages
- Each has correct hierarchy: Home → Page Name
- Position numbers are sequential (1, 2)
- Home item has URL, last item may not have URL

---

## Test 5: Publications Page - CollectionPage Schema ℹ️ (Not Rich Result Eligible)

### Purpose
Verify publications page has valid CollectionPage schema. Not expected to show rich results but schema should be valid.

### Test Steps

1. **Get Publications page**
   ```bash
   cat _site/publications/index.html
   ```

2. **Test in Google Rich Results Test**
   - Paste into: https://search.google.com/test/rich-results
   - Click "TEST CODE"

### Expected Results

⚠️ **Expected: "No rich results detected"** or breadcrumb only

This is **CORRECT** - CollectionPage is not a rich result type.

### Verification

```bash
uv run python scripts/validate_schema.py _site/publications/index.html
```

Should show:
- ✓ CollectionPage: All required fields present
- ✓ BreadcrumbList: All required fields present
- 0 errors

### Success Criteria

✅ **PASS if:**
- No errors in validation
- CollectionPage + BreadcrumbList both present
- Google test shows valid schema (even if no rich results)

---

## Test 6: Podcast Page - PodcastSeries Schema ℹ️ (Limited Support)

### Purpose
Verify podcast page has valid PodcastSeries schema.

### Test Steps

1. **Get Podcast page**
   ```bash
   cat _site/podcast/index.html
   ```

2. **Test in Google Rich Results Test**
   - Paste into: https://search.google.com/test/rich-results
   - Click "TEST CODE"

### Expected Results

⚠️ **Expected: Limited or no rich results**

PodcastSeries has limited Google support.

### Verification

```bash
uv run python scripts/validate_schema.py _site/podcast/index.html
```

Should show:
- ✓ PodcastSeries: All required fields present
- ✓ BreadcrumbList: All required fields present
- 0 errors

### Success Criteria

✅ **PASS if:**
- Schemas validate locally
- No errors
- PodcastSeries has: name, url, author, genre

---

## Complete Test Summary Checklist

### Quick Validation (Run First)

```bash
# Validate all pages at once
npm run build
uv run python scripts/validate_schema.py _site/

# Should show:
# - 88 passed schemas
# - 0 errors
```

If this passes, your structured data is technically correct!

### Individual Page Testing

Priority order for manual testing:

1. **High Priority - Expected Rich Results**
   - [ ] Blog post (2024-06-26-cvpr2024) - Should show Article ✅
   - [ ] Another blog post - Should show Article ✅
   - [ ] About page - May show Person ⚠️

2. **Medium Priority - Breadcrumb Testing**
   - [ ] Publications page - Check breadcrumb
   - [ ] Blog index - Check breadcrumb
   - [ ] Podcast page - Check breadcrumb

3. **Low Priority - Valid But Not Rich Results**
   - [ ] Homepage - Verify valid (won't show rich results)
   - [ ] Code page - Verify valid + breadcrumb
   - [ ] Contact page - Verify valid + breadcrumb

### After Testing

Record results:

| Page | Google Test Result | Schema Valid | Rich Result? | Notes |
|------|-------------------|--------------|--------------|-------|
| Blog Post #1 | | | | |
| Blog Post #2 | | | | |
| About | | | | |
| Homepage | | | | |
| Publications | | | | |
| Blog Index | | | | |
| Podcast | | | | |
| Code | | | | |
| Contact | | | | |

---

## Troubleshooting Guide

### Problem: "No rich results detected" for blog posts

**Check:**
1. Is BlogPosting schema present? `grep "BlogPosting" _site/blog/posts/*.html`
2. Does it have headline, author, datePublished?
3. Rebuild: `npm run build`
4. Test different blog post

### Problem: Validation script shows errors

**Fix:**
1. Read error message carefully
2. Check which field is missing
3. Verify in source HTML file front matter
4. Rebuild and retest

### Problem: JSON syntax error in Google test

**Fix:**
1. Run: `uv run python scripts/extract_schema.py [file]`
2. Copy JSON to validator: https://jsonlint.com/
3. Fix syntax error in source file
4. Rebuild

### Problem: Schema.org validator fails

**Check:**
1. Copy exact error message
2. Look for:
   - Missing required fields
   - Wrong @type
   - Invalid property names
3. Compare against working example
4. Fix and rebuild

---

## Post-Deployment Testing

After deploying to production:

### Week 1: Initial Monitoring

1. **Submit to Search Console**
   - Go to: https://search.google.com/search-console
   - Submit sitemap
   - Request indexing for:
     - Homepage
     - About page
     - 2-3 recent blog posts

2. **Monitor Structured Data Report**
   - Check "Enhancements" → "Structured Data"
   - Look for:
     - Number of pages with valid markup
     - Any errors or warnings
     - Types of rich results detected

### Week 2-4: Results Monitoring

1. **Check Rich Results Performance**
   - Search Console → Performance
   - Filter by "Appearance: Rich results"
   - Monitor:
     - Impressions (how often shown)
     - Clicks
     - CTR (click-through rate)
     - Average position

2. **Manual Search Tests**
   - Search: `site:itzikbs.com cvpr`
   - Check if blog posts show rich results
   - Search: `Itzik Ben-Shabat`
   - Check if Knowledge Graph appears

### Month 2-3: Long-term Monitoring

- Continue monitoring Search Console
- Track any changes in rich result impressions
- Note any new rich result types appearing
- Watch for schema-related errors

---

## Success Metrics

### Technical Success (Immediate)

✅ All schemas validate with 0 errors
✅ Blog posts show Article rich results
✅ About page has complete Person schema
✅ All pages have appropriate structured data

### SEO Success (1-3 months)

📈 Clean structured data report in Search Console
📈 Blog posts showing as rich results in search
📈 Potential Knowledge Graph appearance
📈 Improved click-through rates
📈 Better search visibility

---

## Documentation References

- **Testing Tools**:
  - [Google Rich Results Test](https://search.google.com/test/rich-results)
  - [Schema.org Validator](https://validator.schema.org/)
  - [JSON Validator](https://jsonlint.com/)

- **Google Documentation**:
  - [Person Rich Results](https://developers.google.com/search/docs/appearance/structured-data/person)
  - [Article Rich Results](https://developers.google.com/search/docs/appearance/structured-data/article)
  - [Breadcrumb Rich Results](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb)

- **Local Validation**:
  ```bash
  # Validate all
  uv run python scripts/validate_schema.py _site/
  
  # Extract for testing
  uv run python scripts/extract_schema.py _site/[page].html
  ```

---

**Last Updated**: 2026-01-09  
**PR**: #148 - Enhance rich result test for compliance on home page  
**Status**: Ready for manual testing
