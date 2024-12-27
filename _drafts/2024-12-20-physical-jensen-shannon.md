---
layout: post
title: "A Physical Analogy for the Jensen-Shannon Divergence"
date: 2024-12-21
mathjax: true
---

The current professor that I am working with seemingly knows *everything* about sampling
despite being roughly the same age as me. That's why, on the rare occasions where I know something that he doesn't,
I'm always caught off-guard.

During our most recent weekly meeting, I was talking to him about what I had been up to in the past week. A good portion of my time had been spent chipping away at the six hundred pages of reading that he'd generously recommended to me in our previous meeting. But I'd also spent some time reading about non-equilibrium statistical mechanics. Non-equilibrium statistical mechanics is one of those subjects that I keep revisiting, but have never been able to *quite* conquer---either due to a lack of mathematical maturity or perhaps due to lacking some crucial bit of physical intuition.

A very helpful post-doc recommended this [review article by Christopher Jarzynski](https://terpconnect.umd.edu/~cjarzyns/CHEM-CHPH-PHYS_703_Spr_20/resources/Jarzynski_AnnuRevCondMattPhys_2_329_2011.pdf) that does a good job going over the basics. The article covers major fluctuation theorems (including Jarzynski's equality and Crooks fluctuation theorem) and discusses ways to quantify the irreversibility of a thermodynamic process. (You can think of processes as trajectories in space of thermodynamic coordinates.) One approach is to measure the work dissipated during a process. Another is to quantify how much the distribution of forward trajectories of microstates differs from the distribution of backward trajectories of microstates for the reversed process. (For an example of a non-equilibrium process, imagine moving a piston wall in a finite time. During compression, air bunches up against the wall. During decompression, the space near the moving wall becomes empty. This asymmetry is what we aim to quantify.)

I was explaining all this to the professor. And then I said, "One way to quantify the difference between the distribution of forward and backwards trajectories is the Jensen-Shannon divergence." And he was like, "What's that?"

As I've [mentioned before](c:\Users\ericf\critical-points\blog\_posts\2024-10-30-statistical-optimal-transport.md), there are two "problems" with the KL divergence as a probability metric.

1. If $p$ is not absolutely continuous with respect to $q$, then $\text{KL}(p\|\|q)$ is infinite.
2. The KL divergence is assymetric: $\text{KL}(p\|\\q) = \text{KL}(q\|\|p)$.

The Jenson-Shannon divergence is what I would consider to be the most obvious measure way to fix both of these problems. It's defined as

$$\text{JS}(p||q) = \frac{\text{KL}(p||m) + \text{KL}(q||m}}{2}$$

He then asked what physical context does it arise naturally--which is a decent question. I didn't have a good answer
on the spot, precisely because the Jensen-Shannon divergence probably wasn't physically-motivated.

The answer that I originally came up with was: image you have a cylinder and that they are partitioned into two parts.

Entropy is an extensive quantity about you can talk about the entropy per unit volume. Let's say we quantify that entropy per unit volume based on the distribution of speeds of the gas molecules in each $p$ and $q$. 

I felt pretty satisfied with this at the time, but on reflection, it's all wrong. Let's say that two distributions of gas molecules differ in their distribution of velocities because they are different temperature. Then when you lift the partition, the distribution of gas molecules would settle on the Maxwell-Boltzmann distribution corresponding to the averaged temperature--which is not the same thing as

[Visualization of the two distributions mi]

So here's my attempt to fix the score.
