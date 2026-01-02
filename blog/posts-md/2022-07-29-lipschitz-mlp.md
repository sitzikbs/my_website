---
layout: layouts/blog-post.njk
title: "Learning Smooth Neural Functions via Lipschitz Regularization"
date: 2022-07-29
author: Itzik Ben-Shabat
permalink: "/blog/posts/2022-07-29-lipschitz-mlp.html"
---

<div class="post-content">


<p>In this episode of the <a href="https://www.itzikbs.com/the-talking-papers-podcast" rel="noreferrer noopener" target="_blank">Talking Papers Podcast</a>, I hosted <a href="https://www.dgp.toronto.edu/~hsuehtil/" rel="noreferrer noopener" target="_blank">Hsueh-Ti Derek Liu</a> to chat about his paper “<a href="https://arxiv.org/abs/2202.08345" rel="noreferrer noopener" target="_blank">Learning Smooth Neural Functions via Lipschitz Regularization</a>”, published in SIGGRAPH 2022. </p>
<p>In this paper, they took on the unique task of enforcing smoothness on Neural Fields (modelled as a neural network). They do this by introducing a regularization term that forces the Lipschitz constant of the network to be very small. They show the performance of their method on shape interpolation, extrapolation and partial shape reconstruction from 3D point clouds. I mostly like the fact that it is implemented in only 4 lines of code. <br/> </p>
<p>Derek will soon complete his PhD at the University of Toronto and will start a research scientist position at <a href="https://corp.roblox.com/research/" rel="noreferrer noopener" target="_blank">Roblox Research</a>. This work was done when he was interning at NVIDIA. During our chat, I discovered that Derek is one of the few humans on the plant that has the ability to take a complicated idea and explain it in a simple and easy-to-follow way. His strong background in geometry processing makes this paper, which is well within the learning domain, very unique in the current paper landscape. It was a pleasure recording this episode with him. </p>
<div id="buzzsprout-player-10981175"></div><script charset="utf-8" src="https://www.buzzsprout.com/1914034/10981175-lipschitz-mlp-hsueh-ti-derek-liu.js?container_id=buzzsprout-player-10981175&amp;player=small" type="text/javascript"></script>
<h2 class="wp-block-heading" id="authors">AUTHORS</h2>
<p id="stephen-gould-richard-hartleydylan-campbell"><a href="https://www.itzikbs.com/" rel="noreferrer noopener" target="_blank">Hsueh-Ti Derek Liu, Francis Williams, Alec Jacobson, Sanja Fidler, Or Litany</a></p>
<p> </p>
<h2 class="wp-block-heading" id="abstract">ABSTRACT</h2>
<p>Neural implicit fields have recently emerged as a useful representation for 3D shapes. These fields are commonly represented as neural networks which map latent descriptors and 3D coordinates to implicit function values. The latent descriptor of a neural field acts as a deformation handle for the 3D shape it represents. Thus, smoothness with respect to this descriptor is paramount for performing shape-editing operations. In this work, we introduce a novel regularization designed to encourage smooth latent spaces in neural fields by penalizing the upper bound on the field’s Lipschitz constant. Compared with prior Lipschitz regularized networks, ours is computationally fast, can be implemented in four lines of code, and requires minimal hyperparameter tuning for geometric applications. We demonstrate the effectiveness of our approach on shape interpolation and extrapolation as well as partial shape reconstruction from 3D point clouds, showing both qualitative and quantitative improvements over existing state-of-the-art and non-regularized baselines.</p>
<p> </p>
<h2 class="wp-block-heading" id="related-papers">RELATED (WORKS|PAPERS)</h2>
<p>📚</p>
<p>📚<a href="https://neuralfields.cs.brown.edu/">Neural Fields (collection of works)</a></p>
<p>📚<a href="http://proceedings.mlr.press/v97/anil19a.html">Sorting Out Lipschitz Function Approximation</a></p>
<p></p>
<h2 class="wp-block-heading">LINKS AND RESOURCES</h2>
<p>💻<a href="https://nv-tlabs.github.io/lip-mlp/" rel="noreferrer noopener" target="_blank">Project website</a></p>
<p>📚 <a href="https://www.dgp.toronto.edu/~hsuehtil/pdf/lipmlp.pdf" rel="noreferrer noopener" target="_blank">Paper</a></p>
<p>💻<a href="https://github.com/ml-for-gp/jaxgptoolbox/tree/main/demos/lipschitz_mlp" rel="noreferrer noopener" target="_blank">Code</a></p>
<p></p>
<p>To stay up to date with Derek’s latest research, follow him on:</p>
<p>👨🏻‍🎓<a href="https://www.dgp.toronto.edu/~hsuehtil/" rel="noreferrer noopener" target="_blank">Personal Page</a></p>
<p>🐦<a href="https://twitter.com/HTDerekLiu">Twitter</a></p>
<p>👨🏻‍🎓<a href="https://scholar.google.com/citations?user=-T7Au0kAAAAJ&amp;hl=en&amp;oi=ao">Google Scholar</a></p>
<p></p>
<p></p>
<p></p>
<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/fo5kECey_dg?feature=oembed" title="Learning Smooth Neural Functions via Lipschitz Regularization (SIGGRAPH 2022) on Talking Papers" width="800"></iframe>
</div></figure>
<p>Recorded on May 30th 2022.</p>
<h2 class="wp-block-heading"><br/>CONTACT</h2>
<p>If you would like to be a guest, sponsor or just share your thoughts, feel free to reach out via email: <a class="__cf_email__" data-cfemail="8cf8ede0e7e5e2eba2fcedfce9feffa2fce3e8efedfff8ccebe1ede5e0a2efe3e1" href="/cdn-cgi/l/email-protection">[email protected]</a></p>
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