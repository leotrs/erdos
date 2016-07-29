"""
utils.py
--------

Some utilities for erdos' scripts.

"""

import os
import networkx as nx
from matplotlib.pylab import plt


def example_image(graph, filename, show=False):
    """Generates example image with graph.

    Uses nx.draw_networkx_* methods, and matplotlib to draw and save the
    image.

    """
    # positions for all nodes
    pos = nx.spring_layout(graph)

    # each node is labaled by its own name
    labels = {node: str(node) for node in graph.nodes()}

    # configure the image
    plt.figure(figsize=(2, 2))
    plt.axis('off')

    # draw all of the things!
    nx.draw_networkx_nodes(graph, pos, nodelist=graph.nodes(), node_color='r')
    nx.draw_networkx_edges(graph, pos, width=1.0, alpha=0.5, arrows=True)
    nx.draw_networkx_labels(graph, pos, labels, font_size=16)

    # place the file where it belongs
    path = os.path.join(os.environ['ERDOS_PATH'], "content/images", filename)
    plt.savefig(path)

    if show:
        plt.show()
