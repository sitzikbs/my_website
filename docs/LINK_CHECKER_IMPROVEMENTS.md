# Link Checker Improvements

## Overview
This document explains the improvements made to the link checking workflows to address inconsistent build failures due to external site timeouts and rate limiting.

## Problem Statement
The original link checker had issues with:
- Inconsistent results (pass/fail) for the same website state
- Timeouts from external sites blocking PR merges
- Rate limiting from checking many links concurrently
- Long exclude list that needed constant updates

## Solution: Two-Tier Link Checking Strategy

### 1. Internal Link Check (PR Workflow)
**File:** `.github/workflows/link-check-internal.yml`

**Trigger:** Runs on every pull request to `main`

**Purpose:** Ensures internal site structure is solid before merging

**Behavior:**
- Checks ONLY internal links (relative paths like `/blog/post.html`, same-domain links)
- **FAILS the PR** if broken internal links are detected
- Adds a comment to the PR with details about the failure
- Fast and reliable (no external dependencies)

**Why:** Internal links are under our control and must always work. Breaking them indicates a real problem in the code being merged.

### 2. External Link Check (Nightly Workflow)
**File:** `.github/workflows/link-check-external.yml`

**Trigger:** Runs daily at 2:00 AM UTC (off-peak hours)

**Purpose:** Monitors external links without blocking development

**Behavior:**
- Checks ONLY external third-party links
- **DOES NOT block PRs** - creates/updates GitHub issues instead
- Auto-creates issues when links break
- Auto-updates issues on continued failures
- Auto-closes issues when links are fixed

**Why:** External sites may have temporary downtime, rate limiting, or maintenance windows. These issues shouldn't prevent you from merging code during the day.

## Configuration Changes

### Central Configuration File
**File:** `lychee.toml`

**All link checking settings are centralized in this single file as the source of truth:**

```toml
max_concurrency = 2        # Prevents rate limiting (was unlimited)
timeout = 45               # 45 second timeout per link
max_retries = 5            # Retry failed links up to 5 times
user_agent = "Mozilla..."  # Spoof Chrome browser (prevents bot blocking)
```

**Key Improvements:**
1. **Single Source of Truth:** All exclusions and settings defined in `lychee.toml` - no duplication in workflow files
2. **Rate Limit Protection:** `max_concurrency = 2` prevents triggering rate limiters by checking at most 2 links simultaneously (slower but more stable)
3. **Browser Spoofing:** User-agent set to Chrome 132 to avoid bot detection/blocking
4. **Smart Retries:** Up to 5 retries with proper timeout handling
5. **Centralized Exclusions:** All problematic domains (social media, CDNs, academic sites) excluded in one place

### Excluded Domains
Permanently excluded from ALL checks (in `lychee.toml`):
- **Social media:** LinkedIn, Twitter/X, Facebook, Instagram, YouTube
- **Academic profiles:** ResearchGate, Google Scholar, ORCID
- **CDNs:** Google Fonts, Google Tag Manager, Cloudflare cdn-cgi
- **Problematic external sites:** TensorFlow, Uber, Coursera, Roblox, Mathworks, etc.
- **Academic/university sites:** Various .edu domains and university-specific sites
- **File protocol links:** All file:// URLs
- **Performance hints:** Exact URLs for preconnect/dns-prefetch (not actual links)

## Migration from Old Workflow

The old combined workflow (`.github/workflows/link-check.yml`) has been replaced by two new focused workflows with centralized configuration.

## Benefits

1. **Reliability:** PRs no longer fail due to temporary external site issues
2. **Speed:** Internal link checks are faster (fewer links to check)
3. **Visibility:** External link issues are tracked via GitHub issues
4. **Stability:** Lower concurrency prevents rate limiting
5. **Maintainability:** Centralized configuration in `lychee.toml`
6. **Developer Experience:** Can merge code even if external sites are down

## Usage

### For Developers
- **PR checks:** Your PR will fail if you break internal links (fix before merging)
- **External links:** Check GitHub issues for reports of broken external links (fix when convenient)

### Manual Testing
Both workflows can be triggered manually:
1. Go to GitHub Actions tab
2. Select "Link Checker (Internal) - PR" or "Link Checker (External) - Nightly"
3. Click "Run workflow"

### Viewing Results
- **PR checks:** Results appear in PR status checks
- **Nightly checks:** Check the "Actions" tab or GitHub issues labeled `broken-links`

## Implementation Details

### Workflow Configuration Strategy

Both workflows use the centralized `lychee.toml` configuration file and only add workflow-specific arguments:

**Internal Workflow:** 
- Uses `lychee.toml` for all exclusions and settings
- No additional exclusions needed (all handled centrally)
- Simple and maintainable

**External Workflow:**
- Uses `lychee.toml` for all exclusions and settings
- Adds only internal domain exclusion patterns to define what counts as "external":
  - `--exclude 'itzikbs\.com'` - Exclude same-domain links
  - `--exclude '^/'` - Exclude relative paths starting with `/`
  - `--exclude '^\.'` - Exclude relative paths starting with `.` (e.g., `../`)

### Known Problematic Domains

All problematic domains are excluded globally in `lychee.toml`:
- Bot-detecting sites (LinkedIn, Facebook, Instagram, etc.)
- Rate-limiting sites (academic publishers, university sites)
- Unreliable sites (personal domains, broken redirects)
- CDN/performance hints (Google Fonts, Tag Manager base URLs)

## Future Improvements

Potential enhancements for the future:
1. Add Slack/email notifications for nightly failures
2. Track historical link check data for trend analysis
3. Add retry logic with exponential backoff
4. Implement link checking for specific file changes only

## References
- [Lychee Documentation](https://lychee.cli.rs/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
