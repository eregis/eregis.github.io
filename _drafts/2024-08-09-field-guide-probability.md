---
layout: post
title: "'Field Guide to Probability Distributions' by Gavin Crooks"
date: 2024-09-12
mathjax: true
---

My first intellectual obsession was Pokemon. I watched the show religiously and played Pokemon Silver on my Gameboy Advanced SP until the late hours of the night. 

Pokemon is the largest grossing media franchise in the world. The franchise spans video games, TV Shows, movies, trading card games, action figures, and more. The reason why Pokemon is so popular is that it taps into a childlike need to collect. "Gotta catch 'em all!" isn't just a clever marketing catchphrase, but gets at the very heart of the ethos of Pokemon. When kids are small, they are curious about learning about the natural world: categorizing the different species of flora and fauna that they will be encountering throughout their lifespan. In my case, not only was I obsessed with Pokemon, but I was also obsessed with Animal Planet and books about species of Old World monkeys and apes.

The creator of Pokemon got the idea from collecting bugs, a popular hobby among boys in Japan (which is also why Bug Catcher is such a common class of trainer in the Pokemon Universe.)

I've since moved on from Pokemon. The last Pokemon game I played was Pokemon Ultra Sun near the end of high school. After one slow cutscene too many, I called it quits. (Though I still watch competitive Pokemon on YouTube.)

But the boyhood impulse to collect is still there. Just channeled into different forms. When I started to get into statistical physics and probability theory, I started "collecting" different probability distributions. Just like how the different Pokemon have different stats and attributes, the different (parametric family) of probability distributions have different characteristics: their domain of definition, the number of degrees of freedom, common physical situations where they arise, their relationship to other probability distributions, etc. Wikipedia was helpful for this as it has a page listing various probability distributions organized by their support: https://en.wikipedia.org/wiki/List_of_probability_distributions. When I was bored in class, I would just load the Wikipedia page and read about some obscure distribution that arises in population ecology, fascinated by its high-level characteristics and curious if I will ever encounter a situation where just that distribution might come in handy.

The problem with the Wikipedia page, however, is a lack of structure. Sure, it organizes the distributions by their domain of support. But what's fascinating about probability distributions is that they are interconnected in various ways. Some distributions are special cases of other distributions. Sometimes there are algebraic relationships between distributions like how the chi-squared distribution is the sum of iid normally-distributed random variables squared.

I thought it would be cool to have a side project where I create a *Pokedex* for probability distributions: rather than just cataloguing them in one place, I create a comphrensive go-to encyclopedia for *understanding* the world of probability distributions.

It turns out that Gavin Crooks already beat me to the punch.

#The Structure

Gavin Crooks is a chemist, well-known for his work on non-equilibrium statistical mechanics and thermodynamics (his most famous contribution is perhaps the Crooks fluctuation theorem). Despite being a chemist by training, his work is easy to parse for someone like me who comes from a physics background. (I've leafed through some work under the purview of "chemical thermodynamics"--usually involves lots of $\Delta G$ calculations--and I've had a hard time understanding what was going on.)

After years publishing his various non-equilibrum statistical mechanics results, he decided to write the book *Field Guide to Probability Distributions*. Here is the family tree of probability distributions featured in the book:

[link to picture of heirarchy of probability distributions]

The way the tree is structured is that at the top most root is the most general distribution: the grand unifed distribution (GUT) and then daughters are special cases of the parent leaf. Imagining each point as a parametric family, a special case is a parameteric family which corresponds to some submanifold. That can be acheived either from setting to a concrete value, defining a relationship between a couple given parameters or by taking some type of limit.

The book starts at the bottom leaf nodes. These are familiar distributions like the uniform distribution, the normal distribution, and the exponential distribution. It then considers more and more general cases: the exponential distribution can be viewed as the beta distribution.

In each mini-chapter, there are handy statistics provided about each distributions like its moments and alternative names or alternative parameterizations.

One of the strong points of this book is it uses consistent notation throughout the entire book for various conventions. For example, scale parameters which appear in distributions as diverse as the uniform distribution and the [example distribution] are often denoted as $s$. Or how location parameters are denoted as $a$. Small little consistency checks like this do a lot for helping to understand the connections between the distributions.

This book is limited to continious, uni-dimensional probability distributions. This seems like a wise choice as the heirarchical structure of the book. While there are often connections between discrete and continuous probability distributions, the relationships can't be neatly codified using the hierarcahl structure that the book decides to adopt. Discrete distributions also have a different flavor to them: they lean more heavily on various contexts from combinatorics. As for multivariate distributions, those are much too complicated; as you need to not only specify the marginals, but also the arbitrarily complicated correlation between the individual random variables.

[properties of the uniform distribution]

A common convention is Gen. X, where Generalization stands for the Weibullization of the parameteric family $X$. This was not a convention that I was familiar with before the book, but it's really nice and it can be a way to connect seemingly disparate distributions into one parameter family.

At the very top of the tree is the Grand Unified Distribution:

[picture of grand unified distribution]

It's hypothesized by Crooks that every continuous probability distribution is the solution of a differential equation for some values of the parameters. Furthermore, that all the distributions in this book satisfy the differential equation for low-order (degree 2 polynomials) in the numerator and denominator.

I still haven't fully digested what the GUT is trying to tell me. There is an obvious connection to exponential families: it's in many ways the generalized form of exponential families where in exponential families we often consider moments, but here we consider rational fractions. There is something vaguelly familar about the form of this: like perhaps I've seen this kind of general equation form for Fokker-Plank distributions or something.

Let's work through an example, given the standard normal distribution, it satisfies the equation

$$\frac{d}{dx} \log p(x) = -x$$

Well some obvious observations: the local maxima of the distribution correspond to zeroes of the polynomial.
I'm trying to think if there is a connection between the GUT and each distribution being considered as the Gibbs ensemble for some energy landscape $E(x)$.

Well, for the exponential distribution $E(x)$ is

Okay, I see: So the Gibbs ensemble corresponds to  $E(x) = - \ln Z - \ln p(x)$
So if we view this is a Gibbs Ensemble, then we are saying that the energy landscapes for most distributions tend to be the derivative of low-level rational functions. 

So what's the hypothesis here. For something like the exponential and normal distribution, their prevalence can be interpreted from a maximum entropy perspective where they correspond to the maximum entropy distribution for constrained mean and contrained variance, respectively. What's the physical interpretation of the derivative of the energy landscape with respect to some parameter that is indexing the number of different microstates.

Why would the generic Hamiltonian be a small fraction

It perhaps helps to see which distributions require 

Another wrinkle that I didn't fully appreciate is that we have a leading 1/x term in the GUT. Why is that the convention? Sure, it's more expressive. But is that it?
