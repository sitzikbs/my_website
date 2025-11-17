# Quick Start Guide - WordPress Audit

**⏱️ Estimated Time**: 8-14 hours  
**👤 Prerequisites**: WordPress admin access, basic familiarity with WordPress  
**📋 Goal**: Complete audit of https://itzikbs.com/ for migration

---

## 🚀 Getting Started (5 minutes)

### 1. Read This First
- [ ] Read this entire guide (5 minutes)
- [ ] Review `README.md` in this directory
- [ ] Skim through the audit templates to understand what data you'll collect

### 2. Prepare Your Environment
- [ ] Ensure you have WordPress admin access
- [ ] Open all 4 inventory documents in your editor:
  - `WORDPRESS_AUDIT.md`
  - `PUBLICATIONS_INVENTORY.md`
  - `BLOG_POSTS_INVENTORY.md`
  - `MEDIA_ASSETS_INVENTORY.md`
- [ ] Open `AUDIT_CHECKLIST.md` to track progress
- [ ] Have a browser open to https://itzikbs.com/wp-admin/

---

## 📝 Step-by-Step Audit Process

### Phase 1: Quick Site Survey (30 minutes)

**Goal**: Get familiar with the site structure

1. **Browse the public site** (10 minutes)
   - [ ] Visit https://itzikbs.com/
   - [ ] Click through all main menu items
   - [ ] Note approximate number of pages
   - [ ] Count publications (if visible)
   - [ ] Scroll through blog posts
   - [ ] Take screenshots of key pages

2. **Login to WordPress Admin** (10 minutes)
   - [ ] Go to https://itzikbs.com/wp-admin/
   - [ ] Check Dashboard > At a Glance for quick stats
   - [ ] Note WordPress version
   - [ ] Note theme name
   - [ ] Count active plugins

3. **Quick inventory** (10 minutes)
   - [ ] Pages: Go to Pages > All Pages, note count
   - [ ] Posts: Go to Posts > All Posts, note count
   - [ ] Media: Go to Media > Library, note count
   - [ ] Publications: Check if there's a custom post type

4. **Update `AUDIT_SUMMARY.md`** with initial counts

---

### Phase 2: Detailed Content Audit (4-6 hours)

#### A. Publications (1-2 hours)

**Document in**: `PUBLICATIONS_INVENTORY.md`

