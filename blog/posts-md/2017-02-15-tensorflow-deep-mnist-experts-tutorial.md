---
layout: layouts/blog-post.njk
title: "TensorFlow – Deep MNIST for Experts tutorial"
date: "2017-02-15"
author: Itzik Ben-Shabat
permalink: "/blog/posts/2017-02-16-tensorflow-deep-mnist-experts-tutorial.html"
---

<div class="post-content">


<p>The second step in my quest for deep learning for 3D point clouds was to try recognizing MNIST digits using a deep convolutional network (The first step can be found <a href="https://www.itzikbs.com/first-steps-deep-learning-using-tensorflow" target="_blank">here</a>).</p>
<p>I followed<a href="https://www.tensorflow.org/tutorials/mnist/pros/" target="_blank"> google’s tutorial</a>. I found it very well explained. My final code can be downloaded <a href="https://github.com/sitzikbs/TensorFlow-Tutorials/blob/master/MNIST4ExpertsNoExport.py" target="_blank">here</a>.</p>
<p>Using this code I managed to get a recognition accuracy of about 99.2%.</p>
<p>However, the accuracy wasn’t the thing that troubled me the most. At this point, I realized there are several things I wish to know how to do</p>
<ol>
<li>Export/import the final model</li>
<li>Track the training progress</li>
<li>Visualize the neural net</li>
</ol>
<p>For these tasks, I did not find a single good tutorial. Therefore I decided to summarize my findings. In this post, I will cover export/import the final model and the other two will be covered in future posts.</p>
<p><strong>Export the final model </strong></p>
<p>It turns out that exporting the model is rather simple. It requires about 3 lines of code:<br/>
Two lines before the training loop</p>
<pre><code class="language-python">saver = tf.train.Saver(max_to_keep=3)
CeckPointFilename = "path to where you wish to save the checkpoints"
</code></pre>
<p>I defined to keep the model of the last 3 training iteration (more precisely 300 iterations because I saved once every 100 iterations) because there are a lot of these files and I don’t want it to take too much memory on my hard drive.</p>
<p>Another line in the training loop (or after it, depends if you want the final model or several models throughout the training process):</p>
<pre><code class="language-python">saver.save(sess, CeckPointFilename , global_step = i )
</code></pre>
<p>However, this turned out to be not quite enough. If we wish to make use of our model we should also insert the input and output into a collection so we can use them once the model is restored.</p>
<pre><code class="language-python">tf.add_to_collection("keep_prob", keep_prob)
tf.add_to_collection("x", x)
tf.add_to_collection("y_", y_)
tf.add_to_collection("y_conv", y_conv)
</code></pre>
<p><strong>Loading the model</strong></p>
<p>I found <a href="http://stackoverflow.com/questions/33759623/tensorflow-how-to-restore-a-previously-saved-model-python" target="_blank">this </a>Stack-overflow thread useful. It referenced <a href="https://www.tensorflow.org/api_docs/python/state_ops/exporting_and_importing_meta_graphs" target="_blank">this </a>Tensorflow documentation.</p>
<p>In order to load the model you should change the following lines of code to include the name and path to your model.</p>
<pre><code class="language-python">sess = tf.Session()
new_saver = tf.train.import_meta_graph("PathToModelDir/ModelName.meta")
new_saver.restore(sess, "PathToModelDir/ModelName")
</code></pre>
<p>Once you imported the model you can extract the input and output which we added to the collection</p>
<pre><code class="language-python">y_conv = tf.get_collection("y_conv")[0]
x = tf.get_collection("x")[0]
y_ = tf.get_collection("y_")[0]
keep_prob =  tf.get_collection("keep_prob")[0]
</code></pre>
<p>Now we just need to apply the model to an input image and make a class prediction</p>
<pre><code class="language-python">ImageIndex = 3
InputImage = mnist.test.images[ImageIndex].reshape(1,784)
CorrectLabel = mnist.test.labels[ImageIndex].reshape(1,10)

logit = sess.run(y_conv,feed_dict={ x: InputImage, y_: CorrectLabel, keep_prob: 1.0})
prediction = sess.run(tf.argmax(logit,1))
digit = sess.run(tf.argmax(CorrectLabel,1))
print("Prediction : %d, Actual : %d"% (prediction, digit))
</code></pre>
<p>I’m not sure if this is the best way of doing this but it works. The final version (with exporting) can be found <a href="https://github.com/sitzikbs/TensorFlow-Tutorials/blob/master/MNIST4Experts.py" target="_blank">here</a> and the importing code can be found <a href="https://github.com/sitzikbs/TensorFlow-Tutorials/blob/master/ImportModel.py" target="_blank">here</a>.</p>
 

</div>