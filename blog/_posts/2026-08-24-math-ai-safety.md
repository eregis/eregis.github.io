---
layout: post
title: "AI Safety for Mathematicians"
date: 2026-08-24
mathjax: true
---

Last week I stumbled upon a cool-looking resource: a website called [AI Safety for Mathematicians](https://mathforaisafety.org/). At the top of the page, they lay out their mission statement:

>This is designed to be a very high-level resource for mathematicians to get involved with AI safety work. We believe that:
>1. AI is poised to have a substantial impact on society in the coming years.
>2. With that come many new risks that we need more effort to manage effectively.
>3. There are many opportunities for mathematicians to contribute, including some in which they have a strong comparative advantage.

The website is maintained by the mathematician Jacob Tsimerman and includes contributions from fellow mathematicians Andrew Critch, Lionel Levine, Yevgeny Liokumovich, and Arul Shankar.

[Tsimerman was recently awarded one of the four 2026 Fields Medals](https://www.quantamagazine.org/jacob-tsimerman-wins-2026-fields-medal-for-andre-oort-conjecture-proof-20260723/) for his contributions to arithmetic and complex algebraic geometry. The Fields Medal is widely considered the most prestigious award in mathematics, often described as the Nobel Prize of mathematics. However, soon after reaching the pinnacle of his profession, he caused quite a stir in the mathematics community when [he announced that he was joining OpenAI to work on AI safety](https://www.nytimes.com/2026/07/23/science/jacob-tsimerman-fields-medal.html).

Other than programming, mathematics has probably seen the biggest shakeup of any field from recent advances in AI. Several long-standing conjectures have been toppled this year, including [the disproof of the unit-distance conjecture](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) and [a counterexample to the Jacobian conjecture](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/). And most recently, OpenAI claims that an internal version of an unreleased model named Astra [produced *ten* results on open problems](https://openai.com/index/ten-advances-in-mathematics/)---any one of which would likely net a human mathematician tenure at a respectable university. Tsimerman saw the writing on the wall: "I think AI will be better than mathematicians at doing math within two years."

The website helpfully provides an overview of some research directions to which mathematicians can contribute. It currently offers brief expositions on three of them: Developing Good Heuristics, Interpretability and Feature Manifolds, and Open-Source Game Theory.

**Developing Good Heuristics** is a research direction that aims to provide mechanistic descriptions of AI behavior. 

Machine learning models are black boxes: we don't currently understand the gear-level details of how they work. One way to probe a model's behavior is to feed it inputs and observe what it does. But ideally, we would want to predict a model's outputs without having to run it. Given the complicated nature of large machine learning models, it seems too much to ask for a procedure that takes an arbitrary model and says with certainty whether it will ever output some particular value (e.g., something harmful, like instructions for making a bomb). But one could hope to develop good *heuristics* that allow you to bound the probability that a model exhibits some given behavior.

**Interpretability and Feature Manifolds** is a research direction that aims to develop tools for probing the internals of models in order to understand their behavior.

While we can think of neural networks as parameterized functions that map inputs to outputs, deep neural networks are organized into *layers*. The structure is that the outputs of each layer feed in as inputs to the next, until the final layer produces what we call the output. The outputs of the intermediate layers are called *activations*.

Under this framework, features are patterns in activation space. One conjecture is the linear representation hypothesis: concepts correspond to *directions* in activation space, so that its linear structure carries semantic meaning. If you take the features for two concepts and combine the vectors, the result is a direction we intuitively recognize as meaningfully related to both. Here's a famous example, from the earlier word-embedding literature:

$$\text{king} - \text{man} + \text{woman} \approx \text{queen}$$

But linear geometries aren't the only ones observed in feature space. Features have also been found to lie on manifolds with periodic structure. Understanding the geometry of activation space, and how it relates to the concepts a neural network represents, would be incredibly useful for AI safety. For example, it might let us tell when a model is lying, based on what's going on in its internal representations.

**Open-Source Game Theory** is a research direction that studies game theory in the setting where agents have access to each other's source code. 

Game theory is the study of strategic interaction between rational agents. The classic example is the Prisoner's Dilemma. Suppose you and your friend get arrested for bank robbery. The police interrogate both of you separately, making the same offer: if you rat your friend out and he stays quiet, you go free and he gets twenty years. If he rats you out and you stay quiet, you get twenty years and he goes free. If neither of you talks, you each get five years. And if you both rat each other out, you each get ten years.

|                    | **Friend stays quiet** | **Friend rats**   |
| ------------------ | ---------------------- | ----------------- |
| **You stay quiet** | 5 years, 5 years       | 20 years, free    |
| **You rat**        | free, 20 years         | 10 years, 10 years|

If you're in this scenario, what should you do? If the two of you could reach an agreement beforehand, you would want some binding commitment to cooperate and stay quiet. But because you can't, the "optimal" thing for each of you to do is to rat the other out---netting both of you an extra five years in prison than if you had just cooperated.

When agents work together we call it "cooperating", and when they work against each other we call it "defecting". In the real world, there are all sorts of arrangements we use to enable cooperation. For example, one of the purposes of contracts is to enable cooperation by making defection prohibited by force of law (or at the very least, costly enough to make cooperation the better option). Note that cooperation is not always good from a societal perspective. For example, when large corporations "cooperate" to keep prices above the competitive level, they are successfully cooperating in their prisoner's dilemma---but society labels that form of cooperation as "collusion" and we make it some mixture of illegal and frowned-upon.

What's interesting and different about machine learning models is that, in principle, they could give each other their source code. So trust, rather than resting on things like reputation and context, could in theory be computed directly: you could actually compute *using the agent's own source code* whether an agent is actually going to cooperate with you. Of course, this is easier said than done, for a lot of reasons (setting aside the practical question of what an exchange of source code would even look like), but it's still quite interesting.

In addition to providing an overview of research directions, they also list some prominent AI Safety research organizations:

* [Alignment Research Center (ARC)](https://www.alignment.org/)
* [Iliad](https://www.iliad.ac/)
* [METR](https://metr.org/)
* [Redwood Research](https://www.redwoodresearch.org/)
* [Resolution](https://resolution.org/)
* [Timaeus](https://timaeus.co/) (now part of Resolution)
* [UK AI Security Institute](https://www.aisi.gov.uk/)

This is by no means a comprehensive list of all the AI safety organizations doing interesting work, but it's a good starter list, featuring some of the larger organizations that are looking to expand aggressively. Resolution in particular is clearly looking to grow: it's a new organization that recently received a large allocation of funding from Coefficient Giving (formerly Open Philanthropy). They describe themselves as pursuing a large portfolio of bets across both theoretical and empirical approaches to AI safety---though a notable aspect of their description is the emphasis on how best to use automated research, an area that remains underexplored since we've only had highly capable AI agents for a fairly short amount of time.

The website also offers several repositories of open research questions for those who are looking to jump right in.

* [AISI Alignment Project: Computational Complexity Theory](https://alignmentproject.aisi.gov.uk/research-area/computational-complexity-theory)
* [Iliad Ecosystem](https://www.iliad.ac/incubated-organizations)
* [MAIS Open Problems](https://github.com/lionellevine/MAIS/tree/main/open-problems#readme)
* [Timaeus Project Ideas](https://timaeus.co/projects)

It's cool to see the AI Safety ecosystem continue to grow!