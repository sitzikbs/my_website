# Cloudflare Pages Deployment Guide

Complete step-by-step instructions for deploying your website to Cloudflare Pages and updating your domain.

---

## 🎯 Overview

**What you're deploying:**
- Static website built with 11ty (Eleventy)
- 81 pages (blog posts, publications, podcast episodes, etc.)
- Build time: ~1.3 seconds
- Output directory: `_site/`

**What we'll do:**
1. Deploy to Cloudflare Pages
2. Connect your custom domain
3. Update DNS settings
4. Verify deployment

---

## 📋 Pre-Deployment Checklist

### ✅ Already Complete
- [x] Website builds successfully (`npm run build`)
- [x] All pages rendering correctly locally
- [x] Navigation working on all pages
- [x] SEO meta tags configured
- [x] sitemap.xml and robots.txt present
- [x] Favicon and icons configured
- [x] Repository clean and organized
- [x] Documentation updated

### ⚠️ Recommended Before Deployment
- [ ] Test website locally one final time (`npm run serve`)
- [ ] Review content for typos/errors
- [ ] Verify all important links work
- [ ] Note your current domain's DNS provider

---

## 🚀 Part 1: Deploy to Cloudflare Pages

### Step 1: Access Cloudflare Pages

1. **Go to:** https://pages.cloudflare.com
2. **Log in** to your Cloudflare account (or create one if needed)
3. **Click:** "Create a project"

### Step 2: Connect GitHub Repository

1. **Click:** "Connect to Git"
2. **Select:** "GitHub"
3. **Authorize** Cloudflare to access your GitHub account (if first time)
4. **Select repository:** Choose `sitzikbs/my_website`
5. **Click:** "Begin setup"

### Step 3: Configure Build Settings

Enter the following configuration:

| Setting | Value |
|---------|-------|
| **Project name** | `itzikbs-website` (or your preferred name) |
| **Production branch** | `main` |
| **Framework preset** | Select "Eleventy" from dropdown |
| **Build command** | `npm run build` |
| **Build output directory** | `_site` |
| **Root directory** | (leave empty) |

**Environment variables:** None needed

### Step 4: Deploy

1. **Click:** "Save and Deploy"
2. **Wait** for the build to complete (usually 1-2 minutes)
3. **Verify** deployment succeeded (green checkmark)

You'll get a temporary URL like: `https://itzikbs-website.pages.dev`

### Step 5: Test Deployment

1. **Visit** your temporary Cloudflare Pages URL
2. **Check:**
   - ✅ Homepage loads correctly
   - ✅ Navigation works
   - ✅ Blog posts open
   - ✅ Publications page loads
   - ✅ Images display
   - ✅ Styles look correct

---

## 🌐 Part 2: Connect Your Custom Domain

### Step 6: Add Custom Domain in Cloudflare Pages

1. **In your Cloudflare Pages project**, click **"Custom domains"** tab
2. **Click:** "Set up a custom domain"
3. **Enter your domain:** `itzikbs.com` (and/or `www.itzikbs.com`)
4. **Click:** "Continue"

Cloudflare will show you DNS records to add.

### Step 7: Update DNS Settings

**⚠️ IMPORTANT:** Your domain is currently pointed to another host. You need to:

#### Option A: Domain Hosted on Cloudflare Already
If your domain DNS is already managed by Cloudflare:

1. **Go to:** Cloudflare Dashboard → Your domain → DNS → Records
2. **Find** your current A or CNAME records for `@` and `www`
3. **Delete or update** them according to Cloudflare Pages instructions
4. **Add** the DNS records shown in Cloudflare Pages setup

Typical records needed:
```
Type: CNAME
Name: @
Target: itzikbs-website.pages.dev
Proxy: Enabled (orange cloud)

Type: CNAME  
Name: www
Target: itzikbs-website.pages.dev
Proxy: Enabled (orange cloud)
```

#### Option B: Domain Hosted Elsewhere (e.g., GoDaddy, Namecheap)
If your domain DNS is managed by another provider:

**Best practice:** Transfer DNS to Cloudflare

1. **In Cloudflare Dashboard**, click "Add site"
2. **Enter:** `itzikbs.com`
3. **Select** Free plan
4. **Follow wizard** to scan existing DNS records
5. **Review** scanned records, keep important ones
6. **Get nameservers** from Cloudflare (e.g., `ana.ns.cloudflare.com`)
7. **Go to your domain registrar** (GoDaddy, Namecheap, etc.)
8. **Change nameservers** to Cloudflare's nameservers
9. **Wait** 24-48 hours for DNS propagation (usually faster)
10. **Once DNS is on Cloudflare**, follow Option A above

**Alternative (not recommended):** You can add CNAME records at your current provider pointing to Cloudflare Pages, but you'll lose many Cloudflare benefits.

### Step 8: Verify Domain Connection

1. **In Cloudflare Pages**, check domain status
2. **Wait** for "Active" status (may take a few minutes to hours)
3. **Test** your custom domain: `https://itzikbs.com`
4. **Check both:**
   - `https://itzikbs.com`
   - `https://www.itzikbs.com`

---

## 🔄 Part 3: Handle Old Website Redirect

### Step 9: Identify Current Hosting

Before DNS change, document:
- **Current host:** _________________
- **Important:** Download backup of old site
- **Check for:** Any email services using this domain

### Step 10: Plan for Downtime

