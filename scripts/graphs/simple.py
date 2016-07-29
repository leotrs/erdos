"""simple.py
---------

Code used for graphs/simple.md.

This script uses the .dot graph file format, because networkx doesn't
support drawing multigraphs. This script uses the 'neato' command, which
comes with pygraphviz, which needs graphviz to be installed first.

  apt-get install graphviz
  pip install pygraphviz

"""


import os
import networkx as nx


def example_pic():
    """Generate the example graph picture."""
    path = os.path.join(os.environ['ERDOS_PATH'], "content/images")
    command = 'neato -T png {0} > {1}'

    graph = nx.MultiGraph([(0, 1), (0, 2), (0, 3), (1, 3), (0, 3), (1, 1)])
    tmp_path = '/tmp/simple1.dot'
    nx.drawing.nx_agraph.write_dot(graph, tmp_path)
    os.system(command.format(tmp_path, os.path.join(path, 'simple1.png')))

    graph = nx.Graph([(0, 1), (0, 2), (0, 3), (1, 3)])
    tmp_path = '/tmp/simple2.dot'
    nx.drawing.nx_agraph.write_dot(graph, tmp_path)
    os.system(command.format(tmp_path, os.path.join(path, 'simple2.png')))


if __name__ == '__main__':
    example_pic()
