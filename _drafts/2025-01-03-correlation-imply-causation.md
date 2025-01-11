---
layout: post
title: "Correlation Does Imply Causation"
date: 2024-01-03
mathjax: true
---

In statistical physics, we often consider the 2-D Ising Model. This is given by a Hamiltonian
where we have next-to-nearest neighbour.

I am thinking of writing a blog post called "Correlation Is Causation". It's about how, in statistical physics: two logically distinct quantites--the correlation function which tells you given a Gibbs measure, the correlation between two points in e.g a statistical field and the response function which tells you, given a small response at a point (e.g by applying a localized magnetic field), the expectation value of the order parameter at some point.

It's perhaps understandable that these two quantities turn out to be the same (we have an intuitive notion that points that are close to each other are more "connected" or "coupled" and that would manifest as a larger correlation and also a larger response), but I still think this point is quite deep

So in statistical physics, we often work with the Ising model. Let's consider the 1 D case. The Hamiltonian for the Ising model is given by nearest neighbour interactions H = - \sum J s_i s_j. J is called the coupling constant. It determines both the strength and the type of interaction between nearby points on the lattice. When J is positive, then nearby spins want to align with each other. 

Lower energy states are more likely/favored. We want H to be minimized; due to the presence of a negative sign, this means that we want J s_i s_j to be maximized. This is acheived when the product of all three quantities is positive. As J is positive, that's equivalent to the product of s_i and s_j being positive--which acheived when they are the same sign.

With the Gibbs measure, we have that lower energy states are more likely. This means that--all else being equal--configurations where the lattice point at the origin is spin-up will. That means there will be a statistical correlation between nearby lattice sites. An intuitively, the larger the coupling constant, the larger the correlation.

But it's not just nearby lattice sites that are correlated. Between the lattice point at the site 0 is correlated with the site 1 and site 1 is correlated with site 2, then site 0 is also going to be correlated with site 2--albeit the correlation will be weaker than the correlation with site 1. And this argument keeps extending itself: because the lattice at site 0 is correlated with site 2 and site 2 is correlated with site 3, then site 0 is correlated at site 3. Because the lattice site at site 0 is correlated with the lattice at site n, then it is also correlated with $n$.

As you get further and further, this correlation gets weaker and weaker. You can plot the statistical correlation between the site n and the site 0. This graph will be exponential decay. It's a graph of the correlation function.

It's useful to think about how one would measure the correlation function if you had a 1-D Ising model in the lab. To do so, we will take advantage of the fact that (a) the system doesn't stay static, but tends to change configurations over time. However, we have to be careful. If we don't wait long enough. For example, let's say our initial configuration is one where all of the spins are up. Then it will take some time for the spins to flip, one-by-one. This example is obvious, but this general principle holds in general: all initial states have little idiosyncrasies; we want to give our system time to forget the memory of the initial state. If we do that, then the sequence of states traversed by the system will be a good representation of the random states the system can be in general.

Once we have our list of configurations. We can then find the correlation. The full calculation requires considering what happens when the spin at lattice site 0 is both spin up and spin down, separately. But our Hamiltonian has an interesting symmetry: if you simultaneously flip every spin in the lattice, the energy stays the same! As the energy determines the probability of a given microstate, that means any given microstates is exactly as probable as its reversed counterpart. So to understand the correlation function, it suffices only to consider the microstates when the s_0 is spin-up. 

To experimentally measure the correlation function, it's a simple two-step procedure:

(1) From our sample, we only restrict ourselves to the sub sample when s_0 is spin-up
(2) Among that sub-sample, we average the values of the spin for s_n

Another way to put is that--in this context--the correlation function is a conditional expectation. This gets us the correlation function \langle s_0 s_n \rangle

Now imagine a different procedure. Instead of letting our s_0 flip freely, we intervene on our system such that s_0 is always spin-up. This changes our Hamiltonian; there is no longer a degree of freedom associated with s_0; it's now replaced with a constant function 1.

How does this affect the distributions of spin? We again do that by averaging the value of the spin $n$. This is called the response function. We have a simple two-step procedure to measure the response function:

    We somehow fix the s_0 to be spin-up (whether "by hand" or by some really strong localized magnetic field)
    We average the values for s_n

What do we get for the response function? It look like this:

That looks vaguely familiar. I'm curious what happens when we superimpose our correlation function and response function on the same plot

They're the same! 

But this is a bit curious. They seem like distinct procedures. The correlation function is a passive procedure. We keep our Hamiltonian unperturbed, and we understand the connection between points in the lattice based on the natural variation in the system. The response function is an active procedure. We directly intervene to alter our system--changing our Hamiltonian--to understand the connection between points in the lattice. And yet: they're the same. Why?

In statistics, there is a saying that correlation does not imply causation. A classic example is wearing shorts and eating ice cream. While there is probably a correlation between the two, if you make people wear more shorts, they won't eat more ice cream (probably). Why? Because the correlation is caused by a third variable--how hot it is. It's the temperature that mediates the correlation between the two variables.

But here do seem to have correlation equalling causation. The classic case when correlation implies causation is when one of the variables is upstream. You can represent this by a causal diagram. For example, if you directly intervene on the temperature (somehow) that will make people want to crave ice cream--so we say the relationship be causal. 

So what this implies is that the s_0 being spin-up isn't incidental to the s_n being spin-up, but it is directly causal. Which makes sense from a physical perspective. The way this is usually thought of is that the way spins affect each other is by inducing a magnetic field. When one site is spin-up, it changes the magnetic field such that other nearby sites want to be spin-up. Importantly, while you can say the proximal cause is the experienced magnetic field, in our physical picture, there is no way to change the spin without also changing the magnetic field. This is ultimately why correlation does imply causation. 

This also is the physical justification for mean field theory. In mean field theory, we replace the complicated Hamiltonian involving correlation with a Hamiltonian where each site experiences the effective magnetic field caused by the other sites.

From a causal diagram point of view, there is a causal arrow going from every lattice site to every other lattice site at a latter point in time. And when we replace the mean field theory picture, we sever all the arrows. In favor of a single picture.

The subtlety in mean field theory is that h isn't "caused" (or we would just be back where we started)--it isn't a dynamic variable. Instead, we impose a self-consistency condition on h.

Something that doesn't quite sit right with me: causation usually isn't bidirectional; but here we have a symmetry where the symmetry I believe is broken by time; I don't want to skate past this since spelling out this subtlety seems important if I want to make sure that this is rigorous

Yes, this temperoal aspect is actually something that I realized that I wasn't quite clear about. The correlation picture is one at a given cross section of time; but the response function is one where have a perturbation that extends back into the infinite past; because a perturbation that happens localized at one moment in time--I don't think it's even well-defined what happens later? (I forget if the Hamiltonian is enough to determine time-depedent response function/correlation function)

It's also perhaps maybe a good idea to actually show the math that they are the same--though hilariously, and typical for me, I can't do it off the top of my head so I would need to look it.

Yes, the physical picture involving magnetic fields definitely needs more space--it's in many ways the first or second most important part of the piece (with the other part being the revelation that the correlation function and the response function are the same in the first place).

Claude wrote below (perhaps best not to have this verbatim in the final piece):

""But wait - there's something subtle we need to address. When we talk about causation, we usually think of it as one-way: A causes B, not B causes A. Yet in our Ising model, the correlation function ⟨s₀sₙ⟩ is completely symmetric - it doesn't care which spin we call '0' and which we call 'n'.
So what's going on? The key is in how we set up our response measurement. When we measure the response function, we're actually making two choices:

Which spin we fix to be up (breaking the spatial symmetry)
When we fix it - specifically, in the infinite past (breaking the temporal symmetry)

The correlation equals either response function: the one where we fixed s₀ long ago and measure sₙ now, or the one where we fixed sₙ long ago and measure s₀ now. But each individual response measurement has a clear arrow of time.
This actually deepens our understanding of what the correlation function is measuring. Rather than just telling us 'these spins are aligned', it's telling us about the underlying physical coupling between the points. This coupling manifests in two ways:

As simultaneous alignment in equilibrium (correlation)
As the ability of one spin to influence the other over time (response)

The equality between correlation and response tells us these are two sides of the same coin - the fundamental physical coupling between the points"

