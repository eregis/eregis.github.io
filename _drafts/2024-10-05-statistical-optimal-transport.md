---
layout: post
title: "'Statistical Optimal Transport' by Sinho Chewi"
date: 2024-10-05
mathjax: true
---

A common problem in statistics is that of sampling. We have some unknown distribution $\pi$ and we want to know how quickly we will learn various facts about $\pi$.

Probably the earliest introduction most people have to this concept about the standard deviation of the mean. Let's say that you are sampling from a Gaussian. Then given a sample, you can compute the sample mean and the sample standard deviation. These are the average values of the points in the sample, and the how spread out the points in the sample are, respectively. But the standard deviation *of the mean* is not a property of the sample, but a property of the underlying distribution and its distribution of samples. It tells you, given a sample size of size $n$, how far (in absolute distance) is should you expect the sample mean to be from the true distribution mean?

You could then ask: how does that change with $n$? And what you find is that distance of the standard deviation of the mean goes asymptotically as $1/sqrt{n}$. This is why we care about sample size in the first place: the larger the sample size, the closer you should expect your sample to resemble the true distribution.

But the *mean* is only one property of a probability distribution. For example, if you have a bimodal distribution as your true distribution, then you are less interested in whether the mean of your sample matches the mean of your population, but if empirical distribution of the sample matches . It's straightfoward to ask how close the mean of the sample is to the  mean of the population with random variables. If you have a one-dimensional distrubiton, then you just find the magnitude of the distance; even if you have a multivariate distribution, you just take the magnitude of the difference of the vector of means. There is a natural, canonical metric structure for $\mathbb{R}^n$.

But it's less straightforward to ask whether one probably distribution is "close" to another. One common way is via the KL divergence (also known as the cross entropy).

$$\text{KL}(p||q = \int dp \log \frac{p}{q})$$

But the KL divergence has some unsatisfying properties. The big one is the ultra sensitivity to the support of the distributions. If the coding distribution $q$ is zero on an interval where the true distribution $p$ is non-zero, then the KL divergence is actually infinite. Troubling as well, this is not true for the converse. The KL divergence is assymetric.

But more to the point: we want to compare the distribution of our sample (which is called the empirical distribution) to the true distribution. But the empirical distribution is not smooth. The distribution is discrete, composed of dirac deltas.

$$q(x) = \frac{1}{n} \sum_{i=1}^n \delta(x - x_i)$$

Discrete distributions don't play nicely with the KL divergence. The problem is that the KL divergence is ultimately a *vertical* distance measure. To compute the distance between two distributions, it compares every point in the distribution pointwise and compares the ratio between the two distributions and then sums up over those ratios (taking the log beforehand). So if there is a *single* subset where the coding distribution is not defined where the true distribution is defined the KL divergence is infinite. This leads to weird counterintuitive results like if you consider two uniform distributions both of diameter 1, the KL divergence between them is infinite unless they share the same center and exactly zero if they do.

This doesn't match our intuition--which is more continuous. Our intuition is that the uniform distribution on [0,1] is very similiar to the one on [0.1, 1.1] and very different from the one defined [1000000, 1000001]. Is there a distance measure that does that?

Yes. It's the Wasserstein distance. It comes from a subfield of probability theory that's called optimal transport. If the KL divergence is a vertical notion of distance, then the Wasserstein distance (and optimal transport in general) is concerned with a more horizontal notion of the distance between probability distributions.

The field has it's origin in the Monge's problem. Let see you have a mound of dirt. And you want to transform that mound of dirt into a differently shaped mount. And let's say that cost of transporting a speck of dirt is proportional to both the mass of the speck as well as the distance that it travels. What is then the way to transport dirt in to create the target mound, while minimizing the cost?

The original problem thought in terms of transport maps. But it turns out that this is too restrictive to be interesting. So the modern formulation of the problem, instead of using transport maps, instead imagines the two mounds of dirts as probability distributions $\mu$ and $\nu$ that are the marginals of a joint distribution $\gamma$. We can denote $\Gamma(\mu, \vu)$ to be the set of all joint distributions whose marginals are $\mu$ and $\nu$. Then we can the Wasserstain distance is the optimal coupling with respect to the cost function:

