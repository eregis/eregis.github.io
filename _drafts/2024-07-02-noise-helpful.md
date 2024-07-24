---
layout: post
title: "Why do probability theorists go by their initials?"
date: 2024-06-13
mathjax: true
---

I am at the beginning of a new research project. Help me brainstorm. I want both general ideas and tips on how to brainstorm better, but also

Here is a braindump of where my head is at:

I am interested in the problem of noise in bacterial chemotaxis. In chemotaxis, bacteria represent the internal state of their system using the activity (concentration of CheYP); there is noise in this signalling pathway: the question is: when is the noise beneficial?

Why would we expect the noise to be beneficial? There are a couple high-level general arguments and then there are specific mechanisms as proposed by the literature.

Some high-level organisms: noise is inevitable. Any biochemical system will be on some level stochastic: whether it's receptor-ligated binding events or fluctuations between the equilibrium of enzymes in a feedback network. The only question remains: can fluctuations be limited (without causing problems elsewhere)? And, more provably: can we put those fluctuations to good use?

More on the question of limiting fluctuations: there is an intrinsic tradeoff between sensitivity and noise. This can be thought of from a statistical inference perspective: holding "discrimination ability" constant, there will be a tradeoff between false positives and false negatives. It can also be thought of physically from a fluctuation and dissipation point-of-view: The central insight of fluctuation-dissipation is that dynamical properties--the magnitude of the fluctuation and the  strength of the dissipation--are intimately connected due their mutual connection to the equilibrium distribution: the equilibrium distribution is precisely where the fluctuations and the dissipation balance in some sense. Often this can be written in a really general for <c(0) c(t)> = k_B T \eta: where, holding temperature constant we have that fluctuations and dissipation are proportional: perhaps even more instructively, we can write it interms of thermodynamic beta (where if temperature is a measure of a tendency towards disorder, than thermodynamic beta--the inverse temperature--we have that \beta = \eta/<c(0) c(t) >

These perspectives tend to view fluctuations as costs to be mitigated (there are also interesting non-equilibrium mechanisms to get a system's intrinstic fluctuation-dissipation tradeoff). But an interesting direction to explore is rather than viewing them as tradeoffs to be mitigated, can we view fluctuations as benefits?

This isn't without precendence. We often have "explore-exploit" dilemnas in e.g Machine learning where there is a tradeoff between choosing the locally optimal choice and choosing something that provides value down the line. Could noise be beneficial for exploring certain aspects of the space?

There is also the use of randomness in adversarial games, but I don't think that will be relevant to this problem since the gradient isn't an adversary that's trying to trick the bacteria.

These are interesting showerthoughts, but is there any relevant literature? Yes. One paper was written by Sneddon, an old student of PhD Advisor Thierry Emonet. Here, the central idea is that with long-time scale noise (long-time scale being on the order of ten seconds--hypothesized to be due to the methylation dynamics though I think that's less relevant), we have that noise actually helps climb the gradient. It does so by coordinating the motors: E Coli are believed to have four motors. If you model the switching dynamics with something that reasonably matches the experimental data, then you will have that, without long-time scale noise, the four motors are behaving sub-optimally. The rough idea is that for strong gradients, you want to be hypersensentive, so you want the four motors. For shallower gradients, you want to react less, as there is less signal-to-noise, so you want to extend runs in order to gather more information.