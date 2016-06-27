"""
solutions/nodes_edges.py
========================

Solution for /content/nodes_edges.md.
"""

def nodes_edges():
    """Read the graph from stdin, and return which node has the most edges."""
    num_nodes, num_edges = [int(i) for i in input().split(" ")]
    nodes = range(num_nodes)
    edges = []

    for _ in range(num_edges):
        edges.append([int(n) for n in input().split(" ")])

    degree = {node: len([e for e in edges if node in e])
              for node in nodes}

    return sorted(degree.keys(), key=degree.get)[-1]


if __name__ == '__main__':
    print(nodes_edges())
