Title: Graph Measures
Category: Measures
Date: 2016-07-22
Position: 10
Summary: Measures help describe a network
Disqus_identifier: 2dae387f-measures-help-describe-a-network

{% include "context_header.md" %}

A graph measure is a number that can be calculated from a graph, used to
describe its properties. They are similar in this respect to the statistics
that are calculated from a sample: statistics are numbers derived from the
sample used to describe it and make inferences about the underlying
sample. Similarly, graph measures

Graph Measure[](#graph-measure)
: A **graph measure** is a number that describes the network and helps us
uncover its underlying structure.

In fact, we have already used a couple of them: both the
[degree](http://erdosnet.work/nodes-and-edges.html) and the
[graph density](http://erdosnet.work/graph-density.html) are graph
measures. It is easy to see how they describe the structure of the network,
the degree holds information about each node's importance and the density
helps differentiate between sparse and dense graphs.

{% include "problem_header.md" %}

Before introducing new graph measures, we are going to acquire some
experience with using the adjacency matrix to compute them.

For this challenge, you need to read a file that contains the adjacency
matrix of an undirected graph and compute the graph measures we already
know.

The input is a file which contains one line with a single integer $n$, the
number of nodes in the network. The following $n$ lines each contain one
row of the adjacency matrix of the network, where each entry is separated
by a space.

Output two lines: the node with maximum degree, and the edge density.

Do not convert the matrix into a different graph representation. The point
of this challenge is to get used to using the adjacency matrix to extract
information about the graph.


{% include "input_header.md" %}

```
4
0 1 1 1
1 0 0 1
1 0 0 0
1 1 0 0
```

{% include "output_header.md" %}

```
0
0.667
```


{% include "solutions_header.md" %}

The solution to this challenge is hosted on
[Github](https://github.com/leotrs/erdos/blob/master/solutions/measures/measures.py).


{% include "question_header.md" %}

1. Compare the difficulty of computing these graph measures using the
   adjacency matrix as opposed to using a different representation (see the
   corresponding challenges for
   [degree](http://erdosnet.work/nodes-and-edges.html) and
   [graph density](http://erdosnet.work/graph-density.html)). Was it more
   or less difficult?

2. The degree of a node is simply the sum of all entries in the
   corresponding row in the adjacency matrix. Why?

3. How can you compute the indegree and outdegree of a node in a directed
   graph from its adjacency matrix?


{% include "answers_header.md" %}

1. Difficulty is subjective and the answer might very well go one way or
   the other.  Nevertheless, the adjacency matrix is the preferred way of
   dealing with graph data when performing calculations such as graph
   measures, because of the ease of representing graph data based on the
   entries $a_{ij}$.  Moreoever, by using the adjacency matrix we can take
   advantage of powerful methods from linear algebra.

2. The $i$-th row of the adjacency matrix has a $1$ at position $j$ if and
   only if $i$ is adjacent to $j$.  By adding up all $1$s in this row, we
   obtain the number of neighbors, or the degree of vertex $i$.

3. Entry $a_{ij}$ of a directed adjacency matrix is equal to $1$ if there's
   a link from $i$ to $j$.  We now have

    $$
    indeg(i) = \sum_{j \in G} a_{ji} \\
    outdeg(i) = \sum_{j \in G} a_{ij}
    $$

    In other words, the indegree is computed by summing all the entries of
    the $i$-th column, while the outdegree is the sum of the $i$-th row.
