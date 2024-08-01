---
layout: post
title: "A Framework for Thinking About Information Processing"
date: 2024-07-31
mathjax: true
---

Let's do some high-level brainstorming for a research project that I am working on.

The question that was being investigated is: Is E coli information-limited? That means, is the information that E coli represents in terms of its internal activity being used efficiently to climb the gradient?

There are four parts that need to be modeled:

    The signal (here the derivative of the log concentration)
    Behavioral response: Run-and-tumble navigation where the tumble rate is a function of signal history
    Performance: the drift speed up the gradient
    Information: given by the transfer entropy rate from the signal to the "motor" (run or tumble).

This seems to me (as a second-year graduate student who is new to the field) a very general framework of approaching these types of questions. I am interested in thinking about how I could use this framework to ask further questions about Ecoli or perhaps ask questions about other organisms.

What parts of this can be modified?

For example, is there some better model of the "signal"? Something I remember reading is that the mutual information is invariant under deterministic transformations, so it probably doesn't matter if you have the signal be the time derivative of the log concentration or the log concentration itself; choosing the right functional representation of the signal probably just helps with physically interpreting what is going on (e.g if there is some sort of kernel function)

What about in other organisms? I would guess that we should think broadly in terms of the different types of sensory inputs. In cellular organisms, I would guess that this is most neatly studied in terms of receptors as we have e.g Burg and Purcell math to be able extract an approximation for the amount of information that should be encoded in the signal. What else? I would guess this could also be done for gene transcription networks? (I've seen some analysis along this vein by Pankaj Mehta, I believe). The physics there would still be binding-and-unbinding, so I would assume that this could be considered as a subset of receptor-type transductions models. I can't think of any other physical model of the signal that is relevant for bacteria. In neurons, there is I believe (don't know any neuroscience) signal that can be represented as electric activity.

What about in other organisms? It would seem to get trickier to study this questions as you get to more and more complex organisms. Purely at the level of the signal, the information content would be hard to quantity. For microbiology, as I mentioned before, a lot of the transduction reduces down to some counting-molecule problem. How would one study information transfer in mice? I have done zero reading into this, and it's not relevant to my lab (which studies bacteria and flies), but I'm curious what work has been done here.

    In terms of behavioral response, is there anything better than run-and-tumble motion? Not that I am aware of, personally. I should probably spend a bit more time familiarizing myself with the microbiology, rather than being satisfied with my comfort zone of stochastic processes, information theory, and probability theory, but based on just osmosis and vibes of being in the lab among biologists by training, at a high-level, it seems that bacteria really can be modeled as a two-state system. Though now that I mention it: there was discussion about how it could perhaps be better described by a three state system: run, tumble, and then a transitory phase from run to tumble (because I think the motivation is that the transitory phase is "stereotyped"/has some characteristic time duration that is not well-described by exponentially-distributed transition rates; but this seems like the sort of complication that doesn't pay for itself in the end.)

The other, more nitty-gritty/substantive part is the one that is the details of how we are representing the run-and-tumble motion. The main features of the information-limited model is: 

(1) During both runs and tumbles, bacteria experience rotation diffisuion
(2) During tumbles, bacteria don't move, and experience higher rotational diffusion than during tumbles.
(3) The "run rate" (probability per unit time of transitioning from tumble to run) is not a function of the signal history
(4) The percent change in the tumble rate is a linear functional of the signal history

The first three points are shown by experimental data to be approximately true--again, haven't deeply checked this, but it's not where my main interest lies. The fourth point is interesting and one that I am mulling over a bit. My advisor says that it comes from an Arrhenius equation for the motor switching that becomes linearized in the shallow gradient regime. And that \lambda_R0 is somewhat subtle, constituting an "effective" average over stochastic effects. I might write more about this later.

What about with other bacteria? While the main bacteria of choice in my lab is E coli, we are also starting to look at Vibrio Cholera using some of the same sort of microscopy techniques that we have been using to study Ecoli (my lab is mostly an experimental biology lab though we have a couple theoreticians.) Vibrio cholera has an interesting behavioral pattern; would it be plausible to do "Cholera is information limited?" Or is that too lazy/derivative? 

There probably might not just be the right experimental data. The original information limited was enabled by a set of experiments that were performed within lab that allowed us to constrain some of the various free parameters within our model (the original paper was a dual first-authorship I believe--one theoretician, one experimentalist). And the project that I am working on now was motivated by my advisor by some new experiments that have been performed in the intervening years.

    Performance. Is there some other better performance metric? Probably not hugely better. This is where not knowing as much biology limits how insightful I can be. I have this gestalt impression that organisms should be simultaneously optimizing a multitude of objectives, such that conducting the analysis under the assumption of a single objective must be an oversimplification. But the headline result was the E coli are actually pretty close to climbing the gradient optimally given their biochemical constitution--so I guess that confirms that we chose the right objective function after all? Are there other high-level objectives that other organisms try to acheive? This isn't a rhetorical question. I genuinely don't know. The fly people in my lab have the objective of finding the odor source--which seems spiritually very similar. So it could be just a really common abstract goal that organisms have to solve; Or it could be a searching-for-keys-under-streetlight situation. Hard for me to say without reading more literature.
    Hmm this is interesting as it's the only purely mathematical question: is there a better way to quantity our intuitive notion of "information" other than the entropy transfer rate? I feel distinctly unqualified to approach this question. It would involve clarifying broad questions like "What is information?" Again: this seems to be where looking at the broader information transfer literature would be my friend. But based on my perusals so far, everything I've seen has been some variant of the mutual information, so I will lean towards "No" for now.