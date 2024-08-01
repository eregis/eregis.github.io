---
layout: post
title: "The Tangent Bundle in Information Geometry"
date: 2024-07-25
mathjax: true
---

Information geometry is a niche subfield of mathematics that uses the tools of differential geometry to study parametric families of probability distributions. The key insight is that parametric families of probability distributions have a natural manifold structure. The manifold (called the statistical manifold) is such that each point on the manifold is a probability distribution in the parametric family and the coordinates of the manifold are given the parameter values corresponding to that probability distribution.

Consider the parametric family of normal distributions. It's a two-dimensional statistical manifold where there two coordinates given the mean $\mu$ and the variance $\sigma^2$.

[Insert two images side by side: One is of the "map" of the statistical manifold where the x-axis is the mean $\mu$ and the y-axis is the covariance $\sigma^2$. Two points are labeled red and blue in the statistical manifold

Next to its is a graph of probability distribution where x-axis is x and y-axis the probability density p(x); the corresponding red and blue points in the graph of the statistical manifold are plotted as PDFs.]

Manifolds at locally Euclidean spaces. Similar to how a circle locally looks like a line and a sphere locally looks like a plane, while the global structure of the manifold can be rich, in a neighbourhood of a given point, it looks an $n$-dimensional Euclidean space. We call this $n$-dimensional space the *tangent space* at point $p$.

[Insert visualization of a tangent space]

The tangent space at a given point forms a vector space. But in information geometry, what are the tangent vectors?

Tangent vectors give infinitessimal changes from one point to another in a manifold. In a statistical manifold, they would represent the infinitesimal changes going from one probability distribution to another. 

[Insert visualization of a normal distribution that is shifted and the tangent bundle at that point]

That makes sense as intuitive notion, but let's formalize what "an infintessimal change in a probability distribution" actually means as a mathematical object.

We will consider a generic one-parameter family of distributions $\{\theta \in \mathbb{R}: p(x; \theta) \}$. Consider the log-likelihood $\log p(x; \theta)$. To interpret the log-likelihood, we are going to lean heavily on analogies from physics. A way to think about the log-likelihood our parameters $\theta$ represent the macrostate (e.g the temperature) and $p(x;0)$ is the probability of the microstate $x$ given the macrostate $\theta$. Recall that in the Boltzmann distribution over $x$ we have that

$$p(x) = \frac{e^{- \beta E(x)}}{Z}$$

where $E$ is the energy of microstate $x$, $\beta$ is thermodynamic beta (the inverse temperature), and $Z$ is the partition function, which sums up over the Boltzman factors our different microstates and ensures that our probability distribution is properly normalized.

In stat mechanics, we start with some energy function given by the microscopic physics and then determine the probability distribution over microstates from the Boltzmann distribution. Here we are going to go in reverse: we start with a probability distribution over $x$ and then we back-calculate what the energy  of each microstate (up to an overall constant) must be in order to have the resultant probability distribution.Then to shift the probability distribution that's to acting on the system such that it shifts the free-energy of each microstate by some commensurate amount. We can then convert it back to a probability distribution.

Why is this perspective useful? Because "infinitessimal shifts in probability" doesn't lend itself nicely to a physical interpretation while "infinitessimal shifts in free energy" *does* have a nice interpretation. This type of picture becomes especially useful in non-equilibrium stat mechanics where we consider finite-time paths in thermodynamic parameter space (which is a statistical manifold in the quasistatic limit).

is encoding the negative free energy of the microstate $x$

So the tangent vectors in information geometry