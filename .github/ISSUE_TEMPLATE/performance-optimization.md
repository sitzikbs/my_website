---
name: Performance Optimization
about: Investigate and optimize page load times for slow pages
title: 'Investigate and optimize Core Web Vitals - slow page load times'
labels: performance, enhancement
assignees: ''

---

## Issue Description

Cloudflare Web Analytics shows some pages have slower Core Web Vitals, particularly LCP (Largest Contentful Paint).

## Current Performance Metrics

From Web Analytics dashboard (as of Jan 2, 2026):
- **Average page load time:** 4,258ms
- **LCP ranges:** 3.3s - 6.7s
- **Slower pages identified:**
  - `/israel-maritime-vlsi...`
  - `/tensorflow-deep-m...`
  - Other research/blog pages

## Areas to Investigate

1. **Image optimization:**
   - Are all images using WebP format?
   - Are image dimensions appropriate?
   - Consider lazy loading for below-fold images
   - Check if responsive images are working properly

2. **Font loading:**
   - Font loading strategy (swap, optional, etc.)
   - Consider font subsetting if using custom fonts

3. **JavaScript:**
   - Check if any render-blocking JS
   - Consider deferring non-critical JS
   - Review analytics script impact

4. **CSS:**
   - Check for render-blocking CSS
   - Consider critical CSS inlining for above-fold content

5. **Third-party resources:**
   - Review impact of external embeds (YouTube, Twitter, etc.)
   - Consider lazy loading for embeds

## Goals

- **LCP:** Under 2.5s (currently 3.3s-6.7s)
- **INP:** Under 200ms (currently 438ms - needs improvement)
- **CLS:** Under 0.1 (currently 0.31 - needs improvement)

## Resources

- Cloudflare Web Analytics: Dashboard → Core Web Vitals
- Test tools:
  - https://pagespeed.web.dev
  - https://www.webpagetest.org
  - Chrome DevTools Lighthouse

## Notes

- Site is already optimized with:
  - WebP images (78.3% size reduction achieved)
  - Minified CSS/JS
  - Cloudflare caching and CDN
  - Early Hints enabled
- Focus on identifying specific bottlenecks causing slow LCP on certain pages