This notion of distance is better. It's much better behaved when working with distributions of dissimilar supports, such as when working with discrete and continuous distributions simultaneously. It also doesn't diverge. The Wasserstain distance between any two probability measures is always finite.

Because we have a notion of distance between probability measures that behaves well with both empirical distributions, we can now ask questions like: given a distribution $\mu$ and the random empirical distribution $\mu_n$, what is the *expected* Wasserstein distance as a function of $n$.

$$$$

This is the field of statistical optimal transport.

This book, which was converted based on lecture notes, is meant to be an introduction to the field. It requires a good bit of mathematical maturity (I would peg the book as first-year grad level text), but it assumes surprisingly little background. You will want to understand probability theory at an undergrad level (for example, be comfortable with marginals), but otherwise, the book teaches a lot of the other math it uses in a clear, albeit somewhat brisk manner. 

Importantly, it doesn't assume that you've seen optimal transport before. So the first section of the book is devoted to introducing the concept from the ground up, starting with Monge's problem and then building up from there.

There are then chapters on estimation of transport maps and entropic optimal transport. These are interesting.

But the beating heart of the book is certainly the back half of the book on Wasserstain gradient flows and metric geometry in Wasserstain space. The key idea (that is shares in overlap with information geometry--but is executed *much* better in the case of statistical optimal transport) is that when equipped with the Wasserstain distance, the space of probability measures form a metric space which allows us to do analysis on the otherwise unwieldy space. Actually making this technically precise is a bit of work; in contrast with Information Geometry which uses the Fisher information as a metric tensor as the jumping off point, the Wasserstein distance is not a local tensoral object but a global metric on the entire space. "Locallizing" the Wasserstain distance properly requires a bit of technical exposition that the book prefers to elide (it cites Gradient Flow by Ambrosio as the go to resource to seeing the Riemmanian picture of optimal transport made precise).

The idea behind Wasserstain gradient flow is very similar to the type of picture one might encounter in a classical mechanics class: We can write we can have an ODE of the form

$$\dot{X}_t = v_t(X_t)$$

So an at every point in space, there is a vector field and the 

An important piece of the puzzle for statistical optimal transport is the field of convex optimization. Like with Riemannian geometry, it helps to be familiar with convex optimization, but the book exposits as it goes along.

There are many different notions of convexity. The simplest is probably that a convex function is one where the output of the average of the inputs is always less than the average of the output of the inputs. 

$$f((1-t)x + ty) \le (1-t)f(x) + t f(y)$$

Convexity appears again and again in different spots in this book.

Including at the very beginning. I mentioned at the beginning that the original formulation of Monge's problem was limited due to thinking in terms of Transport maps instead of couplings. But it turns out if $\mu$ (the starting distribution) admits a density, then there *is* a transport map such that the pushfoward of $\mu$ under $T$ is $\nu$.

Another idea that comes from convex optimazation is the Kantorovich dual. Rather than finding the optimal couping, we can instead find the optimal set of function $f(x)$ and $g(y)$ such that (a) the sum f(x) + g(y) is not too big (where too big is determined by the cost function) and their expectation with respect to $\mu(dx)$ and $\nu(dy)$ respectively are maximized. And it turns out that this maximum value is exactly equal to the Wasserstain distance. The connection to convex optiziation is that when the cost function is $c(x,y) = |x - y|^2$ (which corresponss to Wasserstain-2 distance), then the two functions $f$ and $g$ will be convex conjugates of each other.

The two formulations of optimal transport allow us to estimate the Wasserstain distance between two measures. The formulation in terms of couplings is a minimizaton problem. So finding a sub-optimal coupling allows us to upper-bound the Wasserstein distance. But the Kantovorich dual problem is a *maximation problem*. So suboptimal functions $f$ and $g$ allow us to lower-bound the Wasserstein distance.

The key equation for Wasserstein gradient flows is

$$\frac{\partial \mu}{\partial t} 