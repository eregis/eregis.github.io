---
layout: post
title: "Mean-Field Dynamics Explained"
date: 2026-07-14
mathjax: true
permalink: /unlisted/mean-field-dynamics-932e2c63816eef3ea01c/
sitemap: false
noindex: true
description: "How training a wide two-layer network becomes the flow of interacting particles: the four 2018 mean-field papers, the NTK, lazy training, and feature learning."
---

A two-layer neural network is a sum of $N$ simple units:

$$f(x; \theta) = \sum_{i=1}^{N} v_i \, \sigma(w_i \cdot x)$$

Each unit---each *neuron*---does three things:

1. Projects the input $x$ onto a direction $w_i$
2. Applies a scalar nonlinearity $\sigma$
3. Contributes to the output with weight $v_i$

Two-layer neural networks differ from linear networks in that they can learn *features*: relevant aspects of the input data distribution. If the directions $w_i$ were fixed in advance, this would be linear regression on a fixed set of features---the model would be linear in its trainable parameters (the second-layer weights). But in a two-layer network the first-layer weights are trained too, so the network learns which directions matter. A model that learns its own features is necessarily a *nonlinear* function of its parameters---which makes the loss landscape non-convex.

$$L(\theta) = \mathbb{E}_{x}\left[\left(f(x; \theta) - f^*(x)\right)^2\right]$$

To train the model, we must perform some variant of gradient descent on the loss function. But how do we know that gradient descent will work---that the iterates will converge to a global minimum of the loss? It's hard to prove things in the non-convex setting: gradient descent on a generic non-convex landscape can get trapped at a local minimum. Yet everyday experience with deep learning suggests the opposite: make the network wide enough, and gradient descent drives the training loss to near-zero reliably. At the beginning of the deep learning revolution, this simple fact had no adequate explanation in theory---not even for the two-layer network, the simplest network that learns features at all.

<img src="/assets/mean-field-dynamics/three-views.png" alt="The same two-layer network in three views: the network diagram; its parameters stacked into one long vector, split neuron by neuron; and the neurons as particles forming an empirical measure over parameter space." style="max-width: 100%; display: block; margin: 0 auto;">

In the spring of 2018, an explanation arrived. Over the course of five weeks, four different groups posted arXiv papers describing the dynamics of two-layer neural networks in the mean-field regime---the limit as the width of the network goes to infinity. They all shared a common insight: instead of tracking the long vector of parameters, it's better to track the empirical distribution over neurons. All four groups answered the question: in the infinite-width limit, do the dynamics of gradient descent converge to a distributional description? Three of the groups (Mei et al; Rotskoff and Vanden-Eijnden; Chizat et al) tackled the slightly harder question: do those dynamics provably reach a *global* minimum of the loss?

