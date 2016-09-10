"""
clustering.py
-------------

Solution for measures/clustering.md.

"""

import numpy as np


def clustering():
    """Read the adjacency matrix, and return each node's local clustering
    coefficient.

    """
    num_nodes = int(input())

    # Read the matrix row by row
    matrix = np.empty((num_nodes, num_nodes), int)
    for i in range(num_nodes):
        matrix[i] = [int(i) for i in input().split(" ")]

    # The number of triangles with a vertex in a node u is computed from
    # the diagonal of the third power of the adjacency matrix.  Recall the
    # ij-th element of the k-th power of the adjacency matrix equals the
    # number of paths of length k from node i to node j.  Now, every
    # triangle defines two paths of length 3 from each of its vertices to
    # itself.  For example, if u, v, w form a triangle, and we're
    # interested v's clustering coefficient, we want to count the number of
    # triangles with a vertex in v.  If we look at the vv-th entry in the
    # diagonal of matrix³, we find the number of length 3 paths from v to
    # itself.  Since the u, v, w triangle defines two such paths (mainly
    # v-u-w-v and v-w-u-v), we need to divide this entry by 2 to get the
    # real number of triangles with a vertex in v.
    # We proceed in this manner for all nodes at the same time.
    A = matrix
    A2 = np.dot(A, A)
    A3 = np.dot(A2, A)
    triangles = np.diagonal(A3) / 2

    # The number of pairs adjacent to a node u is just the number of
    # possible pairs among its neighbors.  If u's degree is k, there are
    # C(2, k) pairs, where C(n, k) is read "n choose k", and denotes the
    # binomial coefficients.  In this case, C(2, k) = k(k-1)/2
    degrees = np.dot(A, np.ones(num_nodes))
    pairs = [k * (k-1) / 2 for k in degrees]

    # The clustering coefficients are the ratio of both quantities. Careful
    # not to divide by zero.
    coefficients = [tri/pairs if pairs else 0
                    for tri, pairs in zip(triangles, pairs)]

    return coefficients


if __name__ == '__main__':
    print(' '.join(['{:.3f}'.format(c) for c in clustering()]))
