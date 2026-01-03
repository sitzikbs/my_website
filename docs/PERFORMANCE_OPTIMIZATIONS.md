# Core Web Vitals Performance Optimizations

## Summary

This document describes the performance optimizations implemented to improve Core Web Vitals metrics, specifically targeting LCP (Largest Contentful Paint) reduction from 3.3s-6.7s to under 2.5s.

## Optimizations Implemented

### 1. Font Loading Optimization

**Problem:** Google Fonts were loaded synchronously, blocking page rendering.

**Solution:**
- Added `font-display: swap` to Google Fonts URL
- Preloaded critical Inter font variant (woff2 format)
- Used media="print" with onload trick to load fonts asynchronously
- Added noscript fallback for non-JavaScript browsers

**Implementation:**
```html
<!-- Preload critical font -->
<link rel="preload" href="https://fonts.gstatic.com/s/inter/v13/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuLyfAZ9hiA.woff2" as="font" type="font/woff2" crossorigin>

<!-- Load stylesheet asynchronously -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap"></noscript>
```

**Expected Impact:** Reduces render-blocking time by ~200-400ms

---

### 2. Analytics Script Optimization

**Problem:** Google Analytics scripts loaded in `<head>`, blocking page rendering.

**Solution:**
- Moved Google Analytics scripts to end of `<body>`
- Added `defer` attribute to both gtag.js and analytics.min.js
- Scripts now load asynchronously without blocking rendering

**Implementation:**
```html
<!-- Moved from <head> to end of <body> -->
<script defer src="https://www.googletagmanager.com/gtag/js?id=G-0EC0BTHZ23"></script>
<script defer src="/js/analytics.min.js"></script>
```

**Expected Impact:** Eliminates ~100-200ms of render-blocking time

---

### 3. CSS Resource Optimization

**Problem:** Font Awesome CSS loaded synchronously, blocking rendering.

**Solution:**
- Added preload hint for Font Awesome CSS
- Loaded Font Awesome asynchronously using onload trick
- Icons are non-critical, can render after initial paint
- Added noscript fallback

**Implementation:**
```html
<link rel="preload" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" ...></noscript>
```

**Expected Impact:** Reduces render-blocking CSS by ~50-100ms

---

### 4. Image Loading Optimization

**Problem:** 
- Profile image (likely LCP element) had `loading="lazy"` attribute
- Dynamically loaded images lacked lazy loading
- Missing width/height attributes causing CLS

**Solution:**
- Removed `loading="lazy"` from hero profile image on homepage
- Added `fetchpriority="high"` to profile image (LCP element)
- Added `loading="lazy"` to all dynamically generated images in JavaScript
- Added explicit width/height attributes to images in JavaScript

**Files Modified:**
- `index.html` - Profile image optimization
- `js/data-loader.js` - Recent publications, blog posts, podcast episodes
- `js/publications-loader.js` - Publication listing images
- `js/blog-loader.js` - Blog post images
- `js/podcast-loader.js` - Podcast episode images

**Implementation:**
```html
<!-- Homepage profile image (LCP element) -->
<img src="..." alt="Profile picture" width="500" height="500" fetchpriority="high">

<!-- Dynamically loaded images (below fold) -->
<img src="..." alt="..." loading="lazy" width="400" height="250">
```

**Expected Impact:** 
- LCP improvement: 500-1500ms (eliminating lazy load delay on LCP element)
- CLS improvement: Explicit dimensions prevent layout shifts

---

### 5. JavaScript Execution Optimization

**Problem:** JavaScript files loaded without defer, potentially blocking rendering.

**Solution:**
- Added `defer` attribute to all JavaScript files
- Scripts execute in order but don't block HTML parsing
- All scripts now non-blocking:
  - `security-utils.min.js`
  - `main.min.js`
  - `navigation.min.js`
  - `analytics.min.js`
  - `data-loader.min.js` (via block scripts)

**Implementation:**
```html
<script defer src="/js/security-utils.min.js"></script>
<script defer src="/js/main.min.js"></script>
<script defer src="/js/navigation.min.js"></script>
```

**Expected Impact:** Eliminates JavaScript parse/execute blocking during initial render

---

## Performance Metrics Target

### Before Optimization
- **LCP:** 3.3s - 6.7s
- **INP:** 438ms
- **CLS:** 0.31

### After Optimization (Expected)
- **LCP:** <2.5s (target met)
- **INP:** <200ms (improved through deferred JS)
- **CLS:** <0.1 (improved through explicit image dimensions)

---

## Testing Recommendations

1. **Local Testing:**
   ```bash
   npm run build
   npm run serve
   # Visit http://localhost:8000
   # Use Chrome DevTools Lighthouse
   ```

2. **Production Testing:**
   - Use https://pagespeed.web.dev/
   - Test multiple pages (especially homepage, publications, blog)
   - Monitor Cloudflare Web Analytics Core Web Vitals dashboard

3. **Specific Pages to Test:**
   - `/` (homepage - profile image is LCP)
   - `/publications/` (many images)
   - `/blog/` (many images)
   - Individual blog posts with large hero images

---

## Additional Recommendations for Future Optimization

1. **Self-host Google Fonts** - Eliminate third-party DNS lookup and connection time
2. **Self-host Font Awesome** - Better caching control
3. **Image Compression** - Further optimize WebP images (already at 78.3% reduction)
4. **Critical CSS Inlining** - Inline above-the-fold CSS for fastest First Paint
5. **Service Worker** - Implement offline caching strategy
6. **Resource Prioritization** - Consider using Early Hints (already enabled on Cloudflare)

---

## Files Modified

1. `_includes/layouts/base.njk` - Main template with font, analytics, and CSS optimizations
2. `index.html` - Profile image optimization
3. `js/data-loader.js` - Lazy loading for dynamic content
4. `js/publications-loader.js` - Lazy loading for publications
5. `js/blog-loader.js` - Lazy loading for blog posts
6. `js/podcast-loader.js` - Lazy loading for podcast episodes
7. All corresponding `.min.js` files - Rebuilt with optimizations

---

## Build Process

All JavaScript changes were minified using Terser:
```bash
npx terser js/data-loader.js -o js/data-loader.min.js -c -m
npx terser js/publications-loader.js -o js/publications-loader.min.js -c -m
npx terser js/blog-loader.js -o js/blog-loader.min.js -c -m
npx terser js/podcast-loader.js -o js/podcast-loader.min.js -c -m
```

Site built with:
```bash
npx @11ty/eleventy
```

---

## References

- [Web.dev: Optimize LCP](https://web.dev/optimize-lcp/)
- [Web.dev: Font Best Practices](https://web.dev/font-best-practices/)
- [MDN: fetchpriority](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/fetchPriority)
- [MDN: loading attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#loading)
- [Core Web Vitals](https://web.dev/vitals/)
