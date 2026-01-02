---
layout: layouts/blog-post.njk
title: "Aligning Step-by-Step Instructional Diagrams to Video Demonstrations"
date: 2023-05-17
author: Itzik Ben-Shabat
permalink: "/blog/posts/2023-05-17-iaw_dataset.html"
---

<div class="post-content">


<p>In this episode of the <a href="https://www.itzikbs.com/the-talking-papers-podcast" rel="noreferrer noopener" target="_blank">Talking Papers Podcast</a>, I hosted Jiahao Zhang to chat about our CVPR 2023 paper “Aligning Step-by-Step Instructional Diagrams to Video Demonstrations”.</p>
<p>In this paper we proposed a new task, aligning instructional videos and manual images of an IKEA furniture assembly diagram. To do that, we collected and annotated a brand new dataset: “IKEA Assembly in the Wild” where we aligned YouTube videos with IKEA’s instruction manuals. Our approach to addressing this task proposes several supervised contrastive losses that contrast between video and diagram, video and manual, and internal manual images. </p>
<p></p>
<p>Jiahao is currently a PhD student at the Australian National University. His research focus is on human action recognition and multi-modal representation alignment. We first met (virtually) when Jiahao did his Honours project, where he developed an amazing (and super useful) video annotation tool <a href="https://github.com/anucvml/vidat" rel="noreferrer noopener" target="_blank">ViDaT</a>. His strong software engineering and web development background gives him a strong advantage when working on his research projects. Even though we never met in person (yet), we are actively collaborating and I already know what he is cooking up next. I hope to share it with the world soon.</p>
<p></p>
<p></p>
<div id="buzzsprout-player-12858311"></div><script charset="utf-8" src="https://www.buzzsprout.com/1914034/12858311-iaw-dataset-jiahao-zhang.js?container_id=buzzsprout-player-12858311&amp;player=small" type="text/javascript"></script>
<h2 class="wp-block-heading" id="authors">AUTHORS</h2>
<p id="stephen-gould-richard-hartleydylan-campbell"><em>Jiahao Zhang, Anoop Cherian, Yanbin Liu, Yizhak Ben-Shabat, Cristian Rodriguez, Stephen Gould</em></p>
<p><br/></p>
<h2 class="wp-block-heading" id="abstract">ABSTRACT</h2>
<p> </p>
<p>Abstraction is at the heart of sketching due to the simple and minimal nature of line drawings. Abstraction entails identifying the essential visual properties of an object or scene, which requires Implicit Neural Representations (INRs) have emerged in the last few years as a powerful tool to encode Multimodal alignment facilitates the retrieval of instances from one modality when queried using another. In this paper, we consider a novel setting where such an alignment is between (i) instruction steps that are depicted as assembly diagrams (commonly seen in Ikea assembly manuals) and (ii) video segments from in-the-wild videos; these videos comprising an enactment of the assembly actions in the real world. To learn this alignment, we introduce a novel supervised contrastive learning method that learns to align videos with the subtle details in the assembly diagrams, guided by a set of novel losses. To study this problem and demonstrate the effectiveness of our method, we introduce a novel dataset: IAW—for Ikea assembly in the wild—consisting of 183 hours of videos from diverse furniture assembly collections and nearly 8,300 illustrations from their associated instruction manuals and annotated for their ground truth alignments. We define two tasks on this dataset: First, nearest neighbor retrieval between video segments and illustrations, and, second, alignment of instruction steps and the segments for each video. Extensive experiments on IAW demonstrate superior performances of our approach against alternatives.</p>
<p> </p>
<p></p>
<h2 class="wp-block-heading" id="related-papers">RELATED (WORKS|PAPERS)</h2>
<p>📚<a href="https://ikeaasm.github.io/" rel="noreferrer noopener" target="_blank">IKEA ASM dataset</a></p>
<p>📚<a href="https://arxiv.org/abs/2103.00020" rel="noreferrer noopener" target="_blank">CLIP</a></p>
<p>📚<a href="https://arxiv.org/abs/1812.03982" rel="noreferrer noopener" target="_blank">SlowFast </a></p>
<h2 class="wp-block-heading">LINKS AND RESOURCES</h2>
<p>📚 <a href="https://arxiv.org/pdf/2303.13800.pdf" rel="noreferrer noopener" target="_blank">Paper</a></p>
<p>💻<a href="https://academic.davidz.cn/en/publication/zhang-cvpr-2023/" rel="noreferrer noopener" target="_blank">Project page</a></p>
<p>💻<a href="https://iaw.davidz.cn/" rel="noreferrer noopener" target="_blank">Dataset page</a></p>
<p>💻<a href="https://github.com/DavidZhang73/AssemblyVideoManualAlignment">Code</a></p>
<p>To stay up to date with Jiahao’s latest research, follow him on:</p>
<p>👨🏻‍🎓<a href="https://scholar.google.com/citations?user=PpHLOpQAAAAJ&amp;hl=it" rel="noreferrer noopener" target="_blank">personal pag</a><a href="https://academic.davidz.cn/en/">e</a></p>
<p>👨🏻‍🎓<a href="https://scholar.google.com/citations?user=PpHLOpQAAAAJ&amp;hl=it" rel="noreferrer noopener" target="_blank">Google Schola</a><a href="https://scholar.google.co.uk/citations?user=r040KUgAAAAJ" rel="noreferrer noopener" target="_blank">r</a></p>
<p>👨🏻‍🎓<a href="https://github.com/DavidZhang73" rel="noreferrer noopener" target="_blank">Github</a></p>
<p></p>
<p></p>
<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/CIkLsrTC7eY?feature=oembed" title="IAW Dataset (CVPR 2023) with Jiahao Zhang on Talking papers" width="800"></iframe>
</div></figure>
<p>Recorded on May 1st 2023.</p>
<h3 class="wp-block-heading">SPONSOR</h3>
<p>This episode was sponsored by YOOM. YOOM is an Israeli startup dedicated to volumetric video creation. They were voted as the 2022 best start-up to work for by Dun’s 100.<br/><a href="https://www.yoom.com/careers" rel="noreferrer noopener" target="_blank">Join their team</a> that works on geometric deep learning research, implicit representations of 3D humans, NeRFs, and 3D/4D generative models.</p>
<p><br/>Visit <a href="https://www.yoom.com/" rel="noreferrer noopener" target="_blank">YOOM.com</a>.</p>
<h2 class="wp-block-heading"><br/>CONTACT</h2>
<p>If you would like to be a guest, sponsor or share your thoughts, feel free to reach out via email: talking (dor) papers (dot) podcast(at) gmail (dot) com</p>
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