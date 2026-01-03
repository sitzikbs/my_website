---
layout: layouts/blog-post.njk
title: "How to Visualize Normal Vectors on 3D Point Clouds"
date: 2019-04-11
author: Itzik Ben-Shabat
permalink: "/blog/posts/2019-04-11-how-to-visualize-normal-vectors-on-3d-point-clouds.html"
---

<div class="post-content">


<p>This post will show you a good way to visualize normal vectors on 3D point clouds. </p>
<p>At the beginning of my master’s degree, I was working on a project where I used normal vectors on 3D point clouds to perform 3D point cloud over-segmentation. </p>
<p>One of the first things I did was to try and visualize the normal vectors and the point clouds. As a mechanical engineer, my first go-to programming language for such tasks is MATLAB, so I was happy to see that it has a nice function for plotting vectors:</p>
<pre class="wp-block-code"><code>quiver3(x,y,z,u,v,w)</code></pre>
<p>Here <code>x,y,z</code> are the point coordinates and <code>u,v,w</code> are the vector components. </p>
<h4 class="wp-block-heading">The problem</h4>
<p>The problem was that for complex 3D point clouds (like from the NYU Depth V2 dataset) this visualization is not very informative (it is very hard to see where the little arrows are pointing). </p>
<div class="wp-block-image"><figure class="aligncenter is-resized">{% responsiveImage "assets/images/blog/nyu_v2_quiver.jpg", "3D point clouds with normal vectors  visualization as arrows" %}
<figcaption>Normal vector visualization using <code>quiver3</code> of a scene from NYU Depth V2  </figcaption></figure></div>
<h4 class="wp-block-heading">The solution</h4>
<p>Therefore, I created a nice function that maps a vector to the RGB cube: </p>
<pre class="wp-block-code"><code>[RGB] = Sphere2RGBCube(V)</code></pre>
<p> It is available for download on MATLAB file exchange, <a aria-label="here (opens in a new tab)" href="https://www.mathworks.com/matlabcentral/fileexchange/71178-normal-vector-to-rgb" rel="noreferrer noopener" target="_blank">here</a>. It also includes a short demo and an even more comprehensive demonstration of how the color mapping is performed. </p>
<p>For the comprehensive demonstration simply run </p>
<pre class="wp-block-code"><code>TestSphere2CubeMapping();</code></pre>
<p>And you will get the following interface :</p>
<div class="wp-block-image"><figure class="aligncenter is-resized">{% responsiveImage "assets/images/blog/2019-04-Point_loud_rgb_color_conversion.png", "" %}
<figcaption>Normal Vector color mapping comprehensive demonstration</figcaption></figure></div>
<p>In the top left, you can see the RGB cube. At the bottom left, you can see the unit sphere with the mapped colors. Both include a small red dot which you can move using the arrow keys. To the right, you can see the color and its corresponding RGB values of the red dot. This illustrates what the mapping function does – it takes a unit vector (a point on the sphere), finds where it intersects the RGB cube, and uses that color as the vector representation. </p>
<p>Note that there are actually two mapping functions:</p>
<pre class="wp-block-code"><code>[RGB] = Sphere2RGBCube(V)
[RGB] = Sphere2RGBCube_accurate(V)</code></pre>
<p>The main difference between the two is that the “accurate” version generates RGB colors on the cube planes. When plotting a sphere, for example, it is evident that the color mapping is not as smooth as one may want. Therefore, the “non-accurate” version creates a smoother color mapping (basically a sphere encapsulated within the RGB cube). </p>
<p>Finally, here is an example of the same point cloud as before, but this time with color mapping:  </p>
<div class="wp-block-image"><figure class="aligncenter is-resized">{% responsiveImage "assets/images/blog/nyu_v2_1.png", "3D point clouds with normal vectors color mapped visualization" %}
<figcaption>Normal vector visualization using RGB mapping of a scene from NYU Depth V2 <br/></figcaption></figure></div>
<p>This code was used in our recent paper on <a aria-label="normal estimation for 3D point clouds (opens in a new tab)" href="https://www.itzikbs.com/nesti-net-normal-estimation-for-3d-point-clouds" rel="noreferrer noopener" target="_blank">normal estimation for 3D point clouds</a>. If you find this post and code useful, please cite it 🙂 </p>
<p></p>
 

</div>