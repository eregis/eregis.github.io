---
layout: post
title: "'Notes on Contemporary Machine Learning for Physicists' by Jared Kaplan"
date: 2025-11-07
mathjax: true
---

Jared Kaplan is a theoretical physicist who used to specialize in conformal field theory and cosmology, but has recently switched to working in machine learning. He has made several important contributions to the machine learning literature, most notably [his paper on scaling laws](https://arxiv.org/abs/2001.08361): how the performance of neural networks scale as you increase various training inputs (data size, number of parameters, and compute spent). He is a co-founder of Anthropic, one of the leading AI companies (best known for their signature LLM Claude and [recently valued at 183 billion dollars](https://techcrunch.com/2025/09/02/anthropic-raises-13b-series-f-at-183b-valuation/)).

![Claude Scaling Laws](\assets\kaplan-notes-machine-learning\claude_scaling-laws.jpeg)

In 2019, Kaplan released [a concise set of lecture notes](https://sites.krieger.jhu.edu/jared-kaplan/files/2019/04/ContemporaryMLforPhysicists.pdf) aimed at people like his past self: people who have studied physics (so those with a strong quantitative background) who want to get up to speed on the increasingly popular and relevant field of machine learning.

I decided to give the lecture notes a quick read. How could I not? Based on the title of the lecture notes---*Notes on Contemporary Machine Learning for Physicists*---I am squarely in the middle of the target audience.
 
What I found surprised me: these lecture notes are *really* good. If you are a physicist looking to learn more about traditional machine learning, this would be one of the first places that I would look.

Kaplan frames machine learning as "just" a subfield of statistics: given access to data in the form of samples, how do we learn a desired target function? The twist is that, in machine learning, the data is high-dimensional, our models are highly parameterized, and the desired target function is often *highly* non-linear.

> If at any point Machine Learning seems confusing, complicated, jargon-filled, etc., then just remember... 
it's really just curve fitting, or 'regression', with a very, very large number of parameters.

> In ML, we typically represent data as a vector $x$ in a high dimensional (often > 100) vector 
space. Canonical examples include a vector of all the pixel intensities in an image, or a vector that 
can represent all of the words in a language model's vocabulary. That means that we need a way to 
parameterize a complex, non-linear function that acts on this space. Neural networks are the most 
obvious modular construction that can represent a large class of such functions.

This is the framework of statistical learning theory. Kaplan's view of machine learning is conventional: neural networks are highly parameterized non-linear function approximators---as typified by theorems like the "[universal approximation theorem](https://en.wikipedia.org/wiki/Universal_approximation_theorem)": for any continuous function, there exists some neural network with some parameter values that can model that function to arbitrary precision.

![Overfitting on Training Set Data](\assets\kaplan-notes-machine-learning\Overfitting_on_Training_Set_Data.jpg)


# The Three Learning Problems

So neural networks are universal function approximators.

![Feedforward Network](\assets\kaplan-notes-machine-learning\feedforwardnetwork.png)

But what types of functions are they typically trying to approximate? Or put another way: what do we want our models to learn how to *do*? Kaplan focuses on three learning tasks in machine learning:

1. **Unsupervised Learning**

2. **Supervised Learning**

3. **Reinforcement Learning**

**Unsupervised learning** is about learning the structure of the data. An example of an unsupervised learning algorithm would be principal component analysis (PCA). Given a collection of data points, PCA finds the directions along which the data has maximal variance when projected.

![Height vs Shoe Size](\assets\kaplan-notes-machine-learning\height-shoe-size.png)

For example, in the above image we have a scatter plot of data plotting height versus shoe size. Intuitively, we see that the data goes up and to the right. The data looks like an ellipse, and the first principal component corresponds to the direction along the semi-major axis of the ellipse. 

We often try to interpret the components: in this case, we know that the first principal component corresponds to the latent concept of "size"---large people tend to be taller, have larger feet, have larger hands, weigh more, etc. So if you wanted to predict any one of these traits, knowing their size (e.g., their percentile on the size index) would be the single most informative number you could provide.

Another example of an unsupervised learning algorithm is t-SNE (t-distributed stochastic neighbor embedding). t-SNE aims to project high-dimensional data into a lower-dimensional space (most often two dimensions) such that the local structure of the data is preserved, but not necessarily global structure. What "local" versus "global" structure means in this context is that if two data points are part of the same natural cluster in the high-dimensional space, then t-SNE will aim to cluster them together in the two-dimensional space as well. But the relative distance *between* clusters shouldn't be trusted in the two-dimensional representation.

![T-SNE Embedding of MNIST](\assets\kaplan-notes-machine-learning\T-SNE_Embedding_of_MNIST.png)

For example, the image above shows a t-SNE projection of the [MNIST dataset](https://en.wikipedia.org/wiki/MNIST_database), which contains images of handwritten digits. Images are high-dimensional objects. In MNIST, the images are 28x28 pixels, where each pixel has an associated greyscale intensity---so each image is a 784-dimensional vector. There are ten clusters: one for each of the digits. If t-SNE works well, images that represent the same digit will get mapped to the same cluster. However, it's not necessarily true that a "1" is more similar to a "4" than it is to a "7" just because t-SNE maps the corresponding clusters closer together.

![MNIST Dataset Example](\assets\kaplan-notes-machine-learning\MNIST_dataset_example.png)

Generative modeling is also an example of unsupervised learning. With generative modeling, we not only want to learn the structure of the data, but also be able to produce new samples from the same underlying distribution (specifically, not just reproducing the data points that we happened to collect). An example of a generative model is a variational autoencoder. During training, a variational autoencoder has two networks: the encoder and the decoder. The encoder's job is to take a data point and map it to a distribution over latent space. The decoder's job is to take a latent space variable and recover the original data point. Then during inference, when you want to generate a new sample from the same underlying distribution as your data points, you can just sample from your prior distribution over the latent variable and decode it to get a new sample from the data distribution.

![Variational Autoencoder](\assets\kaplan-notes-machine-learning\Variational-Autoencoder.png)

In **supervised learning**, we are trying to learn a function that maps input to output. It's in many ways the most "basic" machine learning task. Many algorithms reduce down to "How do we turn this into a supervised learning task that we know how to do?"

For example, in linear regression, the input would be the $x$-coordinate and the output would be the predicted $y$-coordinate. We attempt to find the line that minimizes the error between the predicted $y$-values and the actual $y$-values in the sample.

![Linear Regression](\assets\kaplan-notes-machine-learning\linear-regression.png)

Another example would be classification. Going back to the MNIST example, you could train a neural network to take images of digits and predict which digit each image represents.

In **reinforcement learning**, we are trying to train an agent to perform optimally in a given environment. The fundamental tension in reinforcement learning is that the agent affects the world around it through short-term actions, but is trying to maximize a long-term objective: the cumulative reward that it receives. 

An example of a reinforcement learning problem is training a network to play Atari games. In a game like Pong, the objective is to win the game. If the agent performs an action every four frames (15 actions per second), there will be many actions within a rally of Pong. If the agent ends up winning the rally, what should the agent's takeaway be? What actions should the agent perform more or less often? Connecting the impact of an action done at the beginning of the rally to the final end result can be difficult. The problem of determining which actions actually led to the desired result and which were irrelevant is called the *credit assignment problem*. 

![Atari Games](\assets\kaplan-notes-machine-learning\atari-games.png)

In reinforcement learning, there are two main tasks that you can train the neural network to learn. You can train the neural network to learn the value function. There are both state value functions (given my current state, what is my expected cumulative reward?) and action value functions (given the current state I am in, how good would selecting this action be for me in the long run?). Alternatively, there are policy networks that take the current state as the input and return a probability distribution over actions.

Reinforcement learning setups that learn action value functions are called Q-learners. This works by training a network to learn the value of each action; then a simple policy would be to just take the value-maximizing action at each stage once fully trained (though in practice you wouldn't necessarily want to be that deterministic in order to be more robust to errors in learning the wrong value function).

Reinforcement learning setups that use policy networks learn the policy directly. This is done by watching the agent behave in accordance with the policy and having it perform more often the actions that do well and less often the actions that do poorly.

# Relevant Mathematics

As with all technical fields, machine learning research can get arbitrarily complicated (there's nothing better than reading a machine learning paper that invokes an obscure result from random matrix theory). That being said, the mathematical prerequisites to understand the basics are essentially just probability theory at the advanced undergraduate level. And considering the empirical nature of the field, this level of mathematical sophistication is all you really need to understand the heuristic reasons why machine learning models work.

What math is relevant to machine learning? Kaplan focuses on four subfields of mathematics:

1. **Probability Theory**

2. **Statistics**

3. **Information Theory**

4. **Optimization**

**Probability theory** is relevant because, in machine learning, the data is distributed according to arbitrarily complicated probability distributions. In each of the three main paradigms, the learning tasks are most naturally expressed in the language of probability theory.

In the case of unsupervised learning, we are learning the structure of the data. A canonical example of an unsupervised learning task is density estimation: where we attempt to learn a function that takes a data point and returns the density at that point: $f(x ; \theta) = p(x)$.

With supervised learning, the setup is that you have data $(x_i, y_i)$ which belongs to some probability distribution over $\mathbb{R}^d \times \mathbb{R}$. The model aims to learn the function $f(x) = \mathbb{E}[Y\|X = x]$. Given an input $x$, this is the expected value of the output $y$ (note that even though $p(y\|x)$ is a distribution, the conditional expectation of $Y$ is a function).

In reinforcement learning, we are training agents to perform optimally in a given environment. The environment is often random: the agent can take the same action in the same state and get different outcomes. Mathematically, what we call the environment in reinforcement learning is the probability distribution $P(s_{t+1}, r_{t}\| s_t, a_t)$: given a current state-action pair, this is the joint distribution over the immediate reward and the state we will transition to next. The policy is *also* a probability distribution: it's a probability distribution over the next action to take conditional on the current state: $\pi(a\|s)$.

There are also deep connections between **information theory** and machine learning. Let's say you are attempting to learn a probability distribution $p$ and you are fitting a model $q_\theta$ to the data. It would help to know how good (or bad) your current model $q_\theta$ is. This is the type of question studied in information theory. In information theory, there is a true distribution and a coding distribution, and the KL divergence tells us the discrepancy between the two distributions:

$$KL(p \| q) = \int dx \, p(x) \log \left( \frac{p(x)}{q(x)} \right)$$

We can say that our model $q_\theta$ is better the lower its KL divergence is with respect to the true distribution.

In **statistics**, we learn how to fit functions to data. A great example is linear regression. Let's say you have data that is generated of the form

$$Y = \beta X + \epsilon$$

where $X$ is the input, $\beta$ is the unknown parameter that we are trying to learn, $\epsilon$ is expectation-zero noise that is uncorrelated with the input, and $Y$ is the output. An algorithm that takes a set of data points $(x_i, y_i)$ and returns a best guess at the parameter value $\hat{\beta}$ that generated the data is called an *estimator*. The canonical estimator in the case of linear regression is the least-squares estimator: it corresponds to the parameter value that minimizes the squared distance between the model's predicted output and the actual output in the data. 

$$\hat{\beta} = \text{argmin}_\beta |Y - X \beta|^2$$

The difference between the learning problem of linear regression and the types of learning problems you see in machine learning is that with linear regression, we can derive a nice closed-form solution for the least-squares estimator as a function of the data, whereas in machine learning, the complexity of the models prevents us from obtaining closed-form solutions.

The final field is **optimization**. So far, I've talked a lot about how using data we can train neural networks to do various things, but haven't really discussed exactly *how* you use the training data to train the network.

Optimization describes the process by which the machine learning model uses data to minimize the loss function. While there is a large body of theory on optimization, neural network loss landscapes are highly non-convex, whereas our theory is mostly developed for the convex case. In the case of linear regression, we don't need iterative optimization because there is a simple closed-form solution for the optimal parameters given the data. But the generic problem in machine learning is a non-convex optimization problem. Roughly speaking, a minimization problem is convex if it looks like a parabola with one global minimum (which is also the only local minimum), whereas non-convex optimization problems have many local minima.

![Loss Landscapes](\assets\kaplan-notes-machine-learning\loss_landscapes.png)

An example of a loss function is the MSE (mean squared error) loss, commonly seen in supervised learning. 

$$\mathcal{L}(\theta) =  \frac{1}{N} \sum_{i=1}^N |y_i - f(x_i; \theta)|^2$$

If you notice, this is very similar to the least-squares loss function in the case of linear regression. The reason why this objective is harder has to do with the non-linearity of $f$ with respect to $\theta$. It helps to notice that the loss function can actually be decomposed into two functions: the model output as a function of $\theta$ and the loss given the output:

$$\mathcal{L} = \ell \circ f$$

where $\ell(\hat{y}) = \|y - \hat{y}\|^2$. The function $\ell$ is the same in both least-squares and MSE loss; it's just the square of the difference between the predicted output and the true output. Since $\ell$ is convex, the overall convexity of the loss depends entirely on the function $f$.

In the case of linear regression, the parameters define a linear mapping: keeping the data matrix fixed, the predicted output is a linear function of the parameters. The composition of a linear function with a convex function is convex---that's why the least-squares objective is convex. 

But in neural networks, $f$ is a non-linear function of the parameters $\theta$. The composition of a non-linear function with a convex function generically gives you a non-convex function. So the fact that neural networks can represent non-linear functions is intimately related to why they are so hard to train.

Because we can't solve for the optimal set of parameters in one go, we instead use some form of gradient descent: we find the direction relative to our current position that decreases the loss and nudge the parameters in that direction. For example, this is the algorithm for gradient descent, the simplest optimization algorithm.

$$\theta_{t+1} = \theta_t - \eta \nabla_\theta \mathcal{L}$$

There are many questions one could ask: What is the optimal step size? What are the strengths and weaknesses of different optimization algorithms? What does momentum add? Optimization is in a unique position where it's one of the most important aspects of machine learning, but also one of the least understood.


# Miscellaneous

He also talks about various normalization techniques like layer norm and batch norm. In batch normalization, you shift and scale the activations so that the statistics across the batch are normalized (i.e. you normalize across different examples at each feature). With layer normalization, you instead normalize across the features for one given example so that its pattern of activations is normalized. These normalization techniques are used because having activations that are centered and of the right magnitude helps to maximize the gradient signal during training.

There is also brief discussion of general architectures like recurrent neural networks (RNNs), convolutional neural networks (CNNs), and transformers. Recurrent neural networks are what are called sequence-to-sequence models: they take a sequence of inputs and return a sequence of outputs. A task that you might train an RNN for is speech recognition: given an audio file (represented as a sequence of audio frames), the RNN outputs a sequence of text characters or words corresponding to what was spoken. If the recurrent neural network acted on each time step independently, it wouldn't be a true sequence model. To capture sequential dependencies, the RNN keeps track of what is called the hidden state. The hidden state is a type of memory that aims to summarize all the relevant information from previous inputs.

![RNN](\assets\kaplan-notes-machine-learning\RNN.png)

CNNs are often used to process image data. They are called convolutional neural networks because they mathematically embody convolution operations.

Transformers are similar to RNNs in that they are also sequence-to-sequence models. Transformers were, at the time of the writing of these notes, the new kid on the block---and they certainly haven't waned in popularity since. They were introduced in a famous paper called "Attention Is All You Need". They work through an attention mechanism: each element in the input sequence can "attend to" (i.e., gather information from) all other elements in the sequence. The key insight of transformers is that having everything attend to everything else allows the model to capture powerful relationships within the sequence---and this becomes especially powerful in the context of deep learning, when you stack multiple attention layers together.

One of the eerie things about the lecture notes is that a lot of the subsections are very similar to posts on this blog. Many of the sections on probability theory adopted very similar framings and even verbiage to previous blog posts that I had written before reading the lecture notes.

![Bayes Theorem](\assets\kaplan-notes-machine-learning\bayes-theorem.png)

One of the meta-themes I am interested in exploring in this blog is: What is the "physics mindset"? There is this folklore that an education in physics is uniquely good at cultivating a specific type of model-based, abstract reasoning. Physicists are known for asking questions like: Are there conserved quantities? Are there symmetries? Can we model this as a harmonic oscillator? What about as a Gaussian? What is the first-order approximation? The second-order approximation? Quantitatively, under what circumstances is the first-order approximation a good approximation for the underlying reality we are trying to model? 

This sounds plausible---but is it true? Will people of differing intellectual backgrounds---physics, pure math, engineering, statistics, computer science, linguistics, psychology, neuroscience, philosophy---when dropped into the setting of machine learning reliably adopt different perspectives and feel most comfortable with the conceptual frameworks that match their original background?



