"""
incmatrix.py
------------

Code used for reprs/incmatrix.md.

"""

import networkx as nx

from os import path, environ
import sys
sys.path.append(path.join(environ['ERDOS_PATH'], 'scripts/'))
import utils


def example_pic():
    """Generate the example graph picture."""
    # create graph from edge list
    graph = nx.Graph([(0, 1), (1, 2), (2, 3), (3, 1), (1, 2), (0, 3)])
    utils.example_image(graph, "incmatrix.png", edge_labels=True)


if __name__ == '__main__':
    example_pic()
