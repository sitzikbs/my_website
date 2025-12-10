#!/usr/bin/env python3
"""
Fix blog post categories by identifying actual podcast episodes from the
WordPress category page.
"""

import json
from pathlib import Path

# All podcast episode URLs extracted from the category pages
PODCAST_URLS = [
    # Page 1
    "https://www.itzikbs.com/phd-guide-advisor-hunt",
    "https://www.itzikbs.com/3dpaintbrush",
    "https://www.itzikbs.com/3dinaction",
    "https://www.itzikbs.com/cameras-as-rays",
    "https://www.itzikbs.com/instant3d",
    "https://www.itzikbs.com/variational-barycentric-coordinates",
    "https://www.itzikbs.com/revenge_ssl",
    "https://www.itzikbs.com/csg_on_nsdf",
    "https://www.itzikbs.com/hmdnemo",
    "https://www.itzikbs.com/cc3d",
    # Page 2
    "https://www.itzikbs.com/nerf-det",
    "https://www.itzikbs.com/magicpony",
    "https://www.itzikbs.com/word_as_image",
    "https://www.itzikbs.com/panoptic-lifting",
    "https://www.itzikbs.com/mobilebrick",
    "https://www.itzikbs.com/iaw_dataset",
    "https://www.itzikbs.com/inr2vec",
    "https://www.itzikbs.com/clipasso",
    "https://www.itzikbs.com/random-walks-for-adversarial-meshes",
    "https://www.itzikbs.com/spsr",
    # Page 3
    "https://www.itzikbs.com/beyond-periodicity",
    "https://www.itzikbs.com/keypointnerf",
    "https://www.itzikbs.com/bacon",
    "https://www.itzikbs.com/lipschitz-mlp",
    "https://www.itzikbs.com/digs",
    "https://www.itzikbs.com/neural-rgb-d-surface-reconstruction",
    "https://www.itzikbs.com/icon-implicit-clothed-humans-obtained-from-normals",
    "https://www.itzikbs.com/samplenet-differentiable-point-cloud-sampling",
    "https://www.itzikbs.com/panoptic-3d-scene-reconstruction-from-a-single-rgb-image",
    "https://www.itzikbs.com/shape-as-points-a-differentiable-poisson-solver",
    # Page 4
    "https://www.itzikbs.com/vln-bert-a-recurrent-vision-and-language-bert-for-navigation",
    "https://www.itzikbs.com/neural-parts-learning-expressive-3d-shape-abstractions-with-invertible-neural-networks",
    "https://www.itzikbs.com/deep-declarative-networks",
    "https://www.itzikbs.com/dori-discovering-object-relationships-for-moment-localization-of-a-natural-language-query-in-a-video",
    "https://www.itzikbs.com/the-talking-papers-podcast",
]

# Extract slugs from URLs
PODCAST_SLUGS = {url.split('/')[-1] for url in PODCAST_URLS}

def categorize_post(post):
    """Determine the correct category for a post."""
    post_id = post.get('id', '')
    title = post.get('title', '').lower()
    excerpt = post.get('excerpt', '').lower()
    
    # Check if this is a podcast episode (using post ID which matches the slug)
    if post_id in PODCAST_SLUGS:
        return ["Talking Papers Podcast"]
    
    # Research keywords for non-podcast posts
    research_keywords = [
        'cvpr', 'iccv', 'eccv', 'nips', 'neurips', 'icml', 'iclr',
        'siggraph', 'wacv', 'bmvc', '3dv', 'accv', 'aaai', 'ijcai',
        'conference', 'paper', 'publication', 'journal', 'arxiv',
        'research', 'dataset', 'benchmark'
    ]
    
    # Check title and excerpt for research keywords
    text = f"{title} {excerpt}".lower()
    if any(keyword in text for keyword in research_keywords):
        return ["Research"]
    
    # Default to Personal
    return ["Personal"]

def main():
    # Load blog index
    blog_index_path = Path(__file__).parent.parent / 'data' / 'blog-index.json'
    
    with open(blog_index_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Processing {len(data['posts'])} posts...")
    
    # Track category changes
    podcast_count = 0
    research_count = 0
    personal_count = 0
    
    for post in data['posts']:
        old_categories = post.get('categories', [])
        new_categories = categorize_post(post)
        
        if new_categories != old_categories:
            post['categories'] = new_categories
            category = new_categories[0]
            
            if category == "Talking Papers Podcast":
                podcast_count += 1
            elif category == "Research":
                research_count += 1
            else:
                personal_count += 1
    
    # Save updated blog index
    with open(blog_index_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print("\nCategory updates:")
    print(f"  Podcast episodes: {podcast_count}")
    print(f"  Research posts: {research_count}")
    print(f"  Personal posts: {personal_count}")
    print(f"\nTotal posts: {len(data['posts'])}")
    
    # Verify podcast count
    actual_podcast = sum(1 for p in data['posts'] if "Talking Papers Podcast" in p.get('categories', []))
    print(f"\nVerification: {actual_podcast} posts now have 'Talking Papers Podcast' category")
    print(f"Expected: {len(PODCAST_SLUGS)} podcast episodes")

if __name__ == "__main__":
    main()
