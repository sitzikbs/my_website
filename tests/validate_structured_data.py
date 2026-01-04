#!/usr/bin/env python3
"""
Validate structured data (Schema.org) in HTML files.
Tests compliance with Google Rich Results requirements.
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple


def extract_json_ld(html_content: str) -> List[Dict]:
    """Extract all JSON-LD structured data from HTML."""
    pattern = r'<script type="application/ld\+json">\s*(.*?)\s*</script>'
    matches = re.findall(pattern, html_content, re.DOTALL)
    
    json_ld_objects = []
    for match in matches:
        try:
            data = json.loads(match)
            json_ld_objects.append(data)
        except json.JSONDecodeError as e:
            print(f"⚠️  JSON parsing error: {e}")
            continue
    
    return json_ld_objects


def validate_person_schema(data: Dict) -> Tuple[bool, List[str]]:
    """Validate Person schema requirements."""
    issues = []
    
    # Check required properties
    if "name" not in data:
        issues.append("Missing required property: name")
    
    # Check recommended properties
    if "image" not in data:
        issues.append("Missing recommended property: image")
    
    if "url" not in data:
        issues.append("Missing recommended property: url")
    
    # Check additional recommended properties
    if "jobTitle" not in data:
        issues.append("Missing recommended property: jobTitle")
    
    if "description" not in data:
        issues.append("Missing recommended property: description (improves rich results)")
    
    if "sameAs" not in data or not data.get("sameAs"):
        issues.append("Missing recommended property: sameAs (social profiles)")
    
    return len(issues) == 0, issues


def validate_website_schema(data: Dict) -> Tuple[bool, List[str]]:
    """Validate WebSite schema requirements."""
    issues = []
    
    if "name" not in data:
        issues.append("Missing required property: name")
    
    if "url" not in data:
        issues.append("Missing required property: url")
    
    # Check for SearchAction (enables sitelinks search box)
    if "potentialAction" not in data:
        issues.append("Missing potentialAction (enables sitelinks search box)")
    else:
        action = data["potentialAction"]
        if action.get("@type") != "SearchAction":
            issues.append("potentialAction should be SearchAction type")
        
        if "target" not in action:
            issues.append("SearchAction missing target property")
        
        if "query-input" not in action:
            issues.append("SearchAction missing query-input property")
    
    return len(issues) == 0, issues


def validate_blog_posting_schema(data: Dict) -> Tuple[bool, List[str]]:
    """Validate BlogPosting schema requirements."""
    issues = []
    
    # Required properties
    required = ["headline", "image", "datePublished", "author"]
    for prop in required:
        if prop not in data:
            issues.append(f"Missing required property: {prop}")
    
    # Check author structure
    if "author" in data:
        author = data["author"]
        if isinstance(author, dict):
            if "@type" not in author or author["@type"] != "Person":
                issues.append("author should have @type: Person")
            if "name" not in author:
                issues.append("author missing name property")
    
    return len(issues) == 0, issues


def validate_structured_data(file_path: Path) -> Dict:
    """Validate all structured data in an HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except Exception as e:
        return {
            "file": str(file_path),
            "error": f"Failed to read file: {e}",
            "valid": False
        }
    
    json_ld_objects = extract_json_ld(html_content)
    
    if not json_ld_objects:
        return {
            "file": str(file_path),
            "error": "No structured data found",
            "valid": False
        }
    
    results = {
        "file": str(file_path),
        "schemas": [],
        "valid": True
    }
    
    for idx, data in enumerate(json_ld_objects):
        schema_type = data.get("@type", "Unknown")
        
        # Handle @graph (multiple schemas in one)
        if "@graph" in data:
            for item in data["@graph"]:
                item_type = item.get("@type", "Unknown")
                if isinstance(item_type, list):
                    item_type = ", ".join(item_type)
                
                schema_result = {"type": item_type, "issues": []}
                
                # Validate based on type
                if "Person" in str(item_type):
                    valid, issues = validate_person_schema(item)
                    schema_result["valid"] = valid
                    schema_result["issues"] = issues
                    if not valid:
                        results["valid"] = False
                
                elif item_type == "WebSite":
                    valid, issues = validate_website_schema(item)
                    schema_result["valid"] = valid
                    schema_result["issues"] = issues
                    if not valid:
                        results["valid"] = False
                
                results["schemas"].append(schema_result)
        
        else:
            # Single schema
            if isinstance(schema_type, list):
                schema_type = ", ".join(schema_type)
            
            schema_result = {"type": schema_type, "issues": []}
            
            if "Person" in str(schema_type):
                valid, issues = validate_person_schema(data)
                schema_result["valid"] = valid
                schema_result["issues"] = issues
                if not valid:
                    results["valid"] = False
            
            elif schema_type == "WebSite":
                valid, issues = validate_website_schema(data)
                schema_result["valid"] = valid
                schema_result["issues"] = issues
                if not valid:
                    results["valid"] = False
            
            elif schema_type == "BlogPosting":
                valid, issues = validate_blog_posting_schema(data)
                schema_result["valid"] = valid
                schema_result["issues"] = issues
                if not valid:
                    results["valid"] = False
            
            results["schemas"].append(schema_result)
    
    return results


