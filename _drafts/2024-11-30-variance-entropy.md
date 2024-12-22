---
layout: post
title: "The Variance and The Entropy"
date: 2024-11-30
mathjax: true
---

so what are supposed to the inputs to the Bregman divergence; the density points?
I see: so as I said earlier Bregman divergence is useful as a measure of distance when you have a notion of substraction,
 but the best distance metric isn't Euclidean. Consider the density at a given point; then we want to know: 
 how different are the density values at that point. Densities live in the positive real numbers; 
 it turns out that the induced distance is the Bregman divergence induced by x log x

Note that in the case that we are in the discrete case; then we are dealing with not densities, 
but probabilities; there it makes even more intuitive sense that the Euclidean metric is not good as probabilities live on [0,1]; 
In that case the entropy, and the variance are not so disimmilar; they are both expected distances in a sense; 
the variance is a horizontal measure; where it measures on average how far points are from their center;
while the entropy is a horizontal measure; where it measures how far on average in Bregman divergence the density is 
from the uniform distribution (this is more tidy when you consider the discrete case; though in the case of the entropy, 
there might be a log N factor floating around to make things be properly centered)

I see and they are connected because of concentration of measure.
Let's unpack this a bit more. Let's work in the finite case of N points for simplicity.
What are high characteristics entropy, but low variance distributions? What about vice versa?
A good example is that the distribution with dirac delta split evenly for the endpoints is the maximum variance distribution given the support. But it's entropy is quite low (log2).
(I wanted to say something like lower than average, but I don't know what the most principled distribution on the space of distributions supported on N points. Would it be Jeffrey's prior? something else?)
One thing that immediately stands out to me is that thinking about the action of maps. The entropy can only decrease on deterministic maps; and if the map is a bijection (a permutation), 
the entropy will remain constant; so there is a sense in which the bijectivity of a map can be quantified by the extend
But the variance can be increased or decreased! While permutations are "on average" going to preserve the variance while the 
mappings that sent flow to the end points will increase variance and mappings that map them to a single point decrease variance
But deterministic maps (as we learned from the Kantorovich formulation of the Monge Problem) are not the most natural way to think 
about mappings on probability distributions. Really we care about how the variance and the entropy behave under the behavior of
Markov 

I think high-entropy low variance is the normal distribution, no? 
It's literally the maximum entropy distribution with that variance (that's on the continuum; 
I'm not sure what the maximum entropy distribution would for a given variance would like on N supported points but 
given reasonably variance relative to support size, it should look "normalish"