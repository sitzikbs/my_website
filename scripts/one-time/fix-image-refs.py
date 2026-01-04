import os, re, glob

# Get all images in the blog directory and create various mappings
all_images = os.listdir("assets/images/blog/")

# Create mapping of base names to actual files (handling -scaled, date prefixes, etc.)
image_map = {}
for img in all_images:
    # Skip webp files
    if img.endswith('.webp'):
        continue
    
    # Add direct mapping
    image_map[img] = img
    
    # Remove -scaled suffix
    if '-scaled' in img:
        base = img.replace('-scaled', '')
        image_map[base] = img
    
    # Remove date prefix if present
    if re.match(r'\d{4}-\d{2}-', img):
        without_date = re.sub(r'^\d{4}-\d{2}-', '', img)
        image_map[without_date] = img
        
        # Also without date and without -scaled
        if '-scaled' in without_date:
            without_both = without_date.replace('-scaled', '')
            image_map[without_both] = img

print(f"Created mapping for {len(image_map)} image variations")

# Now fix all blog post references
blog_files = glob.glob("blog/posts-md/*.md")
fixes = 0
errors = []

for blog_file in blog_files:
    with open(blog_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'(responsiveImage\s+"\.\.\/\.\.\/assets\/images\/blog\/)([^"]+)(")'
    
    modified = False
    matches = list(re.finditer(pattern, content))
    
    for match in matches:
        filename = match.group(2)
        
        # Check if file exists
        full_path = f"assets/images/blog/{filename}"
        if not os.path.exists(full_path):
            # Try to find it in our mapping
            if filename in image_map:
                actual_file = image_map[filename]
                content = content.replace(
                    f'responsiveImage "../../assets/images/blog/{filename}"',
                    f'responsiveImage "../../assets/images/blog/{actual_file}"'
                )
                modified = True
                print(f"  {os.path.basename(blog_file)}: {filename} -> {actual_file}")
                fixes += 1
            else:
                errors.append(f"{blog_file}: Missing {filename}")
    
    if modified:
        with open(blog_file, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"\nFixed {fixes} image references")
if errors:
    print(f"\nStill have {len(errors)} missing images:")
    for err in errors:
        print(f"  {err}")
