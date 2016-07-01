"""
scripts/density.py
==================

Code used for /content/density.md.
"""

import networkx as nx
import os
from matplotlib.pylab import plt


def example_pic():
    """Generate the example graph picture."""

    def draw_graph(graph):
        """Draws the graph using nx.draw_networkx_*."""
        # positions for all nodes
        pos = nx.circular_layout(graph)

        # draw all of the things!
        nx.draw_networkx_nodes(graph, pos, nodelist=graph.nodes(),
                               node_color='r', node_size=100)
        nx.draw_networkx_edges(graph, pos, width=1.0, alpha=0.5)

        # labels = {node: str(node) for node in graph.node.keys()}
        # nx.draw_networkx_labels(graph, pos, labels, font_size=16)

    # configure and config the image
    plt.figure(figsize=(5, 2.5))
    plt.axis('off')

    # create two graphs with the same number of edges
    num_nodes = 10

    # create a fully connected graph
    complete = nx.complete_graph(num_nodes)

    # all following drawings go into the first row, second column
    axes = plt.subplot(121)
    plt.setp(axes.get_xaxis(), visible=False)
    plt.setp(axes.get_yaxis(), visible=False)

    print(type(axes))
    print(dir(axes))

    draw_graph(complete)

    # create a sparse graph
    prob = 0.25                 # probability of an edge between any two nodes
    sparse = nx.erdos_renyi_graph(num_nodes, prob)

    # all following drawings go into the first row, second column
    axes = plt.subplot(122)
    plt.setp(axes.get_xaxis(), visible=False)
    plt.setp(axes.get_yaxis(), visible=False)
    draw_graph(sparse)

    # place the file where it belongs
    path = os.path.join(os.environ['ERDOS_PATH'], "content/images", "density.png")
    plt.savefig(path)
    plt.show()


if __name__ == '__main__':
    example_pic()
