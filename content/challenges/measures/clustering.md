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

{% from 'img_desc.html' import img_desc %}
FIG1

There are many ways one could quantify this intuitive notion.  Locally
speaking, we might want to look at one particular node, `u`, and see how
clustered are its neighbors around it.  One way of doing this is by
counting how many of `u`'s neighbors are connected to each other.  If this
reminds you of transitivity, it's because we're counting exactly how many
triangles have a vertex in `u`.

FIG2

To be able to compare clustering across nodes, however, we need to
normalize this value by the total number of possible triangles.  For every
two nodes adjacent to `u`, they could, potentially, form a triangle.
Therefore, we need to count the number of *pairs* of vertices adjacent to
`u`.  With this, we can formally define the local clustering coefficient of
`u`.

Local Clustering Coefficient
: The *local clustering coefficient* of node `u`, denoted $c_u$, is defined
by the ratio
    $$c_i = \frac{\text{triangles on }u}{\text{pairs adjacent to }u}$$


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


1. Make sure these are actually questions,
2. Or at the very least, explain exactly
3. What it is to be discussed


{% include "answers_header.md" %}


1. Make sure these are actually questions,
2. Or at the very least, explain exactly
3. What it is to be discussed


{% include 'footnote_header.md' %}


[^1]: [footnote 1]()
[^2]: [footnote 2]()
[^3]: [footnote 3]()
