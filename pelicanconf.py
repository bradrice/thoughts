#!/usr/bin/env python

# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Brad Rice'
SITENAME = u'Thoughts'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

FILES_TO_COPY = ( ('extra/robots.txt', 'robots.txt'),
                  ('extra/.htaccess', '.htaccess') )

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
