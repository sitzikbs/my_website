#!/usr/bin/env python3
"""
Extract structured data from HTML files for manual testing.

This script extracts JSON-LD structured data from HTML files and outputs
it in a formatted way for easy copying to Google Rich Results Test tool.

Usage:
    uv run python scripts/extract_schema.py <html_file>
"""

import json
import re
import sys
from pathlib import Path


def extract_json_ld(html_content: str) -> list:
    """Extract all JSON-LD scripts from HTML content."""
    pattern = r'<script\s+type="application/ld\+json"[^>]*>(.*?)</script>'
    matches = re.findall(pattern, html_content, re.DOTALL)
    
    json_ld_objects = []
    for match in matches:
        try:
            json_str = match.strip()
            obj = json.loads(json_str)
            json_ld_objects.append(obj)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON-LD: {e}", file=sys.stderr)
    
    return json_ld_objects


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: uv run python scripts/extract_schema.py <html_file>")
        print("\nExample:")
        print("  uv run python scripts/extract_schema.py _site/index.html")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"Error: File {file_path} does not exist", file=sys.stderr)
        sys.exit(1)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)
    
    schemas = extract_json_ld(content)
    
    if not schemas:
        print(f"No structured data found in {file_path}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Found {len(schemas)} structured data block(s) in {file_path.name}")
    print("="*80)
    
    for i, schema in enumerate(schemas, 1):
        print(f"\n📋 Schema Block {i}:")
        print("-"*80)
        print(json.dumps(schema, indent=2, ensure_ascii=False))
        print("-"*80)
    
    print("\n✅ Copy the above JSON to test at:")
    print("   https://search.google.com/test/rich-results")
    print("   https://validator.schema.org/")
    print()


if __name__ == "__main__":
    main()
