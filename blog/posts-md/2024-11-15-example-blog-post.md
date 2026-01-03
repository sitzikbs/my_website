---
layout: layouts/blog-post.njk
title: "Untitled"
date: 2024-11-15
author: Itzik Ben-Shabat
permalink: "/blog/posts/2024-11-15-example-blog-post.html"
---

<div class="post-content">
<section>
<h2>Introduction</h2>
<p>
                    This is an example blog post. When migrating from WordPress, replace this content 
                    with the actual blog post content. This template shows the structure and metadata 
                    that should be preserved during migration.
                </p>
<p>
                    The actual WordPress content should be exported using the WordPress export tool 
                    (Tools &gt; Export &gt; Posts), then converted to HTML or Markdown format 
                    preserving all formatting, images, code blocks, and other elements.
                </p>
</section>
<section>
<h2>Main Content Structure</h2>
<p>
                    Each blog post should maintain its original structure with:
                </p>
<ul>
<li>Proper heading hierarchy (h1 for title, h2 for sections, h3 for subsections)</li>
<li>Paragraphs with preserved formatting</li>
<li>Images with alt text and captions</li>
<li>Code blocks with syntax highlighting</li>
<li>Links (both internal and external)</li>
<li>Lists (ordered and unordered)</li>
<li>Blockquotes</li>
<li>Tables (if present)</li>
</ul>
</section>
<section>
<h2>Code Examples</h2>
<p>
                    If the blog post contains code snippets, preserve them with proper formatting:
                </p>
<pre><code class="language-python">
import numpy as np
import torch

# Example code from blog post
def process_point_cloud(points):
    """
    Example function to show code formatting
    """
    return torch.tensor(points)
                </code></pre>
</section>
<section>
<h2>Embedded Images</h2>
<p>
                    Images within the content should be properly referenced:
                </p>
<figure>
{# responsiveImage "/assets/images/blog/example-inline-image.jpg", "Example inline image" #}
<figcaption>Example caption for inline image</figcaption>
</figure>
</section>
<section>
<h2>External Links and Resources</h2>
<p>
                    Preserve all external links from the original WordPress post:
                </p>
<ul>
<li><a href="https://example.com/resource1" rel="noopener noreferrer" target="_blank">Example Resource 1</a></li>
<li><a href="https://example.com/resource2" rel="noopener noreferrer" target="_blank">Example Resource 2</a></li>
</ul>
</section>
<section>
<h2>Conclusion</h2>
<p>
                    The conclusion should wrap up the blog post content. Remember to preserve 
                    all original content, formatting, and media from the WordPress export.
                </p>
</section>
</div>