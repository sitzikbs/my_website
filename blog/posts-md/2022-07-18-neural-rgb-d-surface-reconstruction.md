---
layout: layouts/blog-post.njk
title: "Neural RGB-D Surface Reconstruction"
date: 2022-07-18
author: Itzik Ben-Shabat
permalink: "/blog/posts/2022-07-18-neural-rgb-d-surface-reconstruction.html"
---

<div class="post-content">
{% raw %}




<p>In this episode of the <a href="https://www.itzikbs.com/the-talking-papers-podcast" rel="noreferrer noopener" target="_blank">Talking Papers Podcast</a>, I hosted<a href="http://niessnerlab.org/members/dejan_azinovic/profile.html" rel="noreferrer noopener" target="_blank"> Dejan Azinović </a>to chat about his paper “<a href="https://dazinovic.github.io/neural-rgbd-surface-reconstruction/" rel="noreferrer noopener" target="_blank">Neural RGB-D Surface Reconstruction</a>”, published in CVPR 2022. </p>
<p>In this paper, they take on the task of RGBD surface reconstruction by using novel view synthesis.  They incorporate depth measurements into the radiance field formulation by learning a neural network that stores a truncated signed distance field. This formulation is particularly useful in regions where depth is missing and the color information can help fill in the gaps. </p>
<p>I first met Dejan during <a href="https://www.itzikbs.com/reasearch-visit-in-germany" rel="noreferrer noopener" target="_blank">my research visit to TUM during my PhD</a>.  We spent some long evenings at the office but also managed to play a little bit of volleyball (until someone nearly broke a finger).  I am looking forward to catching up in person at CVPR 2022. It was a pleasure hosting him on the podcast. </p>
<div id="buzzsprout-player-10568898">{% endraw %}
</div><script charset="utf-8" src="https://www.buzzsprout.com/1914034/10568898-dejan-azinovic-neural-rgbd-surface-reconstruction.js?container_id=buzzsprout-player-10568898&amp;player=small" type="text/javascript"></script>
<h2 class="wp-block-heading" id="authors">AUTHORS</h2>
<p id="stephen-gould-richard-hartleydylan-campbell">Dejan Azinović Ricardo Martin-Brualla Dan B Goldman Matthias Nießner Justus Thies</p>
<p> </p>
<h2 class="wp-block-heading" id="abstract">ABSTRACT</h2>
<p>In this work, we explore how to leverage the success of implicit novel view synthesis methods for surface reconstruction. Methods which learn a neural radiance field have shown amazing image synthesis results, but the underlying geometry representation is only a coarse approximation of the real geometry. We demonstrate how depth measurements can be incorporated into the radiance field formulation to produce more detailed and complete reconstruction results than using methods based on either color or depth data alone. In contrast to a density field as the underlying geometry representation, we propose to learn a deep neural network which stores a truncated signed distance field. Using this representation, we show that one can still leverage differentiable volume rendering to estimate color values of the observed images during training to compute a reconstruction loss. This is beneficial for learning the signed distance field in regions with missing depth measurements. Furthermore, we correct for misalignment errors of the camera, improving the overall reconstruction quality. In several experiments, we show-cast our method and compare to existing works on classical RGB-D fusion and learned representations.</p>
<p> </p>
<h2 class="wp-block-heading" id="related-papers">RELATED (WORKS|PAPERS)</h2>
<p>📚<a href="https://www.matthewtancik.com/nerf">NeRF</a></p>
<p>📚<a href="https://graphics.stanford.edu/projects/bundlefusion/" rel="noreferrer noopener" target="_blank">Bundle Fusion</a></p>
<p></p>
<h2 class="wp-block-heading">LINKS AND RESOURCES</h2>
<p>💻<a href="https://dazinovic.github.io/neural-rgbd-surface-reconstruction/">Project website</a></p>
<p>💻<a href="https://github.com/dazinovic/neural-rgbd-surface-reconstruction">Code</a></p>
<p>📚 <a href="https://arxiv.org/abs/2104.04532">Paper</a></p>
<p>🎥<a href="https://www.youtube.com/watch?v=iWuSowPsC3g&amp;ab_channel=MatthiasNiessner" rel="noreferrer noopener" target="_blank">Video</a></p>
<p></p>
<p>To stay up to date with Dejan’s latest research, follow him on:</p>
<p>👨🏻‍🎓<a href="http://niessnerlab.org/members/dejan_azinovic/profile.html" rel="noreferrer noopener" target="_blank">Dejan’s homepage</a></p>
<p>🎓<a href="https://scholar.google.com/citations?user=XEeGe_Bcwg4C&amp;hl=en&amp;oi=ao">Google Scholar</a></p>
<p>🐦<a href="https://twitter.com/DejanAzinovic">Twitter</a></p>
<p>👨🏻‍🎓<a href="https://www.linkedin.com/in/dejan-azinovi%C4%87-8b3430101">LinkedIn</a></p>
<p></p>
<p></p>
<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/Brd-8Sdtqrs?feature=oembed" title="Neural RGB-D Surface Reconstruction (CVPR2022) - Dejan Azinović on Talking Papers" width="800"></iframe>
</div></figure>
<p>Recorded on April 4th 2022.</p>
<h2 class="wp-block-heading"><br/>CONTACT</h2>
<p>If you would like to be a guest, sponsor or just share your thoughts, feel free to reach out via email: <a class="__cf_email__" data-cfemail="3347525f585a5d541d4352435641401d435c575052404773545e525a5f1d505c5e" href="/cdn-cgi/l/email-protection">[email protected]</a></p>
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