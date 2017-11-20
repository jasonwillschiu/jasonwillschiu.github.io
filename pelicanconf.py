#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jason Wills Chiu'
SITENAME = 'Jason Wills Chiu'
SITESUBTITLE = u'Where is this subtitle readable?'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Australia/Sydney'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}-{date:%m}-{date:%d}-{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}-{date:%m}-{date:%d}-{slug}/index.html'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#MARKUP = ('md', 'ipynb')
#PLUGINS = ['ipynb.markup']

MARKUP = ['md','ipynb']
PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = [
    'summary',       # auto-summarizing articles
    'feed_summary',  # use summaries for RSS, not full articles
    'ipynb.liquid',  # for embedding notebooks
    'liquid_tags.img',  # embedding images
    'liquid_tags.video',  # embedding videos
    'liquid_tags.include_code',  # including code blocks
    'ipynb.markup', # to use ipynb-meta i think
    'liquid_tags'

]
IGNORE_FILES = ['.ipynb_checkpoints']

# Test ignoring css for notebook content
IPYNB_IGNORE_CSS = True

# for liquid tags
# CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'articles'

# THEME SETTINGS
THEME = './theme/'

ABOUT_PAGE = '/pages/about.html'
GITHUB_USERNAME = 'jasonwillschiu'
STACKOVERFLOW_ADDRESS = 'https://stackoverflow.com/users/8481225/jason-chiu'
SHOW_ARCHIVES = True
SHOW_FEED = False  # Need to address large feeds

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'figures', 'videos', 'downloads', 'favicon.ico']
