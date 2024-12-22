---
layout: post
title: "Order Statistics Explained"
date: 2024-12-06
mathjax: true
---

Imagine that you are a tech company looking to hire a software engineer. Money is tight, so you are only looking to hire the very best.
For simplicity, imagine that your interview process is perfect: you can perfectly deduce the exact ability level of the engineer
that you are interviewing. And that if you extend an offer, then the person will definitely accept the offer.

Let's say that coding ability is normally-distributed among the applicant pool. You want to hire an engineer that is 2 standard
deviations above the mean. How many people should you interview? Interviews cost money. You have to process the paper work for each
applicant, and your best engineering talent has to take time out of their busy days to properly evaluate the applicants. You want
to interview as few people as possible while still having a high probability that the person you end up hiring meets your standards.

If you only interview a single person, then clearly that's not going to work. If you are drawing at random from the distribution of talent, then the person will be (by definition) be expected to be average.

On the other hand, interviewing every person in the world is clearly overkill. The best programmer in the world is over 6 standard deviations above the mean in coding ability. You're not looking for John Cormack or anything. You just need a competent
developer to help maintain your backend infrastructure.

So one person is too few and 8 billion is too many. Our intuition is that the more people you interview, the better the best person 
you interview is. But quantitatively, how does the distribution of the best person you interview change as a function of the number of people you interview.

Let's start simple and ask: if you interview two people, what is the probability that the better of the two people is one standard deviation above the mean in ability. This is one of those situations where it's actually better to think in terms of the complement: what is the probability that the *neither* of the two people are less

We will let $p(x)$ be the PDF of the standard normal distribution and $P(x)$ be the cumulative distribution function. Recall that
the cumulative distribution functions $P(x)$ tells you the 

$$P(x) = \mathbb{P}\{\}$$