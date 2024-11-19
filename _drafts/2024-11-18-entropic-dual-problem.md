---
layout: post
title: "Post Template"
date: 2024-11-18
mathjax: true
---

We will show the derivation of the dual problem in entropic optimal transport. The procedure is similar to the case in the unregularized
problem, but the final step is a bit more interesting as we will have to use *Gibbs Variational Principle* in order to evaluate
the free energy functional.

For entropic optimal transport, we have that the primal problem is of the form

$$S_\epsilon(\mu, \nu) = \inf_{\gamma \in \Gamma(\mu, \nu)}\int ||x-y||^2 \gamma(dx, dy) - \epsilon \text{KL}(\gamma||\mu \otimes \nu)$$

The addition of the KL term makes it so the optimal coupling is higher entropy than the optimal coupling in the unregularized problem.
The regularization parameter $\epsilon$ has the straightfoward physical interpretation as a *temperature*. In the case that $\epsilon = 0$,
we recover the unregulared OT problem. In the case, that $\epsilon$ goes to infinity, then the regularization term will dominate
and our optimal coupling will be the product measure $\mu \otimes \nu$---which is the highest entropy distribution which satisfies
the contraints (marginals $\mu$ and $\nu$).

We will be looking to turn the problem of finding the optimal coupling $\gamma$ to the problem of finding the maximal functions
$f$ and $g$. As we did in the unregularized OT problem, we replace the case.