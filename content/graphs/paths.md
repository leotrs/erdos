Title: Paths and Components
Category: Graphs
Date: 07/25/2016
Position: 50
Summary: Components are the "separate" parts of a graph.
Disqus_identifier: fe6f0ebd-components-are-the-separate-parts-of-a-graph


<div markdown class="erdos-context">
# Context

Networks come in all shapes and sizes, presenting many different properties
and structures. We've already seen how the degree describes the importance
of nodes, and how density quantifies the sparseness of a graph. These two
indicators are calculated from the most basic elements of a graph: its
nodes and edges.

However, there are many other elements that we can identify which are also
of interest when trying to describe a network.

Walk[](#walk)
: A **walk** is an ordered sequence of nodes `(u₁, u₂, ..., uₙ)` where
every consecutive pair of nodes are adjacent. That is, each can be reached
from the previous one by following an edge in the graph.

Path[](#path)
: A **path** is a walk in which every node is unique. This means the walk
does not loop around into itself: it does not self-cross. If there exists a
path from `u` to `v`, we say `u` and `v` are **connected**.

Connected Component[](#component)
: A **connected component**, or simply **component**, is a set of nodes in
which any two are connected by a path.

<div class="img-desc">
  <p><img src="/images/paths.png" title="A graph with three components"></p>
  <p><em>A graph with three components. Note a sole node counts as one more component.</em></p>
</div>
<button type="button" class="btn btn-large btn-default erdos-fadein-challenge">
  Show challenge
  </button>
</div> <!-- erdos-context -->

<div markdown class="erdos-challenge">
<hr />
## Challenge

In this challenge, you are asked to compute the number of components in a
graph.

The input is a file where the first line contains two integers, `n` and
`m`, defining the number of nodes and edges, respectively. The next `m`
lines each contain two integers, representing two nodes that are joined by
an edge. Assume undirected edges.

Print out the number of connected components in the graph.


### Sample Input

```
8 7
0 1
1 2
0 2
3 4
4 6
4 5
6 3
```

### Sample Output

```
3
```

----------------------------------------


## Expansion Questions

1. Make sure these are actually questions,
2. Or at the very least, explain exactly
3. What it is to be discussed


<button type="button" class="btn btn-large btn-default erdos-fadein-solutions">
  Show solutions
  </button>
</div> <!-- erdos-challenge -->

<div markdown class="erdos-solutions">
<hr />
## Solutions

[Solution](https://github.com/Leockard/erdos/blob/master/solutions/graphs/paths.py).