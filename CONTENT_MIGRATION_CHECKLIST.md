# Content Migration Checklist

**Date**: 2025-11-17  
**Purpose**: Track progress of WordPress content migration  
**Status**: Infrastructure Ready - Awaiting Content

---

## Phase 2: Content Extraction - Progress Tracker

### Infrastructure Setup ✅

- [x] Create directory structure
- [x] Create data directory with JSON schemas
- [x] Create blog posts directory
- [x] Create assets directories (images, documents, videos)
- [x] Create example publications.json with schema
- [x] Create example blog-index.json with schema
- [x] Create example blog post templates
- [x] Create migration guide documentation
- [x] Create validation script
- [x] Create README files for each directory

### Blog Posts Migration ⏳

#### Export from WordPress
- [ ] Access WordPress admin at https://itzikbs.com/wp-admin
- [ ] Export all blog posts (Tools → Export → Posts)
- [ ] Save WordPress XML export file
- [ ] Count total blog posts to migrate: ___

#### Convert Blog Posts
- [ ] Install/use WordPress-to-HTML converter tool
- [ ] Convert each blog post to HTML format
- [ ] Verify post count matches WordPress export
- [ ] Create HTML file for each post in `blog/posts/`
- [ ] Follow naming convention: `YYYY-MM-DD-post-slug.html`

#### Update Blog Metadata
- [ ] Update `data/blog-index.json` with all posts
- [ ] Extract and add all categories
- [ ] Extract and add all tags
- [ ] Verify all post metadata is complete
- [ ] Run validation: `python3 scripts/validate-content.py`

#### Download Blog Images
- [ ] Download all blog featured images from WordPress
- [ ] Download all inline blog images
- [ ] Organize images in `assets/images/blog/`
- [ ] Rename images following convention
- [ ] Optimize all images (compress, resize)
- [ ] Update image paths in HTML files
- [ ] Verify all images load correctly

#### Blog Posts Content Review
- [ ] Review all posts for formatting issues
- [ ] Fix any broken links
- [ ] Convert WordPress shortcodes to HTML
- [ ] Verify code blocks are properly formatted
- [ ] Check that all embedded content works
- [ ] Test responsive design on mobile

**Progress**: 0 / ___ blog posts migrated

---

### Publications Migration ⏳

#### Extract Publications Data
- [ ] Access publications on WordPress site
- [ ] Document total number of publications: ___
- [ ] Extract title, authors, venue for each
- [ ] Extract publication year and month
- [ ] Extract abstracts
- [ ] Extract all links (paper, code, video, project, DOI)
- [ ] Copy BibTeX citations
- [ ] Note any awards or special recognition

#### Update Publications JSON
- [ ] Replace example data in `data/publications.json`
- [ ] Add all publications with complete metadata
- [ ] Organize by year (most recent first)
- [ ] Mark featured publications
- [ ] Add tags/keywords for each publication
- [ ] Run validation: `python3 scripts/validate-content.py`

#### Download Publication Assets
- [ ] Download all publication thumbnail images
- [ ] Download all publication figure images
- [ ] Download all publication PDFs
- [ ] Download supplementary materials
- [ ] Organize in `assets/images/publications/`
- [ ] Organize PDFs in `assets/documents/papers/`
- [ ] Rename files following convention
- [ ] Optimize images
- [ ] Update paths in publications.json
- [ ] Verify all files are accessible

**Progress**: 0 / ___ publications migrated

---

### About/Bio Content ⏳

#### Extract Biography
- [ ] Locate bio text on WordPress site
- [ ] Copy short bio (2-3 sentences)
- [ ] Copy extended bio (full paragraphs)
- [ ] Extract research interests list
- [ ] Extract current position/affiliation
- [ ] Extract education history
- [ ] Extract professional experience

#### Create About Data File
- [ ] Create `data/about.json`
- [ ] Add name and title
- [ ] Add short bio for homepage
- [ ] Add extended bio for about page
- [ ] Add research interests
- [ ] Add contact information
- [ ] Add social media links
- [ ] Link to CV file

**Status**: Not started

---

### Media Assets Migration ⏳

#### Profile/Personal Images
- [ ] Download profile photo/headshot
- [ ] Create multiple sizes (large, medium, thumbnail)
- [ ] Save to `assets/images/profile/`
- [ ] Optimize images
- [ ] Update references in content

