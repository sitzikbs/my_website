#!/usr/bin/env python3
"""
Fix broken WordPress image links in blog posts and data files.

This script:
1. Scans JSON and markdown files for WordPress URLs
2. Maps them to local asset paths using existing image-mapping.json
3. Replaces URLs with local paths
4. Generates a report of changes

Usage:
    uv run python scripts/fix-wordpress-urls.py [--dry-run]
"""

import json
import re
import os
from pathlib import Path
from typing import Dict, List, Tuple, Set
from dataclasses import dataclass, field
import argparse


@dataclass
class UrlReplacement:
    """Represents a URL replacement operation."""
    file_path: str
    old_url: str
    new_path: str
    line_number: int = 0


@dataclass
class ReplacementReport:
    """Report of all replacements made."""
    replacements: List[UrlReplacement] = field(default_factory=list)
    files_modified: Set[str] = field(default_factory=set)
    errors: List[str] = field(default_factory=list)
    
    def add_replacement(self, replacement: UrlReplacement):
        self.replacements.append(replacement)
        self.files_modified.add(replacement.file_path)
    
    def add_error(self, error: str):
        self.errors.append(error)
    
    def print_summary(self):
        print("\n" + "="*80)
        print("WORDPRESS URL FIX REPORT")
        print("="*80)
        print(f"\nTotal replacements: {len(self.replacements)}")
        print(f"Files modified: {len(self.files_modified)}")
        print(f"Errors/Warnings: {len(self.errors)}")
        
        if self.replacements:
            print("\n" + "-"*80)
            print("SUCCESSFULLY MAPPED URLS:")
            print("-"*80)
            for file_path in sorted(self.files_modified):
                file_replacements = [r for r in self.replacements if r.file_path == file_path]
                print(f"\n{file_path} ({len(file_replacements)} replacements)")
                for i, repl in enumerate(file_replacements[:3], 1):  # Show first 3
                    print(f"  {i}. {repl.old_url[:60]}...")
                    print(f"     -> {repl.new_path}")
                if len(file_replacements) > 3:
                    print(f"  ... and {len(file_replacements) - 3} more")
        
        # Categorize errors
        missing_images = [e for e in self.errors if 'No local path found' in e and not any(ext in e for ext in ['.pdf', '.zip'])]
        missing_docs = [e for e in self.errors if 'Document file needs manual handling' in e]
        
        if missing_images:
            print("\n" + "-"*80)
            print("IMAGES NOT YET DOWNLOADED (need to download from WordPress):")
            print("-"*80)
            # Extract unique URLs
            urls = set()
            for error in missing_images:
                match = re.search(r'(https?://[^\s]+)', error)
                if match:
                    urls.add(match.group(1))
            for i, url in enumerate(sorted(urls)[:20], 1):  # Show first 20
                print(f"  {i}. {url}")
            if len(urls) > 20:
                print(f"  ... and {len(urls) - 20} more")
        
        if missing_docs:
            print("\n" + "-"*80)
            print("DOCUMENT FILES (PDFs, ZIPs) - NEED MANUAL DOWNLOAD:")
            print("-"*80)
            # Extract unique URLs
            urls = set()
            for error in missing_docs:
                match = re.search(r'(https?://[^\s]+\.(?:pdf|zip))', error)
                if match:
                    urls.add(match.group(1))
            for i, url in enumerate(sorted(urls), 1):
                print(f"  {i}. {url}")
    
    def save_missing_urls_report(self, output_file: Path):
        """Save a report of missing URLs to a file for batch downloading."""
        missing_images = [e for e in self.errors if 'No local path found' in e and not any(ext in e for ext in ['.pdf', '.zip'])]
        missing_docs = [e for e in self.errors if 'Document file needs manual handling' in e]
        
        # Extract unique URLs
        image_urls = set()
        for error in missing_images:
            match = re.search(r'(https?://[^\s]+)', error)
            if match:
                url = match.group(1).split()[0]  # Remove any trailing text
                image_urls.add(url)
        
        doc_urls = set()
        for error in missing_docs:
            match = re.search(r'(https?://[^\s]+\.(?:pdf|zip))', error)
            if match:
                doc_urls.add(match.group(1))
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# Missing WordPress URLs Report\n\n")
            f.write(f"Generated: {Path.cwd()}\n\n")
            
            f.write("## Images to Download\n\n")
            f.write(f"Total: {len(image_urls)}\n\n")
            for url in sorted(image_urls):
                f.write(f"- {url}\n")
            
            f.write("\n## Document Files to Download\n\n")
            f.write(f"Total: {len(doc_urls)}\n\n")
            for url in sorted(doc_urls):
                f.write(f"- {url}\n")
        
        print(f"\n✓ Saved missing URLs report to: {output_file}")


