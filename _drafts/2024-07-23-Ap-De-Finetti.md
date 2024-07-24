---
layout: post
title: "A_p distributin and De Finetti"
date: 2024-06-13
mathjax: true
---

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

This is related to the law of total expectation which informally says that if your best point estimate is $$p$$, then in expectation, upon receiving some new piece of evidence, your average opinion shouldn't change.
You can imagine the A_p distribution almost like a Cauchy surface or something for general relativity or the infinite past in quantum field theory. In the Heisenberg picture of quantum mechanics, states don't evolve over time. So when going from the Schrodinger picture to the Heisenberg picture, you need to choose a representive for each state. One often-made choice is to associate every Heisenberg-state with the associated Schrodinger-state in the limit of the infinite past. So for example the vacuum state is the state which has "nothing in it" in the infinite past.

From this perspective, the Ap distribution is almost like a basis in which to decompose our current beliefs: you describe your current belief in terms of your distribution over future epistemic states that you expect to inhabit.