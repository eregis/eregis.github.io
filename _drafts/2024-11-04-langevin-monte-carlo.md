---
layout: post
title: "Post Template"
date: 2024-11-04
mathjax: true
---

Markov Chain Monte Carlo (MCMC) is a technique for sampling from some desired distribution $\pi$. The idea behind $MCMC$ is that you can sample from $pi$ by constructing a Markov chain whose stationary distribution is $\pi$. You can then initialize at some random point $x_0$, and after letting the chain run for a "long enough" time (what is considered "long enough" is going to be contextual based on how closely your distribution of initialization positions matches the target distribution and the intrinsic properties of the target distribution), the statistics of any given stochastic realization of the Markov process will converge to the statistics of the idealized ensemble as a whole (i.e. to the statistics of $\pi$).

But an important aspect of MCMC is that the statistical realizations are *stochastic* processes: given a current position $x_k$,
it's not deterministic what the next position $x_{k+1}$ will be. One MCMC technique is Langevin Monte Carlo (LMC). Consider the Langevin
equation of the form:

$$dX_t = - \nabla V(X) + \sqrt{2} dB_t$$

where $V$ is the said to be the *potential* and $dB_t$ is standard Brownian noise. It's well known that (given sufficient regularity
conditions on $V$), then the stationary distribution of this Langevin equation will be $\pi \propto e^{-V}$. (For the physicists in the audience, you can interpret the stationary distribution as a Boltzmann distribution over position space with $\beta = 1$.)

But how would you implement this on a computer? We will want to discretize our time, and update $X_t$, step-by-step. A naive way that you would evolve $X_t$ over time would be, given a step size $h$:

$$X_{t+h} = X_t - \nabla V(X_t)$$