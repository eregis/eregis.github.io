---
layout: post
title: "Three Notions of Convexity"
date: 2024-12-13
mathjax: true
---

Convex functions play an important role in sampling. For example, Gibbs measures with convex potentials have strong convergence properties. You can show that the relative entropy between the target distribution and the current distribution will exponentially decay.
This is important because it means that even if the distribution you are starting from is "far" from the distribution you are trying to sample from, you will be able to produce a sample with a reasonable number of iterations of the algorithms.

Because of the importantance of convex functions, it's important to understand their properties as a lot of proofs will rest on being 
comfortable with them. If we restrict ourselves to smooth functions $\f: \mathbb{R}^d \rightarrow \mathbb{R}$, then there are
actually three equivalent notions of convexity.

1. A function is convex if for all $x,y$, we have that $f()$
2. If for $x,y$, 
3 If for every point $x$, $\nabla^2 f \ge \alpha I_d$

There are many other properties of convex functions. But these are the ones, based on my somewhat brief exposure to these concepts, that I see invoked as textit{definitions}.