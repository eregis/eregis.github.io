---
layout: post
title: "Modifying Optimization Problems"
date: 2025-11-25
mathjax: true
---

In a constrained optimization problem there are two parts: (1) there is the objective which is what we are optimizing (2) there is set of viable objects which are the possible arguemnts for the object that are under consideration.

In many different cases, we have an optimization problem that for whatever reason we find insufficient. Sometimes in the case of regularization terms in the context of L2 regulariztaion in machine learning, this is because we think that the naive optimization problem is not "really" the one we want to be optimizing (basically it's only one objective whereas our true objective as competing considerations). But often times: the objective function that we have is in fact that "correct one" (in the sense that in whatever context is under consideration, if we were given the true solution to that objective we would be quite happy), but finding this solution is too hard. This is what I would like to talk about. Some example of this theme are:

(a) the convex relaxation. Non-convex otpimization problems ar ehard whereas non-convex optimization problems are easier. If we can find the convex optimization problem that is a close approximation for our non-convex porblem that would be a lot easier.

(2) changing the objective set. When modifying the objective set there are basically two directions one could go in: one could go smaller (consider a smaller number) of possible solutions. Or one could go larger. Going larger can go one of two ways. It could like you keep the same number of variables but increase the state space. (e.g imagine your feasible set is some complicated set in R^d) and you decide to expand your feasible set to the convex hull of this feasible set. Another way is to augment the number of variables and also modify the optimization problem itself. Really common is to augment your space under consideration into a path space. There is also a conceptual difference between whether one is interested in the value of the objective itself at the minimum or the argmin (this seems to be much more common of a thing to care about)

The original inspiration for this was the Bethe entropy as done by Wainwright in graphical models textbook. It was interesting because it showed how when calculating the entropy of complicated graphical models, how playing around with both the objective and the feasible set can help you make computationally tractable approximations for the more complicated things.