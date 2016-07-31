Title: Incidence Matrix
Category: Representing Graphs
Date: 2016-07-17
Position: 3
Summary: Graphs can be represented by a matrix
Disqus_identifier: d7c72056-graphs-can-be-represented-by-a-matrix

{% include "context_header.md" %}

The incidence matrix is another matrix representation of a graph. It stores
the same information as other representations, but in a different way.

{% from 'img_desc.html' import img_desc %}
{{ img_desc("/images/incmatrix.png",
            "Example graph.",
            "Exampld graph.")}}

To construct the incidence matrix of the example graph, we first need to
order its edges, not just the nodes. The matrix will have one row for each
node, and one column for each edge.

$$\begin {pmatrix}0  &0  &0  &0  &0 \\ 0  &0  &0  &0  &0 \\ 0  &0  &0  &0  &0 \\ 0  &0  &0  &0  &0 \end{pmatrix}$$

Now, for each edge, going through them in order, we need to write down
which nodes it is *incident* to.

Incident Edge[](#incident-edge)
: An edge is **incident** to a node if the node is at one of the edge's
endpoints.

Starting from the first edge, we see it's incident to nodes `0` and `1`, so
we write it like so

$$\begin {pmatrix}1  &0  &0  &0  &0 \\ 1  &0  &0  &0  &0 \\ 0  &0  &0  &0  &0 \\ 0  &0  &0  &0  &0 \end{pmatrix}$$

Edge number `1` is incident to nodes `0` and `3`:

$$\begin {pmatrix}1  &1  &0  &0  &0 \\ 1  &0  &0  &0  &0 \\ 0  &0  &0  &0  &0 \\ 0  &1  &0  &0  &0 \end{pmatrix}$$

We continue in the same fashion until all edges have been accounted for.

$$\begin{pmatrix} 1  &1  &0  &0  &0 \\ 1  &0  &1  &1  &0 \\ 0  &0  &1  &0  &1 \\ 0  &1  &0  &1  &1 \end{pmatrix}$$


This is the incidence matrix of our graph.

Incidence Matrix[](#adjacency-matrix)
: The **incidence matrix** of a graph with $n$ nodes and $m$ edges is an
$n \times m$ matrix whose rows represent nodes and whose columns represent
edges. The entry in the $i$-th row and $j$-th column indicates whether edge
`j` is incident to node `i`.


{% include "problem_header.md" %}

To solve this challenge, you will need to read a file in adjacency list
form, and output its incidence matrix.

The input will be a file where the first line contains just one integer,
$n$, the number of nodes in the graph. Each of the following $n$ lines
holds a list of space-separated integers, representing the adjacencies of
every node. As before, assume that nodes are labeled from `0` to `n-1`. The
lines are in ascending order of node label, e.g., the first line of the
output contains the adjacencies of node `0`, the second line contains the
adjacencies of node `1`, etc.

Output the incidence matrix of the graph.


{% include "input_header.md" %}

```
4
1 3
0 2 3
1 3
0 1 2
```

{% include "output_header.md" %}

```
1 1 0 0 0
1 0 1 1 0
0 0 1 0 1
0 1 0 1 1
```

{% include "question_header.md" %}

1. For a network with $n$ nodes and $m$ edges, how many $1$s will the
   incidence matrix have?
2. Compare the memory usage of adjacency lists, adjacency matrix and
   incidence matrix for a given network with $n$ nodes and $m$ edges.
3. Compute the incidence matrix for a graph equal to the one in the
   example, but whose edges are labeled in a different order. How are these
   two matrices related?
4. Can you build the incidence matrix for a directed graph following the
   same procedure as in this page? Why or why not?
   1. Propose a better way to build incidence matrices for directed graphs.

{% include "solutions_header.md" %}

[Solution](https://github.com/Leockard/erdos/blob/master/solutions/reprs/incmatrix.py).
