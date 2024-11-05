---
layout: post
title: "'Log Concave Sampling' by Sinho Chewi"
date: 2024-11-01
mathjax: true
---

In statistics, there is commonly difficulties with sampling from multi-modal distributions. For example, 
if you have a bimodal distribution of unit variance, but a million units apart, then it will take unacceptably large amount
of time to cross the potential barrier between them if you use a standard algorithm like Metropolis Random Walk. Unfortunately,
generic distributions, *especially* in high-dimensional settings are usually multi-modal. But for theoretical analysis,
it's useful to restrict ourselves to uni-model distributions.

The Platonic ideal of a unimodal distribution is the Gaussian.

[Picture of a Gaussian]

But let's consider a generic distribution $p(x) \propto e^{-V(x)}$ If we want that our distribution is unimodel, then there needs to
be only one local maxima. This is equivalent to the derivative only having one root. Using chain rule, we get that

$$\frac{d p}{dx} \propto V'(x) e^{-V(x)}$$

If we assume that our probability density is non-negative, then $p$ being unimodal is equivalent to $V'(x)$ equaling zero at one point.
It's hard to characterize all functions which only attain a value of zero once. But one important class of functions that have this
property are monotonic functions. If $V'$ is strictly monotonic and equals zero at some $x_0$, then you know that it only becomes zero at
$x_0$. 

If V' is monotonic, what does that tell us about V? Well, the antiderivative of a monotonic increasing function is a convex function. 
And the anti-derivative of a of monotonically-decreasing function is a concave function. So if V is a convex function, then $-V$ is a concave function. That means that if $\log p$ is a concave function, then we know that $p$ is a unimodal probability density function.

Because the unique local maxima, corresponds to global maxima, log-concave distributions are really nice to study in a theoretical
context. Given all their structure, studying them can't be all that complicated, right? Right?!