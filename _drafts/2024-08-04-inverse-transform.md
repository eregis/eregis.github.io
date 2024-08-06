---
layout: post
title: "Inverse Transform"
date: 2024-06-13
mathjax: true
---

We previously talked about how to get the find the PDF of a function of random variable. But we could ask the converse question: given two PDFs, what would be the corresponding function acting on the random variables to go from one function to another?

It's perhaps less obvious why we would care about this question (other than intellectual curiosity of course!). As far as I'm aware, the main application of this in the context of generating samples from random distributions in simulations. It's a well-studied problem how to generate "good" (as in independent and identically distributed) from e.g the uniform distribution. So it would be helpful if, instead of having to invent bespoke algorithms for each probability distribution, we could generate random samples from the uniform distribution and "convert" those to random samples of the distribution of our choosing.