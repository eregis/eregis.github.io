---
layout: post
title: "Simulations Are Just Experiments"
date: 2024-08-20
mathjax: true
keywords: simulations, experiments, theoretical physics, scientific method, computational modeling, research methodology
description: Explore the parallels between simulations and experiments in scientific research. Learn how simulations serve as computational experiments, offering insights into complex systems and aiding in the discovery of new knowledge in theoretical physics and beyond.
---

My research interests lean theoretical. Whether it's mathematics qua mathematics (probability theory) or creating abstract, information-theoretic models of organisms, I like calculations and symbol-manipulation. A year into my PhD, I find that the parts of the research process that I'm most comfortable with are reading papers and self-teaching myself new math. Which isn't too surprising: After twenty years in school, I've had a lot of practice with absorbing large amounts of information quickly. But a PhD isn't about learning what's already well-understood, but creating *new* knowledge. How does one discover a fact about the world that no else has discovered?
 
An important part of doing theoretical work as a working physicist is to be adept at setting up and analyzing simulations. And I've *struggled* with that part of my PhD so far. My attitude towards simulations has been a bit like a seven year old pinching his nose and eating his veggies. *Fine*, I'll code up this simulation (so that I can get back to the fun stuff).

(To my knowledge, my advisor doesn't read this blog. But just in case: Hi Thierry!)

But I've recently come to a pretty obvious epiphany that I think will mark a turning point in my attitude towards simulations: Simulations are just experiments. While normal experiments happen in the physical world, simulations happen in a simplified, computational world as defined by some model.

One of the reasons we need experiments is that there is an irreducible complexity to the real world. This complexity relates to the limitations of [reductionism](https://en.wikipedia.org/wiki/Reductionism)—the philosophical idea that high-level phenomena can be 'reduced' to low-level phenomena (e.g., the notion that humans are 'just' arrangements of atoms).

Even though our best model of how the world works is the [Standard Model Lagrangian](https://en.wikipedia.org/wiki/Mathematical_formulation_of_the_Standard_Model), to predict any actual real-world phenomena, we must use effective theories appropriate for the physical scale of the phenomena in question. For example, when modeling chemical systems, we use reaction rate equations. Similarly, when modeling economic consumers and producers, we use supply-and-demand models.

There is a sense in which reaction rates and supply-and-demand are emergent phenomena implicitly encoded somewhere in the Standard Model Lagrangian. However, it's often more practical and effective to use these "approximations" rather than attempting to derive everything from fundamental physics.

This principle is not unique to the Standard Model Lagrangian, but is quite general. There is an inherent complexity to all models such that we can't deduce all of their consequences even given a precise formulation. A simulation is a tool to quickly probe some high-level, downstream consequences of a model without having to work through a lot of messy and possibly intractable calculations.

There is a tradeoff between performing a 'real' experiment versus creating a simulation. Experiments physically embodied in the real world have the advantage of capturing extensive real-world detail, but they are often expensive and the fidelity of the data can be incredibly challenging to maintain. With simulations, we work in a simplified world, but we can ask any question we like about that world.

How does one choose between performing an experiment versus creating a simulation? Here's a quick schematic of how I envision this decision process:

Let's say a scientific question has grabbed my attention. First, I imagine the *ideal* experiment. For this ideal experiment, I don't worry about any time, resource, or cost constraints. The ideal experiment would be one that, if performed, would definitively resolve the scientific question to the satisfaction of all interested parties. No more debate.

Then, I slowly pare down the resources required, starting with parts that have the worst informativeness-to-cost ratio. At each step, I ask myself:

1. Is there a publicly available dataset that can answer this question?
2. Would it be feasible for me to perform an experiment to answer this question?
3. Would it be feasible for me to perform a simulation to answer this question?

Every experiment is the ideal experiment for some question—but that question is often far more specific than the broader inquiry we're actually interested in. What I need to ask is whether there is sufficient overlap between the narrow question that the experiment precisely answers and the broader question I actually care about.

Consider an experiment where we drop a feather and a bowling ball from a window to see which lands first. This experiment technically answers a very specific question: 'If we drop a green bowling ball and a bald eagle feather from the third-floor window of this particular building, facing north, on a Tuesday in March, with a temperature of 68°F and 45% humidity, which will land first?' However, our actual interest likely lies in the much broader question of how objects with different masses fall under the influence of gravity.

The challenge lies in determining which details are crucial to our broader inquiry and which are extraneous. Does the color of the bowling ball matter? Probably not. Does the air resistance affecting the feather matter? Almost certainly.

With simulations, we face a similar challenge. We must consider whether the real-world details we're omitting from our model are likely to significantly impact the answer to our broader question. If we're simulating the falling objects, do we need to account for wind resistance? The Earth's rotation? The curvature of the Earth's surface?

The art of experimentation—whether physical or simulated—lies in striking the right balance between the specific conditions we can control or model and the general principles we hope to uncover. It's about recognizing which details are essential and which can be safely ignored without compromising the broader applicability of our results.

This perspective suggests a way that I can be a better scientist in the future. When going to code up a simulation, I should approach it with the same rigor and care that an experimentalist uses when creating their experiments. It's about being motivated by a question and then using the tools at your disposal to attempt to answer it.