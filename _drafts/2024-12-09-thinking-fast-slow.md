---
layout: post
title: "Thinking, Fast and Slow Time Scales"
date: 2024-12-09
mathjax: true
---

I didn't get much from my two semesters of quantum field theory. But one idea that managed to make an impression on me 
is the concept of "effective theories". An effective theory is a model that captures the important physics 
at a particular scale while ignoring details that don't matter at that scale---like how you can describe the flow of water
without tracking the individual water molecules. This perspective that different models of reality might be applicable at 
different scales wasn't invented by quantum field theorists---at least I don't think. 
It seems like a fairly old idea. But by way of the renormalization group, this understanding of how our physics 
changes as a function of scale is made precise, rather than simply remaining a philosophical idea.

I think that a simplified version of this idea can help us understand reaction networks, 
which are commonly used when modeling biological systems.

A reaction network is a way to represent the different states of a system and the probabilities of transitioning between these states. 
It's represented by a weighted directed graph. The nodes of the graph represent the different possible states of the system. 
The edges are arrows, where the tail represents the starting state and the head represents the ending state. 
Associated with each directed edge is a weight $k$, which gives the strength of that reaction.

![Generic Reaction Rate Network](/assets/thinking-fast-slow/generic-reaction-rate-network.png)

The reaction weights have units of inverse time. The higher the reaction rate $k$, the more likely the reaction is to occur.
For example, given a reaction rate $k_{AB}$ which represents the rate of transitioning from state $A$ to state $B$, we have:

$$p_{AB} = k_{AB} dt$$

where $p_{AB}$ is the probability that, given the system is in state $A$ at time $t$, it will transition to state $B$ during 
the small time interval $dt$.

An example of a system that can be represented by a reaction network is protein conformation. 
Due to thermal motion and interactions with their environment, free-floating proteins transition between different shapes. 
If we want to understand how a protein's shape evolves over time, we can represent it as a reaction network
where each node is a conformation and each edge represents a transition between conformations.

What I'm going to show is that reaction networks in biology are best understood as defining *effective theories*. 
Implicit to every reaction network is two time scales: the slow time scale and the fast time scale. 
The slow time scale determines which transitions are considered to be possible. 
The fast time scale determines which states of the system are distinguishable from one another.

# Thinking Slow

