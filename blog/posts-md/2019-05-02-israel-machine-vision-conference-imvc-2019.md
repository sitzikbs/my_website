---
layout: layouts/blog-post.njk
title: "Israel Machine Vision Conference (IMVC) 2019"
date: 2019-05-02
author: Itzik Ben-Shabat
permalink: "/blog/posts/2019-05-02-israel-machine-vision-conference-imvc-2019.html"
---

<div class="post-content">


<p>This was my first visit to IMVC which just celebrated 10 years of activity.  I found it to be a very interesting combination of academia and industry work which provides a great platform for disseminating knowledge and fostering future collaborations. Personally, I presented a poster on our recent point cloud classification method.</p>
<p>I would like to thank the committee, IMVC organizers and Nexar for the <strong>graduate student award</strong>.</p>
<p>The <a href="https://www.imvc.co.il/Program/GeneralProgram.aspx" rel="noopener noreferrer" target="_blank">full program</a> and <a href="https://www.imvc.co.il/Program/InvitedSpeakers.aspx" rel="noopener noreferrer" target="_blank">list of speakers</a> can be found on the event website and I will shortly summarize here some of the sessions I attended. Here is also a link to all the<a href="https://www.imvc.co.il/Program/PresentationsVideos.aspx" rel="noopener noreferrer" target="_blank"> videos and presentations</a>.</p>
<p align="center">{% responsiveImage "../../assets/images/blog/imvc2019_Entrance.jpg", "" %}
 {% responsiveImage "../../assets/images/blog/IMVC2019_Name_tag.jpg", "" %}
