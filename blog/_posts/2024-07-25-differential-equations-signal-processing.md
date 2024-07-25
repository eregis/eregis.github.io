---
layout: post
title: "Differential Equations and Linear Filters"
date: 2024-07-25
mathjax: true
---

Compared to other areas of physics, biophysics is light on the mathematical pyrotechnics. In my research, I basically only use two types of mathematical tools: differential equations and linear filters.

Differential equations are ubiquitous in all areas of physics. In biophysics, they are commonly used for modeling the microscopic aspects of biochemical systems. For example, here is a system of differential equations that I use pretty often:

$$
\begin{cases}
a = \frac{1}{1 + e^F}, \\[0.5em]
F = N \left(\alpha(m_0 - m) + \log \left(\frac{1 + \frac{L}{K_i}}{1 + \frac{L}{K_a}} \right) \right), \\[0.5em]
\frac{dm}{dt} = V_r(1-a) - V_b a^2, \\[0.5em]
\frac{da_{\text{FRET}}}{dt} = -\frac{1}{\tau_1}(a_{\text{FRET}} - a)
\end{cases}
$$

This system of equations is called *the standard model of chemotaxis*. [Chemotaxis](https://en.wikipedia.org/wiki/Chemotaxis) is the process of how bacteria navigate chemical gradients in their environment. To do so, a bacterium converts external signals in the form of ligand concentration into changes in its internal state, represented by the concentration of some molecular compound (in the case of *E coli* it's [CheY-P](https://www.sciencedirect.com/topics/medicine-and-dentistry/chey-protein)). The standard model captures how the activity changes with respect to ligand while also taking into account the presence of a negative feedback loop that makes the bacteria adapt to the concentration over time. (Basically, bacteria are built to detect *changes* in the concentration of ligand, not the raw concentration itself).

[Linear filters](https://en.wikipedia.org/wiki/Linear_filter) are a tool from signal processing, often used when taking an abstract information-theoretic view of biophysics. A filter is a mapping from one time series to another. A linear filter is one where the output of the sum of two input signals is equal to the sum of the output of each signal individually:

$$ L\{f(t) + g(t)\} = L\{f(t)\} + L\{g(t)\} $$

In my work on bacterial chemotaxis, we often use filters to examine the relationship between changes in ligand concentration $s(t) = \frac{d}{dt} \log c$ and the internal activity of the cell $a(t)$. (To simplify: activity measures how likely a bacterium is to change direction. High activity makes direction changes more probable, while low activity makes them less likely.)

These two mathematical tools represent differing perspectives on biophysics. Differential equations are used when modeling bacteria as biochemical systems, with each component getting its own equation based on theory and experimental data. Signal processing treats bacteria as information processors, focusing on how external signals affect overall behavior. Thus, we are given complementary views of the same phenomena: a low-level, mechanistic description and a high-level, agentic description, respectively.

When can you go between the two perspectives? The answer is anticlimactic but useful: if you have a linear and time-invariant differential equation, then you can solve it as an integro-equation. This is the makes sense as the time-representation of a filter can be thought of as a [Green's function](https://en.wikipedia.org/wiki/Green%27s_function), so anyone who has taken an electromagnetism class could have seen this punchline coming.

But most differential equations aren't linear? So what do you do then?

One thing that you can do is to linearize your differential equation. You can do this if you expect that the values of your input signal (dependent variable) is going to be small perturbations around a fixed point. Going back to the standard model of chemotaxis, we can linearize it, replacing $s$ and $a$ with perturbations $\Delta s$ and $\Delta a$. This yields the *linearized standard model of chemotaxis*:

$$
\begin{cases}
\frac{d\Delta m}{dt} = -(2 V_b a_0 - V_r) \Delta a , \\[0.5em]
\frac{d\Delta a}{dt} = -a_0(1-a_0)N \left[ \alpha(2 V_b a_0 - V_r) \Delta a + \Delta s \right] \\[0.5em]
\frac{d\Delta a_{\text{FRET}}}{dt} = -\frac{1}{\tau_1}(\Delta \mathsf{a}_{\text{FRET}} - \Delta \mathsf{a})
\end{cases}
$$

Once you have linearized, you can solve for the corresponding response functions.

But do you *have* to linearize your set of differential equations? Instead of looking for a linear filter, can't you find a *non-linear* filter that corresponds to your *non-linear* set of differential equations? I briefly looked into this question and there does seem to a couple of mathematical tools that fall under "non-linear filter theory". The one that seemed the most promising to me was the [Volterra series](https://en.wikipedia.org/wiki/Volterra_series) which can be thought of a Taylor expansion of kernel functions. 

But I am not familiar with a well-developed theory of non-linear filters, so for now: it's differential equations and linear filters.