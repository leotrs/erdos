"""
scripts/incmatrix.py
====================

Code used for /content/incmatrix.md.

"""

import os
import networkx as nx
from matplotlib.pylab import plt


def example_pic():
    """Generate the example graph picture."""
    # create graph from edge list
    graph = nx.Graph([(0, 1), (1, 2), (2, 3), (3, 1), (1, 2), (0, 3)])
    # positions for all nodes
    pos = nx.spring_layout(graph)

    # each node is labaled by its own name
    labels = {node: str(node) for node in graph.nodes()}
    edge_labels = {edge: str(idx) for idx, edge in enumerate(graph.edges())}

    # configure the image
    plt.figure(figsize=(2, 2))
    plt.axis('off')

    # draw all of the things!
    nx.draw_networkx_nodes(graph, pos, nodelist=[0, 1, 2, 3], node_color='r')
    nx.draw_networkx_edges(graph, pos, width=1.0, alpha=0.5, arrows=True)
    nx.draw_networkx_labels(graph, pos, labels, font_size=16)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels)

    # place the file where it belongs
    path = os.path.join(os.environ['ERDOS_PATH'], "content/images", "incmatrix.png")
    plt.savefig(path)

    # plt.show()


if __name__ == '__main__':
    example_pic()
