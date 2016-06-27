"""
solutions/directed.py
=====================

Solution for /content/directed.md.

"""


def directed():
    """Read the graph from stdin, and return the nodes with highest outdegree
    and indegree, respectively.

    This function reads every edge from stdin, computes the degrees of each
    node and then sorts them by degree. This wouldn't be efficient for
    large graphs. In that case, it would be better to keep count of the
    degrees as the edges are read, and never store the edges in memory.

    """

    num_nodes, num_edges = [int(i) for i in input().split(" ")]

    # nodes are just labeled by numbers
    nodes = range(num_nodes)

    # edges are a list of two nodes
    edges = []
    for _ in range(num_edges):
        edges.append([int(n) for n in input().split(" ")])

    # compute the degrees of each node by counting edges that include them
    # every edge is of the form 'source target'
    outdegree = {node: len([e for e in edges if e[0] == node])
                 for node in nodes}

    indegree = {node: len([e for e in edges if e[1] == node])
                for node in nodes}

    # sort nodes by degree and get out desired node
    highest_out = sorted(nodes, key=outdegree.get)[-1]
    highest_in = sorted(nodes, key=indegree.get)[-1]

    return highest_out, highest_in


if __name__ == '__main__':
    print("{0} {1}".format(*directed()))
