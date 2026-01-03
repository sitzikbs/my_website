---
layout: layouts/blog-post.njk
title: "Surface fitting for 3D Point Cloud : DeepFit"
date: 2020-07-27
author: Itzik Ben-Shabat
permalink: "/blog/posts/2020-07-27-surface-fitting-for-3d-point-cloud-deepfit.html"
---

<div class="post-content">
{% raw %}




<p></p>
<h2 class="wp-block-heading">ABSTRACT</h2>
<p>We propose a method for 3D point cloud surface fitting. This method, called DeepFit, incorporates a neural network to learn point-wise weights for weighted least squares polynomial surface fitting. The learned weights act as a soft selection for the neighborhood of surface points thus avoiding the scale selection required of previous methods. To train the network we propose a novel surface consistency loss that improves point weight estimation. The method enables extracting normal vectors and other geometrical properties, such as principal curvatures, the latter were not presented as ground truth during training. We achieve state-of-the-art results on a benchmark normal and curvature estimation dataset, demonstrate robustness to noise, outliers and density variations, and show its application on noise removal.</p>
<figure class="wp-block-image size-large">{% endraw %}
{% responsiveImage "../../assets/images/blog/2020-07-DeepFit_Pipeline.png", "" %}
{% raw %}


<figcaption>DeepFit 3D point cloud surface fitting pipeline </figcaption></figure>
<h3 class="wp-block-heading">Cite</h3>
<p>arXiv (preprint):</p>
<pre class="wp-block-code"><code>@article{ben2020deepfit,
  title={DeepFit: 3D Surface Fitting via Neural Network Weighted Least Squares},
  author={Ben-Shabat, Yizhak and Gould, Stephen},
  journal={arXiv preprint arXiv:2003.10826},
  year={2020}
}</code></pre>
<p>ECCV 2020 (oral) (will update once paper is published)</p>
<pre class="wp-block-code"><code></code></pre>
<h3 class="wp-block-heading">Video</h3>
<figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/jwZDU6hVUzA?start=9&amp;feature=oembed" title="DeepFit : 3D Surface Fitting via Neural Network Weighted Least Squares (ECCV 2020 Oral) - 2 minutes" width="800"></iframe>
{% endraw %}
</div></figure>
<p></p>
<p>Important links: [<a href="https://arxiv.org/abs/2003.10826" rel="noreferrer noopener" target="_blank">preprint</a>] [<a href="https://youtu.be/jwZDU6hVUzA" rel="noreferrer noopener" target="_blank">short video</a>] [<a href="https://www.youtube.com/watch?v=PrlFen2BuaU" rel="noreferrer noopener" target="_blank">full video</a>] [<a href="https://github.com/sitzikbs/DeepFit" rel="noreferrer noopener" target="_blank">code</a>]</p>
<h3 class="wp-block-heading">Surface fitting – additional related content</h3>
<p>If you found DeepFit interesting, you may also like my <a aria-label="undefined (opens in a new tab)" href="https://www.itzikbs.com/nesti-net-normal-estimation-for-3d-point-clouds" rel="noreferrer noopener" target="_blank">Nesti-Net paper on normal estimation for 3D point clouds</a> that tackles a similar problem but instead of selecting points, it chooses the whole neighbourhood radius. Another relevant paper is <a aria-label="undefined (opens in a new tab)" href="https://www.itzikbs.com/3dmfv-net-3d-point-cloud-classification-using-cnns" rel="noreferrer noopener" target="_blank">3DmFV paper on deep learning on 3D point clouds</a> which tackles the first challenge in the DeepFit’s surface fitting pipeline which is applying deep learning on point clouds. A few years ago I made a summary of 3D point cloud classification methods. In this work, we chose to use PointNet, however, this block can be easily replaced with 3DmFV-Net (we actually tested it and got similar results), PointNet++, kd-network or any newer architecture. This obviously introduces a tradeoff between efficiency and accuracy which is inherent to all of these methods.</p>
<p></p>
<p></p>
<p>To stay up to date with my latest research: Follow me on <a aria-label="undefined (opens in a new tab)" href="https://twitter.com/sitzikbs" rel="noreferrer noopener" target="_blank">twitter</a> and subscribe to my <a aria-label="undefined (opens in a new tab)" href="https://www.youtube.com/channel/UCAvd5SJkGaI6lf54pLUioMA" rel="noreferrer noopener" target="_blank">YouTube channel</a>.</p>
 

</div>