---
layout: layouts/blog-post.njk
title: "3D Point Cloud Classification using Deep Learning – Recent Works"
date: 2021-03-10
author: Itzik Ben-Shabat
permalink: "/blog/posts/2021-03-10-3d-point-cloud-classification-using-deep-learning.html"
---

<div class="post-content">
{% raw %}




<p>Last week I gave a talk in the Omek-3D forum. The title of the talk was (the same as the title of this post) “<strong>3D Point Cloud Classification using Deep Learning</strong>“.</p>
<p>Here is a short summary ( that came out a little longer than expected) about what I presented there.</p>
<p><strong>UPDATE 1</strong> (February 2018): We recently uploaded to arXiv a new paper on <a href="https://arxiv.org/abs/1711.08241" rel="noopener" target="_blank">3D point cloud classification</a>. Check it out, we introduced a new representation which enables using CNNs. Our code will be available after publication. I am also working on additional posts on this subject.</p>
<p><strong>UPDATE 2</strong> (April 2018): I am starting to actively search for a post-doc position (to start summer 2019). If you know a professor that might be looking for someone that knows his way around deep learning applied to point clouds (preferably with a robotics / CAD/engineering orientation), please<a href="https://www.itzikbs.com/contact"> contact me</a>.</p>
<p><strong>UPDATE 3</strong> (April 2018): A fellow scholar recently referred me to a few papers I wasn’t familiar with which are a great contribution to this post. They are added below.</p>
<h5>Introduction</h5>
<p>Deep learning on 2D images has been vastly researched in the past few years. It achieves excellent results on classification tasks thanks to two main things</p>
<ol>
<li>Convolutional neural networks.</li>
<li>Data – tons of image data is available.</li>
</ol>
<p>For 3D, data is now growing rapidly. Whether it originated from a  human designed CAD model or a scanned point cloud from a LiDAR sensor or an RGBD camera – point clouds are everywhere.  In addition, most systems acquire 3D directly (rather than take images and process them).</p>
<p>Therefore, one of the expected next steps in research is how can we apply these amazing deep learning tools, that work so well for images, on 3D point clouds?</p>
<h5>Challenges</h5>
<p>It turns out that it is not that simple. I subdivide the challenges into two main categories:  the ‘new’ challenges related to the learning process and ‘old’ challenges related to data corruptions.</p>
<p>Neural Network Challenges:</p>
<ol>
<li>Unstructured data (no grid): point clouds are XYZ points distributed in space. There is no structured grid to help us for the CNN filters.</li>
<li>Invariance to permutations: a point cloud is essentially a long list of points (nx3 matrix where n is the number of points). Geometrically, the order of the points doesn’t matter however in the underlying matrix structure it does, e.g. the same point cloud can be represented by two very different matrices. (the image below illustrates this point).</li>
<li>The number of points changes:  In images, the number of pixels is a given constant and depends on the camera. The number of points, however, may vary dramatically, depending on the sensor.</li>
</ol>
<figure aria-describedby="caption-attachment-546" class="wp-caption aligncenter" id="attachment_546" style="width: 279px">{% endraw %}
{% responsiveImage "../../assets/images/blog/PCchallanges_web.png", "" %}
{% raw %}


<figcaption class="wp-caption-text" id="caption-attachment-546">Permutation Invariance problem</figcaption></figure>
<p>Data Challenges:</p>
<ol>
<li>Missing data: The scanned models are usually occluded and parts of the data are missing.</li>
<li>Noise: All sensors are noisy. There are a few types of noise which include point perturbations and outliers. It means that a point has some probability to be within a sphere of a certain radius around the place it was sampled (perturbations) or it may appear in a random position in space (outliers).</li>
<li>Rotation: a car turning left and the same car turning right will have different point clouds that represent the same car, right?</li>
</ol>
<p>The straightforward approach to applying deep learning on point clouds is to convert the data into a volumetric representation. e.g a voxel grid. This way we can train a CNN with 3D filters without the NN  issues ( the grid provides structure, the conversion to the grid solves the permutation problem and the number of voxels is constant). However, there are some downsides to this. Volumetric data can become very big, very fast. Lets think of a typical image size of 256×256 = 65536 pixels, now lets add a dimension 256x256x256 =16777216 voxels. This is a lot of data (even though GPU memory is growing every day). This also means very slow processing time. Therefore, usually, we need to compromise and take a lower resolution ( some methods use 64x64x64)  but it comes at the cost of quantization errors.</p>
<p>Sooooooooooo, the desired solution is a deep learning method that will work <strong>directly</strong> on the points.</p>
<h5>The Dataset</h5>
<p>Like every vision task, if you want to prove that your method works you have to use a benchmark.</p>
<p>I focused on Princeton’s Modelnet40 dataset. It contains approximately 12311 CAD models of 40 object categories (such as airplanes, tables, plants etc.) represented as triangle meshes. The data is split into 9843 models for training and 2468 for testing. I did some visualization of the dataset using the <a href="https://github.com/charlesq34/pointnet" rel="noopener" target="_blank">GitHub code for PointNet </a>(thanks <a href="https://web.stanford.edu/~rqi/" rel="noopener" target="_blank">Charles</a>!).</p>
<figure aria-describedby="caption-attachment-562" class="wp-caption aligncenter" id="attachment_562" style="width: 560px">{% endraw %}
{% responsiveImage "../../assets/images/blog/2017-09-modelnet40_classes.png", "" %}
{% raw %}


