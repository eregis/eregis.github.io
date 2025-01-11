---
layout: post
title: "The Shift-Composition Rule"
date: 2024-01-03
mathjax: true
---

I've been reading this trilogy of papers by Sinho Chewi and Jason Altshuler called the Shift-Composition Rule.

These sets of papers are really cool to me because they introduce a fairly simple lemma/theorem (the aforementioned
Shift-Composition Rule) and then use that to prove a whole slew of technical results. I'm still chewing on the exact
technical details, but it seems that the key innovation is that the Shift-Composition rule is a purely information-
theoretic theorem. There were previously results that we suspected had to be true based on information theory-type
arguments, but had to be proved my more indirect and inelegant means. The Shift-Composition rule represents
a breakthrough in that respect.

Okay, so what is the Shift Compositition rule?

We've previously talked about the chain rule in probabilitiy: that a joint probability distribution can
be decomposed into a marginal distribution and a conditional distribution.

$$P(A,B) = P(B|A) P(A)$$

There is also a chain rule for the entropy. Given two random variables, $X$ and $Y$ can be decomposed into
a marginal entropy and the (expected) conditional entropy.

$$H(X,Y) = H(Y|X) + H(X)$$

That they are both called "chain rules" is not a coincidence. One can prove the chain rule for the entropy
with few lines of algebra: 

(A general rule of thumb: entropy is the expectation of the logarithm of the probability. The logarithm
is the unique function that maps the positive real numbers as a multiplicative group to the real numbers as
a an additive group $\log(ab) = \log(a) + \log(b)$)