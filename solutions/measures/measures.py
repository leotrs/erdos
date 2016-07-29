"""
measures.py
-----------

Solution for measures/measures.md.

"""


def measures():
    """From the adjacency matrix, return the node with highest degree and the
    graph density.

    """
    num_nodes = int(input())

    # we read the matrix row by row, computing the degree of each node one
    # at a time and keeping track of the number of edges
    degrees = []
    num_edges = 0
    for _ in range(num_nodes):
        row = [int(i) for i in input().split(" ")]
        current_edges = sum(row)
        # the degree of a node is simply the sum of all the entries in its row
        degrees.append(current_edges)
        num_edges += current_edges

    has_max_degree = max(range(num_nodes), key=lambda n: degrees[n])

    # In the matrix, every edge is accounted for twice: if there's an edge
    # between nodes u and v, there will be a '1' in the row corresponding to u,
    # and a '1' in the row corresponding to v.
    num_edges /= 2

    # check http://erdosnet.work/graph-density.html to understand the formula
    max_edges = num_nodes * (num_nodes - 1) / 2
    density = num_edges / max_edges

    return has_max_degree, density


if __name__ == '__main__':
    has_max_degree, density = measures()
    print(has_max_degree)
    print('{:.3f}'.format(density))
