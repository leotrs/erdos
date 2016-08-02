Title: Paths and Components
Category: Graphs
Date: 07/25/2016
Position: 50
Summary: Components are the "separate" parts of a graph.
Disqus_identifier: fe6f0ebd-components-are-the-separate-parts-of-a-graph


{% include "context_header.md" %}

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
which any two are connected by a path. A graph that only has one component
is called **connected graph**

{% from 'img_desc.html' import img_desc %}
{{ img_desc("/images/paths.png",
            "A graph with three components.",
            "A graph with three components. Note a sole node counts as one more component.")}}


{% include "problem_header.md" %}

In this challenge, you are asked to compute the number of components in a
graph.

The input is a file where the first line contains two integers, $n$ and
$m$, defining the number of nodes and edges, respectively. The next $m$
lines each contain two integers, representing two nodes that are joined by
an edge. Assume undirected edges.

Print out the number of connected components in the graph.


{% include "input_header.md" %}

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

{% include "output_header.md" %}

```
3
```

----------------------------------------


{% include "question_header.md" %}

1. In directed graphs, it is necessary to distinguish between nodes `u` and
   `v` being *connected* and `v` being *reachable* from `u` and vice
   versa. Discuss why this is necessary and how this distinction affects
   the number of components in a directed graph.
2. Consider the network of the World Wide Web. In this network, a node
   represents one website, and nodes `u` and `v` are joined by a *directed*
   edge from `u` to `v` if the former contains a link to the latter.
    + For this network, estimate the number of nodes and edges.
    + Imagine you are writing a new search engine for the WWW. Your
      objective is to index (catalogue) *every* website online. Given
      enough resources, can you achieve this goal? Discuss in terms of
      connected components, as well as the possibility of there being nodes
      with no incoming or outgoing edges (websites with no incoming or
      outgoing links).


{% include "solutions_header.md" %}

[Solution](https://github.com/Leockard/erdos/blob/master/solutions/graphs/paths.py).
