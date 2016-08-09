Title: Incidence Matrix
Category: Representations
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
3. Compute the incidence matrix for the example graph, but whose edges are
   labeled in a different order. How are these two matrices related?
4. Can you build the incidence matrix for a directed graph following the
   same procedure as in this challenge? Why or why not?


{% include "solutions_header.md" %}

The solution to this challenge is hosted on
[Github](https://github.com/leotrs/erdos/blob/master/solutions/reprs/incmatrix.py).

{% include "answers_header.md" %}

1. There will be $m$ columns in the incidence matrix, one for each edge,
   and two $1$s in each column, for a total of $2m$.

2. The adjacency list representation needs $n$ lists, each of length equal
   to the degree of the node.  In total, we are using $\sum_{u \in G}
   deg(u) = 2m$ slots.  Each slot in the adjacency lists holds a label of
   one node, so the memory usage is $2m \times L$, where $L$ is the amount
   of space that a node label takes.

    Adjacency matrices are of size $n \times n$ and they hold a single
    number in each entry, for a total memory usage of $n^2 \times N$, where
    $N$ is the memory usage of a single number.

    Incidence matrices take $m \times n \times N$.

    The choice of representation will depend on the nature of node labels
    (they can be single numbers, in which case $L$ = $N$, or strings of
    characters, in which case their size will depend on their length), and
    on the graph being sparse or dense.  However, sometimes representations
    are chosen because of how easy it is to manipulate them, not their
    memory usage.

    Another representation that will be covered later is the sparse array,
    which saves much memory compared to these ones, specifically for
    sparse graphs.

3. Since the nodes have the same labels, the rows of the new matrix will be
   in the same order.  However, the columns will represent the same edges
   but in a different order, ultimately yielding the same matrix but with
   permuted columns.

4. Incidence matrices as we have built them don't carry information
   regarding the direction of edges, since in directed graphs there isn't
   such a thing.  For directed graphs, we could write a $-1$ for the source
   node and $+1$ for the target node of each edge.
