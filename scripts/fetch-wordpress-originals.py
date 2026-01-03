#!/usr/bin/env python3
"""
Extract WordPress backup and replace local images with high-quality originals.

This script:
1. Extracts tar.gz backup to /tmp/wordpress-backup/
2. Navigates to wp-content/uploads/ directory structure (YYYY/MM/)
3. Matches local date-prefixed filenames to server paths
4. Compares file sizes and copies higher quality originals
5. Logs all replacements and cleans up temp directory
"""

import re
import shutil
import tarfile
from pathlib import Path


def extract_date_from_filename(filename):
    """Extract year and month from date-prefixed filename.
    
    Args:
        filename: Filename like '2017-03-image.jpg' or '2017-03-24-image.jpg'
        
    Returns:
        tuple: (year, month) or (None, None) if no date prefix
    """
    match = re.match(r'^(\d{4})-(\d{2})', filename)
    if match:
        return match.group(1), match.group(2)
    return None, None


def get_base_filename(filename):
    """Remove date prefix and get base filename.
    
    Args:
        filename: Filename like '2017-03-image.jpg'
        
    Returns:
        str: Base filename like 'image.jpg'
    """
    # Remove YYYY-MM- or YYYY-MM-DD- prefix
    cleaned = re.sub(r'^\d{4}-\d{2}(-\d{2})?-', '', filename)
    return cleaned


def is_variant(filename):
    """Check if filename is a WordPress variant (not an original).
    
    Args:
        filename: Filename to check
        
    Returns:
        bool: True if it's a variant (scaled, size suffix)
    """
    # Skip -scaled versions and size variants like -300x169, -1024x768
    if '-scaled' in filename or re.search(r'-\d+x\d+\.(jpg|jpeg|png|gif)$', filename):
        return True
    return False


def extract_backup(tar_path, extract_to):
    """Extract tar.gz backup to temporary directory.
    
    Args:
        tar_path: Path to the tar.gz backup file
        extract_to: Directory to extract to
    """
    print(f"📦 Extracting backup from {tar_path}...")
    print("⏳ This may take a few minutes for large backups...")
    with tarfile.open(tar_path, 'r:gz') as tar:
        # Use data filter for Python 3.12+ compatibility
        tar.extractall(extract_to, filter='data')
    print(f"✅ Extracted to {extract_to}")


def find_wordpress_uploads_dir(base_path):
    """Find the wp-content/uploads directory in the extracted backup.
    
    Args:
        base_path: Base path of extracted backup
        
    Returns:
        Path: Path to uploads directory
    """
    # Expected structure: backup/homedir/sites/itzikbs.com/wp-content/uploads/
    uploads_path = (
        base_path
        / 'backup'
        / 'homedir'
        / 'sites'
        / 'itzikbs.com'
        / 'wp-content'
        / 'uploads'
    )
    
    if not uploads_path.exists():
        raise FileNotFoundError(f"WordPress uploads directory not found at {uploads_path}")
    
    print(f"📁 Found WordPress uploads at {uploads_path}")
    return uploads_path


