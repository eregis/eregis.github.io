---
layout: post
title: "How to Find the PDF of a Function of Random Variable"
date: 2024-06-24
mathjax: true
---

Let $$X$$ be a random variable with a PDF given by $$f(x)$$ and a CDF given by $$F(x)$$.
Let Y be a random variable such that $h(X) = Y$. Let $g(y)$ and $G(y)$ be the PDF and CDF of Y, respectively.

The question is: given the PDF and CDF of X, how does one compute the PDF and CDF of Y?

This is a ridicoulosy simple question. When I was first learning probabiity theory, it was the very first question I had. Yet somewhat frustratingly, the usual sources of information (e.g Wikipedia) didn't lay out the procedure simply and in full generality. It was only until I read Gavin Crook's *A Guide To Probability Distributions* that I found what I was looking for. It's quite simple, here's how it works.

The short explanation is that the relationship between the two random variables is most naturally expressed through their CDFs. Specifically, the relation is G(y) = F(h^{-1}(y)). With this formula, two questions come to mind.

1. Why is that there is a simple relation between the CDFs of the two random variables and not the PDFs of the two random variables? (Use of chain rule can quickly derive the relation between the PDFs.)
2. Why is it that we want to apply the *inverse* of h to.