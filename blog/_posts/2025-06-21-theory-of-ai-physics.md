---
layout: post
title: "Theory + AI Workshop: Theoretical Physics for AI"
date: 2025-06-21
mathjax: true
---

About a week ago, [I stumbled upon the website](https://pirsa.org/c25022) for a conference called *Theory + AI Workshop: Theoretical Physics for AI*.

> **Description:** This 5-day program will explore the intersection of AI and fundamental theoretical physics. The event will feature two components, a symposium and a workshop, centered around two complementary themes: AI for theoretical physics and theoretical physics for AI.

This was a conference hosted by the [Perimeter Institute for Theoretical Physics](https://en.wikipedia.org/wiki/Perimeter_Institute_for_Theoretical_Physics), located in Waterloo, Ontario. I didn't personally attend this conference (though I wish I did!), but it seemed like a good idea to spotlight it. It has a great invited speaker list, and recorded videos of the talks can be found at the bottom of the website.

![AI Physics Speakers](/assets/theory-of-ai-physics/ai-physics-speakers.png)

![Speakers Videos](/assets/theory-of-ai-physics/speakers-videos.png)

I haven't gotten around to watching most of the talks yet, but I want to flag David Berman's work as interesting. He has a pair of papers---[Bayesian Renormalization](https://arxiv.org/abs/2305.10491) and [The Inverse of Exact Renormalization Group Flows as Statistical Inference](https://www.mdpi.com/1099-4300/26/5/389)---that connect the renormalization group to Bayesian inference.

One thing that stands out about the conference is the healthy representation from Harvard attending the conference. This matches my experience as someone who has been splashing around in this area for the last couple of months. I don't know anything about the "initiatives" or priorities of different universities, but Harvard seems to be investing resources into artificial intelligence. For example, [they host the Kempner Institute for Artificial Intelligence](https://kempnerinstitute.harvard.edu/), "dedicated to revealing the foundations of intelligence in both natural and artificial contexts." Michael Albergo---current Harvard Junior Fellow, soon-to-be assistant professor in the Applied Math department at Harvard, best known for his work on [stochastic interpolants](https://arxiv.org/abs/2303.08797)---would have fit right into the invited speaker list for the conference as well.

In terms of my personal interests, I've been more interested in the "physics for AI" direction than the converse. Though I can easily imagine all of the interesting research trying to use machine learning to shed light on physical data. I remember stumbling upon some research out of Max Tegmark's group (an MIT physicist) where [they used machine learning models to learn the conserved quantities associated with a set of differential equations](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.109.L023301). And I remember chatting with a classmate about ["equivariant models"](https://arxiv.org/pdf/2205.07362) where they attempt to build the symmetry of the data into the machine learning model (e.g., if you are training a model to learn a function and you know a priori that your function should be rotationally symmetric, then you could build that symmetry directly into the architecture of the model, rather than hoping that the model organically rediscovers the symmetry in the data over the course of learning).

This is all far from my expertise, but it would seem that these ideas could all be put under the umbrella of "inductive biases": especially when dealing with these highly over-parametrized deep learning models, there are many possible parameter values that could fit the training data, so it's important to understand what types of solutions a given architecture will tend to converge to in practice. This can be a useful perspective on even something as simple as a convolutional neural network (CNN). 

Recall that, given two functions $f$ and $g$, the convolution of the two functions is defined as:

$$f * g (y) = \int f(y - x) g(x) dx$$ 

While convolutions are symmetric ($f * g = g * f$), to understand a convolutional neural network it's best to think of $f$ as the kernel (which is to be learned by the network) and $g$ as the input. One can see that there is translation invariance built into the kernel by design. Furthermore, in machine learning, the kernel will also be made to have finite support (called the filter size), which enforces locality. A perspective on why convolutional neural networks work well is that their architecture incorporates these two inductive biases: locality (through finite filter size) and translation symmetry (through the convolution operation itself). Locality and translation symmetry are useful inductive biases because they are (approximately) "actually" true of real-world data.

