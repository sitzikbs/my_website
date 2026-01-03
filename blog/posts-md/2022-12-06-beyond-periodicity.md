---
layout: layouts/blog-post.njk
title: "Beyond Periodicity: Towards a Unifying Framework for Activations in Coordinate-MLPs"
date: 2022-12-06
author: Itzik Ben-Shabat
permalink: "/blog/posts/2022-12-06-beyond-periodicity.html"
---

<div class="post-content">
{% raw %}




<p>In this episode of the <a href="https://www.itzikbs.com/the-talking-papers-podcast" rel="noreferrer noopener" target="_blank">Talking Papers Podcast</a>, I hosted Sameera Ranasinghe. We had a great chat about his paper “<a href="https://arxiv.org/pdf/2111.15135.pdf" rel="noreferrer noopener" target="_blank">Beyond Periodicity: Towards a Unifying Framework for Activations in Coordinate-MLPs</a>”, published in ECCV 2022 as an oral presentation. </p>
<p>In this paper, they propose a new family of activation functions for coordinate MLPs and provide a theoretical analysis of their effectiveness. Their main proposition is that the stable rank is a good measure and design tool for such activation functions. They show that their proposed activations outperform the traditional ReLU and Sine activations for image parametrization and novel view synthesis. They further show that while the proposed family of activations does not require positional encoding they can benefit from using it by reducing the number of layers significantly.</p>
<p>Sameera is currently an applied scientist at Amazon and the CTO and co-founder of <a href="https://conscient.ai/" rel="noreferrer noopener" target="_blank">ConscientAI</a>. His research focus is theoretical machine learning and computer vision. This work was done when he was a postdoc at the Australian Institute of Machine Learning (AIML). He completed his PhD at the Australian National University (ANU). We first met back in 2019 when I was a research fellow at ANU and he was still doing his PhD. I immediately noticed we share research interests and after a short period of time, I flagged him as a rising star in the field. It was a pleasure to chat with Sameera and I am looking forward to reading his future papers. </p>
<p></p>
<div id="buzzsprout-player-11693097">{% endraw %}
</div><script charset="utf-8" src="https://www.buzzsprout.com/1914034/11693097-beyond-periodicity-sameera-ramasinghe.js?container_id=buzzsprout-player-11693097&amp;player=small" type="text/javascript"></script>
<h2 class="wp-block-heading" id="authors">AUTHORS</h2>
<p id="stephen-gould-richard-hartleydylan-campbell"><em>Sameera Ramasinghe, Simon Lucey</em></p>
<p> </p>
<h2 class="wp-block-heading" id="abstract">ABSTRACT</h2>
<p>Neural implicit fields have recently emerged as a useful representation for 3D shapes. These fields are Coordinate-based networks have emerged as a powerful tool for 3D representation and scene reconstruction. These networks are trained to map continuous input coordinates to the value of a signal at each point. Still, current architectures are black boxes: their spectral characteristics cannot be easily Image-based volumetric humans using pixel-aligned features promise generalization to unseen poses and identities. Prior work leverages global spatial encodings and multi-view geometric consistency to Coordinate-MLPs are emerging as an effective tool for modeling multidimensional continuous signals, overcoming many drawbacks associated with discrete grid-based approximations. However, coordinate-MLPs with ReLU activations, in their rudimentary form, demonstrate poor performance in representing signals with high fidelity, promoting the need for positional embedding layers. Recently, Sitzmann et al. proposed a sinusoidal activation function that has the capacity to omit positional embedding from coordinate-MLPs while still preserving high signal fidelity. Despite its potential, ReLUs are still dominating the space of coordinate-MLPs; we speculate that this is due to the hyper-sensitivity of networks — that employ such sinusoidal activations — to the initialization schemes. In this paper, we attempt to broaden the current understanding of the effect of activations in coordinate-MLPs, and show that there exists a broader class of activations that are suitable for encoding signals. We affirm that sinusoidal activations are only a single example in this class, and propose several non-periodic functions that empirically demonstrate more robust performance against random initializations than sinusoids. Finally, we advocate for a shift towards coordinate-MLPs that employ these non-traditional activation functions due to their high performance and simplicity.</p>
<p> </p>
<p></p>
<h2 class="wp-block-heading" id="related-papers">RELATED (WORKS|PAPERS)</h2>
<p>📚</p>
<p>📚</p>
<p>📚”<a href="https://proceedings.neurips.cc/paper/2020/hash/55053683268957697aa39fba6f231c68-Abstract.html" rel="noreferrer noopener" target="_blank">Fourier Features Let Networks Learn High-Frequency Functions in Low Dimensional Domains</a>” </p>
<p>📚<a href="http://proceedings.mlr.press/v97/rahaman19a.html" rel="noreferrer noopener" target="_blank">On the Spectral Bias of Neural Networks</a></p>
<p></p>
<p></p>
<p></p>
<h2 class="wp-block-heading">LINKS AND RESOURCES</h2>
<p>📚 <a href="https://arxiv.org/pdf/2111.15135.pdf">Paper</a></p>
<p>💻<a href="https://github.com/samgregoost/Beyond_periodicity" rel="noreferrer noopener" target="_blank">Code</a></p>
<p></p>
<p></p>
<p>To stay up to date with Marko’s latest research, follow him on:</p>
<p>🐦<a href="https://twitter.com/SameeraRamasin1" rel="noreferrer noopener" target="_blank">Twitter</a></p>
<p>👨🏻‍🎓<a href="https://scholar.google.com.au/citations?view_op=list_works&amp;hl=en&amp;hl=en&amp;user=-j0m9aMAAAAJ" rel="noreferrer noopener" target="_blank">Google Scholar</a></p>
<p>👨🏻‍🎓<a href="https://www.linkedin.com/in/sameeraramasinghe/" rel="noreferrer noopener" target="_blank">LinkedIn</a></p>
<p></p>
<p></p>
<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/3hbkBMPxWqs?feature=oembed" title="Beyond Periodicity (ECCV 2022 oral) with Sameera Ramasinghe  on Talking papers" width="800"></iframe>
</div></figure>
<p>Recorded on November 14th 2022.</p>
<h2 class="wp-block-heading"><br/>CONTACT</h2>
<p>If you would like to be a guest, sponsor or share your thoughts, feel free to reach out via email: <a class="__cf_email__" data-cfemail="e397828f888a8d84cd938293869190cd938c8780829097a3848e828a8fcd808c8e" href="/cdn-cgi/l/email-protection">[email protected]</a></p>
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