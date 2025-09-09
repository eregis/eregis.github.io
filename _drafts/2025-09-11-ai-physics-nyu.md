---
layout: post
title: "AI + Physics Workship at CUNY"
date: 2025-09-08
mathjax: true
---

A couple of weeks ago, Sinho told me there would be an AI + Physics workshop, hosted by the CUNY Graduate Center.
The timing was fortunate. While I've been interested in intersections between AI and physics for the past year,
I've yet to attend a conference on the subject. Attending this conference would give me exposure to other people's
research programs.

# Day 1

The Cuny Graduate Center is located in Midtown Manhattan. While the CUNY system (the public university system for New York City) is old, the Graduate Center itself is quite sleek and modern. The conference was hosted in a small room on the fourth floor of the conference.

The conference was set to last for three days. Each day was split into a morning and and an afternoon section, with talks roughly grouped based on similarity of topics.

Monday morning was focused on physical learning. The first two speakers were Andrea Liu and Marcelo Guzman both from UPenn. Neural networks are used on computers, but there is a vibrant research
program interested in learning in non-silicon based substrates. A motivation for it's research program is the brain: like neural networks, the brain takes training data to learn over time. But there are many important differences between brains and neural networks.

* Energy expenditure. Brains are very efficient, using on the order of picoJoules per computation, while neural networks
are on the order of kJs per computation.

* Learning algorithm. Neural networks are mostly based on feedforward networks where there is one-directional information flow
during inference. The brain is highly recurrent, where two-way connections are the norm.

*Learning algorithm. Neural networks learn using gradient descent and use backpropogation. Brains use local rules to update
their state over time for learning (a canonical example is "neurons who fire together, wire together" while simplistic, it
points to in important principle that neurons update over time in a local fashion.)

* Memory. Neural networks have to be clever about memory allocation, and be careful about pulling and pushing things towards memory. While for brains, we have that inference and learning happens in parallel to memory.

The brain is quite complicated, so what these researchers actually studied is a toy model of resistors circuits.

In a resistor circuit, the input corresponds to the voltage at some pre-desginated node and the output corresponds to the mesaured voltage at some pre-designated output note. The function is computed by the law of physics: given an input voltage at the input node, the voltages at the other nodes in the network will adjust such that the power being expanded by the system is minimized. (This is equivalent to satisfying Kirchoff's law: that each node the currents in equals the currents out. Another way to think about all this is that power minimization, Kirchoff's law, and the steady state all must be acheived.)

The "parameters" of the physical network are the conductances of the resistors connecting the network. The way learning works is that given the current conductances of the network you look at the voltage values of the network.

In the afternoon, there was a more ecletic mixture of talks: including on diffusion models and learning quantum ground states from measurements. I really enjoyed Cengiz Pehlevan's talk on scaling laws. His talk was twice as long as the other speakers and fittingly his talk could be neatly divided into two parts: a history on the empirical evidence of scaling laws in large language models, and a second half where he talked about theoretical work concerned with explaining the origin of scaling laws under various model assumptions.

I was pleasantly surprised to see his overview of the empirics of the scaling law were mostly familiar with me. There were interesting details though that were new to me. One concerned a conflict between to blockbuster papers in the scaling law literature: Kaplan's 2020 paper and the Chinchilla scaling law paper. Kaplan derived that the scaling the compute was actually more important the data (I guess an analogy would be that having a bigger brain is more important than getting more practice.) But Chinchilla, released only two years later, got different results. Which was correct?

The answer was that, both were correct in the domains that they were applicable, but practically speaking the Chinchilla scaling laws was correct. 

# Day 2

