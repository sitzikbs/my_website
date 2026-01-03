---
layout: layouts/blog-post.njk
title: "First Steps in Deep Learning Using TensorFlow"
date: 2018-02-11
author: Itzik Ben-Shabat
permalink: "/blog/posts/2018-02-11-first-steps-deep-learning-using-tensorflow.html"
---

<div class="post-content">


<p>In the past year, there was this phrase that kept popping up everywhere – “Deep learning”. It created the impression that you can do everything with it. Therefore, I have decided to investigate that the fuss is all about.</p>
<p>My first steps (which I recommend for any beginner) were understanding the science behind the magic. Here are several resources which I found helpful (this list will update from time to time):</p>
<ul>
<li><a href="https://www.youtube.com/playlist?list=PLrAXtmErZgOfMuxkACrYnD2fTgbzk2THW" rel="noopener" target="_blank">Deep Learning School 2016 </a>(YouTube videos of individual talks)</li>
<li><a href="https://www.youtube.com/playlist?list=PL6Xpj9I5qXYEcOhn7TqghAJ6NAPrNmUBH" rel="noopener" target="_blank">Neural Network Class</a> (YouTube videos by <a href="http://www.dmi.usherb.ca/~larocheh/index_en.html" rel="noopener" target="_blank">Hugo Larochelle</a> )</li>
<li><a href="https://www.udacity.com/course/deep-learning--ud730" rel="noopener" target="_blank">Udacity – Deep Learning by Google </a>(Videos and assignments)</li>
<li><a href="https://www.coursera.org/learn/neural-networks/" rel="noopener" target="_blank">Coursera – Neural Networks for Machine Learning</a> (Taught by the godfather of NNs Geoffrey Hinton)</li>
</ul>
<p>Update 16.2.17 : Additional resources (Thanks to <a href="https://www.linkedin.com/in/elad-osherov-8181753a/" rel="noopener" target="_blank">Elad Osherov</a>)</p>
<ul>
<li><a href="https://www.youtube.com/playlist?list=PLE6Wd9FR--EfW8dtjAuPoTuPcqmOV53Fu" rel="noopener" target="_blank">Deep Learning at Oxford 2015</a> (by Nando de Freitas, includes <a href="https://www.cs.ox.ac.uk/people/nando.defreitas/machinelearning/" rel="noopener" target="_blank">exercises</a>)</li>
<li><a href="https://www.youtube.com/playlist?list=PLkt2uSq6rBVctENoVBg1TpCC7OQi31AlC" rel="noopener" target="_blank">CS231n: Convolutional Neural Networks for Visual Recognition</a> (Stanford, including <a href="http://cs231n.stanford.edu/" rel="noopener" target="_blank">materials</a>)</li>
<li>CS 4476 / 6476 Computer Vision (James Hays)</li>
</ul>
<p>When I felt that I had a better understanding of this “magic” I immediately wanted to apply it to my engineering problems – a relatively unharvested field of research. I found (based on recommendations from several colleagues) that the best tool for implementation would be to use Google’s <a href="https://www.tensorflow.org/" rel="noopener" target="_blank">TensorFlow</a> with <a href="https://www.python.org/" rel="noopener" target="_blank">Python</a>.</p>
<p> </p>
<p>{% responsiveImage "assets/images/blog/TensorFlow-Logo.png", "TensorFlow logo - Library includes Neural Network tools" %}
</p>
<p> </p>
<p>Confession: I have not worked with python before + I work on a windows machine.</p>
<p>However, learning python for an experienced programmer like myself proved to be relatively easy (once you get used to all of these indentations instead of brackets) and setting it up on a windows machine took a few hours (TensorFlow currently supports python 3.5 on windows machines so I had to <a href="https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/" rel="noopener" target="_blank">create a virtual environment</a> on my anaconda ).</p>
<p>After doing all of this it was time to start programming!</p>
<p>I recommend starting with the <a href="https://www.tensorflow.org/tutorials/" rel="noopener" target="_blank">TensorFlow Tutorials</a>. They are very well explained and very easy for a beginner.</p>
<p>I started with the <a href="https://www.tensorflow.org/tutorials/mnist/beginners/" rel="noopener" target="_blank">MNIST for ML beginners tutorial. </a></p>
<p>Here is my final code (Detailed explanations are given in the tutorial):</p>
<pre><code class="language-python">import tensorflow as tf

#Get the Data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

x = tf.placeholder(tf.float32,[None, 784])

W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax( tf.matmul(x,W) + b )

y_ = tf.placeholder( tf.float32, [None, 10] )
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y, y_))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for i in range(1000):
   batch_xs, batch_ys = mnist.train.next_batch(100)
   sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_predictions = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))

test_Accuracy = sess.run(accuracy,feed_dict={x: mnist.test.images, y_: mnist.test.labels})
print(test_Accuracy)
</code></pre>
<p>It gets approximately 92% accuracy. It is pretty bad for MNIST but we used a very simple model. in the next tutorial (and post) I’m going to use a deep convolutional network to improve this result.</p>
<p>In the next tutorial (and post) I’m going to use a deep convolutional network to improve this result.</p>
 

</div>