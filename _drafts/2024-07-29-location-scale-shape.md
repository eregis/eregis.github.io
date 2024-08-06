---
layout: post
title: Location, Scale, and Shape
date: 2024-07-29
mathjax: true
---

For any given parameteric family, there are many different ways that you can parameterize it. For example, for the normal distribution, you can parametrize it via:

* Using the mean $\mu$ and the standard deviation $\sigma$
* Using the mean $\mu$ and the variance $\sigma^2$
* Using the mean $\mu$ and the second moment $\mu^2 + \sigma^2$

Going between the most common parametrizations of the normal distribution is pretty straightfoward, so we rarely focus too much on which specific parameterization that we use.

But in general, there are certain "types" of parameters that appear over and over again with different parametric families.

Besides being common types of parameters, there is also the relationship between location and scale parameters via exponentiation: given a parameterized family with a location parameter, the exponentiation of that family will have a corresponding scale parameters. This isn't too surprising a relationship. Exponentiation is the unique continuous map from the real numbers as an additive group to the positive real numbers as a multiplicative group. (I believe this intuition is also behind the relationship between Lie Algebra and Lie Groups)