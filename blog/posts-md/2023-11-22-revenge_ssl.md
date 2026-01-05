---
layout: layouts/blog-post.njk
title: "Reverse Engineering Self-Supervised Learning"
date: 2023-11-22
author: Itzik Ben-Shabat
permalink: "/blog/posts/2023-11-22-revenge_ssl.html"
---

<div class="post-content">
{% raw %}




<div id="buzzsprout-player-14009896">{% endraw %}
</div><script charset="utf-8" src="https://www.buzzsprout.com/1914034/14009896.js?container_id=buzzsprout-player-14009896&amp;player=small" type="text/javascript"></script>
<p>In the latest episode of the Talking Papers Podcast, I had the pleasure of hosting Ravid Shwartz-Ziv, a brilliant early career academic, to discuss his recent research paper titled “Reverse Engineering Self-Supervised Learning,” which was published at NeurIPS 2023. Coming from a background in machine learning, I was particularly excited about this paper as it delves into understanding the mechanisms and representations learned through self-supervised learning (SSL).</p>
<p>The paper presents an extensive empirical analysis of SSL-trained representations, exploring different models, architectures, and hyperparameters. One of the intriguing findings is that SSL inherently facilitates the clustering of samples based on semantic labels, driven by the regularization term of the SSL objective. This clustering process not only enhances downstream classification but also showcases the compression power of SSL-trained representations. Additionally, the study establishes that these representations align more closely with semantic classes as compared to random classes, across various hierarchical levels. Importantly, this alignment increases during training and as the network goes deeper.</p>
<p>What makes this paper unique is that it focuses on understanding the semantic clustering effect of SSL methods rather than solely showcasing superior performance on benchmark datasets. This deeper exploration provides valuable insights into the representation learning mechanisms of SSL and their impact on performance with different sets of classes. Furthermore, it highlights the potential for compression in SSL representations, which can have significant implications in practical applications.</p>
<p>During our conversation, Ravid and I shared a connection as colleagues in the field, both based in Israel. Interestingly, despite our proximity, we had never met in person. This paper falls into a genre that I personally find fascinating, as it seeks to comprehend the underlying capabilities of the tools we commonly employ. Ravid’s work and dedication as a CDS Faculty Fellow at NYU Center for Data Science are evident in his research, and I am truly excited to see what future insights his endeavors will bring.</p>
<p>To stay updated on our latest podcast episodes and discussions on cutting-edge research papers like this, make sure to tune in to the Talking Papers Podcast. Join the conversation by using the hashtag #TalkingPapersPodcast.</p>
<h2 class="wp-block-heading">AUTHORS</h2>
<p><br/>Ido Ben-Shaul, Ravid Shwartz-Ziv, Tomer Galanti, Shai Dekel, Yann LeCun</p>
<h2 class="wp-block-heading">ABSTRACT</h2>
<p><br/>Self-supervised learning (SSL) is a powerful tool in machine learning, but understanding the learned representations and their underlying mechanisms remains a challenge. This paper presents an in-depth empirical analysis of SSL-trained representations, encompassing diverse models, architectures, and hyperparameters. Our study reveals an intriguing aspect of the SSL training process it inherently facilitates the clustering of samples with respect to semantic labels, which is surprisingly driven by the SSL objective’s regularization term. This clustering process not only enhances downstream classification but also compresses the data information. Furthermore, we establish that SSL-trained representations align more closely with semantic classes rather than random classes. Remarkably, we show that learned representations align with semantic classes across various hierarchical levels, and this alignment increases during training and when moving deeper into the network. Our findings provide valuable insights into SSL’s representation learning mechanisms and their impact on performance across different sets of classes.</p>
<h2 class="wp-block-heading">RELATED (WORKS|PAPERS)</h2>
<p>📚<a href="https://arxiv.org/abs/2002.05709" rel="noreferrer noopener" target="_blank">SimCLR</a></p>
<p>📚<a href="https://arxiv.org/abs/2105.04906" rel="noreferrer noopener" target="_blank">VICReg</a></p>
<p>📚<a href="https://www.pnas.org/doi/abs/10.1073/pnas.2015509117x" rel="noreferrer noopener" target="_blank">Prevalence of neural collapse</a></p>
<h2 class="wp-block-heading">LINKS AND RESOURCES</h2>
<p>📚<a href="https://arxiv.org/abs/2305.15614" rel="noreferrer noopener" target="_blank">Preprint</a></p>
<p>To stay up to date with his latest research, follow on:</p>
<p>👨🏻‍🎓<a href="https://www.ravid-shwartz-ziv.com/" rel="noreferrer noopener" target="_blank">Personal website</a></p>
<p>👨🏻‍🎓<a href="https://scholar.google.co.uk/citations?view_op=list_works&amp;hl=en&amp;hl=en&amp;user=SqsLFwMAAAAJ" rel="noreferrer noopener" target="_blank">Google scholar</a></p>
<p>🐦<a href="https://twitter.com/ziv_ravid" rel="noreferrer noopener" target="_blank">Twitter</a></p>
<p>👨🏻‍🎓<a href="https://www.linkedin.com/in/ravid-shwartz-ziv-8bb18761/" rel="noreferrer noopener" target="_blank">LinkedIn</a></p>
<figure class="wp-block-embed is-type-rich is-provider-embed-handler wp-block-embed-embed-handler wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/jdr-AL-CbWk?feature=oembed" title="Reverse Engineering SSL (NeurIPS 2023) with Ravid Shwartz-Ziv on Talking Papers Podcast" width="800"></iframe>
</div></figure>
<p>This episode was recorded on October 30th 2023</p>
<h2 class="wp-block-heading">CONTACT</h2>
<p><br/>If you would like to be a guest, sponsor or share your thoughts, feel free to reach out via email: <a class="__cf_email__" data-cfemail="98ecf9f4f3f1f6ffb6e8f9e8fdeaebb6e8f7fcfbf9ebecd8fff5f9f1f4b6fbf7f5" href="/cdn-cgi/l/email-protection">[email protected]</a></p>
<h2 class="wp-block-heading">SUBSCRIBE AND FOLLOW</h2>
<p><br/>🎧Subscribe on your favourite <a href="/podcast/" rel="noreferrer noopener" target="_blank">podcast app</a></p>
<p>📧Subscribe to our <a href="http://eepurl.com/hRznqb" rel="noreferrer noopener" target="_blank">mailing list</a></p>
<p>🐦Follow us on <a href="https://twitter.com/talking_papers" rel="noreferrer noopener" target="_blank">Twitter</a></p>
<p>🎥Subscribe to our </p>
 

</div>