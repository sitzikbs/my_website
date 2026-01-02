---
layout: layouts/blog-post.njk
title: "Deep Learning on 3D Data – References"
date: 2017-05-24
author: Itzik Ben-Shabat
permalink: "/blog/posts/2017-05-24-deep-learning-3d-data-references.html"
---

<div class="post-content">


<p>Deep learning (DL) using convolution neural networks (CNN) architectures is now a standard for solving classification tasks in images. When dealing with 3D data the problem becomes more complex. First, 3D data may be represented using various structures which include:</p>
<ol>
<li>Voxel grid</li>
<li>Point clouds</li>
<li>Multi-view</li>
<li>Depth map</li>
</ol>
<p>For the case of Multi-view and depth maps, the problem is converted into using 2D CNNs on multiple images. A Voxel grid can use extensions of the 2D CNN into 3D by simply defining 3D convolution kernels. However, for the case of 3D point clouds, it is not clear how to apply DL tools.</p>
<p>Second, the available data for images is still much larger (although, recently there is an increase in 3D datasets – more on that in a later post).  However, for the 3D case, synthetic data may be generated easily.</p>
<p>Attached below are a list of papers which used DL tools on 3D data</p>
<ol>
<li>  Voxel Grid – Volumetric CNN:
<ul>
<li><a href="http://ieeexplore.ieee.org/abstract/document/7353481/">Voxnet: A 3D convolutional neural network for real-time object classification</a></li>
<li><a href="http://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Qi_Volumetric_and_Multi-View_CVPR_2016_paper.html">Volumetric and multi-view CNNs for object classification on 3d data </a>– compared volumetric CNNs to Multi-view CNNs for object classification. They showed that the multi-view approach performs better, however, the resolution of the volumetric model was limited</li>
<li><a href="http://www.cv-foundation.org/openaccess/content_cvpr_2015/html/Wu_3D_ShapeNets_A_2015_CVPR_paper.html">3D shapenetes: A deep representation for volumetric shapes</a></li>
</ul>
</li>
<li>  Multi-View CNNs:
<ul>
<li><a href="http://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Qi_Volumetric_and_Multi-View_CVPR_2016_paper.html">Volumetric and multi-view CNNs for object classification on 3d data</a></li>
<li><a href="http://www.cv-foundation.org/openaccess/content_iccv_2015/html/Su_Multi-View_Convolutional_Neural_ICCV_2015_paper.html">Multi-View Convolutional Neural Networks for 3D Shape Recognition</a></li>
</ul>
</li>
<li>Point clouds:
<ul>
<li> <a href="https://arxiv.org/abs/1612.00593">Pointnet: Deep learning on point sets for 3d classification and segmentation</a> – In this work they applied a convolution kernel on each point separately, creating a higher dimensional representation of each point and then max-pooling over the entire point set (max pooling used as a symmetric function) to get invariance to permutations of the input cloud (since there is no geometrical significance to the point order).</li>
</ul>
</li>
<li>Hand-crafted features + DNN :
<ul>
<li><a href="http://www.cv-foundation.org/openaccess/content_cvpr_2015/html/Fang_3D_Deep_Shape_2015_CVPR_paper.html" target="_blank">3D  deep shape descriptor</a> – fed heat kernel signatures (HKS) descriptor into an NN to get an Eigen-shape descriptor and a Fischer shape descriptor.</li>
</ul>
</li>
</ol>
<p> </p>
<p> </p>
 

</div>