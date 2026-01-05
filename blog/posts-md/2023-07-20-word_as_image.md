---
layout: layouts/blog-post.njk
title: "Word-As-Image for Semantic Typography"
date: 2023-07-20
author: Itzik Ben-Shabat
permalink: "/blog/posts/2023-07-20-word_as_image.html"
---

<div class="post-content">
{% raw %}




<p>In this episode of the <a href="https://www.itzikbs.com/the-talking-papers-podcast" rel="noreferrer noopener" target="_blank">Talking Papers Podcast</a>, I hosted Shir Iluz. We had a great chat about her paper “<a href="https://wordasimage.github.io/Word-As-Image-Page/" rel="noreferrer noopener" target="_blank">Word-As-Image for Semantic Typography</a>”, SIGGRAPH 2023 Honorable Mention award winner. </p>
<p>This scientific paper presents an innovative approach for text morphing based on semantic context. The authors demonstrate how they transform an input word, such as “bunny,” into a visually striking representation where each letter takes on the appearance of a bunny. To achieve this, they leverage a bezier curve representation with control points, which is subsequently processed through a rasterizer and a vector diffusion model. This optimization-based approach ensures that the semantics of the word are accurately imposed on the letter shapes. Balancing between readability and semantics is a non-trivial task, and the authors address this by formulating multiple loss functions. These loss functions act as “control knobs,” enabling users to fine-tune the final results, either prioritizing enhanced readability or maximizing semantic meaningfulness. The paper’s compelling results are complemented by an impressive demo, which showcases the transformative capabilities of their methodDon’t miss the amazing <a href="https://huggingface.co/spaces/SemanticTypography/Word-As-Image" rel="noreferrer noopener" target="_blank">demo </a>they created.</p>
<p></p>
<p>Shir, a dedicated Masters student at Tel Aviv University, has embarked on a groundbreaking project in collaboration with Yael Vinker, both making equal contributions to this remarkable endeavor. You may know Yael from her prior appearance as a guest on the podcast (<a href="https://www.itzikbs.com/clipasso" rel="noreferrer noopener" target="_blank">CLIPasso episode</a>). Their work carries immense potential, promising to revolutionize the creative processes of artists and designers. Rather than commencing from a traditional blank canvas or plain font, this innovative approach enables individuals to initiate their logo design journey by transforming a word into a captivating image. The implications of this novel technique hold the power to reshape the very workflow of artistic expression, opening up exciting new possibilities for visual communication and design aesthetics.</p>
<p>I am eagerly anticipating the next set of papers she will sketch out (pun intended).</p>
<p><br/>Check out this result for the word “Podcast” with the semantic context of “Headphones”. I like it. </p>
<div class="wp-block-image"><figure class="aligncenter size-full">{% endraw %}
{% responsiveImage "../../assets/images/blog/LuckiestGuy-Regular_PODCAST_A.png", "" %}
{% raw %}


</figure>{% endraw %}
</div>
<div id="buzzsprout-player-13251083"></div><script charset="utf-8" src="https://www.buzzsprout.com/1914034/13251083-word-as-image-shir-iluz.js?container_id=buzzsprout-player-13251083&amp;player=small" type="text/javascript"></script>
<h2 class="wp-block-heading" id="authors">AUTHORS</h2>
<p>Shir Iluz<em>, Yael Vinker</em>, Amir Hertz, Daniel Berio, Daniel Cohen-Or, Ariel Shamir<br/></p>
<h2 class="wp-block-heading" id="abstract">ABSTRACT</h2>
<p> </p>
<p>Abstraction is at the heart of sketching due to the simple and minimal nature of line drawings. Abstraction entails identifying the essential visual properties of an object or scene, which requires semantic understanding and prior knowledge of high-level concepts. Abstract depictions are therefore </p>
<blockquote class="wp-block-quote is-layout-flow wp-block-quote-is-layout-flow"><p>A word-as-image is a semantic typography technique where a word illustration presents a visualization of the meaning of the word, while also preserving its readability. We present a method to create word-as-image illustrations automatically. This task is highly challenging as it requires semantic understanding of the word and a creative idea of where and how to depict these semantics in a visually pleasing and legible manner. We rely on the remarkable ability of recent large pretrained language-vision models to distill textual concepts visually. We target simple, concise, black-and-white designs that convey the semantics clearly. We deliberately do not change the color or texture of the letters and do not use embellishments. Our method optimizes the outline of each letter to convey the desired concept, guided by a pretrained Stable Diffusion model. We incorporate additional loss terms to ensure the legibility of the text and the preservation of the style of the font. We show high quality and engaging results on numerous examples and compare to alternative techniques.</p></blockquote>
<p> </p>
<p></p>
<h2 class="wp-block-heading" id="related-papers">RELATED (WORKS|PAPERS)</h2>
<p>📚<a href="https://openaccess.thecvf.com/content/CVPR2023/html/Jain_VectorFusion_Text-to-SVG_by_Abstracting_Pixel-Based_Diffusion_Models_CVPR_2023_paper.html" rel="noreferrer noopener" target="_blank">VectorFusion</a></p>
<p></p>
<p></p>
<h2 class="wp-block-heading">LINKS AND RESOURCES</h2>
<p>📚 <a href="https://arxiv.org/pdf/2303.01818.pdf" rel="noreferrer noopener" target="_blank">Paper</a></p>
<p>💻<a href="https://wordasimage.github.io/Word-As-Image-Page/" rel="noreferrer noopener" target="_blank">Project page</a></p>
<p>💻<a href="https://huggingface.co/spaces/SemanticTypography/Word-As-Image" rel="noreferrer noopener" target="_blank">Demo</a></p>
<p>💻<a href="https://github.com/Shiriluz/Word-As-Image" rel="noreferrer noopener" target="_blank">Code</a></p>
<p></p>
<p>To stay up to date with their latest research, follow on:</p>
<p>🐦<a href="https://twitter.com/IluzShir" rel="noreferrer noopener" target="_blank">Twitter</a></p>
<p>👨🏻‍🎓<a href="https://www.linkedin.com/in/shiriluz/" rel="noreferrer noopener" target="_blank">LinkedIn</a></p>
<p></p>
<p></p>
<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="450" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/hej_Yw4SbTA?feature=oembed" title="Word-As-Image (SIGRAPH 2023) with Shir Iluz on Talking papers" width="800"></iframe>
</div></figure>
<p>Recorded on July 11st 2023.</p>
<p><br/><br/>CONTACT</p>
<p>If you would like to be a guest, sponsor or share your thoughts, feel free to reach out via email: <a class="__cf_email__" data-cfemail="b2c6d3ded9dbdcd59cc2d3c2d7c0c19cc2ddd6d1d3c1c6f2d5dfd3dbde9cd1dddf" href="/cdn-cgi/l/email-protection">[email protected]</a></p>
<p></p>
<h2 class="wp-block-heading">SUBSCRIBE AND FOLLOW</h2>
<p>🎧Subscribe on your favourite podcast app: <a href="/podcast/" rel="noreferrer noopener" target="_blank">/podcast/</a></p>
<p>📧Subscribe to our mailing list: <a href="http://eepurl.com/hRznqb" rel="noreferrer noopener" target="_blank">http://eepurl.com/hRznqb</a></p>
<p>🐦Follow us on Twitter: <a href="https://twitter.com/talking_papers" rel="noreferrer noopener" target="_blank">https://twitter.com/talking_papers</a></p>
<p>🎥YouTube Channel: </p>
<p></p>
<p></p>
<p></p>
 

</div>