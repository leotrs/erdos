"""
genarticle.py
-------------

Generate the skeleton of an erdos article by using jinja2 templates.

"""

import os
import argparse
import subprocess
from collections import defaultdict
from string import punctuation
from jinja2 import Environment, FileSystemLoader


ROOT = '/home/leo/code/erdos/'
CONTENT_DIR = os.path.join(ROOT, 'content/')
TEMPLATES_DIR = os.path.join(ROOT, 'scripts/templates/')
TEMPLATE_FILE = 'article.mdpp'   # must be realteive to TEMPLATES_DIR


def make_vars(**kwargs):
    """Returns a dict with var=value pairs, to be passed to the template."""
    vars_dict = defaultdict(str)
    vars_dict.update(kwargs)

    # generate dd/mm/yyyy date string
    vars_dict['date'] = subprocess.getoutput('date "+%x"')

    # generate a random-ish string of 8 chars ..
    md5 = subprocess.getoutput('date | md5sum | cut -c1-8')

    # .. and a hyphenated version of article summary ..
    table = {ord(p): '' for p in punctuation}
    slug = vars_dict['summary'].lower().translate(table).replace(' ', '-')

    # ..to get a unique disqus id!
    vars_dict['disqus_id'] = md5 + '-' + slug

    return vars_dict


def render(**kwargs):
    """Creates the appropriate jinja2 objects and renders the template."""
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    template = env.get_template(TEMPLATE_FILE)

    return template.render(**make_vars(**kwargs))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('path', help='the output file for the new article - '
                        'must be relative to erdos/content directory')
    parser.add_argument("-t", "--title", help="specify article title")
    parser.add_argument("-c", "--category", help="specify article category")
    parser.add_argument("-s", "--summary", help="specify article summary")
    args = parser.parse_args()

    with open(os.path.join(CONTENT_DIR, args.path), 'w+') as outfile:
        text = render(**args.__dict__)
        outfile.write(text)
