Date: 2014-09-23 16:28
Author: Brad Rice
Email: brad@bradrice.com
Title: A vim template for pelican
Slug: vim-template-pelican
Tags: pelican, vim
Category: Pelican

I installed the [vim-template
plugin](https://github.com/aperezdc/vim-template) for creating templates to create a
boilerplate markdown file for pelican.

    :::vim
    Date: %FDATE%
    Author: Brad Rice
    Email: brad@bradrice.com
    Title: %HERE%
    Slug: 
    Tags: 
    Category: 

Now when I am in my content folder, I use vim to create a new post, it
prepopulates the meta at the top of the file and automatically puts the
date and time into the file. My cursor is at the Title field.

Here's my [vim-template
gist](https://gist.github.com/bradrice/465e1d82abd5619b70b8).
