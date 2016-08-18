"""
nodes_edges.py
--------------

Solution for graphs/nodes_edges.md.

"""


def nodes_edges():
    """Read the graph from stdin, and return node with highest degree.

    This function reads every edge from stdin, computes the degree of each
    node and then sorts them by degree. This wouldn't be efficient for
    large graphs. In that case, it would be better to count the degree as
    one reads the edges, and never store the edges in memory.

    """
    num_nodes, num_edges = [int(i) for i in input().split(" ")]

    # nodes are just labeled by numbers
    nodes = range(num_nodes)

    # edges are a list of two nodes
    edges = []
    for _ in range(num_edges):
        edges.append([int(n) for n in input().split(" ")])

    # compute the degree of each node by counting edges that include them
    degree = {node: len([e for e in edges if node in e])
              for node in nodes}

    # sort nodes by degree and get out desired node
    highest = max(nodes, key=degree.get)

    return highest


if __name__ == '__main__':
    print(nodes_edges())