</p>
<p>The day started with an interesting talk by <a href="http://www.cs.huji.ac.il/~peleg/" rel="noopener noreferrer" target="_blank">Prof. Shmuel Peleg</a> on the benefits of combining sight and sounds. He showed a great example of how our mind can fool us to think we are hearing a different sound when a video is manipulated or swapped. He then presented their method for combining video and sound modalities for the application of sound separation and sound enhancement.</p>
<p>Next, <a href="https://researcher.watson.ibm.com/researcher/view.php?person=il-AYAS" rel="noopener noreferrer" target="_blank">Dr. Aya Soffer</a> from IBM talked about moving from perception to comprehension and how they use video and additional modalities for scene detection and semantics. She talked about their experience with applying image models on videos, then moved to detail some  “few shots” learning methods (<a href="https://arxiv.org/abs/1806.04728" rel="noopener noreferrer" target="_blank">RepMet</a>, <a href="https://arxiv.org/abs/1902.09811" rel="noopener noreferrer" target="_blank">LaSO</a>, <a href="https://arxiv.org/abs/1806.04734" rel="noopener noreferrer" target="_blank">delta encoder</a>). Finally, she presented their “<a href="http://moments.csail.mit.edu/" rel="noopener noreferrer" target="_blank">Moments in Time” dataset</a>.</p>
<p>At this point, they announced the graduate and undergraduate award winners (me!!!). I had the privilege to give a 5-minute “pitch” talk of our point cloud classification work. It was a lot of fun to see how many people found it interesting and relevant for their own work.</p>
<p>{% responsiveImage "../../assets/images/blog/IMVC2019_Award.jpeg", "" %}
</p>
<p>{% responsiveImage "../../assets/images/blog/3DmFV_Pitch.jpeg", "" %}
</p>
<p>Next, <a href="https://simons.berkeley.edu/people/naftali-tishby" rel="noopener noreferrer" target="_blank">Prof. Naftali Tishby</a> talked about the information theory of deep learning. He was followed by Dr. <a href="https://www.linkedin.com/in/laurencekeselbrener/?originalSubdomain=il" rel="noopener noreferrer" target="_blank">Laurence Keselbrener</a> from Medtronics who talked about AI for capsule endoscopy, specifically for colorectal cancer using <a href="https://www.medtronic.com/covidien/en-us/products/capsule-endoscopy/pillcam-sb-3-system.html#pillcam-sb-3-capsule" rel="noopener noreferrer" target="_blank">PillCam</a>. They use AI for several tasks, including reducing image reading times, image enhancement, detection, and localization.  As a person who suffers from Crohn’s disease (Type of chronic inflammatory bowel disease), I think this work will be life changing for many people.</p>
<p>Dr. <a href="https://ai.google/research/people/106214" rel="noopener noreferrer" target="_blank">Yael Pritch Knaan</a> talked about Computational photography on googles smartphone. She presented the tech behind one of my favorite features in Android devices the “<a href="https://ai.googleblog.com/2018/11/learning-to-predict-depth-on-pixel-3.html" rel="noopener noreferrer" target="_blank">Portrait mode</a>“. Here, they achieved shallow depth of field with a single camera using dual pixel data.   She also shortly presented “<a href="https://www.theverge.com/2018/11/14/18092660/google-night-sight-review-pixel-2-3-camera-photos-image-quality" rel="noopener noreferrer" target="_blank">Night Sight</a>” (read more in<a href="https://ai.googleblog.com/2018/11/night-sight-seeing-in-dark-on-pixel.html" rel="noopener noreferrer" target="_blank"> Google AI blog post</a>), a cool new feature on pixel devices that produces great images in low lighting conditions.</p>
<p>{% responsiveImage "../../assets/images/blog/Yael_Pritch_Knaan_nightsight.jpg", "" %}
</p>
<p>To conclude the session Dr. Andrey Boisman talked about the mission of the ministry of science and technology.</p>
<p>At this point, there was a coffee break after which parallel sessions started. I will detail below a few talks that I attended and particularly liked, though because of my poster presentation I missed a lot of them.</p>
<p>{% responsiveImage "../../assets/images/blog/IMVC2019_poster.jpg", "" %}
</p>
<p>There was also a great exhibition floor that I did not get to fully explore. I only had a chance to visit the booth of “<a href="https://coraldrowningdetection.com/" rel="noopener noreferrer" target="_blank">Coral Detection Systems</a>” which was co-founded by an old colleague of mine (<a href="https://www.linkedin.com/in/tamar-avraham-1959911a/?originalSubdomain=il" rel="noopener noreferrer" target="_blank">Tammar Avraham</a>). They created an amazing product for drowning detection called MANTA.</p>
<p>Assaf Socher presented several papers on Deep internal learning – super-resolution (<a href="http://www.wisdom.weizmann.ac.il/~vision/zssr/" rel="noopener noreferrer" target="_blank">ZSSR</a>), and <a href="http://www.wisdom.weizmann.ac.il/~vision/ingan/" rel="noopener noreferrer" target="_blank">InGAN</a> .</p>
<p>There was a very mind-opening panel discussion on the future, ethics and social aspects of AI (List of speakers in the image below).</p>
<p>{% responsiveImage "../../assets/images/blog/IMVC2019_Panel.jpg", "" %}
</p>
<p>Ilan Kadar from <a href="https://www.getnexar.com/" rel="noopener noreferrer" target="_blank">Nexar</a> talked about continuous deep learning at the edge and presented their <a href="https://www.youtube.com/watch?v=yc74HHTAMns" rel="noopener noreferrer" target="_blank">MUNET</a> – simultaneous multi-tasks for driving on a mobile device. He discussed some corner cases (when something highly improbable happens) – continuous learning pipeline. He also presented their <a href="https://bair.berkeley.edu/blog/2018/05/30/bdd/" rel="noopener noreferrer" target="_blank">BDD100K dataset</a> for road understanding research.</p>
<p>Elad Richardson from the Israeli defense community presented their work on text detection which finds a common scale for all text elements in an image and mitigates the advantages of multi-scale approach (accurate but slow) and single scale approach (fast but not very accurate)</p>
<p>Finally, <a href="https://chechiklab.biu.ac.il/~gal/" rel="noopener noreferrer" target="_blank">Prof. Gal Chechik</a> presented several works on extracting meaningful concepts without explicit supervision.</p>
 

</div>