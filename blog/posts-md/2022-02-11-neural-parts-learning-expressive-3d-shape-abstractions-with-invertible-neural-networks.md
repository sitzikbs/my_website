---
layout: layouts/blog-post.njk
title: "Neural Parts: Learning Expressive 3D Shape Abstractions with Invertible Neural Networks"
date: 2022-02-11
author: Itzik Ben-Shabat
permalink: "/blog/posts/2022-02-11-neural-parts-learning-expressive-3d-shape-abstractions-with-invertible-neural-networks.html"
---

<div class="post-content">
{% raw %}




<p>In this episode of the <a href="https://www.itzikbs.com/the-talking-papers-podcast" rel="noreferrer noopener" target="_blank">Talking Papers Podcast</a>, I hosted <a href="https://www.buzzsprout.com/1914034/episodes/10048637">Despoina Paschalidou</a> to chat about her paper “Neural Parts: Learning Expressive 3D Shape Abstractions with Invertible Neural Networks”, published in CVPR 2021. Neural Parts learns to parse geometrically accurate and semantically consistent part arrangements without any part-level supervision. Despoina is currently a postdoctoral researcher at the <a href="https://geometry.stanford.edu">Geometric Computation Group</a> at Stanford University. This work was done back when she was still a PhD student at <a href="https://learning-systems.org/">Max Planck ETH Center for Learning Systems</a>. Her unique perspective on interpretable 3D shapes representations makes her stand out in this domain where interpretability is often overlooked. Despoina is the first guest on the podcast that I did not personally know before the interview and she made the experience so pleasant and fun and it was a pleasure recording this episode with her. </p>
<div id="buzzsprout-player-10048637">{% endraw %}
</div><script charset="utf-8" src="https://www.buzzsprout.com/1914034/10048637-despoina-paschalidou-neural-parts.js?container_id=buzzsprout-player-10048637&amp;player=small" type="text/javascript"></script>
<h2 class="wp-block-heading" id="authors">AUTHORS</h2>
<p id="stephen-gould-richard-hartleydylan-campbell"><a href="https://paschalidoud.github.io/">Despoina Paschalidou </a>, <a href="https://angeloskath.github.io/">Angelos Katharopoulos</a>, <a href="http://cvlibs.net/">Andreas Geiger</a>, <a href="https://www.cs.utoronto.ca/~fidler/">Sanja Fidler</a></p>
<p></p>
<h2 class="wp-block-heading" id="abstract">ABSTRACT</h2>
<p>Impressive progress in 3D shape extraction led to representations that can capture object geometries with high fidelity. In parallel, primitive-based methods seek to represent objects as semantically consistent part arrangements. However, due to the simplicity of existing primitive representations, these methods fail to accurately reconstruct 3D shapes using a small number of primitives/parts. We address the trade-off between reconstruction quality and number of parts with Neural Parts, a novel 3D primitive representation that defines primitives using an Invertible Neural Network (INN) which implements homeomorphic mappings between a sphere and the target object. The INN allows us to compute the inverse mapping of the homomorphism, which in turn, enables the efficient computation of both the implicit surface function of a primitive and its mesh, without any additional post-processing. Our model learns to parse 3D objects into semantically consistent part arrangements without any part-level supervision. Evaluations on ShapeNet, D-FAUST and FreiHAND demonstrate that our primitives can capture complex geometries and thus simultaneously achieve geometrically accurate as well as interpretable reconstructions using an order of magnitude fewer primitives than state-of-the-art shape abstraction methods.</p>
<p></p>
<h2 class="wp-block-heading" id="related-papers">RELATED (WORKS|PAPERS)</h2>
<p>📚 “<a href="Unsupervised 3D Keypoint Discovery for Shape Control" rel="noreferrer noopener" target="_blank">KeypointDeformer: Unsupervised 3D Keypoint Discovery for Shape Control</a>“</p>
<p>📚 “<a href="https://openaccess.thecvf.com/content_cvpr_2017/papers/Tulsiani_Learning_Shape_Abstractions_CVPR_2017_paper.pdf" rel="noreferrer noopener" target="_blank">Learning Shape Abstractions by Assembling Volumetric Primitives”: Volumetric primitives</a>“</p>
<p>📚 “<a href="https://openaccess.thecvf.com/content_CVPR_2019/papers/Paschalidou_Superquadrics_Revisited_Learning_3D_Shape_Parsing_Beyond_Cuboids_CVPR_2019_paper.pdf" rel="noreferrer noopener" target="_blank">Superquadrics Revisited: Learning 3D Shape Parsing beyond Cuboids</a>“</p>
<p>📚 “<a href="Learnable Convex Decomposition" rel="noreferrer noopener" target="_blank">CvxNet: Learnable Convex Decomposition</a>“<br/><a href="https://proceedings.neurips.cc/paper/2020/hash/59a3adea76fadcb6dd9e54c96fc155d1-Abstract.html" rel="noreferrer noopener" target="_blank">📚 “Neural Star Domain as Primitive Representation</a>“</p>
<p>📚 “<a href="https://openaccess.thecvf.com/content_ICCV_2019/papers/Genova_Learning_Shape_Templates_With_Structured_Implicit_Functions_ICCV_2019_paper.pdf" rel="noreferrer noopener" target="_blank">Learning Shape Templates with Structured Implicit Functions</a>“</p>
<h2 class="wp-block-heading" id="links-and-resources">LINKS AND RESOURCES</h2>
<p>💻 Project Page: <a href="https://paschalidoud.github.io/neural_parts" rel="noreferrer noopener" target="_blank">https://paschalidoud.github.io/neural_parts</a></p>
<p>💻 CODE: <a href="https://github.com/paschalidoud/neural_parts" rel="noreferrer noopener" target="_blank">https://github.com/paschalidoud/neural_parts</a></p>
<p>💻<a href="https://autonomousvision.github.io/neural-parts/" rel="noreferrer noopener" target="_blank">Blog Post</a></p>
<p>📚 <a href="https://openaccess.thecvf.com/content/CVPR2021/html/Paschalidou_Neural_Parts_Learning_Expressive_3D_Shape_Abstractions_With_Invertible_Neural_CVPR_2021_paper.html" rel="noreferrer noopener" target="_blank">Paper Link</a>: “Neural Parts: Learning Expressive 3D Shape Abstractions with Invertible Neural Networks”</p>
<p><a href="https://www.youtube.com/watch?v=6WK3B0IZJsw&amp;ab_channel=AndreasGeiger" rel="noreferrer noopener" target="_blank">🎥</a> <a href="https://www.youtube.com/watch?v=6WK3B0IZJsw&amp;ab_channel=AndreasGeiger" rel="noreferrer noopener" target="_blank">Paper video</a></p>
<figure class="wp-block-embed is-type-rich is-provider-embed-handler wp-block-embed-embed-handler wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/XEeGIHaXsik?feature=oembed" title="Talking Papers Podcast with  Despoina Paschalidou - Neural Parts" width="800"></iframe>
</div></figure>
<p></p>
<p>This episode was recorded on April, 25th 2021.</p>
<p></p>
<h2 class="wp-block-heading" id="contact"> CONTACT</h2>
<p>If you would like to be a guest, sponsor or just share your thoughts, feel free to reach out via email: <a class="__cf_email__" data-cfemail="4c382d202725222b623c2d3c293e3f623c23282f2d3f380c2b212d2520622f2321" href="/cdn-cgi/l/email-protection">[email protected]</a></p>
<h2 class="wp-block-heading" id="subscribe-and-follow"><br/>SUBSCRIBE AND FOLLOW</h2>
<p> 🎧Subscribe on your favourite podcast app: <a href="https://talking.papers.podcast.itzikbs.com" rel="noreferrer noopener" target="_blank">https://talking.papers.podcast.itzikbs.com</a></p>
<p> 📧Subscribe to our mailing list: <a href="http://eepurl.com/hRznqb" rel="noreferrer noopener" target="_blank">http://eepurl.com/hRznqb</a></p>
<p> 🐦Follow us on Twitter: <a href="https://twitter.com/talking_papers" rel="noreferrer noopener" target="_blank">https://twitter.com/talking_papers</a> </p>
<p>🎥YouTube Channel: </p>
 

</div>