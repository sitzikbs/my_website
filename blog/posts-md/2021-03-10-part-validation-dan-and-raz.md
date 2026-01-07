---
layout: layouts/blog-post.njk
title: "Part Validation using Kinect and Augmented Reality"
date: 2021-03-10
author: Itzik Ben-Shabat
permalink: "/blog/posts/2021-03-10-part-validation-dan-and-raz.html"
---

<div class="post-content">
{% raw %}




<p>As a PhD student, time is my most valuable resource. Unfortunately, there is never enough of it to do all the things I wish I could. Sometimes I get crazy project ideas but balancing research, teaching and family I never get the time to work on them.</p>
<p>Luckily, every once in a while I tell my idea to a student or two and I see a spark in their eyes and every once in a blue moon they actually take it on themselves and create something new and exciting that exceeds my expectations.</p>
<p> </p>
<p>This post is about one of these unique cases where <a href="https://www.linkedin.com/in/dan-nabel-b29151124/" rel="noopener" target="_blank">Dan Nabel </a>and Raz Kochavi created their “<strong>Part Validation using Kinect and Augmented Reality</strong>”  project which received the “best poster” award in the Technion’s mechanical engineering undergraduate projects competition.</p>
<p>You can view the poster <a href="/assets/images/blog/Poster-raz-and-dan.pdf" rel="noopener" target="_blank">here </a>(Hebrew).</p>
<p>*The work was done under the supervision of <a href="https://meeng.technion.ac.il/members/anath-fischer/" rel="noopener" target="_blank">Prof. Anath Fischer</a></p>
<p>{% endraw %}
{% responsiveImage "../../assets/images/blog/2017-08-poster_dan_raz.jpg", "" %}
{% raw %}


</p>
<p> </p>
<p><strong>Intro</strong> (mostly for non- mechanical engineers): The design of a new product encapsulates many stages, from characterizing the customer’s requirements, creating a detailed specification, conceptual design, detailed mechanical design,  manufacturing, assembly and evaluation testing. Between the manufacturing and assembly stages, there is an internal stage called “validation”. In this stage, the manufacturer ( and usually the client too) inspects and measures the manufactured part in order to check if it meets the design specification.  In a perfect world, every manufacturer will supply every single part exactly as the CAD model and sketch specify. However, we don’t live in a perfect world.  The process of validation and inspection is something that takes time (and money). Sometimes there is a person that stands and manually measures the part with a caliper and sometimes there is a very big, very expensive, very calibrated machine that does it automatically for a subset of the manufactured parts. One of the hardest cases to validate are free-form surfaces.  Their unique geometry is usually so complex that traditional measuring instruments are just not enough.</p>
<p> </p>
<p><strong>The goal</strong> of this work was to create a small, portable and low-cost part validation system for mechanical parts with free-form surfaces.</p>
<p> </p>
<p><strong>The challenges </strong>are multiple (especially for an undergraduate), here are some of the questions Dan and Raz faced (and the answers they came up with).</p>
<ul>
<li>How to scan the part?  (<a href="https://en.wikipedia.org/wiki/Kinect" rel="noopener" target="_blank">Microsoft Kinect V2</a> – low-cost 3D camera)</li>
<li>How to separate the scanned part from its surrounding? (<a href="https://en.wikipedia.org/wiki/Image_segmentation" rel="noopener" target="_blank">Segmentation </a>using adjustable color threshold on the image)</li>
<li>How to align between the scanned part and the CAD model? (<a href="https://en.wikipedia.org/wiki/Point_set_registration" rel="noopener" target="_blank">Registration </a>using <a href="https://en.wikipedia.org/wiki/Iterative_closest_point" rel="noopener" target="_blank">ICP</a> with a user interface for initial  coarse alignment)</li>
<li>How to display the computed errors? ( Augmented Reality – project the error map on the part using a projector )</li>
</ul>
<p> </p>
<p><strong>The approach</strong> consists of two main parallel input processing branches:</p>
<ul>
<li>Digital processing</li>
<li>Physical “measuring”</li>
</ul>
<p>These branches unite in the registration stage and finally, the error is evaluated and visualized.</p>
<p>In the<em> digital processing</em> branch, we get the CAD model of the manufactured part.  Commercial CAD software (like Solidworks, Creo, NX etc.) save their models in a parametric representation of its surfaces. We then discretize this model by converting it to a triangle mesh ( faces and vertices). The algorithm that performs this conversion in the CAD software creates a highly non-uniform mesh (few large triangles on planes, many small triangles on curved surfaces).  We wish to get a relatively uniform sampling of points on the surface of the model, therefore remesh and then sample the points.  At the end of this branch, we get a digitally sampled point cloud, evaluated on the faces of the original CAD model. We use this point cloud as the reference for the scanned point cloud that is the output of the physical “measuring” branch.</p>
<p> </p>
<p>In the <em>physical “measuring”</em> stage we take the manufactured part and scan it using a Kinect V2. The Kinect is a low cost but rather accurate 3D camera. It produces two images – an RGB image (just like a regular camera) and a depth image. Each pixel in the depth image contains a value that is proportional to the distance of that point in space from the camera. Using the camera parameters, these two images are aligned and a 3D point cloud is generated, which contains XYZ coordinates for a list of points. The next problem is that the camera “doesn’t know” that we only want points on the part so it “gives us” points on the part and around it. In order to discard the background points we put the part in an area with a distinct background color (for example white) and then discard the white points. In reality, we allowed several different background colors with an adjustable threshold.  At the end of this branch, we get a measured point cloud sampled on the manufactured part.</p>
<p> </p>
<p>Next, we take the two point clouds and align them using a two stage <em>registration</em> process. First, we perform coarse registration using a user specified matching points. Second, we run a variation of the well known Iterative Closest Point (ICP) algorithm for the final fine alignment. Once the two point clouds are</p>
<p> </p>
<p>Once the two point clouds are aligned we compute the distances between every two closest points between the two point clouds. To do this efficiently we use a <a href="https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm" rel="noopener" target="_blank">K nearest neighbor algorithm</a> (K=1 in this case) which uses the<a href="https://en.wikipedia.org/wiki/K-d_tree" rel="noopener" target="_blank"> K-d tree data structure.</a>  If there are no manufacturing errors all of the computed distances should be zero (or a very small number) but, if there is a defect the distance will spike. For <em>visualization</em> purposes, we now map all of the distances to a color map (from blue=acurate to red=high error).    Next, we project these points onto a plane and display it on screen. At this point we realized that just looking at it on the screen is simply not enough anymore (in the world where augmented reality is a great buzz word) so we connected a projector and projected the error map onto the part .  Now we could really see the errors on the part.</p>
<p> </p>
<p>The approach is summarized visually in the flowchart below (click on it to see full-size).  For further details, you can read their full report <a href="/assets/images/blog/Part-Validation-Dan-and-Raz.pdf" rel="noopener" target="_blank">here </a>(Hebrew)</p>
<p><a href="assets/images/blog/FLOW-CHART.png" rel="noopener" target="_blank">{% endraw %}
{% responsiveImage "../../assets/images/blog/FLOW-CHART.png", "" %}
{% raw %}


