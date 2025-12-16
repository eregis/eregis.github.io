---
layout: post
title: "Neural Tangent Kernel Explained"
date: 2025-01-01
mathjax: true
---

In yesterday's post, I made the point loss functions are non-convex because neural networks are non-linear functions of their parameters.

That statement wasn't inaccurate, but it elided a subtle difference: there is a difference between viewing the neural network as a function of the input (with the parameters fixed) and as a function of the parameters (with the data fixed). Specifically, you can have that the neural network is a linear with respect to its parameters while still being a non-linear function with respect to the input. Consider the simple example:

$$f(x; \theta) = \sum_{k=1}^N$$