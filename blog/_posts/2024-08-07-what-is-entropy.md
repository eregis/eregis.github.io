---
layout: post
title: "'What is Entropy?' by John Baez"
date: 2024-08-07
mathjax: true
description: "A comprehensive review of John Baez's pamphlet on entropy, exploring its mathematical definition, applications in thermodynamics, and connections to information theory. This post delves into the concept of entropy as missing information and its significance across various fields of physics."
keywords: entropy, John Baez, thermodynamics, statistical mechanics, information theory, physics, mathematical physics, probability theory, maximum entropy principle
---

No, but seriously: What the hell *is* entropy?

Despite [entropy](https://en.wikipedia.org/wiki/Entropy) being the central object of study in thermodynamics, and thermodynamics being one of the central pillars of physics, the answer to the question of "What is entropy?" can be surprising elusive. Entropy rivals many of the "paradoxes" of quantum mechanics in how much confusion it engenders among both practicing physicists and scientifically-interested laymen.

Mathematical physicist [John Baez](https://math.ucr.edu/home/baez/) attempts to answer the question in his appropriately-titled pamphlet ["What is Entropy?"](https://math.ucr.edu/home/baez/what_is_entropy.pdf) According to Baez, entropy is missing *information*. The entropy of a system is the amount of information that you don't know right now, but could learn in theory (by performing experiments, for example).

This definition of entropy seems alright, but it's only words. What is the precise *mathematical* definition of entropy? Restricting ourselves to finite-state systems for simplicity, the entropy of the system is

$$S = - \sum_{i \in X} p_i \log p_i$$

where $X$ is the set of states and $p_i$ is the probability that the system is in the $i$th state. 

(If you notice, I didn't specify the base of the logarithm. Information can be measured in different units depending on the base of the logarithm. For $\log_2$, information is measured in bits. For $\log_e$, information is measured in nats. For the remainder of this post, the implicit base of our logs will be base 2,and we will be measuring information in bits.)

It helps to consider a couple simple examples to get an intuition for how the entropy works. The multiplicity of a system is the number of possible states that the system can be in. For a system with $N$ different states, all of them equally probable, the entropy of the system is 

$$
\begin{align}
S &= - \sum_{i \in X} \frac{1}{N} \log \frac{1}{N} \\
&= \log N
\end{align}
$$

So if I have a system with $N$ possible states, and I tell you its precise state, you gain $\log N$ bits of information. Why does entropy scale with the logarithm of the multiplicity? Because the logarithm is the unique function with the properties:

1. The entropy is monotonic with respect to the number of different possible outcomes.
2. The entropy is additive for independent systems.

To further motivate the second property: consider the case of $N$ coin flips. Before I perform the $N$ coin flips, there are $2^N$ possible sequences, so the entropy is $N$ bits. But notice that for a single coin flip, the entropy is $1$ bit, as there are only two possibilities. The entropy of $N$ independent coin flips is just $N$ times the entropy of a single coin flip, which is exactly what the logarithm gives us: $\log(2^N) = N \log(2) = N$ bits.

You might notice that this definition of entropy isn't the type of *physical* definition of the entropy that one would find in a thermodynamics class (e.g. in terms of Carnot heat engines). This is an intentional choice. Baez notes that entropy was first defined in thermodynamics and only later generalized by Shannon in information theory. However, Baez consciously decides to develop the concept of entropy in the exact opposite direction of its historical development. He first gives a brief overview of probability theory. Then he talks about entropy as information, using the common motivating example of coinflips. Only at the end does he show that the thermodynamic entropy (which he calls the Gibbs entropy) is a special case of the more generally applicable Shannon entropy, extended to sets of uncountable cardinality.

The book is structured around a simple question: why does hydrogen gas at standard temperature and pressure have 23 bits of entropy per molecule? While the question is simple, answering it satisfactorally requires covering probability theory, information theory, measure theory, statistical mechanics, and even an itty-bitty amount of quantum mechanics. While this book is conversational, heavier on words than equations, it's decidedly *not* a popular science book. To give an example: the basics of measure theory--how the measurable subsets form a sigma algebra and the countable subadditivity property of measures--are breezily covered over the course of a couple of pages. This book assumes a level of mathematical maturity commensurate with an undergraduate degree in a STEM field.

"What is Entropy?" can be best-appreciated if you've already taken a more standard course in thermodynamics and statistical mechanics. Baez is maximum-entropy-pilled: When the book transitions from information theory to statistical mechanics, he uses the maximum entropy formulation of E.T. Jaynes to motivate the Boltzmann distribution. In fact, it's only at the very end of the book does he derive the much-exalted Laws of Thermodynamics as special cases of the maximum entropy principle, while more traditional presentations of thermodynamics take the laws to be axiomatic.

Despite leaning heavily on the maximum entropy principle, Baez sidesteps all of the Bayesian-versus-frequentist quarelling that Jaynes was famous for engaging in. In an amusing aside, Baez describes Jaynes' book *Probability Theory* as "opinionated". In context, it's clear he meant it as a compliment, but it still cracked me up.

Is it a problem that Baez grounds the concept of entropy in probability theory, but then makes no attempt to answer the question of what probability "really" is? If we were attempting to be completely philosophically rigorous, then probably. But I interpret Baez's aims as being more modest. He just wanted to show why the word "entropy" is used for what appears to be many different and only loosely related concepts. I agree with Baez that the philosophical question of probability is too big and contentious to answer satisfactorily in a brief digression.

So does Baez succeed in explaining what entropy is? In my opinion, he does! I would say that this work is the best attempt at answering the question that I've encountered.

But is there anything missing? At the beginning, Baez listed out five different notions of entropy.

1. Entropy in thermodynamics
2. Entropy in classical statistical mechanics
3. Entropy in quantum statistical mechanics
4. Entropy in information theory
5. Algorithmic entropy

Baez spends ample time on thermodynamics, classical statistical mechanics, and information theory. But quantum statistical mechanics and algorithmic entropy are not covered. I know embarrasingly little about quantum statistical mechanics, so I can't comment on the appropriateness of its absense. But I would have liked to see a spirited attempt at incorporating the algorithmic complexity formulation of entropy. I have these floating associations in my head between terms like 'machine learning', 'lossy compression', 'inductive biases', and 'Kolmogorov complexity'--but my understanding is incomplete and dilettantish. As someone on the lookout for how statistical physics could shed light on problems in machine learning, it would have been nice to read Baez's perspective. Nevertheless, I can understand why he opted not to cover algorithmic complexity. The book was structured around understanding the entropy of the ideal gas, so he would have had to be really creative to keep the same structure while still making algorithmic complexity seem natural and not shoe-horned in.