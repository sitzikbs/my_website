---
layout: layouts/blog-post.njk
title: "ICON: Implicit Clothed humans Obtained from Normals"
date: 2022-07-18
author: Itzik Ben-Shabat
permalink: "/blog/posts/2022-07-18-icon-implicit-clothed-humans-obtained-from-normals.html"
---

<div class="post-content">
{% raw %}




<p>In this episode of the <a href="https://www.itzikbs.com/the-talking-papers-podcast" rel="noreferrer noopener" target="_blank">Talking Papers Podcast</a>, I hosted <a href="https://xiuyuliang.cn/" rel="noreferrer noopener" target="_blank">Yuliang Xiu</a> to chat about his paper “<a href="Implicit Clothed humans Obtained from Normals" rel="noreferrer noopener" target="_blank">ICON: Implicit Clothed humans Obtained from Normals</a>”, published in CVPR 2022. </p>
<p>In this paper, they take on the task of reconstructing an animatable human avatar from multiple images. Their key ideas are to use local features which are more robust to pose estimation error and exploit the SMPL(-X) body model to infer clothed humans (conditioned on the normals).  Additionally, they propose an inference-time feedback loop that alternates between refining the body’s normals and the shape. </p>
<p>I am looking forward to meeting Yuliang in person at CVPR 2022. It was a pleasure hosting him on the podcast. </p>
<div id="buzzsprout-player-10466744">{% endraw %}
</div><script charset="utf-8" src="https://www.buzzsprout.com/1914034/10466744-yuliang-xiu-icon.js?container_id=buzzsprout-player-10466744&amp;player=small" type="text/javascript"></script>
<h2 class="wp-block-heading" id="authors">AUTHORS</h2>
<p id="stephen-gould-richard-hartleydylan-campbell"><em>Yuliang Xiu, Jinlong Yang, Dimitrios Tzionas, Michael J. Black</em></p>
<p> </p>
<h2 class="wp-block-heading" id="abstract">ABSTRACT</h2>
<p>Current methods for learning realistic and animatable 3D clothed avatars need either posed 3D scans or 2D images with carefully controlled user poses. In contrast, our goal is to learn an avatar from only 2D images of people in unconstrained poses. Given a set of images, our method estimates a detailed 3D surface from each image and then combines these into an animatable avatar. Implicit functions are well suited to the first task, as they can capture details like hair and clothes. Current methods, however, are not robust to varied human poses and often produce 3D surfaces with broken or disembodied limbs, missing details, or non-human shapes. The problem is that these methods use global feature encoders that are sensitive to global pose. To address this, we propose ICON (“Implicit Clothed humans Obtained from Normals”), which, instead, uses local features. ICON has two main modules, both of which exploit the SMPL(-X) body model. First, ICON infers detailed clothed-human normals (front/back) conditioned on the SMPL(-X) normals. Second, a visibility-aware implicit surface regressor produces an iso-surface of a human occupancy field. Importantly, at inference time, a feedback loop alternates between refining the SMPL(-X) mesh using the inferred clothed normals and then refining the normals. Given multiple reconstructed frames of a subject in varied poses, we use SCANimate to produce an animatable avatar from them. Evaluation on the AGORA and CAPE datasets shows that ICON outperforms the state of the art in reconstruction, even with heavily limited training data. Additionally, it is much more robust to out-of-distribution samples, e.g., in-the-wild poses/images and out-of-frame cropping. ICON takes a step towards robust 3D clothed human reconstruction from in-the-wild images. This enables creating avatars directly from video with personalized and natural pose-dependent cloth deformation.</p>
<p> </p>
<h2 class="wp-block-heading" id="related-papers">RELATED (WORKS|PAPERS)</h2>
<p>📚<a href="https://xiuyuliang.cn/monoport/" rel="noreferrer noopener" target="_blank">Monocular Real-Time Volumetric Performance Capture</a></p>
<p>📚<a href="https://shunsukesaito.github.io/PIFu/" rel="noreferrer noopener" target="_blank">PIFu</a></p>
<p>📚<a href="https://shunsukesaito.github.io/PIFuHD/" rel="noreferrer noopener" target="_blank">PIFuHD</a></p>
<h2 class="wp-block-heading">LINKS AND RESOURCES</h2>
<p>💻<a href="https://icon.is.tue.mpg.de/" rel="noreferrer noopener" target="_blank">Project website</a></p>
<p>💻<a href="https://github.com/yuliangxiu/ICON" rel="noreferrer noopener" target="_blank">Code</a></p>
<p>📚 <a href="https://arxiv.org/abs/2112.09127" rel="noreferrer noopener" target="_blank">Paper</a></p>
<p></p>
<p></p>
<p>To stay up to date with Yulian’s latest research, follow him on:</p>
<p>👨🏻‍🎓 <a href="https://xiuyuliang.cn/" rel="noreferrer noopener" target="_blank">Yulian’gs homepage</a></p>
<p>🎓</p>
<p>🐦<a href="https://twitter.com/yuliangxiu" rel="noreferrer noopener" target="_blank">Twitter</a></p>
<p>👨🏻‍🎓<a href="https://www.linkedin.com/in/yuliangxiu" rel="noreferrer noopener" target="_blank">LinkedIn</a></p>
<p></p>
<p></p>
<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/JPk9gu_dQD0?feature=oembed" title="ICON: Implicit Clothed humans Obtained from Normals (CVPR2022) - Yuliang Xiu on Talking Papers" width="800"></iframe>
</div></figure>
<p>Recorded on March 11th 2022.</p>
<h2 class="wp-block-heading"><br/>CONTACT</h2>
<p>If you would like to be a guest, sponsor or just share your thoughts, feel free to reach out via email: <a class="__cf_email__" data-cfemail="a8dcc9c4c3c1c6cf86d8c9d8cddadb86d8c7cccbc9dbdce8cfc5c9c1c486cbc7c5" href="/cdn-cgi/l/email-protection">[email protected]</a></p>
<p></p>
<h2 class="wp-block-heading">SUBSCRIBE AND FOLLOW</h2>
<p>🎧Subscribe on your favourite podcast app: <a href="https://talking.papers.podcast.itzikbs.com" rel="noreferrer noopener" target="_blank">https://talking.papers.podcast.itzikbs.com</a></p>
<p>📧Subscribe to our mailing list: <a href="http://eepurl.com/hRznqb" rel="noreferrer noopener" target="_blank">http://eepurl.com/hRznqb</a></p>
<p>🐦Follow us on Twitter: <a href="https://twitter.com/talking_papers" rel="noreferrer noopener" target="_blank">https://twitter.com/talking_papers</a></p>
<p>🎥YouTube Channel: </p>
<p></p>
<p></p>
<p></p>
 

</div>