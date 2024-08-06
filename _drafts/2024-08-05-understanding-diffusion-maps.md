---
layout: post
title: "Understanding Diffusion Maps"
date: 2024-05-01
mathjax: true
---

# Distance in Euclidean Space

In Euclidean space, we know how to calculate the distance between two points: you take the difference of the coordinates, square the differences, sum up, and then take the square root.

$$d(\mathbf{x}, \mathbf{y} = \sqrt{\sum_{i=1}^n (x_i - y_i)^2}$$

But it's fun to think up other ways to  measure how far two points are from each other. One way is to generalize the distance formula is the $$p$$-metric.

$$d_p(\mathbf{x}, \mathbf{y}) = \left(\sum_{i=1}^n (x_i - y_i)^p \right)^{1/p}$$

where the Euclidean metric corresponds to the special case where $$p = 2$$. 

Instead of just considering metrics, we can also consider *semimetrics*. A semimetric is a distance measure, similar to metrics, but we don't require that semi-metrics satisfiy the triangle inequality (unlike for metrics).

Consider the overlapping circle semi-metric. Here's how it works. If you want to measure, the distance between two points $x$ and $y$ in $\mathbb{R}^n$, you:

1. Put a unit $n$-sphere of radius 1 centered at each point. This has volume $$V_n$$.
2. You calculate the volume of the region of intersection between the two unit $$n$$-spheres.
3. You take the volume of the overlapping region and subtract it from $$V_n$$.

This is a bit elaborate, but it still works. It satisfies several properties that we would want from a distance measure:

1. It's zero if and only if $x = y$.
2. It's monotonic along straight line trajectories.

We can generalize this. What we did here was
1. Map each point to some more complicated geometric object with structure (in the above case, it was an $n$-sphere).
2. We define some intuitive similarity measure on the space of these more complicated objects (in the above case, spheres more similar if they share common volume).
3. We then do some inversion to turn the *similarity* measure into a *dissimilarity* measure (as distances measure how far apart points are, not how close they are to each other).

Let's do one last example in $$\mathbf{R}^n$$. Here, we map each point in $\mathbb{R}^n$ to the Gaussian measure of unit measure (also known as a normal distribution) and unit variance centered at that point:

$$x \rightarrow \mathcal{N}(x, 1}$$

where $\mathcal{N}(\mu, sigma)$ denotes the normal distribution with mean $\mu$ and standard deviation $\sigma$. Given two probability measures, there is a dissimilarity relation called *the total variation distance*. The total variation distance is the supremum of the absolute difference in probability given by the two measures over all events. 

In our case, the way you can think about it: an event is a subset of $\mathbbf{R}$ (not all subsets are measurable but we won't worry about that). If we express our measure as a probability density function, the total variation distance is simply what you when you integrate over the domain where one function's density is greater than the other function (it doesn't matter which function you choose). This is a nice generalization of our example of the $n$-sphere.

#Diffusion Maps

The previous examples were all considering notions of distance on $$\mathbb{R}^n$$ which is a well-behaved space with an intuitive notion of distance. Let's consider a harder example: determining distance between vertices on an undirected graph.

One way you could determine distance would be to take the shortest path between two points. But this has potential problems depending on your intepretation of the graph.

For example, consider the case when the graph represents different locations and edges roads connecting them. Then there is a certain logic to having the distance between the locations be the length of the shortest path. But what if instead you want your metric to capture something like: "How quickly does it take to get from point A to point B". Then the length of the shortest path is not enough. If there is only one path from A to B, then there will be traffic--some maximum throughput.

We can generalize that throughput example. Consider the case where we have an undirected graph with weighted edges. You can think of the weight of the edge as being the width of the road connecting the two points.  Then we want to take all of that into account when measuring the distance. But how?

To do so, we will do something similar to the Gaussian measure we did in the Euclidean section. The Gaussian measure has many properties, but one of them is that it's kernel of the diffusion equation. Given a point source, under diffusion, the source will spread out into a Gaussian with a wider and wider profile over time.

Our solution won't be a Gaussian as we aren't in Euclidean space. But the process is similar. We need to define what diffusion looks like on the graph. We then associate each point on the vertex with the distribution that results from letting it diffuse for some arbitrary time. This maps each point on the graph to a probability density on the graph

$$v \rightarrow \mu_v$$

We then can use the total variation distance as before to find the dissimilarity between the measures--which gets us a notion of distance.

# Defining Diffusion

In order to define diffusion, we need something analagous to the diffusion equation, but defined on our graph. We need to take the weighted graph and produce a *transition matrix*. The procedure for producing the transition matrix is:
1. if we n vertices in our graph, we produce a matrix $$A$$ such that