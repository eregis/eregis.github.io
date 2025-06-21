---
layout: post
title: "Real Space Renormalization Group Explained"
date: 2025-05-21
mathjax: true
---
*The following is based on a solution to a homework problem.*


The renormalization group is an "apparatus" that is used to analyze how the physics of a system changes as a function of scale. When we 

As far as I'm aware there are two types of renormalization group calculations: real-space renormalization and momentum-space renormalization. In both types of renormalization, we have degrees of freedom that are random variables. In real-space renormalization, the random variables are understood to represent spatial variables. For example, you can have the value of the spin at a lattice site would be a real-space renormalization space. In momentum space renormalization, we have that
the spin variables.


At a high-level, a real-space renormalization group calculation follows the flow chart shown below:



The Hamiltonian of a system gives rise to a probability distribution (through the Gibbs measure) over a set of microscopic degrees of freedom. We can then define a \textit{coarse-graining procedure}, which is simply a function that maps our original set of random variables to a reduced set of random variables. The function must be chosen carefully to agree with the physical intuition of the problem (e.g it must respect the symmetry of the original Hamiltonian). Using the standard change of variables formula, we can then find the probability distribution over our new coarse-grained degrees of freedom. The non-trivial part of the calculation comes next: once we have our new measure defined on the coarse-grained degrees of freedom, we must solve an inverse problem to find the effective Hamiltonian that would result in this probability distribution. The hope is that the new effective Hamiltonian for the coarse-grained degrees of freedom will have the same functional form as the original Hamiltonian, only with different values for coupling constants. If the coarse-grained Hamiltonian has the same functional form, we can make statements about the limiting behavior as we continually coarse-grain---this corresponds to finding the fixed points in our renormalization group flow.

We are asked to perform a decimation RG transformation with $\ell = 2$. With decimation, the coarse-graining procedure retains only the random variables at even lattice sites (essentially, the coarse-graining function is a projection). We will use the convention that lowercase Roman letters denote indices of the original random variables, and uppercase Roman letters denote indices of the coarse-grained lattice.

$$
\begin{align}
s_I' &= f(\{s\}) \\
&= s_{i = 2I}
\end{align} 
$$

For our renormalization procedure to be well-defined, we need to make use of a characteristic property of infinite sets: their proper subsets can be of the same cardinality as the original set. Put another way: when we coarse-grain, we retain only half of our degrees of freedom. But since we still have infinitely many lattice sites (countably infinite), our original system and our coarse-grained system have the same number of degrees of freedom. This is necessary for the Hamiltonian of our original system and the coarse-grained Hamiltonian to be commensurate.

\begin{figure}[htb]
   \centering
   \includegraphics{decimation-RG.png}
   \caption{Illustration of the decimation RG transformation with $\ell = 2$. The upper lattice shows the original system with even sites (blue) and odd sites (gray). The lower lattice shows the coarse-grained system where only even sites are retained, becoming the new degrees of freedom $s'_I$.}
   \label{fig:decimation-RG}
\end{figure}

So far, everything I've done follows Goldenfeld's procedure. But this is where my approach will diverge. In Goldenfeld, he finds the renormalized Hamiltonian by taking the "partial trace" over Boltzmann factors. Instead, I'll use a more formal, probability theory-based approach where I'll apply the change-of-variables formula to find the probability distribution $p'(\{s'_I\})$ over the coarse-grained random variables. Once I find an expression for $p'$, I'll show that it can be expressed as a Gibbs measure derived from a renormalized Hamiltonian with the same functional form as our original Hamiltonian, but with a different value for the coupling constant. Since I arrive at the same final answer as Goldenfeld, our two approaches must be formally equivalent. I'll briefly explain my interpretation of what is "really" happening when we perform a partial trace.

