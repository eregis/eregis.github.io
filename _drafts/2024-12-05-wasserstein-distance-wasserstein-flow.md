---
layout: post
title: "The Intuition Behind Why the Wasserstein-2 Distance is the Correct Metric for Wasserstein Gradient Flow"
date: 2024-12-05
mathjax: true
---

Wasserstein Gradient Flow is the idea that time evolution of a measure can be viewed as the measure "rolling down hill" in the space 
of measures with respect to some functional. The seminal case examined in JKO 1998 is that the Fokker-Plank equation can 
be viewed as governing the time evolution of gradient flow where the functional that is being minimized is the relative entropy
with respect to the stationary distribution $\pi$: $\text{KL}(\mu_t\|\| \pi)$ where the metric is given by the Wasserstein-2 distance.

But why the Wasserstein-2 distance? Why not the Wasserstein-1 distance? Or the Wasserstein-17.3 distance?
There is actually a pretty simple analogy that helps shed light on this question.

What we care about is the evolution of the measure $\mu_t$ over time, but let's actually consider a simpler problem: Let's
say we have an ordinary differential equation (ODE) that tells us the time evolution for $x$ that is governed by gradient flow (so the time derivative can be expressed as the derivative of a scalar potential $V$)

$$\frac{dx}{dt} = -\nabla V(x, t)$$

Let's say that the ODE is not analytically tractable (because $f$ is ugly in some way). How would we find solutions.

We can approximate by discretizing our time step. Rather than having $x(t)$, we instead have $x(t_k)$ where $t_k = t_0 + k \delta t$
and $\delta t$ is some small (but finite) time step.

(There are many different discretizations schemes. For example, we could have made the step size variable. Or have it be dynamic
based on the second derivative. Or evaluate at the right-end point instead of the left-end point. These considerations don't matter
for our purposes as the forward Euler equation will work just fine.)

If we replace our derivative with its difference quotient and don't pass to the limit, we have that

$$\frac{x(t_{k+1}) - x(t_k)}{\delta t} = - nabla V \rightarrow x(t_{k+1}) = x(t_k) + \delta_t (- \nabla V)$$

This approximation scheme is called *Euler's forward equation*.

But we can equivalently cast it as an optimization problem. A way to think about it is with discretization we are performing 