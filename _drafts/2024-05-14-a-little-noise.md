---
layout: post
title: "A Little Noise Has Never Hurt Anyone"
date: 2024-05-14
mathjax: true
---

I'm interested in the idea of when noise is good.

One example is the explore versus exploit; you don't want to just maximize the expected value of your next action; what you are actually optimizing is the total value accrued over the entire lifespan. So for each decision, you need to break out the different ways value accrue for the decision. There is the immediate transfer of value; there is the transfer of value due to what future reachable states (with associated rewards) are gettable in the future time steps, but then there is this extra third component called "information" which is what observing the outcome of your current decision allows you to make better decisions in the future (which a better decision means better according to the three criteria above in a recursive fashion).

Value of information analysis is nothing new; it was really popularized in the 70s when a lot of the theory was worked out. And today, it's well-known to those who work in reinforcement learning the value of information.

What are some other places where noise is good?

**Evolution**

Here we see that the presence of mutations allows evolution to explore the space of different organisms. This manifest as mutations at the level of genome which would appear in asexually reproducing species like bacteria to create genetic variation.

One of the broad principles to think about noise is to borrow a finance term that of *optionality*. An option gives the option (but doesn't demand you) to buy (or sell) a thing at given price. So if you have an option for $100, then if the thing's value rises above $100, you exercise the option and if it falls below the $100, you don't exercise the option (and what you lose is what you paid for the option).

In the case of evolution, because of natural selection, nature has an "option" on the organisms: organism designs that work well will be more common in the future.

Another place that noise can be helpful is to reduce the effective dimension of the space: a kind of high-pass filter or Gaussian blurring or med-filtering. Here, we want that our behavior to be continuous with respect to the domain. And as I outlined in a previous blog post, there is a natural relationship between continuous, broadly construed, and the absense of high-frequency modes of a system.

There was an interesting project that my advisor was working on that used noise as a coordinating mechanism with the motor. The insight that I gained from it is that the noise sets a certain type of scale for the gradient where below a certain gradient (signal-strength), the presence of noise, while degrading the current signal, causes the bacteria to engage in explore dynamics (as is optimal when the current information is weak) and then at higher signals, engage more in exploit dynamics (as is optimal when you have a lot of information already).

Basically, it helps to think about what the bacteria is *really* optimzing for: it's optimizing for the amount of useful information over its lifetime to perform chemotaxis. That means you can tradeoff current information if (a) it's not useful (isn't relevant to the problem of chemotaxis) or (b) it allows you to get *even more* useful information than you would have otherwise.

There is also this interesting idea of noise-induced disorder.
