---
layout: post
title: "Post Template"
date: 2024-06-13
mathjax: true
---
Is this the basic idea of phase transitions made simple:

Given the intrinsic thermodynamic variables, some configurations (phases) will be more probabilistic. If you imagine a Boltzmann distribution (perhaps as a function of temperature of something), that will look like a sigmoid with discrimination factor N\beta. But in the thermodynamic limit (system size goes to infinity; intrinsic variable held constant); that discrimination goes to infinity, so you have what was continuous for finite systems become a step function; and thus as a function of e.g temperature, there is a discontuinity in the arrangement (phase) of the system.

Is that right?

I guess my perspective I am taking is rather than taking a boltzman distribution over microstates, you take a simplified two-state boltzman distribution over macrostates corresponding to a grouping of microstates. So instead of the energy of the microstates, we would use the free energy of the macrostate

(This is actually the most general way to think about the Boltzmann distribution; the special case where we are assigning boltzmann factors to microstates correspond to when the multiplicity of each microstates equals 1, thus the entropy equals 0, thus the energy equals the free energy.)