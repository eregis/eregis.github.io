---
layout: post
title: "Physics-Style Approaches to Machine Learning"
date: 2026-01-08
mathjax: true
---

On the heels of my first successful research project, I want to reflect on what I've been calling a physics-style approach to LLMs.

By physics-style approach, it's honestly not so different from normal ML. But it helped (for me) conceptually to explicitly be telling myself "I am doing physics-style research except instead of natural systems, I am studying some aspect of these artificial systems as neural networks."

I think part of the reason why this is perhaps an usual move is that with physics, we don't know the fundamental laws, but the whole point of the game is that we need to figure out the laws. But in machine learning, it's one of the rare cases where for everything except the data distribution (which as I said that is a pretty big if---since there are many perspectives that a lot of the magic of machine learning comes form some je ne sais quoi property of the data distributions in the real world that make them learnable in some robust way (we choose "natural looking architectures" but those natural looking architectures come with them implicit biases that match the biases of the real world))

But ignoring the data distribution for a moment: what's interesting about machine learning is that we actually do in many cases know the microscopics physics. But in practice what we want is the effective description that is actually relevant to the things we care about: and often times, the goal of machine learning is bridging that gap in a systemic way.

This epiphany occured to me when I was working on my research project on Edge of Stability. I was trying to study Gradient Descent. And at the level of abstraction I was working with, I was even allowed to assume that the loss function was known. But the question becomes: how do you model gradient descent as an ODE? This is interesting because on the one hand "Given a loss function L and a step size $\eta$, find the ODE that passes through the iterates" is a perfectly well-defined mathematical question (that is interesting and hopefully will be answered rigorously in the near future). But the pathway that actually resulted in me making progress in attacking the question was treating gradient descent almost as a natural system that I was trying to model. This involves making a lot of not-very formal approximations, physical analogies. Specifically, the workflow was the biggest giveaway:

The workflow was

(a) observe some experimental phenomena (here that is edge of stability) 
(b) Consider what is known about this phemonema (other people's work)
(c) Then (and this is the part that felt from the most physics-style of the whole approach), start from first-principles and at each step, make reasonably sound, physically-motivated approximations until you end up with a model of the phenomemon that you after.
(d) Compare your model with experimental data (here simulutation) and observe the discrepancy. Based on the discrepancy propose reasons why your model is discrepant. 
(e) Consider the new "micro" empirical information, go back to your previous derivation of the model that involved probably like a dozen approximations and steps and reason about which one them is the one that is causing the discrepancy. Resolve this approxiation in some reasonable way. And derive a new model.
(f) Go back with your new model and compare to experimental data.
(g) Rinse and repeat until you have a model that you feel is satisfactorally optimized considering the range of phenomena that you are trying to model. Get some final experimental data together that show your model and explain the physical reasoning underneath your model (not just why it its the data, but why you believe your model to be "True".)

Move on to the next problem.

Why do I think there is room for physics-style approaches? Because just as the physical world is (we believe) to be mathematical, but is rich in detail.

It's because in the real world, we know that there is hierarchy of theories. 

But if you think about it: the machine learning models that we have are going to 

Again this is not new: but it's interesting to spell out the difference and to have it be.