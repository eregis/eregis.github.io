---
layout: post
title: "Jarzynski's Equality Explained"
date: 2025-01-08
mathjax: true
---

Due to the second law of thermodynamics, we know that for any process the work $ W \le \Delta F$. This is because,
if this were not true, then you could build a perpetual machine--which is equivalent to being able to decrease the
entropy in perpetuity.

One of the annoying things in statistical mechanics is that because the second law is stated
as "entropy must increase over time", a lot of the main results are *inequalities*. They place a bound on
what happens. 

But what would be desirable are statements that are *equalities*.

Another thing is that consider some process where we go from state A to state B. The Free-Energy is what is called a
state function $F$. Every system (described by its thermodynamic coordinates) has some free-energy. And so
the change in free-energy can be found just by taking the difference: $F = F_B - F_A$.

But the work is a bit different than that. The work is called a path function. To know the work, it's not enough
to know the starting and end points. You also need to know the journey taken between.

But there is a subtlety: Knowing the "path taken" is not just about knowing about the path as represented in thermodynamic

But there is an even *further* subtletly: even if you know the exact parametrization of your path,
you *still* don't know the work. The reason why is that our "states" A and B are actually ensembles of microstates.
Specifically, for a given thermodynamic

To see what I mean, consider the problem of the 1 dimensional piston. We can represent the thermodynamic state of the
piston using two thermodynamic coordinates: its temperature $T$ and its volume $V$. The act of compressing the piston
corresponds to the path where we keep the temperature constant and move to the left.

To see how the work is itself stochastic consider two different initial states.

One is a "typical" state where the gas molecules are distributed approximately uniformly throughout the gas with
a distribution of velocities that are both indepedent of their location and in accordance with the temperature of
the system. When compressing the piston, gas molecules that are in the way will bounce off the piston wall.
The imparted momentum per unit time is the force necessary to compress the piston. For a homogenous initial state
with a constant compression velocity, this force will be essentially constant because the large number of gas molecules
will make the standard deviation in the force at any given point in time tiny compared to the average force.

But consider a different initial state where, by happenstance, all of the gas molecules happen to in the left half
of the piston when we initialize our compression. Then we will be able to compress the piston without encountering
an resistance along the way, so no force is required. But that means there is no work!

So even for a well-defined process where we try to keep everything as controlled as possible. Same initial conditions,
same compression velocity, and same ending volume, the work performed is inherently stochastic.

However, while the work is stochastic. There is a solution. We can perform the same process many times over 
and over again, and measure the amount of work performed. This will form a distribution. We can then take the *average*
work. This average work *will* be a well-defined path function.

So that means that we can amend our statement above to be more accurate:

$$F \le \langle W \rangle$$

In machine learning, there is something called a softmax function. It takes the maximum that is given by
for example let's say you have some neural network where the final activations are meant to be probabilities
of classifying a given input in a certain category. 

The softmax function is actually called a generalized mean inequality. You are already implicitely familiar.

For example, for any probability distribution the variance is given as 

$$\sigma^2 = \langle X^2 \rangle - \langle X \rangle^2$$

The variance is always positive

This is called the *generalized* mean inequality. But we can generalize this generalized mean inequality. Instead
of just thinking about powers, we can generalize this into general functions.

How do compare general functions? Based on their *convexity*: convexity, in this case should be thought of in terms
of the the second derivative: how large is it. The exponential is the largest convex function; in that we see that
there is more to it than that. We see that there is more to it than that.

But conversely, the exponential decay is less convex than any power of p--including negative powers.

A way to think about this generalized mean inequality is that the less convex the function used, the more
it "weights" the lower values it's trying to average. This is why using e^x is called the soft-max function.

This is evidently, another way to view the Boltzmann distribution: it's the soft-min function. It averages the 
the.

This notion of a soft-min is quite useful it tells us that it's not just that free energy is

Jarzynki's equality says that the free energy is the soft-min of the work.

The intuition is that the distribution of the work doesn't really have a minimum--or even if you argue that it has a minimum
on physical grounds, this minimum corresponds to exponentially many coincidences to occur. What we care about
is not the minimum about of work that can be performed during a thermodynamic operation, but something like
the minimum amount of work without an absurd number of coincidences. This is the soft-min function.