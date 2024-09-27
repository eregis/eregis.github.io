---
layout: post
title: "Post Template"
date: 2024-06-13
mathjax: true
---

What is the Fisher Information metric? The Fisher Information metric at a point tells you how distinguish

Here's the mathematical expression for the Fisher Information metric:

: <math>
g_{jk}(\theta)
=
- \int_R
 \frac{\partial^2 \log p(x \mid \theta)}{\partial \theta_j \,\partial \theta_k}
 p(x \mid \theta) \, dx.
</math>

While this is a bit of an unwieldy expression, a simple intuition for the Fisher Information metric is that it's a type of Hessian: it encodes second derivative information of the probability distribution at that point in the statistical manifold. 

Consider the two normal distributions below, both centered at the origin, but one have unit variance and the other have a variance of 10.

At a local maxima, the magnitude of the second derivative tells you how "strong" the local maxima: a large second derivative means that the distribution will be sharply peaked while a small second derivative means that distribution will be broad. The Hessian is a matrix because we want to represent the second derivative information along the different parameteric directions in one mathematical object.