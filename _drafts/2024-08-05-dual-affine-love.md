---
layout: post
title: "Learning To Love The Dual Affine Connection"
date: 2024-08-05
mathjax: true
---

Why isn't information geometry more popular? The core insight--that parameteric families of probabilies distributions form a differentiable manifold--is pretty intuitive and was observed all the way back in the 40s by Rao. Yet, not many people know about this field. It hasn't (as far as I am aware) contributed any ground-breaking results to statistical inference; Not that this is fatal flaw. Lagrangian mechanics was at first just an equivalent formulation of Newtonian mechanics. But new formalisms allow for novel extensions can lead to new ground due to which concepts they place as fundamental versus those that are derived.

But as far as I'm aware, information geometry is deeply unpopular among statisticians. It seems mostly to be popular among mathematicians and physicist who are already familiar with differential geometry and then get into statistical inference in an oblique way.

Based on brief discussions with other people interested in information geometry, if I had to pinpoint *one* place where things start to get a bit suspicious is the dual affine connection.

Everyone I know is on-board with the metric tensor being given by the Fisher information matrix. But while in general relativity, the connection is the Levi-Civita connection which is the unique, torsion-free, metric compatible. The problem of the "correct" connection is an important one as the connection ultimately determines how we travel between the local structure of our space to the global structure. And the Levi-Civita connection can be expressed quite simply in terms of partial derivatives of the metric tensor.