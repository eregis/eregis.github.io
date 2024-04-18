---
layout: post
title: "A Continuous Notion of Continuity"
date: 2024-04-18
mathjax: true
---

Here is the rewritten version with $latex... $ replaced by $$ ... $$:

In analysis, we are often concerned with continuous functions. But this is usually a binary distinction: a function is either continuous or it's discontinuous. Is there a way to quantify how continuous a function is?

One obvious way to proceed is to use measure theory. Discontinuous functions can be categorized based on the measure of the set of their discontinuous points. The Heaviside step function would be considered "almost" continuous because it's continuous almost everywhere (in this case, continuous everywhere except at the origin). While the Dirichlet function $$ 1_\mathbb{Q} $$, which evaluates to 1 on the rational numbers and 0 on the irrational numbers, would be considered "very" discontinuous as it's discontinuous everywhere.

But let's only consider the class of functions that are continuous everywhere. Are there continuous functions that are almost discontinuous? Maybe! Consider the sequence of function

$$ f_m(x) = \begin{cases} 0 & \text{if } x \leq 0, \ mx & \text{if } 0 < x < \frac{1}{m}, \ 1 & \text{if } x \geq \frac{1}{m}. \end{cases} $$

Every function in the sequence is continuous. But in the limit, our sequence of functions approaches the Heaviside step function. There seems to be a sense in which we are becoming more and more discontinuous as the sequence progresses--even though every term in the sequence is continuous.

A continuous function is one where small changes in the input correspond to small changes in the output. Considering our sequence $$ (f_m) $$ progresses, the slope of the transition line gets steeper and steeper. And in the limit, the slope becomes infinite.

To better understand how a function changes over its domain, let's use the Fourier transform. The Fourier transform represents our function in frequency space. Functions that change slowly will have a Fourier transform dominated by low frequencies while functions that change quickly will have a Fourier transform with high frequencies.

Let's take a closer look at the step function as it's a canonical example of a discontinuous function. Though we will consider the box function which is easier to Fourier transform due to its bounded support.

$$  g(x) = \begin{cases} 0 & |x| > 1  \ 1 & |x| \le 1 \ \end{cases} $$

Famously, the Fourier transform of the box function is the sinc function $g(k) = $$ \frac{sin k}{k} $$. We care about the large frequency behavior of $$ g(k) $$. And what we see is it that $$ g(k) $$ behaves asymptotically as $$ 1/k $$. But there is an extra wrinkle depending on which value of $$ x $$ we are evaluating the function at. For example--though with sinusoidal term in the numerator causing the integrand to alternate signs. This is the alternating harmonic series in disguise! We can see that by rescaling (which shouldn't change qualitative behavior like the discontinuities of the inverse Fourier transform)

What about if we instead take a look at sin^2 k/k^2. What we then have is now a triangle graph. This is a continuous function. But notice that its derivative is discontinuous. Is this a coincidence? No. It can be seen quite plainly that if we take the derivative with respect to G(x), represented as a Fourier transform, we get a function's whose spectral representation behaves asymptotically as 1/k–which we already showed for the case of the box function to be characteristic of discontinuity.

$$ G(x) = \int_{-\infty}^{\infty} e^{ikx} \frac{\sin(k)}{k} $$

We can then make a general rule of thumb: power law assymptotical behavoir in the spectral representation is connected to discontinuious behavior in the derivatives (or the original function).
Note that we can even extend this principle the other way. Consider the case where we have take the Fourier transform of the contant function. Which is the same as being of order k^0. Following our pattern, that would imply that the -1th derivative is discontinious. Does that make sense?

Actually yes, this integral famously is yields the dirac delta distribution, which, while technically not a function, can be manipulated still be manipulated under the integral sign. The dirac delta is defined such that if your interval of integration contains x =0, the integral evalues to 1. If it doesn't contain x = 0, then the integral evaluates to 0. One can see that, if we define an indefinite integral starting at a lower bound of negative infinity, the antiderivative of the dirac delta is just the step function. So it does make sense to say that if we think of indefinite integration as take a "negative" derivative, our principle still holds. The -1st derivative does indeed contain the discontinuity.