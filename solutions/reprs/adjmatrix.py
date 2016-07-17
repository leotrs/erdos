"""
scripts/adjmatrix.py
==============

Solution /content/reprs/adjmatrix.md.
"""


def adj_matrix():
    """Read the graph from stdin, and output its adjacency matrix."""
    num_nodes = int(input())

    # nodes are just labeled by numbers
    nodes = range(num_nodes)

    # compute each row of the matrix by reading each adjacency list in turn
    matrix = [[0 for _ in nodes] for node in nodes]
    for node in nodes:
        adjacencies = [int(n) for n in input().split(" ")]
        for neighbor in adjacencies:
            matrix[node][neighbor] = 1

    return matrix


if __name__ == '__main__':
    for row in adj_matrix():
        print(" ".join([str(i) for i in row]))
