---
layout: post
title: "Random Variables Versus Probability Density Functions"
date: 2024-08-05
mathjax: true
---
For example, let $X$ and $Y$ be random variables with PDFs given by $f$ and $g$, respectively. There is a big difference between $Z_1 = \frac{1}{2}(X + Y)$ and $Z_2$ whose PDF $q(x)$ is a mixture of the PDFs of $X$ and $Y$: $q(x) = \frac{1}{2}(f(x) + g(x))$. 

Let $\mathcal{N}(\mu, \sigma)$ denote a random variable with mean $\mu$ and standard deviation $\sigma$. We will have $X ~ \mathcal{N}(-1,1)$ and $Y ~ \mathcal{N}(1,1)$. So we have two normally-distributed random variables with the same (unit) variance: $X$ is below-average by one standard deviation while $Y$ is above-average by one standard deviation.

$Z_1$--which is the average of the two random variables--is a normal distribution with mean $0$ and a variance $\sigma^2 = 2$.

[Distribution of $Z_1$]

While for $Z_2$, on the other hand, it's distribution is bimodal

Here's an intuition in terms of height. Imagine $X$ represents the height of women and $Y$ represents the height of men. Then if you imagine a world where men and women are paired together randomly, $Z_1$ represents the distribution of the average height of couples. $Z_2$, on the other hand, represents the distributions of heights of both men and women (assuming that there are an equal number of men and women).