1. **Navigate to publications** (how they're stored)
   - [ ] Custom post type? Go to that menu
   - [ ] Regular posts with category? Filter by category
   - [ ] Pages? List all publication pages

2. **For each publication, copy**:
   - [ ] Title
   - [ ] Authors (in order)
   - [ ] Venue name
   - [ ] Year and month
   - [ ] Abstract
   - [ ] All links (paper PDF, project page, code, video, etc.)
   - [ ] BibTeX citation
   - [ ] Thumbnail image URL
   - [ ] Any tags or categories

3. **Organize by year** in the inventory document

4. **Note patterns**:
   - [ ] How are they currently displayed?
   - [ ] Any special formatting?
   - [ ] Filter/sort functionality?

**💡 Tip**: Copy each publication's data into the template in `PUBLICATIONS_INVENTORY.md`. Work in batches of 5-10.

---

#### B. Blog Posts (1-2 hours)

**Document in**: `BLOG_POSTS_INVENTORY.md`

1. **Export basic metadata first**:
   ```
   WordPress Admin > Tools > Export > Posts > Download
   ```
   - [ ] Save the XML file as `wordpress-export.xml`

2. **In WordPress Admin > Posts > All Posts**:
   - [ ] Switch to "List" view
   - [ ] Increase items per page to 100 (Screen Options)

3. **For each post, document**:
   - [ ] Title
   - [ ] Date published
   - [ ] Categories
   - [ ] Tags  
   - [ ] Featured image
   - [ ] Excerpt (if custom)
   - [ ] Word count (approximate)

4. **Click into 5-10 representative posts** and note:
   - [ ] How many have embedded images?
   - [ ] How many have code blocks?
   - [ ] How many have videos?
   - [ ] What's the typical length?

5. **List all categories and tags**:
   - WordPress Admin > Posts > Categories
   - WordPress Admin > Posts > Tags

**💡 Tip**: You don't need to document every detail of every post. Focus on getting complete metadata and note patterns.

---

#### C. Static Pages (30 minutes)

**Document in**: `WORDPRESS_AUDIT.md` - Section 2

1. **Go to Pages > All Pages**

2. **For each page**:
   - [ ] Homepage/About
   - [ ] Publications page (if separate from posts)
   - [ ] Contact page
   - [ ] CV/Resume page
   - [ ] Any others

3. **For each page, copy**:
   - [ ] URL slug
   - [ ] Page title
   - [ ] Full text content
   - [ ] Images used
   - [ ] Special features (forms, shortcodes, etc.)

4. **Special attention to Homepage**:
   - [ ] Profile image(s)
   - [ ] Bio text (may be in multiple places)
   - [ ] Current position
   - [ ] Contact info
   - [ ] Social media links

---

#### D. Static Content Extraction (30 minutes)

**Document in**: `WORDPRESS_AUDIT.md` - Section 3

1. **Bio and About Text**:
   - [ ] Copy short bio (usually on homepage)
   - [ ] Copy extended bio (usually on about page)
   - [ ] Save to audit document

2. **Professional Information**:
   - [ ] Current position and institution
   - [ ] Research interests
   - [ ] Education (degrees, institutions, years)
   - [ ] Work experience summary

3. **Contact Information**:
   - [ ] Email address
   - [ ] Office address (if public)
   - [ ] All social media links (GitHub, LinkedIn, Scholar, etc.)

4. **CV/Resume**:
   - [ ] Find download link
   - [ ] Download the PDF
   - [ ] Note filename and last update date

---

### Phase 3: Media Assets (1-2 hours)

**Document in**: `MEDIA_ASSETS_INVENTORY.md`

#### Option A: Quick Inventory (30 minutes)

1. **Go to Media > Library**
2. **Switch to List view**
3. **For key images only**:
   - [ ] Profile photo(s)
   - [ ] Site logo
   - [ ] Publication thumbnails
   - [ ] A few blog featured images
   
4. **Note**:
   - [ ] Filenames
   - [ ] Upload dates
   - [ ] File sizes
   - [ ] Where they're used

#### Option B: Complete Download (1-2 hours)

1. **Use SFTP/FTP** (if you have access):
   ```bash
   sftp user@itzikbs.com
   cd /wp-content/uploads/
   get -r . ./wordpress-media/
   ```

2. **Or use a WordPress plugin**:
   - Install "All-in-One WP Migration"
   - Export site (or just media)
   - Download backup file

3. **Or use WP-CLI** (if available):
   ```bash
   wp media list --format=json > media-list.json
   ```

4. **Catalog downloaded files**:
   - [ ] Count total files
   - [ ] Calculate total size
   - [ ] Organize by type (images, PDFs, videos, etc.)

**💡 Tip**: For a quick audit, Option A is sufficient. Full download (Option B) can be done during actual migration.

---

### Phase 4: Site Structure & Features (1 hour)

**Document in**: `WORDPRESS_AUDIT.md` - Sections 5-6

#### Navigation Structure (15 minutes)

1. **Appearance > Menus**:
   - [ ] List all menu items in primary menu
   - [ ] Note menu order
   - [ ] List all menu items in footer menu
   - [ ] Check for any sub-menus

2. **Widgets**:
   - [ ] Appearance > Widgets
   - [ ] List all active widgets
   - [ ] Note which widget areas they're in

#### Plugins (20 minutes)

1. **Plugins > Installed Plugins**:
   - [ ] List all active plugins with versions
   - [ ] Note what each plugin does
   - [ ] Identify critical ones (must replicate functionality)

2. **Focus on**:
   - [ ] SEO plugins (Yoast, All in One SEO, etc.)
   - [ ] Contact form plugins
   - [ ] Security plugins
   - [ ] Performance/caching plugins
   - [ ] Custom functionality plugins

#### Theme Details (10 minutes)

1. **Appearance > Themes**:
   - [ ] Note active theme name and version
   - [ ] Check if it's a child theme

2. **Appearance > Customize**:
   - [ ] Browse customization options
   - [ ] Note any custom CSS
   - [ ] Note color scheme
   - [ ] Note fonts being used

#### Special Features (15 minutes)

Check for and document:
- [ ] Contact forms (which plugin? what fields?)
- [ ] Search functionality (default or custom?)
- [ ] Comments (enabled? which posts? moderation?)
- [ ] Social sharing buttons
- [ ] Newsletter signup
- [ ] Analytics (Google Analytics?)
- [ ] Any custom shortcodes

---

### Phase 5: Export Everything (1 hour)

#### Content Export

1. **WordPress XML Export**:
   - [ ] Tools > Export
   - [ ] Select "All content"
   - [ ] Click "Download Export File"
   - [ ] Save as `wordpress-export.xml` in project root or `/audit` folder

2. **Database Backup** (if WP-CLI available):
   ```bash
   wp db export wordpress-backup.sql
   ```
   Or use phpMyAdmin to export database

3. **Verify exports**:
   - [ ] XML file can be opened
   - [ ] SQL file is not corrupt
   - [ ] File sizes reasonable

#### Media Export

If you did full download in Phase 3:
- [ ] Verify all files downloaded
- [ ] Check file integrity (open a few random files)

If not yet downloaded:
- [ ] Download at least key images (profile, logos, featured publication images)
- [ ] Note: full media download can happen during migration

---

### Phase 6: Review & Finalize (1 hour)

#### Document Review

1. **Check each inventory document**:
   - [ ] `WORDPRESS_AUDIT.md` - All sections filled?
   - [ ] `PUBLICATIONS_INVENTORY.md` - All publications listed?
   - [ ] `BLOG_POSTS_INVENTORY.md` - All posts counted and sampled?
   - [ ] `MEDIA_ASSETS_INVENTORY.md` - Key media documented?

2. **Look for `[To be filled]` or `[#]` placeholders**:
   - [ ] Replace all with actual data
   - [ ] If data not available, note "N/A" or "Unknown"

3. **Verify counts match**:
   - [ ] WordPress "At a Glance" dashboard vs. your counts
   - [ ] Spot check a few items against live site

#### Complete Summary

1. **Fill out `AUDIT_SUMMARY.md`**:
   - [ ] Add all statistics
   - [ ] List key findings
   - [ ] Note any challenges discovered
   - [ ] Add recommendations

2. **Update `AUDIT_CHECKLIST.md`**:
   - [ ] Mark all completed tasks
   - [ ] Note actual time spent
   - [ ] Add any observations

#### Quality Checks

- [ ] All inventory documents have real data (not just templates)
- [ ] All exports completed and saved
- [ ] Key media files downloaded
- [ ] No critical information missing
- [ ] Summary document completed

---

## ✅ Completion Checklist

Before considering audit complete:

### Documentation
- [ ] `WORDPRESS_AUDIT.md` - Complete
- [ ] `PUBLICATIONS_INVENTORY.md` - All publications cataloged
- [ ] `BLOG_POSTS_INVENTORY.md` - All posts inventoried
- [ ] `MEDIA_ASSETS_INVENTORY.md` - Media documented
- [ ] `AUDIT_CHECKLIST.md` - All tasks marked
- [ ] `AUDIT_SUMMARY.md` - Summary completed

### Data Files
- [ ] `wordpress-export.xml` - Content export saved
- [ ] `wordpress-backup.sql` - Database backup (if possible)
- [ ] Key media files downloaded
- [ ] Screenshots of important pages saved

### Verification
- [ ] Counts verified against WordPress dashboard
- [ ] Sample content spot-checked
- [ ] All critical information captured
- [ ] No placeholders remaining in documents

---

## 🎯 Time Management Tips

### If Short on Time (4-hour quick audit)

**Must Do** (3 hours):
1. Publications inventory (1 hour) - CRITICAL
2. Blog posts count + 10 representative posts (1 hour)
3. Static pages content (30 min)
4. WordPress XML export (15 min)
5. Key media files download (30 min)
6. Summary document (15 min)

**Can Skip**:
- Detailed every-post inventory (just get counts and patterns)
- Complete media download (just key images)
- Exhaustive plugin documentation (just critical ones)

### If You Have Time (8+ hours)

**Do Everything**:
- Complete detailed inventory
- Full media download
- Thorough plugin analysis
- Extensive testing of features
- Multiple export formats
- Detailed recommendations

---

## 🚨 Common Pitfalls

### Don't:
- ❌ Skip the WordPress XML export (critical!)
- ❌ Forget to download key images
- ❌ Ignore draft posts (note them separately)
- ❌ Miss custom post types
- ❌ Forget to document URL structure
- ❌ Skip comments decision
- ❌ Ignore mobile view (check a few pages)

### Do:
- ✅ Take screenshots as you go
- ✅ Test all links in publications
- ✅ Note any broken functionality
- ✅ Document anything unusual
- ✅ Save copies of exports in multiple places
- ✅ Keep notes of questions/issues

---

## 🆘 Troubleshooting

### "Can't access WordPress admin"
- Verify credentials
- Check if IP is blocked
- Try different browser/incognito mode
- Contact site owner

### "Export file too large"
- Export in smaller chunks (posts only, pages only, etc.)
- Increase PHP memory limit in wp-config.php
- Use WP-CLI instead

### "Can't download media files"
- Try SFTP/FTP instead of plugin
- Download in batches
- Download just key files for audit, rest during migration

### "Too many publications/posts to document"
- Focus on getting accurate counts
- Document 10-20 representative examples in detail
- Note patterns rather than every detail
- Can fill in complete data during migration

---

## 📞 Questions During Audit

Keep a running list of questions:

**Example questions to ask site owner**:
- Which publications should be featured?
- Are there any draft posts to publish?
- Are comments important to keep?
- What's the most important content?
- Any content that can be archived vs. migrated?
- Preferred URL structure for new site?

Document questions in: `WORDPRESS_AUDIT.md` - Section "Notes & Observations"

---

## ✨ Final Tips

1. **Work in batches**: Don't try to do everything at once. Take breaks.

2. **Start with what matters**: Publications and blog posts are usually most important.

3. **Save frequently**: Save your audit documents as you go.

4. **Don't get stuck**: If something is unclear, note it and move on.

5. **Use templates**: The templates are designed to make this easier - just fill in the blanks.

6. **Ask for help**: If stuck, document the issue and ask the site owner or developer.

---

## 🎉 When You're Done

1. **Commit all changes**:
   ```bash
   git add audit/
   git commit -m "Complete WordPress audit with data"
   git push
   ```

2. **Update TODO.md**:
   - Mark Phase 2.1 as complete

3. **Notify stakeholders**:
   - Audit is complete
   - Ready to begin migration

4. **Celebrate!** 🎊
   You've completed a critical step in the migration process!

---

**Created**: 2025-11-17  
**Version**: 1.0  
**Status**: ✅ Ready to Use
