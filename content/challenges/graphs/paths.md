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

Walk
: A **walk** is an ordered sequence of nodes `(u₁, u₂, ..., uₙ)` where
every consecutive pair of nodes are adjacent.  That is, each can be reached
from the previous one by following an edge in the graph.

Cycle
: A **cycle** is a walk whose starting and ending nodes are the same.  It
is also called a **closed walk**.

Path
: A **path** is a walk in which every node is unique.  This means the walk
does not loop around into itself: it does not self-cross.  If there exists
a path from `u` to `v`, we say `u` and `v` are **connected**.

Connected Component
: A **connected component**, or simply **component**, is a set of nodes in
which any two are connected by a path. A graph that only has one component
is called **connected graph**

{% from 'img_desc.html' import img_desc %}
{{ img_desc("paths.svg",
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


{% include "solutions_header.md" %}

The solution to this challenge is hosted on
[Github](https://github.com/leotrs/erdos/blob/master/solutions/graphs/paths.py).


{% include "question_header.md" %}

1. In directed graphs, it is necessary to distinguish between nodes `u` and
   `v` being *connected*, and `v` being *reachable* from `u` and vice
   versa. Discuss why this is necessary and how this distinction affects
   the number of components in a directed graph.

2. Consider the network of the World Wide Web. In this network, a node
   represents one website, and nodes `u` and `v` are joined by a *directed*
   edge from `u` to `v` if the former contains a link to the latter.
    + For this network, estimate the number of nodes and edges.
    + Imagine you are writing a new search engine for the WWW. Your
      objective is to index (catalogue) every website online. Given enough
      resources, can you achieve this goal? Discuss in terms of connected
      components, as well as the possibility of there being nodes with no
      incoming or outgoing edges (websites with no incoming or outgoing
      links).


{% include "answers_header.md" %}

1. In an undirected graph, if node `u` is reachable from `v`, then `v` is
   also reachable from `u`, because every edge can be traversed in both
   directions.  However, in a directed graph, since edges have an
   orientation and can only be traversed in one direction, we need to
   modify our definition of path and connected component.

    Directed Path
    : A **directed path** is an ordered set of nodes `(u₁, u₂, ..., uₙ)` in
    which every consecutive pair `uᵢ`, `uᵢ₊₁` are such that there is an
    edge *from* `uᵢ` *to* `uᵢ₊₁`. If there is a directed path from `u` to
    `v`, we say `v` is **reachable** from `u`.

    Strongly Connected Component
    : In a directed graph, a **strongly connected component** is a subset
    of nodes in which every node is reachable from all the others.


2. Estimating the size of the WWW is not a simple task.  Different
   sources[^1] [^2] [^3] agree that there are billions of webpages and tens
   if not hundreds of billions of hyperlinks, but the exact number seems
   elusive.  Why is it so hard?  Part of it is because the size is so large
   that the time and space it takes to go through the whole graph are
   massive, and we require complex indexing[^4] algorithms to do it
   correctly.  Another problem is one that arises from the structure of the
   strongly connected components of the WWW graph.  Consider a website
   called "my-site" that contains links to different outside domains, but
   no website links directly to "my-site".  This means that if we start at
   an arbitrary website (say, google.com) and try to *crawl* to all others,
   indexing them as we see them, we are never going to reach "my-site".  In
   other words, "my-site" doesn't belong to the strongly connected
   component of websites that includes google.com.[^5]

    In fact, there's a popular term for websites that aren't indexed by
    search engines: the *deep web*[^6].  Contrary to popular belief, not
    all websites in the deep web are related to criminal or otherwise
    nefarious activities.  It's just a name for the websites that haven't
    yet been reached by search engines. (A related but different term is
    *dark net*, more closely related to illegal activities.)

    With such complicated structure, we need a useful way of visualizing
    the structure of this graph.  One such way is by using a *bow tie*
    diagram.  By using algorithms to crawl path of the WWW and determine
    its components, websites can be arranged in such a way that the overall
    structure resembles a bow
    tie. [Here](http://www.nature.com/nature/journal/v405/n6783/fig_tab/405113a0_F1.html)
    is an example.[^7]


{% include 'footnote_header.md' %}

[^1]: [Number of websites hits a BILLION](http://www.dailymail.co.uk/sciencetech/article-2759636/Number-websites-hits-BILLION-counting-Tracker-reveals-new-site-registered-SECOND.html).

[^2]: [Hyperlink Graphs](http://webdatacommons.org/hyperlinkgraph/).

[^3]: [Wikipedia: World Wide Web - Statistics](https://en.wikipedia.org/wiki/World_Wide_Web#Statistics).

[^4]: [Google: Crawling and Indexing](https://www.google.com/insidesearch/howsearchworks/crawling-indexing.html).

[^5]: We are assuming the only way to index a website is by navigating to
it from another one. This is not entirely true, but we have simplified the
indexing process for illustration purposes.

[^6]: [Deep Web](https://en.wikipedia.org/wiki/Deep_web).

[^7]: [The web is a bow tie](http://www.nature.com/nature/journal/v405/n6783/full/405113a0.html).
