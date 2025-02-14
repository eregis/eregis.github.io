---
layout: post
title: "My Current Research Agenda"
date: 2025-01-31
mathjax: true
---

I've been working with my current professor for a couple months now. These months have mostly been spent reading. Even
though I am a physics student, I am working in statistics and machine learning. While I had some background in these topics (which is
why I wanted to work with him in the first place), I still had a *lot* of catching up to do---especially with respect to some of
the more technical things he researches (e.g optimal transport theory).

But we both agreed that I'm ready to start getting my hands dirty on some actual research. We've settled on a couple different
directions that seem promising. What they all have in common is that they allow me to carry over my physics background to
help acheive understanding quickly and perhaps provide a somewhat different perspective than other people working on the same
problems. There are three main areas:

1. Diffusion Models

2. Entropic Optimal Transport

3. Renormalization and Sampling

# Diffusion Models

Diffusion models are a type of generative model, most commonly found in popular image generators like Dalle-2. The way a diffusion model
work is that during training, images are gradually blurred until they become white pixel noise. You then train a neural network to be able to deblur the image. Then, once the model is fully trained, you

# Entropic Optimal Transport

Optimal transport is a subfield of probability that, abstractly, studies the property of a "transport plan": a way to transform
one probability distribution into another with minimal "cost" (where the precise cost function can vary). The most common type
of cost functions studied as the Wasserstein-$p$ cost functions where the cost function is the Euclidean metric raised the the $p$-th power. (It's important to keep in mind that the the Euclidean metric raised to the $p$ power is decidedly *not* the same thing
as the $p$-norm of the difference of two vectors!)

$$W^p(\mu, \nu) = \inf_{\gamma \in \Gamma} ||x-y||^p d\gamma(dx,dy)$$



# Renormalization and Sampling

The last research direction I am think about exploring is applications of the renormalization group to sampling.

The renormalization group is an "apparatus" from physics that your physics changes with scale.

Despite being central to the last fifty years of theoretical physics, the renormalization group remains obscure outside of physics.
I personally no idea what it was when I graduated from undergrad and couldn't give anything more than the vaguest articulation until
after I had started my PhD.

But recently, renormalization group has drawn the interest of mathematicians who are looking to formalize the tool. My advisor and I
have been reading the work of Roland Bauerschidmt, a probability theorist at NYU, who has been working on a formalization
of the renormalization group in purely probability-theoretic language. 

This is useful because it has potential applications to sampling. In sampling, we often

One of the most important theories in sampling is the Bakry-Emergy theorem. Let's say you have a Gibbs measure of the form $e^{-V}$. 
An intuition is that this distribution is easy to sample from if the distribution is unimodal. If a distribution is unimodal 

Bakry-Emery theorem allows us to connect the properties of the potential (it's convexity parameter $\alpha$) and 

But a lot of distributions are not unimodal. So you wa

Imagine that you have following distribution; If you naively try to sample from this distribution

Indeed, similar to the work on entropic OT, there's a perspective that smoothing or adding noise just isn't useful, but actually
has some deeper physical meaning: when probing any system there is some minimal length scale

This is the idea behind a slew of techniques that my advisor calls multi-scale Bakry-Emery theory: you have a complicated distribution
with lots of modes, but if you course-grain enough it becomes a smooth distribution that you can sample from due to Bakry-theorem.