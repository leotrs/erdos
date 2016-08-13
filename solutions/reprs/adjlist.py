"""
adjlist.py
==========

Solutions for /content/adjlist.md.

"""


def adjlist():
    """Read a file edge by edge and output the adjacency list of each node."""
    num_nodes, num_edges = [int(i) for i in input().split(" ")]

    # nodes are just labeled by numbers
    nodes = range(num_nodes)

    # edges are a list of two nodes, read each one and append to the
    # corresponding adjacency list
    neighbors = {node: [] for node in nodes}
    for _ in range(num_edges):
        source, target = [int(i) for i in input().split(" ")]
        neighbors[source].append(target)
        neighbors[target].append(source)

    # print the lines and the lists in order
    for node in sorted(neighbors.keys()):
        print(" ".join([str(n) for n in sorted(neighbors[node])]))


if __name__ == '__main__':
    adjlist()
