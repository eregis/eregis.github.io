---
layout: post
title: "Thinking Fast and Slow Time Scales"
date: 2024-08-02
mathjax: true
---

I didn't get much out my two semesters of Quantum Field Theory. But one idea that managed to make an impression on me is the idea of "effective theories". The idea is that different models of reality might be applicable at different "scales" wasn't invented by quantum field theorists--at least I don't think. It seems like a fairly old idea. But by way of the renormalization group, this idea of how our physics changes as a function of scale is made sophisticated and mathematical, rather than simply philosophical.

We sometimes represent Markov processes by directed graphs, where each node reprents a different state and each weighted directed edge represents a reaction.

Then when you represent a system by a graph, if $k$ is the reaction rates

Given a distribution of time scales in a problem, there is sometimes a natural seperation of time scales. Given a collection of time scales, the fastest relevant time scale is given by $\frac{1}{\sum_{i=1}^N k_i}$. This time scale represents, loosely, how long until the next transition happens (in jump processes, this is precise; with continuous Markov processes, this intuition is more heuristic.)

The slowest time scale would be $\sum \frac{1}{k_i}$. The physical interpretation of this would be if (for some reason), the equilibriation process needs to happen one step at a time. This seems more rare/contrived and as opposed to the fast time scale limit; most commonly, the slowest relevant time scale is $\max\{k_i\}$.

The lower time scale cutoff means that processes that happen faster than this equilibriate. This 

This is intuitive, and relates to what we consider a state. What we consider a state in our model is actually a composite of many different physically-distinct states, where the node represents the equilibrium ensemble over the fast dynamics.

So what would be relevant here is the overall time scale of switching: