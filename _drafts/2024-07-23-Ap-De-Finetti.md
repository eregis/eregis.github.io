---
layout: post
title: "The A_p distribution and Length Scales of Evidence"
date: 2024-06-13
mathjax: true
---

In my introductory post on the $A_p$ distribution, I appealed to the intuition that the proposition $A_p$ stands for an "infinite" amount of evidence. It's perhaps a good idea to unpack that intuition.

The reasoning behind the intuition was that the defining absorption propery of the proposition $A_p$ was similar to how infinite objects interact with finite objects (e.g the cardinality of the union of an infinite set and a finite set is infinite, not infinity plus one or whatever).

$$P(A|A_p E) = P(A|A_p) = p$$

This is a nice definition, but an immediate question appeals to mind: what happens when you condition on two $A_p$ distributions?

$$P(A|A_p A_q) =???$$

This is not fatal--in fact, it isn't even an uncommon problem to have in probability theory. If you condition on two mutually exclusive propositions, then there is no well-defined probability for any attempted computed conditional probabilities.


But what does the A_p distribution *look* like? Envisioning it as a Venn diagram, if you imagine it that $A$ is represented by red and $not-A$ is represented by blue, then the AP distribution looks like fractally red-blue.

[Some visualization of fractally blue-and-red]

This would be taking any such subset (which is equivalent to encountering some evidence $E$) is equivalent to taking some subset.