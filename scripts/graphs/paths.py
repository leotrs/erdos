"""
paths.py
--------

Code used for graphs/paths.md.

"""

import networkx as nx

from os import path, environ
import sys
sys.path.append(path.join(environ['ERDOS_PATH'], 'scripts/'))
import utils


def example_pic():
    """Generate the example graph picture."""
    # create graph from edge list
    graph = nx.Graph([(0, 1), (1, 2), (0, 2), (3, 4), (4, 6), (4, 5), (6, 3)])
    graph.add_node(7)
    utils.example_image(graph, "paths.png", layout="shell")


if __name__ == '__main__':
    example_pic()
