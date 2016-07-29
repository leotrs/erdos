"""
triangles.py
------------

Solution for measures/triangles.md.

"""

import numpy as np


def triangles():
    """From the adjacency matrix, return the number of triangles."""
    num_nodes = int(input())

    # read the matrix row by row
    matrix = np.empty((num_nodes, num_nodes), int)
    for i in range(num_nodes):
        matrix[i] = [int(i) for i in input().split(" ")]

    trace = np.trace(np.dot(np.dot(matrix, matrix), matrix))

    return int(trace/6)


if __name__ == '__main__':
    print(triangles())
