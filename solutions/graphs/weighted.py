"""
weighted.py
-----------

Solution for graphs/weighted.md.

"""


def weighted():
    """Read in the graph and return the node with hightest strength."""
    num_nodes, num_edges = [int(i) for i in input().split(" ")]

    # We don't need to store which node are adjacent, just keep track of
    # the running count of each node's strength, as each weight is read in.
    strengths = {node: 0 for node in range(num_nodes)}
    for edge in range(num_edges):
        node1, node2, weight = [i for i in input().split(" ")]
        weight = float(weight)
        strengths[int(node1)] += weight
        strengths[int(node2)] += weight

    # Maximum key in strengths sorted by their value
    return max(strengths, key=strengths.get)


if __name__ == '__main__':
    print(weighted())
