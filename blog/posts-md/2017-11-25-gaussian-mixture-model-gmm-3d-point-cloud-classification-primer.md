---
layout: layouts/blog-post.njk
title: "What is a Gaussian Mixture Model (GMM) – 3D Point Cloud Classification Primer"
date: "2017-11-25"
author: Itzik Ben-Shabat
permalink: "/blog/posts/2021-03-10-gaussian-mixture-model-gmm-3d-point-cloud-classification-primer.html"
---

<div class="post-content">


<p>Recently we finished a paper about 3d point cloud classification and segmentation using our proposed 3D modified Fisher Vector (3DmFV) representation and convolutional neural networks (CNNs).  It is currently <a href="https://arxiv.org/abs/1711.08241" rel="noopener" target="_blank">available on ArXiv</a>.  I believe in making research accessible to everyone and I realized that this paper requires some level of familiarity with two main topics:</p>
<ol>
<li>Gaussian Mixture Models (GMM)</li>
<li>Fisher Vectors</li>
</ol>
<p>This post is the first in a series of three and aims to be a GMM primer for using 3DmFV for 3D point cloud classification.</p>
<p>So, what is a GMM (sometimes referred to as Mixture of Gaussians)?</p>
<p>The shortest answer is a probability distribution composed of several Gaussians.</p>
<p>I will start with some mathematical definitions but will also give a more intuitive example at the bottom.</p>
<h2>The Math</h2>
<p>The Gaussian (also known as a multivariate normal distribution) of a random D dimensional point <img alt="p" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=p&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"> can be specified using <img alt="\mu" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=%5Cmu&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/> and <img alt="\Sigma" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=%5CSigma&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/> , which are its expected value (mean), and covariance matrix  respectively.  Therefore the likelihood of a single point <img alt="p" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=p&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/> with respects to the k<sup>th </sup>Gaussian is given by</img></p>
<p style="text-align: center;"><img alt="u_k(p) = \frac{1}{(2\pi)^{D/2}|\Sigma_k|^{1/2}}\exp\left\{-\frac{1}{2}(p-\mu_k)'\Sigma_k^{-1}(p-\mu_k)\right\}" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=u_k%28p%29+%3D%26nbsp%3B%5Cfrac%7B1%7D%7B%282%5Cpi%29%5E%7BD%2F2%7D%7C%5CSigma_k%7C%5E%7B1%2F2%7D%7D%5Cexp%5Cleft%5C%7B-%5Cfrac%7B1%7D%7B2%7D%28p-%5Cmu_k%29%27%5CSigma_k%5E%7B-1%7D%28p-%5Cmu_k%29%5Cright%5C%7D&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/>,</p>
<p>and the likelihood of <img alt="p" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=p&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/> associated with the GMM</p>
<p style="text-align: center;"><img alt="u_\lambda(p) = \sum_{k=1}^{K}w_ku_k(p)" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=u_%5Clambda%28p%29+%3D+%5Csum_%7Bk%3D1%7D%5E%7BK%7Dw_ku_k%28p%29&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/></p>
<p>Here,  <img alt="w_k" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=w_k&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/> are the mixture weights ( informally representing the number of points/ the amount of influence of each Gaussian).</p>
<p> </p>
<p>Let’s say that you have some D dimensional data points (I will focus on 2D and 3D data because it is easy to visualize but it works for much higher dimensions).  In addition, let us assume that each one of these data points came from one of K different sources. Each source is a Gaussian in a D dimensional space.  The challenge is to find the Gaussians parameters that will maximize their expectation. This is usually done using the <a href="https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm" rel="noopener" target="_blank">Expectation Maximization (EM) algorithm</a>.</p>
<p>Basically what we want to do is find  <img alt="\lambda=(w_k,\mu_k,\Sigma_k)" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=%5Clambda%3D%28w_k%2C%5Cmu_k%2C%5CSigma_k%29&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/> for the Gaussians that best fits the data.</p>
<h2>The Intuition</h2>
<p>We can imagine a more intuitive (and adventurous) problem:</p>
<p>Once upon a time, there was a rich man with a lot of gold in his pockets. He also had a hole in one of them and whenever he walked around his garden some coins fell to the ground. What you want to do is draw a treasure map for adventurers and let them know where are they most likely to find gold.</p>
<p>In the image below you can see the coins that fell out as points ( each coin has a different color corresponding to the Gaussian that was used to generate it) and a treasure map overlay that shows four different areas to finding gold (the lines transparency indicates the probability – close to the center of each Gaussian the probability is higher to find gold and as you go farther away it reduces.</p>
<p>{% responsiveImage "assets/images/blog/2D_GMM_demonstration.png", "2D Gaussian Mixrure Model example" %}
</p>
<p>We can do something very similar for 3D points (abandoning the rich man example). In the image below you can see the generated 3D points and a semi-transparent surface representing the Gaussian location and scale ( 3 standard deviations in each axis).</p>
<p>{% responsiveImage "assets/images/blog/3D_GMM_demonstration.png", "3D GMM example" %}
</p>
<p> </p>
<p>You can see how we can basically represent all of these 4000 points using only 4 Gaussians.  Each points gets a likelihood value (<img alt="u_k" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=u_k&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002">) for each Gaussian.  In our paper, we show that we can use a GMM with Gaussians on a grid (and not using EM algorithm) to represent 3D point clouds for the classification and part segmentation task. But, more on that in a later post.</img></p>
<p> </p>
<h2>The Code</h2>
<p>The code used for generating the images above is available on <a href="https://github.com/sitzikbs/gmm_tutorial" rel="noopener" target="_blank">github</a>.</p>
<p>It is composed of three main parts</p>
<ul>
<li>Generating data</li>
<li>Fitting the Gaussian Mixture Model</li>
<li>Visualization</li>
</ul>
<p><strong>Generating data</strong></p>
<p>First, we specify the number of points to generate in each Gaussian,  the problems dimensionality (2/3), and the parameters for the Gaussians that we will use to generate the data.</p>
<pre>## Generate synthetic data
N,D = 1000, 2 # number of points and dimenstinality

if D == 2:
    #set gaussian ceters and covariances in 2D
    means = np.array([[0.5, 0.0],
                      [0, 0],
                      [-0.5, -0.5],
                      [-0.8, 0.3]])
    covs = np.array([np.diag([0.01, 0.01]),
                     np.diag([0.025, 0.01]),
                     np.diag([0.01, 0.025]),
                     np.diag([0.01, 0.01])])
elif D == 3:
    # set gaussian ceters and covariances in 3D
    means = np.array([[0.5, 0.0, 0.0],
                      [0.0, 0.0, 0.0],
                      [-0.5, -0.5, -0.5],
                      [-0.8, 0.3, 0.4]])
    covs = np.array([np.diag([0.01, 0.01, 0.03]),
                     np.diag([0.08, 0.01, 0.01]),
                     np.diag([0.01, 0.05, 0.01]),
                     np.diag([0.03, 0.07, 0.01])])
n_gaussians = means.shape[0]</pre>
<p>Next, we generate points using a multivariate normal distribution for</p>
<pre>points = []
for i in range(len(means)):
    x = np.random.multivariate_normal(means[i], covs[i], N )
    points.append(x)
points = np.concatenate(points)</pre>
<p><strong>Fitting the Gaussian Mixture Model</strong></p>
<p>Using the EM algorithm (provided in <a href="http://scikit-learn.org/stable/modules/mixture.html" rel="noopener" target="_blank">scikit-learn</a>) we were able to find all of the Gaussians parameters</p>
<pre>#fit the gaussian model
gmm = GaussianMixture(n_components=n_gaussians, covariance_type='diag')
gmm.fit(points)</pre>
<p><strong>Visualization</strong></p>
<p>Finally, we visualize the data using some custom functions (see the <a href="https://github.com/sitzikbs/gmm_tutorial/blob/master/visualization.py" rel="noopener" target="_blank">git repository for the functions</a>)</p>
<pre>#visualize
if D == 2:
    visualization.visualize_2D_gmm(points, gmm.weights_, gmm.means_.T, np.sqrt(gmm.covariances_).T)
elif D == 3:
    visualization.visualize_3d_gmm(points, gmm.weights_, gmm.means_.T, np.sqrt(gmm.covariances_).T)</pre>
<p>This concludes my very brief primer on GMMs.</p>
<p>Additional resources:</p>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Normal_distribution" rel="noopener" target="_blank">Normal distribution on Wikipedia.</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multivariate_normal_distribution" rel="noopener" target="_blank">Multivariate normal distribution on Wikipedia</a>.</li>
<li><a href="https://www.youtube.com/watch?v=9YA2t78Ha68" rel="noopener" target="_blank">Expectation maximization by Victor Lavrenko on Youtube.</a></li>
</ul>
<p> </p>
<p> </p>
<p> </p>
 

</div>