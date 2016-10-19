"""
path_length.py
--------------

Solution for measures/peath_length.md.

"""

import networkx as nx


def read_adj_list():
    """Read an adjacency list from stdin and return a nx.Graph."""
    num_nodes = int(input())
    nodes = range(num_nodes)

    graph = nx.Graph()
    graph.add_nodes_from(nodes)

    for node1 in nodes:
        neighbors = [int(n) for n in input().split(' ')]

        for node2 in neighbors:
            graph.add_edge(node1, node2)

    return graph


def dijkstra(graph, node):
    """Compute distances from node to each other node in the network.

    Returns: a list containing the distances, in the order that they appear
    in graph.nodes().  The distance from a node to itself is 0.

    """
    # Final distance dictionary
    distances = {}

    # Store the nodes we have already viisted in a set for quick access
    visited = set([])

    # Store the nodes yet to be visited in a stack, along with the current
    # shortest distance to it.  Even if we've already visited it, we may
    # find a shorter path than the one we already have.
    stack = [(node, 0)]

    while stack:
        node, distance_to_node = stack.pop()
        visited.add(node)
        distances[node] = distance_to_node

        for neighbor in graph.neighbors(node):

            # We want to store each neighbor for later visit only if we haven't
            # visited before or if we have visited it, but the current shortest
            # path to it is longer than the one we just discovered.
            to_visit = neighbor not in visited \
                       or distances[neighbor] > distance_to_node

            if to_visit:
                stack.append((neighbor, distance_to_node + 1))

    # Force ordering of the distances
    return [distances[n] for n in graph.nodes()]


def distances():
    """Read the adjacency  list and return two floats: the  average path length
    and the diameter.

    """
    graph = read_adj_list()

    # Dijkstra's algorithm is a well-known method that will output the
    # distance from a starting node to each other node in the graph.  Since
    # we need the diameter, we need to compute the distance between every
    # possible pair of nodes.  Thus, we run Dijkstra's algorithm starting
    # from each node, and we keep the running total and maximum.
    total = 0
    max_distance = float('-inf')

    for node in graph.nodes():
        distances = dijkstra(graph, node)
        total += sum(distances)
        max_distance = max(max_distance, max(distances))

    num_nodes = graph.number_of_nodes()
    num_pairs = (num_nodes * (num_nodes - 1) / 2)

    # Note that we counted the distance between every pair twice
    average_path_length = (total / 2) / num_pairs

    return average_path_length, max_distance


if __name__ == '__main__':
    print('{:.3f} {:.3f}'.format(*distances()))
