Title: Simple Graphs
Category: Graphs
Date: 2016-06-26
Position: 20
Summary: The most common type of graph.
Disqus_identifier: 64bd8458-the-most-common-type-of-graph

{% include "context_header.md" %}

Last time we didn't put any restrictions on the general structure of our
graphs. However, the general definition of a graph as just a set of nodes
and a set of edges allows for many different possibilities, including some
that might be undesirable in certain cases. For this reason, there's a
stricter definition that we introduce next.

Simple graph
: A **simple graph** is a graph whose edges never join the same node and any
pair of nodes is joined by at most one edge.

Self-loop
: An edge that has the same node as both endpoints is called a **self-loop**.

Multigraph
: A graph that is not a simple graph is called **multigraph**.

{% from 'img_desc.html' import img_desc %}
{{ img_desc("/images/simple1.png",
            "A multigraph with one self-edge and two parallel edges.",
            "A multigraph with one self-edge and two parallel edges.")}}

{{ img_desc("/images/simple2.png",
            "A simple graph similar to the previous multigraph.",
            "A simple graph similar to the previous multigraph.")}}

From now on, we will work exclusively with simple graphs, unless explicitly
stated otherwise.

{% include "problem_header.md" %}

For this challenge, you need to read a file in the usual format and check
if the graph is a simple graph.

The input is a file where the first line contains two integers, $n$ and
$m$, defining the number of nodes and edges, respectively. The next $m$
lines each contain two integers, representing two nodes that are joined by
an edge.

Output 'YES' or 'NO', depending on whether or not the graph is simple.

{% include "input_header.md" %}

```
4 5
0 1
0 2
0 3
1 3
3 0

```

{% include "output_header.md" %}

```
NO
```

{% include "question_header.md" %}

1. For the following networks, decide if they are simple or multigraphs. If
   they are not simple, explain what would self-loops or multiedges
   represent.
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


{% include "solutions_header.md" %}

The solution to this challenge is hosted on
[Github](https://github.com/leotrs/erdos/blob/master/solutions/graphs/simple.py).


{% include "answers_header.md" %}

1. On Facebook, no one can be friends with themselves, so there are no
   self-loops. Also, two people can't be friends more than once, therefore
   there are no parallel edges. This is a simple graph.

2. The main difference between the social graphs defined by Facebook and
   Twitter is that Facebook's *friendships* area a reciprocal relationship:
   if person `x` is friends with `y`, then `y` must be friends with `x`. On
   the other hand, Twitter's *follows* is not reciprocal: if `x` follows
   `y`, it does not imply that `y` follows `x`. This is an important
   difference which will be studied in further challenges. Moreover, if
   both `x` and `y` follow each other on Twitter, it means there are two
   edges joining them. This makes Twitter a multigraph.

3. Any two cities may have more than one road connecting them. In that
   case, this graph isn't simple.

4. If a device has more than one way to connect to the Internet, and both
   can be active at the same time, then it would establish a parallel edge.