* **[Mei, Montanari, and Nguyen (April 2018)](https://arxiv.org/abs/1804.06561)** showed that the distribution of the neurons evolves according to a nonlinear partial differential equation and provided quantitative bounds showing that stochastic gradient descent tracks this PDE. They also provided a global-convergence guarantee for noisy SGD using this description. They worked from the perspective of statistical physics, treating the neurons as a mean-field interacting system and the loss as an energy functional over the distributions of particles.
* **[Rotskoff and Vanden-Eijnden (May 2018)](https://arxiv.org/abs/1805.00915)** recast the neurons as an interacting particle system, establishing a law of large numbers and a central limit theorem for their empirical distribution---and, with them, how the trained network's accuracy scales with its width. They also gave conditions under which the flow reaches the global minimum. They worked from the perspective of applied mathematics and numerical analysis, where interacting particle systems are a standard tool for approximating measures.
* **[Sirignano and Spiliopoulos (May 2018)](https://arxiv.org/abs/1805.01053)** proved a rigorous law of large numbers: as the width grows, the empirical measure of neurons trained by SGD converges to a deterministic limit. They worked from the perspective of applied probability and stochastic analysis, using weak-convergence techniques to establish the limit.
* **[Chizat and Bach (May 2018)](https://arxiv.org/abs/1805.09545)** identified the distributional dynamics as a Wasserstein gradient flow where the measure evolves to minimize the loss functional. They showed that, under certain conditions, the flow converges to a global minimizer of the unregularized loss. They worked from the perspective of optimization, viewing training as an optimization problem over the space of measures.

Collectively, they founded what is now called the **mean-field theory of two-layer neural networks**.

(A note on the term. "Mean field" is one of the most overloaded phrases in applied mathematics. In this article, the term refers to the McKean--Vlasov-type limit of two-layer networks. This is not to be confused with the *dynamical mean-field theory* of deep networks---developed in this form by Bordelon and Pehlevan---which tracks order parameters like kernels and correlation functions rather than a particle density. Nor is it to be confused with *mean-field variational inference* in Bayesian machine learning which refers to product-measure approximations.)

<img src="/assets/mean-field-dynamics/timeline.png" alt="Timeline from spring 2018 to late 2020: four mean-field papers clustered within five weeks, the neural tangent kernel one month later, then lazy training and Yang and Hu's feature-learning paper completing the arc." style="max-width: 90%; display: block; margin: 0 auto;">

However, that wasn't the end of the infinite-width story. One month later, a fifth paper landed. [Jacot, Gabriel, and Hongler (June 2018)](https://arxiv.org/abs/1806.07572) *also* studied neural networks in the infinite-width limit, and *also* concluded that gradient descent provably fits the training data. But their description looked nothing like the mean-field picture. In their limit, the network behaves as a kernel method---a linear model built on a fixed set of features---with the kernel being the *neural tangent kernel*.

So we have two incompatible pictures of what training looks like in the infinite-width limit. Which one describes the real-world networks we actually train?

Resolving that question took **[Chizat, Oyallon, and Bach (December 2018)](https://arxiv.org/abs/1812.07956)**, who identified two regimes: a *lazy* regime, in which the parameters barely move from their initialization, and a *feature-learning* regime, in which they move an $O(1)$ distance. The resolution runs through a single idea: *scaling*. How you scale the network's output with $N$ determines which regime you land in: NTK scaling puts you in the lazy regime, mean-field scaling in the feature-learning one. [Yang and Hu (2020)](https://arxiv.org/abs/2011.14522) later extended this classification to arbitrary architectures.

# The Mean-Field Limit

We will walk through the derivation of the mean-field dynamics of two-layer neural networks. We will follow most closely the approach of Chizat and Bach, though we will note the other three perspectives where appropriate.

First, we set up the two-layer neural network. The network is composed of $N$ individual units called neurons. Each neuron has its own parameters and can be viewed as a function of the input: it projects the input down, composes with a nonlinearity, and then weights the result. Bundling everything the $i$-th neuron owns into a single vector $\theta_i = (v_i, w_i) \in \mathbb{R}^{d+1}$, we write the single-neuron function as

$$g(x; \theta_i) = v_i \, \sigma(w_i \cdot x).$$

We can then define the network in the **mean-field parametrization**, which *averages* the neuron outputs instead of simply summing them:

$$f(x; \theta_1, \ldots, \theta_N) = \frac{1}{N} \sum_{i=1}^{N} g(x; \theta_i)$$

Notice that $f$ has a symmetry: relabel the neurons---swap $\theta_3$ with $\theta_{17}$---and the function is unchanged. The output doesn't depend on the *list* of neurons. It depends only on *how many neurons sit where* in parameter space. All of that information is carried by the empirical measure:

$$\mu_N = \frac{1}{N} \sum_{i=1}^{N} \delta_{\theta_i},$$

the probability measure that places a point mass of weight $1/N$ at each neuron's location. The network output is then an integral of the single-neuron function against this measure:

$$f(x; \mu_N) = \int g(x; \theta) \, d\mu_N(\theta)$$

This is the same move a physicist makes in passing from a list of $10^{23}$ molecule positions to a particle density field: identical particles should be described by *where they are*, not by *which one is which*. The neurons of a two-layer network are identical particles---which is why the empirical measure description is so natural.

Consider the population mean-squared error loss:

$$L_N(\theta_1, \ldots, \theta_N) = \frac{1}{2} \, \mathbb{E}_{(x,y)} \big[ (f(x; \theta_1, \ldots, \theta_N) - y)^2 \big]$$

We want to re-express this in terms of the measure. Conveniently, since $f$ depends on the parameters only through $\mu_N$, so does the loss:

$$\mathcal{L}[\mu] = \frac{1}{2} \, \mathbb{E}_{(x,y)} \left[ \left( \int g(x; \theta) \, d\mu(\theta) - y \right)^{2} \right]$$

The loss has been promoted to a *functional* on the space of probability measures. Written this way, it makes sense for *any* probability measure $\mu$ over $\mathbb{R}^{d+1}$, not just empirical measures supported on $N$ points.

The term "mean field" is statistical physics jargon. It's when each particle responds to the aggregate field generated by the other particles rather than to each of its $N-1$ neighbors individually. That description applies here precisely because the loss is a functional of the empirical measure alone.

It's useful to break down the loss functional into separate terms. Expanding the square in $\mathcal{L}$:

$$\mathcal{L}[\mu] = \frac{1}{2} \, \mathbb{E}\!\left[y^2\right] + \int V(\theta) \, d\mu(\theta) + \frac{1}{2} \iint U(\theta, \theta') \, d\mu(\theta) \, d\mu(\theta')$$

where

$$V(\theta) = -\mathbb{E}_{(x,y)} \big[ y \, g(x; \theta) \big], \qquad U(\theta, \theta') = \mathbb{E}_{x} \big[ g(x; \theta) \, g(x; \theta') \big]$$

There are three terms: a constant term, a single-particle potential, and an interacting-particle potential. The single-particle potential $V$ pulls each neuron toward configurations whose output correlates with the labels. The interaction $U$ raises the energy of pairs of neurons whose outputs are positively correlated, causing a repulsion force between neurons.

It's time to tackle the dynamics: what does gradient descent on the $N$ neurons correspond to in terms of the distributional dynamics of $\mu_N$? Since measures are unfamiliar territory, we first need two pieces of mathematical machinery.

Given a loss functional $\mathcal{L}$, the **first variation** $\frac{\delta \mathcal{L}}{\delta \mu}$ tells you how small density perturbations of the measure change the value of the functional: perturb $\mu$ by a small signed measure $\varepsilon \chi$, and the loss changes, to first order, by $\varepsilon \int \frac{\delta \mathcal{L}}{\delta \mu} \, d\chi$. For our quadratic loss, it is straightforward to compute the first variation:

$$\frac{\delta \mathcal{L}}{\delta \mu}(\theta) = \mathbb{E}_{(x,y)} \big[ \left( f(x; \mu) - y \right) g(x; \theta) \big]$$

This makes sense: the first variation at $\theta$ is the marginal cost of neuron-mass at $\theta$. It is large and positive where a neuron at $\theta$ fires in phase with the current *residual* $f(x;\mu) - y$---adding mass there would only increase the loss. It is negative where the neuron's output runs opposite to the residual---adding mass there improves the fit.

However, while neurons move to decrease the loss, they cannot teleport---they must flow. This locality constraint is what the second piece of machinery encodes. If particles distributed as $\mu_t$ move through parameter space with velocity field $v_t(\theta)$, their density is transported according to the **continuity equation**,

$$\partial_t \mu_t = -\nabla \cdot (\mu_t \, v_t),$$

the same equation that expresses conservation of mass in a fluid. It imposes two constraints on the dynamics: probability mass is neither created nor destroyed, and mass flows *continuously* through space.

Suppose that our measure evolves in accordance with the continuity equation. We would then have for the time derivative of the loss:

$$ \begin{align}
\frac{d}{dt} \mathcal{L}[\mu_t] &= \int \frac{\delta \mathcal{L}}{\delta \mu} \, \partial_t \mu_t \, d\theta \\
&= - \int \frac{\delta \mathcal{L}}{\delta \mu} \, \nabla \cdot (\mu_t v_t) \, d\theta \\
&= \int \left\langle \nabla_\theta \frac{\delta \mathcal{L}}{\delta \mu}, \; v_t \right\rangle d\mu_t
\end{align}$$

where the integration by parts discards a boundary term (the density and its flux vanish at infinity).

Which velocity field corresponds to gradient flow? *The one that decreases the loss fastest*. And we can see from the above expression that the loss drops fastest---per unit of kinetic energy $\int \lVert v_t \rVert^2 d\mu_t$---when every particle moves down the spatial gradient of the first variation:

$$v_t = -\nabla_\theta \frac{\delta \mathcal{L}}{\delta \mu_t}$$

This velocity field is (minus) the **Wasserstein gradient** of $\mathcal{L}$, so named because measuring velocity fields by kinetic energy is precisely what endows the space of measures with the Wasserstein-2 geometry of [optimal transport](https://en.wikipedia.org/wiki/Transportation_theory_%28mathematics%29). Substituting it into the continuity equation gives the **Wasserstein gradient flow**:

$$\partial_t \mu_t = \nabla \cdot \left( \mu_t \, \nabla_\theta \frac{\delta \mathcal{L}}{\delta \mu_t} \right)$$

This PDE is the object that all four 2018 papers describe. And the PDE is more than just formalism: gradient descent on a finite-width two-layer network is a particle discretization of this flow. To see it, differentiate the finite-$N$ loss with respect to one neuron. Because the network output carries a $1/N$ prefactor, so does the gradient:

$$\begin{align}
\nabla_{\theta_i} L_N &= \frac{1}{N} \, \mathbb{E}_{(x,y)} \big[ (f(x) - y) \, \nabla_\theta g(x; \theta_i) \big] \\
&= \frac{1}{N} \, \nabla_\theta \frac{\delta \mathcal{L}}{\delta \mu} \bigg|_{\mu_N} (\theta_i)
\end{align}$$

The gradient with respect to neuron $i$ is exactly the Wasserstein gradient of the loss functional shrunk by a factor of $N$. The factor has a simple reading: each neuron contributes only a $1/N$ sliver of the output, so the loss is $N$ times less sensitive to it.

That factor of $1/N$ necessitates a somewhat strange convention: in order to have a well-defined limit with the mean-field parametrization, one runs gradient descent with a step size that *grows* with the width, $\gamma = \eta N$. Substituting,

$$
\theta_i - \eta N \, \nabla_{\theta_i} L_N = \theta_i - \eta \, \nabla_\theta \frac{\delta \mathcal{L}}{\delta \mu_N}(\theta_i),
$$

The factor of $N$ of the step size cancels out the $1/N$ factor in front of the Wasserstein gradient. So even in the infinite-width limit, every neuron takes an $O(1)$ step down the Wasserstein gradient.

Let me make a small physicist's aside on the step size convention. Notice that the following expressions are (trivially) equivalent:

$$\theta_i - \eta N \, \nabla_{\theta_i} L_N = \theta_i - \eta \, \nabla_{\theta_i} \big( N L_N \big)$$

So we actually have a choice. Rather than letting the step size grow by a factor of $N$, one could instead let the *loss* grow by a factor of $N$. The appeal of scaling the loss instead of the step size is that the step size has a natural physical interpretation as a small unit of time, and it isn't clear why time should be measured differently as the number of particles in the system grows.

In physics, *extensive* quantities scale with system size---volume, mass, energy---while *intensive* quantities are local and do not---temperature, pressure, density. Now consider a large system of gas molecules: if you double the number of particles, you would not expect the relaxation time to halve. You would expect the characteristic timescale of relaxation to be a quantity that converges in the thermodynamic limit. This would suggest that the step size---which is a time-scale---should behave like an intensive quantity and be independent of the system size.

Under the current convention, the loss is intensive. If you take an empirical distribution of $N$ neurons and place a duplicate at each location, the loss doesn't change. But do the same to a physical system and its energy doubles. Multiplying the loss by $N$ would make it extensive---which is a natural choice if you read the loss as an energy. What machine learning calls the loss can then be interpreted as an energy *per particle*.

One downside is that $N L_N$ does not converge to a finite value in the infinite-width limit. Physically-speaking, that's fine though: what matters is that the per-particle gradients $\nabla_{\theta_i} (N L_N)$ converge to an $O(1)$ quantity. Another downside is that the value of $N L_N$ is not comparable across systems of different size. So to compare the quality of fit of two networks of different width, the intensive $L_N$ is the appropriate object. But if you want the object that governs the dynamics, I would argue that the extensive $N L_N$ is more appropriate. This is exactly how Rotskoff and Vanden-Eijnden set up the problem: they take the loss multiplied by $N$ as their energy, which puts the neurons in the standard form of an interacting particle system.

That the finite-$N$ particle system really does converge to the PDE is a theorem, and Sirignano and Spiliopoulos proved it, in the form of a law of large numbers---where the neurons are treated as independent samples. The key subtlety is that the neurons are independent only at initialization. But what saves the theorem is that they are coupled only through the mean field, each supplying just $1/N$ of it.

It's helpful to visualize the manifestation of the law of large numbers. The widget below trains two independently initialized networks---same architecture, same data, different random seeds---at whatever width you choose. For narrow networks, the two particle clouds evolve visibly differently: which features get found is partly luck. For wide networks, the two clouds trace out the same flow: the randomness of initialization washes out as the empirical measure converges to the deterministic limit.

<div id="lln-widget"></div>
<script src="/assets/mean-field-dynamics/lln-width.js" defer></script>

*Two random seeds, one slider. Both networks train live in your browser by gradient descent in the mean-field parametrization; the scatter shows each network's neurons as particles $(w_i, v_i)$. As you increase $N$, the two empirical measures---and the two fits---converge to the same deterministic flow.*

So the dynamics of the measure are a Wasserstein gradient flow of the loss. But why would that flow converge to a *global* minimum?

One approach is that of Chizat & Bach. In their setting, they worked with units that are positively homogeneous (e.g. the ReLU unit). Given that assumption, they proved convergence if the following holds:

1. The flow converges to some limit $\mu_\infty$.

2. The neurons are initialized so that no direction in parameter space is left unoccupied---for any direction you pick, however narrow the sliver around it, some neurons are pointing that way.

3. The loss functional $\mathcal{L}$ is convex along density interpolations.

Condition (1) ensures local convergence. Condition (2) rules out the failure mode in which mass is cheaper somewhere the flow has no neurons and so cannot feel it. Condition (3) then upgrades these local optimality conditions to global optimality. We will show that the loss functional for the two-layer neural network is indeed convex along density interpolations.

Let $\mu_0$ and $\mu_1$ be two measures, and consider the convex combination $\mu_t = (1-t)\,\mu_0 + t\,\mu_1$ for $0 \le t \le 1$. The key observation is that the network output is *linear* in the measure:

$$f(x; \mu_t) = (1-t) f(x;\mu_0) + t\, f(x;\mu_1)$$

Write $r_i(x,y) = f(x;\mu_i) - y$ for the residual of $\mu_i$. Since the weights $(1-t)$ and $t$ sum to one, the label passes through the combination untouched, and the residual is affine in $t$ as well:

$$r_t = (1-t)\, r_0 + t\, r_1$$

Now the only nonlinearity left is the square, and for scalars the identity $\big((1-t)a + tb\big)^2 = (1-t)a^2 + t\,b^2 - t(1-t)(a-b)^2$ holds. Applying it pointwise and taking expectations:

$$
\begin{align}
\mathcal{L}[\mu_t] &= \tfrac{1}{2}\, \mathbb{E}_{(x,y)}\big[ ((1-t)\,r_0 + t\,r_1)^2 \big] \\[4pt]
&= \tfrac{1}{2}\, \mathbb{E}_{(x,y)}\big[ (1-t)\,r_0^2 + t\,r_1^2 - t(1-t)(r_0 - r_1)^2 \big] \\[4pt]
&= (1-t)\, \mathcal{L}[\mu_0] + t\, \mathcal{L}[\mu_1] - \frac{t(1-t)}{2}\, \mathbb{E}_{(x,y)}\big[ (r_0 - r_1)^2 \big]
\end{align}
$$

The final term is nonnegative, so

$$\mathcal{L}[\mu_t] \le (1-t)\, \mathcal{L}[\mu_0] + t\, \mathcal{L}[\mu_1],$$

which is exactly convexity in $\mu$.

Mei, Montanari, and Nguyen arrive at a convergence guarantee by a different route. They studied *noisy* SGD, where independent Gaussian noise is added to each step. In the mean-field limit that noise becomes a diffusion term, so the continuity equation picks up a Laplacian and the dynamics become the Wasserstein gradient flow of a regularized objective---a weight decay to keep neurons from escaping to infinity, plus an entropy:

$$\mathcal{F}[\mu] = \mathcal{L}[\mu] + \frac{\lambda}{2} \int \lVert \theta \rVert^2 \, d\mu + \beta^{-1} \int \mu \log \mu.$$

The entropy functional is strictly convex. Adding it as a regularization term to the objective buys us two things. First, the regularized objective now has a unique minimizer, characterized explicitly as the fixed point of a Gibbs relation $\mu \propto e^{-\beta \psi_\mu}$, where $\psi_\mu$ is that marginal cost of neuron-mass. With the unregularized objective, while all local minima are global minima, we could have many global minima. Second, the noise keeps spreading mass into every region of parameter space, so we no longer have to worry about having a well-spread out initialization---no direction can go empty, because diffusion refills it. The tradeoff is that because we've modified the objective, the flow converges to the minimizer of the *regularized* problem rather than the original one, which is only close to it when $\beta$ is large.

# Lazy Training Versus Feature Learning

However, the mean-field limit is not the only valid infinite-width limit of neural networks. There is also the neural tangent kernel limit.

Write $\theta$ for the full parameter vector---all $N(d+1)$ coordinates at once now, not one neuron's slice---and Taylor expand around the initialization $\theta_0$:

$$f(x; \theta) \approx f(x; \theta_0) + \nabla_\theta f(x; \theta_0) \cdot (\theta - \theta_0)$$

Everything on the right depends on $\theta$ only linearly---and a model that is linear in its parameters is a kernel method in disguise. By the kernel trick, every feature map has an associated kernel. In this case, the features are the components of $\nabla_\theta f(x; \theta_0)$. The associated kernel between two inputs is given by the inner product of their features:

$$\Theta(x, x') = \nabla_\theta f(x; \theta_0) \cdot \nabla_\theta f(x'; \theta_0)$$

This is the **neural tangent kernel** (NTK).

When does this picture of training apply? Jacot, Gabriel, and Hongler proved that it is exactly what happens in the infinite-width limit, *provided you normalize the output by $1/\sqrt{N}$ instead of $1/N$*:

$$f_{\mathrm{NTK}}(x) = \frac{1}{\sqrt{N}} \sum_{i=1}^{N} v_i \, \sigma(w_i \cdot x)$$

Under this scaling, two things happen as $N \to \infty$. First, the kernel at initialization stops being random: it is an average over many independently initialized neurons, so it concentrates at a deterministic $\Theta$ fixed by the architecture. Second, it stays frozen for the entire duration of training. Infinite-width training under NTK scaling is kernel regression.

But how can a network fit the data if its features never move? Fix a training set of $P$ points and hold $P$ fixed as $N$ grows. The tangent features $\nabla_\theta f(x_p; \theta_0)$ are generically linearly independent across distinct inputs, so the linearized model can interpolate all $P$ points at once. So the only question is how far $\theta$ has to travel.

It turns out---not very far. The NTK $1/\sqrt{N}$ prefactor makes each coordinate of the tangent feature vector $O(1/\sqrt{N})$. But because there are $O(N)$ of them, the tangent feature vector is $O(1)$ in *magnitude*. Since the change in output is just the inner product of the tangent vector with $\Delta\theta$, an $O(1)$ displacement in parameter space suffices to induce an $O(1)$ change in the function output---necessitating only an $O(1/\sqrt{N})$ change in each individual parameter. Contrast this with the mean-field limit, where each particle travels an $O(1)$ distance: the neurons migrate in order to learn features.

Which limit describes real training? One answer came at the end of the year.
[Chizat, Oyallon, and Bach (December 2018)](https://arxiv.org/abs/1812.07956)
showed that the frozen-feature behavior---which they named **lazy training**---can
be induced without taking an infinite-width limit. To do so, take *any*
differentiable model whose output vanishes at initialization (this can be done by
initializing as normal and then subtracting off the initial function), and
multiply its output by a scale factor $\alpha$:

$$f_\alpha(x; \theta) = \alpha \, f(x; \theta)$$

Introducing $\alpha$ forces us to choose the step size with care. Recall that with the mean-field parametrization, we had that the output changes an $O(1)$ amount each iteration of gradient descent. We want that property to survive amplification: one step should *still* change the output by $O(1)$, whatever $\alpha$ is. The complication is that $\alpha$ enters the training dynamics *twice*---once through the forward pass, where any parameter motion now moves the output $\alpha$ times as far, and once through the backward pass, where the gradient of the loss with respect to each parameter also picks up a factor of $\alpha$. The two compound, so a step of fixed size $\eta_\alpha$ moves the output $\alpha^2$ times as much as it would at $\alpha = 1$:

$$\Delta f_\alpha \;=\; \underbrace{\alpha \, \nabla_\theta f}_{\text{forward}}
\cdot \, \Delta \theta, \qquad
\Delta \theta \;=\; -\, \eta_\alpha \underbrace{\alpha \, \nabla_\theta f \;
\partial_f (N L)}_{\text{backward}}
\qquad \Longrightarrow \qquad
\Delta f_\alpha \;\propto\; \alpha^2 \, \eta_\alpha$$

To keep $\Delta f_\alpha = O(1)$---and the dynamics well defined---we must
compensate by shrinking the step size by exactly that factor:

$$\theta \;\mapsto\; \theta - \frac{\eta}{\alpha^2} \, \nabla_\theta \big( N L(\theta) \big)$$

Under the compensated step size, the output still moves an $O(1)$ amount per step---but the parameters themselves now move only $O(1/\alpha)$. As $\alpha \to \infty$, the training dynamics converge to those of the linearized model. Under their framework, the NTK limit is simply one road into the lazy regime: relative to the mean-field parametrization, the $1/\sqrt{N}$ scaling is an output amplification that grows with the width:

$$f_{\mathrm{NTK}} = \sqrt{N} \, f_{\mathrm{MF}},$$

so the NTK parametrization sits at $\alpha = \sqrt{N}$, while the mean-field
parametrization corresponds to $\alpha = 1$. The $O(1/\alpha)$ parameter
displacement is then $O(1/\sqrt{N})$---the vanishing parameter motion of the
previous section, recovered from the scaling alone.

The widget below trains the same two-layer network at different output scales $\alpha$. At $\alpha = 1$ (the mean-field end), watch the particles migrate: the neurons physically relocate to the features the target demands. Crank $\alpha$ up and the fit still converges---but the particles freeze in place, and the network fits the data through imperceptible collective adjustments of the features it started with.

<div id="lazy-rich-widget"></div>
<script src="/assets/mean-field-dynamics/lazy-rich.js" defer></script>

*One network, one dial. The slider sets the output scale $\alpha$ (with the step size compensated by $1/\alpha^2$, and the units paired at initialization so the initial output vanishes); training runs live by gradient descent. Left: the fit converging to the target. Right: the neurons as particles, with their initial positions ghosted---rich training moves them, lazy training does not.*

Chizat, Oyallon, and Bach showed that on real tasks lazily trained networks tend to underperform their feature-learning counterparts. So feature-learning is a more accurate description of the networks we actually train.

Just like the mean-field parametrization, the NTK parametrization has a thermodynamic reading. Recall that in the mean-field case we could interpret training as gradient descent with an $O(1)$ time step on the extensive energy $N L_N$. The force this energy exerts on a single neuron, $-\nabla_{\theta_i} (N L_N)$, is intensive---an $O(1)$ pull, no matter how many particles share the system.

Amplifying the output by $\alpha = \sqrt{N}$ upsets that balance. Each neuron now
couples to the output $\sqrt{N}$ times more strongly, so the per-particle force is
no longer intensive: it diverges as $O(\sqrt{N})$. The only way to keep a system
with diverging forces from exploding is to shrink the time step to $O(1/N)$---which
is exactly what the $1/\alpha^2$ compensation does. A diverging force integrated
over a vanishing time moves each particle only $O(\sqrt{N}) \cdot O(1/N) =
O(1/\sqrt{N})$.

So laziness, in thermodynamic terms, is *stiffness*: an enormous restoring force
producing a minuscule displacement. Whereas the physical
picture of mean-field training was a fluid flowing smoothly into its
minimum-energy configuration, the picture of NTK training is a rigid body under
load---responding to the external force elastically, reaching equilibrium without
ever appreciably deforming.

The final synthesis came from [Yang and Hu (2020)](https://arxiv.org/abs/2011.14522), who mapped the space of scalings systematically. In an *abc-parametrization*, three kinds of exponent govern how everything scales with width:

1. the multiplier on each layer's weights ($N^{-a}$),
2. the standard deviation of the initialization ($N^{-b}$),
3. the learning rate ($N^{-c}$).

The mean-field and NTK setups are each a single point in this space. Yang and Hu's *dynamical dichotomy* theorem then says that every abc-parametrization admitting a stable, non-trivial infinite-width limit lands in one of exactly two phases: either the limit is a *kernel* method---frozen features, NTK-style---or it *learns features*. There is nothing in between.

And within the feature-learning phase there is a distinguished point, the **maximal update parametrization** ($\mu$P), at which every layer's features move at the largest stable rate. $\mu$P has since become a practical tool: [Yang et al. (2022)](https://arxiv.org/abs/2203.03466) showed that because it keeps optimal hyperparameters stable across widths. You can tune a small model and transfer the hyperparameters to a large one.

The abc-coordinates come with a built-in redundancy---which makes the phase diagram easier to draw. Fix the initialization at its standard $O(1)$ scale, and the two-layer scalings that remain form a plane whose axes are the two knobs this article has been turning: how the output scales with $N$, and how the step size scales with $N$.

<img src="/assets/mean-field-dynamics/phase-diagram.png" alt="Phase diagram in the (a, c) plane of the two-layer network: every stable, non-trivial infinite-width limit lies on the segment 2a + c = 1, running from the NTK point at (1/2, 0) to the mean-field point at (1, -1), which sits at the kink of the stability boundary." style="max-width: 100%; display: block; margin: 0 auto;">

*The phase plane of the two-layer network, after Yang and Hu (2020). Both layers keep their standard $O(1)$ initialization; what varies is how the output multiplier ($N^{-a}$) and the step size ($\eta N^{-c}$) scale with width. Every stable, non-trivial infinite-width limit lives on one segment, $2a + c = 1$: the dynamical dichotomy made visible. Chizat, Oyallon, and Bach's dial slides along it---the amplification $\alpha = N^{1-a}$ runs from $\sqrt{N}$ at the NTK end down to $1$ at the mean-field end, where the segment dead-ends into instability. $\mu$P is that endpoint: the largest update rate the network can bear, the edge of stability.*

# Beyond Two Layers

Extending mean-field theory beyond two layers is more delicate. In a two-layer network the neurons enter exchangeably, so the state of the system is captured by a single measure over $\mathbb{R}^{d+1}$. In a deeper network, the hidden layers compose: exchangeability holds only within a layer, not across particles residing in different layers. The limiting object is then no longer one measure over particles but a hierarchy of coupled measures.

Rigorous multi-layer mean-field limits do exist. [Sirignano and Spiliopoulos (2019)](https://arxiv.org/abs/1903.04440), [Araújo, Oliveira, and Yukimura (2019)](https://arxiv.org/abs/1906.00193), and [Nguyen and Pham (2020)](https://arxiv.org/abs/2001.11443) all constructed versions. But the mathematical objects are heavier.

There is a second way for the particle picture to survive depth. When each layer adds only a small correction to a running hidden state, the layer index reads as *time* and the forward pass becomes a discretized differential equation. Taking that depth continuum jointly with the width limit, [Lu, Ma, Lu, Lu, and Ying (2020)](https://arxiv.org/abs/2003.05508) arrived at a mean-field ODE. The depth limit has since turned out to be stronger than expected: [Chizat (2025)](https://arxiv.org/abs/2509.10167) showed that it performs the averaging all by itself, so an infinitely deep ResNet behaves as if it were infinitely wide whatever its actual width.

In practice, though, the scaling perspective has proved quite useful. Yang's [Tensor Programs](https://arxiv.org/abs/1910.12478) framework handles arbitrary architectures by asking about scaling exponents rather than particle densities. Its physics falls out of a practitioner's question: how large a learning rate should each layer get? Demand feature learning everywhere---every layer's pre-activations moving $O(1)$ per step---and each weight's budget is set by its fan-in. Running this bookkeeping through an arbitrary network *is* the maximal update parametrization, and for two-layer networks it returns the mean-field parametrization exactly.
