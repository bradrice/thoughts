Date: 2014-09-19 05:00
Author: Brad Rice
Email: brad@bradrice.com
Title: A pelican post
Slug: a-pelican-post
Tags: pelican, python, writing
Category: Python

I’ve utilized different blog software such as [Drupal](http://drupal.com/) and [Wordpress](https://wordpress.org/). Perhaps for serving up a blog, that is too much overhead. I suppose all software is complex, but wouldn’t it be nice if there was a way to write without having to worry so much about installing and updating software. Wouldn’t it be nice to find simplicity. A system for writing using just a text editor such as [vim](http://www.vim.org/) or [IA Writer](http://www.iawriter.com/mac/). Then I could write and save it somewhere and have it show up on my blog. That is what [Pelican](http://blog.getpelican.com/) is. It is a static site generator. It uses Python code and scripts to generate out all the site code from templates and markdown files. I write the markdown, save it and then run the script. Walla, a blog post. The only catch is to put some meta data into the top of the markdown so the script knows what to do with the story, how to date and categorize it.

My site is hosted on [webfaction](http://www.webfaction.com). So I found a good source to get me started: [Pelicans on Webfaction](http://martinfitzpatrick.name/article/pelicans-on-webfaction/). I got stuck a few times, but after banging away at it I now have the framework to get it off the ground. I’ve created a repo so I can pull and edit my files from any machine I would like to use. I’m still trying to get Windows to work properly. Pelican has some nice scripts and they have some shortcuts that are really nice, but they utilize ‘make’ which is Unix only. So I’m still working on getting a nice method of writing and editing on windows so I can use my Samsung laptop. I’ll post updates here as I make progress.

Pelican uses Jinja templates, so I launched using the packaged theme called Simple, which give you the basic template files. I did a small amount of editing of those files and did most of the work in the css. I used [SASS](http://sass-lang.com/) and [Susy](http://susy.oddbird.net/) to write and compile my CSS. My image is created in Adobe Illustrator CC.
