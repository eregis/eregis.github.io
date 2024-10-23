---
layout: post
title: "'Statistical Optimal Transport' by Sinho Chewi"
date: 2024-10-21
mathjax: true
---

A common problem in statistics is that of sampling. Let's say we have some unknown distribution $\pi$. We can ask

1. Practically, how do we go about producing samples that "draw" from $pi$?

2. When can we be sure that our sample sufficiently resembles the true underlying distribution? 


Most people's earliest introduction to sampling is in high school when they learn about introductory statistics concepts like the
standard deviation of the mean. The standard deviation of the mean, while simple, is actually a nice illustration of the type
of questions that the field of sampling is concerned with.

To recap: Let's say that you are sampling from some distribution $\pi$. Then given a sample of size $n$, you can compute the sample mean
and the sample variance. These are measures of the average values of the points in the sample,
and how spread out the points in the sample are, respectively.

$$\bar{x} = \frac{1}{n} \sum_{i=1}^n X_i \quad \text{and} \quad s^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{x})^2$$

The standard deviation of the mean (SEM) is a bit different than the sample mean and sample standard deviation.
Unlike the latter two quantities, the SEM is not a property of the *sample*,
but a property of the underlying distribution and its distribution of samples.
It tells you, given a sample size of $n$, how far (in absolute distance) you should expect the sample mean 
to be from the true population mean.

You could then ask: how does the SEM change with $n$? Intuitively, we know that it should decrease; the larger your sample, the more
likely it is that your sample is representive of the population that it was drawn from. But can we quantify this relationship?

Yes. Computing the standard deviation of the mean when drawing from a univariate Gaussian is straightforward 
and worth computing for yourself. What you will find is that as a function of sample size,
the standard deviation of the mean goes asymptotically as $\frac{1}{sqrt{n}}$. 

But the *mean* is only one property of a probability distribution. If, for example, you have a bimodal distribution
as your true distribution, then you are less interested in whether the mean of your sample matches the mean of your population.
Instead, you might be more concerned with more complex questions, 
such as how quickly the relative weights of the two modes in your samples come to resemble the relative weights in the true distribution.

It's straightfoward to ask how close the mean of the sample is to the mean of the population. 
If you have a one-dimensional distrbution, then you just find the magnitude of the distance; 
even if you have a multivariate distribution, you just take the magnitude of the difference of the vector of means. 
There is a natural, canonical metric structure for $\mathbb{R}^d$.

But it's less straightforward to ask whether one probability distribution is "close" to another. 
One common way is via the KL divergence (also known as the cross entropy):

$$\text{KL}(p||q) = \int dp \log \frac{dp}{dq}$$

($\frac{dp}{dq}$ is something called the Radon derivative. Don't worry too much about it. For our purposes, 
$\frac{dp}{dq} \equiv \frac{p(x)}{q(x)})

But the KL divergence has some unsatisfying properties. The big one is the sensitivity to the support of the distributions. 
If the coding distribution $q$ is zero on an interval where the true distribution $p$ is non-zero, 
then the KL divergence is actually infinite. (One can see from the expression for the KL that we would be dividing by zero---which is not good)
Somewhat troubling, this is not true for the converse. If the coding distribution is non-zero when the true distribution is zero, then
the KL evaluates to 0 ($\lim_{x \rightarrow 0} x \log x \rightarrow 0$). The KL divergence is assymetric.

But more to the point: we want to compare the distribution of our sample (which is called the empirical distribution)
to the true distribution. However, the empirical distribution is not smooth. It is discrete, composed of Dirac delta functions.
The probability density function of the empirical distribution is typically written as:

$$\hat{f}_n(x) = \frac{1}{n} \sum_{i=1}^n \delta(x - X_i)$$

where $\delta$ is the Dirac delta function, $X_i$ are the observed values, and $n$ is the sample size.

Discrete distributions don't play nicely with the KL divergence. The problem is that the KL divergence is ultimately a *vertical* distance
measure. To compute the distance between two distributions, it takes the ratio between them at each point, 
takes the log of those ratios, and then sums everything up.

So if there is a *single* interval where the coding distribution is zero, but the true distribution is non-zero, 
the KL divergence is infinite. This leads to weird counterintuitive results like if you consider two uniform distributions, 
both of diameter 1, 
the KL divergence between them is infinite unless they share the same center (and zero in the case that they do share the same center).

