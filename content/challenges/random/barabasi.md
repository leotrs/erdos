Title: Barabási-Albert random graph
Category: Random Graphs
Date: 09/30/2016
Position: 20
Summary: Generating random scale-free graphs
Disqus_identifier: 3291e54e-generating-random-scalefree-graphs


{% include "context_header.md" %}


Last time we created a simple random graph model where the appearance of
every edge is decided at random.  While this is a good baseline model, not
many real world networks are formed completely at random.  For example, my
college friends are more likely to also be friends among themselves, while
they are less likely to know a childhood friend of mine.  Their connections
are not completely random.

To account for this, we need another model that more closely follows real
life networks.  First of all, real networks are constantly changing, with
more people signing up for Twitter and Facebook, neurons in the brain
making new connections while you learn and remember, and more computers
constantly talking to each other over the Internet.  A model of real
networks should account for growth.

Second of all, connections in a real network aren't completely random.  If
I sign up for Twitter, I'm more likely to follow famous celebrities,
journalists or public figures; that is, people who already have many
followers.  This phenomenon is called *preferential attachment*.

Preferential Attachment
: **Preferential Attachment** is the phenomenon by which a node in a
network is more likely to connect to a high degree node.

In 1999,
[Barabási and Albert](http://science.sciencemag.org/content/286/5439/509)
published a paper with a simple model that included both growth and
preferential attachment.  In it, they detail an amazing discovery.  The
degree distribution of their model followed a power law.

Power Law
: A function is said to follow a **power law** when it is (approximately)
proportional to a power of its argument,
$$ f(x) \sim x^{-a}, $$
for some constant $a$.

Scale Free Network
: A network is called scale-free if its degree distribution follows a
power-law,
$$ p(k) \sim k^{-\gamma}. $$
In this case, $\gamma$ is called the **degree exponent** of the network.

Mathematically, power laws have different interesting properties.  For
example, they are *scale-invariant*, which means that they will look the
same after the argument is scaled,
$$ f(cx) \sim (cx)^{-a} = c^{-a}f(x) \sim f(x). $$

In practical terms, this means the following.  Suppose the growth of a real
network (the WWW, say) follows a mechanism similar to preferential
attachment.  In that case, we conclude that the degree distribution of the
WWW today will look essentially the same as it will look in ten years.  The
network will keep growing, but the proportion of high-degree nodes will
stay the same.

The model follows a simple growth step, as follows.

Barabási-Albert Random Graph
: The **Barabási-Albert Random Graph** is a model for generating scale-free
networks.  It depends on two parameters, $N$, the final number of nodes,
and $m$, the new number of links at each time step.  Starting with $m$
nodes all joined to each other, at each time step we add a new node until
there are a total of $N$ nodes.  The links of each new node are formed by
choosing among the old ones in proportion to their degree.  The probability
of a new node linking to an older node with degree $k$ is
$$ \Pi(k) = \frac{k}{\sum_{i} k_i}, $$
where the sum is across all nodes present at the current time step.


{% include "problem_header.md" %}


Write a script that generates a Barabási-Albert network.

The input is a file with a single line with two integers: $N$, the final
number of nodes in the network, and $m$, the number of new links per node.

For the output, either save your network to a file, or visualize it using
software like Gephi, or NetworkX if you're using Python.


{% include "input_header.md" %}

```
100 3
```

{% include "output_header.md" %}

The output is your desired visualization of a network.


{% include "solutions_header.md" %}


The solution to this challenge is hosted on
[Github](https://github.com/leotrs/erdos/blob/master/solutions/random/barabasi.py).


{% include "question_header.md" %}


1. Suppose you grow a Barabási-Albert graph and want to know which nodes
   have the highest degree.  Would you start looking from the newest or the
   oldest nodes?

2. What happens if you grow a network similarly to the Barabási-Albert
   model, but in which new nodes form their links without preferential
   attachment?  That is, every new link is formed by choosing a node with
   equal probability.[^1]

3. What happens if you grow a network similarly to the Barabási-Albert
   model, but in which there is no growth?  That is, start with $N$
   isolated nodes and at each time step choose a node to form $m$ new
   links, proportionately to node degree.[^1]

The following questions require knowledge of calculus and probability.

3. Express the expected degree of an arbitrary node $i$ as a function of
   time step $t$, $k_i(t)$.  Approximate $k_i(t)$ as a continuous variable,
   and perform this analysis in the case where $N$ is large.[^1]

4. Express the degree distribution of the network, $p(k)$, as a function of
   $N$ and $m$, again in the case where $N$ is large.[^1]


{% include "answers_header.md" %}


1. You start looking at the oldest nodes (the ones that appeared first on
   the network), for two reasons.  First of all, by virtue of having been
   there first, there are more nodes that can connect to them.  More
   importantly, as their degree grows, so is their chance of being chosen
   to form new links.  This starts a snowball, "rich gets richer" effect.
   The pioneer nodes will take a sizable proportion of all nodes in the
   network, and for this reason they are called *hubs*.

	Hub
	: A node is called a **hub** when it holds a considerable proportion of
    the links in a network.  There is no clear-cut definition to call a
    node a **hub**.

	Some authors will refer to the top 10% of nodes, ordered by degree, as
    hubs, whether or not the network is scale-free.

2. In the absence of preferential attachment, one gets a random network
   much like an Erdos-Renyi graph, since at any given time step, each node
   chooses its edges uniformly at random.

3. In the absence of growth, the network will resemble a Barabási-Albert
   graph during its initial stages, but in the end, when more and more
   links are being formed, it will reach the complete graph.

4. Let $X$ be a node chosen uniformly at random in a BA network with $N$
    nodes, where at each time-step we add a new node to the network, with
    $m$ links connecting to nodes chosen proportionately to their
    degree.[^2]  We identify each node by the time $t$ at which it appeared
    in the network, so we have $X=t_X$.  We need to describe how the degree
    of a random node $X$ changes with time.  For this, we approximate the
    increase in the degree of $X$ by the expected increase across all
    nodes,

    $$ \frac{dk_X}{dt} = m \frac{k_X}{\sum_j k_j}, $$

    where we assume that each of the $m$ new edges is placed at the same time
    and independently of each other.  Now, we have $\sum_j k_j = 2mt-m$, since
    we start at time $t=0$ with zero nodes (and hence, zero edges), and we
    don't count the edges we are adding at this particular time step.

    Thus,

    $$ \frac{dk_X}{dt} = \frac{k_X}{2t-1} \approx \frac{k_X}{2t}, $$

    where we can assume the last approximation when $t$ (and, thus, $N$) is
    large.

    By integrating $ dk_X/k_X = dt/2t$, we obtain

    $$ k_X(t) = m (\frac{t}{t_X})^\beta, \quad \beta = \frac{1}{2}, $$

    where we have used the fact that $k_X(t_X) = m$.

5. We want $p_k = P(k_X = k)$, where $k$ is a fixed constant between $0$
    and $N-1$[^2].  With the approximation we derived in $4$, we compute
    the cumulative degree distribution, $P(k_X \leq k)$.

    Now, observe that the event in which $k_X \leq k$ is the same event as
    $\frac{m}{k}^\frac{1}{\beta} \leq \frac{t_X}{t}$.  Since $t = N$, and
    $t_X=X$, we can interpret the time fraction $\frac{t_X}{t}$ as a node
    fraction $\frac{X}{N}$.

    Since $X$ is chosen uniformly at random from the set of nodes ${1, 2, 3,
    ..., N}$, we have that $\frac{X}{N} \sim Uniform(\{1/N, 2/N, ..., 1\})$,
    which, for large $N$, we can approximate as a continuous $Uniform([0, 1])$.

    With these observations, we have

    $$\begin{align*}
    P(k_X \leq k) &= P(\frac{m}{k}^\frac{1}{\beta} \leq \frac{X}{N}) \\
                &= 1 - P(\frac{X}{N} \lt \frac{m}{k}^\frac{1}{\beta}) \\
                &= 1 - \frac{m}{k}^\frac{1}{\beta} \\
    \end{align*}
    $$

    We finish by taking derivatives.

    $$\begin{align*}
    p_k &= \frac{dP(k_X \leq k)}{dk} \\
        &= \frac{1}{\beta}\frac{m^{\frac{1}{\beta}}}{k^{(1 + \frac{1}{\beta})}} \\
        &= 2m^2k^{-3}
    \end{align*}
    $$


{% include 'footnote_header.md' %}

[^1]: These questions extracted from
[Network Science](http://barabasi.com/book/network-science).

[^2]: These solutions extracted from
[Leo Torres](http://leotrs.com/blog/distribution.html).
