#!/usr/bin/env python3
"""
Content Validation Script
Validates publications.json and blog-index.json for correctness
"""

import json
import sys
from pathlib import Path
from datetime import datetime

def validate_json_syntax(filepath):
    """Validate JSON syntax"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            json.load(f)
        return True, "Valid JSON syntax"
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {e}"
    except FileNotFoundError:
        return False, f"File not found: {filepath}"

def validate_publications(filepath):
    """Validate publications.json structure and content"""
    errors = []
    warnings = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        return [f"Cannot read file: {e}"], []
    
    # Check required top-level keys
    if 'publications' not in data:
        errors.append("Missing 'publications' array")
        return errors, warnings
    
    publications = data['publications']
    
    # Validate each publication
    for idx, pub in enumerate(publications):
        pub_id = pub.get('id', f'publication_{idx}')
        
        # Required fields
        required_fields = ['id', 'title', 'authors', 'venue', 'year']
        for field in required_fields:
            if field not in pub:
                errors.append(f"Publication '{pub_id}': Missing required field '{field}'")
        
        # Validate authors is a list
        if 'authors' in pub and not isinstance(pub['authors'], list):
            errors.append(f"Publication '{pub_id}': 'authors' must be an array")
        
        # Validate year is a number
        if 'year' in pub and not isinstance(pub['year'], int):
            errors.append(f"Publication '{pub_id}': 'year' must be a number")
        
        # Validate year is reasonable
        if 'year' in pub and isinstance(pub['year'], int):
            current_year = datetime.now().year
            if pub['year'] < 1900 or pub['year'] > current_year + 2:
                warnings.append(f"Publication '{pub_id}': Year {pub['year']} seems unusual")
        
        # Check for links
        if 'links' in pub:
            if not isinstance(pub['links'], dict):
                errors.append(f"Publication '{pub_id}': 'links' must be an object")
        else:
            warnings.append(f"Publication '{pub_id}': No 'links' field provided")
        
        # Check for image
        if 'image' not in pub:
            warnings.append(f"Publication '{pub_id}': No 'image' field provided")
        
        # Check for bibtex
        if 'bibtex' not in pub:
            warnings.append(f"Publication '{pub_id}': No 'bibtex' field provided")
        
        # Check for abstract
        if 'abstract' not in pub:
            warnings.append(f"Publication '{pub_id}': No 'abstract' field provided")
    
    return errors, warnings

def validate_blog_index(filepath):
    """Validate blog-index.json structure and content"""
    errors = []
    warnings = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        return [f"Cannot read file: {e}"], []
    
    # Check required top-level keys
    if 'posts' not in data:
        errors.append("Missing 'posts' array")
        return errors, warnings
    
    posts = data['posts']
    post_ids = set()
    
    # Validate each post
    for idx, post in enumerate(posts):
        post_id = post.get('id', f'post_{idx}')
        
        # Check for duplicate IDs
        if post_id in post_ids:
            errors.append(f"Duplicate post ID: '{post_id}'")
        post_ids.add(post_id)
        
        # Required fields
        required_fields = ['id', 'title', 'date', 'author', 'excerpt', 'content']
        for field in required_fields:
            if field not in post:
                errors.append(f"Post '{post_id}': Missing required field '{field}'")
        
        # Validate date format
        if 'date' in post:
            try:
                datetime.strptime(post['date'], '%Y-%m-%d')
            except ValueError:
                errors.append(f"Post '{post_id}': Invalid date format (should be YYYY-MM-DD)")
        
        # Validate content path
        if 'content' in post:
            content_path = Path(post['content'])
            if not content_path.is_absolute():
                # Check if file exists relative to root
                full_path = Path(__file__).parent.parent / post['content'].lstrip('/')
                if not full_path.exists():
                    warnings.append(f"Post '{post_id}': Content file not found: {post['content']}")
        
        # Check for categories
        if 'categories' in post:
            if not isinstance(post['categories'], list):
                errors.append(f"Post '{post_id}': 'categories' must be an array")
        else:
            warnings.append(f"Post '{post_id}': No 'categories' field provided")
        
        # Check for tags
        if 'tags' in post:
            if not isinstance(post['tags'], list):
                errors.append(f"Post '{post_id}': 'tags' must be an array")
        else:
            warnings.append(f"Post '{post_id}': No 'tags' field provided")
        
        # Check for image
        if 'image' not in post:
            warnings.append(f"Post '{post_id}': No 'image' field provided")
    
    # Validate categories
    if 'categories' in data:
        if not isinstance(data['categories'], list):
            errors.append("'categories' must be an array")
        else:
            for cat in data['categories']:
                if 'name' not in cat or 'slug' not in cat:
                    errors.append(f"Category missing 'name' or 'slug': {cat}")
    
    # Validate tags
    if 'tags' in data:
        if not isinstance(data['tags'], list):
            errors.append("'tags' must be an array")
    
    return errors, warnings

def main():
    """Main validation function"""
    print("=" * 70)
    print("Content Validation Script")
    print("=" * 70)
    print()
    
    base_path = Path(__file__).parent.parent / 'data'
    publications_path = base_path / 'publications.json'
    blog_index_path = base_path / 'blog-index.json'
    
    all_errors = []
    all_warnings = []
    
    # Validate publications.json
    print("Validating publications.json...")
    print("-" * 70)
    
    valid, msg = validate_json_syntax(publications_path)
    if not valid:
        print(f"❌ {msg}")
        all_errors.append(msg)
    else:
        print(f"✅ {msg}")
        errors, warnings = validate_publications(publications_path)
        all_errors.extend(errors)
        all_warnings.extend(warnings)
        
        if errors:
            print(f"\n❌ Found {len(errors)} error(s):")
            for error in errors:
                print(f"   - {error}")
        else:
            print("✅ No errors found")
        
        if warnings:
            print(f"\n⚠️  Found {len(warnings)} warning(s):")
            for warning in warnings:
                print(f"   - {warning}")
    
    print()
    
    # Validate blog-index.json
    print("Validating blog-index.json...")
    print("-" * 70)
    
    valid, msg = validate_json_syntax(blog_index_path)
    if not valid:
        print(f"❌ {msg}")
        all_errors.append(msg)
    else:
        print(f"✅ {msg}")
        errors, warnings = validate_blog_index(blog_index_path)
        all_errors.extend(errors)
        all_warnings.extend(warnings)
        
        if errors:
            print(f"\n❌ Found {len(errors)} error(s):")
            for error in errors:
                print(f"   - {error}")
        else:
            print("✅ No errors found")
        
        if warnings:
            print(f"\n⚠️  Found {len(warnings)} warning(s):")
            for warning in warnings:
                print(f"   - {warning}")
    
    print()
    print("=" * 70)
    
    # Summary
    if all_errors:
        print(f"❌ Validation failed with {len(all_errors)} error(s)")
        return 1
    elif all_warnings:
        print(f"⚠️  Validation passed with {len(all_warnings)} warning(s)")
        print("   (Warnings indicate missing optional fields or placeholder content)")
        return 0
    else:
        print("✅ All validations passed!")
        return 0

if __name__ == "__main__":
    sys.exit(main())
