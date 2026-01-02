---
layout: layouts/blog-post.njk
title: "Deep Declarative Networks"
date: 2022-02-05
author: Itzik Ben-Shabat
permalink: "/blog/posts/2022-02-05-deep-declarative-networks.html"
---

<div class="post-content">


<p>In this episode of the <a href="https://www.itzikbs.com/the-talking-papers-podcast" rel="noreferrer noopener" target="_blank">Talking Papers Podcast</a>, I hosted Dylan Campbell to chat about his paper “Deep Declarative Networks – A New Hope”, published in TPAMI. DDN is a general name for injecting and solving an optimization problem within a neural network. They are particularly useful if you need to enforce constraints or get some guarantees for the solution. Dylan is currently a postdoc at the Visual Geometry Group (VGG) in Oxford and this work was done back when he was still a Research Fellow in The Australian Centre for Robotic Vision (ACRV) at the Australian National University (ANU) Node. Dylan has a unique perspective on optimization, in particular in applications involving geometry. He is a great researcher and a good friend and it was a pleasure recording this episode with him.</p>
<div id="buzzsprout-player-9879802"></div><script charset="utf-8" src="https://www.buzzsprout.com/1914034/9879802-dylan-campbell-deep-declarative-networks.js?container_id=buzzsprout-player-9879802&amp;player=small" type="text/javascript"></script>
<p></p>
<h2 class="wp-block-heading" id="authors">AUTHORS</h2>
<p id="stephen-gould-richard-hartleydylan-campbell"><a href="http://users.cecs.anu.edu.au/~sgould/" rel="noreferrer noopener" target="_blank">Stephen Gould</a>, Richard Hartley, Dylan Campbell</p>
<p></p>
<h2 class="wp-block-heading" id="abstract">ABSTRACT</h2>
<p>We explore a new class of end-to-end learnable models wherein data processing nodes (or network layers) are defined in terms of desired behaviour rather than an explicit forward function. Specifically, the forward function is implicitly defined as the solution to a mathematical optimization problem. Consistent with nomenclature in the programming languages community, we name these models deep declarative networks. Importantly, we show that the class of deep declarative networks subsumes current deep learning models. Moreover, invoking the implicit function theorem, we show how gradients can be back-propagated through many declaratively defined data processing nodes thereby enabling end-to-end learning. We show how these declarative processing nodes can be implemented in the popular PyTorch deep learning software library allowing declarative and imperative nodes to co-exist within the same network. We also provide numerous insights and illustrative examples of declarative nodes and demonstrate their application for image and point cloud classification tasks.</p>
<p></p>
<h2 class="wp-block-heading" id="related-papers">RELATED (WORKS|PAPERS)</h2>
<p>📚”<a href="https://arxiv.org/abs/1607.05447" rel="noreferrer noopener" target="_blank">On differentiating parameterized argmin and argmax problems with application to bi-level optimization</a>” : </p>
<p> 📚”<a href="Differentiable Optimization as a Layer in Neural Networks" rel="noreferrer noopener" target="_blank">OptNet: Differentiable Optimization as a Layer in Neural Networks</a>” : </p>
<p></p>
<h2 class="wp-block-heading" id="links-and-resources">LINKS AND RESOURCES</h2>
<p>CODE: 💻<a href="https://github.com/anucvml/ddn" rel="noreferrer noopener" target="_blank">https://github.com/anucvml/ddn</a></p>
<p>💻<a href="https://nbviewer.org/github/anucvml/ddn/tree/master/tutorials/" rel="noreferrer noopener" target="_blank">Jupiter notebooks</a></p>
<p><a href="https://arxiv.org/abs/1909.04866" rel="noreferrer noopener" target="_blank">Preprint Link</a>: “Deep Declarative Networks: a new hope” </p>
<p><a href="https://ieeexplore.ieee.org/abstract/document/9355027" rel="noreferrer noopener" target="_blank">Paper Link</a>: “Deep Declarative Networks”</p>
<p><a href="https://anucvml.github.io/ddn-eccvt2020/" rel="noreferrer noopener" target="_blank">ECCV 2020 Tutorial</a></p>
<p> <a href="https://anucvml.github.io/ddn-cvprw2020/" rel="noreferrer noopener" target="_blank">CVPR 2020 Workshop</a></p>
<p></p>
<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/TcbErocpnak?feature=oembed" title="Talking Papers Podcast with Dylan Campbell - Deep Declarative Networks" width="800"></iframe>
</div></figure>
<p></p>
<p>This episode was recorded on March, 31th 2021.</p>
<p></p>
<h2 class="wp-block-heading" id="contact"> CONTACT</h2>
<p>If you would like to be a guest, sponsor or just share your thoughts, feel free to reach out via email: <a class="__cf_email__" data-cfemail="8bffeae7e0e2e5eca5fbeafbeef9f8a5fbe4efe8eaf8ffcbece6eae2e7a5e8e4e6" href="/cdn-cgi/l/email-protection">[email protected]</a></p>
<h2 class="wp-block-heading" id="subscribe-and-follow"><br/>SUBSCRIBE AND FOLLOW</h2>
<p> 🎧Subscribe on your favourite podcast app: <a href="https://talking.papers.podcast.itzikbs.com" rel="noreferrer noopener" target="_blank">https://talking.papers.podcast.itzikbs.com</a></p>
<p> 📧Subscribe to our mailing list: <a href="http://eepurl.com/hRznqb" rel="noreferrer noopener" target="_blank">http://eepurl.com/hRznqb</a></p>
<p> 🐦Follow us on Twitter: <a href="https://twitter.com/talking_papers" rel="noreferrer noopener" target="_blank">https://twitter.com/talking_papers</a> </p>
<p>🎥YouTube Channel: </p>
 

</div>