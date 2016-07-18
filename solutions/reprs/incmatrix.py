"""
scripts/incmatrix.py
--------------------

Solution for /content/reprs/incmatrix.md.
"""

import numpy as np


def inc_matrix():
    """Read the graph from stdin, and output its incidence matrix."""
    num_nodes = int(input())
    # nodes are just labeled by numbers
    nodes = range(num_nodes)

    # Since we don't know the number of edges in the network before hand,
    # we first create a matrix with an empty column and append each edge as
    # we read them. We need the empty column because numpy needs to know
    # the number of rows in the matrix to append a column to it.
    matrix = np.array([[0] for i in range(num_nodes)])

    # Every edge appears twice in the adjacency list form, because if u and
    # v are joined by an edge, v appears in u's adjacency list and vice
    # versa. To avoid repeating edges, we need to keep a running count of
    # the ones that we have already observed. To do so efficiently, we keep
    # a dictionary similar to the full adjacency list, but only with the
    # edges we have read.
    edges = {node: set([]) for node in nodes}

    # The remaining of the input file has one line for each node.
    for node in nodes:
        current_edges = [(node, int(n)) for n in input().split(" ")]

        for edge in [(n1, n2) for n1, n2 in current_edges if n1 not in
                     edges[n2]]:
            column = np.array([[1] if n in edge else [0] for n in nodes])
            matrix = np.append(matrix, column, axis=1)

        for node1, node2 in current_edges:
            edges[node1].add(node2)
            edges[node2].add(node1)

    # Remember the first column is empty.
    return matrix[:, 1:]



if __name__ == '__main__':
    for row in inc_matrix():
        print(" ".join([str(i) for i in row]))
