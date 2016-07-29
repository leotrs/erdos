"""
utils.py
--------

Some utilities for erdos' scripts.

"""

import os
import networkx as nx
from matplotlib.pylab import plt


LAYOUT_DICT = {'spring': nx.spring_layout, 'shell': nx.shell_layout}


def example_image(graph, filename, layout='spring', edge_labels=False,
                  node_labels=False, show=False):
    """Generates example image with graph.

    Uses nx.draw_networkx_* methods, and matplotlib to draw and save the
    image.

    """
    # positions for all nodes
    pos = LAYOUT_DICT[layout](graph)

    # configure the image
    plt.figure(figsize=(2, 2))
    plt.axis('off')

    # draw all of the things!
    nx.draw_networkx_nodes(graph, pos, nodelist=graph.nodes(), node_color='r')
    nx.draw_networkx_edges(graph, pos, width=1.0, alpha=0.5, arrows=True)

    if node_labels:
        nlabels = {node: str(node) for node in graph.nodes()}
        nx.draw_networkx_labels(graph, pos, nlabels, font_size=16)

    if edge_labels:
        elabels = {edge: str(idx) for idx, edge in enumerate(graph.edges())}
        nx.draw_networkx_edge_labels(graph, pos, elabels)

    # place the file where it belongs
    path = os.path.join(os.environ['ERDOS_PATH'], "content/images", filename)
    plt.savefig(path)

    if show:
        plt.show()
