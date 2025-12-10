#!/usr/bin/env python3
"""Replace navigation sections with dynamic loader placeholder"""

from pathlib import Path
import re

files = ['index.html', 'contact.html']

for filename in files:
    filepath = Path(filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match the entire nav section
    nav_pattern = r'<nav class="navbar">.*?</nav>'
    
    # Replace with dynamic loader
    new_content = re.sub(nav_pattern, '<div id="main-nav"></div>', content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ Updated {filename}")
    else:
        print(f"✗ No changes needed for {filename}")
