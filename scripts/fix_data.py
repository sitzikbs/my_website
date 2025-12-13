import json
import re
import os

def fix_publications():
    filepath = 'data/publications.json'
    with open(filepath, 'r') as f:
        pubs = json.load(f)
    
    modified = False
    for pub in pubs:
        venue = pub.get('venue', '')
        # Look for pattern "Name Name . Venue"
        # The dot might be surrounded by spaces
        match = re.match(r'^(.+?)\s+\.\s+(.+)$', venue)
        if match:
            author_part = match.group(1)
            real_venue = match.group(2)
            
            # Check if author_part looks like a name (no numbers, reasonable length)
            if not any(char.isdigit() for char in author_part):
                print(f"Fixing: {pub['title']}")
                print(f"  Moving '{author_part}' from venue to authors")
                
                # Append to authors
                if 'authors' in pub:
                    pub['authors'] = f"{pub['authors']}, {author_part}"
                else:
                    pub['authors'] = author_part
                
                pub['venue'] = real_venue
                modified = True
    
    if modified:
        with open(filepath, 'w') as f:
            json.dump(pubs, f, indent=4)
        print("Saved fixed publications.json")
    else:
        print("No changes needed for publications.json")

def fix_blog_posts():
    filepath = 'data/blog-index.json'
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    posts = data.get('posts', [])
    # Remove example posts
    posts = [p for p in posts if "Example" not in p['title']]
    data['posts'] = posts
    modified = True # Always save to ensure removal
    
    for post in posts:
        # Fix Categories
        if not post.get('categories'):
            title_lower = post['title'].lower()
            if any(x in title_lower for x in ['paper', 'research', '3d', 'vision', 'cvpr', 'iccv', 'eccv', 'neurips', 'learning', 'dataset']):
                post['categories'] = ['Research']
            else:
                post['categories'] = ['Personal']
            modified = True
            print(f"Assigned category {post['categories']} to '{post['title']}'")
            
        # Fix Excerpt
        current_excerpt = post.get('excerpt', '')
        if not current_excerpt or current_excerpt == "Could not extract content.":
            content_path = post.get('content')
            if content_path:
                # Remove leading slash for local path
                local_path = content_path.lstrip('/')
                # Handle the case where the path might be relative to the root
                if not os.path.exists(local_path):
                     # Try adding 'my_website' if we are in dev folder, but we are in root
                     pass
                
                if os.path.exists(local_path):
                    try:
                        with open(local_path, 'r') as f:
                            content = f.read()
                            # Simple regex to find the first paragraph text
                            # This is a rough heuristic
                            p_match = re.search(r'<p>(.*?)</p>', content, re.DOTALL)
                            if p_match:
                                excerpt = p_match.group(1)
                                # Strip HTML tags from excerpt
                                excerpt = re.sub(r'<[^>]+>', '', excerpt)
                                # Truncate
                                if len(excerpt) > 150:
                                    excerpt = excerpt[:147] + '...'
                                post['excerpt'] = excerpt
                                modified = True
                                print(f"Generated excerpt for '{post['title']}'")
                    except Exception as e:
                        print(f"Error reading {local_path}: {e}")
    
    if modified:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        print("Saved fixed blog-index.json")
    else:
        print("No changes needed for blog-index.json")

if __name__ == "__main__":
    fix_publications()
    fix_blog_posts()