#### General Site Assets
- [ ] Download site logo
- [ ] Download favicon
- [ ] Download any background images
- [ ] Download social media icons
- [ ] Save to `assets/images/general/` and `assets/images/icons/`
- [ ] Optimize all assets

#### Documents
- [ ] Download current CV/resume
- [ ] Save to `assets/documents/cv/`
- [ ] Download any other documents
- [ ] Organize in appropriate subdirectories
- [ ] Update file references

#### Videos (if any)
- [ ] List all videos on WordPress site
- [ ] Decide: keep local or use external hosting
- [ ] If local: download and save to `assets/videos/`
- [ ] If external: verify all video links work
- [ ] Update video references

**Progress**: 0 / ___ media files migrated

---

### Content Verification ⏳

#### Validate Data Files
- [ ] Run `python3 scripts/validate-content.py`
- [ ] Fix any validation errors
- [ ] Address any warnings
- [ ] Verify JSON syntax is correct

#### Check File References
- [ ] Verify all image paths are correct
- [ ] Verify all PDF paths are correct
- [ ] Verify all internal links work
- [ ] Check for any 404s or broken links

#### Content Quality Check
- [ ] All blog posts display correctly
- [ ] All publications display correctly
- [ ] All images load properly
- [ ] No placeholder content remains
- [ ] Formatting is consistent
- [ ] Mobile view works correctly

#### SEO and Metadata
- [ ] All pages have proper titles
- [ ] All pages have meta descriptions
- [ ] All images have alt text
- [ ] Open Graph tags present
- [ ] Structured data added where appropriate

---

## Acceptance Criteria Status

From Issue #6 - Phase 2: Content Extraction:

- [ ] Export all blog posts with metadata (date, tags, categories)
- [ ] Export publications list with complete details
- [ ] Extract About/bio text and format appropriately
- [ ] Download entire WordPress media library
- [ ] Convert blog posts to HTML or Markdown format
- [ ] Create `data/publications.json` with structured publication data
- [ ] Create `data/blog-index.json` with blog post metadata
- [ ] Organize all media assets in appropriate directories
- [ ] Verify all content has been successfully extracted

---

## Tools Needed

### Required
- [ ] WordPress admin access
- [ ] FTP/SFTP access (for media download)
- [ ] Text editor for JSON editing
- [ ] Python 3 (for validation script)

### Recommended
- [ ] WordPress-to-HTML converter
- [ ] Image optimization tool (TinyPNG, ImageOptim, etc.)
- [ ] JSON validator/editor
- [ ] Link checker tool

---

## Estimated Time

Based on WordPress site size:

### Small Site (< 20 posts, < 10 publications)
- Blog posts: 2-4 hours
- Publications: 1-2 hours
- Media: 1-2 hours
- **Total**: 4-8 hours

### Medium Site (20-50 posts, 10-30 publications)
- Blog posts: 4-8 hours
- Publications: 2-4 hours
- Media: 2-4 hours
- **Total**: 8-16 hours

### Large Site (> 50 posts, > 30 publications)
- Blog posts: 8-16 hours
- Publications: 4-8 hours
- Media: 4-8 hours
- **Total**: 16-32 hours

---

## Progress Summary

### Overall Completion: 20%

| Task | Status | Progress |
|------|--------|----------|
| Infrastructure Setup | ✅ Complete | 100% |
| Blog Posts Migration | ⏳ Not Started | 0% |
| Publications Migration | ⏳ Not Started | 0% |
| About/Bio Content | ⏳ Not Started | 0% |
| Media Assets Migration | ⏳ Not Started | 0% |
| Content Verification | ⏳ Not Started | 0% |

---

## Next Steps

1. **Immediate**: Gain access to WordPress admin and FTP/SFTP
2. **Phase 1**: Export and convert blog posts
3. **Phase 2**: Extract and format publications data
4. **Phase 3**: Download and organize media assets
5. **Phase 4**: Extract about/bio content
6. **Phase 5**: Verify all content and run validations
7. **Phase 6**: Mark issue as complete and move to Phase 3 (static site implementation)

---

## Notes

- Infrastructure is ready and waiting for content
- All schemas and examples are in place
- Validation tools are working
- Follow MIGRATION_GUIDE.md for detailed instructions
- Reference example files for correct format
- Run validation after each major update

---

**Last Updated**: 2025-11-17  
**Status**: Infrastructure Complete - Ready for Content Migration  
**Blocker**: WordPress site access required to proceed
