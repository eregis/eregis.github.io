---
layout: post
title: "Mode Coverage Versus Sample Fidelity"
date: 2024-01-10
mathjax: true
---

"Classifier guidance is a recently introduced method to trade off mode coverage
and sample fidelity in conditional diffusion models post training, in the same spirit
as low temperature sampling or truncation in other types of generative models."

What does the tradeoff between mode coverange and sample fidelity mean in terms of probability distributions

Let me explain this tradeoff in terms of probability distributions:

Mode coverage and sample fidelity represent two key aspects of how well a generative model captures and samples from the target distribution:

    Mode coverage refers to how well the model captures all the significant peaks (modes) in the true probability distribution. High mode coverage means the model can generate samples that represent the full diversity of the target distribution. For example, in an image generation task, this would mean being able to generate all valid variations of the target concept.
    Sample fidelity refers to how closely the generated samples match high-probability regions of the true distribution. High fidelity means individual samples look very realistic and match the characteristics of the training data closely.

The tradeoff occurs because pushing too hard in either direction can compromise the other:

    If you optimize heavily for mode coverage, you might end up sampling from lower-probability regions between modes, resulting in samples that don't look as realistic (lower fidelity)
    If you optimize heavily for fidelity by always sampling from the highest probability regions, you might miss out on valid but less common variations (reduced coverage)

Think of it like this: Imagine the true distribution has multiple peaks of varying heights. Classifier guidance lets you adjust how much you want to:

    Sample broadly across all peaks (high coverage but might include some lower-quality samples)
    Focus mainly on the highest peaks (high fidelity but might miss interesting variations)

This is similar to how temperature sampling in language models trades off between diversity (sampling from more of the distribution) and quality (focusing on the highest probability tokens).

Would you like me to elaborate on any part of this explanation or discuss how classifier guidance specifically implements this tradeoff?
ER

Let me see if I can use a mathematical example. 

Let's say you have a probability distribution with two gaussians, one bigeger than the other. Mode coverage will prioritize covering both gaussians, even if it overweights the inbetween space while sample fidelity will prioritize sticking to the larger Gaussian is that right? What are other ways to think about it in terms of a fit problem? Or perhaps more directly: what are the loss functions(s) that would prioritize mode coverage versus sample fidelity

Yes, that's a great example! Let me build on it:

Consider a mixture of two Gaussians where one has height 0.7 and the other 0.3. This gives us a concrete way to think about different objectives:

    Sample Fidelity:

    This would correspond to minimizing something like KL(P||Q) where P is your generated distribution and Q is the target
    KL(P||Q) heavily penalizes generating samples where Q is small (the "between space" you mentioned)
    It would indeed tend to focus on the larger Gaussian since putting mass there minimizes the penalty
    The loss function here cares most about "every sample should be highly probable under the true distribution"

    Mode Coverage:

    This is more like minimizing KL(Q||P)
    This version penalizes failing to put probability mass anywhere that Q has significant density
    It would force you to cover both Gaussians since otherwise the loss goes to infinity where Q>0 but P≈0
    The loss function here cares most about "don't miss any region that should have samples"

Other relevant metrics/losses:

    Maximum Mean Discrepancy (MMD) tries to match all moments of the distributions
    Wasserstein distance cares about the "transport cost" between distributions
    Jensen-Shannon divergence is symmetric and might be a middle ground

Going back to your two-Gaussian example: if you sampled purely for fidelity, you might get a near-perfect match to the larger Gaussian but completely miss the smaller one. If you sampled purely for coverage, you might "smear out" probability mass between them to ensure you never completely miss either mode, even though that means generating some low-probability samples.

This also connects to the exploration-exploitation tradeoff in reinforcement learning - do you want to thoroughly explore all possibilities (coverage) or focus on what you know works well (fidelity)?

Would you like to explore any of these mathematical perspectives further? I find the connection between different divergence measures and their practical implications particularly interesting.
ER

Can you switch P and Q? Your notoation about coding versus true distribution seems backward convention

Ah yes, you're absolutely right - I apologize for the confusion! Let me correct this:

