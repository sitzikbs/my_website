---
layout: layouts/blog-post.njk
title: "New Year, New Website: How I Migrated from WordPress Using AI Coding Agents"
date: 2026-01-03
author: Itzik Ben-Shabat
permalink: "/blog/posts/2026-01-03-migrating-from-wordpress-with-ai-coding-agents.html"
---

<div class="post-content">

<p>Happy 2026! As the new year kicks off, I'm excited to share something I've been working on: a complete redesign and migration of my website. But here's the twist—I didn't do it alone. I had help from an army of AI coding agents, and the experience was equal parts enlightening and nostalgic (more on that ICQ reference later).</p>

<h2 class="wp-block-heading">The WordPress Years: A Love Story Gone Stale</h2>

<p>I created my first website way back when I was an early PhD student. My mission was simple: make research more accessible to everyone. The problem? My front-end and back-end coding skills were, to put it mildly, non-existent. After building a basic Joomla website (yes, Joomla—I'm <em>that</em> old), I decided to try this up-and-coming platform called WordPress.</p>

<p>At the time, WordPress was great. Easy to create and upload new posts, everything uses a GUI, and not a lot of hacking required after the initial setup. Perfect for someone like me who just wanted to share ideas without wrestling with code.</p>

<p>But over time, the honeymoon ended. Themes and plugins needed constant updates. They'd break. I'd have to revert to backups. Then came the hacker attacks. The design became outdated, but the thought of migrating away while keeping all my existing content—blog posts, podcast episodes, everything—seemed overwhelming. So I stuck with it, grumbling quietly.</p>

<p>Enter: AI coding agents.</p>

<h2 class="wp-block-heading">Why AI Coding Agents Are the Real Deal</h2>

<p>If you're reading this blog, you probably don't need me to explain how transformative AI is for coding. Whether you use Cursor, Claude, Gemini CLI, or GitHub Copilot (my tool of choice), the bottom line is the same: these tools make us exponentially more productive with minimal effort.</p>

<p>The main challenge isn't the tools themselves—it's figuring out the right workflow. Even <a href="https://x.com/karpathy/status/2004607146781278521" target="_blank" rel="noopener noreferrer">Andrej Karpathy shared</a> how he feels behind as a programmer in this new AI era. So I decided to document my experience. I don't know if it's the <em>best</em> workflow, but it definitely worked for me.</p>

<h2 class="wp-block-heading">The 9-Step Copilot Migration Workflow</h2>

<h3 class="wp-block-heading">1. Plan Mode: Build the Blueprint</h3>

<p>The first step—and the one I spent the most time on—was planning. GitHub Copilot has a built-in plan mode that creates to-do lists, but I found that some tweaks made it much better. I instructed the agent to:</p>

<ul>
<li>Create one high-level to-do list with major work packages</li>
<li>Provide detailed descriptions for each work package</li>
<li>Make sure everything was crystal clear from the start</li>
</ul>

<p>The goal was to migrate from WordPress to a static site hosted on a platform like Cloudflare Pages or GitHub Pages. I wanted something modern, fast, and maintainable.</p>

<h3 class="wp-block-heading">2. Refine the Plan: Self-Contained Work Packages</h3>

<p>Next, I helped the AI refine its plan. Each work package needed to be self-contained and do one thing well. I also asked it to:</p>

<ul>
<li>Work on separate branches when relevant</li>
<li>Write thorough tests</li>
<li>Stop before committing so I could manually inspect the current state</li>
</ul>

<p>This was crucial. I wanted control over the process without micromanaging every line of code.</p>

<h3 class="wp-block-heading">3. The Dependency Graph: Parallelization FTW</h3>

<p>I asked Copilot to create a dependency graph showing which work packages could run independently and which needed to be done sequentially. This allowed me to identify phases where I could parallelize the work—one of the biggest productivity unlocks.</p>

<h3 class="wp-block-heading">4. Issues: Organization Is Key</h3>

<p>For each work package, I had Copilot open a dedicated GitHub issue. Each issue referenced the detailed description and the dependency graph. This made tracking progress incredibly straightforward.</p>

<h3 class="wp-block-heading">5. Agents: The Parallel Processing Magic</h3>

<p>Here's where things got really interesting. I launched multiple agents in parallel for work packages that could run independently. It felt like having a team of talented engineers, all working at the same time on different parts of the project.</p>

<h3 class="wp-block-heading">6. Manual Inspection: Trust, but Verify</h3>

<p>Once the agents completed their tasks, I went through each one. I ran their tests locally, verified that every visual element worked as expected, and decided whether to resolve issues in the same agent's chat or open a new issue. This balance kept things moving efficiently.</p>

<h3 class="wp-block-heading">7. Deployment: Detailed Instructions</h3>

<p>When it was time to deploy, I asked Copilot for step-by-step instructions for my platform of choice (Cloudflare Pages). The instructions were incredibly detailed, though a few UI differences were easy enough to overcome. Copilot even gave me tips I hadn't thought of, like setting up preview deployments for branches.</p>

<h3 class="wp-block-heading">8. Security Checks: Better Late Than Never</h3>

<p>After most of the migration was done, I created a dedicated issue focused on security. As an Israeli, my websites tend to get randomly targeted by hackers, so this was important. In retrospect, I should have made this a work package from the beginning. Lesson learned.</p>

<h3 class="wp-block-heading">9. Final Tweaks: SEO and Beyond</h3>

<p>By this point, I was basically done. But because making changes had become so easy, I asked Copilot to help improve SEO (or should we call it LLMO now—Large Language Model Optimization?). These final touches made the site even better.</p>

<h2 class="wp-block-heading">What We Actually Built</h2>

<p>Let me give you a sense of the scope without getting too specific (since this repo isn't public, but you can replicate the process):</p>

<ul>
<li><strong>Migration to Eleventy (11ty):</strong> We chose 11ty as the static site generator. It's lightweight, fast, and flexible.</li>
<li><strong>74 Blog Posts:</strong> All migrated from WordPress to Markdown with proper frontmatter and formatting preserved.</li>
<li><strong>Image Optimization:</strong> Downloaded 1,847 images from the WordPress CDN, converted 489 to WebP format with responsive sizes (200px, 400px, 800px, 1200px), achieving a 78.3% size reduction (107MB → 23MB).</li>
<li><strong>Asset Minification:</strong> CSS and JavaScript files were minified for faster loading.</li>
<li><strong>Build Automation:</strong> Set up npm build scripts that run CSS minification, JS minification, and 11ty generation in one command.</li>
<li><strong>SEO Optimization:</strong> Added Schema.org metadata, Open Graph tags, sitemap.xml, robots.txt, and Google Analytics 4.</li>
<li><strong>Performance:</strong> The build completes in ~1.3 seconds. Yes, seconds.</li>
</ul>

<p>The entire process was broken into phases: setup, content migration, styling, asset optimization, SEO, accessibility, security audits, and deployment.</p>

<h2 class="wp-block-heading">The Big Unlocks: Why This Worked</h2>

<p>Looking back, here are the key reasons this project was successful:</p>

<h3 class="wp-block-heading">Parallelization</h3>

<p>Running multiple agents on independent work packages simultaneously was a game-changer. What would have taken weeks became days.</p>

<h3 class="wp-block-heading">High-Quality Code in Unfamiliar Territory</h3>

<p>I'm not a web developer by trade. But Copilot helped me write clean, modern, performant code in areas where I had little experience. It was also a great learning opportunity—I now understand 11ty, WebP optimization, and build pipelines much better.</p>

<h3 class="wp-block-heading">Quick Debugging and Iteration</h3>

<p>When something didn't work, I could quickly iterate with the agent to fix it. No more Googling for hours or waiting for Stack Overflow responses.</p>

<h3 class="wp-block-heading">Impeccable Documentation</h3>

<p>One thing I usually struggle with is "getting back into" a project after stepping away. This time, the documentation generated by the agents was so thorough that a short conversation brought me right back up to speed. This was huge for a project I stretched over several weeks.</p>

<h2 class="wp-block-heading">A Personal Anecdote</h2>

<p>Working with these AI agents felt oddly familiar. I'm used to collaborating with students on repos—talented engineers who need direction on <em>what</em> to do and <em>how</em> I like it done. This experience was similar, except I had an entire army of very capable agents ready to execute on my nudges. It was incredibly empowering.</p>

<p>And here's the nostalgic part: the whole process felt like a long chat conversation. As a kid, I spent countless nights on ICQ chatting with friends. This brought back that same vibe—just with code instead of gossip.</p>

<h2 class="wp-block-heading">A Few Caveats and Tips</h2>

<p><strong>P.S. #1:</strong> If a Copilot dev is reading this, please add to the system prompt not to use <code>!</code> at the end of bash commands. It breaks the terminal every time. (Yes, I put it in my custom instructions, but it's still annoying.)</p>

<p><strong>P.S. #2:</strong> I feel like this workflow was mostly prompt engineering, and there are probably even smoother tools out there. I genuinely enjoyed this learning experience, and if anyone has their own workflow to share, please do.</p>

<p><strong>P.S. #3:</strong> All of this—planning, execution, debugging—used less than 20% of my monthly GitHub Copilot Pro subscription (40 USD/month). That's remarkable ROI.</p>

<h2 class="wp-block-heading">The Punchline</h2>

<p>One of my main goals was to make updating my website easier. Adding publications or writing new blog posts should be mostly automatic. Did you notice that this post was largely generated with Copilot? Obviously not entirely—I had the content and ideas—but it stripped away the editorial work I personally dislike.</p>

<p>At the end of the day, this project transformed what could have been a dreadful, annoying task into something genuinely enjoyable. The unlockers of AI coding agents are real: parallelization, high-quality code, rapid iteration, and excellent documentation. If you've been putting off a similar project, maybe it's time to give AI agents a shot.</p>

<p>Now, if you'll excuse me, I have a sudden urge to reinstall ICQ and see if anyone's still online. 🎉</p>

</div>
