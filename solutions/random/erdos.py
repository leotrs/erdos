"""
erdos.py
--------

Solution for random/erdos.md.

"""

import numpy as np
import networkx as nx
from random import random
from matplotlib.pylab import plt


def erdos_renyi(num_nodes, probability):
    """Generate one G(n, p) graph and return its adjacency matrix."""
    matrix = np.zeros((num_nodes, num_nodes), int)

    # Perform a random process with probability p for each edge
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random() <= probability:
                # Since the graph is undirected, the adjacency matrix
                # contains two entries equal to 1 per edge.
                matrix[i][j] = 1
                matrix[j][i] = 1

    return matrix


def draw_matrix(matrix):
    nx.draw(nx.from_numpy_matrix(matrix))


if __name__ == '__main__':
    num_nodes, probability = input().split(" ")
    num_nodes = int(num_nodes)
    probability = float(probability)

    draw_matrix(erdos_renyi(num_nodes, probability))
    plt.show()
