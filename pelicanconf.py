#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import re
import os
import markdown as md


#############################################################################
### Tweaks to defaults
#############################################################################

# Basic quickstart stuff
AUTHOR = 'dleonardotn'
SITENAME = 'erdos'
SITEURL = ''
SITESUBTITLE = 'Learn about Network Science through problem solving.'
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
          ('github', 'https://github.com/Leockard/erdos'),
          ('email', 'mailto:leo@erdosnet.work'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Read into 'DIRECT_TEMPLATES' in pelican/settings.py
DIRECT_TEMPLATES = ['index', 'categories', 'glossary'] # 'tags', 'authors'


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
    """Reads all pages and extracts definition lists.

    Return a list of the form
    [('def_title', 'def_link', 'def_content'), ... ]
    """
    articles = []

    for subdir in [d for d in os.listdir(PATH) if os.path.isdir(os.path.join(PATH, d))]:
        if subdir == 'images' or subdir == 'pages':
            continue

        subpath = os.path.join(PATH, subdir)
        articles += [os.path.join(subpath, f) for f in os.listdir(os.path.join(PATH, subdir))]

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

<p>Erdos has been inspired by projects like
<ahref="https://projecteuler.net/">Project Euler </a> for math and
programming, <a href= "http://rosalind.info/about/">ROSALIND</a> for
bioninformatics, and the <a href="https://cryptopals.com/">cryptopals
challenges</a> for cryptography.</p>

<p>If you want to know more about Network Science, start <a
href="/pages/network-science.html">here.</a></p>

<p>If you want to dive right in, see our problem sets <a
href="/categories.html">here.</p>

"""

# "About This Site" section in root url
LANDING_PAGE_ABOUT = {'title': 'Erdos', 'subtitle': SITESUBTITLE,
                      'details': LANDING_PAGE_DETAILS}


#############################################################################
### Custom filters
#############################################################################

# def get_definitions(html):
#     """Extract definition lists from html and return as dictionary."""
#     url_regex = re.compile(r'"og:url=".*?"(.*?)"', re.DOTALL)
#     url = re.findall(url_regex, html)

#     title_regex = re.compile(r'<dt>(.*?)</dt>', re.DOTALL)
#     titles = re.findall(title_regex, html)
#     contents_regex = re.compile(r'<dd>(.*?)</dd>', re.DOTALL)
#     contents = re.findall(contents_regex, html)

#     definitions = [(title, content) for title, content in zip(titles, contents)]
#     return definitions

# def regex_replace(s, find, replace):
#     """A non-optimal implementation of a regex filter"""
#     return re.sub(find, replace, s)

# def print_filter(s):
#     """Debug filter."""
#     print(s)
#     return s

JINJA_FILTERS = {
    # 'print': print_filter,
    # 'regex_replace': regex_replace,
    # 'get_definitions': get_definitions
}
