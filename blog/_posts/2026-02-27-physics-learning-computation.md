---
layout: post
title: "Physics of Learning and Neural Computation"
date: 2026-02-27
mathjax: true
description: "An overview of the Physics of Learning and Neural Computation collaboration and its survey lectures on synthetic data, diffusion models, and edge of stability."
keywords: physics of learning, neural computation, Surya Ganguli, Simons Foundation, synthetic data, diffusion models, renormalization group, edge of stability, machine learning
---

A couple months ago, someone in my lab shared a really helpful-looking resource on the Slack channel: a website called [Physics of Learning and Neural Computation](https://www.physicsoflearning.org/). It's a collaboration of notable researchers who work at the intersection of physics and machine learning. It's directed by Surya Ganguli, a Stanford Applied Physics professor who has made many contributions to the machine learning literature, including being the last author on [the paper that introduced the now-ubiquitous diffusion models](https://arxiv.org/abs/1503.03585). 

It brands itself as a Simons collaboration (so affiliated with the Simons Foundation). The Simons Foundation was founded by mathematician and finance person Jim Simons (notable in mathematics for advances like Chern-Simons theory and in finance for Renaissance Technologies). The Simons Foundation sponsors a lot of work in this type of vein: they specialize in interdisciplinary work that incorporates perspectives from multiple different STEM fields, especially work with a computational flavor. It is a natural home for work at the physics-ML intersection, which draws on fields such as statistical mechanics and dynamical systems to understand how neural networks learn and generalize.

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


Helpfully, the website is running a series of survey lectures where principal investigators give an hour-long lecture on some of their research. These are recorded and can be found on the website or [the associated YouTube channel](https://www.youtube.com/@PhysicsofLearning). Some of the lectures include:

### Julia Kempe - Synthetic Data: Friend or Foe in the Age of Scaling?

[Link to lecture](https://youtu.be/x3DrcQs3Lk8?si=Pl0Ttc4b6elOwq-b)

> As AI model size grows, neural **scaling laws** have become a crucial tool to predict the improvements of large models when increasing capacity and the size of original (human or natural) training data. Yet, the widespread use of popular models means that the ecosystem of online data and text will co-evolve to progressively contain increased amounts of synthesized data.

This is an interesting challenge facing the training of large language models (LLMs). LLMs are trained on data from the Internet, but the Internet is increasingly being filled with the outputs of other LLMs. What happens when the ouroboros starts to eat its own tail?

This is already happening to some extent. I recall that there used to be a hilarious issue where [LLMs from labs other than OpenAI would mistakenly think that they were ChatGPT](https://eval.16x.engineer/blog/llm-identity-crisis-models-dont-know-who-they-are). It was speculated that because ChatGPT was the most prevalent AI in the training data, it ended up being an attractor in persona space---the other LLMs collapsed toward the most common AI persona they had been trained on. 

More seriously, the outputs of LLMs are not "high quality" in the sense that training another model on the uncurated output of other LLMs will result in a less capable model. 

During pre-training, LLMs are trained on next-token prediction: given a chunk of text, their job is to predict what the next token will be. This learning paradigm is called *self-supervised learning* because it cleverly turns an unsupervised task into a supervised one. The underlying goal is unsupervised: the LLM wants to learn the structure of the data---the distribution of natural language. And in a paragraph of text there is no obvious "input" and "output" as you would have in something like digit classification. But you can reformulate this as a supervised learning task by asking the LLM to learn the function: "Given the previous sequence of tokens, what is the most likely next token?"---a well-defined problem with input-output structure, amenable to standard supervised training.

The reason next-token prediction works so well is that once the LLM has learned the easy patterns, the best way to get better at predicting text is to actually understand the world the data came from. This is what demarcates high-quality data from low-quality data: high-quality data is entangled with reality, meaning it is more likely to be produced in the real world than in alternative possible worlds. While LLMs are clearly more than stochastic parrots at this point, it does seem true that human output is more semantically-grounded than comparable LLM output.

This is all difficult to formalize properly---people throw around phrases like "low entropy" and "mode collapse" to explain why, even though LLMs are quite capable as next-token predictors, they still aren't truly generating the same distribution of text as humans do. But empirically, training on LLM-generated data does seem to degrade model quality.

But there are also reasons to be optimistic. Currently, LLMs are being trained on a *massive* portion of the text on the Internet—and there are concerns about novel data sources running out. But could it be possible to use synthetic data (text generated by an LLM) to ameliorate any forthcoming data scarcity concerns?

### Miranda Cheng - GUD: Generation with Unified Diffusion

[Link to lecture](https://youtu.be/A2IWWceVbpk?si=-5ZXT0QqPnWZv2oY)

> We present the GUD model, a unified diffusion model interpolating between standard diffusion and autoregressive models. Inspired by concepts from the renormalization group in physics, which analyzes systems across different scales, we revisit diffusion models by exploring three key design aspects: 1) the choice of representation in which the diffusion process operates, 2) the prior distribution that data is transformed into during diffusion, and 3) the scheduling of noise levels applied separately to different parts of the data, captured by a component-wise noise schedule. Incorporating the flexibility in these choices, we develop a unified framework for diffusion generative models with greatly enhanced design freedom.

The renormalization group and diffusion models are two ideas from different areas of science (the renormalization group comes from theoretical physics; diffusion models come from machine learning) that nonetheless have various thematic similarities---though there are interesting differences once you get down to the technical details.

The renormalization group is an apparatus for understanding how the physics of a system changes as a function of scale. In a renormalization group flow, you integrate out the high-frequency (short-wavelength) degrees of freedom until only the low-frequency (long-wavelength) physics is left. Renormalization is commonly used in both statistical field theory and quantum field theory.

Diffusion models are a generative modeling paradigm for generating new samples from a data distribution of your choosing (e.g. the distribution of natural images). During training, you gradually add noise to a sample. The training task for the diffusion model is to denoise the corrupted version of the image to recover the original sample. Then during inference, you can give the diffusion model random pixel noise and it will attempt to denoise it---effectively drawing a sample from the distribution of images it was trained on.

Renormalization and diffusion models are similar in that both are based on the idea that complex objects can be decomposed hierarchically into different aspects at different scales. 

In renormalization, we talk about UV physics (high-frequency) and IR physics (low-frequency). When coarse-graining, you lose the fine details of the theory while preserving the large-scale structure. If you were to invert a renormalization group flow, you would start with the low-frequency physics and build your theory back up to include higher and higher frequencies---finding the UV theory associated with an IR theory. 

In a diffusion model, the forward noising process progressively destroys information, and the high-frequency details---sharp edges, fine textures---are the first to go. When you run the process in reverse to generate an image, the high-level aspects come in first---the overall composition, the rough shapes---and then finer and finer details get filled in over the course of the reverse process. One possible explanation for why diffusion models work so well is that by learning a dynamic denoising process, the model effectively learns the distribution at different scales, corresponding to different points in the noising process. And this might somehow be easier than trying to learn the whole image distribution at once.

There are important mathematical and conceptual differences between renormalization and diffusion though. One difference is what we take as the independent variable. Renormalization is a transformation over *scale*, not time. While you can conceptualize coarse-graining as a process of "zooming out", we typically don't think of renormalization as something that happens to a system over time---it's a parametric family of descriptions that are all simultaneously true, depending on what scale you view the system at. In diffusion, by contrast, the process is explicitly happening over time.

Another difference is the fundamental mathematical object. In diffusion, we care about the evolution of the probability measure over time. The dynamics can be described by an SDE whose marginal distribution at each time point matches the correct target marginal. By constrast, in renormalization we are more interested in the potential that generates the Gibbs measure---specifically, the coupling constants of key terms in the potential that we track over the course of renormalization. The evolution of the theory is described by an ODE for the coupling constants.

### Maissam Barkeshli - Sharpness Dynamics in Neural Network Training

[Link to lecture](https://youtu.be/mZ_DpkL95os?si=2O5YTZGpHdGd8hj8)

> In this talk I discuss certain robust, universal phenomena that appear when tracking the top eigenvalue of the Hessian of the loss, which we refer to as the sharpness. The sharpness tracks the local geometry of the training loss landscape and plays a key role in determining the maximal allowable learning rate. It is also conjectured to play an important role in generalization capability. I will demonstrate how sharpness exhibits various universal phenomena during early, middle, and late stages of training across architectures and tasks, and how this phenomena can be understood through the lens of a simple toy model. I will also show how sharpness provides an important lens into understanding the underlying mechanisms of learning rate warmup, and how to make it more efficient.

I wrote a [previous post on edge of stability](/blog/2025/09/08/edge-of-stability) that goes into more detail, but the basic idea is this: during gradient descent, the sharpness (the largest eigenvalue of the Hessian) tends to rise until it hits the critical threshold $2/\eta$, where $\eta$ is the learning rate. On a quadratic loss, $2/\eta$ is the value of sharpness at which gradient descent diverges---the iterates overshoot instead of converging to the minimum. What's surprising is that neural networks train right at this edge, with the sharpness hovering at the stability threshold throughout training.

These dynamics turn out to be remarkably robust across different architectures and tasks. This is significant because sharpness is conjectured to play a key role in generalization: training at the edge of stability may act as an implicit regularizer, biasing gradient descent toward flatter minima that generalize better.