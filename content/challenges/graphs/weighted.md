Title: Weighted Graphs
Category: Graphs
Date: 08/17/2016
Position: 35
Summary: Edges can have associated weights.
Disqus_identifier: cddbbede-edges-can-have-associated-weights


{% include "context_header.md" %}


With an undirected graph we represent reciprocal relationships, while with
a directed graph we can study asymmetric ones.  With a weighted graph, we
can represent the *intensity* of each relationship.

In a social network, we represent acquaintances with the presence or
absence of edges.  However, we may also be interested in the *frequency*
with which two people interact with one another.  Two nodes in a social
network may represent two people who only speak every once in a while, or
two best friends who can't stop talking to each other.  Since the presence
or absence of a link doesn't provide frequency or intensity data, we must
add a further feature to our graph.

Weighted Graph
: A graph $G$ is a **weighted graph** when there is a real number
associated to each of its edges.  If nodes $i$ and $j$ are connected by an
edge, then its **weight** is denoted by $w_{ij}$.

{% from 'img_desc.html' import img_desc %}
{{ img_desc("weighted.svg",
    "Weights are usually displayed as labels accompanying each edge.") }}

If one needs to assign arbitrary weights to an unweighted graph, all
present edges receive a weight of $1$, while all absent edges are assigned
a weight of $0$.  If, on the contrary, one needs to convert a weighted
graph into an unweighted graph, all edges with weight less than a
predefined value are cut off and removed from the graph, and all edges with
weight greater than the threshold are assigned the same weight of $1$.
This process is sometimes called **binarization** of a weighted network.

For weighted networks, we need to extend the definition of degree, as we
can't simply count the number of incident edges for each node.

Node Strength
: For a given node `i`, its **strength** is the sum of the weights of all
edges that connect to `i`.


{% include "problem_header.md" %}


For this challenge, you need to read a file and output the node with
highest strength.

The input is a file in which the first line contains two integers, $n$ and
$m$, defining the number of nodes and edges, respectively.  The next $m$
lines each contain three integers, `u`, `v` and `w`, representing two
nodes, `u` and `v`, joined by an edge with weight `w`.

Output one integers, representing the node with the highest strength.

{% include "input_header.md" %}

```
4 5
0 1 0.5
1 3 3.3
2 0 3.1
3 2 0.7
3 0 2.4
```

{% include "output_header.md" %}

```
3
```


{% include "solutions_header.md" %}


The solution to this challenge is hosted on
[Github](https://github.com/leotrs/erdos/blob/master/solutions/challenges/graphs/weighted.py).


{% include "question_header.md" %}


For the following networks, discuss the possible meaning of edge weights.

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


1. As was discussed, edge weights in social networks can indicate the
   frequency of communication between two people, such as, for example,
   average number of interactions per day.

2. Similar to the previous network, edge weights can measure average number
   of interactions per day, in this case @-mentions.  Since @-mentions have
   a source and a target, they preserve the directedness on the network.

3. In road networks, edge weights usually represent geographical distance:
   a link between edges `i` and `j` with weight `w` means there's a road
   between places `i` and `j` that is `w` kilometers long.

4. There are many choices for the meaning of edge weights in this network.
   One of them is the average time in milliseconds it takes a message to
   arrive from one device to the next.

Remark
: In the first and second examples, edge weights represent similar concepts
both in directed and undirected networks.

Remark
: In the first two examples, higher weights represent a stronger connection
(more frequent interaction), while in the last two, smaller weights
represent a stronger connection (closer entities, either geographically, or
temporally).
