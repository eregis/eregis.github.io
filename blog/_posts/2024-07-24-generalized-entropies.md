---
layout: post
title: "Generalized Entropies"
date: 2024-07-24
mathjax: true
---

In a standard thermodynamics class, you learn about the [thermodynamic potentials](https://en.wikipedia.org/wiki/Thermodynamic_potential). The way that they are presented is as generalizations of the internal energy $$U$$ to different thermodynamic conditions. And this is corroborated by dimensional analysis: they all have units of energy.

This presentation is so misleading as to almost be wrong. The "thermodynamic potentials" should really be thought of as generalizations of *[entropy](https://en.wikipedia.org/wiki/Entropy)*, not the internal energy.

Consider the [Helmholtz free energy](https://en.wikipedia.org/wiki/Helmholtz_free_energy) $F$. We have that

$$F = - k_B T \ln Z$$

where $Z$ is the [partition function](https://en.wikipedia.org/wiki/Partition_function_(statistical_mechanics)). Let's define the Helmholtz *entropy* $\mathtt{F} = - \frac{F}{T}$. If you do that, we then have that

$$\mathtt{F} = k_B \ln Z$$

which is in direct analogy to our definition of entropy in terms of the [multiplicity](https://en.wikipedia.org/wiki/Multiplicity_(statistical_mechanics)).

$$S = k_B \ln \Omega$$.

This makes the analogy between the various thermodynamic ensembles much cleaner. The multiplicity gets mapped to the partition function and the entropy gets mapped to the generalized entropy. In the microcanonical ensemble, the probability is concentrated in macrostates that maximize the entropy. In the other ensembles, the probability is maximized in those that maximize the generalized entropy.

Why isn't the generalized entropies approach standard? As far as I can tell, it has to do with how thermodynamics was historically developed. The various thermodynamic potentials represent the amount of "useful work" that can be extracted from a system under various conditions. This approach makes a lot of sense in chemistry where we care about the potential barrier between different chemical states. But I would argue that in physics, especially undergrad-level physics where we don't spend any time on non-equilibrium phenomena, what we really care about is understanding how the macrostate relates to the equilibrium distribution of microstates.

The generalized entropies perspective is nothing new, of course. It's exactly how statistical mechanics is formulated by [E.T. Jaynes](https://journals.aps.org/pr/abstract/10.1103/PhysRev.106.620) in terms of *the maximum entropy principle*. While the maximum entropy principle isn't literally all of statistical mechanics, presentations in standard books [e.g., Schroeder] leave a lot to be desired by how they just gloss over it as if it's an interesting curiosity.