[As Kevin Garnett famously once said](https://www.youtube.com/watch?v=EiMcu4bH85g), "Anything is possible!" Given any two states 
$A$ and $B$, there is always *some* chance that the system could transition from $A$ to $B$ within a given
window of time.

To justify this statement, I could appeal to quantum mechanics (where the probabilities of transitioning between any two
states can become arbitrarily small, but never strictly vanish). But my contention is a bit more philosophical:
the fully-specified reaction rate network is a complete graph---one where every vertex is connected to every other vertex.

![Complete Graph](/assets/thinking-fast-slow/complete-graph.png)

But in practice, the reaction networks we actually use are relatively *sparse*---where for any given state, transitions are only possible
to some small subset of the remaining states. Where does this discrepancy come from?

First, it's an empirical reality that all complex systems have reactions occurring at varying time scales, and these time scales
span many orders of magnitude. For example, consider the time scales of the human body. 
There is the time scale of thermal molecular motion. There is the time scale of the subtle, pendulum-like swaying of limbs. There is 
the time scale of blinking, the time scale of circadian rhythms, the time scale of hormonal changes like puberty or menopause. 
There is the time scale of mortality.

And often, it's not just that there exists a wide range of time scales, but there is a quasi-separation between them 
because transitions sharing a common mechanism tend to occur at similar rates. Going back to the human body example: 
the thermal motions of water molecules and hydrochloric acid are technically different due to their distinct chemical structures. 
But in the grand scheme of things---compared to the wide range of reactions that *can* occur in the body---they happen at 
similar time scales and both live in the "thermal motion" regime.

When studying biological processes, we often focus on processes within specific time scales. 
For example, if we want to understand the physiological dynamics underpinning the fight-or-flight response, 
the microsecond time scale associated with the thermal motions of molecules would be too fast to be relevant, 
while time scales spanning multiple years, such as those associated with aging, would be too slow.

we apply a *slow time scale* threshold. 
The procedure is simple: we define a minimum reaction rate $k_min$ and delete every edge from the graph whose rate 
falls below this threshold (or equivalently, set those rates to 0).

![Slow Time Scale Pruning](/assets/thinking-fast-slow/slow-time-scale-pruning.png)

The slow time scale represents something like the "total observing time." 
It's the length of time we are observing the experiment or natural process. 

By the way, this is generally what we mean when we say something is "impossible". 
It means that given some expected length of observing time, the probability of that event happening falls below a certain threshold.

# Thinking Fast

Next, we consider the application of a fast time scale. Fast time scales appear frequently in nature. For example,
a camera's exposure captures the average intensity of light over time. More generally, when measuring or interacting with a system, 
there is always some finite duration of interaction---meaning we're actually observing a time-averaged version of the system.

Because every realistic system has some shortest time scale below which we can't resolve details, we want our 
final graphical representation to exclude any rates $k$ larger than $k_max$.
However, we can't simply delete edges corresponding to weights greater than $k_max$. So how do we ensure our final effective theory
doesn't contain any edges above this maximum reaction rate?

Consider this rectangular graph:

![Rectangular Reaction Network](/assets/thinking-fast-slow/rectangular-reaction-network.png)

In this graph, there are four states, denoted by a letter and a number. States that are the same 

If applying the slow time scale corresponded to snipping the edge, the application of the fast time scale corresponds to *glueing*.
If two nodes are connected by a large reaction rates, then then the system will quickly reach equilibrium distribution with respect
to those weights. Our new node that we got from gluing is weighted average of the previous nodes, with the weights proportional
to the time-averaged time that a realization of the system would have spent in that component node.

![Coarse Graining Rectangular Network](/assets/thinking-fast-slow/coarse-graining-rectangular-network.png)

This explains what happens to nodes when you apply a fast time scale. But what about the edges? How do we find the weight of the new
edges? Well, just like how the nodes before should be viewed as a weighted average of the component nodes, the weight of the new
composite edge will be a weighted average of reaction weights of the component edges it was formed from.

Consider the example of a enzyme latching on to an enzyme site. In biology, there is the idea of form implying function. The idea
is that what a molecule is supposed to do is determined by its shape. You can think about this as lock-and-key model of biology.
In the context of enzymes, they latch onto proteins and change the conformation which changes the properties of that protein. But
to successfully latch on the allosteric site, the enzyme needs to be be of the right orientation.

To simplify things immensely, let's imagine that the different conformations of the enzyme can be represented by a circle. And
imagine that the enzyme needs to facing to the right in order to successfully latch on the allosteric site. Then we can
represent that using this reaction network:

![Circular Conformations Protein Network](/assets/thinking-fast-slow/circular-conformations-protein-network.png)

We can see that, unless the enzyme is in the right conformation, there is no edge connecting it to the bound state.
But in practice, we don't know what the $k_on$ is for the enzyme that is in the right conformation. The thermal motions of the
rotation of the protein are much to fast. So instead, we create an effective $k_on$ which is the average 

$$k_eff = \int \d\Omega k_on(\Omega)$$

And then that $k_eff$ is what we actually understand to be $k_on$ are reported by experimental results. This is important because
it shows how something can be deterministic at high-level, but be effective random at our description because we are course-graining
over microscropic details.

![Coarse Grained Enzyme Network](/assets/thinking-fast-slow/coarse-grained-enzyme-network.png)

# A Brief Note on Commutivity

So we've introduced two operations that you can perform on reaction network graphs. An application of an upper time scale
where prune edges whose reactions are to low. And the application of a lower time scale, where nodes connected by the fast reactions
are treated as composite nodes that are equilibrium distributions over the constituent nodes.

But what happens if you want to apply both procedures to the same reaction network? Here, you have to be careful. You'll get different
results, depending on the order.

To me, the correct order is clear. Given an upper time scale and lower scale, you first apply the fast time scale, creating a composite
node. And only then do you apply the slow time scale. The simple reason

Why would this be the correct order, conceptually? I'm not completely sure. One intuition is that when prune edges, you are throwing away
information in a sense; it's a much conspicuous, discontinuous operation than the more elegant approach of combining nodes as we do with
fast time scales