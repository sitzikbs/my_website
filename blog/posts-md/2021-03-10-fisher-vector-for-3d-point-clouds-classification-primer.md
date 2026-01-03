---
layout: layouts/blog-post.njk
title: "What is a Fisher Vector for 3D point clouds – 3D Point Cloud Classification Primer"
date: 2021-03-10
author: Itzik Ben-Shabat
permalink: "/blog/posts/2021-03-10-fisher-vector-for-3d-point-clouds-classification-primer.html"
---

<div class="post-content">


<p>Recently we published a paper about 3d point cloud classification (and segmentation) using our proposed 3D modified Fisher Vector (3DmFV) representation and convolutional neural networks (CNNs).  The preprint is <a href="https://arxiv.org/abs/1711.08241" rel="noopener noreferrer" target="_blank">available on ArXiv</a> and the final version is available in <a href="https://ieeexplore.ieee.org/abstract/document/8394990/" rel="noopener noreferrer" target="_blank">Robotics and Automation Letters (RA-L)</a> journal.</p>
<p>I believe in making research accessible to everyone and I realized that this paper requires some level of familiarity with two main topics:</p>
<ol class="wp-block-list"><li><a href="https://www.itzikbs.com/gaussian-mixture-model-gmm-3d-point-cloud-classification-primer" rel="noopener noreferrer" target="_blank">Gaussian Mixture Models (GMM). </a></li><li>Fisher Vectors</li></ol>
<p>This post is the second in a series of three and aims to be a Fisher Vector (FV) primer for using 3DmFV for 3D point cloud classification. The first is about GMMS, if you are unfamiliar with it you should start <a href="https://www.itzikbs.com/gaussian-mixture-model-gmm-3d-point-cloud-classification-primer">there</a>.</p>
<p>So, what is a Fisher Vector?</p>
<p>The shortest answer is a feature aggregation method.  For an in-depth answer make sure to read Perronnin’s papers – I personally like <a href="https://link.springer.com/article/10.1007/s11263-013-0636-x" rel="noopener noreferrer" target="_blank">this one</a>.  Intuitively, FV describes points by their deviation from a GMM.</p>
<p>I will start with some mathematical definitions but will also give a more intuitive example at the bottom.</p>
<h2 class="wp-block-heading">The Math</h2>
<p>Remember that the likelihood of every point <img alt="p" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=p&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"> associated with the GMM is given by</img></p>
<img alt="u_\lambda(p) = \sum_{k=1}^{K}w_ku_k(p)" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=u_%5Clambda%28p%29+%3D+%5Csum_%7Bk%3D1%7D%5E%7BK%7Dw_ku_k%28p%29&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/>
<p>The Fisher Vector may be written as the sum of normalized gradient statistics for each point</p>
<img alt="FV_\lambda^X = \sum_{t=1}^TL_\lambda\nabla_\lambda\log u_\lambda(p_t)" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=FV_%5Clambda%5EX+%3D+%5Csum_%7Bt%3D1%7D%5ETL_%5Clambda%5Cnabla_%5Clambda%5Clog+u_%5Clambda%28p_t%29&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/>
<p>Here, <img alt="\lambda" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=%5Clambda&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/> is the set of parameters of a <img alt="K" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=K&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/> component GMM:  <img alt="\lambda=\{(w_k,\mu_k,\Sigma_k), k=1,...K\}" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=%5Clambda%3D%5C%7B%28w_k%2C%5Cmu_k%2C%5CSigma_k%29%2C+k%3D1%2C...K%5C%7D&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/>, where <img alt="w_k,\mu_k,\Sigma_k" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=w_k%2C%5Cmu_k%2C%5CSigma_k&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/> are the mixture weight, expected value, and covariance matrix of the <img alt="k^{th} " class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=k%5E%7Bth%7D+&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/> Gaussian.</p>
<p>We perform a change of variables from <img alt="\{w_k\}" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=%5C%7Bw_k%5C%7D&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/> to <img alt="\{\alpha_k\}" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=%5C%7B%5Calpha_k%5C%7D&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/>, ensures that <img alt="u_\lambda(x)" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=u_%5Clambda%28x%29&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/> is a valid distribution and simplifies the gradient calculation:</p>
<img alt="w_k = \frac{exp(\alpha_k)}{\sum_{j=1}^{K}exp(\alpha_j)} " class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=w_k+%3D+%5Cfrac%7Bexp%28%5Calpha_k%29%7D%7B%5Csum_%7Bj%3D1%7D%5E%7BK%7Dexp%28%5Calpha_j%29%7D+&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/>
<p>The soft assignment of a point to a gaussian is given by</p>
<img alt="\gamma_t(k) = \frac{w_k u_k(p_t)}{\sum_{j=1}^{K} w_j u_j(p_t)}" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=%5Cgamma_t%28k%29+%3D+%5Cfrac%7Bw_k+u_k%28p_t%29%7D%7B%5Csum_%7Bj%3D1%7D%5E%7BK%7D+w_j+u_j%28p_t%29%7D&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/>
<p>The normalized gradients are:</p>
<img alt="FV_{\alpha_k}^X = \frac{1}{\sqrt{w_k}} \sum_{t=1}^T(\gamma_t(k)-w_k)" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=FV_%7B%5Calpha_k%7D%5EX+%3D+%5Cfrac%7B1%7D%7B%5Csqrt%7Bw_k%7D%7D+%5Csum_%7Bt%3D1%7D%5ET%28%5Cgamma_t%28k%29-w_k%29&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/>
<img alt="FV_{\mu_k}^X = \frac{1}{\sqrt{w_k}} \sum_{t=1}^T \gamma_t(k) \left( \frac{p_t-\mu_k}{\sigma_k} \right)" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=FV_%7B%5Cmu_k%7D%5EX+%3D+%5Cfrac%7B1%7D%7B%5Csqrt%7Bw_k%7D%7D+%5Csum_%7Bt%3D1%7D%5ET+%5Cgamma_t%28k%29+%5Cleft%28+%5Cfrac%7Bp_t-%5Cmu_k%7D%7B%5Csigma_k%7D+%5Cright%29&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/>
<img alt="FV_{\sigma_k}^X = \frac{1}{\sqrt{2w_k}} \sum_{t=1}^T \gamma_t(k) \left[ \frac{(p_t-\mu_k)^2}{\sigma_k^2}-1 \right]" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=FV_%7B%5Csigma_k%7D%5EX+%3D+%5Cfrac%7B1%7D%7B%5Csqrt%7B2w_k%7D%7D+%5Csum_%7Bt%3D1%7D%5ET+%5Cgamma_t%28k%29+%5Cleft%5B+%5Cfrac%7B%28p_t-%5Cmu_k%29%5E2%7D%7B%5Csigma_k%5E2%7D-1+%5Cright%5D&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/>
<p>Finally, the Fisher vector is formed by concatenating all of these components and normalizing them by the number of points <img alt="T" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=T&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/>.</p>
<h2 class="wp-block-heading">The Intuition</h2>
<p>It is much easier to understand the FV for points with some nice visualizations.</p>
<p>Let’s take a single 2D point in a single Gaussian and show its FV next to it. In the image below, the Gaussian is qualitatively visualized with a dashed circle with a radius of a single standard deviation.</p>
<div class="wp-block-image"><figure class="aligncenter">{% responsiveImage "assets/images/blog/fv_0-300x225.png", "Point fisher vector example" %}
</figure></div>
<p>Now let’s see what happens when we move the point (hint FV changes)</p>
<div class="wp-block-image"><figure class="aligncenter">{% responsiveImage "assets/images/blog/fv_34-300x225.png", "Point fisher vector example" %}
</figure></div>
<p>Finally, we can see what happens when we move the point all around.</p>
<div class="wp-block-image"><figure class="aligncenter">{% responsiveImage "assets/images/blog/fv_smaller-compressor.gif", "Point fisher vector animation" %}</figure></div>
<h2 class="wp-block-heading">The Code</h2>
<p>A great implementation of fisher vectors is available in <a href="https://gist.github.cnsom/danoneata/9927923" rel="noopener noreferrer" target="_blank">this link </a></p>
<p>In order to recreate the images above you can use my repository for this <a href="https://github.com/sitzikbs/3DmFV-Tutorial" rel="noopener noreferrer" target="_blank">FV tutorial on my GitHub</a>.</p>
<p>Make sure to check out the next post in this series about our 3D modified Fisher Vectors (3DmFV) for point cloud classification.</p>
 

</div>