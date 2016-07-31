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

# Choose theme
THEME = os.path.join(THEME_PATH, 'pelican-elegant')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/ErdosNS'),
          ('github', 'https://github.com/leotorr/erdos'),
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
### Extract definitions from all articles
#############################################################################

def get_definitions_md(markdown):
    r"""Extract definition lists from markdown and return as dictionary.

    Each definition list in a page must conform to the following format:

        Title[](#<anchor>)
        : <content>.

    - The title must begin at the start of the line.
    - The anchor should link to empty text.
    - The anchor name should not contain '/'.
    - There must be one newline after the anchor.
    - There must be some whitespace between the colon and the content.
    - The content must end in a '.'.

    In other words, each entry in devery definiiton list must conform to
    the following regexp, with only the re.M active:

        r'^(.*?)\[\]\((#.*?)\)\n:((?:.*\n)+?)^$'

    """
    page_title_regex = re.compile(r'^Title:\s*(.*)')
    article_title = re.search(page_title_regex, markdown).groups()[0]
    article_title = article_title.lower().replace(" ", "-") + '.html'

    definition_regex = re.compile(r'^(.*?)\[\]\((#.*?)\)\n:((?:.*\n)+?)^$', re.M)
    matches = re.findall(definition_regex, markdown)

    definitions = [(title, article_title + anchor, md.markdown(content)) for
                   title, anchor, content in matches]

    return definitions


def all_definitions():
    """Reads all Markdown pages and extracts definition lists.

    Return a list of the form

        [('def_title', 'def_link', 'def_content'), ... ]

    Note: reads only .md, not .mdpp files.
    """
    articles = []

    for subdir in [d for d in os.listdir(PATH) if
                   os.path.isdir(os.path.join(PATH, d))]:
        if subdir == 'images' or subdir == 'pages':
            continue

        subpath = os.path.join(PATH, subdir)

        for filename in os.listdir(os.path.join(PATH, subdir)):
            fullname = os.path.join(subpath, filename)
            if os.path.splitext(fullname)[1] == '.md':
                articles.append(fullname)

    definitions = []
    for article in articles:
        with open(article, 'r') as articlefile:
            definitions += get_definitions_md(articlefile.read())

    return definitions


# DEFINITIONS will be visible to all templates as a
DEFINITIONS = all_definitions()


#############################################################################
### Landing page config
#############################################################################

LANDING_PAGE_DETAILS = """

<p>Erdos is a site with educational problem sets of increasing difficulty
for learning about <a
href="https://en.wikipedia.org/wiki/Network_science">Network
Science.</a></p>

<p>If you're curious about NetSci, but don't know where to begin, you can
read about it <a href="/pages/network-science.html">here</a>. If this
exciting area of science sounds interesting, come try out Erdos and <a href=mailto:dleonardotn@gmail.com target="_blank">let us know</a>
how what you think.</p>

<p>If you want to learn how to use this site, read the <a
href="/pages/how-to.html">how to.</a> If you want to dive right in, see our
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
PLUGINS = ['pelican-jinja2content', 'render_math', 'glossary']
