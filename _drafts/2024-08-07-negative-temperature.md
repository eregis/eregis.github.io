---
layout: post
title: "Negative Temperature"
date: 2024-08-07
mathjax: true
---

I was already familiar with most of the topics that were covered in this book, but there were two topics that were clarified for me: negative temperature and the Hagedorn temperature. Negative temperature was briefly covered in my undergrad thermodynamics class. (I believe we were assigned a homework problem on the classic problem of entropy and gravitational systems.) I had this vague intuition that negative temperature systems are systems which gain entropy when they lose energy (as opposed to the usual relationship where systems gain entropy when they gain energy), but I didn't feel too secure in my understanding. 

Baez cleared things up quite nicely by pointing out that thermodynamic beta is a more natural quantity than the temperature. Thermodynamic beta is the the recipricoal of the temperature: $\beta = \frac{1}{kT}$. You can think of $beta$ as the "price" at which system is willing to sell its energy. At high $beta$ (low temperature), the system is reluctant to give away its energy. As $\beta$ gets closer to 0 from the right, the system is more and more willing to 

Basically, with temperature, the topology of thermally-equilbriates systems is two open intervals $(-\infty, 0)$ and $(0, \infty)$, compactified such that $\pm \infty$ are connected. If you notice, $0$ is not an accessible temperature. And importantly, the limit of approaching $0$ from the left and from the right do *not* converge on the same system. Both limits approaching $0$ are minimal entropy configurations, but they are different minimal entropy configurations. When approaching $0$ from the right, all the probability concentrates in the lowest energy state (the ground state). When approaching $0$ from the left, all of the probability concentrates in the highest energy state.

A negative temperature system is simply one which is in thermodynamic equilibrium, and the higher energy states are more probable than the lower energy states. 

With thermodynamic beta