If $X$ and $Y$ are two random variables such that $T(X) = Y$, then the change of variable formula\footnote{For a derivation of the change-of-variables formula, please refer to this blog post: \url{https://eregis.github.io/blog/2024/08/01/functions-random-variable.html}}---which relates the density $p_X$ of $X$ to the density $p_Y$ of $Y$---can be expressed as:

$$p_Y(y) = \int dx \ \delta(y - T(x)) p_X(x)$$

Here's an intuition for the change-of-variables formula: When we marginalize, we multiply by a length and remove a degree of freedom. When we insert a Dirac delta, a delta has units of inverse-length and we are adding a degree of freedom.

Another interpretation is that when you are inserting a Dirac delta, you are augmenting your original distribution over $x$ into a joint distribution over both $x$ and $y$. This is because the Dirac delta $\delta(y - T(x))$ is \textit{precisely} the conditional distribution $p(y|x)$. And by the chain rule, $p(x,y) = p(y|x) p(x)$. So when you are integrating with respect to $x$, you are simply marginalizing the joint distribution $p(x,y)$, giving you $p(y)$.

"Taking the trace" is nothing more than the discrete analog of marginalization. When Goldenfeld is performing a "partial trace," what he is describing is a procedure where he marginalizes over only a subset of the microscopic degrees of freedom. This approach isn't incorrect, but I think it's conceptually clearer to think of the partial trace as really being composed of the two steps outlined above: inserting a Dirac delta for each degree of freedom of our coarse-grained random variables and then marginalizing over \textit{all} the microscopic degrees of freedom of the original distribution. Said another way: We're not tracing over half of our original degrees of freedom. Rather, we're tracing over all of our original degrees of freedom and replacing them with new degrees of freedom. It just so happens that because we choose decimation as our coarse-graining procedure, the coarse-grained degrees of freedom happen to be equal in value to a subset of our original degrees of freedom.

(The paragraph above is my perspective on real-space RG. With momentum-space RG, I actually do think that the partial-trace/partial-marginalization perspective is the right way to be thinking about things.)

Putting the conceptual discussion behind us, we are now ready to perform the change of variables in order
calculate $p'(\{s_I'\})$, the probability distribution of the coarse-grained random variables. Recalling that the trace is the discrete analog of marginalization, we have that:

