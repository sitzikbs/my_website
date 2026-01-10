#!/usr/bin/env python3
"""
Validate structured data (Schema.org) in HTML files.

This script extracts JSON-LD structured data from HTML files and validates
that they contain the required fields for Google Rich Results.

Usage:
    uv run python scripts/validate_schema.py [path_to_html_file]
    
    # Validate all HTML files in _site directory
    uv run python scripts/validate_schema.py _site/
    
    # Validate specific file
    uv run python scripts/validate_schema.py _site/index.html
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Any


class SchemaValidator:
    """Validator for Schema.org structured data."""
    
    # Required fields for different schema types per Google's guidelines
    REQUIRED_FIELDS = {
        "Person": ["@type", "name"],
        "BlogPosting": ["@type", "headline", "datePublished", "author"],
        "WebSite": ["@type", "name", "url"],
        "BreadcrumbList": ["@type", "itemListElement"],
        "PodcastSeries": ["@type", "name", "url"],
        "CollectionPage": ["@type", "name", "url"],
        "Blog": ["@type", "name", "url"],
        "ProfilePage": ["@type", "name", "url"],
        "ContactPage": ["@type", "name", "url"],
    }
    
    # Recommended fields for rich results
    RECOMMENDED_FIELDS = {
        "Person": ["image", "jobTitle", "url", "description", "knowsAbout", "sameAs"],
        "BlogPosting": ["image", "publisher", "dateModified", "description"],
        "WebSite": ["description", "author"],
    }
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.successes = []
    
    def extract_json_ld(self, html_content: str) -> List[Dict[str, Any]]:
        """Extract all JSON-LD scripts from HTML content."""
        pattern = r'<script\s+type="application/ld\+json"[^>]*>(.*?)</script>'
        matches = re.findall(pattern, html_content, re.DOTALL)
        
        json_ld_objects = []
        for match in matches:
            try:
                # Clean up the JSON string
                json_str = match.strip()
                obj = json.loads(json_str)
                json_ld_objects.append(obj)
            except json.JSONDecodeError as e:
                self.errors.append(f"Invalid JSON-LD: {e}")
        
        return json_ld_objects
    
    def validate_schema(self, schema: Dict[str, Any], schema_name: str = "Unknown") -> bool:
        """Validate a single schema object."""
        is_valid = True
        
        # Handle @graph structures
        if "@graph" in schema:
            for item in schema["@graph"]:
                if not self.validate_schema(item, schema_name):
                    is_valid = False
            return is_valid
        
        schema_type = schema.get("@type")
        if not schema_type:
            self.errors.append(f"{schema_name}: Missing @type field")
            return False
        
        # Check required fields
        if schema_type in self.REQUIRED_FIELDS:
            required = self.REQUIRED_FIELDS[schema_type]
            missing = [field for field in required if field not in schema]
            
            if missing:
                self.errors.append(
                    f"{schema_name} ({schema_type}): Missing required fields: {', '.join(missing)}"
                )
                is_valid = False
            else:
                self.successes.append(
                    f"{schema_name} ({schema_type}): All required fields present ✓"
                )
        
        # Check recommended fields
        if schema_type in self.RECOMMENDED_FIELDS:
            recommended = self.RECOMMENDED_FIELDS[schema_type]
            missing = [field for field in recommended if field not in schema]
            
            if missing:
                self.warnings.append(
                    f"{schema_name} ({schema_type}): Missing recommended fields: {', '.join(missing)}"
                )
        
        # Validate specific fields
        self._validate_specific_fields(schema, schema_type, schema_name)
        
        return is_valid
    
    def _validate_specific_fields(self, schema: Dict[str, Any], schema_type: str, schema_name: str):
        """Validate specific field requirements."""
        
        # Person schema validations
        if schema_type == "Person":
            # Check image
            if "image" in schema:
                image = schema["image"]
                if isinstance(image, dict):
                    if "width" not in image or "height" not in image:
                        self.warnings.append(
                            f"{schema_name}: Person image should include width and height"
                        )
                elif isinstance(image, str):
                    self.warnings.append(
                        f"{schema_name}: Person image should be ImageObject with dimensions"
                    )
            
            # Check worksFor
            if "worksFor" in schema:
                works_for = schema["worksFor"]
                if isinstance(works_for, dict) and "url" not in works_for:
                    self.warnings.append(
                        f"{schema_name}: worksFor organization should include URL"
                    )
            
            # Check alumniOf
            if "alumniOf" in schema:
                alumni = schema["alumniOf"]
                if isinstance(alumni, list):
                    for edu in alumni:
                        if edu.get("@type") == "Organization":
                            self.warnings.append(
                                f"{schema_name}: alumniOf should use CollegeOrUniversity instead of Organization"
                            )
        
        # BlogPosting validations
        elif schema_type == "BlogPosting":
            # Check author
            if "author" in schema:
                author = schema["author"]
                if isinstance(author, dict):
                    if "@type" not in author or "name" not in author:
                        self.warnings.append(
                            f"{schema_name}: BlogPosting author should have @type and name"
                        )
        
        # BreadcrumbList validations
        elif schema_type == "BreadcrumbList":
            if "itemListElement" in schema:
                items = schema["itemListElement"]
                if not isinstance(items, list) or len(items) == 0:
                    self.warnings.append(
                        f"{schema_name}: BreadcrumbList should have at least one item"
                    )
                else:
                    for i, item in enumerate(items):
                        if "position" not in item:
                            self.errors.append(
                                f"{schema_name}: BreadcrumbList item {i} missing position"
                            )
                        if "name" not in item:
                            self.errors.append(
                                f"{schema_name}: BreadcrumbList item {i} missing name"
                            )
    
    def validate_file(self, file_path: Path) -> bool:
        """Validate structured data in an HTML file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.errors.append(f"Error reading {file_path}: {e}")
            return False
        
        schemas = self.extract_json_ld(content)
        
        if not schemas:
            self.warnings.append(f"{file_path.name}: No structured data found")
            return True  # Not an error, just no schema
        
        is_valid = True
        for i, schema in enumerate(schemas):
            schema_name = f"{file_path.name} (schema {i+1})"
            if not self.validate_schema(schema, schema_name):
                is_valid = False
        
        return is_valid
    
    def print_report(self):
        """Print validation report."""
        print("\n" + "="*80)
        print("STRUCTURED DATA VALIDATION REPORT")
        print("="*80)
        
        if self.successes:
            print(f"\n✅ PASSED ({len(self.successes)}):")
            print("-" * 80)
            for success in self.successes:
                print(f"  ✓ {success}")
        
        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            print("-" * 80)
            for warning in self.warnings:
                print(f"  ⚠ {warning}")
        
        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            print("-" * 80)
            for error in self.errors:
                print(f"  ✗ {error}")
        
        print("\n" + "="*80)
        print(f"SUMMARY: {len(self.successes)} passed, {len(self.warnings)} warnings, {len(self.errors)} errors")
        print("="*80 + "\n")
        
        # Google Rich Results Test reminder
        print("📝 Next Steps:")
        print("  1. Test with Google Rich Results: https://search.google.com/test/rich-results")
        print("  2. Validate with Schema.org: https://validator.schema.org/")
        print("  3. Check Search Console for indexed structured data")
        print()


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: uv run python scripts/validate_schema.py <path>")
        print("\nExamples:")
        print("  uv run python scripts/validate_schema.py _site/")
        print("  uv run python scripts/validate_schema.py _site/index.html")
        sys.exit(1)
    
    path = Path(sys.argv[1])
    validator = SchemaValidator()
    
    if path.is_file():
        # Validate single file
        print(f"Validating {path}...")
        validator.validate_file(path)
    elif path.is_dir():
        # Validate all HTML files in directory
        html_files = list(path.rglob("*.html"))
        print(f"Found {len(html_files)} HTML files to validate...")
        
        for html_file in sorted(html_files):
            validator.validate_file(html_file)
    else:
        print(f"Error: {path} is not a valid file or directory")
        sys.exit(1)
    
    validator.print_report()
    
    # Exit with error code if there are errors
    sys.exit(1 if validator.errors else 0)


if __name__ == "__main__":
    main()
