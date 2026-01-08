---
layout: layouts/blog-post.njk
title: "Constructive Solid Geometry on Neural Signed Distance Fields"
date: 2023-11-09
author: Itzik Ben-Shabat
permalink: "/blog/posts/2023-11-09-csg_on_nsdf.html"
---

<div class="post-content">
{% raw %}




<div id="buzzsprout-player-13932902">{% endraw %}
</div><script charset="utf-8" src="https://www.buzzsprout.com/1914034/13932902.js?container_id=buzzsprout-player-13932902&amp;player=small" type="text/javascript"></script>
<p>In our latest episode of the Talking Papers Podcast, I had the pleasure of hosting Zoë Marschner, a first-year PhD student at Carnegie Mellon University. We delved into her research paper titled “Constructive Solid Geometry on Neural Signed Distance Fields,” which was published in SIGGRAPH Asia 2023. The topic revolves around the challenge of editing shapes encoded by neural SDFs, a popular geometric representation.</p>
<p>Zoë and her co-authors tackled the issue of incorrect non-Signed Distance Fields (SDFs) outputs resulting from common geometric operations. These outputs, referred to as Pseudo-SDFs, hinder their usability for downstream tasks. To address this, they characterized the space of Pseudo-SDFs and introduced the closest point loss, a novel regularizer that ensures an exact SDF as the output. This regularization technique has wide applicability in several operations, such as CSG and swept volumes.</p>
<p>As a former mechanical engineer, I find the combination of Constructive Solid Geometry (CSG) and Neural Signed Distance Fields intriguing, especially considering its potential in computer-aided design (CAD) applications. The seamless integration of traditional methods with the power of neural networks opens up new possibilities in shape editing and content creation.</p>
<p>Recording the episode with Zoë was a delightful experience, even though we haven’t had the chance to meet in person. It amazes me how early in her career she has already worked with some of the most esteemed individuals in the field. It was truly inspiring to hear her insights and dedication to driving innovation through academic research. I am excited about Zoë’s future research and the impact it will have on the field of Constructive Solid Geometry and Neural Signed Distance Fields. </p>
<h2 class="wp-block-heading">AUTHORS</h2>
<p><br/>Zoë Marschner, Silvia Sellán, Hsueh-Ti Derek Liu, Alec Jacobson</p>
<h2 class="wp-block-heading">ABSTRACT</h2>
<p><br/>Signed Distance Fields (SDFs) parameterized by neural networks have recently gained popularity as a fundamental geometric representation. However, editing the shape encoded by a neural SDF remains an open challenge. A tempting approach is to leverage common geometric operators (e.g., boolean operations), but such edits often lead to incorrect non-SDF outputs (which we call Pseudo-SDFs), preventing them from being used for downstream tasks. In this paper, we characterize the space of Pseudo-SDFs, which are eikonal yet not true distance functions, and derive the closest point loss, a novel regularizer that encourages the output to be an exact SDF. We demonstrate the applicability of our regularization to many operations in which traditional methods cause a Pseudo-SDF to arise, such as CSG and swept volumes, and produce a true (neural) SDF for the result of these operations.</p>
<h2 class="wp-block-heading">RELATED (WORKS|PAPERS)</h2>
<p>📚<a href="https://openaccess.thecvf.com/content_CVPR_2019/papers/Park_DeepSDF_Learning_Continuous_Signed_Distance_Functions_for_Shape_Representation_CVPR_2019_paper.pdf" rel="noreferrer noopener" target="_blank">DeepSDF</a></p>
<p>📚<a href="https://www.dgp.toronto.edu/projects/swept-volumes/" rel="noreferrer noopener" target="_blank">Swept Volumes via Spacetime Numerical Continuation</a></p>
<p>📚<a href="https://iquilezles.org/articles/interiordistance/" rel="noreferrer noopener" target="_blank">Inigo Quilez blog</a></p>
<h2 class="wp-block-heading">LINKS AND RESOURCES</h2>
<p>📚<a href="https://zoemarschner.com/papers/csg_on_neural_sdfs_lo_res.pdf" rel="noreferrer noopener" target="_blank">Paper</a></p>
<p>💻<a href="https://zoemarschner.com/research/csg_on_neural_sdfs.html" rel="noreferrer noopener" target="_blank">Project page</a></p>
<p>To stay up to date with herlatest research, follow on:</p>
<p>👨🏻‍🎓<a href="https://zoemarschner.com/" rel="noreferrer noopener" target="_blank">Personal website</a></p>
<p>👨🏻‍🎓<a href="https://scholar.google.com/citations?user=HqL4J0MAAAAJ&amp;hl=en&amp;oi=ao" rel="noreferrer noopener" target="_blank">Google scholar</a></p>
<p>👨🏻‍🎓<a href="https://www.linkedin.com/in/zoemarschner/" rel="noreferrer noopener" target="_blank">LinkedIn</a></p>
<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" style="border: none;" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/vUaauuw4Si8?feature=oembed" title="CSG on Neural SDFs (SIGGRAPH Asia 2023) with Zoë Marschner on Talking Papers Podcast" width="800"></iframe>
</div></figure>
<p>This episode was recorded on October 24th 2023</p>
<h2 class="wp-block-heading">CONTACT</h2>
<p><br/>If you would like to be a guest, sponsor or share your thoughts, feel free to reach out via email: <a class="__cf_email__" data-cfemail="5c283d303735323b722c3d2c392e2f722c33383f3d2f281c3b313d3530723f3331" href="/cdn-cgi/l/email-protection">[email protected]</a></p>
<h2 class="wp-block-heading">SUBSCRIBE AND FOLLOW</h2>
<p><br/>🎧Subscribe on your favourite <a href="https://talking.papers.podcast.itzikbs.com" rel="noreferrer noopener" target="_blank">podcast app</a></p>
<p>📧Subscribe to our <a href="http://eepurl.com/hRznqb" rel="noreferrer noopener" target="_blank">mailing list</a></p>
<p>🐦Follow us on <a href="https://twitter.com/talking_papers" rel="noreferrer noopener" target="_blank">Twitter</a></p>
<p>🎥Subscribe to our </p>
 

</div>