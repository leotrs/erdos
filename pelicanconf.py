#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import re
import os
import markdown as md


#############################################################################
### Tweaks to defaults
#############################################################################

# Basic stuff
AUTHOR = 'leotorr'
SITENAME = 'erdos'
SITESUBTITLE = 'Problem-based NetSci'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
DISQUS_SITENAME = "erdos"
SITEURL = ''                    # gets overwritten by publishconf.py

# Directories
PATH = 'content'
CACHE_PATH = '.cache'
LOAD_CONTENT_CACHE = True
CACHE_CONTENT = True
THEME_PATH = '../pelican/pelican-themes/'
ARTICLE_PATHS = ['challenges']
ARTICLE_URL = 'challenges/{slug}.html'
ARTICLE_SAVE_AS = 'challenges/{slug}.html'
PAGE_PATHS = ['']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'


# Choose theme
THEME = os.path.join(THEME_PATH, 'elegant')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/ErdosNS'),
          ('github', 'https://github.com/leotrs/erdos'),
          ('email', 'mailto:leo@erdosnet.work'),)

# How many articles per page
DEFAULT_PAGINATION = 10

# Allow document-relative URLs when developing
RELATIVE_URLS = True

# These templates don't need files that use them: they are rendered directly
DIRECT_TEMPLATES = ['index', 'categories', 'glossary', '404']

# Set to empty string to avoid generating these pages
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''


#############################################################################
### Landing page config
#############################################################################

LANDING_PAGE_DETAILS = """

<p>Erdos is a site with educational problem sets of increasing difficulty
for learning about <a
href="https://en.wikipedia.org/wiki/Network_science">Network
Science.</a></p>

<p>If you're curious about NetSci, but don't know where to begin, you can
read about it <a href="/network-science.html">here</a>. If this exciting
area of science sounds interesting, come try out Erdos and <a
href=mailto:dleonardotn@gmail.com target="_blank">let us know</a> how what
you think.</p>

<p>If you want to learn how to use this site, read the <a
href="/how-to.html">how to.</a> If you want to dive right in, see our
problem sets <a href="/categories.html">here.</a></p>

"""

# "About This Site" section in root url
LANDING_PAGE_ABOUT = {'title': 'Erdos', 'subtitle': SITESUBTITLE,
                      'details': LANDING_PAGE_DETAILS}


#############################################################################
### Custom filters
#############################################################################

JINJA_FILTERS = {}


#############################################################################
### Define positions for categories
#############################################################################

CATEGORIES_POS = {
    'Graphs': 10,
    'Representations': 20,
    'Measures': 30
}


#############################################################################
### Pelican plugins
#############################################################################
PLUGIN_PATHS = ['../pelican/pelican-plugins/']
PLUGINS = ['jinja2content', 'render_math', 'glossary']
GLOSSARY_EXCLUDE = ['Hint']
