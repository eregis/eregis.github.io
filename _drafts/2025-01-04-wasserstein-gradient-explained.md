---
layout: post
title: "The Wasserstein Gradient Explained"
date: 2025-01-04
mathjax: true
---
# Wasserstein Gradient Explained

Understanding the Wasserstein gradient requires building up several layers of concepts, starting from basic calculus and moving to measure theory. Let's explore this step by step.

## The First Variation
We start with a functional F that maps probability measures to real numbers:

```
Definition 5.9 (First variation). Let F : P2,ac(Rd) → R be a functional. The first variation of F at μ, denoted δF(μ) : Rd → R, is the function defined by:

lim
ε↘0
F(μ + εχ) − F(μ)
ε =
Z
δF(μ) dχ

for all signed measures χ such that μ + εχ ∈ P2,ac(Rd) for all sufficiently small ε.
```

## Building Up From Simple Derivatives
To understand this object, let's build up from simpler concepts we're familiar with:

1) Single Variable Derivative:
   - Basic derivative: f'(x) = lim_{h→0} [f(x + h) - f(x)]/h
   - This measures how a function changes when we perturb its input

2) Multivariable Case:
   - Directional derivative: ∂_v f(x) = lim_{h→0} [f(x + hv) - f(x)]/h
   - v is a vector giving the direction

3) Functional Derivative:
   - Instead of perturbing by a number or vector, we perturb by a measure χ
   - The derivative is a function that we integrate against perturbations

## Understanding Through Covectors
A key insight is that for any function(al) from A → R, the associated covector will be of the same "type" as objects in the input space:

- Single variable function: covector is a real number 
- Multi-variable function: covector is a tuple of numbers
- When input is a measure: covector is a function over the space where the measure lives

All of these covectors can be understood as functions:
- Single variable case: function {1} → R
- Multivariable case: function [1:n] → R
- Measure case: function Rd → R

The topology of Rd isn't crucial here - it's just providing an uncountable index set for our "arguments".

## Time Evolution and Measure Derivatives
When we consider curves of measures (μt)t≥0, we can write:
```
μt+ε ≈ μt + ε ∂tμt
```
where ∂tμt is the time derivative. This derivative can be made rigorous in several ways:

1) Through densities
2) Through distributions
3) Through weak derivatives (often most useful):
   ```
   d/dt ∫φ dμt = ∫φ d(∂tμt)
   ```

## The Wasserstein Gradient
Now we come to the key object:

```
Proposition 5.10. Let F : P2,ac(Rd) → R be a functional with first variation δF. 
Then, the Wasserstein gradient of F is the vector field ∇∇F(μ) : Rd → Rd defined by
∇∇F(μ) = ∇δF(μ)
where ∇ on the right-hand side denotes the usual Euclidean gradient.
```

Two important points:
1) The first variation is what we normally associate with gradients
2) The Wasserstein gradient has no direct analogy in finite dimensions - it's using the topology of Rd in a fundamental way

## Understanding the Two Gradients
This leads to a key insight about the different structures being used:

- First variation: uses the differential structure of R (the codomain)
- Wasserstein gradient: uses the differential structure of Rd (the domain)

Crucially, the Wasserstein gradient is not a vector field in the space of measures - it's a vector field in the base space at a given measure.

## Why This Matters: The Final Synthesis
The importance becomes clear when we consider how measures evolve:

1) We can express the change in the functional using the first variation (covector)
2) But changes in measure must come from flowing mass continuously (Fokker-Planck equation)
3) Since measure changes are expressed via vector fields, changes in our functional can be too
4) The Wasserstein gradient is exactly the object we need for this

This is demonstrated in the key equation:
```
∂tF(μt) = ∫δF(μt) ∂tμt = -∫δF(μt) div(μtvt) = ∫⟨∇δF(μt), vt⟩ dμt = ⟨∇δF(μt), vt⟩μt
```

The Wasserstein gradient emerges naturally because we're restricting ourselves to changes in measure that come from flowing mass around smoothly. It's the object we need when we want to work with actual trajectories in the space of measures, rather than arbitrary perturbations.