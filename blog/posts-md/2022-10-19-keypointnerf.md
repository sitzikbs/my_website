---
layout: layouts/blog-post.njk
title: "KeypointNeRF: Generalizing Image-based Volumetric Avatars using Relative Spatial Encoding of Keypoints"
date: 2022-10-19
author: Itzik Ben-Shabat
permalink: "/blog/posts/2022-10-19-keypointnerf.html"
---

<div class="post-content">
{% raw %}




<p>In this episode of the <a href="https://www.itzikbs.com/the-talking-papers-podcast" rel="noreferrer noopener" target="_blank">Talking Papers Podcast</a>, I hosted <a href="https://www.research-collection.ethz.ch/discover?filtertype_1=contributors&amp;filter_relational_operator_1=authority&amp;filter_1=354592b81cfc3f244b7970316f2887c3">Marko</a> <a href="https://markomih.github.io/" rel="noreferrer noopener" target="_blank"><a href="https://www.research-collection.ethz.ch/discover?filtertype_1=contributors&amp;filter_relational_operator_1=authority&amp;filter_1=354592b81cfc3f244b7970316f2887c3">Mihajlovic</a></a><a href="https://www.dgp.toronto.edu/~hsuehtil/" rel="noreferrer noopener" target="_blank"> </a>. We had a great chat about his paper “<a href="https://www.research-collection.ethz.ch/handle/20.500.11850/563568" rel="noreferrer noopener" target="_blank">KeypointNeRF: Generalizing Image-based Volumetric Avatars using Relative Spatial Encoding of Keypoints</a>”, published in ECCV 2022. </p>
<p>In this paper, they create a generalizable NeRF for virtual avatars. To get a high-fidelity reconstruction of humans (from sparse observations), they leverage an off-the-shelf keypoint detector in order to condition the NeRF. Given as input two or three RGB images they generate a volumetric radiance representation that can be rendered from novel views. In other words, take a few selfies and get your own personal avatar. </p>
<p>Marko is a 2nd year PhD student at ETH, supervised by Siyu Tang. His research focuses on photorealistic reconstruction of static and dynamic scenes and also modeling of parametric human bodies. This work was done mainly during his internship at Meta Reality Labs. Marko and I met at <a href="https://www.itzikbs.com/shape-as-points-a-differentiable-poisson-solver" rel="noreferrer noopener" target="_blank">CVPR 2022</a>. In fact, <a href="https://www.itzikbs.com/shape-as-points-a-differentiable-poisson-solver" rel="noreferrer noopener" target="_blank">Songyou Peng</a> (who was also a guest on the podcast) introduced us. It was a pleasure to chat with Marko and I am looking forward to reading his future papers. </p>
<p></p>
<div id="buzzsprout-player-11527637">{% endraw %}
</div><script charset="utf-8" src="https://www.buzzsprout.com/1914034/11527637-keypointnerf-marko-mihajlovic.js?container_id=buzzsprout-player-11527637&amp;player=small" type="text/javascript"></script>
<h2 class="wp-block-heading" id="authors">AUTHORS</h2>
<p id="stephen-gould-richard-hartleydylan-campbell"><em>Marko</em> <em>Mihajlovic, <em>Aayush</em></em> <em>Bansal, <em>Michael</em></em> <em>Zollhoefer, <em>Siyu</em></em> <em>Tang, <em>Shunsuke</em></em> <em>Saito</em></p>
<p> </p>
<h2 class="wp-block-heading" id="abstract">ABSTRACT</h2>
<p>Neural implicit fields have recently emerged as a useful representation for 3D shapes. These fields are Coordinate-based networks have emerged as a powerful tool for 3D representation and scene reconstruction. These networks are trained to map continuous input coordinates to the value of a signal at each point. Still, current architectures are black boxes: their spectral characteristics cannot be easily Image-based volumetric humans using pixel-aligned features promise generalization to unseen poses and identities. Prior work leverages global spatial encodings and multi-view geometric consistency to reduce spatial ambiguity. However, global encodings often suffer from overfitting to the distribution of the training data, and it is difficult to learn multi-view consistent reconstruction from sparse views. In this work, we investigate common issues with existing spatial encodings and propose a simple yet highly effective approach to modeling high-fidelity volumetric humans from sparse views. One of the key ideas is to encode relative spatial 3D information via sparse 3D keypoints. This approach is robust to the sparsity of viewpoints and cross-dataset domain gap. Our approach outperforms state-of-the-art methods for head reconstruction. On human body reconstruction for unseen subjects, we also achieve performance comparable to prior work that uses a parametric human body model and temporal feature aggregation. Our experiments show that a majority of errors in prior work stem from an inappropriate choice of spatial encoding and thus we suggest a new direction for high-fidelity image-based human modeling.</p>
<p> </p>
<p></p>
<h2 class="wp-block-heading" id="related-papers">RELATED (WORKS|PAPERS)</h2>
<p>📚</p>
<p>📚<a href="https://arxiv.org/abs/2102.13090" rel="noreferrer noopener" target="_blank">IBRNet</a></p>
<p>📚<a href="https://arxiv.org/abs/1905.05172">PIFu</a></p>
<p></p>
<p></p>
<h2 class="wp-block-heading">LINKS AND RESOURCES</h2>
<p>💻<a href="https://markomih.github.io/KeypointNeRF">Project website</a></p>
<p>📚 <a href="https://www.research-collection.ethz.ch/handle/20.500.11850/563568" rel="noreferrer noopener" target="_blank">Paper</a></p>
<p>💻<a href="https://github.com/facebookresearch/KeypointNeRF" rel="noreferrer noopener" target="_blank">Code</a></p>
<p>🎥<a href="https://youtu.be/RMs1S5k9vrk">Video</a></p>
<p></p>
<p>To stay up to date with Marko’s latest research, follow him on:</p>
<p>👨🏻‍🎓<a href="https://markomih.github.io" rel="noreferrer noopener" target="_blank">Personal Page</a></p>
<p>🐦<a href="https://twitter.com/marko_mih">Twitter</a></p>
<p>👨🏻‍🎓<a href="https://scholar.google.com/citations?user=RYicr-QAAAAJ&amp;hl=en">Google Scholar</a></p>
<p></p>
<p></p>
<figure class="wp-block-embed is-type-rich is-provider-embed-handler wp-block-embed-embed-handler wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" style="border: none;" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/nzMOJEV_iY0?feature=oembed" title="KeypointNeRF: Generalizing Image-based Volumetric Avatars (ECCV 2022) on Talking Papers" width="800"></iframe>
</div></figure>
<p>Recorded on August 8th 2022.</p>
<h2 class="wp-block-heading"><br/>CONTACT</h2>
<p>If you would like to be a guest, sponsor or just share your thoughts, feel free to reach out via email: <a class="__cf_email__" data-cfemail="493d28252220272e673928392c3b3a6739262d2a283a3d092e24282025672a2624" href="/cdn-cgi/l/email-protection">[email protected]</a></p>
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