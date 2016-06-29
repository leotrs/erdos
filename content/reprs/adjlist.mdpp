Title: Adjacency Lists
Category: Representing Graphs
Date: 2016-06-26
Position: 1
Summary: Graphs can be represented by lists defining the adjacencies of every node.

In the previous two problems, we read a graph from a file which listed
every edge at once. Implicitly, we were representing the graph as a list of
edges, eveery edge joining two nodes.

For this problem, we are going to represent a graph in a different, more
succint way. For every node `u`, we want to create a list defining the
nodes adjacent to `u`.

Consider a graph with `n` nodes and `m` edges. In the former
representation, the file contained one line to define the number of nodes
and edges, `n` and `m`, and one line for each edge, `m + 1` lines in
total. In the new representation, our file will still need one line for `m`
and `n`, but only `n` lines will follow, one for each node's adjacencies.

As we saw before, a graph can hold up to `n(n+1)/2` edges in total, so
that, in general, we will have `n < m`, and therefore, our new graph
representation will be in general shorter than the previous one, judging by
the number of lines.

For this problem, you need to read a file representing a graph in the
previous, long, format, and output it in the new, shorter one.

### Input

The input is a file where the first line contains two integers, `n` and
`m`, defining the number of nodes and edges, respectively. The next `m`
lines each contain two integers, representing two nodes that are joined by
an edge. Assume undirected edges.

### Output

Write `n` lines, where each line holds a list of space-separated integers,
representing the adjacencies of every node. As before, assume that nodes
are labeled from 0 to n. Write the lines in ascending order of node label,
e.g., the first line of the output should contain the adjacencies of node
`0`, the second line should contain the adjacencies of node `1`, etc. Print
each adjacency list in ascending order.

### Test Input

```
4 4
0 1
0 2
1 3
3 0

```

### Test Output

```
1 2 3
0 3
0
0 1
```

--------------------------------------------------------
[Solution](https://github.com/Leockard/erdos/blob/master/solutions/reprs/adjlist.py).
