---
layout: post
title: "The Piston Problem"
date: 2024-08-05
mathjax: true
---

Non-equilibrium thermodynamics is not usually covered in most undergrad classes. In order to build an intuition for the subject, let's consider the simple problem of the (effectively) one-dimensional piston: Given a prescribed path through thermodynamic parameter space, what is the distribution of microstates at the end of the trajectory?

[Picture of a piston being compressed]

In equilibrium thermodynamics, we limit ourselves to thermodynamic transformations in the *quasistatic* limit. Quasistatic transformations are those which, at each time point, the system can be treated as being in equilibrium. It corresponds to a limit where the thermodynamic transformation happens infinitely slowly. From a probability theory perspective, the thermodynamic equilibrium is a stringent constraint. The space of probability distributions over the phase coordinates of $N$ particles is forms an infinite-dimensional space projective vector space. In typical systems where we have 2 or 3 thermodynamic variables, the set of equilibrium distributions forms a manifold equalling the number of independent thermodynamic coordinates. Transformations in the quasistatic limit are constrained to paths on the statistical manifold of equilibrium probability distributions. 

A big thing about non-equilibrium statistical mechanics is that our notion of the "ensemble" subtly changes--or perhaps more accurately expands. In equilibrium thermodynamics, when we talk about the ensemble, what we mean is roughly: for a given set of thermodynamic coordinates, what is the distribution of microstates corresponding to it?

An important discussion point about the equilibrium ensemble is that it's a timeless picture: it's about the sample distribution of microstates for a given set of thermodynamic coordinates, but there is no (explicit) mention of dynamics or *time-averages*. If you want to talk about time-average of some statistical realization of our system, you need an extra ad-hoc assumption called ergodocity. Ergodicity says that if you have a system at a given set of thermodynamic coordinates, if you repeatedly sample from the system at "random" time points, you will recover the theoretical ensemble. Time-averages are the same as ensemble averages.

But in non-equilbrium stat mech, rather than associating the ensemble with each thermodynamic coordinate, we now have an ensemble associated with each *path*. Here the assumption is: given the same starting initial thermodynamic conditions, if you change the thermodynamic variables of e.g the resevoir in the exact same way, at each time point along the path in thermodynamic space, you will get some distribution of microstates. This distribution won't be the same as the equilibrium distribution, but will depend on the exact path taken.
The quasistatic assumption is so special because it takes the distribution of microstates, which in full generaltiy is a *path*-function and turns it instead into a state function of the thermodynamic coordinates.

You also need to supply extra, physical information to calculate non-equilibrium distributions. If transformations happen in finite time, you can no longer throw away the low-level Hamiltonian dynamics that govern the system. Going back to the problem of the piston, if you compress the piston in finite time, you need to now make physical assumptions about what the moving wall of the piston does to particles it makes contact to.

In the problem of the one-dimensional piston, we have that there is