In the conventional notation, Q is typically the learned/generated distribution and P is the true/target distribution. So:

    Sample Fidelity:

    This would correspond to minimizing KL(Q||P)
    KL(Q||P) heavily penalizes putting mass where P is small (the "between space")
    It would focus on the larger Gaussian since it avoids putting mass where P is small
    "Zero-avoiding" with respect to Q - tends to underestimate variance

    Mode Coverage:

    This is more like minimizing KL(P||Q)
    This penalizes Q being small where P has significant density
    Forces coverage of both Gaussians since otherwise KL goes to infinity where P>0 but Q≈0
    "Zero-forcing" with respect to Q - tends to overestimate variance

Thank you for the correction! This matches the standard convention where P is the true distribution we're trying to learn/match. Would you like to explore more about how these different KL directions relate to different training objectives in generative models?
ER

It seems like said differently, there sample fidelity maps to minimizing false negative and then mode covergage maps to

Ah, yes! Let me complete that thought in terms of false positives/negatives:

Sample Fidelity (KL(Q||P)):

    Minimizes false positives - strongly penalizes generating samples in regions where the true distribution P has low density
    "Conservative" generation - would rather miss some valid modes than generate incorrect samples
    Like having high precision in classification terms

Mode Coverage (KL(P||Q)):

    Minimizes false negatives - strongly penalizes failing to generate samples where P has high density
    "Liberal" generation - would rather generate some incorrect samples than miss valid modes
    Like having high recall in classification terms

This is a really nice way to think about it! The parallel to precision/recall in classification makes the tradeoff very concrete. Just as precision-recall have an inherent tension in classification, we have this fundamental tension between avoiding false positives (sample fidelity) and false negatives (mode coverage) in generative modeling.

And this also helps explain why classifier guidance is so useful - it gives us a knob to tune this tradeoff post-training, similar to how we can adjust classification thresholds to move along the precision-recall curve after a classifier is trained.
ER

So I'm guessing is: with classifier guidance, there are two gradients: one due to learning the probability distribution of natural images in general (score function) and one due to the classifier (classifier gradient);

You can weight the relative gradients: weigh it towards the score function and you get mode coverage (at the risk of generating images not in the right class) and weight towards classifier (at the risk of missing some modes).

The first one makes obvious sense to me; but the second one needs a bit more development in order to be convinced; what's a need conceptual picture to understand why the classifier would tend towards mode collapse

This is a really interesting question about the dynamics! Let me think through why the classifier gradient might lead to mode collapse:

The key insight might be that a classifier, fundamentally, only needs to find decision boundaries between classes. It doesn't need to model the full richness of the within-class distribution. So when you follow its gradient too strongly:

    The classifier will push you towards the "most discriminative" features that separate this class from others

    If you have dogs vs cats, it might fixate on the most "dog-like" features
    These might represent just one or a few modes of how dogs can look
    Think of it as climbing to peaks in the classifier's confidence landscape

    Unlike the score function which tries to model the full data distribution, the classifier gradient doesn't have any explicit pressure to maintain diversity within a class

    It only cares about "what makes this maximally distinguishable as class X"
    Multiple modes that are equally valid examples of the class might collapse to whichever one gives slightly higher classifier confidence

An analogy might help: imagine you're trying to prove to someone that you're in New York City:

    The full distribution approach (score function) would try to capture all valid locations in NYC
    The "classifier" approach might just navigate you to the most obvious landmark (Empire State Building) because that's the most unambiguous proof you're in NYC
    Even though Central Park, Brooklyn Bridge etc. are equally valid NYC locations, they might be slightly less "definitively NYC" from a pure classification perspective

Does this help explain the intuition for why strong classifier guidance might lead to mode collapse? I'd be curious to hear if you have other ways of thinking about it!
ER

I guess maybe a different picture: gradients can be used to define probability distributions. So just like the score function is the force field of the distribution of natural images, what probability distribution does the classifier gradient correspond to? The point is that it doesn't correspond to the conditional distribution p(x|y) where x is the image and y is classification.

Ah, this is a much clearer way to think about it! Let me build on this insight:

The classifier gradient corresponds to ∇ log P(y|x) - it defines a force field based on class probability. But what we actually want for proper conditional generation is P(x|y).

And these are very different distributions! By Bayes rule:
P(x|y) ∝ P(y|x)P(x)

