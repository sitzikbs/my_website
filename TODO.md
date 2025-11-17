# Website Conversion Plan: WordPress to Pure HTML/CSS/JavaScript

## Overview
Convert the current WordPress-based personal website (https://itzikbs.com/) to a modern, lightweight, pure HTML/CSS/JavaScript implementation. The goal is to eliminate WordPress dependencies while maintaining all existing content and improving the design inspired by clean academic websites like https://www.vincentsitzmann.com/.

---

## Phase 1: Project Setup & Planning ✓

### 1.1 Repository Structure
- [ ] Create main project directories:
  - [ ] `/css` - All stylesheets
  - [ ] `/js` - JavaScript files
  - [ ] `/assets` - Images, fonts, icons
  - [ ] `/blog` - Blog posts (HTML or markdown)
  - [ ] `/publications` - Publications data and templates
  - [ ] `/data` - JSON files for dynamic content
- [ ] Set up `.gitignore` for unnecessary files
- [ ] Create `package.json` if using build tools (optional)

### 1.2 Documentation
- [ ] Create comprehensive README.md with:
  - [ ] Project description and structure
  - [ ] Local development setup instructions
  - [ ] How to add new blog posts
  - [ ] How to add new publications
  - [ ] How to deploy the site
  - [ ] Contribution guidelines

---

## Phase 2: Content Extraction from WordPress

### 2.1 Audit Current Website
- [ ] Catalog all existing pages on itzikbs.com:
  - [ ] Homepage/About
  - [ ] Publications page
  - [ ] Blog posts (list all posts)
  - [ ] Any other pages
- [ ] Document all static content (bio, CV, contact info)
- [ ] Extract all images and media files
- [ ] Document navigation structure
- [ ] Note any special features or widgets

### 2.2 Content Migration
- [ ] Export WordPress content:
  - [ ] All blog posts (with metadata: date, tags, categories)
  - [ ] Publications list with details
  - [ ] About/bio text
  - [ ] Media library (images, PDFs, etc.)
- [ ] Convert blog posts to:
  - [ ] HTML files, or
  - [ ] Markdown files (if using a static site generator approach)
- [ ] Create structured data files:
  - [ ] `publications.json` with all publication details
  - [ ] `blog-index.json` with blog post metadata
- [ ] Download and organize all media assets

---

## Phase 3: Design System & Core Structure

### 3.1 Design Research
- [ ] Analyze vincentsitzmann.com design elements:
  - [ ] Typography choices
  - [ ] Color palette
  - [ ] Layout patterns
  - [ ] Navigation style
  - [ ] Responsive breakpoints
- [ ] Define design system:
  - [ ] Color scheme (primary, secondary, accent colors)
  - [ ] Typography scale (font families, sizes, weights)
  - [ ] Spacing system (margins, padding)
  - [ ] Component styles (buttons, links, cards)

### 3.2 CSS Architecture
- [ ] Create base stylesheet structure:
  - [ ] `reset.css` or `normalize.css` - Browser normalization
  - [ ] `variables.css` - CSS custom properties (colors, fonts, spacing)
  - [ ] `base.css` - Global styles
  - [ ] `layout.css` - Layout utilities and grid system
  - [ ] `components.css` - Reusable component styles
  - [ ] `responsive.css` - Media queries
- [ ] Implement responsive design:
  - [ ] Mobile-first approach
  - [ ] Tablet breakpoint (~768px)
  - [ ] Desktop breakpoint (~1024px)
  - [ ] Large desktop breakpoint (~1440px)

### 3.3 HTML Templates
- [ ] Create base template structure:
  - [ ] Header with navigation
  - [ ] Footer with links and copyright
  - [ ] Main content area
- [ ] Design page templates:
  - [ ] `index.html` - Homepage template
  - [ ] `publication-page.html` - Publications listing template
  - [ ] `blog-index.html` - Blog listing template
  - [ ] `blog-post.html` - Individual blog post template
  - [ ] `404.html` - Error page

---

## Phase 4: Core Pages Implementation

### 4.1 Homepage
- [ ] Create `index.html` with:
  - [ ] Hero section with name and title
  - [ ] Professional photo/headshot
  - [ ] Brief bio/introduction
  - [ ] Key research areas or expertise
  - [ ] Links to publications, blog, social media
  - [ ] Contact information or contact form
- [ ] Implement responsive layout
- [ ] Add smooth scrolling and animations (optional)
- [ ] Optimize images for web

### 4.2 Publications Page
- [ ] Design publication entry format:
  - [ ] Title, authors, venue, year
  - [ ] Abstract (collapsible or full)
  - [ ] Links (paper PDF, project page, code, video, etc.)
  - [ ] Thumbnail/teaser image
  - [ ] BibTeX citation (collapsible)
- [ ] Implement `publications.html`:
  - [ ] Load publications from `data/publications.json`
  - [ ] Display publications in reverse chronological order
  - [ ] Group by year (optional)
  - [ ] Filter/search functionality (optional)
  - [ ] Highlight selected or featured publications
- [ ] Create JavaScript to dynamically render publications
- [ ] Style publication cards/entries

### 4.3 Blog Section
- [ ] Create `blog/index.html`:
  - [ ] List all blog posts
  - [ ] Show post preview (title, date, excerpt, featured image)
  - [ ] Pagination or "Load More" functionality
  - [ ] Search/filter by tags or categories
- [ ] Individual blog post template:
  - [ ] Post title and metadata (date, author, tags)
  - [ ] Full post content with proper formatting
  - [ ] Code syntax highlighting (if needed)
  - [ ] Image galleries (if needed)
  - [ ] Previous/Next post navigation
  - [ ] Comments section (consider alternatives like Disqus, utterances, or remove)
- [ ] Create blog post generator script (optional):
  - [ ] Template for new posts
  - [ ] Automatic index update

---

## Phase 5: JavaScript Functionality

### 5.1 Navigation
- [ ] Implement responsive navigation:
  - [ ] Mobile hamburger menu
  - [ ] Smooth scrolling to sections
  - [ ] Active page/section highlighting
  - [ ] Sticky/fixed header (optional)

### 5.2 Dynamic Content Loading
- [ ] Create `publications.js`:
  - [ ] Fetch and parse `publications.json`
  - [ ] Render publication entries dynamically
  - [ ] Implement filtering/sorting
- [ ] Create `blog.js`:
  - [ ] Fetch blog post index
  - [ ] Render blog post previews
  - [ ] Implement pagination
  - [ ] Handle search/filter

### 5.3 Interactive Features
- [ ] Implement dark mode toggle (optional but recommended)
- [ ] Add search functionality
- [ ] Implement "back to top" button
- [ ] Add lazy loading for images
- [ ] Implement smooth animations and transitions
- [ ] Add analytics tracking (Google Analytics, Plausible, etc.)

### 5.4 Forms and Contact
- [ ] Create contact form (if applicable):
  - [ ] Form validation
  - [ ] Integration with email service (Formspree, Netlify Forms, etc.)
  - [ ] Success/error messages

---

## Phase 6: Content Management & Updates

### 6.1 Publication Management
- [ ] Create structured `publications.json` format:
  ```json
  {
    "publications": [
      {
        "id": "unique-id",
        "title": "Publication Title",
        "authors": ["Author 1", "Author 2"],
        "venue": "Conference/Journal Name",
        "year": 2024,
        "abstract": "Abstract text...",
        "links": {
          "paper": "url-to-pdf",
          "project": "url-to-project-page",
          "code": "url-to-github",
          "video": "url-to-video"
        },
        "image": "path-to-thumbnail",
        "bibtex": "BibTeX citation...",
        "featured": true
      }
    ]
  }
  ```
- [ ] Document how to add new publications
- [ ] Create helper script to validate publication data (optional)

### 6.2 Blog Post Management
- [ ] Define blog post format:
  - [ ] Markdown or HTML
  - [ ] Frontmatter with metadata (title, date, tags, excerpt)
- [ ] Create blog post template
- [ ] Document blog post creation workflow:
  - [ ] File naming convention (e.g., `YYYY-MM-DD-title.md`)
  - [ ] How to add images
  - [ ] How to update blog index
- [ ] Create script to generate new blog post from template (optional)

---

## Phase 7: Performance Optimization

### 7.1 Asset Optimization
- [ ] Optimize all images:
  - [ ] Compress images (use tools like ImageOptim, TinyPNG)
  - [ ] Convert to modern formats (WebP with fallbacks)
  - [ ] Create multiple sizes for responsive images
  - [ ] Implement lazy loading
- [ ] Minify CSS:
  - [ ] Combine and minify stylesheets
  - [ ] Remove unused CSS
- [ ] Minify JavaScript:
  - [ ] Combine and minify scripts
  - [ ] Use async/defer loading where appropriate
- [ ] Optimize fonts:
  - [ ] Use system fonts or optimized web fonts
  - [ ] Subset fonts if using custom fonts
  - [ ] Implement font-display: swap

### 7.2 Performance Testing
- [ ] Test with Lighthouse:
  - [ ] Aim for 90+ performance score
  - [ ] Check accessibility score
  - [ ] Verify SEO score
  - [ ] Check best practices
- [ ] Test page load times
- [ ] Verify mobile performance
- [ ] Check cross-browser compatibility:
  - [ ] Chrome
  - [ ] Firefox
  - [ ] Safari
  - [ ] Edge
  - [ ] Mobile browsers

---

## Phase 8: SEO & Accessibility

### 8.1 SEO Implementation
- [ ] Add meta tags to all pages:
  - [ ] Title tags (unique per page)
  - [ ] Meta descriptions
  - [ ] Open Graph tags for social sharing
  - [ ] Twitter Card tags
- [ ] Create `sitemap.xml`
- [ ] Create `robots.txt`
- [ ] Implement schema.org structured data:
  - [ ] Person schema for homepage
  - [ ] Article schema for blog posts
  - [ ] ScholarlyArticle for publications (optional)
- [ ] Add canonical URLs
- [ ] Implement proper heading hierarchy (h1, h2, h3, etc.)

### 8.2 Accessibility (WCAG 2.1 AA)
- [ ] Semantic HTML throughout
- [ ] Proper alt text for all images
- [ ] Sufficient color contrast (4.5:1 for normal text)
- [ ] Keyboard navigation support
- [ ] Focus indicators visible
- [ ] ARIA labels where needed
- [ ] Skip to main content link
- [ ] Test with screen reader (NVDA, JAWS, or VoiceOver)

---

## Phase 9: Deployment & Infrastructure

### 9.1 Hosting Setup
- [ ] Choose hosting platform:
  - [ ] GitHub Pages (free, easy)
  - [ ] Netlify (free tier, continuous deployment)
  - [ ] Vercel (free tier, great performance)
  - [ ] Cloudflare Pages (free, fast CDN)
  - [ ] Traditional hosting (if preferred)
- [ ] Set up custom domain (itzikbs.com)
- [ ] Configure HTTPS/SSL
- [ ] Set up DNS records

### 9.2 Continuous Integration/Deployment
- [ ] Create deployment workflow:
  - [ ] Automatic deployment on push to main branch
  - [ ] Preview deployments for pull requests (if using Netlify/Vercel)
- [ ] Set up GitHub Actions (optional):
  - [ ] Automated builds
  - [ ] Link checking
  - [ ] HTML validation
- [ ] Create build scripts:
  - [ ] Minification
  - [ ] Image optimization
  - [ ] Asset copying

### 9.3 Backup & Version Control
- [ ] Ensure all content is in Git
- [ ] Document backup procedures
- [ ] Set up automated backups (if using external services)

---

## Phase 10: Testing & Quality Assurance

### 10.1 Functionality Testing
- [ ] Test all internal links
- [ ] Test all external links
- [ ] Verify navigation works on all pages
- [ ] Test forms and interactive elements
- [ ] Verify all publications load correctly
- [ ] Verify all blog posts display properly
- [ ] Test search/filter functionality

### 10.2 Cross-Device Testing
- [ ] Test on mobile devices:
  - [ ] iPhone (Safari)
  - [ ] Android (Chrome)
- [ ] Test on tablets:
  - [ ] iPad
  - [ ] Android tablet
- [ ] Test on desktop:
  - [ ] Windows
  - [ ] macOS
  - [ ] Linux

### 10.3 Performance Verification
- [ ] Run Lighthouse audits
- [ ] Test page load speeds
- [ ] Verify resource optimization
- [ ] Check Core Web Vitals:
  - [ ] Largest Contentful Paint (LCP)
  - [ ] First Input Delay (FID)
  - [ ] Cumulative Layout Shift (CLS)

---

## Phase 11: Migration & Launch

### 11.1 Pre-Launch Checklist
- [ ] Content verification:
  - [ ] All WordPress content migrated
  - [ ] No broken links
  - [ ] All images displaying correctly
- [ ] Analytics setup:
  - [ ] Google Analytics or alternative
  - [ ] Track key metrics
- [ ] Performance verification:
  - [ ] Pass Lighthouse audits
  - [ ] Fast page loads
- [ ] Accessibility verification:
  - [ ] WCAG 2.1 AA compliance

### 11.2 Launch Process
- [ ] Set up redirects from old WordPress URLs (if structure changed)
- [ ] Update DNS to point to new hosting
- [ ] Monitor for issues during transition
- [ ] Verify all pages accessible
- [ ] Test from different locations/networks

### 11.3 Post-Launch
- [ ] Monitor analytics for traffic patterns
- [ ] Check for 404 errors and broken links
- [ ] Gather feedback from visitors
- [ ] Address any issues promptly
- [ ] Update social media links if needed

---

## Phase 12: Documentation & Maintenance

### 12.1 Documentation Completion
- [ ] Finalize README.md with:
  - [ ] Complete setup instructions
  - [ ] Content update procedures
  - [ ] Deployment instructions
  - [ ] Troubleshooting guide
- [ ] Create CONTRIBUTING.md (if open to contributions)
- [ ] Document code structure and organization
- [ ] Create style guide for consistent content formatting

### 12.2 Maintenance Plan
- [ ] Schedule regular updates:
  - [ ] Security updates (dependencies)
  - [ ] Content updates (publications, blog posts)
  - [ ] Performance monitoring
- [ ] Plan for future enhancements:
  - [ ] New features to add
  - [ ] Design improvements
  - [ ] Additional content sections

---

## Success Criteria

### Must Have ✓
- [x] All WordPress content successfully migrated
- [x] Website fully responsive (mobile, tablet, desktop)
- [x] Fast page loads (Lighthouse score 90+)
- [x] No WordPress dependencies
- [x] Easy to add new blog posts and publications
- [x] Custom domain (itzikbs.com) working with HTTPS
- [x] Clean, professional design

### Should Have
- [ ] Dark mode support
- [ ] Publication search/filter functionality
- [ ] Blog post tags/categories
- [ ] Analytics tracking
- [ ] SEO optimization complete

### Nice to Have
- [ ] Advanced animations and transitions
- [ ] Interactive visualizations (if relevant to research)
- [ ] Automated blog post generation tools
- [ ] RSS feed for blog
- [ ] Newsletter signup (optional)

---

## Resources & References

### Design Inspiration
- https://www.vincentsitzmann.com/ - Clean academic website design
- Other academic personal websites for inspiration

### Tools & Libraries
- **CSS Frameworks** (optional): Bootstrap, Tailwind CSS, or custom
- **JavaScript Libraries**: Vanilla JS preferred for simplicity
- **Build Tools** (optional): Parcel, Webpack, or simple npm scripts
- **Markdown Parser** (if using markdown): marked.js, markdown-it
- **Syntax Highlighting**: Prism.js or highlight.js
- **Image Optimization**: ImageOptim, Squoosh, sharp

### Testing Tools
- Lighthouse (Chrome DevTools)
- WebPageTest.org
- GTmetrix
- WAVE (accessibility testing)
- axe DevTools (accessibility)

### Hosting Options
- GitHub Pages: https://pages.github.com/
- Netlify: https://www.netlify.com/
- Vercel: https://vercel.com/
- Cloudflare Pages: https://pages.cloudflare.com/

---

## Timeline Estimate

- **Phase 1-2** (Setup & Content Extraction): 1-2 days
- **Phase 3-4** (Design & Core Pages): 3-5 days
- **Phase 5** (JavaScript Functionality): 2-3 days
- **Phase 6** (Content Management): 1-2 days
- **Phase 7-8** (Optimization & SEO): 2-3 days
- **Phase 9** (Deployment): 1 day
- **Phase 10-11** (Testing & Launch): 2-3 days
- **Phase 12** (Documentation): 1 day

**Total Estimated Time**: 2-3 weeks (working part-time)

---

## Notes

- This plan is designed to be broken down into separate GitHub issues for each major task
- Tasks can be assigned priorities (P0-Critical, P1-High, P2-Medium, P3-Low)
- Some tasks can be done in parallel (e.g., design work and content extraction)
- Regular testing and iteration throughout the process is crucial
- Keep commits small and atomic for easier review and rollback if needed
- Document decisions and trade-offs in commit messages or separate docs

---

**Last Updated**: 2025-11-17
**Status**: Planning Phase
**Next Steps**: Begin Phase 1 - Project Setup & Planning