In many common instances, the KL divergence doesn't match our intuition---which is more continuous. 
Our intuition is that the uniform distribution on $[0,1]$ is very similiar to the uniform distribution on $[0.1, 1.1]$ and 
very different from the one defined on $[1000000, 1000001]$. Is there a distance measure that does that?

Yes. It's called the Wasserstein distance. It comes from a subfield of probability theory called optimal transport. 
If the KL divergence is a vertical notion of distance, then the Wasserstein distance (and optimal transport in general) 
is concerned with a more horizontal notion of the distance between probability distributions.

The field has its origin in the Monge problem. Let's say you have a mound of dirt. 
And you want to transform that mound of dirt into a differently-shaped mound. 
And let's say that cost of transporting a speck of dirt is proportional to both the mass of the speck as well as 
the distance that the speck travels. What is then the way to transport dirt to create the target mound, while minimizing the cost?

"C:\Users\ericf\critical-points\assets\statistical-optimal-transport\the_monge_problem.png"

The Monge problem is old, first proposed in the 18th century. The original problem asked for a
solution in terms of transport maps. But it turns out that this is too restrictive to be interesting. 
So the modern formulation of the problem (which we owe to Russian mathematician Kantorovich), instead of using transport maps, 
instead imagines the two mounds of dirts as probability distributions $\mu$ and $\nu$ that are 
the marginals of a joint distribution $\gamma$. 
We can denote $\Gamma(\mu, \nu)$ to be the set of all joint distributions whose marginals are $\mu$ and $\nu$. 

The Wasserstein distance is the minimal expected distance achieved by the optimal coupling:

$$\inf_{\gamma \in \Gamma(\mu, \nu)} \int |x-y| \gamma(dx, dy)$$"

This notion of distance is better. It's much better behaved when working with distributions of dissimilar supports, 
such as when working with discrete and continuous distributions simultaneously. 
It also doesn't diverge. The Wasserstein distance between any two probability measures is always finite.

Because we have a notion of distance between probability measures that behaves well with both discrete and continuous distributions, 
we can now ask questions like: given a distribution $\mu$ and the random empirical distribution $\mu_n$, 
what is the *expected* Wasserstein distance as a function of $n$.

This is the field of statistical optimal transport.

# Optimal Transport

This book is meant to be an introduction to the field of statistical optimal transport.
It requires a good bit of mathematical maturity (I would peg the book as first-year grad level text), 
but it assumes surprisingly little background. You will want to understand probability theory at an undergrad level 
(for example, be comfortable with marginals), but otherwise, the book teaches a lot of the other math it uses in a clear, 
albeit somewhat brisk manner. 

The first four chapters of the book introduce optimal transport and briefly discuss some of the most common problems
studied in optimal transport theory.

The first chapter of the book is devoted to explaining optimal transport from the ground up, starting with the Monge problem 
and then building up from there.

In the Monge problem, we assume that the cost is proportional to the distance. But there are many different possible cost functions. 
The most general formulation of Kantorovich's problem is:
$$\inf_{\gamma \in \Gamma(\mu, \nu)} \int c(x,y) \gamma(dx, dy)$$
where $c$ is the cost function.
The Monge problem corresponds to the case when $c(x,y) = |x - y|$. 
One important generalization is $c(x,y) = ||x -y||^p$, which is analogous to $p$-norms on vectors in Euclidean space. 
The case that is most studied throughout this book is the Wasserstein-2 metric, corresponding to the cost function:
$$c(x,y) = ||x-y||^2$$

Another interesting case is the total variation distance. If you imagine two probability distributions as graphs 
plotted on the same set of axes, the total variation distance measures the area where they do not overlap

"C:\Users\ericf\critical-points\assets\statistical-optimal-transport\total_variation_distance.png"

This turns out that the total variation distance is the Wasserstein-0 metric. If your cost function is the indicator function: 
$c(x,y) = \mathbb{1}_{x \neq y}$ 
(so there is a cost associated with moving the speck of dirt, but the cost is not sensitive to the distance traveled), 
then you recover the total variation distance.

A running theme throughout this book is *convex optimization*. Convex optimization is a subfield of math concerned with
optimization problems where the set of objects under consideration is convex. There are multiple equivalent notions of convexity.
One definition is that a set is convex if, for any two objects in the set, the object halfway
between them is also in the set (what "halfway between" means will depend on the mathematical structure of the set in question).

Optimal transport is a convex optimization problem; the set of couplings $Gamma(\mu, \nu)$ is convex. If $\gamma_1, \gamma_2 \in Gamma$,
then the mixture measure $\gamma = \frac{1}{2}(\gamma_1 + \gamma_2) will retain the marginals of \mu and \nu 
(meaning that $\gamma$ will be in Gamma(\mu, \nu) as well).

