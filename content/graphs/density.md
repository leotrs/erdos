Title: Graph Density
Category: Graphs
Date: 2016-06-26
Position: 40
Summary: Density is a global graph property.
Disqus_identifier: 8675fa49-density-is-a-global-graph-property

# Context

We have seen one property of nodes, the degree, and one property of edges,
whether or not they are directed. These are called local properties,
because they describe the properties of just one element of a network.

We can also study the network as a whole, and describe the properties that
do not depend on just one node or edge, but on a collection of elements
within the network. One of the simplest global measures is the *edge
density*.

Density[](#density)
: The **density** of a network is the the number of edges present in the
network divided by the total number of possible edges.

Complete graph[](#complete-graph)
: A **complete graph** is a graph that has all possible edges present,
i.e., its density is equal to `1`.

<div class="img-desc">
  <p><img src="/images/density.png" title="Two graphs with different densities."></p>
  <p><em>Two graphs with different densities.</em></p>
</div>

## Challenge

For this challenge, you need to read a file representing a graph, and
compute the density of the network.

The input is a file where the first line contains two integers, `n` and
`m`, defining the number of nodes and edges, respectively. The next `m`
lines each contain two integers, representing two nodes that are joined by
an edge. Assume undirected edges.

Output the density of the network as a single floating point number,
rounded to three decimal places,

Hint
: First, you will need to figure out the maximum possible number of edges
in a graph with `n` nodes. You can compute it in the following way. First,
start with a graph with `n` nodes and no edges. Pick one arbitrary node and
count all the edges connecting it to all others, and mark that edge as
'done'. Proceed the same way with all other nodes, picking one unmarked
node and connecting it to all other unmarked nodes, until they are all
marked as 'done'. Keep a running count and finally output the total.

### Sample Input

```
4 4
0 1
0 2
1 3
3 0
```

### Sample Output

```
0.667
```

## Expansion Questions

1. If you followed the hint to solve the problem above, then you might have
   found yourself computing a sum of numbers that looked like the
   following. Can you find a formula for this sum, without needing to add
   up all the numbers every time? This is a very important fact that will
   be used throughout future problem sets.
   ![\displaystyle (n - 1) + (n - 2) + (n - 3) + ... + 2 + 1 ](http://quicklatex.com/cache3/bf/ql_9ef4c642ac0c0fe62857b337cc097dbf_l3.png "\displaystyle (n - 1) + (n - 2) + (n - 3) + ... + 2 + 1 ")



--------------------------------------------------------

## Solutions

[Solution](https://github.com/Leockard/erdos/blob/master/solutions/graphs/density.py).
