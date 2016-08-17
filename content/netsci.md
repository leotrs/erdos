Title: Network Science
Position: 1
Side: left


## NetSci in 1 minute

During the study of many different disciplines, scientists have come across
a diverse set of **complex systems** that are organized in a networked
fashion.  Some examples include computers interconnected to form the
Internet, social networks of friendships and acquaintances, academic
networks of co-authorship and collaboration, utility networks of the energy
grid, transportation networks of cities and roads.  The list goes on.  What
all of these systems have in common is that they are all formed by a set of
**interconnected entities**, to form a distributed, scattered system that
is, in many cases, more than just the sum of its parts.

**Network Science** arises from the effort to gather up all research about
networks under the same regime.  In its most basic form, it eliminates the
identity of the networks, and focuses on the organizational structure only,
also known as the network's **topology**, through the study of mathematical
objects known as **graphs**.  In its applied form, it deals directly with
the networks themselves, manipulating massive amounts of real-world data,
with applications to Computer Science, Sociology, Physics, Economics, and
Neuroscience.


## NetSci in 10 minutes

### What does *Erdos* mean, anyway?

During the mid twentieth century, Hungarian mathematician **Paul Erdos**
became known for his passion for mathematics, his eccentric demeanor, and
his astoundingly prolific output.  He published more than 1500 articles in
many different areas of mathematics, including **graph theory**, the
mathematical toolbox underlying Network Science.

Erdos had around 500 direct collaborators for his publications, and due to
his fame and the prestige it meant to publish with him, his colleagues
invented the notion of an **Erdos number**.  Erdos himself got an Erdos
number of $0$, while his direct collaborators were assigned the number $1$.
Collaborators of Erdos' direct co-authors received an Erdos number of at
most $2$, and so every person is assigned the smallest value among all
their collaborators plus one.

The Erdos number also defines an interesting social network of scientific
co-authorship, in which we can identify authors as the entities, or
**nodes**, of the network, and we can mark the existing co-authorships as
relationships, or **edges**, in the network.

You can see how this network looks like
[here](http://www.orgnet.com/Erdos.html).

In this way, Erdos was not only an expert in graph theory, but he also wove
a real interconnected network of mathematicians, scientists and authors.
The Erdos number is part of the folklore of mathematics and academia, used
to this day as a tongue-in-cheek ranking among the academic community.
There is even a *Bacon number*, defined much in the same way but around
actor Kevin Bacon, which traces the network of collaboration among stage
artists.


### It *is* a small world, after all

Around the same time, in the 1960's, Stanley Milgram conducted several
experiments known now as the **small-world experiments**.  He chose people
at random in Omaha, Nebraska, and asked them to forward a letter to a
certain person in Boston, Massachusetts.  If the chosen person didn't know
the recipient in Boston, they were to forward the letter to an acquaintance
of their choosing, given that the next person person to receive the letter
had a higher chance of knowing the original recipient.

Milgram then tracked the correspondence chain and studied the number of
steps that it usually took a letter to reach the intended recipient.  To
his surprise, the average number of steps was between *five* and *six*.
This and other results are now widely known as the rule of **six degrees of
separation**, and it has led researchers to further investigate the
properties of large **social networks**.

One would expect that Milgram's letters would have arrived after dozens of
steps, since they had to cross more than 1,000 miles and had to be routed
through millions of people.  As it turns out, many real-life networks
exhibit the same pattern where any two nodes are likely to be connected by
a surprisingly low number of steps.  This is a measured called **average
path length**.  When a network has low average path length relative to the
number of nodes, scientists say it's a **small-world network**.

Since then, evidence have been found that supports the fact that many other
networks are also small-world: from real-life and online social networks to
cities interconnected by a **network of roads**, networks of **protein
interactions**, and even networks of **brain cells**.


## NetSci in a little more than 10 minutes

If you're ready to spend some more time learning about Network Science, you
can start with our [challenges](/categories.html) or
[resources](resources.html) pages.
