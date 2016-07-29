"""
nodes_edges.py
--------------

Code used for nodes_edges.md.
"""

import networkx as nx

from os import path, environ
import sys
sys.path.append(path.join(environ['ERDOS_PATH'], 'scripts/'))
import utils


def example_pic():
    """Generate the example graph picture."""
    # create graph from edge list
    graph = nx.Graph([(0, 1), (0, 2), (1, 3), (3, 0)])
    utils.example_image(graph, "nodes_edges_example.png")


if __name__ == '__main__':
    example_pic()