<figcaption class="wp-caption-text" id="caption-attachment-562">Modelnet40 objects</figcaption></figure>
<h5>Related Work</h5>
<p>In the talk, I surveyed three recent papers that did just that (apply deep learning on point clouds). But before I get into that I wanted to show a nice bar-plot that summarizes the latest accuracy results on the dataset. It shows the type of data each method is working on. You can see that in 2015 most methods worked on multi-view data (which is a short way of saying – let’s take a few pictures of the 3D model and process them using 2D methods), in 2016 more methods used volumetric representation with the pioneer of point cloud learnings and 2017 has a large increase in point-based methods.</p>
<figure aria-describedby="caption-attachment-551" class="wp-caption aligncenter" id="attachment_551" style="width: 734px">{% endraw %}
{% responsiveImage "../../assets/images/blog/method_barchart_4web.png", "" %}
{% raw %}


<figcaption class="wp-caption-text" id="caption-attachment-551">3D classification accuracy publications (accuracy, years and data type)</figcaption></figure>
<p>*All images below were taken from the original papers linked in the title ( credit to the authors )</p>
<p><a href="https://arxiv.org/abs/1612.00593" rel="noopener" target="_blank"><strong>Pointnet (CVPR2017)</strong></a></p>
<p><del>The pioneers! (from Stanford, no surprise there) They were the first to take on this challenge (The deletion is because a similar paper was published at around the same time. I don’t want to step on anyone’s toes).</del> The paper was posted on arXiv in 2016 and immediately got a lot of attention.  They did something surprisingly simple and proved why it works well they trained an MLP on each point separately (with shared weights across points). Each point was ‘projected’ to a 1024 dimension space. Then, they solved the order problem using a symmetric function (max-pool) over the points. This yielded a 1 x 1024 global feature for every point cloud which they fed into a nonlinear classifier.  They also solved the rotation problem using a ‘mini-network’ they called T-net.  It learns a transformation matrix over the points (3 x 3) and over mid-level features (64 x 64). Calling it ‘mini’ is a bit misleading since it is actually about the size of the main network. In addition, because of the large increase in the number of parameters they introduced a loss term to constraint the  64 x 64 matrix to be close to orthogonal.</p>
<p>They also used a similar network for part segmentation.</p>
<p>Oh, and they also did scene semantic segmentation.</p>
<p>Oh, and they also did normal vector estimation.</p>
<p>Great work! I highly recommend the read (or you can watch the presentation <a href="https://www.youtube.com/watch?v=Cge-hot0Oc0" rel="noopener" target="_blank">video </a>too).</p>
<p>This paper had a great 89.2% accuracy on the ModelNet40 dataset.</p>
<figure aria-describedby="caption-attachment-570" class="wp-caption alignnone" id="attachment_570" style="width: 600px">{% endraw %}
{% responsiveImage "../../assets/images/blog/pointnet_classification_architecture.png", "" %}
{% raw %}


