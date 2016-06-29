Title: Simple Graphs
Category: Graphs
Date: 2016-06-26
Position: 20
Summary: The most common type of graphs.

# Context

Up to this point we haven't put any restrictions on the general structure
of our graphs. However, the general definition of a graph as just a set of
nodes and a set of edges allows for many different possibilities, including
some that might be undesirable in certain cases. For this reason, there's
a stricter definition that we introduce next.

### Simple graph

- A *simple graph* is a graph whose edges never join the same node and any
  pair of nodes is joined by at most one edge.
- An edge that has the same node as both endpoints is called a self-loop.
- A graph that is not a simple graph is called multigraph.


IMAGE1
IMAGE2


## Problem

For this problem, you need to read a file in the usual format and check if
the graph is a simple graph. Assume the graph is undirected.

The input is a file where the first line contains two integers, `n` and
`m`, defining the number of nodes and edges, respectively. The next `m`
lines each contain two integers, representing two nodes that are joined by
an edge.

Output 'YES' or 'NO', depending on whether or not the graph is simple.

### Sample Input

```
4 5
0 1
0 2
0 3
1 3
3 0

```

### Sample Output

```
NO
```

--------------------------------------------------------
[Solution](https://github.com/Leockard/erdos/blob/master/solutions/graphs/simple.py).
