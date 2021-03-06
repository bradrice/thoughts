#!/usr/bin/env python

# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Brad Rice'
SITENAME = u'Electric-Barnyard'
SITESUBTITLE = u'Mucking about with code in rural Ohio'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Brad Rice', 'http://www.bradrice.com'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

MENUITEMS = (('Home', '/thoughts'),
			)

DEFAULT_PAGINATION = 10
PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
	'extra/robots.txt',
	'extra/.htaccess'
	]

EXTRA_PATH_METADATA = {
	'extra/robots.txt': {'path': 'robots.txt'},
	'extra/.htaccess': {'path': '.htaccess'}
	}

ARTICLE_URL = 'posts/{slug}'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
PAGE_URL = '{slug}' 
PAGE_SAVE_AS = '{slug}.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}.html'

TYPOGRIFY = True

FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/atom.xml'

THEME = 'themes/electric-barnyard'
