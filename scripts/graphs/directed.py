"""
directed.py
-----------

Code used for graphs/directed.md.
"""

import networkx as nx

from os import path, environ
import sys
sys.path.append(path.join(environ['ERDOS_PATH'], 'scripts/'))
import utils


def example_pic():
    """Generate the example graph picture."""
    # create graph from edge list
    graph = nx.DiGraph([(0, 1), (0, 2), (1, 3), (3, 0), (0, 3)])
    utils.example_image(graph, "directed_example.png")


if __name__ == '__main__':
    example_pic()
