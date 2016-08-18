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
{{ img_desc("directed.svg",
            "A graph with four nodes and five directed edges.")}}

Outdegree
: For a given node `u`, the number of outgoing edges from `u` is called
**outdegree** of `u`.

Indegree
: The number of incoming edges to `u` is the **indgree** of `u`.


{% include "problem_header.md" %}


For this challenge, you need to read a file and output two integers: the
node with the highest number of *outgoing* edges and the node with the
highest number of *incoming* edges.

The input is a file in which the first line contains two integers, $n$ and
$m$, defining the number of nodes and edges, respectively.  The next $m$
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


{% include "solutions_header.md" %}

The solution to this challenge is hosted on
[Github](https://github.com/leotrs/erdos/blob/master/solutions/graphs/directed.py).


{% include "question_header.md" %}

For the following networks, decide if they are directed or undirected.

1. The social network of your immediate Facebook friends. In this graph,
  every node stands in for one of your friends, and there is an edge
  between two nodes if the corresponding persons are friends with each
  other.

2. The social network of your followers on Twitter. In this graph, every
  node stands for one user, and each edge between users A and B
  represents the relationship "A follows B".

3. The transportation network of roads between cities in a country. In
  this graph, every node represents a city and there is one edge
  between any two cities for each road connecting them.

4. The information network of devices connected to the internet
  (computers, routers, cell phones, etc), where every node represents a
  device and every edge represents physical or wireless connections
  to network devices.


{% include "answers_header.md" %}

1. The relationship "`x` is friends with `y`" on Facebook is always
   symmetrical: it always implies that "`y` is friends with `x`" too. This
   is an undirected network.

2. In contrast, "`x` follows `y`" on Twitter doesn't imply that "`y`
   follows `x`" back. This relationship is asymmetrical, and the graph is
   directed.

3. Most roads between cities can be traveled in both directions, so the
   relationship "there's a road that goes from `this` city to `that` city"
   will almost certainly be reciprocal. If at least one of the roads was
   one way only, the network would be directed instead.

4. The question is vague on purpose, as the answer depends on the exact
   definition of the relationship. If the relationship is "device `x`
   connects to the Internet through device `y`", then it won't be
   reciprocal (as my cell phone connects to the Internet through my router
   but not the other way around). If the relationship is "devices `x` and
   `y` share online data" then it must be reciprocal and the graph
   undirected.
