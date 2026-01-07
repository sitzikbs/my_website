---
layout: layouts/blog-post.njk
title: "SampleNet: Differentiable Point Cloud Sampling"
date: 2022-07-18
author: Itzik Ben-Shabat
permalink: "/blog/posts/2022-07-18-samplenet-differentiable-point-cloud-sampling.html"
---

<div class="post-content">
{% raw %}




<p>In this episode of the <a href="https://www.itzikbs.com/the-talking-papers-podcast" rel="noreferrer noopener" target="_blank">Talking Papers Podcast</a>, I hosted <em><a href="http://manuel-dahnert.com/" rel="noreferrer noopener" target="_blank">Itai Lang</a></em> to chat about his paper “SampleNet: Differentiable Point Cloud Sampling”, published in CVPR 2020. </p>
<p>In this paper, they propose a point soft-projection to allow differentiating through the sampling operation and enable learning task-specific point sampling. Combined with their regularization and task-specific losses, they can reduce the number of points to 3% of the original samples with a very low impact on task performance. </p>
<p>I met Itai for the first time <a href="https://www.itzikbs.com/cvpr-2019" rel="noreferrer noopener" target="_blank">at CVPR 2019</a>.  Being a point-cloud guy myself, I have been following his research work ever since. It is amazing how much progress he has made and I can’t wait to see what he comes up with next. It was a pleasure hosting him on the podcast. </p>
<div id="buzzsprout-player-10330506">{% endraw %}
</div><script charset="utf-8" src="https://www.buzzsprout.com/1914034/10330506-itai-lang-samplenet.js?container_id=buzzsprout-player-10330506&amp;player=small" type="text/javascript"></script>
<h2 class="wp-block-heading" id="authors">AUTHORS</h2>
<p id="stephen-gould-richard-hartleydylan-campbell"><em>Itai Lang, Asaf Manor, Shai Avidan</em></p>
<p> </p>
<h2 class="wp-block-heading" id="abstract">ABSTRACT</h2>
<p>There is a growing number of tasks that work directly on point clouds. As the size of the point cloud grows, so do the computational demands of these tasks. A possible solution is to sample the point cloud first. Classic sampling approaches, such as farthest point sampling (FPS), do not consider the downstream task. A recent work showed that learning a task-specific sampling can improve results significantly. However, the proposed technique did not deal with the non-differentiability of the sampling operation and offered a workaround instead. We introduce a novel differentiable relaxation for point cloud sampling that approximates sampled points as a mixture of points in the primary input cloud. Our approximation scheme leads to consistently good results on classification and geometry reconstruction applications. We also show that the proposed sampling method can be used as a front to a point cloud registration network. This is a challenging task since sampling must be consistent across two different point clouds for a shared downstream task. In all cases, our approach outperforms existing non-learned and learned sampling alternatives. Our code is publicly available.</p>
<p> </p>
<h2 class="wp-block-heading" id="related-papers">RELATED (WORKS|PAPERS)</h2>
<p>📚 <a href="https://openaccess.thecvf.com/content_CVPR_2019/html/Dovrat_Learning_to_Sample_CVPR_2019_paper.html">Learning to Sample</a></p>
<p>📚 </p>
<h2 class="wp-block-heading">LINKS AND RESOURCES</h2>
<p>💻</p>
<p>📚 </p>
<p></p>
<p></p>
<p>To stay up to date with Itai’s latest research, follow him on:</p>
<p>🎓</p>
<p>🐦<a href="https://twitter.com/ItaiLang">Twitte</a><a href="https://twitter.com/ItaiLang" rel="noreferrer noopener" target="_blank">r</a></p>
<p></p>
<p></p>
<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" style="border: none;" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/NgpYkumkTAc?feature=oembed" title="SampleNet : Differentiable Point Cloud Sampling -  Itai Lang on the Talking Papers Podcast" width="800"></iframe>
</div></figure>
<p>Recorded on February 15th 2022.</p>
<h2 class="wp-block-heading"><br/>CONTACT</h2>
<p>If you would like to be a guest, sponsor or just share your thoughts, feel free to reach out via email: <a class="__cf_email__" data-cfemail="e99d88858280878ec79988998c9b9ac799868d8a889a9da98e84888085c78a8684" href="/cdn-cgi/l/email-protection">[email protected]</a></p>
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