$$p'(\{s_I'\}) = \text{Tr}_{\{s_i\}} \ \delta(s_I' - f(\{s_i\})) \  p(\{s_i\}) $$

(One should note that, as we are working with discrete random variables, the Dirac delta should \textit{really} be a Kronecker delta. More proper would be to notate the above as $\delta_{s_I', f(\{s_i\})}$. We will keep the Dirac delta notation, both to maintain consistency with Goldenfeld and because it is less cluttered to look at.)

Substituting in our particular choice of coarse-graining function $f$, we then have that:

$$p'(\{s_I'\}) = \text{Tr}_{\{s_i\}} \ \delta(s_I' - s_{i = 2I}) \ p(\{s_i\})$$

For the probability distribution of our microscopic degrees of freedom, we have that:

$$\begin{align}
p(\{s_i\}) &= \frac{1}{Z}\exp\mathcal{H}(\{s_i\}) \\
&= \frac{1}{Z} \exp \left (K \sum_i \delta_{s_i, s_{i+1}} \right )
\end{align}$$

It is useful at this step to break up our trace into two traces over the even and odd lattice sites:

$$\text{Tr}_{\{s_i\}} = \text{Tr}_{\{s_{\text{odd}}\}} \, \text{Tr}_{\{s_{\text{even}}\}}$$

One should note that, in exact analogy to the case when we are integrating, we have the following identity for the trace:

$$\text{Tr}_{\{x\}} \left[ \delta(y - x) f(x) \right] = f(y)$$

Then we have that:
$$
\begin{align}
p'(\{s_I'\}) &= \text{Tr}_{\{s_i\}} \delta(s_I' - s_{i=2I}) \left[ \frac{1}{Z} \exp \left ( K \sum_i \delta_{s_i, s_{i+1}} \right ) \right]\\
&= \frac{1}{Z} \text{Tr}_{\{s_i\}} \delta(s_I' - s_{i=2I})   \exp \left ( K \sum_{I} \left[\delta_{s_{i = 2I}, s_{i = 2I+1}} +  \delta_{s_{i = 2I + 1}, s_{i = 2I +2}} \right] \right )\\
&= \frac{1}{Z} \text{Tr}_{\{s_{\text{odd}}\}} \, \text{Tr}_{\{s_{\text{even}}\}} \delta(s_I' - s_{i=2I})   \exp \left ( K \sum_{I} \left[\delta_{s_{i = 2I}, s_{i = 2I+1}} +  \delta_{s_{i = 2I + 1}, s_{i = 2I +2}} \right] \right )\\
&= \frac{1}{Z} \text{Tr}_{\{s_{\text{odd}}\}} \exp \left ( K \sum_{I} \left[\delta_{s'_I, s_{i = 2I+1}} +  \delta_{s_{i = 2I + 1}, s'_{I+1}} \right] \right )\\
&= \frac{1}{Z} \text{Tr}_{\{s_{\text{odd}}\}}\prod_I \exp \left( K\left[\delta_{s_I', s_{i=2I +1}} + \delta_{s_{i=2I +1}, s_{I +1}'}\right]\right) \\
&= \frac{1}{Z} \prod_I \text{Tr}_{\{s_{i=2I+1}\}}  \exp \left( K\left[\delta_{s_I', s_{i=2I +1}} + \delta_{s_{i=2I +1}, s_{I +1}'}\right]\right) \\
&= \frac{1}{Z} \prod_I \psi(s_I', s_{I+1}') \\
\end{align}
$$
In the step where we interchange the order of the product over $I$ and the trace over the odd microscopic degree of freedoms, we are allowed to do this because each term in the product is a function of only one odd variable. 

All that's left is to find an expression for $\psi(s_I', s_{I+1}')$. It's a simple function to evaluate. While there are theoretically $q^2$ different cases to analyze (corresponding to $q$ possible states for each of our two coarse-grained random variables), in actuality, there are only two unique cases: when the coarse-grained variables are aligned and when the coarse-grained variables are unaligned.

$$
\psi(s_I', s_{I+1}') = \begin{cases}
   e^{2K} + (q -1) & \text{when } s_I' = s_{I+1}' \\
   2e^K + (q-2) & \text{when } s_I' \neq s_{I+1}'
\end{cases}
$$

Ignoring the normalization constant $Z$ for the moment, we have now found an expression for $p'(\{s_I'\})$! Next, we want to solve the inverse problem where we express $p'$ as a Gibbs measure with Hamiltonian $\mathcal{H}'$ where $\mathcal{H}'$ has the same functional form as $\mathcal{H}$.

$$\begin{align}
p'(\{s_I'\}) &= \frac{1}{Z'} \exp \mathcal{H}' \\
&= \frac{1}{Z'} \exp \left (K' \sum_I \delta_{s_I', s_{I+1}'} \right )
\end{align}$$

Note that if you add a constant to the Hamiltonian, it does not change the resultant probability density. So we actually have a choice in how to represent our ansantz. One choice would be the one represented above: where there is no constant term in the Hamiltonian. But the most common choice (often made implicitly) is to add a constant such that the partition function of our coarse-grained distribution matches the partition function of our microscopic degrees of freedom.

$$
\begin{align}
p'(\{s_I'\}) &= \frac{1}{Z} \exp \left (K' \sum_I \left ( \delta_{s_I', s_{I+1}'}+ C' \right) \right) \\
&= \frac{1}{Z} \prod_I \exp \left (K'(\delta_{s_I', s_{I+1}'} + C') \right )
\end{align}
$$

(If your eyebrow is raising at the casual insertion of a finite constant into an infinite sum, recall that our partition function is \textit{already} infinite. I assume the formal way to handle this would be to wait on passing to the $N = \infty$ limit, make the partition functions commensurate for $Z_N = Z_N'$, and then pass to the limit. In any case, it's probably fine.)

This choice is both mathematically convenient and physically motivated. It's convenient because when we set the ansatz above equal to the form of the density that we got from the change-of-variables formula, the $Z$s on both sides will cancel. It's physically motivated because a perspective on coarse-graining is that we are viewing the \textit{same} system, but at \textit{different} scales. Since it's the same system being represented, it's perhaps logical that the total free energy (which is related to the partition function) doesn't change under coarse-graining. It also allows us to physically interpret the added-on constant $C'$: it's the "internal free energy"---the free energy of the microscopic degrees of freedom that we coarse-grained over.

Setting our ansatz equal to our derived formula, we have:

$$
\frac{1}{Z} \prod_I \exp \left( K' (\delta_{s_I', s_{I+1}'} + C') \right) = \frac{1}{Z} \prod_I \psi(s_I', s_{I+1}') \longrightarrow \exp\left( K' (\delta_{s_I', s_{I+1}'} + C') \right) =  \psi(s_I', s_{I+1}') $$

