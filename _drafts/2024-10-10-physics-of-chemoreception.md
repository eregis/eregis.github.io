---
layout: post
title: "Physics of Chemoreception"
date: 2024-10-12
mathjax: true
---
For my first reading assignment, my research advisor gave me a classic paper in the field of bacterial chemotaxis 
called 'Physics of Chemoreception' [Physics of Chemoreception](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1473391/).

Chemotaxis is the process by which organisms use chemicals in the environment to navigate. 
The field of bacterial chemotaxis (specifically with E. coli) is one of the largest in all of biophysics, 
and the father of bacterial chemotaxis is Howard Berg. He passed away just a couple of years ago.

In order to perform chemotaxis, E. coli sense chemicals in the environment using receptors. 
A basic question you could ask is: how well, on purely physical grounds, 
should you expect E. coli to be able to measure the chemical concentrations around it? 
The gist of how chemoreception works is that if the intended molecule makes contact with the receptor, 
it will bind to the receptor, which will be transduced into some chemical messenger within the bacteria. 
So the more receptor binding events, the higher the estimated concentration of outside ligand.

But ligand binding events have an element of randomness. 
While we can talk about the average concentration of ligand in the environment, 
at any given time, there will be local fluctuations in the ligand concentration 
due to the randomness of diffusion. 

(This is not even taking into account other sources of randomness like the fact that not all ligand-receptor
collisions lead to binding events or that the amount of time that the ligand spends bound to the receptor is random.)

Given some average ligand concentration $M$ in the
environment, in any given subvolume, the number of ligands within that subvolume will be distributed according
to the Poisson distribution. The Poisson distribution is a one-parameter family of probability distributions
which is uniquely determined by the mean count (which can be interpreted as the "true" rate of the population
being sampled from). In this case, the mean count is equal to the concentration of ligand
multiplied by the volume of the region: $MV$.

$$P(N) = \frac{e^{-MV} (MV)^N}{N!}$$


As both the mean and the variance of a Poisson distribution are equal to the rate parameter (here $MV$),
the coefficient of variation (CV) of the Poisson distribution goes as the inverse-square root of $MV$.

$$\text{CV}_\text{Poisson} = \frac{\sigma}{\mu} \propto \frac{1}{\sqrt{V}}$$ 

That means that the larger the volume that you sample from, the better your estimate of the concentration. 
So reducing the error can be phrased in terms of increasing the effective volume which the E. coli is sampling over.

How do you increase the effective sampling volume? One way is to increase the cross sectional area of the receptor.
Another way is to increase the number of receptors on the E. coli, making sure that they are spread out evenly
over the surface of the bacteria in order to minimize the effect of spatial correlations in concentration. 
Another way is to lengthen the "integration time": the amount of time that the E. coli spends counting binding 
events before making a best guess at the concentration. (Excuse the anthropomorphic language.)
The longer the E. coli collects data (ligand binding events), the more accurate its estimation of
the concentration will be.

But we are not dealing with a hypothetical sensing apparatus, but an actual organism. We can see (roughly) how many receptors
repectors a typical E. coli has and the approximate size of each of these receptors. And E coli don't just want to know 
the concentration accurately, but they also want to learn it *quickly*. In the real world, 
the concentration of ligand is not static. In order to effectively make decisions, the E. coli needs to be able to
adapt to changes in concentration over time (in order to navigate towards higher concentrations in the case of
attractants or towards lower concentrations in the case of repellants). E. coli move by alternating between
runs (moving forward in a straight line) and tumbles (randomly spinning themselves around to change direction). Runs 
are on average about a second long, which gives a rough time scale for how long previously acquired information
remains informative.

Given these empirical constraints---the number of receptors, their size, and the maximum integration time--how
well could E. coli theoretically measure ligand concentrations?


It turns out you only need a small fraction of the area of the Ecoli covered in order to sense the concentration


It's a brilliant paper that is a perfect example of what is beautiful about biophysics. It's central result relies
on a really clever physical analogy due to similar form of the diffusion equation and Poisson's equation. But the
main result also has a nice and tidy physical explanation (that molecules will tend to hover in the vincinity 
of the radius of the sphere for an extended period of time, allowing multiple chances to hit a receptor).