---
layout: post
title: "Generalized Entropies"
date: 2024-04-30
mathjax: true
---

In a standard thermodynamics class, you learn about the thermodynamic potentials. The way that they are presented is as generalizations of the internal energy $$U$$ to different thermodynamic conditions. And this corroborrated by their units: they all have units of energy.

This presentation is so misleading as to almost wrong. The "thermodynamic potentials" should really be thought of as generalizations of *entropy*, not the internal energy. 

If you don't like that the units of the thermodynamic potentials are different than those of entropy, we can always divide by the temperature $$T$$. So instead of the Helholtz free energy $F$, we would have the Helmholtz entropy $$\mathtt{F} = - \frac{F}{T}$$ If you do that, notice what happens: we then have that

$$\mathtt{F} = k_B \ln Z$$

which is in direct analogy to our definition of entropy in terms of the multiplicity.

$$S = k_B \ln \Omega$$.

This makes the analogy between the various thermodynamic ensembles much cleaner and clear. The multiplicty
gets mapped to the partition function and the entropy gets mapped to the generalized entropy. In the microcanonical ensemble, probably is concentrated in macrostates that maximize the entropy while in other ensembles probability is maximized in those that maximize the generalized entropy.

This perspective is nothing new, of course. It's exactly how stastistical mechanics is formulated by E.T. Jaynes and others in terms of *the maximum entropy principle*. While the maximum entropy principle isn't literally all of statistical mechanics, presentations in standard books like (e.g Schroeder) leave a lot to be desired by how they just gloss over it as if it's an interesting curiosity.
