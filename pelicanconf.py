#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jason Wills Chiu'
SITENAME = 'Jason Wills Chiu'
SITEURL = 'https://jasonwillschiu.github.io'

PATH = 'content'

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = 'English'

# To modify pelican-blue theme
LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/jason-chiu-476b5411b/'),
          ('github', 'https://github.com/jasonwillschiu/jasonwillschiu.github.io')
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#Need this for theme to work relative paths
RELATIVE_URLS = True

# For Dan's notebook plugin and render latex
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['plugins','./plugins']
PLUGINS = ['render_math','ipynb.markup','sitemap','tipue_search']

# To get latex equations rendered
#PLUGINS = ["render_math"]


# To use a theme
THEME = 'theme/chris'
# THEME = 'notmyidea'

# For pelican-blue theme
SIDEBAR_DIGEST = 'Data Science Student'
DISPLAY_PAGES_ON_MENU = True
MENUITEMS = (('About','about.html'),('Blog','about.html'),('Resume','about.html'))
