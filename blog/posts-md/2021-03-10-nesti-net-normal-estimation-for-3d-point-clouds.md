---
layout: layouts/blog-post.njk
title: "Nesti-Net: Normal estimation for 3D Point Clouds"
date: 2021-03-10
author: Itzik Ben-Shabat
permalink: "/blog/posts/2021-03-10-nesti-net-normal-estimation-for-3d-point-clouds.html"
---

<div class="post-content">


<p>Important links:  [<a href="https://arxiv.org/abs/1812.00709" rel="noopener noreferrer" target="_blank">paper</a>], [<a href="https://github.com/sitzikbs/Nesti-Net" rel="noopener noreferrer" target="_blank">code</a>], [<a href="https://www.youtube.com/watch?v=E7PudeA4XvM" rel="noopener noreferrer" target="_blank">video</a>],[<a aria-label="poster (opens in a new tab)" href="/assets/images/blog/Nesti-Net_poster.pdf" rel="noreferrer noopener" target="_blank">poster</a>]</p>
<h2 class="wp-block-heading">ABSTRACT</h2>
<p>We propose a normal estimation method for unstructured 3D point clouds. This method, called Nesti-Net, builds on a new local point cloud representation which consists of multi-scale point statistics (MuPS), estimated on a local coarse Gaussian grid. This representation is suitable input to a CNN architecture. The normals are estimated using a mixture-of-experts (MoE) architecture, which relies on a data-driven approach for selecting the optimal scale around each point and encourages sub-network specialization. Interesting insights into the network’s resource distribution are provided. The scale prediction significantly improves robustness to different noise levels, point density variations and different levels of detail. We achieve state-of-the-art results on a benchmark synthetic dataset and present qualitative results on real scanned scenes.  </p>
<p>Code and trained models are available on <a href="https://github.com/sitzikbs/Nesti-Net"> https://github.com/sitzikbs/Nesti-Net</a>.</p>
<div class="wp-block-image"><figure class="aligncenter is-resized">{% responsiveImage "../../assets/images/blog/NestiNet_pipeline-01_for_web.jpg", "Nesti-Net normal estimation from unstructured 3D point clouds pipeline" %}
<figcaption>Nesti-Net normal estimation pipeline</figcaption></figure></div>
<h3 class="wp-block-heading"><strong>Cite</strong>:</h3>
<p>arXiv (preprint):</p>
<pre class="wp-block-code"><code>@article{ben2018nesti,   
title={Nesti-Net: Normal Estimation for Unstructured 3D Point Clouds using Convolutional Neural Networks},   
author={Ben-Shabat, Yizhak and Lindenbaum, Michael and Fischer, Anath},   journal={arXiv preprint arXiv:1812.00709}, 
year={2018} }</code></pre>
<p>CVPR :</p>
<pre class="wp-block-code"><code>@inproceedings{ben2018nesti,  
 title={Nesti-Net: Normal Estimation for Unstructured 3D Point Clouds using Convolutional Neural Networks},   
author={Ben-Shabat, Yizhak and Lindenbaum, Michael and Fischer, Anath},   booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},  
pages={},   
year={2019} }</code></pre>
<h3 class="wp-block-heading"><strong>Summary video</strong></h3>
<p><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/E7PudeA4XvM?feature=oembed" title="Nesti-Net: Normal Estimation for Unstructured 3D Point Clouds using Convolutional Neural Networks" width="800"></iframe></p>
<p>Additional tutorials: </p>
<p><a aria-label="How to visualize normal vectors on 3D point clouds ? (opens in a new tab)" href="https://www.itzikbs.com/how-to-visualize-normal-vectors-on-3d-point-clouds" rel="noreferrer noopener" target="_blank">How to visualize normal vectors on 3D point clouds ?</a></p>
 

</div>