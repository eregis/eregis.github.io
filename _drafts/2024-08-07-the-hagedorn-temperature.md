---
layout: post
title: "The Hagedorn temperature"
date: 2024-08-07
mathjax: true
---

The partition function is the most powerful object in all of statistical mechanics. If you have the partition function as a function of thermodynamics, then every other thermodynamic quantity can be derived from it.

Which is why it's funny in that in a more banal sense, all the partitition function is a normalization constant. Most students first encounter the partition function in the context of the Boltzmann distribution. We show that the probabiliy of a state with energy $E_n$ has to proportional to its Boltzmann factor $e^{-\beta E_n}$. But to get the probability of a given state, we need a normalization constant which is the sum over all Boltzmann factor

$$Z = \sum e^{-\beta E_n}$$

And this object is the partition function. As the partition function is "just" a normalization constant, one can ask: are there systems where the partition function fails to be finite--or in other words, the probability distribution fails to be defined?

Sure, consider the example, where you have countably infinite number of states indexed by $n \in \mathbb{N}$ all with the same energy. Then for any $\beta$, all states will have the same Boltzmann factor equal to the same constant

$$
Z &= \sum_n e^{-\beta E_n} \\
&= \sum_n c
&= \infty\\
$$

This example make sense, but is kind of boring. More interestingly, are there systems where the partition function is defined for some temperatures, but not all temperatures?

Yes, it depends on how quickly the spectrum of energies grow with respect to $n$. If the spectrum of energy grows sufficiently quickly (which most physical systems we consider will satisfy), then the system's partition function will be well-defined for all temperatures. But if the energy spectra grows sufficiently slowly, then the system can be well-defined below some thresholds of temperature $T_H$ (or equivalently, above some thresholds of thermodynamic beta $\beta_H$).

It's called the Hagedorn temperature because a system satisfying this propery was first proposed by Hagedorn to resolve a mystery in nuclear physics (though he didn't answer the question that he was attempting to answer, he still provided a fun toy model for physicists to play with).

What sort of system would satisfy this? Let's try a linear system where $E_n = E n$ where $E > 0$(this would be energy spectra of a harmonic osccialtor, for example).

Then we have that

$$
\begin{align}
Z &= \sum_n e^{-E n} \\
&= \sum_n c^n \\
&= \frac{1}{1-c}\\
\end{align}
$$

So a linear energy spectra gets mapped to a geometric series--which converges.

Let's try and work backwards then: start with a series we know that diverges, and then figure out what sort of energy spectra results in that series. The harmonic series is the "least" diverges series in some sense. If you consider series of the form

$$\sum_n \frac{1}{n^p}$$

which are called $p-series$. For $p > 1$, the $p$-series converges. But for $p \le 1$, the p-series diverges. The special case when $p=1$ is called the harmonic series.

$$\sum_n \frac{1}{n}$$

So we want the energy spectra $E(n) = E_n$ to map to Boltzmann factors that follow a harmonic series. Matching the $n$ term in the harmonic series to the $n$th term in the sum over Boltzmann factors.

$$\frac{1}{n} = e^{-\beta E_n} \longrightarrow \frac{1}{\beta} \log n$$

So an energy spectra that grows as

So that is the threshold temperature

What's interesting about the Hagedorn temperature is that it's a nice clear example of physics as computation. Every thermodynamic system, via its partition function, is implicitely computing some complicated series/integral. Though often times to make sense of this, we would need the thermodynamic paramaters (e.g thermodynamic beta) to be extended to be complex-valued--which probably isn't always physically realizable.