<figcaption class="wp-caption-text" id="caption-attachment-570">PointNet classification architecture</figcaption></figure>
<p> </p>
<p>Cite: Charles R. Qi, Hao Su, Kaichun Mo, and Leonidas J. Guibas. Pointnet: Deep learning on point sets for 3d classication and segmentation. In The IEEE Conference on Computer Vision and Pattern Recognition (CVPR), July 2017.</p>
<p>The code is available on GitHub: <a href="https://github.com/charlesq34/pointnet" rel="noopener" target="_blank">PointNet code </a></p>
<p><strong>Deep sets (<a href="https://papers.nips.cc/paper/6931-deep-sets.pdf" rel="noopener" target="_blank">NIPS2017 </a>/ <a href="https://arxiv.org/pdf/1611.04500.pdf" rel="noopener" target="_blank">ICLR2017</a>)</strong></p>
<p>These guys from CMU posted <a href="https://arxiv.org/pdf/1611.04500.pdf" rel="noopener" target="_blank">this work</a> a few weeks before PointNet. The general idea is quite similar (not taking sides on who was first 🙂 ). While PointNet focus is mainly on the architecture, Deep sets focus is primarily to produce a layer similar to convolution for sets – the “permutation equivariance”  (PE) layer which has linear time complexity in the size of the set. They claim that the PE layer is the most expressive form of parameter sharing for its purpose. Experiments show better results for point-cloud classification (90%).</p>
<p>They also predicted the sum of MNIST digits.</p>
<p>They also did a set anomaly detection.</p>
<p>Very interesting work, I highly recommend it for machine/deep learning-oriented readers.</p>
<p>Cite: Ravanbakhsh, Siamak, Jeff Schneider, and Barnabas Poczos. “Deep learning with sets and point clouds.” <i>arXiv preprint arXiv:1611.04500</i> (2016).</p>
<p>Zaheer, M., Kottur, S., Ravanbakhsh, S., Poczos, B., Salakhutdinov, R. R., &amp; Smola, A. J. (2017). Deep sets. In <i>Advances in Neural Information Processing Systems</i> (pp. 3394-3404).</p>
<p>The code is available on GitHub: <a href="https://github.com/manzilzaheer/DeepSets" rel="noopener" target="_blank">Deep sets code</a></p>
<p><a href="https://arxiv.org/abs/1706.02413" rel="noopener" target="_blank"><strong>Pointnet++  (NIPS 2017)</strong></a></p>
<p>When I first read the PointNet paper, there was one thing that bothered me the most – why are they not using local neighborhoods of points?  So, I guess it bothered them too because not long after PointNet, they introduced  Pointnet++. It is essentially a hierarchical version of PointNet. Each layer has three sub stages: sampling, grouping, and PointNeting. In the first stage, they select centroids and in the second stage, they take their surrounding neighboring points (within a given radius) to create multiple sub-point clouds. Then they feed them to a PointNet and get a higher dimensional representation of these sub-point clouds. Then, they repeat the process (sample centroids, find their neighbors and Pointnet on their higher order representation to get an even higher one). They reported using 3 of these layers. They also tested some different aggregation methods for the different hierarchy levels in order to overcome differences in sampling density (which is known to be a big issue for most sensors = sample densely when objects are near and sparsely when they are far away).</p>
<p>They got an improvement on the original PointNet with a 90.7% accuracy on ModelNet40. (It got even better scores when they incorporated additional features).</p>
<figure aria-describedby="caption-attachment-568" class="wp-caption aligncenter" id="attachment_568" style="width: 600px">{% endraw %}
{% responsiveImage "../../assets/images/blog/pointnet.jpg", "" %}
{% raw %}


<figcaption class="wp-caption-text" id="caption-attachment-568">Pointnet++ architecture</figcaption></figure>
<p> </p>
<p>Cite: Charles R Qi, Li Yi, Hao Su, and Leonidas J Guibas. Pointnet++: Deep hierarchical feature learning on point sets in a metric space. arXiv preprint arXiv:1706.02413, 2017.</p>
<p> </p>
<p><a href="https://arxiv.org/abs/1704.01222" rel="noopener" target="_blank"><strong>Kd-Network (ICCV 2017)</strong></a></p>
<p>This paper uses the well-known <a href="https://en.wikipedia.org/wiki/K-d_tree" rel="noopener" target="_blank">Kd-tree</a> to create some order in the point cloud. Once the point cloud is structured they learned weights for each node in the tree (which represents a subdivision along a specific axis). The weights are shared for each axis across a single tree level (so all the greens in the image below have shared weights because they subdivided the data along the x dimension ). They tested random and deterministic subdivisions of space and reported that the random version works best. They report some drawbacks. It is sensitive to rotations (since it changes the tree structure) and to noise (if it changes the tree structure).  I found another drawback – for every number of input points you either need to upsample, downsample or train a new model.</p>
<p>They report a 90.6% accuracy dataset for 1024 points (depth 10 tree) and 91.8% for ~32K points (depth 15 tree) on the Modelnet40 .</p>
<p>Despite its drawbacks, I find the approach very interesting. It also seems that there is some additional work to be done (like try other tree types as they suggested).</p>
<p>Oh, and they also did part segmentation.</p>
<p>Oh, and they also did shape retrieval.</p>
<figure aria-describedby="caption-attachment-575" class="wp-caption aligncenter" id="attachment_575" style="width: 300px">{% endraw %}
{% responsiveImage "../../assets/images/blog/kdnetwork.png", "" %}
{% raw %}


<figcaption class="wp-caption-text" id="caption-attachment-575">Kd-Network subdivisions and color coded shared weights</figcaption></figure>
<p> </p>
<p>Cite: Roman Klokov and Victor Lempitsky. Escape from cells: Deep kd-networks for the recognition of 3d point cloud models. arXiv preprint arXiv:1704.01222, 2017.</p>
<h6>Summary</h6>
<p>In the vision community, scores are really important so let’s line them up</p>
<p>{% endraw %}
{% responsiveImage "../../assets/images/blog/final_scores.png", "" %}
{% raw %}


</p>
<p>Since the scores are so close to each other and could be affected by a lot of parameters I find great interest in the different approaches. Pointnet and Pointnet++ used a symmetric function to solve the order problem while kd-Network used the Kd-tree. The Kd-tree also solved the structure problem while in the PointNets the MLP was trained on each point separately.</p>
<p>I have a method of my own to solve the point cloud classification task cooking up. I’ll post it after it’s published and link to it. (Here is the <a href="https://arxiv.org/abs/1711.08241" rel="noopener" target="_blank">link </a>again if you missed the update at the top)</p>
<p>I just hope no one will publish it before me 🙂</p>
 

{% endraw %}
</div>