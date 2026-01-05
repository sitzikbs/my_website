---
layout: layouts/blog-post.njk
title: "Panoptic Lifting for 3D Scene Understanding with Neural Fields"
date: 2023-07-10
author: Itzik Ben-Shabat
permalink: "/blog/posts/2023-07-10-panoptic-lifting.html"
---

<div class="post-content">
{% raw %}




<p>In this episode of the <a href="https://www.itzikbs.com/the-talking-papers-podcast" rel="noreferrer noopener" target="_blank">Talking Papers Podcast</a>, I hosted Yawar Siddiqui to chat about his CVPR 2023 highlight paper “Panoptic Lifting for 3D Scene Understanding with Neural Fields”.</p>
<p>In this paper, they proposed a new method for “lifting” 2D panoptic segmentation into a 3D volume represented as neural fields using in-the-wild scene images.  While the semantic segmentation part is simply represented as an MLP, the instance indices are very difficult to keep track of inbetween the different frames. This is solved using a Hungarian algorithm and a set of custom losses. </p>
<p></p>
<p>Yawar is currently a PhD student at the Technical University of Munich (TUM) under the supervision of Prof. Matthias Niessner. This work was done as part of his latest internship with Meta Zurich. Funnily, he shares an office with onther guest of the podcast – <a href="/podcast//1914034/10004179" rel="noreferrer noopener" target="_blank">Guy Gafni</a>. I first met Yawar at ECCV 2022 in Israel and then again at CVPR 2023. I have been following his works for a while now and it is amazing how much his research has grown over the years. It was a pleasure chatting with him and I can’t wait to see what he cooks up next. </p>
<p></p>
<p></p>
<div id="buzzsprout-player-13188478">{% endraw %}
</div><script charset="utf-8" src="https://www.buzzsprout.com/1914034/13188478-panoptic-lifting-yawar-siddiqui.js?container_id=buzzsprout-player-13188478&amp;player=small" type="text/javascript"></script>
<h2 class="wp-block-heading" id="authors">AUTHORS</h2>
<p id="stephen-gould-richard-hartleydylan-campbell"><em><a href="https://niessnerlab.org/members/yawar_siddiqui/profile.html">Yawar Siddiqui</a>, <a href="https://scholar.google.com/citations?user=vW1gaVEAAAAJ">Lorenzo Porzi</a>, <a href="https://scholar.google.com/citations?hl=de&amp;user=484sccEAAAAJ">Samuel Rota Bulò</a>, <a href="https://niessnerlab.org/members/norman_mueller/profile.html">Norman Müller</a>, <a href="https://niessnerlab.org/members/matthias_niessner/profile.html">Matthias Nießner</a>, <a href="https://www.3dunderstanding.org/team.html">Angela Dai</a>, <a href="https://scholar.google.com/citations?user=CxbDDRMAAAAJ&amp;hl=en">Peter Kontschieder</a></em></p>
<p></p>
<h2 class="wp-block-heading" id="abstract">ABSTRACT</h2>
<p>We propose Panoptic Lifting, a novel approach for learning panoptic 3D volumetric representations from images of in-the-wild scenes. Once trained, our model can render color images together with 3D-consistent panoptic segmentation from novel viewpoints.Unlike existing approaches which use 3D input directly or indirectly, our method requires only machine-generated 2D panoptic segmentation masks inferred from a pre-trained network. Our core contribution is a panoptic lifting scheme based on a neural field representation that generates a unified and multi-view consistent, 3D panoptic representation of the scene. To account for inconsistencies of 2D instance identifiers across views, we solve a linear assignment with a cost based on the model’s current predictions and the machine-generated segmentation masks, thus enabling us to lift 2D instances to 3D in a consistent way. We further propose and ablate contributions that make our method more robust to noisy, machine-generated labels, including test-time augmentations for confidence estimates, segment consistency loss, bounded segmentation fields, and gradient stopping.Experimental results validate our approach on the challenging Hypersim, Replica, and ScanNet datasets, improving by 8.4, 13.8, and 10.6% in scene-level PQ over state of the art.</p>
<p> </p>
<p></p>
<h2 class="wp-block-heading" id="related-papers">RELATED (WORKS|PAPERS)</h2>
<p>📚<a href="https://www.matthewtancik.com/nerf" rel="noreferrer noopener" target="_blank">NeRF</a></p>
<p>📚<a href="https://openaccess.thecvf.com/content/CVPR2022/papers/Cheng_Masked-Attention_Mask_Transformer_for_Universal_Image_Segmentation_CVPR_2022_paper.pdf">Mask2Former</a></p>
<p>📚<a href="https://shuaifengzhi.com/Semantic-NeRF/" rel="noreferrer noopener" target="_blank">Semantic NeRF</a></p>
<h2 class="wp-block-heading">LINKS AND RESOURCES</h2>
<p>📚 <a href="https://nihalsid.github.io/panoptic-lifting/static/PanopticLifting.pdf">Paper</a></p>
<p>💻<a href="https://nihalsid.github.io/panoptic-lifting/" rel="noreferrer noopener" target="_blank">Project page</a></p>
<p>💻<a href="https://github.com/nihalsid/panoptic-lifting" rel="noreferrer noopener" target="_blank">Code</a></p>
<p>To stay up to date with Yawar’s latest research, follow him on:</p>
<p>👨🏻‍🎓<a href="https://nihalsid.github.io/" rel="noreferrer noopener" target="_blank">Personal page</a></p>
<p>👨🏻‍🎓<a href="https://www.linkedin.com/in/yawarnihal">LinkdIn</a></p>
<p>🐦<a href="https://twitter.com/yawarnihal" rel="noreferrer noopener" target="_blank">Twitter</a></p>
<p></p>
<p></p>
<figure class="wp-block-embed is-type-rich is-provider-embed-handler wp-block-embed-embed-handler wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/qqseAaTSCOQ?feature=oembed" title="Panoptic Lifting (CVPR 2023) with Yawar Siddiqui on Talking papers" width="800"></iframe>
</div></figure>
<p>Recorded on July 6th 2023.</p>
<h3 class="wp-block-heading">SPONSOR</h3>
<p>This episode was sponsored by YOOM. YOOM is an Israeli startup dedicated to volumetric video creation. They were voted as the 2022 best start-up to work for by Dun’s 100.<br/><a href="https://www.yoom.com/careers" rel="noreferrer noopener" target="_blank">Join their team</a> that works on geometric deep learning research, implicit representations of 3D humans, NeRFs, and 3D/4D generative models.</p>
<p><br/>Visit <a href="https://www.yoom.com/" rel="noreferrer noopener" target="_blank">YOOM.com</a>.</p>
<h2 class="wp-block-heading"><br/>CONTACT</h2>
<p>If you would like to be a guest, sponsor or share your thoughts, feel free to reach out via email: talking (dor) papers (dot) podcast(at) gmail (dot) com</p>
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