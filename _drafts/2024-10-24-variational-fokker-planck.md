---
layout: post
title: "The Variational Formulation of the Fokker-Planck Equation"
date: 2024-10-24
mathjax: true
---

Let's say that you have a Langevin equation:

$$dX_t = - b X_t dt + \sqrt{2} dW_t$$

This is the OU-process. Given this stochastic differential equation, we have the associated Fokker-Planck equation

$$\frac{\partial \rho}{\partial t} = \Delta pho + \nabla \cdot (b \rho)$$

It's well-known that for the OU process, the stationary distribution is a Gaussian. But


[Picture of generic diagram of space of measures with multiple lines connecting them]

We would naturally expect that given the original measure, $\rho_0$, that the time-evolution is a "straight line" from the
original measure to the target measure $\pi$. But what does a straight line mean in the space of measures.

It's due to a landmark paper by Jordan, Kindelburger, and Otto the time evolution of the Fokker-Plank can be viewed as a gradient
flow in the space of measures. That at each point in time, the probability density evolves such that it is in the direction of steepest
descent with respect to a specific functional: the KL-Divergence with respect to the target measure acting as the coding distribution?

$$\mathcal{F}(\mu) = \text{KL}(\mu || \pi)$$

The KL-divergence measures the relative entropy between two distributions. It's non-negative and it's only zero when
the $\mu = \pi$.

![alt text](iterative-discrete-scheme.png)

In this discrete scheme, we can interpret $h$ as an effective step size. Given our current density $\pho^k$, we want to find 
the density