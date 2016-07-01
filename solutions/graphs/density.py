"""
solutions/density.py
========================

Solution for /content/density.md.

"""


def density():
    """Read the graph from stdin, and return the density of the network."""
    num_nodes, num_edges = [int(i) for i in input().split(" ")]

    # We don't need to label the nodes or even read the edges.
    # Just compute the maximum number of edges and the density.

    # If we pick one node arbitrarily, there are n-1 other nodes to connect
    # it to. For the second node we pick, there will be n-2, and n-3 for
    # the third and so for the i-th node, there will be n-i edges
    # available.
    max_edges = 0
    for i, node in enumerate(range(num_nodes)):
        max_edges += num_nodes - (i+1)

    return num_edges / float(max_edges)


if __name__ == '__main__':
    print("{0:.3f}".format(density()))