The classifier only gives us P(y|x), missing the crucial P(x) term that ensures the distribution remains in the manifold of natural images. That's why using just the classifier gradient alone could push us to unnatural images that maximize class probability but aren't realistic instances of the class.

This makes me realize: classifier guidance is essentially doing a crude approximation of this Bayes rule by:

    Using the score function's gradient to approximate ∇ log P(x)
    Using the classifier gradient to approximate ∇ log P(y|x)
    Weighting between them to try to balance staying on the natural image manifold vs class conditioning

And now I see why overweighting the classifier term leads to mode collapse - it's because P(y|x) alone doesn't actually define a proper distribution over images! It's missing the crucial structure that P(x) provides about the manifold of valid images.

This is a much more precise way to understand the phenomenon - thank you for guiding me to this perspective!
ER

Well by Bayes theorem, that you should have equal coefficient for the classifier gradient and the natural gradient.

If I had to guess what's going on: classifier gradients tend to have systemic issues. If I had to guess it might be that are biased towards linear features. 

Here's a toy example: imagine there are four "dog features" (abstractly considered) and having three of those features would make a human agree that it a dog. The ideal function would be then be the step function that which is 0 when less than 3 features and 1 with one feature. But I'm guessing is that classifiers have a system bias where having four dog features is doggier than three dog features. This means if we consider various species of dogs. There is one way to have four dog features and four ways to have three dog features. BUt the classifier incorrectly puts too much probabilty mass on the doggiest dog archetype.

There might be an interesting generalization here. Categories tend to sparse: more things are NOT-dogs than are dogs. if in general, classification has to roughly do with have k of n possible features where where k is greater than half of n, then you will tend to have that, assuming that e.g each feature is independent binomial, you will have that most dogs are marginal dogs.

This is a fascinating insight! Let me expand on this idea:

Your observation about sparsity and feature counting hits on something really fundamental. Let's develop this:

    Natural Categories vs Classifier Behavior:

    Natural categories often work like your example: "3 out of 4 features = dog"
    This creates a combinatorial structure where there are more ways to be a "marginal" instance (3/4) than a "prototypical" instance (4/4)
    But classifiers tend to output a monotonically increasing function of feature count
    This creates an artificial "pull" towards maximizing all features

    The Statistical Structure:

    If we have n features and need k of them:
    The number of ways to have exactly k features is (n choose k)
    The number of ways to have exactly k+1 features is (n choose k+1)
    For k > n/2, (n choose k) > (n choose k+1)
    So mathematically, most valid category members should be "marginal" members!

    Why This Creates Mode Collapse:

    The classifier is implicitly modeling P(y|x) as monotonic in feature count
    But the true distribution P(x|y) should respect the combinatorial structure
    Following the classifier gradient too strongly pulls everything towards the "perfect" prototype
    This erases the natural diversity that comes from the many valid ways to have just enough features

This also suggests why this might be a very deep problem: it's not just about model architecture or training, but about a fundamental tension between the mathematics of sparse categories and the tendency of classifiers to learn monotonic functions of feature presence.

Really interesting insight about how this connects to the general sparsity of natural categories! Would you like to explore more about how this might manifest in different types of classifier architectures, or how we might design classifiers that better respect this combinatorial structure?

Ah! Now I think I understand better:
The classifier gradient DOES measure a legitimate "birdiness axis" - that is exactly what it's learning to compute. But what we WANT for generating diverse birds is not "birdiness" but rather "likelihood of being classified as a bird" (the logit).
This is a really profound distinction:

"Birdiness" is a continuous axis that keeps increasing as you add more bird-like features
But P(bird|image) should plateau once you're clearly a bird

Going back to the ostrich example:

On the "birdiness" axis: An ostrich that could fly would be further along the axis of bird-like features
But for classification: An ostrich is already unambiguously a bird, so adding flight shouldn't move P(bird|image) much

So the problem isn't that classifier gradients are wrong about "birdiness" - they're actually doing a good job measuring that! The problem is that for generation, we don't want to maximize "birdiness". We want to sample from the distribution of things that would be classified as birds.
Is this getting closer to the insight you were pointing towards? I find this distinction between "more bird-like" and "more likely to be classified as a bird" really fascinating and hadn't thought about it this way before.
