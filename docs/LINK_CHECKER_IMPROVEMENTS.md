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
- Separates strict checks from known flaky domains
- Auto-creates issues when links break
- Auto-updates issues on continued failures
- Auto-closes issues when links are fixed

**Why:** External sites may have temporary downtime, rate limiting, or maintenance windows. These issues shouldn't prevent you from merging code during the day.

## Configuration Changes

### Central Configuration File
**File:** `lychee.toml`

All link checking settings are now centralized in this file:

```toml
max_concurrency = 2        # Prevents rate limiting (was unlimited)
timeout = 45               # 45 second timeout per link
max_retries = 5            # Retry failed links up to 5 times
user_agent = "Mozilla..."  # Spoof Chrome browser (prevents bot blocking)
```

**Key Improvements:**
1. **Rate Limit Protection:** `max_concurrency = 2` prevents triggering rate limiters by checking at most 2 links simultaneously (slower but more stable)
2. **Browser Spoofing:** User-agent set to Chrome to avoid bot detection/blocking
3. **Smart Retries:** Up to 5 retries with proper timeout handling
4. **Centralized Exclusions:** Common problematic domains (social media, Google Fonts) excluded once

### Excluded Domains
Permanently excluded from ALL checks (in `lychee.toml`):
- Social media: LinkedIn, Twitter/X, Facebook, Instagram, YouTube
- Academic profiles: ResearchGate, Google Scholar, ORCID
- CDNs: Google Fonts, Google Tag Manager
- File protocol links

## Migration from Old Workflow

The old combined workflow (`.github/workflows/link-check.yml`) has been:
- Renamed to `link-check.yml.old` (archived for reference)
- Replaced by two new focused workflows

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

### Internal Link Detection
The internal link check uses these patterns to identify internal links:
- `--include '^/'` - Relative paths starting with `/`
- `--include '^\.'` - Relative paths starting with `.` (e.g., `../`)
- `--include 'itzikbs\.com'` - Same-domain absolute URLs

### External Link Detection
The external link check excludes internal patterns:
- `--exclude 'itzikbs\.com'` - Exclude same-domain links
- `--exclude '^/'` - Exclude relative paths
- `--exclude '^\.'` - Exclude relative paths with `.`

### Known Flaky Domains
These domains are checked in warn-only mode (don't fail the build):
- CMU Robotics Institute event pages
- Oculus developer documentation
- Various university personal pages
- Personal project domains

## Future Improvements

Potential enhancements for the future:
1. Add Slack/email notifications for nightly failures
2. Track historical link check data for trend analysis
3. Add retry logic with exponential backoff
4. Implement link checking for specific file changes only

## References
- [Lychee Documentation](https://lychee.cli.rs/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
