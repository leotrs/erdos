"""
brabasi.py
----------

Solution for random/barbasi.md.

"""

import numpy as np
import networkx as nx
from random import random
from matplotlib.pylab import plt


def barabasi_albert(num_nodes, edges_per_node):
    """Generate a Barabasi-Albert graph and return a NetworkX.Graph."""
    graph = nx.Graph()
    graph.add_node(0)
    graph.add_node(1)
    graph.add_edge(0, 1)

    for node in range(2, num_nodes):
        graph.add_node(node)
        nodes = graph.nodes()
        degrees = graph.degree()
        normalization = sum(degrees.values())
        weights = [degrees[n]/normalization for n in nodes]
        targets = np.random.choice(nodes, size=edges_per_node, p=weights)

        for node2 in targets:
            graph.add_edge(node, node2)

    return graph


def draw_graph(graph):
    nx.draw(graph)
    plt.show()


if __name__ == '__main__':
    num_nodes, edges_per_node = [int(n) for n in input().split(" ")]
    draw_graph(barabasi_albert(num_nodes, edges_per_node))