Convex functions also plays an important role in one of the crowing jewels of optimal transport theory: Brenier's theorem. 
We mentioned before that the strength of Kantorovich's formulation of the Monge problem 
is that it doesn't assume the existence of a transport map 
(and indeed, one can show that in certain simple cases that no transport map exists).

But if the target measure $\nu$ is absolutely continuous with respect to original measure $\mu$. Then a transport map *does* exist.

$$T_{#}\mu = \nu$$

where the expression above should be read as "$\nu$ is the pushforward measure of $\mu$ acted on by $T$".

Brenier's theorem says that this transport map must be the gradient of some convex function $\phi$. And this is an if and only if: if
there is a transport map $T$ which pushforwards $\mu$ to $\nu$ and $T$ is the gradient of a convex function, 
the optimal coupling *must* correspond to the law of $(X, T(X))$ where $X ~ \mu$.

Convex optimization also plays an important role in the dual formulation of the optimal transport problem. Rather than simply finding
the coupling cost function, one can instead find the set of function $f(x)$ and $g(y)$ such that their expectation with respect to $\mu$
and $\nu$ are maximized. With the constraint that their sum has to be less than the original cost function.

To show that the two formulations are equivalent is not too complicated, but I will still elide the proof. But the intuitive idea
is that if two measures are very different from each other, then they will return.

The reason behind Brenier's theorem is that gradients of convex functions are the natural generalization higher dimensional of monotonic
functions in one dimension.

There are then chapters on estimation of transport maps and entropic optimal transport. These are interesting.

Chapter 2 is on estimation of Wasserstein distances. A large part of this chapter are fussy proofs involving dyadic cubes
which bored me when I were first exposed to them when I first learned measure theory and still bore me now.

But there is an interesting treatment of the *curse of dimensionality*. We mentioned before the standard deviation of the mean
behaves asymptotically as a function of the sample size as the inverse square root of $n$. But in settings like machine learning
or genomics---spaces where the data is extremely high-dimensional---we also care about the assymptotic behavior of the estimator
as a function of the dimension $d$ of the underlying data space. And it turns out that a lot of the concepts in statistics
break down in the the limit of high dimensions.

Let's revisit our example of the standard deviation of the mean, but for simplicity, restrict ourselves to the problem of Gaussians
that are the product distributions of uncorrelleated uni-dimensional Gaussians of unit variance.

$$P_d(\vec{x}) = $$

We are interested in two questions:

1. Keeping the sample size $n$ fixed, what is the asymptotic relationship between the SEM and the number of dimensions $d$?
2. Keeping the number of dimensions $d$ fixed, what is the asymptotic relationship between the SEM and the sample size $n$?

For the case of the standard deviation of the mean, we have that the the SEM goes as the sqrt of the dimension, and that the inverse sqrt
of n (We only showed this to be true in the Gaussian case, but the Law of Large numbers ensures that this is quite general and holds for all
distributions)

But what about the case when we have the Wasserstein distance between the empirical distribution and true distribution. Here,
the relationship is more complicated.

"C:\Users\ericf\critical-points\assets\statistical-optimal-transport\wasserstein-law-large-numbers.png"

We won't dwell on the details (like the particularly interesting case when $d = 2$). But the key point is that in the case of SEM, the assympotic behavior of $n$ is independent of the dimension $d$. But for the case
of the Wasserstein distance, we have a $d$-dependence on the assymptotic behavior: the large that $d$ is the smaller that the dimension is.

This is the curse of dimensionality. 

Chapter 3 discusses estimating transfer maps and Chapter 4 discusses entropic optimal transport (optimal transport but with
an added regularization term that penalizes low-entropy couplings). Both are interesting topics. What they have in common is
that they both lean heavily on the dual problem. For transfer maps, it's a common problem where we have an empirical distribution
but we aren't sure how to extropolate to other data points. The generalized approach is to impose "smoothness" conditions where your
notion of smoothness depends on what structural assumptions you are bringing with you. This can actually be most naturally done
in the dual formulation as imposing a smoothness condition on the Kantorovich potentials will naturally endow the transfer map
with the desired smoothness properties. And for entropic optimal transport, we can turn our previous constaint on the sum of 
the Kantorovich potentials into instead a smooth function which approaches the hard constraint in the limit as epsilon goes to zero.


# Wasserstein Gradient Flows and Wasserstein Geometry

But the beating heart of the book is certainly the back half of the book on Wasserstain gradient flows and metric geometry in Wasserstain space. The key idea (that is shares in overlap with information geometry--but is executed *much* better in the case of statistical optimal transport) is that when equipped with the Wasserstain distance, the space of probability measures form a metric space which allows us to do analysis on the otherwise unwieldy space. Actually making this technically precise is a bit of work; in contrast with Information Geometry which uses the Fisher information as a metric tensor as the jumping off point, the Wasserstein distance is not a local tensoral object but a global metric on the entire space. "Locallizing" the Wasserstain distance properly requires a bit of technical exposition that the book prefers to elide (it cites Gradient Flow by Ambrosio as the go to resource to seeing the Riemmanian picture of optimal transport made precise).

The idea behind Wasserstain gradient flow is very similar to the type of picture one might encounter in a classical mechanics class: We can write we can have an ODE of the form

$$\dot{X}_t = v_t(X_t)$$

So an at every point in space, there is a vector field and the 

An important piece of the puzzle for statistical optimal transport is the field of convex optimization. Like with Riemannian geometry, it helps to be familiar with convex optimization, but the book exposits as it goes along.

There are many different notions of convexity. The simplest is probably that a convex function is one where the output of the average of the inputs is always less than the average of the output of the inputs. 

$$f((1-t)x + ty) \le (1-t)f(x) + t f(y)$$

Convexity appears again and again in different spots in this book.

Including at the very beginning. 
I mentioned at the beginning that the original formulation of Monge's problem was limited due to thinking in terms of Transport maps instead of couplings. But it turns out if $\mu$ (the starting distribution) admits a density, then there *is* a transport map such that the pushfoward of $\mu$ under $T$ is $\nu$.

Another idea that comes from convex optimazation is the Kantorovich dual. 
Rather than finding the optimal couping, we can instead find the optimal set of function 
$f(x)$ and $g(y)$ such that (a) the sum f(x) + g(y) is not too big 
(where too big is determined by the cost function) and their expectation with respect to $\mu(dx)$ and $\nu(dy)$ respectively are 
maximized. And it turns out that this maximum value is exactly equal to the Wasserstain distance. 
The connection to convex optiziation is that when the cost function is $c(x,y) = |x - y|^2$ (which corresponss to Wasserstain-2 distance),
 then the two functions $f$ and $g$ will be convex conjugates of each other.

The two formulations of optimal transport allow us to estimate the Wasserstain distance between two measures. 
he formulation in terms of couplings is a minimizaton problem. So finding a sub-optimal coupling allows us to upper-bound the Wasserstein distance. But the Kantovorich dual problem is a *maximation problem*. So suboptimal functions $f$ and $g$ allow us to lower-bound the Wasserstein distance.

The key equation for Wasserstein gradient flows is

$$\frac{\partial \mu}{\partial t} 

The last chapter is on Wasserstein barycenters. Barycenters are generalizations of the mean to spaces where there isn't
a well-defined notion of addition. In Euclidean space, we can find the mean but. But a generic metric space doesn't
have a notion of addition. The mean also has the property that, given a set of points $x_i$, it minimizes the functional

$$D(\mu) = \sum_i^n d^2(x_i, \mu)$$

where $d^2(\cdot, \cdot)$ is the Euclidean metric squared. This definition can be generalized to other metric space: the center
of a cluster of points that which is the least far from all of them.

This idea of a barycenter becomes interesting when considering more abstract spaces than Euclidean space. For example, consider
the space of images. We can represent images with $d$ pixels with three colors (so the overall space is encoded in $\mathbb{R}^{3d}).

But you could ask: given two images, what's the average of the two images? The naive way of doing it---averaging the pixel values---isn't
the correct approach. But why not?

"C:\Users\ericf\critical-points\assets\statistical-optimal-transport\average_pixel_intensity.png"

The short answer: Because our embedding from the abstract space of images to their representations in pixels isn't an isometry.

To elaborate: You can imagine that images live in some abstract space where images are close to each other if they are *semantically*
similar. They represent the same underlying concept. The distance measure we care about is that distance measure.

There is no reason why the true semantic distance measure matches the Euclidean structure of $\mathbb{R}^{3d}$.

This motivating example was interesting enough that I wanted to include it. I think a lot about semantic structure of language,
especially in the context of machine learning. But I notice (unless I missed it during my re-reading) that the book never answers
how one would go about finding the semantic distance between images. But I guess that's a rich topic better suited for a different book.