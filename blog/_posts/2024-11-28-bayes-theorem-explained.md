---
layout: post
title: "Bayes Theorem Explained"
date: 2024-11-28
mathjax: true
---

It's a not-so-busy Saturday. You've finished all your grading for the week, the NSF grant proposal that you've been slaving away at has *finally* been submitted, and you've even been making some solid progress on your research project. So you decide to treat yourself by going to the local art gallery which has a special exhibit on Maya ceramics this month.

As you are about to leave, you see your umbrella by the door. You pause for a moment before thinking to yourself, 
"It'll probably be fine." You step out of your apartment and see an overcast sky with grey, moody clouds circulating over your head. You go back inside to grab your umbrella.

What just happened there? Why did you go back for your umbrella? Because your beliefs *changed*. It's been a relatively dry autumn, so 
you thought that there was a small chance that it would rain. But you know that grey skies portend rain, so when you saw the overcast
sky, your probability that it would rain increased such that it was now worth the hassle to bring the umbrella along for the trip.

We all do these sorts of calculations every moment of every single day, instinctually. But we can actually mathematically describe what's going on in our heads when we make these sorts of calculations. [Bayes theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem) is a simple but powerful formula that tells you how to update your subjective probability of an event happening upon encountering new information. It's given as

$$P(A|B) = \frac{P(B|A)}{P(B)} P(A)$$

where $A$ is the event whose probability that we are tracking and $B$ is the event corresponding to the encountered evidence. 

$P(A)$ is called the *prior*. It's the probability that you give for $A$ happening *before* you encounter the evidence $B$. In our case, the prior corresponds to the probability we would give for it raining later that day before we stepped out of our apartment. $P(A\|B)$ is called the *posterior*. It's a conditional probability: the probability we give for $A$ to happen *after* encountering the evidence $B$. In the given example, the posterior would be the probability that we would give for it raining later after we saw the grey sky overhead.

To go from your prior to posterior, you have to "update" based on the encountered evidence. This is given by the odds ratio $$\frac{P(B|A)}{P(B)}$$. The key to understanding this term is that what we care about is not the raw probability of $B$ happening, 
*but on how much more likely $B$ is to happen in worlds where $A$ happens as well*.

It helps to consider the two cases: $P(B\|A) > P(B)$ and $P(B\|A) < P(A)$.

In the case that $P(B\|A) > P(B)$, $B$ is *more* likely to happen in worlds that $A$ happens as well. So the ratio $\frac{P(B\|A)}{P(B)}$ is greater than one. This means that our posterior probability of $A$ is higher than our prior probability.

$$P(B|A) > P(B) \longrightarrow P(A|B) > P(A)$$

Conversely, in the case that $P(B\|A) < P(B)$, $B$ is *less* likely to happen in worlds that $A$ happens. So the ratio $\frac{P(B\|A)}{P(B)}$ is less than one. This means that our posterior probability of $A$ is lower than than our prior probability.

$$P(B|A) < P(B) \longrightarrow P(A|B) < P(A)$$

In our example, we have that $P(B\|A) > P(B)$. Grey skies are more likely to happen on days when it rains than a randomly-selected day (or equivalently, grey skies are more likely to happen on days when it rains than on days where it doesn't rain). So we update towards rain being more likely to happen and go grab our umbrella.

If you notice, I use a lot of phrasing like "the probability that *we would give*" versus "the probability that". Bayes theorem is most
natural to interpret when you consider "the probability it's going to rain later today" to be a property of the model in your head, rather
than an "objective" fact about the weather. When we encounter evidence, it's the model in your head that's
evolving over time. This is the sense I mean when I say that Bayes theorem tells you how the "subjective" probability that you give
changes over time.

But also notice: while Bayes theorem can't tell you what correct probabilities to assign to $P(A), P(B), P(B\|A)$, and $P(A\|B)$, it imposes
a self-consistency condition on what values you can assign to all four simultaneously. This is important because a common critique of
using Bayesian statistics is that there is no "correct" prior. How do you know whether a priori there is a $5 \%$ chance it's going to rain? Or  a $20 \%$ chance? This is a valid critique. But what Bayes theorem does tell you is that if $P(B\|A) > P(B)$, then your posterior *must* be higher than your prior. Otherwise, your system of beliefs isn't internally consistent.