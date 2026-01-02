---
layout: layouts/blog-post.njk
title: "Shape As Points: A Differentiable Poisson Solver"
date: 2022-07-18
author: Itzik Ben-Shabat
permalink: "/blog/posts/2022-07-18-shape-as-points-a-differentiable-poisson-solver.html"
---

<div class="post-content">


<p>In this episode of the <a href="https://www.itzikbs.com/the-talking-papers-podcast" rel="noreferrer noopener" target="_blank">Talking Papers Podcast</a>, I hosted <a href="https://pengsongyou.github.io/" rel="noreferrer noopener" target="_blank">Songyou Peng</a> to chat about his paper “Shape As Points: A Differentiable Poisson Solver”, published in NeurIPS 2021. In this paper, they take on the task of surface reconstruction and propose a hybrid representation that unifies explicit and implicit representation in addition to a differentiable solver for the classic Poisson surface reconstruction. I have been following Songyou’s work for a while and was very surprised to discover that he is just about midway through his PhD (with so many good papers, I thought he is about to finish!). We first met online at the ICCV 2021 workshop on “<a href="http://ivl.cs.brown.edu/3DReps/posters.html" rel="noopener" target="_blank">Learning 3D Representations for Shape and Appearance</a>” and I immediately flagged him as one of the next guests on the podcast.<br/>It was a pleasure recording this episode with him.</p>
<div id="buzzsprout-player-10135005"> </div>
<p><script charset="utf-8" src="https://www.buzzsprout.com/1914034/10135005-songyou-peng-shape-as-points.js?container_id=buzzsprout-player-10135005&amp;player=small" type="text/javascript"></script></p>
<h2 class="wp-block-heading" id="authors">AUTHORS</h2>
<p id="stephen-gould-richard-hartleydylan-campbell">Songyou Peng, Chiyu Jiang, Yiyi Liao, Michael Niemeyer, Marc Pollefeys, Andreas Geiger</p>
<p> </p>
<h2 class="wp-block-heading" id="abstract">ABSTRACT</h2>
<p>In recent years, neural implicit representations gained popularity in 3D reconstruction due to their expressiveness and flexibility. However, the implicit nature of neural implicit representations results in slow inference time and requires careful initialization. In this paper, we revisit the classic yet ubiquitous point cloud representation and introduce a differentiable point-to-mesh layer using a differentiable formulation of Poisson Surface Reconstruction (PSR) that allows for a GPU-accelerated fast solution of the indicator function given an oriented point cloud. The differentiable PSR layer allows us to efficiently and differentiably bridge the explicit 3D point representation with the 3D mesh via the implicit indicator field, enabling end-to-end optimization of surface reconstruction metrics such as Chamfer distance. This duality between points and meshes hence allows us to represent shapes as oriented point clouds, which are explicit, lightweight and expressive. Compared to neural implicit representations, our Shape-As-Points (SAP) model is more interpretable, lightweight, and accelerates inference time by one order of magnitude. Compared to other explicit representations such as points, patches, and meshes, SAP produces topology-agnostic, watertight manifold surfaces. We demonstrate the effectiveness of SAP on the task of surface reconstruction from unoriented point clouds and learning-based reconstruction.</p>
<p> </p>
<h2 class="wp-block-heading" id="related-papers">RELATED (WORKS|PAPERS)</h2>
<p>📚 <a href="https://www.cse.iitd.ac.in/~mcs112609/poission.pdf" rel="noopener" target="_blank">Poisson Surface Reconstruction</a></p>
<p>📚 <a href="https://openaccess.thecvf.com/content_CVPR_2019/html/Mescheder_Occupancy_Networks_Learning_3D_Reconstruction_in_Function_Space_CVPR_2019_paper.html" rel="noopener" target="_blank">Occupancy Networks</a></p>
<p>📚 <a href="https://link.springer.com/chapter/10.1007/978-3-030-58580-8_31" rel="noreferrer noopener" target="_blank">Convolutional Occupancy Networks</a></p>
<p></p>
<h2 class="wp-block-heading">LINKS AND RESOURCES</h2>
<p>💻Project Page: <a href="https://pengsongyou.github.io/sap" rel="noreferrer noopener" target="_blank">https://pengsongyou.github.io/sap</a></p>
<p>💻CODE: <a href="https://github.com/autonomousvision/shape_as_points" rel="noreferrer noopener" target="_blank">https://github.com/autonomousvision/shape_as_points</a></p>
<p>📚 <a href="https://arxiv.org/abs/2106.03452" rel="noreferrer noopener" target="_blank">Paper</a></p>
<p>🤐<a href="https://openreview.net/forum?id=Ecuu521mPpG" rel="noreferrer noopener" target="_blank">Paper’s peer review</a></p>
<p>To stay up to date with Songyou’s latest research, check out <a href="https://pengsongyou.github.io/" rel="noreferrer noopener" target="_blank">his personal page</a> and follow him on:</p>
<p>🎓<a href="https://scholar.google.com/citations?user=eNypkO0AAAAJ" rel="noreferrer noopener" target="_blank">Google Scholar</a></p>
<p>🐦<a href="https://twitter.com/songyoupeng" rel="noreferrer noopener" target="_blank">Twitter</a></p>
<p>👨🏻‍🎓<a href="https://www.linkedin.com/in/songyou-peng-53717648/" rel="noreferrer noopener" target="_blank">LinkedIn</a></p>
<p></p>
<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/1bZaKno2FFg?feature=oembed" title="Talking Papers Podcast with Songyou Peng - Shape as points" width="800"></iframe>
</div></figure>
<h2 class="wp-block-heading"><br/>CONTACT</h2>
<p>If you would like to be a guest, sponsor or just share your thoughts, feel free to reach out via email: <a class="__cf_email__" data-cfemail="f286939e999b9c95dc829382978081dc829d9691938186b2959f939b9edc919d9f" href="/cdn-cgi/l/email-protection">[email protected]</a></p>
<p></p>
<h2 class="wp-block-heading">SUBSCRIBE AND FOLLOW</h2>
<p>🎧Subscribe on your favourite podcast app: <a href="https://talking.papers.podcast.itzikbs.com" rel="noreferrer noopener" target="_blank">https://talking.papers.podcast.itzikbs.com</a></p>
<p>📧Subscribe to our mailing list: <a href="http://eepurl.com/hRznqb" rel="noreferrer noopener" target="_blank">http://eepurl.com/hRznqb</a></p>
<p>🐦Follow us on Twitter: <a href="https://twitter.com/talking_papers" rel="noreferrer noopener" target="_blank">https://twitter.com/talking_papers</a></p>
<p>🎥YouTube Channel: </p>
<p></p>
<p></p>
<p></p>
 

</div>