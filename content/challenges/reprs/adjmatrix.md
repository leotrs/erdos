Title: Adjacency Matrix
Category: Representations
Date: 2016-06-26
Position: 2
Summary: Graphs can be represented by a matrix
Disqus_identifier: 2c59cbd3-graphs-can-be-represented-by-a-matrix

{% include "context_header.md" %}

Adjacency matrices provide another way to represent a graph, using a square
array of numbers. They are slightly more complicated than adjacency lists,
but it pays off to study them, since we can use all the power of matrix
algebra to manipulate them.

Consider the graph in the picture and assume we were trying to write down
all of the edges in the graph.

{% from 'img_desc.html' import img_desc %}
{{ img_desc("/images/adjmatrix.png",
            "Example graph.",
            "Example graph.")}}

If all we had was this drawing (instead of, say, an adjacency list
representation of the network), we would need to examine node by node and
write down each of the node's neighbors. Thus, we start at the node labeled
`0` and look at every node in order, while asking ourselves these
questions: 'Is `0` connected to `0`?' 'Is `0` connected to `1`?' 'Is `0`
connected to `2`?', and so on and so forth, while we write down our answers
as follows.

```
NO YES YES YES
```

We repeat the same process for every other node, asking if `1` is connected
to each node in turn, if `2` is connected to each node in turn, and so on,
to get the following set of answers,

```
NO  YES YES YES
YES NO  NO  YES
YES NO  NO  NO
YES YES NO  NO
```

Hint
: When you consider a node `u` and go through every node, remember to ask
if a node is connected to itself (allow for self-loops), and to cover the
nodes always in the same order.

Now, this 'array of answers' holds a lot of information about the graph. In
fact, it holds *all* the information about edges that we care about, just
as well as the adjacency list representation. However, it is not very easy
to compute anything with a bunch of words sorted in a nice way. For real
computational power, we need a matrix.

To write down our adjacency matrix, all we need to do is convert our array
of answers into an array of numbers, by replacing every occurrence of `YES`
to $1$, and every `NO` to $0$.

$$\begin {pmatrix}0  &1  &1  &1 \\ 1  &0  &0  &1 \\ 1  &0  &0  &0 \\ 1  &1  &0  &0 \end{pmatrix}$$

The array of numbers we have constructed is called the adjacency matrix of
the graph.

Adjacency Matrix[](#adjacency-matrix)
: The **adjacency matrix** of a graph with $n$ nodes is an $n \times n$ matrix
whose element at the $i$-th row and $j$-th column indicates whether nodes
`i` and `j` are adjacent or not.

{% include "problem_header.md" %}

To solve this challenge, you will need to read a file in adjacency list
form, and output its adjacency matrix.

The input will be a file where the first line contains just one integer,
$n$, the number of nodes in the graph. Each of the following $n$ lines
holds a list of space-separated integers, representing the adjacencies of
every node. As before, assume that nodes are labeled from `0` to `n-1`. The
lines are in ascending order of node label, e.g., the first line of the
output contains the adjacencies of node `0`, the second line contains the
adjacencies of node `1`, etc.

Output the adjacency matrix of the graph.

{% include "input_header.md" %}

```
4
1 2 3
0 3
0
0 1
```

{% include "output_header.md" %}

```
0 1 1 1
1 0 0 1
1 0 0 0
1 1 0 0
```

{% include "question_header.md" %}

1. Consider the adjacency matrix of an undirected graph.
    1. What can you say about the entry at row $i$, column $j$, as compared
       to the entry at row $j$, column $i$?
    2. What if the graph is directed?
3. What happens to the adjacency matrix of a graph if its nodes are labeled
   in a different order?
2. For a given node `u` in the example network, compute the degree of `u`
   using only the adjacency matrix.
3. Compute the density of the example network using only its adjacency
   matrix.
4. Can you construct the adjacency matrix of a multigraph? Why or why not?

{% include "solutions_header.md" %}

The solution to this challenge is hosted on
[Github](https://github.com/leotrs/erdos/blob/master/solutions/reprs/adjmatrix.py).


{% include "answers_header.md" %}

1. If the graph is undirected and node `u` is connected to node `v` means
   the entry $a_{uv}$ is equal to $1$.  But the connection is reciprocal,
   which means that `v` is also connected to `u`, and $a_{vu}$ is also
   equal to $1$. A matrix whose entries all hold this property is called a
   *symmetric* matrix.

    Symmetric Matrix
    : The matrix $A$ is **symmetric** when $a_{ij} = a_{ji}$ for every
    possible value of $i$ and $j$.

    A graph is undirected *if and only if* its adjacency matrix is
    symmetric. If a graph is undirected, its matrix is not symmetric.

    Symmetric matrices have various useful properties[^1], many of which are
    directly used in graph theory and Network Science[^2].

2. The adjacency matrix will include the same information, with each row
   marking the neighbors of each node.  However, since each row represents
   one node, the rows will be the same, but in different order than the
   original matrix.

2. The degree of `u` is just the number of nodes adjacent to it. If we look
   at the row corresponding to `u` in the adjacency matrix of an undirected
   graph, we see there's a $1$ in exactly those nodes that are adjacent to
   `u`.  Thus, we need only count the number of occurrences of $1$, or just
   add them up which yields the same result.  If $G$ is our graph, $A$ is
   its adjacency matrix, and we write $v \in G$ to mean `v` is a node of
   $G$, we have

    $$ deg(u) = \sum_{v\in G} a_{uv} $$

    We can perform the sum over all entries of the row since the ones we're
    not interested in all contain zeroes.

3. Because of the above remarks, every edge in the network generates two
   entries equal to $1$ in the adjacency matrix.  Thus, if we want the
   total number of edges, we can add up all the $1$'s present in the matrix
   and divide by two.  Then we just need to divide by the maximum number of
   edges the graph could support.

    $$\begin{align*}
    density(G) &= \frac{1}{\text{total edges}} \times \text{present edges} \\
               &= \frac{2}{n(n-1)}\:\:\:\, \times \frac{1}{2}\sum_{u \in G} \sum_{v \in G}a_{uv} \\
               &= \frac{1}{n(n-1)}\:\:\:\, \times \sum_{u \in G} deg(u) \\
    \end{align*}
    $$

4. A graph with self-loops has non-zero diagonal entries (the entries of
   the form $a_{ii}$), and poses no trouble for adjacency matrices.

    A non-simple graph with parallel edges calls for a way of signaling the
    number of edges joining any pair of nodes.  One could replace the $1$
    in the entries for a natural number equal to the amount of edges
    joining the corresponding nodes, but using numbers different to $1$ in
    adjacency matrices is reserved for matrices of *weighted graphs*.
    Weighted graphs will be covered in a future challenge.


{% include 'footnote_header.md' %}

[^1]: [Symmetric matrix properties](https://en.wikipedia.org/wiki/Symmetric_matrix#Properties).

[^2]: [Adjacency matrix properties](https://en.wikipedia.org/wiki/Adjacency_matrix#Properties).