def match_and_replace_images(local_dir, wp_uploads_dir):
    """Match local images to WordPress originals and replace with higher quality.
    
    Args:
        local_dir: Path to local images directory (assets/images/blog)
        wp_uploads_dir: Path to WordPress uploads directory
        
    Returns:
        dict: Statistics about replacements
    """
    stats = {
        'checked': 0,
        'replaced': 0,
        'skipped_no_match': 0,
        'skipped_lower_quality': 0,
        'total_size_before': 0,
        'total_size_after': 0,
    }
    
    replacements = []
    
    # Process each local image
    for local_file in sorted(local_dir.glob('*')):
        if not local_file.is_file() or local_file.name == '.gitkeep':
            continue
            
        stats['checked'] += 1
        filename = local_file.name
        
        # Extract date and base filename
        year, month = extract_date_from_filename(filename)
        base_name = get_base_filename(filename)
        
        # Try to find matching WordPress file
        wp_file = None
        
        if year and month:
            # Look in YYYY/MM/ directory for original (non-variant) files
            year_month_dir = wp_uploads_dir / year / month
            if year_month_dir.exists():
                # Try base name first (original)
                candidate = year_month_dir / base_name
                if candidate.exists() and not is_variant(candidate.name):
                    wp_file = candidate
                else:
                    # Try with date prefix in case it exists on server
                    candidate_with_date = year_month_dir / filename
                    if candidate_with_date.exists() and not is_variant(candidate_with_date.name):
                        wp_file = candidate_with_date
        
        if not wp_file:
            stats['skipped_no_match'] += 1
            continue
        
        # Compare file sizes
        local_size = local_file.stat().st_size
        wp_size = wp_file.stat().st_size
        
        stats['total_size_before'] += local_size
        
        # Replace if WordPress version is larger (higher quality)
        if wp_size > local_size:
            size_improvement = wp_size - local_size
            improvement_pct = (size_improvement / local_size) * 100
            
            # Backup and replace
            shutil.copy2(wp_file, local_file)
            stats['replaced'] += 1
            stats['total_size_after'] += wp_size
            
            replacements.append({
                'filename': filename,
                'old_size': local_size,
                'new_size': wp_size,
                'improvement_mb': size_improvement / (1024 * 1024),
                'improvement_pct': improvement_pct,
            })
            
            print(
                f"✅ {filename}: {local_size / 1024:.1f}KB → {wp_size / 1024:.1f}KB "
                f"(+{improvement_pct:.1f}%)"
            )
        else:
            stats['skipped_lower_quality'] += 1
            stats['total_size_after'] += local_size
    
    return stats, replacements


def main():
    """Main function to orchestrate the backup extraction and image replacement."""
    # Paths
    tar_path = Path(
        '/mnt/c/Users/sitzi/Downloads/'
        'download_havrakon_1767420934_64223.tar.gz'
    )
    temp_dir = Path('/tmp/wordpress-backup')
    local_images = Path('assets/images/blog')
    
    # Verify tar file exists
    if not tar_path.exists():
        print(f"❌ Backup file not found: {tar_path}")
        print("Please verify the path to your WordPress backup tar.gz file")
        return
    
    # Check if already extracted
    wp_uploads_check = (
        temp_dir
        / 'backup'
        / 'homedir'
        / 'sites'
        / 'itzikbs.com'
        / 'wp-content'
        / 'uploads'
    )
    
    if wp_uploads_check.exists():
        print(f"✅ Backup already extracted at {temp_dir}")
    else:
        # Clean temp directory if it exists
        if temp_dir.exists():
            print(f"🧹 Cleaning existing temp directory...")
            shutil.rmtree(temp_dir)
        
        temp_dir.mkdir(parents=True, exist_ok=True)
        
        # Extract backup
        extract_backup(tar_path, temp_dir)
    
    try:
        
        # Find WordPress uploads directory
        wp_uploads = find_wordpress_uploads_dir(temp_dir)
        
        # Match and replace images
        print("\n🔍 Matching local images to WordPress originals...\n")
        stats, replacements = match_and_replace_images(local_images, wp_uploads)
        
        # Print summary
        print("\n" + "=" * 70)
        print("📊 REPLACEMENT SUMMARY")
        print("=" * 70)
        print(f"Total images checked: {stats['checked']}")
        print(f"Images replaced: {stats['replaced']}")
        print(f"Skipped (no match): {stats['skipped_no_match']}")
        print(f"Skipped (lower quality): {stats['skipped_lower_quality']}")
        print(
            f"Total size improvement: "
            f"{(stats['total_size_after'] - stats['total_size_before']) / (1024 * 1024):.2f} MB"
        )
        
        if replacements:
            print("\n📈 Top 10 Improvements:")
            for item in sorted(replacements, key=lambda x: x['improvement_mb'], reverse=True)[:10]:
                print(
                    f"  {item['filename']}: "
                    f"+{item['improvement_mb']:.2f} MB (+{item['improvement_pct']:.1f}%)"
                )
        
    finally:
        # Clean up temp directory
        print(f"\n🧹 Cleaning up {temp_dir}...")
        shutil.rmtree(temp_dir)
        print("✅ Cleanup complete")


if __name__ == "__main__":
    main()
