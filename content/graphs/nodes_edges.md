Title: Nodes and edges
Category: Graphs
Date: 2016-06-26
Position: 10
Summary: Graphs are made of nodes and edges

# Context

**Graph** is the mathematical term for a network, and we use these two terms
interchangeably throughout the problem sets.

Graph[](#graph)
: A **graph** is defined as a set of **nodes**, defining the locations, sites or
elements of the graph, and a set of **edges**, representing the relationships
between two nodes.

![Couldn't load image](/images/nodes_edges_example.png A graph with four
 nodes and four edges.)

There are many ways to represent a graph, and both nodes and edges can have
many different properties. For now, we choose the simplest possible way to
represent a graph, where each node is represented by a single integer, and
each edge by a pair of two nodes.

With these conventions, we can represent a graph in a file by defining the
number of nodes, edges, and each edge in a separate line.

Degree[](#degree)
: The number of edges connecting to a node `u` is called the **degree** of
`u`.

Adjacent / Neighbors[](#neighbors)
: If two nodes `u` and `v` are connected by an edge, they are called
**adjacent** or **neighbors**.


## Problem


For this problem, you need to read a file in this format and find the node
with the most edges or *highest degree*.


The input is a file in the aforementioned format, where the first line
contains two integers, `n` and `m`, defining the number of nodes and edges,
respectively. The next `m` lines each contain two integers, representing two
nodes that are joined by an edge.


Output the node with the highest degree.

### Sample Input

```
4 4
0 1
0 2
1 3
3 0

```

### Sample Output

```
0
```

--------------------------------------------------------
[Solution](https://github.com/Leockard/erdos/blob/master/solutions/graphs/nodes_edges.py).


## Expansion Questions

1. this is a question?
2. this is a question?
3. this is a question?
