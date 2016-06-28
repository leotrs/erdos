"""
solutions/simple.py
=====================

Solution for /content/simple.md.

"""


def simple():
    """Read a graph and output 'YES' if the graph is simple, or 'NO' otherwise.

    This function checks every read edge on the fly, and does not need to
    read the whole file. It will break as soon as it sees an invalid edge
    (self-loop or multi-edge).

    """
    num_nodes, num_edges = [int(i) for i in input().split(" ")]

    # we don't need to store the nodes
    # nodes = range(num_nodes)

    # read each edge and quit as soon as we find an invalid one
    edges = []
    is_simple = True
    for _ in range(num_edges):
        edge = sorted([int(n) for n in input().split(" ")])
        if edge in edges or edge[0] == edge[1]:
            is_simple = False
            break
        else:
            edges.append(edge)

    print('YES' if is_simple else 'NO')


if __name__ == '__main__':
    simple()
