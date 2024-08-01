---
layout: post
title: "Deriving The Fokker-Planck Equation From The Langevin Equation"
date: 2024-06-13
mathjax: true
---

This is yet another "folklore" derivation where "everyone" knows the derivation, but it's hard to find on the internet in one neat place. There are plenty of derivations that derive the Fokker-Planck equation given the Markov transition matrices, but it's harder to find derivations that start with Langevin equation.

A key idea in probability theory is differentiating between *random variables* and the *probability density function* of the random variables.

For example, let $X$ and $Y$ be random variables. There is a big difference between Z_1 = \frac{1}{2}(X + Y) and Z_2 whose pdf is a mixture of the pdfs of X and Y: h(x) = \frac{1}

The Langevin equation is an equation about stochastic differential equation. It's about an infinetsimal version of the algebra of random variables.

The Fokker Plank equation is about the probability density function where we have a multivariable function p(x,t) where for at any given time slice, we have a well-behaved probability density function.

How do we go between the two?

The way to think to derive the Fokker Plank equation is to consinder the PDF as an *operator*. Specifically, the PDF, when paired with definite integration over the bounds, can be thought of as a linear operator that maps functions of the random variable $X$ to scalars (the expectation).

This perspsective is not so odd. Students of physics will be familiar with a similar derivation for the commutator of $\hat{X}$ and $\hat{P}$ in undergrad quantum mechanics.

To recap the commutator is defined as 

$$[A,B] = AB - BA$$

A key insight is that the commutator of two linear operators is *also* a linear operator. If we know how the linear operator acts on an arbitrary vector (which in the quantum mechanical case would the space of wavefunctions), then we have defined our linear operator.

The next step is the proof is that we can be clever about our choice of basis. In this case, we work in the position basis.