---
layout: layouts/blog-post.njk
title: "How to write a paper using LaTeX"
date: 2018-09-08
author: Itzik Ben-Shabat
permalink: "/blog/posts/2018-09-08-write-paper-using-latex.html"
---

<div class="post-content">


<p>*<strong>UPDATE</strong> (8.9.18)  – I recently discovered a wonderful online LaTex writing tool called <a href="https://www.overleaf.com/" rel="noopener" target="_blank">overleaf.</a> I strongly recommend it over TeXMaker (presented below). It offers a nice and clean user interface along with a great platform for collaborating with coauthors which includes change tracking,  .git, and more. Nonetheless, the template provided here can be uploaded and used there as well. Here is a <a href="https://www.overleaf.com/signup?ref=1cc2f114ccdf" rel="noopener" target="_blank">registration link to overleaf</a>.</p>
<p> </p>
<p>Getting started with LaTeX can be a little discouraging. LaTeX has a learning curve, but, its totally worth the effort!</p>
<p>This post contains some tips and tricks for LaTeX beginners and will help you write your first paper using LaTeX.</p>
<p><a href="#the_gist_latex"> Skip to the gist </a> at the bottom of the page for the download links without detail.</p>
<p> </p>
<h2>Step 0:  The TeX distribution</h2>
<p>If you are working on windows (like me) you need to install a TeX distribution (like<a href="https://miktex.org/download" rel="noopener"> MiKTeX</a>) first .  The editor is used to create and edit the TeX code, while the TeX distribution is used to compile and create the pdf file.</p>
<p>So install <a href="https://miktex.org/download" rel="noopener">MikTex</a>.  Make sure to do this before you install the editor. This way you won’t have to worry about configuring the editor to use it.</p>
<p> </p>
<h2>Step 1:  The editor</h2>
<p>I work with <a href="http://www.xm1math.net/texmaker/download.html" rel="noopener">Texmaker.</a>  I found that it has some great customization features That I really like.</p>
<p>So, install <a href="http://www.xm1math.net/texmaker/download.html" rel="noopener">Texmaker</a>.</p>
<p>After you install it I recommend doing the following:</p>
<ol>
<li>Create a build subdirectory automatically:  Options -&gt; Configure Texmaker – &gt;  check the box “use a “build” subdirectory for output files”.   When you compile a TeX file it creates the pdf file but it also creates some other files and it becomes a mess very fast. working with a build subdirectory will automatically put the pdf (and the other files) there.{% responsiveImage "assets/images/blog/built_in_option.jpg", "" %}
</li>
<li>Built-in pdf viewer:  If you are working with one screen you will find the embedded built-in viewer very efficient. If you are working with two screens (like me) then make sure that the “embed” checkbox is unchecked and drag the viewer window to the secondary screen.<br/>
{% responsiveImage "assets/images/blog/pdf_viewer-300x164.jpg", "" %}
</li>
<li>External viewer: If you want to preview your pdf using an external viewer, and you followed step 1, you need to change the external viewer path to ” “Path to your viewer” .\build\%.pdf”. I use Adobe pdf reader so for me its :   “C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe” .\build\%.pdf. Just remember to close it before you recompile the document (you will get an error unless you use a reader that allows updates and refreshes)<br/>
{% responsiveImage "assets/images/blog/built_in_viewer-300x123.jpg", "" %}
</li>
<li>Adjust font size:   options -&gt; Configure Texmaker,-&gt;  editor (on the left) -&gt;  editor font size. I like 11.</li>
</ol>
<h2>Step 2:  The Paper</h2>
<p>Now that you have everything set up you can start working on your paper.</p>
<p>Before you do, I highly recommend watching these<a href="https://www.youtube.com/watch?v=SoDv0qhyysQ&amp;list=PL1D4EAB31D3EBC449" rel="noopener"> youtube tutorials </a>by Michelle Krummel. It will help you understand the basics.</p>
<p>Now that you know the basics you can simply download <a href="/assets/images/blog/LaTeX-General-Template.zip" rel="noopener">this template</a> and read the following explanations without actually having to do anything.</p>
<ol>
<li>Download <a href="/assets/images/blog/LaTeX-General-Template.zip" rel="noopener">this template</a>.</li>
<li>Extract the template files into your working directory (keep the zip file for future papers).</li>
<li>Open “<em>main.tex</em>” in TexMaker.</li>
<li>Run a quick build.</li>
<li>BOOM ! Your first paper in LaTeX is ready! (assuming that you had no errors)</li>
</ol>
<p>Now let us try to understand what is going on in the template:</p>
<h2>The Preamble</h2>
<p>The preamble includes all lines  that come  before:</p>
<pre>\begin{document}</pre>
<p>In the preamble, you define many things.  Usually, you will define the type of document, which packages to use and other custom definitions.</p>
<p>The document class is defined by :</p>
<pre>\documentclass[10pt,twocolumn,letterpaper]{article}</pre>
<p>Here you can set the paper size, one or two columns, font syze etc.</p>
<p>I included some useful packages. There are surely more packages that you will need in the future but this will get you started.</p>
<h2>The document</h2>
<p>The document is whatever comes between</p>
<pre>\begin{document}</pre>
<p>and</p>
<pre>\end{document}</pre>
<p>You can basically start writing your entire document here.</p>
<p>I recommend working slightly differently and use separate files for the different sections.</p>
<h2>Sections</h2>
<p>Most papers have the same general structure (names may change according to the field and other sections may be added) :</p>
<ul>
<li>Abstract</li>
<li>Introduction</li>
<li>Related Work</li>
<li>Approach / Method</li>
<li>Results</li>
<li>Summary / Conclusion</li>
</ul>
<p>In the template, each section has its own .tex file inside the “<em>sections</em>” subdirectory.</p>
<p>The following lines basically insert these separate .tex files into the main document.</p>
<pre>\input{sections/abstract}
\input{sections/intro}
\input{sections/related-work}
\input{sections/approach}
\input{sections/results}
\input{sections/summary}</pre>
<p>In TexMaker you can see them on the left. Simply clicking them will open each file for editing.</p>
<p>If you want to be able to compile the main file (without having to go back to it each time you edit a section) you can simply choose the Options -&gt; Define current document as ‘Master Document’  option (make sure you are editing the main document when doing so).</p>
<h2>Assets</h2>
<p>Assets are valuable things (by definition). In our case, it usually refers to images and figures but can include any other type of file that your .tex file uses.  In the template, I created an assets folder. You can simply place all your images in it.</p>
<p>The line</p>
<pre>\graphicspath{{assets/}}</pre>
<p>makes sure that the compiler will know where to find our images.</p>
<h2>Figures and Tables</h2>
<p>To insert a figure into the document you can use :</p>
<pre>\begin{figure}
\centering
\includegraphics[width=0.5\linewidth]{test.jpg}
\caption{This is how you include an image}
\label{fig:approach} %always put label after caption
\end{figure}</pre>
<p>Here the image name is “<em>test.jpg</em>” (it is located inside the assets directory).  The label you give here is the string you will use in order to reference this figure in the text ( in this case its “fig:approach”).</p>
<p>I recommend adopting a labeling method that uses a colon between the type of element you want to reference and its description.  In this case “fig” is the type and stands for figure and “approach” is the image description (I use “sec” for sections, “eq” for equations and “table” for tables).</p>
<p>To reference this figure in the text  use</p>
<pre>\ref{fig:approach}</pre>
<p>TexMaker will help you with some autocomplete options so make sure to give short, yet meaningful descriptions.</p>
<p> </p>
<p>Tables are super important in scientific work and I must say that I find styling them super annoying in LaTeX.</p>
<p>To insert a table use the following code:</p>
<pre>    \begin{table}[t]
	\centering	
		\tabcolsep = 0.01\textwidth
		\begin{tabular}{| m{0.1\textwidth} | M{0.15\textwidth} | M{0.15\textwidth}|} 
			\hline
			\centering\textbf{Method} &amp; \textbf{Criterion 1} &amp; \textbf{Criterion 2}
 			\tabularnewline
 			\hline
 			Method 1 &amp; score 1 &amp; score 2 \\
 			Method 2 &amp; score 1 &amp; score 2 \\
 			Ours  &amp; The best &amp; The best \\
		    \hline
		\end{tabular}
	\caption{Example of a table }
	\label{table:example_table}
