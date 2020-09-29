<h1 class="gap">0x09. Python - Everything is object</h1>
 <article id="description" class="gap formatted-content">
    <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/252/r_208403_QPSN8.jpg" alt="" style="" /><br /></p>

<h2>Background Context</h2>

<p>Now that we understand that everything is an object and have a little bit of knowledge, let&rsquo;s pause and look a little bit closer at how Python works with different types of objects.</p>

<p>BTW, have you ever modified a variable without knowing it or wanting to? I mean:</p>

<pre><code>&gt;&gt;&gt; a = 1
&gt;&gt;&gt; b = a
&gt;&gt;&gt; a = 2
&gt;&gt;&gt; b
1
&gt;&gt;&gt; 
</code></pre>

<p>OK. But what about this?</p>

<pre><code>&gt;&gt;&gt; l = [1, 2, 3]
&gt;&gt;&gt; m = l
&gt;&gt;&gt; l[0] = &#39;x&#39;
&gt;&gt;&gt; m
[&#39;x&#39;, 2, 3]
&gt;&gt;&gt; 
</code></pre>

<p><img src="https://media.giphy.com/media/wAjfQ9MLUfFjq/giphy.gif" alt="" style="" /><br />
<br /></p>

<p>This project is a little bit different than the usual projects. The first part is only questions about Python&rsquo;s specificity like &ldquo;What would be the result of&hellip;&rdquo;. 
You should <strong>read all documentation first (as usual :))</strong>, then take the time to <strong>think and brainstorm with your peers</strong> about what you think and why. <strong>Try to do this without coding anything for a few hours</strong>.</p>

<p>Trying examples in the Python interpreter will give you most of the answers without having to think about it. <strong>Don&rsquo;t go this route</strong>. First read, then think, then brainstorm together. Only then you can test in the interpreter.</p>

<p>It&rsquo;s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types.
The biggest mandatory task is the blog post and it will count for 50% of the total score of the project.</p>

<p>Note that during interviews for Python positions, <strong>you will most likely have to answer to these type of questions</strong>.</p>

<p>All your answers should be only one line in a file. No space before or after the answer.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/n1x09X-KJSllpJkJorBw2A" title="9.10. Objects and values" target="_blank">9.10. Objects and values</a> </li>
<li><a href="/rltoken/3teQMNNfDeyGvCtZfjsf5g" title="9.11. Aliasing" target="_blank">9.11. Aliasing</a> </li>
<li><a href="/rltoken/JuPVygeoG27Q_qKxB2lP8g" title="Immutable vs mutable types" target="_blank">Immutable vs mutable types</a> </li>
<li><a href="/rltoken/UbL96sV3cIxewdQPW_zwRw" title="Mutation" target="_blank">Mutation</a> (<em>Only this chapter</em>)</li>
<li><a href="/rltoken/-t_1VsmKlgWHszL5y1YiKA" title="9.12. Cloning lists" target="_blank">9.12. Cloning lists</a> </li>
<li><a href="/rltoken/IdBAdTYNLuS3YpRRQIam6Q" title="Python tuples: immutable but potentially changing" target="_blank">Python tuples: immutable but potentially changing</a> </li>
</ul>

 <h4 class="task">
    0. Who am I?
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>What function would you use to print the type of an object?</p>

<p>Write the name of the function in the file, without <code>()</code>.</p>

 <h4 class="task">
    1. Where are you?
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>How do you get the variable identifier (which is the memory address in the CPython implementation)?</p>

<p>Write the name of the function in the file, without <code>()</code>.</p>

 <h4 class="task">
    2. Right count
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>

 <h4 class="task">
    3. Right count =
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>

  <h4 class="task">
    4. Right count =
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>

<h4 class="task">
    5. Right count =+
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>

<h4 class="task">
    6. Is equal
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>What do these 3 lines print?</p>

<h4 class="task">
    7. Is the same
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>What do these 3 lines print?</p>

 <h4 class="task">
    8. Is really equal
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>What do these 3 lines print?</p>

  <h4 class="task">
    9. Is really the same
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>What do these 3 lines print?</p>

 <h4 class="task">
    10. And with a list, is it equal
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>What do these 3 lines print?</p>

 <h4 class="task">
    11. And with a list, is it the same
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>What do these 3 lines print?</p>

 <h4 class="task">
    12. And with a list, is it really equal
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>What do these 3 lines print?</p>
