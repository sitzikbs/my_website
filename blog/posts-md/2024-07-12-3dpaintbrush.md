---
layout: layouts/blog-post.njk
title: "3D Paintbrush: Local Stylization of 3D Shapes with Cascaded Score Distillation"
date: 2024-07-12
author: Itzik Ben-Shabat
permalink: "/blog/posts/2024-07-12-3dpaintbrush.html"
---

<div class="post-content">
{% raw %}




<div id="buzzsprout-player-15398198">{% endraw %}
</div><script charset="utf-8" src="https://www.buzzsprout.com/1914034/15398198.js?container_id=buzzsprout-player-15398198&amp;player=small" type="text/javascript"></script>
<p>I am thrilled to share the latest episode of the Talking Papers Podcast where I had the pleasure of hosting Dale Decatur, a brilliant 3rd year PhD student from the University of Chicago’s 3DL lab. Together, we delved into the intricate details of his paper titled “3D Paintbrush: Local Stylization of 3D Shapes with Cascaded Score Distillation,” recently published in CVPR 2024. The paper introduces an innovative technique, 3D Paintbrush, which allows for the automatic texturing of local semantic regions on meshes through text descriptions.</p>
<p>One of the key contributions of Dale’s paper is the development of Cascaded Score Distillation (CSD), a technique that employs multiple stages of a cascaded diffusion model to enhance the details and resolution of textured areas on 3D shapes. The approach of simultaneously generating localization maps and conforming texture maps not only refines the quality of editing but also streamlines the integration of textured areas into standard graphics pipelines. This advancement marks a significant stride in simplifying the process of editing 3D assets, particularly through text prompts, thus making it more accessible to a broader audience.</p>
<p>As I delved deeper into the paper, I was truly impressed by the clever utilization of generative priors learned from images at different resolutions to supervise the local editing technique. This not only showcases the depth of research conducted by Dale but also highlights the potential impact of his work on the broader research community. It is fascinating to witness the evolution of techniques that leverage the synergy between machine learning and 3D modeling, ultimately pushing the boundaries of what is achievable in the realm of computer graphics.</p>
<p>Reflecting on my interactions with Dale, I am reminded of our initial encounter at CVPR 2023 when he presented his 3D highlighter paper. Our paths crossed again at CVPR 2024, where I had the opportunity to chat with Dale about 3D Paintbrush. It was a moment of realization that this was a conversation that needed to be shared with our listeners. I am eagerly looking forward to witnessing Dale’s future research endeavors and the innovative contributions he will undoubtedly make to the field of computer graphics and deep learning.</p>
<h2 class="wp-block-heading">AUTHORS</h2>
<p><br/>Dale Decatur, Itai Lang, Kfir Aberman, Rana Hanocka</p>
<h2 class="wp-block-heading">ABSTRACT</h2>
<p><br/>In this work we develop 3D Paintbrush, a technique for automatically texturing local semantic regions on meshes via text descriptions. Our method is designed to operate directly on meshes, producing texture maps which seamlessly integrate into standard graphics pipelines. We opt to simultaneously produce a localization map (to specify the edit region) and a texture map which conforms to it. This synergistic approach improves the quality of both the localization and the stylization. To enhance the details and resolution of the textured area, we leverage multiple stages of a cascaded diffusion model to supervise our local editing technique with generative priors learned from images at different resolutions. Our technique, referred to as Cascaded Score Distillation (CSD), simultaneously distills scores at multiple resolutions in a cascaded fashion, enabling control over both the granularity and global understanding of the supervision. We demonstrate the effectiveness of 3D Paintbrush to locally texture a variety of shapes within different semantic regions.</p>
<h2 class="wp-block-heading">RELATED (WORKS|PAPERS)</h2>
<p>📚<a href="https://threedle.github.io/3DHighlighter/" rel="noreferrer noopener" target="_blank">3D Highlghter</a></p>
<p>📚<a href="https://dreamfusion3d.github.io/" rel="noreferrer noopener" target="_blank">DreamFusion</a></p>
<p>📚<a href="https://pals.ttic.edu/p/score-jacobian-chaining" rel="noreferrer noopener" target="_blank">Score Jacobian Chaining</a></p>
<h2 class="wp-block-heading">LINKS AND RESOURCES</h2>
<p>📚<a href="https://arxiv.org/abs/2311.09571" rel="noreferrer noopener" target="_blank">Preprint</a></p>
<p>📚<a href="https://threedle.github.io/3d-paintbrush/static/3d-paintbrush.pdf" rel="noreferrer noopener" target="_blank">Paper</a></p>
<p>💻<a href="https://threedle.github.io/3d-paintbrush/" rel="noreferrer noopener" target="_blank">Project page</a></p>
<p>💻<a href="https://github.com/threedle/3d-paintbrush" rel="noreferrer noopener" target="_blank">Code</a></p>
<p>To stay up to date with his latest research, follow on:</p>
<p>👨🏻‍🎓<a href="https://ddecatur.github.io/" rel="noreferrer noopener" target="_blank">Personal website</a></p>
<p>👨🏻‍🎓<a href="https://scholar.google.com/citations?user=rIZXMMAAAAAJ" rel="noreferrer noopener" target="_blank">Google scholar</a></p>
<p>🐦<a href="https://x.com/DecaturDale" rel="noreferrer noopener" target="_blank">Twitter</a></p>
<p>👨🏻‍🎓<a href="https://www.linkedin.com/in/dale-decatur-246a38192/" rel="noreferrer noopener" target="_blank">LinkedIn</a></p>
<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube"><div class="wp-block-embed__wrapper">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/BU8gbf0zml0?feature=oembed" title="3D Paintbrush (CVPR 2024) with Dale Decatur on Talking Papers Podcast" width="800"></iframe>
</div></figure>
<p>This episode was recorded on July 10th 2024</p>
<h2 class="wp-block-heading">CONTACT</h2>
<p><br/>If you would like to be a guest, sponsor or share your thoughts, feel free to reach out via email: <a class="__cf_email__" data-cfemail="85f1e4e9eeecebe2abf5e4f5e0f7f6abf5eae1e6e4f6f1c5e2e8e4ece9abe6eae8" href="/cdn-cgi/l/email-protection">[email protected]</a></p>
<h2 class="wp-block-heading">SUBSCRIBE AND FOLLOW</h2>
<p><br/>🎧Subscribe on your favourite <a href="/podcast/" rel="noreferrer noopener" target="_blank">podcast app</a></p>
<p>📧Subscribe to our <a href="http://eepurl.com/hRznqb" rel="noreferrer noopener" target="_blank">mailing list</a></p>
<p>🐦Follow us on <a href="https://twitter.com/talking_papers" rel="noreferrer noopener" target="_blank">Twitter</a></p>
<p>🎥Subscribe to our <a href="https://bit.ly/3eQOgwP" rel="noreferrer noopener" target="_blank">YouTube channel</a></p>
 

</div>