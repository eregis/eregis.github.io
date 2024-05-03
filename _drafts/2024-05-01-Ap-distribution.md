---
layout: post
title: "The Ap Distribution"
date: 2024-05-01
mathjax: true
---

E.T. Jaynes introduces this really interesting concept called the $$A_p$$ distribution in his book on probability theory. Despite being almost two decades old, this concept has not seemed to spread at all. When I google "Ap distribution" in an attempt to learn more, I got very little. Here's an attempt to explain it for a wider audience.

The A_p distribution is a probability about a probability. The proposition A_p says that "regardless of whatever evidence that I've observed, the probability that I will assign to proposition A is p". For example, let's we have a proposition that 

The intuition is that if we say that there is a 1/2 probability of A happening is 1/2, that can reprsent very different practical epistemic states. For example, imagine that you know for *sure* that a coin is fair: that in the long run, the number of heads equals the number of tails. Then in the A_p space, that would be represented by a delta function at p=1/2.

But imagine a different scenario where you haven't seen a coin get flipped yet, but you *know* that it's perfectly biased towards either heads or tails. Because of the principle of indifference, we would assign a probability of 1/2 as well--but it's a very different 1/2. Just one single flip of the coin is enough to collapse the probability to p = 0 or p =1 for all time.

That's what we are attempting to formalize.

So it makes sense that there is some uncountable basis

(But notice that there is no requirement that specifying the distribution over all A_p) fully determines our belief system. There can be propositions B which have bearing on our beliefs about A.
Thinking out loud here: is there a way to think about this in terms of some sort of kernel?

The mathematics of the A_p distribution turns out to not be very new. It's owed all the way to De Finitti about how distributions over exchangeable binary variables can be expressed using the binomial distribution with different $p$ as a "basis". What is new, however, is the interpretation in terms of metabeliefs that E.T. Jaynes brings.

How should we visualize the AP distribution. The babyish Venn diagram approach to thinking about probability is to imagine that you have a space and each proposition cover some subset of that space.

With this picture, what the A_p distribution describes is a region of the

Part of what makes the A_p distribution feel odd is the same reason why Dirac delta functions make students feel a bit quesy the first time they encounter it: It's pathological in the sense that, given finite time,

This becomes much more natural if, rather than considering a continuous pro

This then introduces a different notion of what is "strong" evidence. One notion of strong evidence is that it restricts what world you are in (I guess we could say strong, with respect to some proposition). But another notion of strong evidence--strong *meta-evidence*--

It seems normal strong evidence says something about what happens when you try to zoom out. (When you zoom out things will stay red) while strong meta-evidence says something about what will happen when you zoom in (when you zoom in the relative color)

So there are two notions of how strong a piece of evidence is: one is that it constrains what region you are allowed to be in
