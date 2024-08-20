---
layout: post
title: "The Mutual Information Between Gaussian Processes"
date: 2024-08-09
mathjax: true
---

For bacterial chemotaxis, we care about how the "signal" (usually the time derivative of the log of the ligand concentration) is tranducted into the activity (the concentration of CheY-P in the cell). One approximation, that can be used when the bacteria is navigating in shallow gradients, is that the signal is a Gaussian, and that the activity is related by a linear kernel to the signal, plus some uncorrelated noise. In frequency space, that looks like

$$A(w) = K(w) S(w) + N(w)$$

where $A$ is the activity, $K$ is the response function from signal to activity, $S$ is the signal, and $N$ is the noise.

$S(w)$ and $A(w)$ are stochastic processes, and stochastic processes are nothing more than infinite-dimensional random variables (often indexed by time, though here we are considering the frequency representation). Just as with single random variables, we can ask: what is the mutual information between $S$ and $A$ under our assumptions? The mutual information is given by the following formula:

$$I = \int d\omega \log \left (1 + \frac{K(w) S(w)^2}{N(w)^2} \right)$$

The derivation for this formula is surprisingly hard to find. It's a key lemma used in the *E coli is information limited*, a blockbuster paper that my lab produced a couple years ago. The citation attached to the formula goes to this 2009 paper by ten Wolde where the formula is produced without elaboration. So let's try to fill in the steps.
