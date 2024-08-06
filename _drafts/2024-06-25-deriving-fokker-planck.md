---
layout: post
title: "Deriving The Fokker-Planck Equation From The Langevin Equation"
date: 2024-08-05
mathjax: true
---

In probability theory, it's important to to differentiate between *random variables* and *probability density functions*. While random variables are uniquely defined by their PDFs, the "calculus"--the rules of manipulation--for random variables versus those for probability density functions are quite different. It's important not to get them confused.

We will be deriving the Fokker-Plank equation from the Langevin equation. The Langevin equation is a stochastic differential equation that was originally used to model the velocity of a Brownian particle acted on by a drag force and thermal fluctuations:

$$\frac{dX}{dt} = - \lambda X + \eta(t)$$

where $\eta$ is delta-correlated noise (noise whose fluctuations from moment-to-moment are uncorrelated with each other).

The Fokker-Plank equation is partial differential equation that governs the time-evolution of the probability density function. The Fokker-Plank equation gives us the partial time derivitive of the probability density function in terms of a convection term and a diffusion term.

$$\frac{\partial p}{\partial t} = \frac{\partial}{\partial x} [\mu(x,t) p(x,t)] + \frac{\partial^2}{\partial x^2} [D(x,t) p(x,t)]$$

The Langevin equation is formulated in terms of of the infinesstimal calculus of random variables whereas the Fokker-Plank equation treats the flow of probability density.

This is yet another folklore derivation where "everyone" already knows the derivation, but it's hard to find it on the internet presented simply. There are plenty of derivations that derive the Fokker-Planck equation starting with Markov transition matrices, but it's harder to find derivations that start with the Langevin equation.

(If I am not mistaken, the reason why the derivation using Markov transition matrices is more popular is that this was how it was originally derived by Kolgomorov; the Fokker-Plank equation goes by many names, including being called Kolgomorov's forward equation.)

The Langevin equation is an equation about stochastic differential equation. It's about an infinetsimal version of the algebra of random variables.

The Fokker Plank equation is about the probability density function where we have a multivariable function p(x,t) where for at any given time slice, we have a well-behaved probability density function.

How do we go between the two?

The way to think to derive the Fokker Plank equation is to consinder the PDF as an *operator*. Specifically, the PDF, when paired with definite integration over the bounds, can be thought of as a linear operator that maps functions of the random variable $X$ to scalars (the expectation).

This perspsective is not so odd. Students of physics will be familiar with a similar derivation for the commutator of $\hat{X}$ and $\hat{P}$ in undergrad quantum mechanics.

To recap the commutator is defined as 

$$[A,B] = AB - BA$$

A key insight is that the commutator of two linear operators is *also* a linear operator. If we know how the linear operator acts on an arbitrary vector (which in the quantum mechanical case would the space of wavefunctions), then we have defined our linear operator.

The next step is the proof is that we can be clever about our choice of basis. In this case, we work in the position basis.