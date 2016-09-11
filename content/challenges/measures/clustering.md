Title: Clustering Coeficient
Category: Measures
Date: 09/10/2016
Position: 30
Summary: How tightly-knit are a node's neighbors
Disqus_identifier: 9c1d83e4-how-tightlyknit-are-a-nodes-neighbors


{% include "context_header.md" %}


Last time, we saw how counting triangles gives us a measure of
transitivity.  This time, we introduce a related measure: clustering.

Clustering
: *Clustering* refers to the extent to which nodes in a network are
tightly-knit.

For example, if a triad of nodes form a triangle, we intuitively think of
them as more tightly-knit (or *clustered*) than three nodes with fewer or
no links between them.

There are many ways one could quantify this intuitive notion.  Locally
speaking, we might want to look at one particular node, `u`, and see how
clustered are its neighbors around it.  One way of doing this is by
counting how many of `u`'s neighbors are connected to each other.  If this
reminds you of transitivity, it's because we're counting exactly how many
triangles have a vertex in `u`.

{% from 'img_desc.html' import img_desc %}
{{ img_desc("clustering1.svg", "Neighbors can be more or less clustered around a node.")}}

To be able to compare clustering across nodes, however, we need to
normalize this value by the total number of possible triangles.  For every
two nodes adjacent to `u`, they could, potentially, form a triangle.
Therefore, we need to count the number of *pairs* of vertices adjacent to
`u`.  With this, we can formally define the local clustering coefficient of
`u`.

Local Clustering Coefficient
: The *local clustering coefficient* of node `u`, denoted $c_u$, is defined
by the ratio
    $$c_u = \frac{\text{triangles on }u}{\text{pairs adjacent to }u}$$

Observe that, since the numerator is never grater than the denominator, we
have $c_u \in [0, 1]$.


{% include "problem_header.md" %}


Compute the local clustering coefficient of each node.

The input is a file which contains one line with a single integer $n$, the
number of nodes in the network.  The following $n$ lines each contain one
row of the adjacency matrix of the network, where each entry is separated
by a space.

Output a list of numbers, the clustering coefficients of each node, on a
single line, separated by a space.  Print the numbers with three decimal
places.


{% include "input_header.md" %}

```
10
0 1 1 0 1 0 0 1 0 0
1 0 0 0 0 0 1 1 1 0
1 0 0 1 0 0 0 0 1 0
0 0 1 0 0 0 1 0 1 1
1 0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 1 0 0 1
0 1 0 1 0 1 0 0 0 0
1 1 0 0 0 0 0 0 0 0
0 1 1 1 1 0 0 0 0 0
0 0 0 1 0 1 0 0 0 0
```

{% include "output_header.md" %}

```
0.167 0.167 0.333 0.167 0.000 0.000 0.000 1.000 0.167 0.000
```


{% include "solutions_header.md" %}


The solution to this challenge is hosted on
[Github](https://github.com/leotrs/erdos/blob/master/solutions/measures/clustering.py).


{% include "question_header.md" %}


1. Compare the concepts of density, transitivity, and clustering.

2. What can you say about a network all of whose nodes have local
   clustering coefficients equal to 1?

3. Consider the social network of your Facebook friends.  What can you say
   about your college friends as opposed to all of your acquaintances in
   terms of clustering?  Are they more or less clustered together than on
   average?

4. There are two other popular measures of clustering in a network.

    Global Clustering Coefficient
	: Often written as just $C$, it is defined by the following ratio.
	    $$ C = \frac{\text{3 \(\times\) triangles}}{\text{connected triads}}$$
        We count each triangle three times because they each contain three
        connected triads.

	Average Clustering Coefficient
	: It's the average of all local clustering coefficients.
        $$ \bar{c} = \frac{1}{n} \sum_{u}{c_u}$$

    Compute the global clustering coefficient and the average clustering
    coefficient for the two following networks.

	{{ img_desc("clustering2.svg", "Two graphs with different measures of clustering.")}}


{% include "answers_header.md" %}


1. Briefly put, density is a measure of the number of edges present in a
   network, relative to the maximum possible number of edges.  Transitivity
   is the concept behind clustering, and indicates the extent to which two
   nodes that are connected to the same node are connected to each other.
   Clustering is a way of measuring transitivity, by counting triangles,
   relative to the maximum possible number of said triangles (either
   locally, or globally).

2. If one node has clustering coefficient equal to $1.0$, it means that all
   its neighbors are connected to each other.  If all nodes have clustering
   coefficient equal to $1.0$, it means that all nodes are connected to
   each other.  This means that the network is a complete graph.

3. It is highly more likely that your college friends know each other than
   it is for them to know your other acquaintances.  In other words, the
   relationship "we are friends from college" is more transitive than "we
   are friends".  Formally speaking, your college friends (and other
   tightly-knit groups) are expected to be highly more clustered than the
   total of your friends.

4. The global clustering coefficient and average clustering coefficient for
   both networks is $0.5$, and $0.5$ for the network on the left, and
   $0.626$, $0.4$ for the network on the right, respectively.
