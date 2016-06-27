"""
scripts/nodes_edges.py
==============

Code used for /content/nodes_edges.md.
"""

import networkx as nx
import os
from matplotlib.pylab import plt


def example_pic():
    """Generate the example graph picture."""
    # create graph from edge list
    graph = nx.Graph([(0, 1), (0, 2), (1, 3), (3, 0)])

    # positions for all nodes
    pos = nx.spring_layout(graph)

    # each node is labaled by its own name
    labels = {node: str(node) for node in graph.node.keys()}

    # configure the image
    fig = plt.figure(figsize=(2, 2))
    # ax = fig.add_subplot(111)
    # ax.set_title('A graph with four nodes and four edges.')
    plt.axis('off')

    # draw all of the things!
    nx.draw_networkx_nodes(graph, pos, nodelist=[0, 1, 2, 3], node_color='r')
    nx.draw_networkx_edges(graph, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_labels(graph, pos, labels, font_size=16)

    # place the file where it belongs
    path = os.path.split(os.getcwd())[0]
    path = os.path.join(path, "content/images", "nodes_edges_example.png")
    plt.savefig(path)

    # plt.show()

if __name__ == '__main__':
    example_pic()