def main():
    """Main function to validate structured data."""
    site_dir = Path("_site")
    
    if not site_dir.exists():
        print("❌ Error: _site directory not found. Build the site first.")
        sys.exit(1)
    
    # Test homepage
    print("=" * 70)
    print("🔍 Validating Homepage Structured Data")
    print("=" * 70)
    
    homepage = site_dir / "index.html"
    if homepage.exists():
        result = validate_structured_data(homepage)
        
        print(f"\n📄 File: {result['file']}")
        
        if "error" in result:
            print(f"❌ {result['error']}")
        else:
            for schema in result["schemas"]:
                print(f"\n📋 Schema Type: {schema['type']}")
                
                if "valid" in schema:
                    if schema["valid"]:
                        print("   ✅ Valid")
                    else:
                        print("   ⚠️  Issues found:")
                        for issue in schema["issues"]:
                            print(f"      - {issue}")
                else:
                    print("   ℹ️  Not validated (type not recognized)")
        
        if result["valid"]:
            print("\n✅ Homepage structured data is valid!")
        else:
            print("\n⚠️  Homepage has some issues that should be addressed.")
    else:
        print(f"❌ Homepage not found at {homepage}")
    
    # Test a sample blog post
    print("\n" + "=" * 70)
    print("🔍 Validating Blog Post Structured Data")
    print("=" * 70)
    
    blog_posts_dir = site_dir / "blog" / "posts"
    if blog_posts_dir.exists():
        blog_posts = list(blog_posts_dir.glob("*.html"))
    else:
        blog_posts = []
    
    if blog_posts:
        sample_post = blog_posts[0]
        result = validate_structured_data(sample_post)
        
        print(f"\n📄 Sample File: {sample_post.name}")
        
        if "error" in result:
            print(f"❌ {result['error']}")
        else:
            for schema in result["schemas"]:
                print(f"\n📋 Schema Type: {schema['type']}")
                
                if "valid" in schema:
                    if schema["valid"]:
                        print("   ✅ Valid")
                    else:
                        print("   ⚠️  Issues found:")
                        for issue in schema["issues"]:
                            print(f"      - {issue}")
                else:
                    print("   ℹ️  Not validated")
        
        if result["valid"]:
            print("\n✅ Blog post structured data is valid!")
        else:
            print("\n⚠️  Blog post has some issues that should be addressed.")
    else:
        print("\nℹ️  No blog posts found or blog directory doesn't exist.")
        print("   This is OK if blog posts haven't been generated yet.")
    
    print("\n" + "=" * 70)
    print("📊 Validation Summary")
    print("=" * 70)
    print("\n✅ Next Steps:")
    print("1. Test with Google Rich Results Test:")
    print("   https://search.google.com/test/rich-results")
    print("2. Validate JSON-LD syntax:")
    print("   https://validator.schema.org/")
    print("3. Deploy and monitor in Google Search Console")
    print("\n")


if __name__ == "__main__":
    main()
