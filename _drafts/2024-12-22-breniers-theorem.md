---
layout: post
title: "Breniers Theorem"
date: 2024-12-22
mathjax: true
---

One intended purpose of this blog is to make various important theorems and definitions in the subfields that I work in legible to search engines. A lot of the most useful theorems in optimal transport don't have well-maintained Wikipedia articles. This is annoying because sometimes I'll look up. Posts like this might be somewhat more inside baseball than what I usually aim for in this blog, but they are really meant for Future Me to have a quick place to reference.

Brenier's theorem says that the Wasserstein-2 distance is given by the 

The idea behind Brenier's theorem is that gradients of convex function.

A convex function is on where the output of the average is less than the average of the outputs

$$f((1-t)x + ty) < (1-t)f(x) + tf(y)$$

Geometrically, this means that given two points of a function.

The Platonic convex function is the upwards-facing quadratic $f(x) = x^2$. (Downwards facing quadratics are importantly *not* convex. They are concave.) This is perhaps the easiest way to think about convex functions: is it roughly shaped like a 

Another notion of convexity, applicable to when $f$ is twice-differentiable, is when the Hessian $\nabla^2f$ is positive-semidefinite.