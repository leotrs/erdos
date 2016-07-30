Title: Directed Graphs
Category: Graphs
Date: 2016-06-26
Position: 30
Summary: Edges can have a direction
Disqus_identifier: fd6d2c66-edges-can-have-a-direction

{% include "context_header.md" %}

Edges in a graph join any two nodes, representing a relationship between
them. Sometimes, this relationship can be bilateral (or symmetric), e.g.,
"Alice and Bob are friends of each other", while other times, the
relationship can be unilateral (or asymmetric): "Alice follows Bob's blog
(but not the other way around)".

Directed graph[](#directed)
: A graph is **directed** when the edges represent an asymmetric
relationship. In this case, every edge is represented by an *oredered pair*
of nodes: `(u, v)`, with the first one sometimes being called the *source*
and the second, the *target*.

Undirected graph[](#undirected)
: A graph is **undirected** when the relationship between nodes is
symmetrical. In this case, every edge is written as an *unordered pair* of
nodes: `{u, v}`.

When drawing an undirected graph, we draw the edges as lines or arcs,
whereas, for directed graphs, we draw them with arrows stemming from source
nodes into target nodes.

{% from 'img_desc.html' import img_desc %}
{{ img_desc("/images/directed_example.png",
            "A graph with four nodes and five directed edges.",
            "A graph with four nodes and five directed edges.")}}

Outdegree[](#Outdegree)
: For a given node `u`, the number of outgoing edges from `u` is called
**outdegree** of `u`.

Indegree[](#Indegree)
: The number of incoming edges to `u` is the **indgree** of `u`.

{% include "problem_header.md" %}

For this challenge, you need to read a file from stdin and output two
integers: the node with the highest number of *outgoing* edges and the node
with the highest number of *incoming* edges.


The input is a file in which the first line contains two integers, `n` and
`m`, defining the number of nodes and edges, respectively. The next `m`
lines each contain two integers, `u` and `v`, representing two nodes that
are joined by a directed edge, `(u, v)` with `u` as the source and `v` as
the target.

Output two integers, representing the nodes with the highest outdegree and
highest indegree.

{% include "input_header.md" %}

```
4 5
0 1
1 3
2 0
3 2
3 0
```

{% include "output_header.md" %}

```
0 3
```

{% include "question_header.md" %}

1. For the following networks, decide if they are simple or multigraphs. If
   they are not simple, explain what would self-loops or multiedges
   represent.
    + The social network of your immediate Facebook friends. In this graph,
      every node stands in for one of your friends, and there is an edge
      between two nodes if the corresponding persons are friends with each
      other.
    + The social network of your followers on Twitter. In this graph, every
      node stands for one user, and each edge between users A and B
      represents the relationship "A follows B".
    + The transportation network of roads between cities in a country. In
      this graph, every node represents a city and there is one edge
      between any two cities for each road connecting them.
    + The information network of devices connected to the internet
      (computers, routers, cell phones, etc), where every node represents a
      device and every edge represents physical or wireless connections
      to network devices.

{% include "solutions_header.md" %}

[Solution](https://github.com/Leockard/erdos/blob/master/solutions/graphs/directed.py).