\end{table}</pre>
<p>Make sure that you have the following line in the preamble</p>
<pre>\newcolumntype{M}[1]{&gt;{\centering\arraybackslash}m{#1}}</pre>
<p>I won’t go into detail here. I refer the interested reader<a href="https://en.wikibooks.org/wiki/LaTeX/Tables" rel="noopener"> to this page</a>.</p>
<p>If you find yourself lost, you can try this <a href="https://www.tablesgenerator.com/" rel="noopener">online LaTeX table generator</a>.</p>
<h2>Math</h2>
<p>You will mostly insert math into the text using equations but sometimes you will want to insert math inline into the text.</p>
<p>For inline text, simply use the $ sign to open and close the math you wish to write, like this:</p>
<pre>$x^2 + y^2 + z^2 = R^2 $</pre>
<p>If you need a numbered equation then simply use:</p>
<pre>\begin{equation} \label{eq:circle}
x^2 + y^2 + z^2 = R^2
\end{equation}</pre>
<p>Here is a tip – if you have a really complicated equation and you are not a LaTeX Guru yet, you can use some software tools to help you get the code. I used MathType to style my equations and then exported the LaTeX code.  There are also some free online tools like <a href="http://www.sciweavers.org/free-online-latex-equation-editor" rel="noopener">this one.</a></p>
<h2>Footnotes</h2>
<p>I was working on a document with some collaborators and found that using tagged footnotes useful (though, not as good as review mode in Microsoft word). If a collaborator wants to write a comment regarding a specific region of the text you can simply create a tag for him using:</p>
<pre>\newcommand{\IBS}[1] {\footnote{Itzik: #1}}</pre>
<p>Now wherever you write</p>
<pre>\IBS{My footnote comment}</pre>
<p>You will get a footnote with your name followed by a colon in the beginning of the comment.</p>
<h2>References</h2>
<p>I use BibTex.</p>
<p>To insert the bibliography simply use</p>
<pre>\bibliographystyle{plain}
\bibliography{references}</pre>
<p>In your “<em>reference.bib</em>” file you place your references.</p>
<p>For example here is a citation of one of my papers :</p>
<pre>@article{ben2017graph,
title={Graph Based Over-Segmentation Methods for 3D Point Clouds}
author={Ben-Shabat, Yizhak and Avraham, Tamar and Lindenbaum, Michael and Fischer, Anath}
journal={arXiv preprint arXiv:1702.04114}
year={2017}
}</pre>
<p>To cite it in the text simply use:</p>
<pre>\cite{ben2017graph}</pre>
<p>I use google scholar a lot, you can get your citations from there by clicking cite (now its the ” symbol to the bottom left of each entry) and click BibTex to get the code. PAY ATTENTION – google scholar doesn’t get the citations right about 60% of the time. I had to manually edit a lot of references so make sure to do it for each entry as you insert it (and not when you finish the paper because it is very tedious).</p>
<h2>Step 3:  Becoming a LaTeX Guru</h2>
<p>Well, I just recently started so I am still working on this step. I think that the best way to do this is simply to use LaTeX a lot.</p>
<p>If you find yourself stuck trying to do something simple (which in the beginning happens very often) I recommend the following helpful links:</p>
<ul>
<li><a href="https://tex.stackexchange.com/" rel="noopener">LaTeX stack exchange </a>– ask a question and you will get an answer (just, read the rules first).</li>
<li><a href="https://en.wikibooks.org/wiki/LaTeX" rel="noopener" target="_blank">LaTeX Wikibook</a> – A general guide to LaTeX markup language.</li>
<li><a href="https://www.sharelatex.com/learn" rel="noopener">https://www.sharelatex.com/learn</a> – great detailed explanations and code.</li>
<li><a href="https://www.youtube.com/watch?v=SoDv0qhyysQ&amp;list=PL1D4EAB31D3EBC449" rel="noopener">Michelle Krummel youtube tutorials</a></li>
</ul>
<p> </p>
<h2 id="the_gist_latex">The Gist</h2>
<p>If you already read everything or just want the important links without having to scroll through. I summarized it here:</p>
<ul>
<li>Install <a href="https://miktex.org/download" rel="noopener" target="_blank">MiKTeX.</a></li>
<li>Install <a href="http://www.xm1math.net/texmaker/download.html" rel="noopener" target="_blank">TexMaker.</a></li>
<li>Download the <a href="/assets/images/blog/LaTeX-General-Template.zip" rel="noopener" target="_blank">template</a>.</li>
<li>Good luck!</li>
</ul>
 

</div>