"""
paths.py
--------

Solution for graphs/nodes_edges.md.

"""

from collections import defaultdict


def num_components():
    """Read the graph from stdin, and return the number of components."""
    num_nodes, num_edges = [int(i) for i in input().split(" ")]

    # edges are a list of two nodes
    edges = []
    for _ in range(num_edges):
        edges.append([int(n) for n in input().split(" ")])

    # first, we build a dictionary from every node to all its neighbors
    neighbors = defaultdict(list)
    while len(edges) > 0:
        node1, node2 = edges.pop()
        neighbors[node1].append(node2)
        neighbors[node2].append(node1)

    # To build the first component, we pick an arbitraty node, and follow
    # all its edges, as well as its neighbors' edges and so on, until there
    # are no more edges to follow. All nodes reached this way must be in
    # the same component. Then we pick a node we haven't examined yet and
    # do the same to get the second component, and so on until all nodes
    # have been examined.

    # what we're calculating
    num_comps = 0

    # nodes we haven't yet seen
    nodes_to_examine = list(range(num_nodes))

    # nodes in the current component whose edges we haven't followed yet
    comp_to_examine = []

    # while there are nodes to be accounted for..
    while nodes_to_examine:

        # start with the next unexamined node - start of a new component
        comp_to_examine = [nodes_to_examine[0]]

        # while there are more nodes in the current component..
        while comp_to_examine:

            # examine the next available node in the component
            current = comp_to_examine.pop()

            # all of its neighbors belong to the same component,
            # BUT only schedule them to be examined if they haven't already
            comp_to_examine += [n for n in neighbors[current] if n not in
                                comp_to_examine and n in nodes_to_examine]

            # we're done with this node - we followed all its edges
            nodes_to_examine.remove(current)

        # we're done with the current component
        num_comps += 1

    return num_comps


if __name__ == '__main__':
    print(num_components())
