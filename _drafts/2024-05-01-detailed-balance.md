---
layout: post
title: "Six Intuitions About Detailed Balance"
date: 2024-05-01
mathjax: true
---

Shorter post:

Wikipedia has to ways to check if a transition matrix obeys detailed balance. That is in terms of the stationary distribution and in terms of the cycles of the graph. These are fine intuitions, but I feel like Wikipedia neglects a couple perspectives on detailed balance that are practically useful when considering the condition on a research setting.


A transition matrix $$T$$ describes a system obeying detailed balance if

$$T = D S$$

where $$D$ is a diagonal matrix and $$S$$ is a symmetric matrix. This means that 

Consider the following analogy.


# Pairwise Stationarity

Imagine there is a system of banks that have to send money to each other. And for some reason, money is exchanged in the old-fashioned way where each person sends a representative with a briefcase to exchange money with the other banks so representative with a briefcase (so if there $N$ banks, then each bank has $N-1$ representatives corresponding to its relationship with the other banks.)

The way money is exchanged is that each bank must send a certain percentage of its total money to each of the other banks. The percentage that e.g bank A has to send to bank B is fixed and doesn't change day-to-day.

Assume that no money enters or leaves the system, so the total amount of money across all the banks is constant. Furthermore assume that we eventually reach a steady state.


# Rescaled Symmetric Transition Matrix

Detailed balance is closely related to the thermodynamic arrow of time: systems that obey detailed balance are such that forward trajectories are indistinguishable from backward trajectories. Given that physical intuition, it would seem reasonable to guess that in a system that obeys detailed balance the transition matrix should be symmetric.

This turns out not be *quite* correct, but it's pretty close to the truth. With a slight modification, we get the actual constraint which the Markov matrix must obey.