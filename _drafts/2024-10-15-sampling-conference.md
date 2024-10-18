---
layout: post
title: "Recent Advances and Future Directions for Sampling"
date: 2024-10-17
mathjax: true
---

A couple weeks ago, the professor for my Statistical Optimal Transport class said that there would be a conference on sampling
happening at Yale over the fall break. The time was fortuitous; I've been engrossed in reading my professor's books and papers,
but his perspective is of course limited. Attending this conference would give me a better idea of the field as a whole.

# Day 1

On Day 1, the conference took place at 14th floor of Klein Tower, Yale's largest academic building. The 14th floor is the faculty lounge,
but it doubles as a nice venue for conferences, department holiday parties, and expos. It's gorgeous: there is 
a large room where main events take place, and there are ceiling high windows surrounding the room, giving you
an unparraleled view of the surrounding campus.

Courtesy of being a Yale graduate student, my registration fee for the conference was waived. My goal for the
conference was to expose myself to this new subfield. The invited speakers were academics chosen by Sinho Chewi
and Andre Wibisono, two Yale faculty members whose work I've been reading over the past couple weeks. I trust
their judgement in terms of whose work to expose myself to. I had the secondary goal of socializing and "networking".
But this is always a pipe dream I'm afraid. I always go into conferences with the goal of being a Fake Extrovert
before inevitably burning out and finding a nice dark corner to listen to music. (This happened this time too.)

The topics covered in Day 1 felt broad, befitting a conference which claims to be on sampling. Because of the small
nature of the conference (I would guess somewhere between 40 and 50 attendees), the entire conference was split
between two rooms (and connecting hallways): one room for the current speaker and another room for food and beverage.

Again, I'm not familiar with sampling as an academic field, but there definitely seemed to be a flow to the
presentations. The morning was focused on Markov Chain Monte Carlo. The first speaker was Gareth Roberts who has 
been doing work MCMC at least since the 90s (if not earlier). Sinho Chewi even credited him with being one of 
the people who originally got him into the field. While the meat of the talk didn't quite make sense to me, I did get
exposure to some cool ideas in MCMC. One was non-versible Markov Chains. In more traditional MCMC algorithms,
the Markov chain (whose stationary distribution is the target distribution) is reversible: for any sequence of points visited
by the chain, the reversed sequence is equally probable. (This property is also known as detailed balance.) But this behavior
is ultimately diffusive which can a bit too slow depending on the context. So under certain conditions, non-reversible algorithms
can outperform reversible ones by allowing them to explore the state space more quickly. He also provided the first clear explanation
of simulated tempering: a way to handle sampling when you have a multi-modal distribution. Naive algorithms struggle with probability landscapes with local minima, so there are many research programs dedicating to coming up with different answers to the question.
I've come across simulated tempering before in the context of machine learning, but I had never seen the mathematical formalism
before, and to my pleasant surprise, it was pretty approachable. I didn't have the same luck with parallel tempering, unfortunately.

I also really enjoyed the talk of Dan Lacker, a professor at Columbia. In terms of the presenters I saw on Day 1, his work was
the most closely aligned with what I find interesting. His work involved entropic optimal transport (optimal transport but with an entropic cost term) and also variational inference. (So rather than simply finding the optimal distribution over the space of all coupling, you limit yourself to some subset e.g. the Bures-Wasserttein space (space of Gaussians) or the product measure (spac)).
He brought up the Schrodinger's gas experiment, which I had heard before mentioned in class, but it didn't conceptually click with me
until I read this. My understanding is that Schrodinger imagined: if you have a gas in one state and then some time later the gas is in 
another state (by diffusing, let's say), what is the likely intermediate state of the gas. Nowadays, we can recognize the connection
with optimal transport and stochastic differential equations. But Schrodinger proposed his thought experiment without all of that 
mathematical machinery.

The early afternoon talks had to do with graphs. Then the last couple talks were on diffusion models. I understand the basic conceptual idea of diffusion models, but I'm really interested in learning how they work on a more technical level. One of the papers that 
got me to start looking in the direction of this field---Renormalizing Diffusion Models by Jordan Cotler and Semon Rechnikov---analogies 
reversing the renormalization group transformations from low-energy to high-energy as what a diffusion model does, trying to learn
the inverse process for diffusion.

One thing that stood out to me was just how useful my physics background was for quickly understanding what was "really" going on with
many of the different sampling techniques. Whether's it's Hamilton Monte Carlo or Donsker-Varadhan variational representation,
being able to analogize the language of sampling and statistics back into physics never stopped being useful.

What's nice is how interdisciplinary sampling is as a discipline. I already mentioned how helpful physics is for interpreting the various
sampling algorithms. But the various professors I talked to were from many different departments. There were the staticians, obviously. But also a lot of CS people, applied mathematicians, and even the odd engineer.

# Day 2

This was a tougher day for me. The previous day of conferencing took a lot out of me. The the mental strain of following along 
the technical talks, the fake extroverting, and the schmoozing with other academics at the banquet while trying not to talk
with my mouth full of cheese-filled baked potato---it all took a lot out of me.

The second day of the conference wasn't at the 14th floor, but the 13th floor. Still a nice space, but not the expansive venue.
I stumbled in around 10:30 AM, half way through the keynote speaker's talk. I didn't want to interrupt, so I watched the talk in the dining room where the talk was being livestreamed on a huge flat screen TV. I didn't seem to have missed much; the talk was fairly 
technical. I couldn't make out what it was about halfway through, but I recognized standard notion like the Dirichlet energy, log-Sobolov
inequality, etc that I had been exposed to in my Statistical Optimal Transport Class.

The afternoon talks seemed to be focused on different modifications of Hamilton Monte Carlo. "Normal" Monte Carlo is all about creating a Markov chain whose stationary distribution is the target distribution. Hamiltonon Monte Carlo has a "position" space which represents the original space and then also a momentum space which (analogusly). Physically, it replaces the first-order equation of normal Monte carlo (where gradients of the potential directly affect the transition) with a second-order equation. The idea is that the marginal distribution
where you integrate out the momentum degrees of freedom should get you your target distribution. I'm quite new to Hamilton Monte Carlo (like, I learned about it last week levels of new), so I don't understand in detail what it has to offer over normal MCMC methods.

A lot of the talks seemed centered around a modification of Hamilton Monte Carlo called NUTS which stands fo No U-turn Sampling.
There is an explanation here (https://stats.stackexchange.com/questions/311813/can-somebody-explain-to-me-nuts-in-english), though 
I can't pretend to understand the core insight behind why its better than normal HMC. There was a talk given by Bob Carpenter on GIST
which from what I gathered is a general framework for understand HMC under variable time step, length of sample, etc which has NUTS
as a special case. This is important as working in the GIST framework allows you to understand various theoretical guarantee better
than working with NUTS directly (that's my hazy recollection of the talk; errors are mine). This was super neat as my first introduction
to academic statistics was Andrew Gelman's blog. And Bob Carpenter is a frequent guest blogger. It was cool to finally see him in the flesh.

This is weird and specific, but one weird thing was seeing so many experts roughly the same age as me. The conference skewed fairly 
young, not only in terms of the composition of graduate students versus professors, but also among the professors themselves. A *lot*
of the professors both that I talked to and that were giving presentations were assistant professors in the first couple years of their 
position. There was something sort of eerie about people in their late twenties and early thirties going up to front of the room
and commanding it like that. 