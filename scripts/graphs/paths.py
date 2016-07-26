"""
paths.py
--------

Code used for graphs/paths.md.

"""

import networkx as nx
import os
from matplotlib.pylab import plt


def example_pic():
    """Generate the example graph picture."""
    # create graph from edge list
    graph = nx.Graph([(0, 1), (1, 2), (0, 2), (3, 4), (4, 6), (4, 5), (6, 3)])
    graph.add_node(7)
    nodes = range(8)

    # positions for all nodes
    pos = nx.shell_layout(graph)

    # each node is labaled by its own name
    labels = {node: str(node) for node in graph.node.keys()}

    # configure the image
    plt.figure(figsize=(3, 3))
    plt.axis('off')

    # draw all of the things!
    nx.draw_networkx_nodes(graph, pos, nodelist=nodes, node_color='r')
    nx.draw_networkx_edges(graph, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_labels(graph, pos, labels, font_size=16)

    # place the file where it belongs
    path = os.path.join(os.environ['ERDOS_PATH'], "content/images",
                        "paths.png")
    plt.savefig(path)

    # plt.show()


if __name__ == '__main__':
    example_pic()
