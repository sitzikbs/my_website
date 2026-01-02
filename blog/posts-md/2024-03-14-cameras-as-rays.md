---
layout: layouts/blog-post.njk
title: "Cameras as Rays: Pose Estimation via Ray Diffusion"
date: 2024-03-14
author: Itzik Ben-Shabat
permalink: "/blog/posts/2024-03-14-cameras-as-rays.html"
---

<div class="post-content">


<div id="buzzsprout-player-14686846"></div><script charset="utf-8" src="https://www.buzzsprout.com/1914034/14686846.js?container_id=buzzsprout-player-14686846&amp;player=small" type="text/javascript"></script>
<p>In the latest episode of Talking Papers Podcast, I had the immense pleasure of hosting Jason Zhang, who’s currently cutting a dynamic path as a PhD student at the Robotics Institute at Carnegie Mellon University. Our conversation revolved around his captivating paper, “Cameras as Rays: Pose Estimation via Ray Diffusion,” which was recently accepted to ICLR 2024 as an oral presentation. This work is a game-changing twist in the arena of camera pose estimation, where they estimate camera poses by treating a camera as a bundle of rays rather than the standard practice of predicting global parametrizations of camera extrinsics. This unique representation, linked tightly with spatial image features, elevates the precision aspect of the pose.</p>
<p>Zhang’s work is a profound reflection of out-of-the-box thinking, an attribute I always advocate for in research. The idea of camera pose estimation embodied as a combination of rays opens up an entirely new vista. While further exploring this avenue, both regression and diffusion models are deployed that seemed to robustly work in harmony with this representation. The outcome? Even with the bare minimum of views, the results are staggeringly impressive, hinting at a breakthrough in the realm of camera pose estimation. The paper escalates to demonstrate state-of-the-art performance, attaining a notable landmark in CO3D applications while being versatile enough to fit into unseen object categories and in-the-wild captures.</p>
<p>It’s interesting how these professional encounters can lead to personal connections, and this was certainly the case with Jason. Before this podcast episode, our paths had never crossed. What started as a conversation about his trailblazing paper morphed into learning about his personal journey from the Bay Area to Pittsburgh. The exchange was so natural, so comfortable, that the thought of wrapping up the conversation seemed almost preposterous. It’s these fascinating encounters and path-breaking research like Jason’s that keeps the intellectual flame burning, and I eagerly look forward to his future works. Stay tuned with Talking Papers Podcast and  ICLR2024 for more such enriching experiences.</p>
<h2 class="wp-block-heading">AUTHORS</h2>
<p><br/>Jason Y. Zhang, Amy Lin, Moneish Kumar, Tzu-Hsuan Yang, Deva Ramanan, Shubham Tulsiani</p>
<h2 class="wp-block-heading">ABSTRACT</h2>
<p><br/>Estimating camera poses is a fundamental task for 3D reconstruction and remains challenging given sparse views (&lt;10). In contrast to existing approaches that pursue top-down prediction of global parametrizations of camera extrinsics, we propose a distributed representation of camera pose that treats a camera as a bundle of rays. This representation allows for a tight coupling with spatial image features improving pose precision. We observe that this representation is naturally suited for set-level level transformers and develop a regression-based approach that maps image patches to corresponding rays. To capture the inherent uncertainties in sparse-view pose inference, we adapt this approach to learn a denoising diffusion model which allows us to sample plausible modes while improving performance. Our proposed methods, both regression- and diffusion-based, demonstrate state-of-the-art performance on camera pose estimation on CO3D while generalizing to unseen object categories and in-the-wild captures.</p>
<h2 class="wp-block-heading">RELATED (WORKS|PAPERS)</h2>
<p>📚<a href="https://openaccess.thecvf.com/content_CVPR_2020/html/Schops_Why_Having_10000_Parameters_in_Your_Camera_Model_Is_Better_CVPR_2020_paper.html" rel="noreferrer noopener" target="_blank">Why Having 10000 Parameters in Your Camera Model Is Better Than Twelve</a></p>
<p>📚<a href="https://ieeexplore.ieee.org/abstract/document/937611" rel="noreferrer noopener" target="_blank">A general imaging model and a method for finding its parameters</a></p>
<p>📚<a href="https://openaccess.thecvf.com/content/ICCV2023/html/Wang_PoseDiffusion_Solving_Pose_Estimation_via_Diffusion-aided_Bundle_Adjustment_ICCV_2023_paper.html" rel="noreferrer noopener" target="_blank">PoseDiffusion</a></p>
<h2 class="wp-block-heading">LINKS AND RESOURCES</h2>
<p>📚<a href="https://arxiv.org/abs/2402.14817" rel="noreferrer noopener" target="_blank">Preprint</a></p>
<p>💻<a href="https://jasonyzhang.com/RayDiffusion/" rel="noreferrer noopener" target="_blank">Project page</a></p>
<p>💻<a href="https://github.com/jasonyzhang/RayDiffusion" rel="noreferrer noopener" target="_blank">Code</a></p>
<p>To stay up to date with his latest research, follow on:</p>
<p>👨🏻‍🎓<a href="https://jasonyzhang.com/" rel="noreferrer noopener" target="_blank">Personal website</a></p>
<p>👨🏻‍🎓<a href="https://scholar.google.com/citations?authuser=2&amp;user=j56HgqYAAAAJ" rel="noreferrer noopener" target="_blank">Google scholar</a></p>
<p>🐦<a href="https://twitter.com/jasonyzhang2" rel="noreferrer noopener" target="_blank">Twitter</a></p>
<figure class="wp-block-embed is-type-rich is-provider-embed-handler wp-block-embed-embed-handler wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/KgHwv3Nf8rg?feature=oembed" title="Cameras as Rays (ICLR 2024 Oral) with Jason Y. Zhang on Talking Papers Podcast" width="800"></iframe>
</div></figure>
<p>This episode was recorded on March 13th 2024</p>
<h2 class="wp-block-heading">CONTACT</h2>
<p><br/>If you would like to be a guest, sponsor or share your thoughts, feel free to reach out via email: <a class="__cf_email__" data-cfemail="0a7e6b666163646d247a6b7a6f7879247a656e696b797e4a6d676b636624696567" href="/cdn-cgi/l/email-protection">[email protected]</a></p>
<h2 class="wp-block-heading">SUBSCRIBE AND FOLLOW</h2>
<p><br/>🎧Subscribe on your favourite <a href="https://talking.papers.podcast.itzikbs.com" rel="noreferrer noopener" target="_blank">podcast app</a></p>
<p>📧Subscribe to our <a href="http://eepurl.com/hRznqb" rel="noreferrer noopener" target="_blank">mailing list</a></p>
<p>🐦Follow us on <a href="https://twitter.com/talking_papers" rel="noreferrer noopener" target="_blank">Twitter</a></p>
<p>🎥Subscribe to our </p>
 

</div>