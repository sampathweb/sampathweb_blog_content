Title: Starting a Blog with Pelican
Date: 2013-11-20 18:50
Comments: true
Slug: Starting-a-Blog

<!-- PELICAN_BEGIN_SUMMARY -->
I have been wanting to start a blog for a while, but kept giving excuses.  Now it's finally time to catch up on my New Year resolution before the year is done.  After searching for a blogging platform, I decided on Pelican hosted on github pages.  I can use Python and IPython notebook for blogging too and that might just be what I need to write some code.
<!-- PELICAN_END_SUMMARY -->

Choosing a blogging platform
----------------------------
I follow Jake Vanderplas and when he moved from Octopress to Pelican I was curious.  But when he created a plug-in to embedd IPython Notebook into a Pelican blog, I was sold.  I followed the steps in [Jake's blog post](http://jakevdp.github.io/blog/2013/05/07/migrating-from-octopress-to-pelican/) to get this blog setup.

I also get to write in Markdown, which is very cool.  It lets me focus on content and have my jinja2 template do the magic of laying it out pretty with css.  I am mostly using the default theme, but plan to tinker around the css styling sometime in the next few months.

And with that, I have my own Blog Post.  I did a quick hello world in IPython and got it rendered here.  Now, I should have no excuses in writing a blog post regularly.  All I need to do is publish IPython notebooks with Markdown text.

{% notebook hello_world.ipynb cells[:] %}

Hosting the Blog
----------------
To host the blog on github, I created a branch 'gh-pages'.  I found a great blog post on how to keep gh-pages in sync with master branch.  I found great help in [Lea's blog post](http://lea.verou.me/2011/10/easily-keep-gh-pages-in-sync-with-master/)

Finally, to have it served under your domain name, I had to create a CNAME file and add my domain name. The steps are in [Githup post here](https://help.github.com/articles/setting-up-a-custom-domain-with-pages)

Summary
-------
That's a wrap for first blog post for today.  Tomorrow, I plan on solving some Euler Project challenges in IPython and embed it in my blog post.