class WordPressUrlFixer:
    """Fixes WordPress URLs in website files."""
    
    # WordPress URL patterns to match
    WP_PATTERNS = [
        r'https://www\.itzikbs\.com/wp-content/uploads/',
        r'http://www\.itzikbs\.com/wp-content/uploads/',
        r'https://i0\.wp\.com/www\.itzikbs\.com/wp-content/uploads/',
    ]
    
    def __init__(self, root_dir: Path, mapping_file: Path):
        self.root_dir = root_dir
        self.mapping_file = mapping_file
        self.url_mapping = self._load_mapping()
        self.report = ReplacementReport()
        
    def _load_mapping(self) -> Dict[str, str]:
        """Load existing image mapping from JSON file."""
        try:
            with open(self.mapping_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Warning: Could not load mapping file: {e}")
            return {}
    
    def _normalize_url(self, url: str) -> str:
        """Normalize URL by removing query parameters and HTML entities."""
        # Remove query parameters
        url = url.split('?')[0]
        # Decode HTML entities
        url = url.replace('&amp;', '&')
        return url
    
    def _find_local_path(self, wp_url: str) -> str:
        """Find local path for a WordPress URL."""
        normalized_url = self._normalize_url(wp_url)
        
        # Try exact match first
        if wp_url in self.url_mapping:
            return self.url_mapping[wp_url]
        
        if normalized_url in self.url_mapping:
            return self.url_mapping[normalized_url]
        
        # Try to extract filename and search for it
        filename = Path(normalized_url).name
        
        # Search in image mapping for similar filename
        for mapped_url, local_path in self.url_mapping.items():
            if filename in local_path:
                return local_path
        
        # Try to construct path from URL structure
        # Extract path after /uploads/
        match = re.search(r'/wp-content/uploads/(.+)', normalized_url)
        if match:
            rel_path = match.group(1)
            filename = Path(rel_path).name
            
            # Check if file exists in blog images
            potential_paths = [
                f"assets/images/blog/{filename}",
                f"assets/images/general/{filename}",
                f"assets/images/publications/{filename}",
            ]
            
            for path in potential_paths:
                full_path = self.root_dir / path
                if full_path.exists():
                    return path
        
        return None
    
    def _is_wordpress_url(self, url: str) -> bool:
        """Check if URL is a WordPress URL."""
        for pattern in self.WP_PATTERNS:
            if re.search(pattern, url):
                return True
        return False
    
    def _fix_json_file(self, file_path: Path, dry_run: bool = False) -> None:
        """Fix WordPress URLs in a JSON file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            replacements_in_file = []
            
            # Find all WordPress URLs
            for pattern in self.WP_PATTERNS:
                for match in re.finditer(pattern + r'[^\s"\']+', content):
                    wp_url = match.group(0)
                    local_path = self._find_local_path(wp_url)
                    
                    if local_path:
                        replacement = UrlReplacement(
                            file_path=str(file_path.relative_to(self.root_dir)),
                            old_url=wp_url,
                            new_path=local_path
                        )
                        replacements_in_file.append(replacement)
                        self.report.add_replacement(replacement)
                        content = content.replace(wp_url, local_path)
                    else:
                        self.report.add_error(f"No local path found for: {wp_url} in {file_path}")
            
            # Write back if changes were made
            if content != original_content and not dry_run:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✓ Fixed {len(replacements_in_file)} URLs in {file_path.name}")
            elif content != original_content:
                print(f"[DRY RUN] Would fix {len(replacements_in_file)} URLs in {file_path.name}")
                
        except Exception as e:
            self.report.add_error(f"Error processing {file_path}: {e}")
    
    def _fix_markdown_file(self, file_path: Path, dry_run: bool = False) -> None:
        """Fix WordPress URLs in a markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            modified = False
            replacements_in_file = []
            
            for line_num, line in enumerate(lines, 1):
                original_line = line
                
                # Find all WordPress URLs in the line
                for pattern in self.WP_PATTERNS:
                    for match in re.finditer(pattern + r'[^\s"\'<>)]+', line):
                        wp_url = match.group(0)
                        local_path = self._find_local_path(wp_url)
                        
                        if local_path:
                            replacement = UrlReplacement(
                                file_path=str(file_path.relative_to(self.root_dir)),
                                old_url=wp_url,
                                new_path=local_path,
                                line_number=line_num
                            )
                            replacements_in_file.append(replacement)
                            self.report.add_replacement(replacement)
                            line = line.replace(wp_url, local_path)
                        else:
                            # Check if it's a document file (PDF, ZIP)
                            if wp_url.endswith(('.pdf', '.zip')):
                                self.report.add_error(
                                    f"Document file needs manual handling: {wp_url} "
                                    f"in {file_path} (line {line_num})"
                                )
                            else:
                                self.report.add_error(
                                    f"No local path found for: {wp_url} "
                                    f"in {file_path} (line {line_num})"
                                )
                
                if line != original_line:
                    modified = True
                    lines[line_num - 1] = line
            
            # Write back if changes were made
            if modified and not dry_run:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                print(f"✓ Fixed {len(replacements_in_file)} URLs in {file_path.name}")
            elif modified:
                print(f"[DRY RUN] Would fix {len(replacements_in_file)} URLs in {file_path.name}")
                
        except Exception as e:
            self.report.add_error(f"Error processing {file_path}: {e}")
    
    def fix_all(self, dry_run: bool = False) -> ReplacementReport:
        """Fix WordPress URLs in all relevant files."""
        print(f"Starting WordPress URL fix {'(DRY RUN)' if dry_run else ''}...")
        print(f"Root directory: {self.root_dir}")
        print(f"Loaded {len(self.url_mapping)} URL mappings")
        
        # Fix JSON files in data/
        print("\n" + "="*80)
        print("Processing JSON files...")
        print("="*80)
        data_dir = self.root_dir / 'data'
        for json_file in data_dir.glob('*.json'):
            if json_file.name != 'image-mapping.json':  # Skip the mapping file itself
                print(f"\nProcessing {json_file.name}...")
                self._fix_json_file(json_file, dry_run)
        
        # Fix markdown files in blog/posts-md/
        print("\n" + "="*80)
        print("Processing Markdown files...")
        print("="*80)
        blog_dir = self.root_dir / 'blog' / 'posts-md'
        if blog_dir.exists():
            md_files = list(blog_dir.glob('*.md'))
            print(f"Found {len(md_files)} markdown files")
            for md_file in md_files:
                print(f"\nProcessing {md_file.name}...")
                self._fix_markdown_file(md_file, dry_run)
        
        return self.report


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Fix broken WordPress image links in blog posts and data files.'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without actually modifying files'
    )
    parser.add_argument(
        '--save-missing',
        type=str,
        default='scripts/missing-wordpress-urls.md',
        help='Path to save report of missing URLs (default: scripts/missing-wordpress-urls.md)'
    )
    args = parser.parse_args()
    
    # Setup paths
    root_dir = Path(__file__).parent.parent
    mapping_file = root_dir / 'data' / 'image-mapping.json'
    
    # Create fixer and run
    fixer = WordPressUrlFixer(root_dir, mapping_file)
    report = fixer.fix_all(dry_run=args.dry_run)
    
    # Print summary
    report.print_summary()
    
    # Save missing URLs report
    if args.save_missing:
        output_file = root_dir / args.save_missing
        report.save_missing_urls_report(output_file)
    
    if args.dry_run:
        print("\n" + "="*80)
        print("This was a DRY RUN. No files were modified.")
        print("Run without --dry-run to apply changes.")
        print("="*80)
    else:
        print("\n" + "="*80)
        print("All changes have been applied!")
        print("Please review the changes and test the site.")
        print("="*80)


if __name__ == '__main__':
    main()
