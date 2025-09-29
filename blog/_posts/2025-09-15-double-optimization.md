---
layout: post
title: "Double Optimization Problems"
date: 2025-09-15
mathjax: true
---

When I was at the AI + Physics workshop at CUNY, Marcelo Guzman's talk introduced an interesting conceptual framework: double optimization problems.

Guzman's talk was on physical learning: learning that doesn't happen on a computer (like with neural networks), but on some other substrate (in his case, he was studying resistor circuits). A motivating force behind the physical learning paradigm is that rather than having to rely on GPUs, we can have the laws of physics do some of the computation for us.

The idea behind "double optimization" is that physical learning can be divided into two separate optimization processes:

1. Given a current input voltage, the network itself (via the laws of physics) is performing an optimization problem over the voltages of the nodes such that the power is minimized across the network.

2. We, the controllers, shift the conductances of the network so that over time the physical network learns to embody the desired function that we want it to compute.

The important story here seemed to be two details: (1) that we get the first optimization "for free" and (2) there is a separation of time scales between the two optimization processes (equilibrating in response to external voltage happens on a much shorter time scale than adjusting the conductances to learn the target function).

![Physical Hessian](\assets\double-optimization\physical-Hessian.png)

*Figure from Guzman 2025*

The meat of Guzman's talk is that the optimization landscapes of the two optimization problems (as can be mathematically represented by their respective Hessians) are intimately related to each other.

I like the double-optimization framework because it seems quite general. I have recently been learning some reinforcement learning and it also features a double optimization problem.

In brief: Reinforcement learning is the study of how agents learn to maximize long-term rewards by way of short-term actions. Two fundamental objects in reinforcement learning are the policy (the function that dictates which actions the agent will take in any given state) and the value function (the function that says, given the agent's current behavioral policy, how good visiting a given state will be for the agent in the long run).

Where double optimization comes into play is how the agent learns to update its policy to become more optimal over time. In a class of reinforcement models called actor-critic models (these have a neural network tasked with learning the policy [the actor] and a separate neural network for learning the value function [the critic]), the idea is that given a current policy, you estimate the value function of that policy by having your agent act in accordance with the policy and observing what happens. You then update your policy so that actions that do better than expected for that state (called having a positive advantage) are performed more often, while actions that do worse than the average for that state (negative advantage) are performed less often. You then estimate the value function for your new policy, rinse and repeat, until (hopefully) your policy is globally optimal in the space of all possible policies.

![Big Picture RL](\assets\double-optimization\big-picture-RL.png)

*Figure from Sun 2024*

One of the difficulties is that the value function for a given policy is actually non-trivial to calculate. Its technical definition is that it's the expected value of the cumulative reward (often exponentially discounted) conditional on starting in that state. This is an expectation with respect to a very complicated measure; for episodes (sequences of states) of reasonable length, you will soon be overwhelmed by combinatorial explosion.

So there is a double-optimization problem: given a policy, you have to perform an optimization problem to estimate the value function. And given a value function, you have to use that to update your policy. But what's interesting about the reinforcement learning setting is that you don't have the clean time-scale separation as you do with the physical networks. Instead, it seems that what reinforcement algorithms do is that instead of attempting to calculate the value function for a policy exactly (which would take forever), they approximate it through sampling and bootstrapping from their previous value estimates. So rather than alternating optimization problems, it's instead two coupled, concurrent optimization problems that hopefully are balanced in such a way that everything  converges.