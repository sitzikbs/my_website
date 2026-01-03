---
layout: layouts/blog-post.njk
title: "The 1st Winter School in Computer Science and Engineering on Computer Vision"
date: 2017-01-30
author: Itzik Ben-Shabat
permalink: "/blog/posts/2017-01-30-the-1st-winter-school-in-computer-science-and-engineering-on-computer-vision.html"
---

<div class="post-content">


<p>As the title implies, on 8-13 of January 2017 I attended “<a href="http://ias.huji.ac.il/cse">The 1st Winter School in Computer Science and Engineering on Computer Vision</a>” At the<a href="https://www.google.com/maps/place/The+Institute+for+Advanced+Studies/"> Israel Institute for Advanced Studies</a> in Givat Ram Campus in Jerusalem, Israel.</p>
<p>{% responsiveImage "../../assets/images/blog/IMG_20170108_091832.jpg", "img_20170108_091832" %}
</p>
<p>This conference was very interesting, inspiring and motivating.They had a dream team of speakers from the vision community. I wrote a lot of notes but here is a brief summary.</p>
<p>The goal of this post is to summarize the contents and provide a source for all of the useful links from the winter school.</p>
<p>Video lectures are available on youtube in this <a href="https://www.youtube.com/playlist?list=PLTn74Qx5mPsSniA5tt6W-o0OGYEeKScug">Link</a>.</p>
<h2><strong>Day 1</strong></h2>
<p><a href="https://people.eecs.berkeley.edu/~malik/">Prof. Jitendra Malik</a>  from UC Berkley gave a talk via skype called “Deep Visual Understanding from Deep Learning”  surveying some of his most recent work on</p>
<ul>
<li>Feedback Architecture</li>
<li>3D understanding</li>
<li>Predicting and self-supervision</li>
</ul>
<p>Selected quote: “Object detection is nearly solved’</p>
<p>Next <a href="http://cs.nyu.edu/~fergus/pmwiki/pmwiki.php">Prof. Rob Fergus</a> from NYU and Facebook gave a very good “Introduction to Convolutional networks” starting with LeCun’s work and working his way through non-linearity, pooling, and choosing learning rates. He stated that the main challenge in this field is the question of “how to design the network?”  (How many layers, filter size, number of elements in each layer etc.) The main conclusion is that deeper networks are better.</p>
<p>Selected quote: ” Its not about the parameters, Its about the depth”</p>
<p>After lunch, there was a great panel which presented classic papers in computer vision. The panel included the legendary <a href="http://www.ri.cmu.edu/person.html?person_id=136">Takeo Kanade</a> from Carnegie Mellon (which later came to talk to me about my poster and gave me some great ideas), <a href="http://www.cs.columbia.edu/~nayar/">Shree K. Nayar</a> from Columbia and <a href="http://www.wisdom.weizmann.ac.il/mathusers/irani/">Michal Irani</a> from <a href="http://www.weizmann.ac.il/">The Weizmann Institute of Science</a>.</p>
<p>On this day I presented my poster, including a short spotlight presentation ( 5 minutes).</p>
<p>{% responsiveImage "../../assets/images/blog/20170108_161315.jpg", "20170108_161315" %}
 {% responsiveImage "../../assets/images/blog/2017-01-20170108_161943.jpg", "20170108_161943" %}
{% responsiveImage "../../assets/images/blog/IMG_20170108_174806.jpg", "img_20170108_174806" %}
</p>
<p>Best poster of the day (in my opinion) was <a href="http://people.eecs.berkeley.edu/~shiry/">Shiry Ginosar</a> “<a href="https://people.eecs.berkeley.edu/~shiry/projects/yearbooks/yearbooks.html">Century of Portraits: A Visual Historical Record of American High School Yearbooks</a>“. Here is a small teaser: she made an Afro haircut classifier (those who knew me during 2001-2002 know why this is very <a href="/assets/images/blog/ItzikAfro.jpg" target="_blank">sentimental </a>🙂 ).</p>
<h2><strong>Day 2</strong></h2>
<p><a href="http://www.cs.huji.ac.il/~yweiss/">Prof. Yair Weiss</a> from The Hebrew University of Jerusalem opened the day with a very interesting talk titled ” Neural Networks, Graphical Models, and Image Restoration”. He presented his work on denoising and the <a href="http://www.cs.tut.fi/~foi/GCF-BM3D/">BM3D</a>. He emphasized that graphical models have the advantage of being interpretable and modular. Looking into the future he said that intelligent system should perform unsupervised learning and incorporate between neural networks and graphical models because we now expect papers that do more than just improve the performance of a single task.</p>
<p>Selected quote: “In 1998, the keywords that were most likely to predict rejection from NIPS were: Neural Networks”</p>
<p>Prof. <a href="http://www.wisdom.weizmann.ac.il/mathusers/irani/">Michal Irani</a> gave a talk about ” “Blind” visual inference”. She presented several works on the following topics</p>
<ul>
<li>Blind Optics
<ul>
<li>Blind Deblurring</li>
<li>Blind Dehazing</li>
</ul>
</li>
<li>Detecting similar objects and actions</li>
<li>Analyzing and segmenting video without constraint</li>
</ul>
<p>All of these papers were significantly different from each other yet seem to share the principle of searching for patch \ regions reoccurrence and similarity.</p>
<p>Selected quote: “while this has nothing to do with deep neural networks, If we want to scale up we need to learn how to incorporate these principals into neural networks”.</p>
<p>After lunch Prof. <a href="http://www.ri.cmu.edu/person.html?person_id=136">Takeo Kanade</a> gave an amazingly inspiring talk titled “Fun Research in Computer Vision”. He talked about his moments of fame with his <a href="https://www.ri.cmu.edu/events/sb35/tksuperbowl.html">Eyevision </a>system for the 35th super Bowl and his guest appearance in the Bruce Willis movie “surrogates”. Next, he addressed fundamental questions such as ” what is your wish as a researcher\engineer?”  he presented the problematic “expert thinking” and said</p>
<p>selected quote: “<strong>Think like an amateur, do as an expert</strong>“</p>
<p>He then continued to blow our minds with grandiose projects (from the late 70’s – present)  of his autonomous car, 3D Dome, 4D digitalization, car lights that avoid rain or snow reflections and much more.</p>
<p>Another selected quote: “Newness is not virtue, usefulness is”</p>
<p>He finished with the story of how he had a student that did some very simple work, so simple he thought it wasn’t worth publishing but because the student insisted he approved its publication in an obscure conference. It turned out this was the famous<a href="https://en.wikipedia.org/wiki/Lucas%E2%80%93Kanade_method"> Lucas-Kanade</a> optical flow algorithm that has over 14000 citations.</p>
<p>Finally, he signed off with Allen Newell quote: “Problems are waiting for you to solve”.</p>
<p>INSPIRING! ! !</p>
<p>{% responsiveImage "../../assets/images/blog/Takee_Yair_Michal_Me.jpg", "takeo_yair_michal_me" %}
</p>
<p>(A photo of Takeo, Yair, Michal and me – Only on the last day I decided I can’t go home without one, now I have a picture with celebrities ! ! ! )</p>
<p>After this amazing talk, there were some more student spotlights and poster sessions followed by a visit to <a href="http://www.mobileye.com/">Mobileye</a>, where they presented their cutting edge technology followed by <a href="http://www.orcam.com/">Orcam</a>.</p>
<h2><strong>Day 3</strong></h2>
<p>The day started with a great talk by <a href="http://homes.cs.washington.edu/~kemelmi/">Ira Kemelmacher</a> from the university of Washington titled “People modeling from Historical Footage”. Her goal was to create 3D models that move and act like real people. Her 3D Obama and holocaust survivors was amazing. I also loved the <a href="https://www.youtube.com/watch?v=qqmXPj-oIN4&amp;list=PLSCK7y_AEdoZLOjca-f0yNCtGl1MakBWt&amp;index=6">HoloChess </a>virtual and augmented reality capstone project. I can’t wait to start playing around with the <a href="https://www.youtube.com/watch?v=fLQtssJDMMc">Face Movie</a> feature in picasa (which I did not even know exists).</p>
<p>selected quoute : “Rembrandt was the creator of the selfie”</p>
<p>Next, <a href="http://thoth.inrialpes.fr/~schmid/">Cordelia Schmidt</a> from INRIA Grenoble gave a talk about “Action Recognition and automatic video understanding”. she explained that the main difficulties are in large variations in appearance, manual collection of training data and that action vocabulary is not well defined. She then presented work on the subject.</p>
<p>After lunch, <a href="http://thoth.inrialpes.fr/~schmid/">Cordelia Schmidt</a>, <a href="http://cs.nyu.edu/~fergus/pmwiki/pmwiki.php">Rob Fergus</a> and <a href="https://people.eecs.berkeley.edu/~efros/">Alexei (Alyosha) Efros</a> held a panel about “Deep Learning in Computer Vision” in which Alyosha emphasized the importance of data and Rob presented a predictive model of a simple world “Physnet” to predict falling cubes. During the Q&amp;A  portion of the panel, Yair Weiss said (when asked about the future of deep learning) ” Neural nets would be like matrix multiplication – a tool like many tools”</p>
<p>Selected quotes (by Alyosha): “The Revolution will not be Supervised”, “ConvNets is a particular useful black box”.</p>
<p>Best poster of the day (in my opinion) was by <a href="https://scholar.google.co.il/citations?user=XqHYn7EAAAAJ&amp;hl=en">Tal Remez</a> titled “Deep Class Aware Denoising” where he used convolutional networks to denoise images according to their class – very simple with some interpretation of what the layers are doing. A close second best was <a href="http://www.cs.technion.ac.il/~royorel/">Roy Or-El</a> with a poster titled “Learning Detailed Face Reconstruction from a Single Image”.</p>
<h2><strong>Day 4</strong></h2>
<p>The day started with a MIND BLOWING (!!!) talk by Prof. <a href="http://www.cs.columbia.edu/~nayar/">Shree K. Nayar</a> titled “Computational imaging”. He said that there is a paradigm shift from traditional imaging to computational imaging which uses optics that encode additional useful information with new functionality and reduced complexity. During the talk, Shree answered the following questions (the answers to all of the questions is yes and a link to each his paper\ product in brackets)</p>
<ul>
<li>Can a camera capture everything around it? (<a href="http://www.cs.columbia.edu/CAVE/projects/cata_edof/">Catadioptrics</a>)</li>
<li>Can a camera capture bright skies and dark shadows? (<a href="http://www.cs.columbia.edu/CAVE/projects/hdr_ap/">Dynamic Range: Assorted Pixels</a>)</li>
<li>Can a camera take a photo with a billion pixels? (<a href="http://gigapan.com/">Gigapan </a>demo, <a href="http://www.cs.columbia.edu/CAVE/projects/gigapixel/">Gigapixel</a>)</li>
<li>Can a camera see what you see? (<a href="http://www.cs.columbia.edu/CAVE/projects/world_eye/">The world in an eye</a>)</li>
<li>Can we refocus a photograph?</li>
<li>Can a photo be focused everywhere? (<a href="http://www.cs.columbia.edu/CAVE/projects/focal_sweep_camera/">Focal Sweep</a>)</li>
<li>Can a camera separate direct and indirect light? (<a href="http://www.cs.columbia.edu/CAVE/projects/separation/">Direct and Global</a>)</li>
<li>Can a camera power itself? (<a href="http://www.cs.columbia.edu/CAVE/projects/self_powered_camera/">Eternal video</a>)</li>
<li>Can a camera be flexible? (<a href="http://www.cs.columbia.edu/CAVE/projects/flexible_sheet_cameras/">Elastic Optics</a>)</li>
<li>Can a camera Educate? (<a href="http://www.bigshotcamera.com/">BigShot </a>,<a href="http://www.cs.columbia.edu/CAVE/projects/cambits/">Cambits</a>– I can’t wait for my son to be old enough)</li>
</ul>
<p>He finished the lecture by declaring that ” The future of Imaging is bright”.</p>
<p>Selected quote(s):</p>
<p>“We talked about neural networks … one of the enabling factors is the <span style="text-decoration: underline;">sensors</span>“</p>
<p>“We are in the middle of an imaging revolution”</p>
<p>“SIGGRAPH is a lifestyle, it is not a conference” (joking)</p>
<p>Next Prof.<a href="https://billf.mit.edu/"> William (Bill) T.Freeman </a>from MIT and Google gave a talk about ” Accidental Imaging and motion magnification”. He talked about the well known <a href="https://play.google.com/store/apps/details?id=com.google.android.apps.photos.scanner&amp;hl=en">PhotoScan App</a>, <a href="http://people.csail.mit.edu/mrub/vidmag/">Motion magnification</a> (which has a <a href="https://www.ted.com/talks/michael_rubinstein_see_invisible_motion_hear_silent_sounds_cool_creepy_we_can_t_decide">TEDx talk</a>) but also about</p>
<ul>
<li>Pinhole and Pinspeck cameras</li>
<li>Edge cameras</li>
<li>Surface cameras</li>
</ul>
<p>He showed some results for “Seeing around the corner”.</p>
<p>What I found fascinating most about this talk is the way he looked at problems differently (Generating images through shadows rather than light)</p>
<p>Selected quote: “I want to take a picture of the earth by looking at the moon” (using a satellite is cheating!)</p>
<p>After lunch, we went on a tour of the old city of Jerusalem and took a great photo near the Kotel \ Western wall\ Wailing wall (There were a lot of other great photos but i think this one was the best one)</p>
<p>{% responsiveImage "../../assets/images/blog/CSE_OldCityofJerusalemPhoto.jpg", "Old City of Jerusalem 1st winter school" %}
</p>
<p> </p>
<p>After the tour, we went to visit Intel in the Perceptual computing group. They presented fun demos of applications that use their <a href="http://www.intel.com/content/www/us/en/architecture-and-technology/realsense-overview.html">RealSense </a>RGBD camera. The demos included<a href="https://zenbo.asus.com/"> Asus zenbo</a>, <a href="https://newsroom.intel.com/chip-shots/intel-unveils-project-alloy/">Project alloy</a> (which I didn’t get to try because the line was sooooo long, I can only guess how awesome it was) and a fun balloon popping game using <a href="https://www3.oculus.com/en-us/rift/">oculus Rift</a>. Here is a picture of me trying to pop some balloons:</p>
<p>{% responsiveImage "../../assets/images/blog/OculusRiftRealSenseDemo.jpg", "Intel Oculus Rift Realsense Demo" %}
</p>
<p>Finally, we all went out to Machne Yehuda and drank some beer as it was the last night together for most of us.</p>
<p>{% responsiveImage "../../assets/images/blog/Machne-Yehuda-Beer.jpg", "All the students driniking beer in Machneyehuda" %}
</p>
<h2><strong>Day 5</strong></h2>
<p>The day started with a talk by<a href="http://szeliski.org/RichardSzeliski.htm"> Richard (Rick) Szeliski</a> (which is literally the guy who wrote the <a href="http://szeliski.org/Book/">book </a>on computer vision) titled “3D Reconstruction for <del>Image Based Rendering</del> Computational photography. He talked about</p>
<ul>
<li>Image-based rendering (<a href="https://www.microsoft.com/en-us/research/publication/the-lumigraph/">Lumigraph</a>)</li>
<li>Virtual viewpoint video</li>
<li>360 video</li>
<li>Immersive video stabilizer</li>
<li>Large scale environmental capture (<a href="http://phototour.cs.washington.edu/">Photo Tourism</a>, <a href="https://photosynth.net/">PhotoSynth</a>)</li>
<li>Reflection and transparency</li>
</ul>
<p>He also mentioned the state-of-the-art in 3D reconstruction:</p>
<ul>
<li><a href="https://www.cs.cornell.edu/~snavely/bundler/">Bundler</a></li>
<li><a href="http://ccwu.me/vsfm/">VisualSFM</a></li>
<li><a href="https://colmap.github.io/">COLMAP</a></li>
</ul>
<p>SLAM (Simultaneous Localization and Mapping)</p>
<ul>
<li><a href="http://webdiis.unizar.es/~raulmur/orbslam/">Orb-SLAM </a></li>
<li>PSO</li>
</ul>
<p>Multi-View Stereo</p>
<ul>
<li><a href="https://www.di.ens.fr/cmvs/">CMVS</a></li>
<li><a href="https://github.com/flanggut/smvs">Shading aware multiview stereo</a></li>
</ul>
<p>Next <a href="https://people.eecs.berkeley.edu/~efros/">Alexei (Alyosha) Efros</a> gave a talk titled “Self-supervised Deep Learning with application to image Synthesis. He started by saying “Life is good in Deepland”  and formalized the framework for deep learning: Get data → Define Cost function → Train your network → Train your network  → Sell your startup and become a millionaire</p>
<p>Alyosha focused on the first two steps and said ” King Midas did not think enough about his cost function”. He emphasized the importance of finding a way to perform self supervised learning and demonstrated a way to get context and semantics from a non-semantic task. Next, he demonstrated their <a href="http://www.whatimade.today/two-weeks-of-colorizebot-conclusions-and-statistics/">ColorizeBot</a>. He also recommended avoiding a common phenomenon caused in many DNN related tasks – The “Graduate Student Decent”. he then continued with their work on GANS.</p>
<p>The final panel of the conference was titled “Academia and Industry” and hosted <a href="http://szeliski.org/RichardSzeliski.htm">Rick Szeliski</a>, <a href="http://homes.cs.washington.edu/~kemelmi/">Ira Kemelmacher</a> and <a href="https://billf.mit.edu/">Bill Freeman </a>. It was not recorded  (in order to allow the speakers to speak freely, or as Ira said it “This session never happened”). Each of them presented their unique story of how they juggle academic appointments and industry. Bill referred us to two sources of information on “<a href="http://people.csail.mit.edu/billf/publications/How_To_Do_Research.pdf">How to do research</a>” and  “<a href="https://homes.cs.washington.edu/~mernst/advice/academic-job.html#The_job_talk">Getting an Academic Job</a>“. I will not be very specific (just to make sure i don’t write something they are not comfortable with) I will just say that the thing I liked most about this panel is that it talked about issues I was (and I’m sure many other students in the audience)  struggling with such as balancing family and work, failures and dead ends (knowing that the best people in the world had some is comforting).</p>
<p>selected quote (Bill): “Go and be the star”</p>
<p>After these great talks and panel the final poster session was held. The best poster of the day (in my opinion) was “<a href="https://arxiv.org/abs/1604.08685">Single Image 3D Interpreter Network</a>” presented by <a href="https://jiajunwu.com/">Jiajun Wu</a>.</p>
<p> </p>
<p>Finally, Takeo summarized the winter school  and said</p>
<p>“I hope you learned the passion of the speakers”</p>
<p>and</p>
<p>“You are our dream team of students”</p>
<p> </p>
<h2><strong>On a personal note</strong></h2>
<p>This winter school was a one once in a lifetime experience. I met some amazing people which I’m sure I will see and hear from again. I learned from the best minds. During the school I felt like a little kid, meeting celebrities and getting to talk to them over lunch.</p>
<p>Most importantly I was inspired and motivated.</p>
<p>I wish to thank the organizers: Michael Rabin( General Director), Takeo Kanade(Director), Alexei (Aloysha) Efros (Codirector), Yair Weiss (Codirector). Thank you for this amazing experience.</p>
<p>And to all the readers who got so far – I hope you find this useful (All the links here are pure gold – hopefully they won’t break too fast). If you feel that I have missed something important, should add some more photos, have an additional link that I should add – <a href="https://www.itzikbs.com/contact/">please contact me</a>.</p>
<p><strong>Update 30.1.17</strong>: Recently I found out that one of the students that I met during the winter school also started a blog. So give <a href="https://oranshayer.wordpress.com/" target="_blank">Oran Shayer’s blog</a> a visit.</p>
 

</div>