Title: Nodes and Edges
Category: Graphs
Date: 2016-06-26
Position: 10
Summary: Graphs are made of nodes and edges
Disqus_identifier: 81be0b7a-graphs-are-made-of-nodes-and-edges

{% include "context_header.md" %}

When we study a real-life network, we usually refer to an underlying
mathematical object, called a *graph*. We use the terms *network* and
*graph* interchangeably throughout the problem sets.

Graph
: A **graph** is defined as a set of **nodes**, defining the locations,
entities or elements of the graph, and a set of **edges**, representing the
relationships between two nodes. Nodes are also called **vertices**, and
edges are sometimes called **links**.

Graph Theory
: The field of mathematics concerned with the study of graphs is called
**graph theory**. Network Science relies heavily on graph theory, as every
network is represented by a graph.

{% from 'img_desc.html' import img_desc %}
{{ img_desc("/images/nodes_edges_example.png",
            "A graph with four nodes and four edges.",
            "A graph with four nodes and four edges.")}}

Both nodes and edges can have many different properties. One of the most
fundamental properties of graphs is the number of edges connecting to each
node. This gives a rough measure of importance, size, or
connectedness. These concepts will become clearer as we delve deeper into
Network Science and Graph Theory.

Degree
: The number of edges connecting to a node `u` is called the **degree** of
`u`.

Adjacent or Neighbors
: If two nodes `u` and `v` are connected by an edge, they are called
**adjacent** or **neighbors**. If `u` and `v` are adjacent, we write `u ~
v`.

{% include "problem_header.md" %}

There are many ways to represent a graph, for now, we choose the simplest
possible way to do it, where each node is represented by a single integer,
and each edge by a pair of two nodes. In this way, we can represent a graph
in a file by defining the number of nodes, edges, and each edge in a
separate line.

For this challenge, you need to read a file in this format and find the
node with the most edges (or highest degree).

The input is a file in the aforementioned format, where the first line
contains two integers, $n$ and $m$, defining the number of nodes and edges,
respectively. The next $m$ lines each contain two integers, representing
two nodes that are joined by an edge. If there are $n$ nodes, they are
assumed to be labeled by the integers from `0` to `n - 1`.


Output the node with the highest degree.

{% include "input_header.md" %}

```
4 4
0 1
0 2
1 3
3 0

```

{% include "output_header.md" %}

```
0
```

{% include "question_header.md" %}


1. We've defined one measurement of the "importance" of a node, its
   degree. What might be other ways of measuring the importance of a node
   in a network?
2. Consider the social network of your immediate Facebook friends. In this
   graph, every node stands in for one of your friends, and there is an
   edge between two nodes if the corresponding persons are friends with
   each other.
    1. Estimate the number of nodes and edges in this network.
    2. What is your degree in this network?
    3. Consider the extended network of all Facebook users. Estimate the
      number of nodes and edges. (Doesn't have to be an exact number.)
3. Discuss the possibility of measuring the "importance" of an edge in a
   network. Can you come up with a proposal for how to measure it?


{% include "solutions_header.md" %}

The solution to this challenge is hosted on
[Github](https://github.com/leotrs/erdos/blob/master/solutions/graphs/nodes_edges.py).


{% include "answers_header.md" %}

1. Roughly speaking, the importance of a node is called *centrality*. There
   are many ways to measure centrality, such as *betweenness
   centrality*[^1], *closeness centrality*[^2], *eigenvector
   centrality*[^3], *degree centrality*[^4] (or *degree*), and *Katz
   centrality*[^5].  We will see each of them in turn in later challenges.

2. According to one source[^6], young adult Facebook users have a median of
    $300$ friends. For the sake of example, let's say I have exactly $300$
    friends on Facebook. Since I am connected to each one of them, my
    degree in this network is $300$, while the total number of nodes is
    $301$.

    Now, estimating the number of edges can pose a challenge. Consider the
    nature of your Facebook friends. Most social networks can be
    partitioned in three big groups: close friends, family, and
    acquaintances. Now, most if not all of my close friends know each
    other, and the same is true for members of my family. Some of my
    friends know some of my family too. In other words, these two groups
    are very tightly knit, or *dense*, within themselves, while the
    connections between them are few, or *sparse*. And what about
    acquaintances? Well, some of them know some of my friends and/or family
    and some don't. In other words, it's a mixed bag of nuts.

    Depending on the size of these groups, the total number of edges in the
    graph can vary considerably. Let's say I have $35$ really close
    friends, all of whom know each other (from school, say), $15$ family
    members, all of whom know each other, and a long list of $250$
    acquaintances, who know some of my other connections to varying
    degrees, say $10$ on average.  That's $595$ edges within my group of
    friends, $105$ in my family plus $1250$ edges from acquaintances, for a
    total of $1950$. In contrast, if I have a big family, say $30$ members,
    all other things being equal, the total number of edges would be
    $2280$. And if I was more popular in school, it might get to more than
    $3000$.

    To estimate the total size of all of Facebook is a different matter.
    The problem with estimating real-life networks is that even though it
    is possible to gather the data in principle, it can be too large for
    meaningful analysis.  Furthermore, There are Facebook "users" who are
    not human, e.g. company or automated accounts, and there are also a
    number of users with more than one account. In these cases, we need
    careful and sophisticated analysis. Some sources[^7]$^,$[^8], for example,
    estimate the number of users just shy of one billion, and the number of
    edges in the tens of billions.

3. Just like nodes, edges are "first-class citizens" in networks. Since
   they define the relationships between nodes, they are as important, if
   not more. Since every edge is connected to only two edges at most, there
   isn't a counterpart for node degree in the case of edges. However, there
   are many ways to measure edge centrality[^9]$^,$[^10]$^,$[^11].


{% include 'footnote_header.md' %}

[^1]: [Betweenness centrality](https://en.wikipedia.org/wiki/Betweenness_centrality)
[^2]: [Closeness centrality](https://en.wikipedia.org/wiki/Centrality#Closeness_centrality)
[^3]: [Eigenvector centrality](https://en.wikipedia.org/wiki/Centrality#Eigenvector_centrality)
[^4]: [Degree centrality](https://en.wikipedia.org/wiki/Centrality#Degree_centrality)
[^5]: [Katz centrality](https://en.wikipedia.org/wiki/Katz_centrality)
[^6]: [6 new facts about Facebook](http://www.pewresearch.org/fact-tank/2014/02/03/6-new-facts-about-facebook/)
[^7]: [One Trillion Edges: Graph Processing at Facebook-Scale](http://www.vldb.org/pvldb/vol8/p1804-ching.pdf)
[^8]: [The Anatomy of the Facebook Social Graph](https://arxiv.org/pdf/1111.4503.pdf)
[^9]: [A novel measure of edge centrality in social networks](http://www.sciencedirect.com/science/article/pii/S0950705112000160)
[^10]: [Spanning Edge Centrality: Large-scale Computation and Applications](https://www.cs.cmu.edu/~jkoutis/papers/spanning_edge.pdf)
[^11]: [Edge betweenness centrality](https://reference.wolfram.com/language/ref/EdgeBetweennessCentrality.html)
