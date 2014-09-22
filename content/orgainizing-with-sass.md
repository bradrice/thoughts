Date: 2014-09-22 10:00 AM
Author: Brad Rice
Email: brad@bradrice.com
Title: Organizing css with sass
Slug: orgainizing-with-sass
Tags: sass, css
Category: SASS

If you use SASS to compile your css, you have access to a nice way of organizing your css code to make it easier to read and easier to find what needs to change when you are tweaking a layout. Consider the following.

	:::scss 

    nav#menu {
        background-color: #a27bfe;
        @include border-radius(8px);
    }

    nav#menu ul {
        padding: 12px 6px;
        margin: 0 12px;
    }

    nav#menu ul li {
        display: inline;
    }

    nav#menu ul li>a {
        text-decoration: none;
        color: #fff;
        padding: 12px 6px;
    }

    nav#menu ul li>a:hover {
        color: #334bf1;
        background-color: #fff;
    }

Notice the repeat of nav#menu in each specification as well as with the
top level for that item? Using SASS we can wrap all the specifications
for nav#menu into it's own outer set of braces so we don't have to
repeat that directive over and over.

    :::scss

    nav#menu {
        background-color: #a27bfe;
        @include border-radius(8px);

        ul {
            padding: 12px 6px;
            margin: 0 12px;
        }

            ul li {
            display: inline;
        }

        ul li>a {
            text-decoration: none;
            color: #fff;
            padding: 102px 6px;
        }

        ul li>a:hover {
            color: #334bf1;
            background-color: #fff;
        }
    }
