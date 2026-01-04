# Backup & Recovery Procedures

This document outlines backup and recovery procedures for the website.

## Overview

The website uses a multi-layered backup approach:
- **Git version control** provides code and content history
- **Cloudflare Pages** maintains deployment history with rollback capability
- **GitHub** serves as the remote backup repository

---

## Git Version Control Recovery

### Restoring Deleted Files

If you accidentally delete a file:

```bash
# Restore a specific file from the last commit
git checkout HEAD -- path/to/file.html

# Restore a file from a specific commit
git checkout <commit-hash> -- path/to/file.html
```

### Reverting Commits

To undo recent commits:

```bash
# Undo last commit but keep changes
git reset --soft HEAD~1

# Undo last commit and discard changes
git reset --hard HEAD~1

# Revert a specific commit (creates new commit)
git revert <commit-hash>
```

### Finding Lost Content

Search through Git history to find deleted content:

```bash
# Find commits that modified a specific file
git log -- path/to/file.html

# Search for text in commit history
git log -S "search text" --source --all

# View file content from a specific commit
git show <commit-hash>:path/to/file.html
```

### Recovering from Uncommitted Changes

If you made changes but didn't commit:

```bash
# Discard all uncommitted changes
git checkout .

# Discard changes to a specific file
git checkout -- path/to/file.html

# View uncommitted changes
git diff
```

---

## Cloudflare Pages Deployment Recovery

### Rollback to Previous Deployment

Cloudflare Pages maintains a history of all deployments. To rollback:

1. **Access Cloudflare Pages Dashboard:**
   - Go to [pages.cloudflare.com](https://pages.cloudflare.com)
   - Select your project (itzikbs-website)

2. **Navigate to Deployments:**
   - Click "Deployments" tab
   - View list of all past deployments with timestamps

3. **Rollback Process:**
   - Find the last known good deployment
   - Click "Rollback to this deployment"
   - Wait ~30 seconds for rollback to complete
   - Verify site loads correctly at https://itzikbs.com

### Viewing Deployment Logs

To troubleshoot deployment issues:

1. Go to Cloudflare Pages → Your project → Deployments
2. Click on a specific deployment
3. View build logs to identify errors
4. Check build settings if needed

### Manual Redeployment

Force a fresh deployment:

1. **Option A: Trigger via Git**
   ```bash
   # Make a trivial change and push
   git commit --allow-empty -m "Trigger redeployment"
   git push origin main
   ```

2. **Option B: Trigger via Dashboard**
   - Go to Cloudflare Pages → Deployments
   - Click "Retry deployment" on any past deployment
   - Or use "Manage deployment" → "Deploy site"

---

## Data Recovery

### Publications and News Data

Content stored in JSON files:
- `data/publications.json`
- `data/news.json`
- `data/blog.json`

**Recovery steps:**

```bash
# View history of data file
git log -- data/publications.json

# Restore from specific commit
git show <commit-hash>:data/publications.json > data/publications.json

# Compare current with previous version
git diff HEAD~1 data/publications.json
```

### Blog Posts Recovery

Blog posts are in `blog/posts-md/`:

```bash
# List deleted blog posts
git log --diff-filter=D --summary -- blog/posts-md/

# Restore specific blog post
git checkout <commit-hash> -- blog/posts-md/post-name.md
```

### Asset Recovery

Images and documents in `assets/`:

```bash
# Find when asset was deleted
git log --all --full-history -- assets/images/photo.jpg

# Restore asset
git checkout <commit-hash> -- assets/images/photo.jpg
```

---

## Emergency Full Recovery

### Complete Site Recovery from GitHub

If you need to completely rebuild from scratch:

```bash
# Clone fresh copy
git clone https://github.com/sitzikbs/my_website.git
cd my_website

# Install dependencies
npm install

# Build site
npm run build

# Test locally
npm run serve
```

Then redeploy to Cloudflare Pages (will auto-deploy on push to main).

### Recovering to Specific Point in Time

```bash
# Find commit at specific date
git log --before="2026-01-01" --after="2025-12-01"

# Create new branch from that commit
git checkout -b recovery-branch <commit-hash>

# Verify it looks correct
npm run build
npm run serve

# If good, merge to main
git checkout main
git merge recovery-branch
git push origin main
```

---

## Preventive Measures

### Before Major Changes

1. **Create a backup branch:**
   ```bash
   git checkout -b backup-$(date +%Y%m%d)
   git push origin backup-$(date +%Y%m%d)
   ```

2. **Tag important releases:**
   ```bash
   git tag -a v1.0 -m "Release version 1.0"
   git push origin v1.0
   ```

3. **Test changes locally before deploying:**
   ```bash
   npm run build
   npm run serve
   ```

### Regular Maintenance

- **Keep main branch stable**: Use feature branches for development
- **Commit frequently**: Small, focused commits are easier to revert
- **Write clear commit messages**: Follow Conventional Commits format
- **Test before pushing**: Run local build/serve to verify changes
- **Monitor deployments**: Check Cloudflare Pages dashboard after pushing

---

## Backup Verification

Periodically verify backups are working:

```bash
# Verify Git history is intact
git log --oneline --graph --decorate --all

# Verify remote backups
git remote -v
git fetch origin
git branch -r

# Verify builds work
npm run build

# Check deployment history (via Cloudflare Pages dashboard)
```

---

## Additional Resources

- **Cloudflare Pages Documentation**: https://developers.cloudflare.com/pages/
- **Git Documentation**: https://git-scm.com/doc
- **Repository**: https://github.com/sitzikbs/my_website
- **Deployment Guide**: [CLOUDFLARE_DEPLOYMENT.md](CLOUDFLARE_DEPLOYMENT.md)

---

**Last Updated:** January 4, 2026
