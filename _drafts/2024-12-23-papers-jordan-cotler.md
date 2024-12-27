---
layout: post
title: "Jordan Cotler's Papers on Optimal Transport and Machine Learning"
date: 2024-12-23
mathjax: true
---

Global pandemics are mostly bad. 

But there were some bright spots. One of them was that a lot of techniques,

While I enjoyed the talk, I couldn't actually engage with any of the technical details.
Things have changed. It's been two years, and in the intervening time, I've matured considerably as a physicist.
I've now read a couple graduate-level books on statistical physics and optimal transport, and I'm even a bit more
familiar with some of the technical details of machine learning. So when I revisited Cotler's papers, I found them
accessible, albeit still technical and challenging, of course.

On this blog, I usually aim to explain the concept that I talk about because otherwise---what's the point? I've gone
back and forth on whether or not I want to talk about cool papers that I've read. I've held up on not doing them
because to properly explain why a given paper is interesting will require summarizing the entire state of the subfield--which at that point, that's as much work as a book review (but book reviews are easier because the first couple chapters are all about setting the stage anyway. So I can just follow the structure of the book when motivating the book to the reader.)

The compromise that I've settled on is rather than going all out with the physical analogies and concrete examples, I'm going to talk about a big batch of papers at once and explain what I like about them/found interesting about them--without worrying at all about if it makes any sense. This seems particularly apt in the case of Cotler's papers
that I will be talking about in that a lot of them are more interesting is how interdisciplinary they are. I have
a better handle on the optimal transport concepts, for example, but he connects them to high-energy theory concepts like Polchinski flow and the Wegner Morris equation which I weren't familiar with before reading the papers.


# Renormalization Group as Optimal Transport

The idea behind this paper is that when the renormalization group can be thought of as defining a gradient flow with 
respect to field-theoretic entropy. Moreover, this field-theoretic entropy is precisely the field-theoretic functional
given by the Gaussian free theory with that corresponding mass parameter at that energy scale.

The formulation of Renormalization Group that he uses is the Polnchiski equation. The Polchinski equation is an example of an exact RG flow. The most famous example of an RG flow is Kadanoff Block spin renormalization