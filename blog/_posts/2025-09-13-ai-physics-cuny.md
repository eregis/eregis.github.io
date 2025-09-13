---
layout: post
title: "AI + Physics Workshop at CUNY"
date: 2025-09-13
mathjax: true
---

A couple of weeks ago, Sinho told me about an upcoming [AI + Physics workshop hosted by the CUNY Graduate Center](https://www.gc.cuny.edu/events/ai-physics-workshop). The timing was fortunate. While I've been interested in topics at the intersection of AI and physics for the past year, I had yet to attend a conference on the subject. Attending this workshop would give me exposure to other researchers' work in the area.

# Day 1

The CUNY Graduate Center is located in Midtown Manhattan. While the CUNY system (the public university system for New York City) is old, the Graduate Center itself is quite sleek and modern. The conference was hosted in a small room on the fourth floor of the building.

The conference was set to last for three days (though I personally could only attend the first two days of the conference). Each day was split into morning and afternoon sections, with talks roughly grouped by topic similarity (though this was amended slightly to accommodate the travel needs of featured speakers).

![Workshop Schedule](\assets\ai-physics-cuny\workshop-schedule.png)

Monday morning focused on physical learning. Neural networks typically run on computers, but there is a vibrant research program interested in learning on non-silicon-based substrates. A key motivation for this research program is the brain: like neural networks, the brain uses training data to learn over time. However, there are many important differences between brains and artificial neural networks.

| Aspect | Brain | Neural Networks |
|--------|-------|-----------------|
| **Energy expenditure** | Very efficient, using on the order of picojoules per operation ($10^{-13}$ to $10^{-18}$ J)  | Much less efficient, typically consuming millijoules per operation ($10^{-3}$ J) on GPUs  |
| **Learning algorithm (Architecture)** | Highly recurrent, where two-way connections are the norm | Mostly based on feedforward networks where there is one-directional information flow during inference |
| **Learning algorithm (Update method)** | Use local rules to update state over time for learning (a canonical example is "neurons who fire together, wire together")| Learn using backpropagation |
| **Memory** | Inference and learning happens in parallel to memory | Have to be clever about memory allocation, and be careful about pulling and pushing things to/from memory |

Unfortunately, the brain is quite complicated, so what these researchers actually studied is a toy model of resistor circuits.

In a resistor circuit, the input corresponds to the voltage at some pre-designated input node and the output corresponds to the measured voltage at some pre-designated output node. The function is computed by the laws of physics: given an input voltage at the input node, the voltages at the other nodes in the network will adjust such that the power being expended by the system is minimized. (This is equivalent to satisfying Kirchoff's law: that at each node, the current flowing in equals the current flowing out.)

![Resistor Circuit](\assets\ai-physics-cuny\resistor-circuit.png)

The "parameters" of the physical network are the conductances of the resistors connecting the network. The way learning works is that given the current conductances of the network, you look at the voltage values of the network and compare them to the voltage values when you fix the output node at the desired target voltage. You then nudge the conductances of the network such that the voltage of the output node is closer to the target.

In the afternoon, there was a more eclectic mixture of talks: including on diffusion models and learning quantum ground states from measurements. I really enjoyed Cengiz Pehlevan's talk on scaling laws. Scaling laws concern how the performance of a neural network scales as you increase the size of the training data set (data), increase the number of model parameters (parameters), or increase the total computational resources spent during training (compute). What's been found is that these scaling laws are (a) power-laws when graphing the test loss against any of these varied quantities, and (b) robust across both different model architectures and across order-of-magnitude changes in the varied quantities.

![Kaplan 2020 scaling laws](\assets\ai-physics-cuny\Kaplan-2020.png)

*Figure from Kaplan 2020*

Pehlevan's talk was twice as long as the other speakers and fittingly his talk could be neatly divided into two parts: a history on the empirical evidence of scaling laws in large language models, and a second half where he talked about theoretical work concerned with explaining the origin of scaling laws.

I was pleasantly surprised to see that his overview of the empirics of scaling laws were mostly familiar with me. There were interesting details that were new to me though. One concerned a conflict between two blockbuster papers in the scaling law literature: Kaplan's 2020 paper and the Chinchilla scaling law paper.

Kaplan found that the optimal amount of compute given a network of parameter count $N$ and a data size of $D$ was $C = 6ND$. The key question was: given a limited compute budget, should you spend more compute on longer training (necessitating a larger data set) or on a model with more parameters (making each individual training step more expensive)? Under these settings, Kaplan found that $D \sim C^{0.27}$ while $P \sim C^{0.73}$. (Notice that, by necessity, the sum of the powers of the two relations equals one.) Kaplan's results suggested that scaling the parameter count was relatively more important than scaling the size of the data set---an analogy would be that having a bigger brain is more important than getting more practice.

But Chinchilla, released only two years later, got different results. Which was correct?

The answer was that both were correct in the domains that they were applicable, but practically speaking the Chinchilla scaling laws was correct. Kaplan's scaling laws are valid for smaller networks while Chincilla was more valid for larger networks and a more inclusive definition of "parameter".

# Day 2

![Tuesday schedule](\assets\ai-physics-cuny\tuesday-schedule.png)

Day 2 opened with Victor Galitski's talk. His work fell under the purview of "analyzing neural networks as spin glasses".

A spin glass is a lattice model where the coupling constants $\{J_{ij}\}$ are random variables (often Gaussian-distributed). In a normal Ising model, we take the coupling constants to be positive and uniform in space. This causes the ground state to be the one where all the spins are aligned (either spin-up or spin-down). In a spin glass, the picture is more complicated---much more complicated. Because the coupling constants can be both positive and negative, a lattice site will want to be aligned with some nearby spins and anti-aligned with other nearby spins. But with overwhelming probability, when you try to satisfy all these relationships simultaneously, you won't be able to. You will have to sacrifice some pairwise relationships in order to allow for energetically favorable bonds elsewhere in the lattice. This is called *frustration*: you can't satisfy all pairwise relationships simultaneously.

![Spin glass ground state](\assets\ai-physics-cuny\spin-glass-ground-state.png)

Spin glasses are a common theoretical tool used in computer science and statistics. Before I started learning statistics, I didn't know anything about them despite there being a landmark result in statistical physics---Giorgio Parisi won the Nobel Prize back in 2021 for his stunning results in solving the spin glass problem.

The relevance to neural networks is that we can make an analogy: the neurons in a neural network are like lattice sites in a spin glass, and the weights between neurons are like the coupling constants between spins. A common initialization scheme for neural networks is to draw the weights from a Gaussian distribution---exactly as the coupling constants are drawn in spin glass models. This correspondence suggests that tools from spin glass theory might help us understand the behavior of neural networks.

I also enjoyed Elliot Paquette's talk on theoretically motivating scaling laws. While scaling laws have been observed empirically, we still don't fully understand where they come from theoretically. Paquette's talk focused on connecting the power law covariance of the data to the scaling laws. I'll admit that I don't understand the connection he made (and I vaguely recall him saying that the talk was based on soon-to-be-published work---which makes sense since I can't find a promisingly-related title on his Google Scholar page). But I might as well use this as a good opportunity to speculate about how the distribution of feature importance might connect to scaling laws.

Consider the game of chess. Imagine that you are training a network to learn to evaluate which player is winning given a board position. The network will learn semantically meaningful features of the chess board. For example, the network will notice that the player with more pieces tends to win the game more often than not---so it will learn that as a relevant feature. Similarly, the network learns that the player with more "space" also tends to win more often, all else being equal. And so on and so forth. We have an intuition that some features are more important than others (e.g., total piece value is more important than knowing if the h-pawn is on the third rank or the fourth rank). But the question is: if you rank-order the features by importance, how important is the most important feature versus the tenth most important feature? Does the importance drop off extremely quickly (exponential distribution in importance of features) or does it drop off gradually (power law distribution in importance)? A power law distribution implies a long tail: there is always more to learn, small little heuristics that help you win 0.1% of the time.

There was also Jiequn Han's talk on score-based diffusion models with tilted transport. The way that a diffusion model works is that, during training, you give the diffusion model a noised version of an image and it learns to denoise it. Once the diffusion model has been trained, you can give it an image that's pure noise (one that wasn't derived from any real image) and it will produce a "denoised" image---effectively generating a new sample from the natural distribution of images.

The key mathematical framework is that the noising process---turning a natural image into random noise in pixel space---can be thought of as running a stochastic differential equation (SDE). To go from the noise distribution back to the data distribution, we need to run the corresponding "reverse SDE". It turns out that the reverse SDE has a very similar form to the forward SDE, except with an additional drift term. This extra drift term is proportional to the score function---the gradient of the log probability density---of the marginal distribution of the data at that point in time for the corresponding forward process. This is why diffusion models need to learn the score function: it tells them how to "undo" the noising process and recover natural images from noise.

But often times in diffusion models, you don't want a completely random image, but a random image of a specific object like a cat. Mathematically, that represents a desire not to sample from $p(x)$ (the natural distribution of images) but from $p(x\|y)$ (the distribution of cat images).

Traditionally, the way that sampling an image from a specific category is handled is that you modify the score gradients when running your reverse SDE so that it transforms the original Gaussian distribution into $p(x\|y)$ instead of $p(x)$. But what Han proposed is that you can actually keep the dynamics the same (as represented by the drift of your SDE), but change your *initial conditions*. Rather than having your initial latent space be a Gaussian, you instead "tilt" the distribution, so that after running the model with your original reverse SDE you end up with the desired conditional distribution.

This idea is pretty clever. I'd actually been exposed to this paper when I was originally learning about diffusion models, but the subtlety of the re-framing was lost on me since I wasn't familiar with the standard approach at the time.

![Bruna 2024](\assets\ai-physics-cuny\Bruna 2024.png)

*Figure from Bruna 2024*
