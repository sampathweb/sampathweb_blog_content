Title: Starting a Blog with Pelican
date: 2013-11-26 18:50
comments: true
slug: Starting a Blog with Pelican

<!-- PELICAN_BEGIN_SUMMARY -->
I have been wanting to start a blog for a while, but kept giving excuses.  When I saw that Hacker School applications are now open, I needed a blog to show that I can do a program or two.  After searching for a blogging platform, I decided on Pelican hosted on github pages.  I can use Python and IPython notebook for blogging too and that might just be what I need to write some code.
<!-- PELICAN_END_SUMMARY -->

Choosing a blogging platform
----------------------------
I follow Jake Vanderplas and when he moved from Octopress to Pelican I was curious.  But when he created a plug-in to embedd IPython Notebook into a Pelican blog, I was sold.  I followed the steps in [Jake's blog post](http://jakevdp.github.io/blog/2013/05/07/migrating-from-octopress-to-pelican/) to get this blog setup.

I also get to write in Markdown, which is very cool.  It lets me focus on content and have my jinja2 template do the magic of laying it out pretty with css.  I am mostly using the default theme, but plan to tinker around the css styling sometime in the next few months.

And with that, I have my own Blog Post.  I did a quick hello world in IPython and got it rendered here.  Only four more days before I need to submit my application to Hacker School.  Wish me luck.  I need to write lot more than a Hello World program to show that I love this stuff.

{% notebook hello_world.ipynb cells[:] %}

Hosting the Blog
----------------
To host the blog on github, I created a branch 'gh-pages'.  I found a great blog post on how to keep gh-pages in sync with master branch.  I found great help in [Lea's blog post](http://lea.verou.me/2011/10/easily-keep-gh-pages-in-sync-with-master/)

Finally, to have it served under your domain name, I had to create a CNAME file and add my domain name. The steps are in [Githup post here](https://help.github.com/articles/setting-up-a-custom-domain-with-pages)

Summary
-------
That's a wrap for first blog post for today.  Tomorrow, I plan on solving some Euler Project challenges in IPython and embed it in my blog post.