---
layout: post
title: "Physics of Learning and Neural Computation"
date: 2025-11-29
mathjax: true
---


A couple weeks ago, someone in my lab shared on the Slack channel a really helpful looking resource for learning more about research at the intersection of physics and machine learning: a website called [Physics of Learning and Neural Computation](https://www.physicsoflearning.org/). It's a collaboration of notable researchers who work in the area. The collaboration is directed by Suryu Ganguli, a Stanford Applied Physics Professor. He has made many contributions to the machine learning literature, including being the last author on the paper that introduced diffusion models: Deep Unsupervised Learning Using Non-Equilibrium Thermodynamics. 

It brands itself as Simons collaboration (so affilliated with the Simons Foundation). The Simons foundation was founded by mathematician and finance person Jim Simons (notable in mathematics for advances like Chern Simons theory and in finace for Renaisance technology which was famous for being highly cryptic about their trading strategies and making outlandish, efficient-market-defying returns year after year). The Simons foundation sponsors a lot of work in this type of vein: they specialize in interdisplicnary work that incorporates perspectives from multiple different STEM field, epecially work with a computationa flavor. It i

Their summary paragraph for some of the contributions that physics and physicists have done in understanding artificial intelligence is quite good:

> Indeed ideas from the physics of complex systems have long played a profound role in the development and analysis of machine learning and neural computation, ranging from the Hopfield model and Boltzmann machine (2024 physics Nobel prize), and the understanding of optimization dynamics and geometry in high dimensional disordered systems (2021 physics Nobel prize), to more recent advances in the discovery and analysis of scaling laws, and the inspiration of nonequilibrium statistical mechanics for diffusion models in generative AI. 

On the team page, you can see a list of principal investagors and affiliates. They are organized into principal investigators, affiliates, and collaboraters.

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


  And helpfully, the website is running a series of survey lectures where principal investigators give an hour-long lecture on some of their research. These are recorded and can be found on the website or the associated YouTube channel. As usual with these style of blog posts, I will briefly go over some of the survey lectures to give a flavor of the type of work that people are doing. (And the usual caveats apply that explaining other people's work simply is difficult, so hopefully no terrible mistakes or over simplifications creep in.) I will probably moreso being providing context for the general area that the researcher is working in, then explaining the nuances of their contribution specifically. I find these sorts of posts helpful for me personally as often I have this vague idea of what other people are up to, but it isn't I try to actually write out from first-principles the purpose of a research program to myself, do I fully understand the core assumptions and motivations.
  
I will go in chronological order as listed on the website

[# Cengiz Pehlevan - Mean-field theory of deep network learning dynamics and applications to neural scaling laws](https://youtu.be/A9V_VEkgkGE?si=itAqpXUlv8dX0DAl)

> I will review recent developments in obtaining a mean-field description of the high-dimensional learning dynamics of deep neural networks. These mean-field theories result from various infinite limits, including width, depth and attention-heads. I will present applications of these ideas to neural scaling laws in lazy and feature-learning regimes.


Mean-field theory descriptions are very cool and very physical-picture of the dynamics of neural networks.

The picutre of of mean-field theory goes roughly like this: Over the course of training, the parameters of the network will descend via gradient descent to minimize the loss function. Instead of imagining the parameters of the network as a whole, you can imagine you imagine each set of parameters associated with a neuron as a set of coupled equations. The loss function is like a Hamiltonian: and the fact that loss function isn't seperable in neurons, means that neurons are coupled---akin to how particles interact via forces.

For finite number of neurons this is all very complicated. But in the limit as N goes to infinity, you can actually replace the complicated set of coupled equation with a probability density over the weights. And the distribution over neurons will move deterministically to minimize the loss function and you can describe the evolution of the probability distribution analytically.

The set-up Pehlevan used here is a bit different though it seems. He seems to be using something called "dynamical mean field theory". And they don't track a probability density over the neurons, but instead order parameters that summarize the state of the network at that point in time. From [the associated paper](https://pehlevan.seas.harvard.edu/sites/g/files/omnuum6471/files/pehlevan/files/bordelonpehlevan_ml4phys_neurips_2022.pdf), the order parameters appear to be


[# Julia Kempa - Synthetic Data: Friend or Foe in the Age of Scaling?](https://youtu.be/x3DrcQs3Lk8?si=Pl0Ttc4b6elOwq-b)

> As AI model size grows, neural **scaling laws** have become a crucial tool to predict the improvements of large models when increasing capacity and the size of original (human or natural) training data. Yet, the widespread use of popular models means that the ecosystem of online data and text will co-evolve to progressively contain increased amounts of synthesized data.

This is an interesting challenge awaiting training the neural networks. I've seen two things brought up in two contexts: one is the challenge that the AI models are trained on Internet data, but increasingly, Internet data consists of text generated by LLMs. This could lead to a host of issues: some hilarious, some more serious. On the hilarious end, I recall that there used to be an issue where LLMs from other labs other than OpenAi would think that they were ChatGPT and it was speculated that being ChatGPT is the AI agent in the training data, it ended up being an attractor in persona space. On the more serious side, the output of LLMs are not "high quality" in the sense that they aren't entangled with reality in the way that we would desire for high-quality training data. It's hard to exactly formally explain in my own words why training an LLM on LLM data would be bad ("low entropy" "mode collapse"), but it anecdotally seems to be a problem.

Other discussion I've seen with synthetic data was more positive: can we use synthetic data to supplement any coming data lacking concerns? While it seems that forefront labs are not scaling quite as vigoruously as they used to, there will still likely be a trend toward training bigger models and that will require more data. It might be necessary to (with careful engineering) create text for other LLMs to train on.

[# Miranda Cheng - GUD: Generation with Unifed Diffusion](https://youtu.be/A2IWWceVbpk?si=-5ZXT0QqPnWZv2oY)

> We present the GUD model, a unified diffusion model interpolating between standard diffusion and autoregressive models. Inspired by concepts from the renormalization group in physics, which analyzes systems across different scales, we revisit diffusion models by exploring three key design aspects: 1) the choice of representation in which the diffusion process operates , 2) the prior distribution that data is transformed into during diffusion , and 3) the scheduling of noise levels applied separately to different parts of the data, captured by a component-wise noise schedule. Incorporating the flexibility in these choices, we develop a unified framework for diffusion generative models with greatly enhanced design freedom.

Diffusion models and renormalization group share similar high-level similiarties (though there are interesting wrinkles and differences once you get down to the technical details.) One is this hierarchical picture: with renormalization you integrate out the high-wavelenfth degrees of freedom, until only the low-wavelenfth physics is left. With diffusion, the hgih-wavelenfth structure is also what is create. If you were to invert a renormalization flow, you would start with low-wavelength physics and build your theory up until higher and higher wavelengths. In reverse diffusion, you see thatthe high-level aspects of the image come in first and then finer and finer details gets clarified over the course of the reverse diffusion process.

[# Maissam Barkeshli - Sharpness Dynamics in Neural Network Training](https://youtu.be/mZ_DpkL95os?si=2O5YTZGpHdGd8hj8)

> In this talk I discuss certain robust, universal phenomena that appear when tracking the top eigenvalue of the Hessian of the loss, which we refer to as the sharpness. The sharpness tracks the local geometry of the training loss landscape and plays a key role in determining the maximal allowable learning rate. It is also conjectured to play an important role in generalization capability. I will demonstrate how sharpness exhibits various universal phenomena during early, middle, and late stages of training across architectures and tasks, and how this phenomena can be understood through the lens of a simple toy model. I will also show how sharpness provides an important lens into understanding the underlying mechanisms of learning rate warmup, and how to make it more efficient.






