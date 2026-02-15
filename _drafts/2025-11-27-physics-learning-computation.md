---
layout: post
title: "Physics of Learning and Neural Computation"
date: 2026-02-03
mathjax: true
---

A couple months ago, someone in my lab shared a really helpful-looking resource on the Slack channel: a website called [Physics of Learning and Neural Computation](https://www.physicsoflearning.org/). It's a collaboration of notable researchers who work at the intersection of physics and machine learning. The collaboration is directed by Surya Ganguli, a Stanford Applied Physics professor. Ganguli has made many contributions to the machine learning literature, including being the last author on the paper that introduced the now-ubiquitous diffusion models: [Deep Unsupervised Learning Using Non-Equilibrium Thermodynamics](https://arxiv.org/abs/1503.03585). 

It brands itself as a Simons collaboration (so affiliated with the Simons Foundation). The Simons Foundation was founded by mathematician and finance person Jim Simons (notable in mathematics for advances like Chern-Simons theory and in finance for Renaissance Technologies). The Simons Foundation sponsors a lot of work in this type of vein: they specialize in interdisciplinary work that incorporates perspectives from multiple different STEM fields, especially work with a computational flavor. It is a natural home for work at the physics-ML intersection, which draws on statistical mechanics, information theory, and dynamical systems to understand how neural networks learn and generalize.

The website's summary of the contributions that physics has made to understanding artificial intelligence is quite good:

> Indeed ideas from the physics of complex systems have long played a profound role in the development and analysis of machine learning and neural computation, ranging from the Hopfield model and Boltzmann machine (2024 physics Nobel prize), and the understanding of optimization dynamics and geometry in high dimensional disordered systems (2021 physics Nobel prize), to more recent advances in the discovery and analysis of scaling laws, and the inspiration of nonequilibrium statistical mechanics for diffusion models in generative AI.

On the team page, you can see a list of principal investigators and affiliates. They are organized into principal investigators, affiliates, and collaborators.

- **Principal Investigators**
  - Yasaman Bahri
  - Maissam Barkeshli
  - Miranda Cheng
  - Michael Douglas
  - Surya Ganguli (Director)
  - James Halverson
  - Julia Kempe
  - Florent Krzakala
  - Yann LeCun
  - Alex Maloney
  - Brice Ménard
  - Cengiz Pehlevan
  - Irina Rish
  - Bernd Rosenow
  - Eva Silverstein
  - Matthieu Wyart
  - Lenka Zdeborová

- **Affiliates**
  - Paul Ginsparg
  - Andrey Gromov
  - Jared Kaplan
  - Dmitry Krotov
  - Dan Roberts
  - Yuhai Tu

- **Collaborators**
  - Francesco Cagnetta
  - G. Bruno De Luca
  - Christian Ferko


Helpfully, the website is running a series of survey lectures where principal investigators give an hour-long lecture on some of their research. These are recorded and can be found on the website or the associated YouTube channel. As usual with these style of blog posts, I will briefly go over some of the survey lectures to give a flavor of the type of work that people are doing. (And the usual caveats apply that explaining other people's work simply is difficult, so hopefully no terrible mistakes or oversimplifications creep in.)

## Cengiz Pehlevan - Mean-field theory of deep network learning dynamics and applications to neural scaling laws

[Link to lecture](https://youtu.be/A9V_VEkgkGE?si=itAqpXUlv8dX0DAl)

> I will review recent developments in obtaining a mean-field description of the high-dimensional learning dynamics of deep neural networks. These mean-field theories result from various infinite limits, including width, depth and attention-heads. I will present applications of these ideas to neural scaling laws in lazy and feature-learning regimes.

Mean-field theory descriptions are a very physical picture of the dynamics of neural network training.

The picture of mean-field theory goes roughly like this: Over the course of training, the parameters of the network will descend via gradient descent to minimize the loss function. Instead of imagining the parameters of the network as a whole, you can imagine each set of parameters associated with a neuron as a set of coupled equations. The loss function is like a Hamiltonian, and the fact that the loss function isn't separable in neurons means that neurons are coupled—akin to how particles interact via forces.

For a finite number of neurons this is all very complicated. But in the limit as $N$ goes to infinity, you can actually replace the complicated set of coupled equations with a probability density over the weights. And the distribution over neurons will move deterministically to minimize the loss function, allowing you to describe the evolution of the probability distribution analytically.

The set-up Pehlevan uses here is a bit different though. He uses something called "dynamical mean field theory" (DMFT). Rather than tracking a probability density over the neurons directly, DMFT tracks order parameters that summarize the state of the network at each point in time. From [the associated paper](https://pehlevan.seas.harvard.edu/sites/g/files/omnuum6471/files/pehlevan/files/bordelonpehlevan_ml4phys_neurips_2022.pdf), the order parameters are things like the kernel matrix (capturing the similarity structure of the network's representations) and various correlation functions between layers. The key insight is that in the infinite-width limit, these order parameters evolve according to deterministic differential equations, even though the individual weights are random. This gives you a tractable description of learning dynamics that would otherwise be intractable.

The payoff of all this machinery is that you can derive neural scaling laws—the empirical observation that test loss decreases as a power law in the amount of data and model size. By analyzing the mean-field equations, you can predict the exponents of these scaling laws and understand when the network is in the "lazy" regime (where features don't change much during training) versus the "feature-learning" regime (where the network adapts its representations to the task).


## Julia Kempe - Synthetic Data: Friend or Foe in the Age of Scaling?

[Link to lecture](https://youtu.be/x3DrcQs3Lk8?si=Pl0Ttc4b6elOwq-b)

> As AI model size grows, neural **scaling laws** have become a crucial tool to predict the improvements of large models when increasing capacity and the size of original (human or natural) training data. Yet, the widespread use of popular models means that the ecosystem of online data and text will co-evolve to progressively contain increased amounts of synthesized data.

This is an interesting challenge facing the training of neural networks, and it has two faces---one concerning, one potentially helpful.

The concerning face is this: AI models are trained on Internet data, but increasingly, Internet data consists of text generated by LLMs. This could lead to a host of issues, some hilarious and some more serious. On the hilarious end, I recall that there used to be an issue where LLMs from labs other than OpenAI would think that they were ChatGPT. It was speculated that because ChatGPT was the dominant AI agent in the training data, it ended up being an attractor in persona space—the model collapsed toward the most common AI persona it had seen. On the more serious side, the outputs of LLMs are not "high quality" in the sense that they aren't entangled with reality in the way that we would desire for high-quality training data. It's hard to formally explain in my own words why training an LLM on LLM-generated data would be bad—phrases like "low entropy" and "mode collapse" get thrown around—but empirically it does seem to be a problem. The intuition is something like: LLM outputs reflect the statistical regularities of language without the grounding in actual experience that human-generated text has, so training on them amplifies the artificiality.

The potentially helpful face is this: can we use synthetic data to supplement any coming data scarcity concerns? While it seems that frontier labs are not scaling quite as vigorously as they used to, there will still likely be a trend toward training bigger models, and that will require more data. At some point we may exhaust the supply of high-quality human-generated text on the Internet. It might be necessary to (with careful engineering) create synthetic text for LLMs to train on. The key question becomes: under what conditions does synthetic data help versus hurt? This is the kind of question that admits a rigorous, physics-style analysis—you can study how the properties of the synthetic data distribution affect the learned model, and derive conditions for when augmentation is beneficial.

## Miranda Cheng - GUD: Generation with Unified Diffusion

[Link to lecture](https://youtu.be/A2IWWceVbpk?si=-5ZXT0QqPnWZv2oY)

> We present the GUD model, a unified diffusion model interpolating between standard diffusion and autoregressive models. Inspired by concepts from the renormalization group in physics, which analyzes systems across different scales, we revisit diffusion models by exploring three key design aspects: 1) the choice of representation in which the diffusion process operates, 2) the prior distribution that data is transformed into during diffusion, and 3) the scheduling of noise levels applied separately to different parts of the data, captured by a component-wise noise schedule. Incorporating the flexibility in these choices, we develop a unified framework for diffusion generative models with greatly enhanced design freedom.

Diffusion models and the renormalization group share similar high-level structure, though there are interesting wrinkles and differences once you get down to the technical details.

The similarity is this hierarchical picture: with renormalization, you integrate out the high-frequency (short-wavelength) degrees of freedom, until only the low-frequency (long-wavelength) physics is left. You're coarse-graining the system, zooming out, losing the fine details while preserving the large-scale structure. If you were to invert a renormalization flow, you would start with low-frequency physics and build your theory back up to include higher and higher frequencies—you'd be adding back the fine details.

In reverse diffusion, something similar happens. The forward diffusion process progressively destroys information by adding noise, and the high-frequency details (sharp edges, fine textures) are the first to go. When you run the process in reverse to generate an image, the high-level aspects of the image come in first—the overall composition, the rough shapes—and then finer and finer details get clarified over the course of the reverse diffusion process. It's as if you're running an inverted RG flow, progressively adding back the short-wavelength structure.

What Cheng and collaborators do with GUD is take this analogy seriously and ask: what design freedoms does this perspective reveal? Standard diffusion models make particular choices about the noise schedule (how quickly you add noise at each step), the representation (pixel space vs. frequency space), and the prior (pure Gaussian noise). But these choices aren't fundamental—they're just one point in a larger design space. By thinking in terms of scale hierarchies, you can design diffusion models that interpolate between the standard approach and autoregressive models (which generate one token at a time in a fixed order). The renormalization group perspective provides a unifying language for understanding this whole family of generative models.

## Maissam Barkeshli - Sharpness Dynamics in Neural Network Training

[Link to lecture](https://youtu.be/mZ_DpkL95os?si=2O5YTZGpHdGd8hj8)

> In this talk I discuss certain robust, universal phenomena that appear when tracking the top eigenvalue of the Hessian of the loss, which we refer to as the sharpness. The sharpness tracks the local geometry of the training loss landscape and plays a key role in determining the maximal allowable learning rate. It is also conjectured to play an important role in generalization capability. I will demonstrate how sharpness exhibits various universal phenomena during early, middle, and late stages of training across architectures and tasks, and how this phenomena can be understood through the lens of a simple toy model. I will also show how sharpness provides an important lens into understanding the underlying mechanisms of learning rate warmup, and how to make it more efficient.

This talk centers on the phenomenon of "edge of stability." Edge of stability is the empirical observation that during training, the sharpness (the largest eigenvalue of the Hessian—which is the second derivative of the loss with respect to the parameters) hovers at a critical threshold determined by the learning rate.

The intuition is this: because we are taking finite-sized steps during gradient descent, our algorithm can't converge when the loss landscape becomes too curved. If the curvature (sharpness) is too high, then when you try to take a step downhill to minimize the loss, you will instead overshoot and bounce to the other side of the valley. The critical sharpness is $2/\eta$ where $\eta$ is the learning rate—above this threshold, gradient descent becomes unstable.

What's surprising is that in practice, neural networks train right at this edge. The sharpness rises until it hits the stability threshold, and then it hovers there, occasionally exceeding it and causing the loss to temporarily increase before settling back down. This is a self-organized criticality of sorts: the dynamics of training naturally push the system toward the edge of instability.

Barkeshli and collaborators characterize the different phases of this edge-of-stability dynamics. They find that training alternates between phases with rising sharpness and decreasing loss (the network is learning and the landscape is becoming more curved) and phases with decreasing sharpness and rising loss (the network has become unstable and is readjusting). Understanding these phases has practical implications—for instance, it explains why learning rate warmup (starting with a small learning rate and gradually increasing it) is helpful. If you start with too large a learning rate, you'll immediately hit instability before the network has had a chance to find a good region of the loss landscape.