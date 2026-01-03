---
layout: layouts/blog-post.njk
title: "What is 3D modified Fisher Vector (3DmFV) representation for 3D point clouds"
date: 2021-03-10
author: Itzik Ben-Shabat
permalink: "/blog/posts/2021-03-10-what-is-3d-modified-fisher-vector-3dmfv-representation-for-3d-point-clouds.html"
---

<div class="post-content">


<p>Recently we published a paper about 3D point cloud classification (and segmentation) using our proposed 3D modified Fisher Vector (3DmFV) representation and convolutional neural networks (CNNs).  The preprint is <a href="https://arxiv.org/abs/1711.08241" rel="noopener" target="_blank">available on ArXiv</a> and the final version is available in <a href="https://ieeexplore.ieee.org/abstract/document/8394990/" rel="noopener" target="_blank">Robotics and Automation Letters (RA-L)</a> journal.</p>
<p>I believe in making research accessible to everyone so I give here a brief explanation about the 3DmFV representation for point clouds.</p>
<p>Before reading this post it is important to have a solid understanding of Gaussian Mixture Models (GMMs) and Fisher Vectors (FVs). If you are a bit rusty on these subjects I posted two primers in the links below:</p>
<ol>
<li><a href="https://www.itzikbs.com/gaussian-mixture-model-gmm-3d-point-cloud-classification-primer" rel="noopener" target="_blank">Gaussian Mixture Models (GMM). </a></li>
<li><a href="https://www.itzikbs.com/what-is-a-fisher-vector-for-3d-point-clouds-3d-point-cloud-classification-primer" rel="noopener" target="_blank">Fisher Vectors</a></li>
</ol>
<p>The 3D modified Fisher Vector (3DmFV) generalizes the <a href="https://www.itzikbs.com/what-is-a-fisher-vector-for-3d-point-clouds-3d-point-cloud-classification-primer" rel="noopener" target="_blank">Fisher Vector</a> along two directions</p>
<ol>
<li>GMM choice – 3DmFV uses a uniform Gaussian grid – The Gaussians parameters ( mean, standard deviation and weights) are not estimated from the data, they are predefined and position on a 3D grid, with equal weights and standard deviation.</li>
<li>Symmetric functions – adding minimum and maximum (in addition to the summation) operating on all points, for each Gaussian.</li>
</ol>
<h2>The Math</h2>
<p>3DmFV is formally defined by :</p>
<p style="text-align: center;"><img alt="3DmFV_{\lambda}^X = \left[ \begin{array}{c}\left. \sum_{t=1}^TL_\lambda\nabla_\lambda\log u_\lambda(p_t) \right|_{\lambda=\alpha,\mu,\sigma} \\\left. \max_t(L_\lambda\nabla_\lambda\log u_\lambda(p_t)\right|_{\lambda=\alpha,\mu,\sigma} \\\left. \min_t(L_\lambda\nabla_\lambda\log u_\lambda(p_t))\right|_{\lambda=\mu,\sigma} \end{array}\right]" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=3DmFV_%7B%5Clambda%7D%5EX+%3D+%5Cleft%5B+%5Cbegin%7Barray%7D%7Bc%7D%5Cleft.+%5Csum_%7Bt%3D1%7D%5ETL_%5Clambda%5Cnabla_%5Clambda%5Clog+u_%5Clambda%28p_t%29+%5Cright%7C_%7B%5Clambda%3D%5Calpha%2C%5Cmu%2C%5Csigma%7D+%5C%5C%5Cleft.+%5Cmax_t%28L_%5Clambda%5Cnabla_%5Clambda%5Clog+u_%5Clambda%28p_t%29%5Cright%7C_%7B%5Clambda%3D%5Calpha%2C%5Cmu%2C%5Csigma%7D+%5C%5C%5Cleft.+%5Cmin_t%28L_%5Clambda%5Cnabla_%5Clambda%5Clog+u_%5Clambda%28p_t%29%29%5Cright%7C_%7B%5Clambda%3D%5Cmu%2C%5Csigma%7D+%5Cend%7Barray%7D%5Cright%5D&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/></p>
<h2>The Intuition</h2>
<p>It is much easier to understand the 3DmFV for points with some nice visualizations.</p>
<p>Let’s take a single 3D point in a single Gaussian and show its 3DmFV (here the grid is  basically 1x1x1):</p>
<p style="text-align: center;">{% responsiveImage "../../assets/images/blog/fv_3d000.png", "" %}
</p>
<p>Now let’s see what happens when we move the point (hint 3DmFV changes)</p>
<p style="text-align: center;">{% responsiveImage "../../assets/images/blog/fv_3d0.500.png", "" %}
</p>
<p>Next, we can see what happens when we move the point all around (the .gif file might take a few seconds to load).</p>
<p style="text-align: center;"><img alt="" class="alignnone size-full wp-image-801" height="329" loading="lazy" src="../../assets/images/blog/3d_fv_smaller-compressor.gif" width="350"/></p>
<p>Finally, let’s see how the 3DmFV looks like when we take multiple points on a GMM of 2x2x2:</p>
<p style="text-align: center;">{% responsiveImage "../../assets/images/blog/fv_3d_model.png", "" %}
</p>
<h2>Reconstruction from 3DmFV</h2>
<p>Some may argue that 3DmFV is simply another handcrafted feature. However, we argue that it is simply another form to represent the data and therefore, the process is reversible. It is possible to show analytically that for simple cases it is reversible (single point, single Gaussian, points on a plane in a Gaussian). It gets a bit more complex in the general case when more points and more Gaussians are present. Therefore, we trained a simple 3DmFV decoder that is able to take a 3DmFV representation as input and produce a 3D point cloud as output.</p>
<p>Here is an image of a reconstructed point cloud of an airplane:</p>
<p>{% responsiveImage "../../assets/images/blog/decoder_original_vs_reconstruction-01.png", "" %}
</p>
<h2>The Code</h2>
<p>In order to recreate the images above you can use my repository for this <a href="https://github.com/sitzikbs/3DmFV-Tutorial" rel="noopener" target="_blank">3DmFV tutorial on my GitHub</a>.</p>
<p>For 3D point cloud classification using the 3DmFV representation use the <a href="https://github.com/sitzikbs/3DmFV-Net" rel="noopener" target="_blank">3DmFV-Net repository</a> which uses TensorFow to perform the computation on the GPU.</p>
 

</div>