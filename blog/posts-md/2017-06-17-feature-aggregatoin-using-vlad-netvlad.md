---
layout: layouts/blog-post.njk
title: "Feature aggregation using VLAD and netVLAD"
date: 2017-06-17
author: Itzik Ben-Shabat
permalink: "/blog/posts/2017-06-17-feature-aggregatoin-using-vlad-netvlad.html"
---

<div class="post-content">
{% raw %}




<p>Before the age of deep learning, hand-crafted features such as SIFT ruled the computer vision world. These features combined with Bag of Features (BOF) methods were very popular in indexing and categorization tasks. Their main advantage was getting a very discriminative higher dimensional representation of the image. The best one was the <a href="http://image.ntua.gr/iva/files/PerronninDance_CVPR2007%20-%20Fisher%20Kernels%20on%20Visual%20Vocabularies%20for%20Image%20categorization.pdf" rel="noopener" target="_blank">Fisher Vectors</a> (FV) kernel which uses a Gaussian Mixture Model (GMM) and their derivatives to approximate the feature distribution in the image. They had excellent performance in various tasks but their main drawback was a very (sometimes too) high dimensionality.</p>
<p>Inspired by BOF and FV  arose <a href="https://hal.inria.fr/file/index/docid/548637/filename/jegou_compactimagerepresentation.pdf" rel="noopener" target="_blank">VLAD </a>– Vector of Locally Aggregated Descriptors.  VLAD had performance similar to FV while having a much lower dimensionality.</p>
<p>The main idea behind VLAD is:</p>
<ul>
<li>Compute k centers of features (using kmeans).</li>
<li>Assign features to their closest center.</li>
<li>Sum over the residual between the features and their corresponding center.</li>
<li>Flatten the matrix into a vector and normalize (L2)</li>
</ul>
<p>Mathematically, it looks like this:</p>
<p style="text-align: center;"><img alt="{{v}_{ij}}=\sum\limits_{x\,such\,that\,NN(x)={{c}_{i}}}{\left( {{x}_{i}}-{{c}_{ij}} \right)}" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=%7B%7Bv%7D_%7Bij%7D%7D%3D%5Csum%5Climits_%7Bx%5C%2Csuch%5C%2Cthat%5C%2CNN%28x%29%3D%7B%7Bc%7D_%7Bi%7D%7D%7D%7B%5Cleft%28+%7B%7Bx%7D_%7Bi%7D%7D-%7B%7Bc%7D_%7Bij%7D%7D+%5Cright%29%7D&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/></p>
<p>Here, <img alt="v_{ij}" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=v_%7Bij%7D&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/> is the VLAD representation, <img alt="x" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=x&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/> is the input and <img alt="c" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=c&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/> are the centers.</p>
<p> </p>
<p>In the age of deep learning, the question arises – can we learn this representation?</p>
<p>The short answer is – YES.</p>
<p>I found the <a href="http://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Arandjelovic_NetVLAD_CNN_Architecture_CVPR_2016_paper.pdf" rel="noopener" target="_blank">netVLAD </a>paper (the<a href="https://github.com/Relja/netvlad" rel="noopener" target="_blank"> original code</a> is available on Github and uses MATLAB and MatConvNet). The general idea is the same as the original VLAD with two main difference:</p>
<ol>
<li>netVLAD uses a learned softmax for the assignment (because it is differentiable).</li>
<li>netVLAD performs intra-normalization (presented the paper<a href="http://www.cv-foundation.org/openaccess/content_cvpr_2013/papers/Arandjelovic_All_About_VLAD_2013_CVPR_paper.pdf" rel="noopener" target="_blank"> All about VLAD</a>) before the normalization over the entire VLAD vector.</li>
</ol>
<p style="text-align: center;"><img alt="{{v}_{ij}}=\sum\limits_{i=1}^{N}{\frac{{{e}^{w_{k}^{T}{{x}_{i}}+{{b}_{k}}}}}{\sum\limits_{k'}{{{e}^{w_{k}^{T}{{x}_{i}}+{{b}_{k}}}}}}}\left( {{x}_{ij}}-{{c}_{kj}} \right)" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=%7B%7Bv%7D_%7Bij%7D%7D%3D%5Csum%5Climits_%7Bi%3D1%7D%5E%7BN%7D%7B%5Cfrac%7B%7B%7Be%7D%5E%7Bw_%7Bk%7D%5E%7BT%7D%7B%7Bx%7D_%7Bi%7D%7D%2B%7B%7Bb%7D_%7Bk%7D%7D%7D%7D%7D%7B%5Csum%5Climits_%7Bk%27%7D%7B%7B%7Be%7D%5E%7Bw_%7Bk%7D%5E%7BT%7D%7B%7Bx%7D_%7Bi%7D%7D%2B%7B%7Bb%7D_%7Bk%7D%7D%7D%7D%7D%7D%7D%5Cleft%28+%7B%7Bx%7D_%7Bij%7D%7D-%7B%7Bc%7D_%7Bkj%7D%7D+%5Cright%29&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/></p>
<p>Here, <img alt="w_k" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=w_k&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/>, <img alt="b_k" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=b_k&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/>, <img alt="c_k" class="latex" decoding="async" src="https://s0.wp.com/latex.php?latex=c_k&amp;bg=ffffff&amp;fg=000&amp;s=0&amp;c=20201002"/> are parameters learned by the network.</p>
<p>The netVLAD architecture is presented below</p>
<p> </p>
<figure aria-describedby="caption-attachment-451" class="wp-caption aligncenter" id="attachment_451" style="width: 1024px">{% endraw %}
{% responsiveImage "../../assets/images/blog/netVLAD_Architecture.png", "" %}
{% raw %}


<figcaption class="wp-caption-text" id="caption-attachment-451"><span style="color: #999999;"><em><span style="color: #999999;">netVLAD architecture as presented in the original <a href="http://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Arandjelovic_NetVLAD_CNN_Architecture_CVPR_2016_paper.pdf" rel="noopener" target="_blank">netVALD </a>paper </span></em><em>by R. Arandjelovic et al.</em></span></figcaption></figure>
<p> </p>
<p>In the original paper, they stated that the centers and weights should be initialized to some pre-trained value (using kmeans on features learned without the VLAD layer). However, I experienced no change in performance while just using the standard truncated normal distribution initialization or Xavier.</p>
<p> </p>
<p>And now for my contribution to the community (and the world) – I implemented the VLAD orderless pooling layer in Tensorflow 1.0.  The code is available on my <a href="https://github.com/sitzikbs/netVLAD" rel="noopener" target="_blank">Github</a>.</p>
<p> </p>
 

{% endraw %}
</div>