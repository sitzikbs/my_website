# Broken Links Analysis - Workflow Run 20702644097

**Workflow Run:** https://github.com/sitzikbs/my_website/actions/runs/20702644097
**Date:** 2026-01-05
**Status:** Failed (Link Checker step)

## Summary

This document contains an analysis of broken links detected by the automated link checker workflow. The workflow uses [lychee](https://github.com/lycheeverse/lychee) to check all HTML files in the built site.

## Links Fixed in This PR

### 1. CVPR 2019 Author Links (FIXED)
**File:** `blog/posts-md/2019-06-25-cvpr-2019.md`
**Issue:** 80 instances of broken author profile links
**Pattern:** `http://openaccess.thecvf.com/CVPR2019.py#`
**Problem:** Links ended in invalid `.py#` extension
**Solution:** Removed links, kept author names as plain text
**Status:** ✅ FIXED

### 2. Typo in CVPR 2024 Post (FIXED)
**File:** `blog/posts-md/2024-06-26-cvpr2024.md`
**Issue:** Typo "odcast" should be "podcast"
**Status:** ✅ FIXED

### 3. CV Download Link (FIXED)
**File:** `about.html`
**Issue:** Link path didn't match actual filename (spaces vs hyphens)
**Solution:** Updated link to use URL-encoded spaces
**Status:** ✅ FIXED

## Potentially Broken Links (Needs Investigation)

### Niessnerlab Links
The following niessnerlab.org links exist in the repository and are **NOT** currently excluded in the link checker:

**From `blog/posts-md/2018-10-19-reasearch-visit-in-germany.md`:**
- http://niessnerlab.org/
- http://niessnerlab.org/members/matthias_niessner/profile.html
- http://niessnerlab.org/members/andreas_roessler/profile.html
- http://niessnerlab.org/projects/roessler2018faceforensics.html
- http://niessnerlab.org/members/manuel_dahnert/profile.html
- http://niessnerlab.org/members/dejan_azinovic/profile.html
- http://niessnerlab.org/members/aljaz_bozic/profile.html
- http://niessnerlab.org/members/ji_hou/profile.html
- http://niessnerlab.org/members/armen_avetisyan/profile.html
- http://niessnerlab.org/team.html
- http://niessnerlab.org/members/justus_thies/profile.html

**From `blog/posts-md/2022-07-18-neural-rgb-d-surface-reconstruction.md`:**
- http://niessnerlab.org/members/dejan_azinovic/profile.html

**From `blog/posts-md/2023-07-10-panoptic-lifting.md`:**
- https://niessnerlab.org/members/yawar_siddiqui/profile.html
- https://niessnerlab.org/members/norman_mueller/profile.html
- https://niessnerlab.org/members/matthias_niessner/profile.html

**Action Items:**
1. Verify if these links are actually broken (404)
2. If broken, check if there are updated URLs
3. If the site blocks automated checkers but works manually, add to workflow exclusions

## Workflow Configuration Notes

The link checker workflow (`feat/link-check-workflow` branch) currently excludes:
- Social media: LinkedIn, Twitter/X, Facebook, Instagram, YouTube
- Academic: ResearchGate, Google Scholar, ORCID
- Services: Google Tag Manager, Google Fonts, TensorFlow.org
- Education: MathWorks, Udacity, Coursera
- Companies: TechRepublic, Tesla, Uber
- University domains: staff.qut.edu.au, services.anu.edu.au, dmi.usherb.ca
- File protocol: `file://` links

**Note:** `niessnerlab.org` is currently **NOT** excluded.

## Recommendations

1. **For niessnerlab links:**
   - Option A: Add `--exclude 'niessnerlab\.org'` to workflow if site blocks checkers but works
   - Option B: Update individual URLs if site structure changed
   - Option C: Contact site maintainers about correct URLs

2. **For future link checking:**
   - Consider running link checker locally before committing
   - Document any known-good sites that block automated checkers
   - Keep exclusion list updated

## Additional Notes

- Podcast URL `https://talking.papers.podcast.itzikbs.com/` confirmed working (not broken)
- Links that return 403 (Forbidden) are accepted by the workflow
- Links that return 404 (Not Found) will fail the check

---

**Created:** 2026-01-05
**Related Issue:** #75
**Related PR:** #76
