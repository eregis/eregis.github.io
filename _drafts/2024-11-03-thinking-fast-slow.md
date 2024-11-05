---
layout: post
title: "Thinking, Fast and Slow Time Scales"
date: 2024-08-02
mathjax: true
---

I didn't get much out my two semesters of quantum field theory. But one idea that managed to make an impression on me is the idea of "effective theories". An effective theory is basically a model that captures the important physics at a particular scale while ignoring details that don't matter at that scale---like how you can describe water flow without keeping track of individual molecules. This idea that different models of reality might be applicable at different "scales" wasn't invented by quantum field theorists--at least I don't think. It seems like a fairly old idea. But by way of the renormalization group, which tells us mathematically how physical interactions change with energy scale, this idea of how our physics changes as a function of scale is made precise, rather than simply remaining a philosophical idea.

I think a baby version of this idea can help us understand finite-state Markov processes. In many systems inWe sometimes represent Markov processes by directed graphs, where each node reprents a different state and each weighted directed edge represents a "reaction" or transition rate.

[Picture of some Graph representing a Markov process]

The weight of the directed edge tells you the strength of the reaction: the faster the reaction is to occure.

Then when you represent a system by a graph, if $k$ is the reaction rates

Given a distribution of time scales in a problem, there is sometimes a natural seperation of time scales. Given a collection of time scales, the fastest relevant time scale is given by $\frac{1}{\sum_{i=1}^N k_i}$. This time scale represents, loosely, how long until the next transition happens (in jump processes, this is precise; with continuous Markov processes, this intuition is more heuristic.) This time scale is *really* important, both in terms of conceptually understanding your model of the system and when you have to do the technical work of actually implementing the model in a simulation.

The slowest time scale would be $\sum \frac{1}{k_i}$. The physical interpretation of this would be if (for some reason), the equilibriation process needs to happen one step at a time. This seems more rare/contrived and as opposed to the fast time scale limit; most commonly, the slowest relevant time scale is $\max\{k_i\}$.

The lower time scale cutoff means that processes that happen faster than this equilibriate. This 

This is intuitive, and relates to what we consider a state. What we consider a state in our model is actually a composite of many different physically-distinct states, where the node represents the equilibrium ensemble over the fast dynamics.

So what would be relevant here is the overall time scale of switching: