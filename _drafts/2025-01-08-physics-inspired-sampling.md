---
layout: post
title: "The Unreasonable Effectiveness of Physics in Sampling"
date: 2024-01-09
mathjax: true
---

When I have to tell people what I work on, the phrase that I've settled on is "physics-inspired sampling". 
It does a good job conveying the gestalt situation: I'm a Physics PhD student who is now working in statistics
and machine learning.

But a lot of people are (understandably) confused about why a Physics PhD student would be working in statistics. 
"Statistics? Like what sports fans use to win arguments on the Internet? What does that have to do with physics?" 
It's a decent question: what *does* statistics have to do with quantum mechanics? Or gravity? 
People with STEM backgrounds *might* be aware of some applications 
of statistical physics in machine learning---maybe not in detail, but in a vague 
"my freshmate roommate from undergrad who now works at Google does stuff like that" kind of way.

But it turns out that the connection between sampling and physics is quite old. Dating back to the middle of the
20th century, many sampling algorithms were either outright invented by physicists or invented to help solve
some physical problem.

* The Monte Carlo method was invented by the physicist Stanislaw Ulam (in collarobaration with John von Neumann)
during the Manhattan project. It was developed to aid with the required
nuclear physics calculations.

* The Metropolis algorithm was *also* invented at Los Alamos by a group of physicists 
(including Edward Teller, inventor of the hydrogren bomb) shortly after World War II.

* Hamilton Monte Carlo was invented by a team of 
physicists to help with lattice quantum chromodynamics calculations.


When I say "physics-inspired sampling", there are two senses in which I mean it. 
There is the more straightforward sense in which I mean "sampling techniques which use mathematics from physics." 
But there is a stronger sense in which it has something to do with how sampling becomes embodied in 
physical reality---and how the distributions that manifest in reality can be hints for how we design algorithms.

#Ergodicity

A big unifying idea behind physics-inspired sampling is ergodicity: it says that if you follow the trajectory of a
microstate ensemble over time, its distribution of microstates will be equal to the ensemble. 
This might seem trivial, but a lot of systems don't exhibit this property. 
For example, consider if you are interested in sampling from a distribution over time. 
What wouldn't work is taking one person and following them around recording their height 
every morning to get an idea of the distribution of adult heights.

Ergodicity helps explain Markov chain Monte Carlo and why that works. 
But an important part is that ergodicity says something about how the asymptotic distribution of states 
approaches the ensemble. There is a stronger condition that many sampling algorithms 
have where if you wait long enough, the marginal distribution at a given time slice is equivalent.

The physics here comes from the fact that in physical systems, 
we often lose information over time due to randomness. Ergodicity gets broken when you have deterministic dynamics.
 A way to think about it is that if you have a deterministic system, then along trajectories you will have the same value for any conserved quantity. This would correspond to something like the microcanonical ensemble in statistical mechanics.

But in practice, just like the role of temperature where connecting to the heat bath allows random influxes of heat, we want randomness such that even if we are centered around some mean value of energy, we can explore nearby energy hypersurfaces.

Consider a procedure where you have a system connected to a temperature bath. Then disconnect it from the temperature bath and then sample the closed system repeatedly. That would violate ergodicity with respect to the initial bath-connected distribution (even though each initial measurement would be distributed according to the ensemble).

#Metropolis Algorithm

There are two main innovations of Metropolis algorithm. One is that probability distributions can be conceived
as Boltzmann disttribution. Boltzmann distributions are statistical distributions from physics.

The way Boltzmann distributions work is that what wants to be maximized is the entropy of the whole universe.

The entropy of the universe can be decomposed. In general we have that S = \log \Omega. But how do we go
about counting the microstates of the universe as a whole?

Is that while it would be difficult to know the multiplicity of the . The ratio of the probability of two
states is based on the delta in the entropy e^{S}. This is 

The other physical innovation of the Metropolis-Hastings algorithm is that of detailed balance. Detailed balance
is the property that the system's traversing the reverse microstates is just as likely as visiting. 

To understand detailed balance, consider the following triangle graphs.

In the first graph, at every time step. In this graph, if I give you a sequence of states, you can perfecly
distinguish between backwards and forwards trajectories. In the second graph.

But what's interesting is that the long-run statistics of each
The Metropolis algorithm was actually the original physics-inspired sampling algorithm, invented by a team of physicists. It relies on a Markov chain that we can follow like a "particle" to yield access to a distribution. But here we also rely on a new physical intuition: detailed balance. Detailed balance says that given any sequence, the reversed sequence is equally probable.

The way Metropolis algorithm works is that you have a proposal function Q(x,y); this will be some simple function like a Gaussian. You also have access to the potential V. It helps to think of it this way: given a proposal, if the proposal would take you from a region of lower probability to higher probability (equivalently from higher potential to lower potential), then you always accept the proposal. But if the proposal would take you from higher probability to lower probability, then you reject the proposal with a probability that is proportional to the gap in probability: the more the proposal has you go "uphill" the more likely to reject.

The rejection probability is chosen such that high-to-low sequences are as frequent as low-to-high.

#Langevin Monte Carlo

If you look at a free-floating particle suspended in a liquid, it will jitter--moving in a herky-jerky fashion. This was famously discovered by Einstein as Brownian motion. We can describe this by a stochastic differential equation.

Because the particle is small, it has what we call Low Reynolds number. That means that the particle's inertia is small; so the net force is always equal. Because of that, its velocity is always such that the forces balance. That means, while Newton's is a second-order equation, we can actually express the dynamics as a first-order equation in terms of the first time derivative of the position on one side and the forces on the other side.

One of the key insights is that if we set up the Langevin equation we have two terms: a drag force term proportional to negative the velocity and then Brownian noise. But we know that for a particle at thermodynamic equilibrium, its velocity in any given direction must be a Gaussian. In stochastic processes, this is called an Ornstein-Uhlenbeck process.

We can actually generalize this form to sample from an arbitrary distribution of the form e^(-V). A way to think about it is that while the drag force is not due to a potential as we understand it in physics, we can analogize it to being the force generated by some hypothetical force generated by a potential \frac{1}{2}v^2 where the "gradient" would be with respect to the velocity. Using this formulation, we have that our equation becomes:

-nabla_v \frac{1}{2} v^2 + dW_t

If we write it like this we see that the term being taken by the gradient is precisely what appears in the steady-state distribution in the exponential.

We can then reason: if we change the form of the drift then we can change the steady-state distribution which our process approaches. This allows us to sample from any distribution we desire as long as we have access to the gradient of the potential. We just (a) discretize the time step and (b) run the algorithm until the marginal distribution matches the steady-state distribution (c) use that value as our sampled value.

This feels physics-inspired both in that it has deep ties to a bit of history in statistical mechanics (Langevin equation), but also that it feels embodied. You can imagine carrying out this sampling algorithm in the real world. You watch the particle and then you record the speed and you get a Gaussian distribution.

Yes, this is analogous to "generalized forces" that students often cover briefly in classical mechanics during a lecture or a textbook, but isn't covered in-depth (e.g., rarely will it be assigned as a homework problem).

#Diffusion Models

The most recent example I want to cover is diffusion models, which were discovered by a team of Stanford physicists and incorporate principles from non-equilibrium statistical mechanics.

The way a diffusion model works is that you learn a neural network that learns how to take Gaussian noise and turn it into an image; this is learning a deblurrer. During training, you give it an image and it gradually adds noise to the image until the image is completely blurred--random white pixel noise. It's then the decoder's job to try and predict what the noise was at the previous time step given the current blurred image.

The reason why diffusion models work so well is that they allow different parts of deblurring to learn different levels of the image. The last layers "chronologically" will try to turn the random image into high-level features. And then each subsequent layer will try and denoise by adding more and more fine-grained details until finally you have an image that should be from the same distribution as the distribution of natural images.

Though as I type this explanation, the connection to non-equilibrium statistical mechanics is a bit obscure to me. What's clear is that the physical intuition of noise and diffusion processes has led to one of the most powerful tools in modern machine learning, showing how physics continues to inspire new approaches to sampling and generative modeling.