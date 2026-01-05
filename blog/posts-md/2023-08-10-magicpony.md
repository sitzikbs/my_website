---
layout: layouts/blog-post.njk
title: "🎠 MagicPony: Learning Articulated 3D Animals in the Wild"
date: 2023-08-10
author: Itzik Ben-Shabat
permalink: "/blog/posts/2023-08-10-magicpony.html"
---

<div class="post-content">
{% raw %}




<p>In this episode of the <a href="https://www.itzikbs.com/the-talking-papers-podcast" rel="noreferrer noopener" target="_blank">Talking Papers Podcast</a>, I hosted Tomas Jakab. We had a great chat about his paper “MagicPony: Learning Articulated 3D Animals in the Wild”, published in CVPR 2023. </p>
<p>The motivation behind the MagicPony methodology stems from the challenge posed by the scarcity of labeled data, particularly when dealing with real-world scenarios involving freely moving articulated 3D animals. In response, the authors propose an innovative solution that addresses this issue. This novel approach takes an ordinary RGB image as input and produces a sophisticated 3D model with detailed shape, texture, and lighting characteristics. The method’s uniqueness lies in its ability to learn from diverse images captured in natural settings, effectively deciphering the inherent differences between them. This enables the system to establish a foundational average shape while accounting for specific deformations that vary from instance to instance. To achieve this, the researchers blend the strengths of two techniques, radiance fields and meshes, which together contribute to the comprehensive representation of the object’s attributes. Additionally, the method employs a strategic viewpoint sampling technique to enhance computational speed. While the current results may not be suitable for practical applications just yet, this endeavor constitutes a substantial advancement in the field, as demonstrated by the tangible improvements showcased both quantitatively and qualitatively.</p>
<p></p>
<p>Tom is a postdoc in the VGG lab at Oxford University, where he recently completed his PhD with Andrea Vedaldi.  His research focuses on single-view 3D reconstruction, 2D/3D object representations, and self-supervised learning. We crossed paths at CVPR 2023, introduced by Despoina Paschalidou (of the <a href="https://www.itzikbs.com/neural-parts-learning-expressive-3d-shape-abstractions-with-invertible-neural-networks" rel="noreferrer noopener" target="_blank">Neural Parts episode</a>). Upon learning he’s one of the author of MagicPony, I invited him to the podcast. Our conversation was delightful, and I’m excited about his future projects.<br/></p>
<div id="buzzsprout-player-13379828">{% endraw %}
</div><script charset="utf-8" src="https://www.buzzsprout.com/1914034/13379828-magicpony-tomas-jakab.js?container_id=buzzsprout-player-13379828&amp;player=small" type="text/javascript"></script>
<h2 class="wp-block-heading" id="authors">AUTHORS</h2>
<p>Shangzhe Wu*<em>, Ruining Li*</em>, Tomas Jakab*, Christian Rupprecht, Andrea Vedaldi<br/></p>
<h2 class="wp-block-heading" id="abstract">ABSTRACT</h2>
<p> We consider the problem of learning a function that can estimate the 3D shape, articulation, viewpoint, texture, and lighting of an articulated animal like a horse, given a single test image. We present a new method, dubbed MagicPony, that learns this function purely from in-the-wild single-view images of the object category, with minimal assumptions about the topology of deformation. At its core is an implicit-explicit representation of articulated shape and appearance, combining the strengths of neural fields and meshes. In order to help the model understand an object’s shape and pose, we distil the knowledge captured by an off-the-shelf self-supervised vision transformer and fuse it into the 3D model. To overcome common local optima in viewpoint estimation, we further introduce a new viewpoint sampling scheme that comes at no added training cost. Compared to prior works, we show significant quantitative and qualitative improvements on this challenging task. The model also demonstrates excellent generalisation in reconstructing abstract drawings and artefacts, despite the fact that it is only trained on real images.</p>
<p> </p>
<p></p>
<h2 class="wp-block-heading" id="related-papers">RELATED (WORKS|PAPERS)</h2>
<p>📚<a href="https://akanazawa.github.io/cmr/" rel="noreferrer noopener" target="_blank">CMR</a></p>
<p>📚<a href="https://nv-tlabs.github.io/DMTet/" rel="noreferrer noopener" target="_blank">Deep Marching Tetrahedra</a></p>
<p>📚<a href="https://github.com/facebookresearch/dino" rel="noreferrer noopener" target="_blank">DINO-ViT</a></p>
<p></p>
<p></p>
<h2 class="wp-block-heading">LINKS AND RESOURCES</h2>
<p>📚 <a href="https://arxiv.org/pdf/2211.12497.pdf" rel="noreferrer noopener" target="_blank">Paper</a></p>
<p>💻<a href="https://3dmagicpony.github.io/" rel="noreferrer noopener" target="_blank">Project page</a></p>
<p>💻<a href="https://github.com/elliottwu/MagicPony" rel="noreferrer noopener" target="_blank">Code</a></p>
<p></p>
<p>To stay up to date with their latest research, follow on:</p>
<p>👨🏻‍🎓<a href="https://www.robots.ox.ac.uk/~tomj/" rel="noreferrer noopener" target="_blank">Personal page</a></p>
<p>🐦<a href="https://twitter.com/JakabTomas" rel="noreferrer noopener" target="_blank">Twitter</a></p>
<p>👨🏻‍🎓<a href="https://scholar.google.com/citations?hl=en&amp;user=-gFCCLMAAAAJ" rel="noreferrer noopener" target="_blank">Google Scholar</a></p>
<p></p>
<p></p>
<figure class="wp-block-embed is-type-rich is-provider-embed-handler wp-block-embed-embed-handler wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/IUsY_FB2XHM?feature=oembed" title="MagicPony (CVPR 2023) with Tomas Jakab on Talking papers" width="800"></iframe>
</div></figure>
<p>Recorded on July 27th 2023.</p>
<p><br/><br/>CONTACT</p>
<p>If you would like to be a guest, sponsor or share your thoughts, feel free to reach out via email: <a class="__cf_email__" data-cfemail="f387929f989a9d94dd839283968180dd839c9790928087b3949e929a9fdd909c9e" href="/cdn-cgi/l/email-protection">[email protected]</a></p>
<p></p>
<h2 class="wp-block-heading">SUBSCRIBE AND FOLLOW</h2>
<p>🎧Subscribe on your favourite podcast app: <a href="/podcast/" rel="noreferrer noopener" target="_blank">/podcast/</a></p>
<p>📧Subscribe to our mailing list: <a href="http://eepurl.com/hRznqb" rel="noreferrer noopener" target="_blank">http://eepurl.com/hRznqb</a></p>
<p>🐦Follow us on Twitter: <a href="https://twitter.com/talking_papers" rel="noreferrer noopener" target="_blank">https://twitter.com/talking_papers</a></p>
<p>🎥YouTube Channel: </p>
<p></p>
<p></p>
<p></p>
 

</div>