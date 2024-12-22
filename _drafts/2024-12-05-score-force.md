---
layout: post
title: "The Score is the Just The Force"
date: 2024-12-05
mathjax: true
---

There many different types of generative models. A generative model is one that wants to learn the distribution of data. It should be
contrasted to a supervised learning model which wants to learn the correct mapping from input. For example, a supervised model might 
classify the digits. But it doesn't *explicitely* model how frequently each digit appears in the data set (though I assume that
the distribution of the data does implicitely get encoded in the supervised model. For example: let's say the model is asked
to evaluate an image that's ambigious: let's say between a 4 and 9. Then my intuition tells me that if 4's were more represented
in the original training set, borderline cases are more likely to be classified as 4's (and vice versa in the case that there were more
9's in the original training set))

So if you intepret our probability distributions as Boltzmann distributions $e^{-V}$. Then taking the log of the probability is
trying to learn the correct energy landscape that induces the above probability distribution. Extending the analogy, for score
based models that learn the gradient of the log probability $\nabla_x \log p(x)$ 

(The subscript on the gradient $\nabla_x$ is to denote that its the derivative
with respect to the underlying space. This is helpful because, historically, the score referred to the gradient of the probability 
distribution with respect to the *parameters*. The more modern definition of the score coincides with the older definition if we interpret $\nabla_x$ as gradient with respect to hypothetical location parameters that shift the probability distribution.)

This also may be a hint for why score-based modeling works. In the real world, we can't actually measure energies. What we can measure
are the forces. 