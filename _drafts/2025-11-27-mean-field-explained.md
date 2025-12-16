---
layout: post
title: "Post Template"
date: 2025-01-01
mathjax: true
---
 # Cengiz Pehlevan - Mean-field theory of deep network learning dynamics and applications to neural scaling laws

  > I will review recent developments in obtaining a mean-field description of the high-dimensional learning dynamics of deep neural networks. These mean-field theories result from various infinite limits, including width, depth and attention-heads. I will present applications of these ideas to neural scaling laws in lazy and feature-learning regimes.

  The way that we train neural networks is that optimize them to minimize some loss function. Because the loss functions of neural network loss functions is very complicated, use some form of gradient descent to optimize them: rather than trying to solve for the minimum of the loss function in one-go, we compute the direction which minimizes the loss and 

  We are interested in trajectory in parameter space as the network minimizes the loss. However, understanding this is in the context of mean field theory is very complicated for many reaosns, but I want to focus on two. One is the gradient descent is a discrete algorithm (which are harder to analyze thean their continuous analogues). Second is that the dynamics of each of the indivudla neurons are highly coupled. Imagine that you hae a simple neural network with one hidden layer:

  $$f(x ; w) = \sum \sigma(w \cdot x)$$. 

  We often represent the first layer as a weight matrix, but you conceive of teh weight matrix as a set of N neurons. Each neuron represents a direction into which the project the data. You can think of these directions in which to project the data as trying to detect features. Some aspects of the data are more meaningful for the target function than others, and over the course of training one would hope that the network learns to  shift the neurons such that they are aligned with the meaningful features of the data.

  An algorith is gradient descent which can be represented of the form

  Let's say that we have N neurons each of them d dimension, then the gradient descent equation above is representing the dynamics of the Nd-dimension vector representing the state of the entire neural network. But we could also decompose this into gradient associated with each neuron

  $$w^(1)_{t+1} = w^{1}_t - \eta \nabla_w_1 L(w)
  

  w^(N)_{t+1} = w^{1}_t - \eta \nabla_w_1 L(w)$$

  This is mathematically identical to the full gradient descnet equation above, but it suggests an interesting physical picture: eavh of the neurons is like a particl eliving in a d-dimensional space and the L(w) is joint Hamiltonian on the N particles. Because the Loss function between the different neurons is coupled (it isn't linear seperable based on neurons), we have what are effectively interactions between the different 

  (For an intuition for why that might be the case: recall that the neurons can be thought of as trying to learn features of the data: dimension in which to project the data that are relevant to learning the target function. If one neuron has already learned a relevant feature direction, then it would make some intuitive sense for other neurons to try a learn other features of the data that haven't been learned yet. This could be visualized as a repulsive force between the neuron that has learned the feature and the other neuron weights.)

  This is where the payoff comes in: in the limit that the number of neurons N goes to infinity, things actually get simpler, not harder. When there are infinite particles, rather than considering the complicated couplings between the dynamics between all the neurons, we can actually just treat the neurons as one object $p(w)$. This is mean field theory, often used in many-body systems: we can treat each particle as experiencing the field it would get on average from the the other neurons.

  By being suitably careful about taking the N to infinity limit, we can then understand the training dynamics of the network by understanding the continuous time evolution of distribution $p(w)$. (Apparently, the mathematics is similar to those used in plasma physics, the Vlasov equation, where you have a fluid of charged particles that interact via long-range Coulombic forces.)

He applies this mean-field framework for both the lazy and feature-learning regimes.