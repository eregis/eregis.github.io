---
layout: post
title: "Double Optimization Problems"
date: 2025-09-12
mathjax: true
---

Guzman's talk introduced an interesting conceptual framework: double optimization problems. The idea is that physical learning can be neatly seperated into two seperate optimization problems:

1. Given a current input voltage, the network itself (via the laws of physics) is performing an optimization problem over the voltages of the nodes such that the power is minimized across the network.
2. We, the controllers, shift the conduncdances of the network so that over the time the physical network learns to embody the desired function that we want it to compute.

The important story here seemed to be two details: (1) That we get the first optimization "for free" and (2) Seperation of time scales between the two optimization processes (equilibriating in response to external voltage happens on a much shorter time scale than adjusting the conductances to learn the target function).

I like this framework because it seems quite general. I have been recently learning some reinforcement learning and it also features a double optimization problem.

In brief: Reinforcement learning is the study of how agents learn how to maximize the long-term rewards by way of short-term actions. Two fundamental objects in reinforcement learning are the policy (the function that dictates which actions the agent will take in any given state) and the value function (the function that says, given the agent's current behavioral policy, how good visiting a given state will be for the agent in the long-run.)

Where double optimization comes into play is how the agent learns how to update its policy to become more optimal over time. In a class of reinforcement models called actor-critic models (these are models that have a neural network tasked with learning the policy [actor] and a seperate neural network for learning the value function "the critic".) The idea is that given a current policy, you estimate the value function of that policy. You then update your policy so that you actions that do better than expected for that state (called having a positive advantage) are done more often, while actions that do worse than the average for that state (negative advantage) are done less often. You then compute the value function for your new policy, rinse and repeat, until (hopefully) your policy is globally optimal in the space of all possible policies.

One of the difficulties is that the value function for a given policy is actually non-trivial to calculate. It's technical definition is that it's the expected value of the cumulative reward (often exponentially discouted) conditional on being in starting in that state. This is an expectation with respect to a very complicated measure; for episodes (sequences of states) of reasonable length, you will soon be overwhelmed by combinatorial explosion.

So there is a double-optimization problem. But what's interesting about the reinforcement learning setting is that you don't have the clean time-scale seperation as you do with the physical networks. Instead, it seems that what reinforcement algorithms do is that instead of attempting to calculate the value for a policy exactly (which would take forever), they are. So rather than alternating optimization problems, its instead two coupled, concurrent optimization problems that hopefully are balanced in such a way that everything converges.