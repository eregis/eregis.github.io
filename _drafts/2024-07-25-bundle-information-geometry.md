---
layout: post
title: "The Tangent Bundle in Information Geometry"
date: 2024-09-13
mathjax: true
---

# The Tangent Bundle in Information Geometry

## Introduction to Information Geometry

Information geometry is a niche subfield of mathematics that uses the tools of differential geometry to study parametric families of probability distributions. The key insight is that parametric families of probability distributions have a natural manifold structure. The manifold (called the statistical manifold) is such that each point on the manifold is a probability distribution in the parametric family and the coordinates of the manifold are given by the parameter values corresponding to that probability distribution.

## The Statistical Manifold

Consider the parametric family of normal distributions. It's a two-dimensional statistical manifold where there two coordinates given the mean $\mu$ and the variance $\sigma^2$.

[Insert two images side by side: One is of the "map" of the statistical manifold where the x-axis is the mean $\mu$ and the y-axis is the covariance $\sigma^2$. Two points are labeled red and blue in the statistical manifold

Next to its is a graph of probability distribution where x-axis is x and y-axis the probability density p(x); the corresponding red and blue points in the graph of the statistical manifold are plotted as PDFs.]

Manifolds at locally Euclidean spaces. Similar to how a circle locally looks like a line and a sphere locally looks like a plane, while the global structure of the manifold can be rich, in the neighbourhood of a given point, it looks an $n$-dimensional Euclidean space. We call this $n$-dimensional space the *tangent space* at point $p$.

[Insert visualization of a tangent space]

## Tangent Spaces in Information Geometry

The tangent space at a given point forms a vector space. But in information geometry, what are the tangent vectors?

Tangent vectors give infinitessimal changes from one point to another in a manifold. In a statistical manifold, they would represent the infinitesimal changes going from one probability distribution to another. 

[Insert visualization of a normal distribution that is shifted and the tangent bundle at that point]

## Tangent Vectors as Infinitesimal Changes in Probability Distributions

That makes sense as intuitive notion, but let's formalize what "an infintessimal change in a probability distribution" actually means as a mathematical object.

## The Log-Likelihood and Free Energy Interpretation

We will consider a generic one-parameter family of distributions $\{\theta \in \mathbb{R}: p(x; \theta) \}$. Consider the log-likelihood $\log p(x; \theta)$. To interpret the log-likelihood, we are going to lean heavily on analogies from physics. A way to think about the log-likelihood our parameters $\theta$ represent the macrostate (e.g the temperature) and $p(x;0)$ is the probability of the microstate $x$ given the macrostate $\theta$. Recall that in the Boltzmann distribution over $x$ we have that

$$p(x) = \frac{e^{- \beta E(x)}}{Z}$$

where $E$ is the energy of microstate $x$, $\beta$ is thermodynamic beta (the inverse temperature), and $Z$ is the partition function, which sums up over the Boltzman factors our different microstates and ensures that our probability distribution is properly normalized.

## Physical Interpretation and Connections to Statistical Mechanics

In statistical mechanics, we start with some energy function given by the microscopic physics and then determine the probability distribution over microstates from the Boltzmann distribution. Here we are going to go in reverse: we start with a probability distribution over $x$ and then we back-calculate what the energy  of each microstate (up to an overall constant) must be in order to have the resultant probability distribution. Then to shift the probability distribution that's to acting on the system such that it shifts the free-energy of each microstate by some commensurate amount. We can then convert it back to a probability distribution.

Why is this perspective useful? Because "infinitessimal shifts in probability" doesn't lend itself nicely to a physical interpretation while "infinitessimal shifts in free energy" *does* have a nice interpretation. This type of picture becomes especially useful in non-equilibrium stat mechanics where we consider finite-time paths in thermodynamic parameter space (which is a statistical manifold in the quasistatic limit).

is encoding the negative free energy of the microstate $x$

So the tangent vectors in information geometry

I guess the idea of how tangent vector relate to shifts in free energy is that if you view the domain x at which the probability distribution is defined, then we can consider it the Gibbs ensemble of some energy function over the domain. So shifting the probability flow into a microstate would correspond to changing the energy associated with that macrostate (or rather, the relative energy relative to other microstates)

This would correspond to some perturbation of the Hamiltonian of the system I think? I'm not sure if the connection between perturbation theory of Hamiltonian and small perturbations in the Gibbs ensemble is deep or actually has some fruitful mathematical structure.

## Traditional Mathematical Treatment of Tangent Vectors

The more traditional mathematical treatment of tangent vectors involves (I think) parametrized paths that pass through the point, and then some equivalence class on them, right? Maybe I could cover this in brief, but I never found this super important or enlightening. I guess this definition has to do with the fact that fundamentally the manifold is a collection of charts, so we want to derive things from function that map to the charts: but again, once you define the tangent vector formally, I tend to think of it as a primitive. It's pretty rare that I think about the formal definition when actually thinking about tangent vectors.

## Limitations and Considerations

So considering the case of your example, it would seem to be "no" as the ratio of log (p(x)/p'(x)) is not always defined if either p(x) or p'(x) are zero when the other is not (physically, if we have that our perturbed Hamiltonian is a bounded smooth function, then you can't have infinite energy at a point in phase space--which is what you would need to transition from a non-zero probability to zero probability)

It would then seem that non all probability distributions can be reached with a perturbation, strictly speaking. However, I think that you can define a sequence of perturbations Hamiltonians such that they converge pointwise almost everywhere, so I'm not sure how interesting this objection is.

More interesting was your point about physical realizability.

I also realize that there is perhaps a more interesting perspective when you consider not just a perturbation, but rather path through Hamiltonian space where our perturbations are indexed by time. This would be a more physical picture in that you imagine arbitrary processes from this perspective.

So okay, if instead of considering the general function space, we instead consider the some subset of Hamiltonians (can be be either an infinite dimension subset e.g spherical symmetry or a finite dimensional subset if we consider some parameterized set), then things might get interesting again: specificically in the parameterization case, we have a more clear distinction between the set of all possible Hamiltonians and the set of all perturbations.

I don't understand what you mean by "natural gradient". The Fisher information metric at a given point, roughly, tells you how easy it to distinguish a given set of parameter values from its neighbours given its the true generating distribution.

Though as I write this: isn't the more natural setting in which to understand parameterized distributions be using some thermodynamic parameters, not via a perturbation theory analysis of the Hamiltonian? 

For intensive parameters, this wouldn't be too hard to think about (e.g for thermodynamic beta)--though I am wondering about the correspondence between a given thermodynamic transformation (e.g lowering temperature) and the corresponding perturbation of the Hamiltonian at fixed temperature. 

In the maximum entropy formalism, intensive parameters correspond to Lagrange multipliers. Would this correspond to some "nice" parametric family of probability distributions? For the cases we consider in a basic stat mech class, the answer is yes: but it's not clear that this is true in general.

For extensive parameters, this seems more difficult to handle. Well, not necessarily: this could also be translated into a Hamiltonian, though I'm not sure the perturbation theory approach is the right, most natural way to think about things. (For example, if you wanted to represent particles being constrained to some volume, that could be an infinite potential V \Theta (r^2 - L^2) where we take the limit as V goes to infinity. And then increasing the volume would be increasing the parameter L; but that isn't so amenable to a perturbation theory way of thinking about things, perhaps due to "true" Hamiltonian be represented by a limit of smooth, bounded Hamiltonians that are nicer to work with.)