</a></p>
<p> </p>
<p>In the image below you can see the <strong>results</strong> of visualization on a test part.  We took a big chunk of Plasticine and placed it on the part (right) and the projected visualization (left). The system shows the expected high errors on the Plasticine. (Note that even though the part is shiny and red the projection is seen well)</p>
<p>{% endraw %}
{% responsiveImage "../../assets/images/blog/Error-Map.jpg", "" %}
{% raw %}


</p>
<p> </p>
<p>Remember how a picture is worth a thousand words? So how many words is a demo?</p>
<p><strong>Demo: </strong> The video below shows each of the stages of the solution (prototype)</p>
<p><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" style="border: none;" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/bA0NUccz3BM?start=11&amp;feature=oembed" title="Part Validation for Demonstration" width="800"></iframe></p>
<p> </p>
<p>Disclaimer: I must say that Dan and Raz built a great prototype but, as in any other system, there are some drawbacks. We all agreed that the overall accuracy of the system can be improved. Each of the steps contributes to inaccuracy, starting from the Kinect itself which has a limited depth resolution and ending with the registration that may be inaccurate (especially in scenarios of high deformation).  In addition, when projecting the error map on the part some manual alignment is performed. All of these issues are solvable but when squeezed into an undergraduate project we just didn’t get to them ( future work anyone?).</p>
<p> </p>
<p>You can download their source code <a href="/assets/images/blog/PartsValidator.zip">here</a>. It contains MATLAB files and some sample STL files (the package also contains its dependencies like <a href="https://www.mathworks.com/matlabcentral/fileexchange/29276-dragzoom-drag-and-zoom-tool" rel="noopener" target="_blank">Dragzoom</a>).</p>
<p> </p>
<p>In <strong>summary</strong>, I think Dan and Raz did a great job. They created a new low-cost, portable system for mechanical parts validation.  Most importantly, they learned a lot in the process and had some fun, I know I did.</p>
 

{% endraw %}
</div>