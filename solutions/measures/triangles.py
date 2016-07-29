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

    # Consider three nodes i, j, and k. One way to determine if they form a
    # triangle is the following. Say A is the adjacency matrix of the
    # graph, and aᵢⱼ is the entry in the i-th row and j-th column of A. If
    # i and j are adjacent, then aᵢⱼ is equal to 1. If i, j, and k form a
    # triangle, we need all of aᵢⱼ, aᵢₖ, and aₖⱼ all equal to 1. This happens
    # if and only if the product aᵢⱼ * aᵢₖ * aₖⱼ is also equal to 1.
    # Knowing this, we can count the number of triangles that include node i
    # by summing up over all j and k:
    #
    #     ∑ⱼ∑ₖ aᵢⱼ aᵢₖ aₖⱼ,
    #
    # which can be rearranged as follows:
    #
    #     ∑ⱼ aᵢⱼ ( ∑ₖ aᵢₖ aₖⱼ).
    #
    # Now, the term inside parentheses is equal to bᵢⱼ, on the i-th row,
    # j-th column of A², the second power of the adjacency matrix A. (This
    # fact can be checked in any introductory matrix algebra book.) Observe
    # that the expression bᵢⱼ = aᵢₖ aₖⱼ is equal to 1 if and only if there
    # is a length-2 path from i to j, going through k. By summing up over
    # k, we obtain that bᵢⱼ is the total number of length-2 paths starting
    # in i and ending in k. This will be used later.
    #
    # Now, we have
    #
    #     ∑ⱼ aᵢⱼ * bⱼᵢ.
    #
    # By the same token as before, this expression is equal to cᵢᵢ, the
    # i,i-th entry in the *third* power of A. (Where we have used the fact
    # that A² is a symmetryc matrix to say that bᵢⱼ = bⱼᵢ.)
    #
    # In all, we have proved that the cᵢᵢ entry in the third power of A
    # holds the number of triangles that include node i. There's still two
    # more observations we have to make before we are done:
    #
    # 1. The entry cᵢᵢ lies at the diagonal of A³, for every i.
    #
    # 2. Every triangle has three nodes, so if i, j, and k form a triangle
    #    and we count the triangles involving i, j, and k separately, we
    #    will be counting the same triangle three times, one for each node.
    #
    # 3. We discussed how the entries of A² count the number of length-2
    #    paths between pairs of nodes. Similarly, the entries of A³ hold
    #    the number of length-3 paths. Thus, cᵢᵢ holds the number of
    #    length-3 paths that start and end in i. For every triangle, there
    #    are two such paths, for if i, j, and k are a triangle, then both
    #    i-j-k and i-k-j are length-3 paths that start and end in i.
    #
    # Remark 1 says we need only look at the diagonal of A³, while
    # observations 2 and 3 indicate we are counting every triangle six
    # times in total.

    A = matrix
    A2 = np.dot(A, A)
    A3 = np.dot(A2, matrix)

    # the trace is the sum of all diagonal entries in a matrix
    #     trace(A) = ∑ᵢ aᵢᵢ
    trace = np.trace(A3)

    return int(trace/6)


if __name__ == '__main__':
    print(triangles())
