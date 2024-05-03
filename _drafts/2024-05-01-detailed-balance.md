---
layout: post
title: "Six Intuitions About Detailed Balance"
date: 2024-05-01
mathjax: true
---

Shorter post:

Wikipedia has to ways to check if a transition matrix obeys detailed balance. That is in terms of the stationary distribution and in terms of the cycles of the graph. These are fine intuitions, but I feel like Wikipedia neglects a couple perspectives on detailed balance that are practically useful when considering the condition on a research setting.


A transition matrix $$T$$ describes a system obeying detailed balance if

$$T = D S$$

where $$D$ is a diagonal matrix and $$S$$ is a symmetric matrix. This means that 