**Expected downtime:** Minimal to none
- DNS propagation: 5 minutes to 48 hours (usually < 1 hour)
- Cloudflare handles SSL automatically
- Old site remains accessible until DNS propagates

### Step 11: Monitor DNS Propagation

**Check DNS propagation:**
- Use: https://dnschecker.org
- Enter: `itzikbs.com`
- Verify: Points to Cloudflare Pages across multiple locations

**Test from different locations:**
```bash
# From your terminal:
dig itzikbs.com
nslookup itzikbs.com

# Check which server responds:
curl -I https://itzikbs.com
```

---

## 📊 Part 4: Post-Deployment Verification

### Step 12: Comprehensive Testing Checklist

**Functionality:**
- [ ] Homepage loads and displays correctly
- [ ] All navigation links work
- [ ] Blog posts load and render properly
- [ ] Publications page displays all papers
- [ ] Podcast page shows episodes
- [ ] Code page loads
- [ ] Contact page accessible
- [ ] Search/filter features work
- [ ] All images load
- [ ] Favicon displays

**Performance:**
- [ ] Run Lighthouse audit (aim for 90+ scores)
- [ ] Check page load speed (< 3 seconds)
- [ ] Verify responsive design on mobile

**SEO:**
- [ ] Submit sitemap to Google Search Console: `https://itzikbs.com/sitemap.xml`
- [ ] Verify robots.txt: `https://itzikbs.com/robots.txt`
- [ ] Check meta tags in page source
- [ ] Test social sharing (Twitter, LinkedIn)

**Security:**
- [ ] Verify HTTPS works (should be automatic)
- [ ] Check SSL certificate is valid
- [ ] Ensure HTTP redirects to HTTPS

### Step 13: Update External Links

Update your website URL in:
- [ ] Google Scholar profile
- [ ] LinkedIn profile
- [ ] Twitter/X bio
- [ ] GitHub profile README
- [ ] ORCID profile
- [ ] ResearchGate profile
- [ ] Email signature
- [ ] Other social media profiles

### Step 14: Search Console Setup

**Google Search Console:**
1. **Go to:** https://search.google.com/search-console
2. **Add property:** `itzikbs.com`
3. **Verify ownership** (DNS or HTML file method)
4. **Submit sitemap:** `https://itzikbs.com/sitemap.xml`

**Bing Webmaster Tools:**
1. **Go to:** https://www.bing.com/webmasters
2. **Add site:** `itzikbs.com`
3. **Verify ownership**
4. **Submit sitemap:** `https://itzikbs.com/sitemap.xml`

---

## 🔧 Troubleshooting

### Common Issues

**Problem:** "Build failed" on Cloudflare
- **Solution:** Check build logs, verify `npm run build` works locally
- **Check:** Node version compatibility (Cloudflare uses Node 18 by default)

**Problem:** CSS/JS not loading
- **Solution:** Check paths are relative (starting with `/`)
- **Check:** Files exist in `_site/` directory

**Problem:** Images not displaying
- **Solution:** Verify image paths in `_site/`
- **Check:** Images are copied in `.eleventy.js` passthrough

**Problem:** Domain showing old website
- **Solution:** Clear browser cache, check DNS propagation
- **Wait:** DNS can take up to 48 hours (usually much faster)

**Problem:** SSL certificate error
- **Solution:** Wait for Cloudflare to provision certificate (can take 24 hours)
- **Check:** Cloudflare Pages SSL settings

---

## 🎉 Success Criteria

Your deployment is successful when:
- ✅ Website loads at `https://itzikbs.com`
- ✅ All pages accessible and render correctly
- ✅ HTTPS working (green padlock)
- ✅ No console errors
- ✅ Lighthouse scores 90+
- ✅ Mobile responsive design working
- ✅ All content migrated correctly

---

## 📝 Post-Launch Notes

### Automatic Deployments

**Good news:** Every time you push to `main` branch:
1. Cloudflare automatically detects the push
2. Runs `npm run build`
3. Deploys new version to production
4. Takes ~1-2 minutes

**No manual deployment needed!**

### Rollback Process

If something goes wrong:
1. **In Cloudflare Pages**, go to "Deployments" tab
2. **Find** previous successful deployment
3. **Click** "Rollback to this deployment"
4. **Wait** ~30 seconds for rollback to complete

### Branch Previews

**Automatic preview deployments:**
- Every branch gets a preview URL
- Example: `https://feature-branch.itzikbs-website.pages.dev`
- Test changes before merging to main

---

## 🆘 Getting Help

**Cloudflare Pages Documentation:**
- https://developers.cloudflare.com/pages/

**11ty Documentation:**
- https://www.11ty.dev/docs/

**Your DNS Provider:**
- Check their support docs for nameserver changes

---

## ✅ Deployment Checklist Summary

**Before deployment:**
- [x] Code in GitHub repository
- [x] Build working locally
- [ ] Ready to change DNS

**During deployment:**
- [ ] Create Cloudflare Pages project
- [ ] Connect GitHub repository
- [ ] Configure build settings
- [ ] Deploy successfully
- [ ] Add custom domain
- [ ] Update DNS records

**After deployment:**
- [ ] Verify site loads correctly
- [ ] Test all functionality
- [ ] Submit sitemaps
- [ ] Update social media links
- [ ] Monitor for 24-48 hours

---

**Estimated time:** 30-60 minutes (plus DNS propagation wait time)

**Last updated:** January 2, 2026
