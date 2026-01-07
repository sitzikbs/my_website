---
layout: layouts/blog-post.njk
title: "Random Walks for Adversarial Meshes"
date: 2022-12-14
author: Itzik Ben-Shabat
permalink: "/blog/posts/2022-12-14-random-walks-for-adversarial-meshes.html"
---

<div class="post-content">
{% raw %}




<p>In this episode of the <a href="https://www.itzikbs.com/the-talking-papers-podcast" rel="noreferrer noopener" target="_blank">Talking Papers Podcast</a>, we hosted <a href="https://www.linkedin.com/in/amir-belder-89889b103/" rel="noreferrer noopener" target="_blank">Amir Belder</a>. We had a great chat about his paper “<a href="https://arxiv.org/abs/2202.07453">Random Walks for Adversarial Meshes</a>”, published in SIGGRAPH 2022. </p>
<p>In this paper, they take on the task of creating an adversarial attack for triangle meshes. This is a non-trivial task since meshes are irregular. To solve the irregularity they use random walks instead of the raw mesh. On top of that, they trained an imitating network that mimics the predictions of the attacked network and used the gradients to perturb the input points. </p>
<p></p>
<p>Amir is currently a PhD student at the <a href="https://cgm.technion.ac.il/" rel="noreferrer noopener" target="_blank">Computer Graphics and Multimedia Lab at the Technion Israel Institute of Technology</a>.  His research focus is on computer graphics and geometric processing and machine learning. We spend a lot of time together at the lab and chat often about science, papers and where the field is headed. Having this paper published was a great opportunity to share one of these conversations with you.</p>
<p></p>
<p></p>
<div id="buzzsprout-player-11869506">{% endraw %}
</div><script charset="utf-8" src="https://www.buzzsprout.com/1914034/11869506-random-walks-for-adversarial-meshes-amir-belder.js?container_id=buzzsprout-player-11869506&amp;player=small" type="text/javascript"></script>
<h2 class="wp-block-heading" id="authors">AUTHORS</h2>
<p>Amir Belder<a href="https://dl.acm.org/profile/99660532511"></a>, Gal Yefet<a href="https://dl.acm.org/profile/99660533514"></a>, Ran Ben-Itzhak<a href="https://dl.acm.org/profile/99660533358"></a>, Ayellet Tal<a href="https://dl.acm.org/profile/81100507022"></a></p>
<p><br/></p>
<h2 class="wp-block-heading" id="abstract">ABSTRACT</h2>
<p> </p>
<p>Neural implicit fields have recently emerged as a useful representation for 3D shapes. These fields are We A polygonal mesh is the most-commonly used representation of surfaces in computer graphics. Therefore, it is not surprising that a number of mesh classification networks have recently been proposed. However, while adversarial attacks are wildly researched in 2D, the field of adversarial meshes is under explored. This paper proposes a novel, unified, and general adversarial attack, which leads to misclassification of several state-of-the-art mesh classification neural networks. Our attack approach is black-box, i.e. it has access only to the network’s predictions, but not to the network’s full architecture or gradients. The key idea is to train a network to imitate a given classification network. This is done by utilizing random walks along the mesh surface, which gather geometric information. These walks provide insight onto the regions of the mesh that are important for the correct prediction of the given classification network. These mesh regions are then modified more than other regions in order to attack the network in a manner that is barely visible to the naked eye.</p>
<p> </p>
<p></p>
<h2 class="wp-block-heading" id="related-papers">RELATED (WORKS|PAPERS)</h2>
<p>📚<a href="https://arxiv.org/abs/1412.6572" rel="noreferrer noopener" target="_blank">Explaining and Harnessing Adversarial Examples</a></p>
<p>📚</p>
<p><br/></p>
<p></p>
<h2 class="wp-block-heading">LINKS AND RESOURCES</h2>
<p>📚 <a href="https://arxiv.org/abs/2202.07453">Paper</a></p>
<p>💻<a href="https://github.com/amirbelder/Random-Walks-for-Adversarial-Meshes">Code</a></p>
<p></p>
<p></p>
<p>To stay up to date with Amir’s latest research, follow him on:</p>
<p>🐦<a href="https://twitter.com/amir_belder" rel="noreferrer noopener" target="_blank">Twitter</a></p>
<p>👨🏻‍🎓<a href="https://scholar.google.com/citations?user=d30gRrcAAAAJ&amp;hl=en&amp;oi=ao" rel="noreferrer noopener" target="_blank">Google Scholar</a></p>
<p>👨🏻‍🎓<a href="https://www.linkedin.com/in/amir-belder-89889b103/">LinkedI</a><a href="https://www.linkedin.com/in/silvia-gonzalez-sellan-870525189/">n</a></p>
<p></p>
<p></p>
<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" style="border: none;" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/pzWFE6F-4bI?feature=oembed" title="Random Walks for Adversarial Meshes (SIGGRAPH 2022) with Amir Belder on Talking papers" width="800"></iframe>
</div></figure>
<p>Recorded on November 23rd 2022.</p>
<h2 class="wp-block-heading"><br/>CONTACT</h2>
<p>If you would like to be a guest, sponsor or share your thoughts, feel free to reach out via email: <a class="__cf_email__" data-cfemail="3145505d5a585f561f4150415443421f415e555250424571565c50585d1f525e5c" href="/cdn-cgi/l/email-protection">[email protected]</a></p>
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