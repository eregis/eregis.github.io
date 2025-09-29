---
layout: post
title: "'Notes on Machine Learning for Physicist' by Jared Kaplan"
date: 2025-09-22
mathjax: true
---

Jared Kaplan is a former conformal field theorists who switched to machine learning. He's most famous for being a co-founder
of Anthropic, one of the leading AI companies. He's also known (in the context of machine learning) for his work
on machine learning.

I am taking a Physics of AI class that is using Jared Kaplan's lecture notes as the main resource for guiding the course.
I decided to give them a quick read as---based on the title---I am exactly the target audience. What I found surprised me: these lectures
notes are *really* good. I hadn't heard of them before, so I wasn't expecting. I would say that if you are a
physicists looking to learn more about traditional machine learning (not machine learning that is specifically relevant to physics),
these are one of the first places that I would look for.

# Three Types of Learning 
In the first section, Kaplan does a great job of grounding the discussion.

One of the eerie things about these lecture notes is that 

Kaplan focuses on three main areas of machine learning:

* Supervised Learning

* Reinforcement learning

* Unsupervised Learning


And there's a fun reduction of unsupervised learning to supervised learning by Kaplan.


# Mathematical Foundations of Machine Learning

In terms of mathematical pre-requisites: while like with all technical fields, machine learning research get arbitrarily complicated (nothing is better than reading a machine learning paper that invokes an obscure result from random matrix theory),
the mathematical prerequisites to understand the basics at the level that Kaplan is presenting (and honestly, considering the empirical nature of the field, it's the level needed to understand the heuristic reasons why machine learning models work) is probability theory at the advanced undergraduate level. Kaplan dedicates a section going over the mathematical basics of information theory. Probability theory plays a key role in all three of the main areas of machine learning that Kaplan looks at.

In the context of unsupervised learning, we are literally learning a probability distribution over the data distribution. For the case of supervised learning, it helps to revisit the perspective that machine learning is "just" very complicated highly parametreized regression. In statistics, they often revisit the probability theory basics for proving various things about regression. And for reinforcement learning, we often model our policy (the mapping from current state onto actions) as a probability distribution over the next action and often times the environemnt (which dictates the reward and twhat state we transition to next) will be stochastic as well. In unsupervised learning, you often talk about the bias of an estimator

He has one chapter on information theory and another chapter on probability theory.

# The Empirics

Kaplan also has a nice overview of more empirical considerations relevant to physicists.

One is optimization. Optimization describes the proces sin which the machine learning model uses data to minimize the loss function. While there is a large volume on optimization, neural network loss landscapes are highly non-convex whereas our theory is mostly understood for the convex case. In terms of optimization algorithms, the main one to understand is stochastic gradient descent. With stochastic gradient descent, you choose a mini-batch of your data and update the parameters based on the gradient for your mini-batch.

He also talks about various like layer norm and batch norm. In batch norm, you make shift the parameters so that the statistics across the batch is normalized. With layer norm, you instead normalize across the layer for one given example.