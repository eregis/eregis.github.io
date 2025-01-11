---
layout: post
title: "The Different Types of Fisher Information"
date: 2024-12-11
mathjax: true
---

Depending on the application 

But an alternative way to characterize a probability distribution is called the Fisher Information. But somewhat confusingly,
the terminology and notation here is weirdly non-standard: different literatures have different notions of the Fisher information depending on their purpose. What they all have in common is that they seek to understand the probability distribution in terms of its
*gradients*--but different notions of the Fisher Information will have different notion of the gradients and the gradient will
act on different transforms

#Fisher Information from Information Geometry

The original Fisher information that you will see in context like Information Geometry. It's Let $p(x\theta)$ be a
parametric family of probability distributions. Then the Fisher Information is given as

$$\

# Fisher Information from Score-Based Generative Models

A common way to represent probability distributions is of the form $p(x) = \frac{e^{V(x)}{Z}$}$ You can view an arbitrary probability
distribution as a Boltzmann distribution over the sample space. This is helpful. Let's say from this perspective when you are performing
variational inference where you are trying to minimize the KL divergence between your reference 

# The Relative Fisher Information

This is also known as the relative fisher information. 
It's a pretty direct analogy between the how the KL divergence measures the *relative* entropy between 
the source distribution and the target distribution.

The relative Fisher Information is given as 

$$\mathbb{E}_p[\nabla \log(\frac{dp}{dq})]$$

The relative Fisher information is the quantity that appears in things like the Poincare and log-Sobolev
inequalities (These are called "functional inequalities").

Somewhat confusingly, there is an alternative form that the relative Information sometimes takes

$$\mathbb{E}_q[\nabla sqrt{f}]$$

But this expression can actually be shown to be equivalent to the definition of the relative Fisher information.

The definition of the relative Fisher Information. A general property of the Fisher information is that.

As I explained in my previous post, the score is just the force, so the Fisher Information quantifies the extent
to which two distributions tend to locally look the same from each other.