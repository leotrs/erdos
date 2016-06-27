#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Basic quickstart stuff
AUTHOR = 'dleonardotn'
SITENAME = 'erdos'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Choose theme
THEME = 'pelican-elegant'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/ErdosNS'),
          ('email', 'mailto:leo@erdosnet.work'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


#############################################################################
### pelican-elegant specific configuration
#############################################################################

# "About This Site" section in root url
LANDING_PAGE_ABOUT = {'title': 'Erdos', 'subtitle': 'About this site', 'details':
                      '<p>Erdos is a site with educational problem sets of '
                      'increasing difficulty for learning about <a href='
                      '"https://en.wikipedia.org/wiki/Network_science">Network'
                      ' Science.</a></p><p>Erdos has been inspired by projects'
                      ' like <a href="https://projecteuler.net/">Project Euler'
                      '</a> for math and programming, <a href='
                      '"http://rosalind.info/about/">ROSALIND</a> for bioninformatics,'
                      ' and <a href="https://cryptopals.com/">the cryptopals'
                      ' challenges</a> for cryptography.</p><p>Erdos is '
                      'coming soon!</p>'}
