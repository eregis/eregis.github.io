---
layout: post
title: Location, Scale, and Shape
date: 2024-08-08
mathjax: true
---

For any given parameteric family of probability distributions, there are many different ways that you can parameterize it. For example, for the normal distribution, you can parametrize it by:

* Using the mean $\mu$ and the standard deviation $\sigma$
* Using the mean $\mu$ and the variance $\sigma^2$
* Using the mean $\mu$ and the second moment $\mu^2 + \sigma^2$

Going between the most common parametrizations of the normal distribution is pretty straightfoward, so we rarely focus too much on which specific parameterization that we are using.

But in general, there are certain "types" of parameters that appear over and over again with different parametric families. For example, there are support parameters which define the domain in which the probability distribution is non-zero. The parametric family of uniform distributions on the $\mathbb{R}$ can be parametrized by $\mathbf{U}(x; a, b)$ where $a$ and $b$ are the left and right end-points of the interval of support, respectively. There are degrees of freedom parameters for distributions that appear in statistical hypothesis testing like the chi-squared distributions or the F-distribution, where different sized data sets which have different shaped curves for various statistics.

I want to focus on three types of parameters: location parameters, scale parameters, and shape parameters. Besides being ubiquitous, they also are related to each other by exponentiation.

A location parameter is one that tells you where a probability distribution is located. For example, consider the alternative parametrization of the uniform distribution $\mathbf{U}(x; s, a)$. The It'sBesides being common types of parameters, there is also the relationship between location and scale parameters via exponentiation: given a parameterized family with a location parameter, the exponentiation of that family will have a corresponding scale parameters. This isn't too surprising a relationship. Exponentiation is the unique continuous map from the real numbers as an additive group to the positive real numbers as a multiplicative group. (I believe this intuition is also behind the relationship between Lie Algebra and Lie Groups)