To solve for $K'$ and $C'$, we just need to set our ansatz equal to $\psi(s_I', s_{I+1}')$ for each of the two cases. Doing so, we yield the following two equations:

$$
\begin{align}
e^{K' + C'} &= e^{2K} + q -1 &\text{ when } s_I' = s_{I+1}'\\
e^{C'} &= 2 e^K + q - 2 &\text{ when } s_I' \neq s_{I+1}' \\
\end{align}$$

To solve for $C'$, we can take the log of both sides of the second equation:

$$e^{C'} &= 2 e^K + q - 2\longrightarrow C' = \ln \left( 2 e^K + q - 2 \right )$$

To solve for $K'$, we can divide the first equation by the second equation:

$$e^{K'} = \frac{e^{2K} + q -1}{2 e^K + q - 2} \longrightarrow K'  = \ln \left(\frac{e^{2K} + q -1}{2 e^K + q - 2}\right)$$

What I like about being explicit about working with measures is that it gives a hint on how to proceed in cases where we aren't so lucky to have our coarse-grained measure belong to the same parametric family as our original measure. It would seem that in more general coarse-graining procedures where the renormalization is not exact, we are in practice solving some sort of variational problem where we try to find the ansatz Hamiltonian that best approximates the coarse-grained system. This variational perspective on RG is nice because it not only makes contact with a large statistical inference literature (which is surely gleaming with insights and received wisdom), but also because it provides a systematic framework for approximate renormalization schemes. 

\item 

Fixed points of our renormalization group flow correspond to values of $K$ where $K' = K$. The 1-D Potts model has two fixed points: $K = 0$ and $K = \infty$. Let $K'(K)$ denote the value of the coupling constant $K'$ that results from one iteration of our RG flow starting from the coupling constant $K$. We then have that for $K=0$:

$$\begin{align}
K'(0) &= \ln \left(\frac{e^{0} + q -1}{2 e^0 + q - 2}\right) \\
&= \ln \left(\frac{q}{q}\right) \\
&= 0
\end{align}$$

And for $K = \infty$:

$$\begin{align}
K'(\infty) &= \lim_{K \rightarrow \infty} \ln \left(\frac{e^{2K} + q -1}{2 e^K + q - 2}\right) \\
&= \lim_{K \rightarrow \infty} \ln \frac{e^K}{2} \\
&= \infty
\end{align}$$

The $K =0$ fixed point corresponds to the disordered phase. The $K = \infty$ fixed point corresponds to the ordered phase. For there to be a phase transition, there has to be a finite value of $K_c$ such that for all values $K < K_c$, the fixed point of the RG flow is $K =0$ and for all values of $K > K_c$, the fixed point of the RG flow is $K = \infty$.

As was the case with the 1D Ising model, there is \textit{no} phase transition for the 1D Potts model---for all values of $q$. To demonstrate this, we will show that both small and large values of $K$ flow to the $K = 0$ fixed point.

Taking $K \ll 1$, we can show that:

$$\begin{align}
K'(K) &=\ln \left (\frac{e^{2K} + q-1}{2e^{K} + q-2} \right) \\
&\approx \ln \left ( \frac{[1 + 2K + \frac{1}{2} (2K)^2] + q-1}{2[1 + K] + q-2}\right) \\
&= \ln \left ( \frac{q + 2K + 2K^2}{q + 2K}\right)\\
&= \ln \left ( 1 + \frac{2K^2}{q + 2K}\right ) \\
&\approx \frac{2K^2}{q + 2K} \\
&\approx \frac{2K^2}{q}
\end{align}$$

We assumed $K$ to be small, so $K' \sim \Theta(K^2)$ is even smaller. It follows that for small values of $K$, the fixed point of the RG flow is the $K = 0$ fixed point.

For large $K$, we have that:

$$\begin{align}
K'(K) &= \log \left ( \frac{e^{2K} + q -1}{2 e^K + q-2} \right ) \\
&\approx \log \left ( \frac{e^{K}}{2}\right) \\
&= K - \ln 2 \\
\end{align}$$

So for large $K$, we have that $K' < K$.

This is an indication that the only stable fixed point is $K^{*} = 0$---the disordered phase. We have no phase transition for the $q$-state Potts model. 