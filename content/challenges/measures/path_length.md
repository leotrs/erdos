Title: Path Lengths
Category: Measures
Date: 10/19/2016
Position: 40
Summary: Average path length and diameter.
Disqus_identifier: d3d41ed8-average-path-length-and-diameter


{% include "context_header.md" %}


An important way to describe networks is by how far apart its nodes are.
Consider an airport network, where each node is an airport and two nodes
are joined if there is a civilian plane route going from one to the other.
In this network, it's easy to say how separate two nodes are, because they
are geographically determined, and we can just measure the distance between
them.

But what happens if we're looking at a social network?  Is the distance
between two nodes the physical distance between the two people they
represent?  And what happens if the people travel and meet?

To generalize the notion of distance to networks where physical distances
don't seem to be the right choice, we introduce a distance concept
intrinsic to graphs.

Distance
: In graph-theoretical terms, the **distance** between two nodes is the
length of the shortest path joining them.  If there is no such path, the
distance is $\infty$.  The distance from a node to itself is zero.

Average Path Length
: The **average path length** is the average distance between every pair of
nodes in a graph.

Diameter
: The **diameter** of a graph is the maximum distance between any pair of
nodes.


{% include "problem_header.md" %}


This time, you need to compute the average path length and the diameter of
the graph.

The input is a file which contains one line with two integers $n$, the
number of nodes in the network.  The following $n$ lines each contain one
the adjacency list of the $i$-th node, where each entry is separated by a
space.  Assume the nodes are 0-indexed.

As output, write two numbers, the average path length and the diameter of
the network.  Output both as floats to three decimal places.


{% include "input_header.md" %}

```
6
1 3 5
0 2 3
0 1 3 5
1 2 4
2 3 5
0 2 4
```

{% include "output_header.md" %}

```
1.400 2.000
```


{% include "solutions_header.md" %}


The solution to this challenge is hosted on
[Github](https://github.com/leotrs/erdos/blob/master/solutions/measures/path_length.py).


{% include "question_header.md" %}


1. Find the maximum possible distance between a pair of nodes in an
   undirected, connected graph.

2. Generalize the definition of distance to directed and weighted networks.

3. What do you expect the average path length and the diameter to be in a
   global social network like Facebook?


{% include "answers_header.md" %}


1. Consider a connected graph with $n$ nodes.  The longest possible path
   between a pair of nodes in this graph has to go through every node
   exactly once.  It can't loop back around because in that case there
   would be a way of choosing a shorter path with no loops.  Thus, the
   maximum diameter of a connected network is $n-1$.

2. The definition for directed networks is the same as for undirected
   networks, except one must be mindful of the direction of the each link
   in the path.  For weighted networks, the distance between two nodes
   depends on the meaning of the weights.  If the weights represent a
   distance concept (e.g. in road networks where weights is physical
   distance from one place to another), then the shortest path between two
   nodes will be the least-weighted path.  On the contrary, if the weights
   represent a closeness concept (e.g. in social networks where we may join
   two users with a stronger weight the more frequently they interact),
   then the shortest path between two nodes will be the highest weighted
   path, because it represents the volume or frequency of interaction,
   which we can take as a proxy for "closeness".

3. Due to the Six Degrees of Separation[^1] experiment, we know that
   average path lengths are considerably less than one would expect in
   networks that exhibit the small-world[^2] phenomenon.  The folks at
   Facebook know this, and so they repeated Milgram's experiment[^3]
   recently, discovering a surprising three and a half degrees of
   separation[^4].



{% include 'footnote_header.md' %}

[^1]: [Six Degrees of Separation](https://en.wikipedia.org/wiki/Six_degrees_of_separation)

[^2]: [Small-world Network](https://en.wikipedia.org/wiki/Small-world_network)

[^3]: [Milgram's small-world experiment](https://en.wikipedia.org/wiki/Small-world_experiment)

[^4]: [Three and a half degrees of separation](https://research.facebook.com/blog/three-and-a-half-degrees-of-separation/)
