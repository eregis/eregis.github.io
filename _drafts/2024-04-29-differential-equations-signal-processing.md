---
layout: post
title: "Differential Equations and Linear Filters"
date: 2024-04-29
mathjax: true
---

Compared to other areas of physics, biophysics is lite on the mathematical pyrotechnics. In my research, I basically only use two types of mathematical tools: differential equations and linear filters.

Differential equations are ubiquitous in all areas of physics. In biophysics, they are commonly used when modeling the microscopic aspects of biochemical systems. For example, here is a system of differential equations that I use pretty often:

$$
\begin{cases}
a = \frac{1}{1 + e^F}, \\[0.5em]
F = N \left(\alpha(m_0 - m) + \log \left(\frac{1 + \frac{L}{K_i}}{1 + \frac{L}{K_a}} \right) \right), \\[0.5em]
\frac{dm}{dt} = V_r(1-a) - V_b a^2, \\[0.5em]
\frac{da_{\text{FRET}}}{dt} = -\frac{1}{\tau_1}(a_{\text{FRET}} - a)
\end{cases}
$$

This system of equations is called *the standard model of chemotaxis*. Chemotaxis is the process of bacteria navigates chemical gradients in their enviroment. To do so, they have to convert external signals in the form of ligand concentration into changes in its internal state, represented by the concentration of some molecular compound. The standard model of chemotaxis captures how the activity changes with respect to ligand while also taking into account the presence of a negative feedback loop that makes the bacteria adapt to the concentration of ligand over time. (Basically, bacteria are built to detect *changes* in the concentration of ligand, not the raw concentration itself).

Linear filters are tool from signal processing. You often see  this when you take an abstract information theoretic view of biophysics. For example, in my work in bacterial chemotaxis, we often ask about the relationship between the concentration of ligand change in the log concentration of ligand $$s(t) = \frac{d}{dt} \log c$$ and the internal activity of the cell. (To simplify things: actitity is measure of how badly a bacteria wants to change direction. A bacteria that is high in activity is prone to change direction while a bacteria that is low in activity is less prone to changing direction.) 

A filter is mapping from one time series to another. A linear filter is one where the output of the sum of two input signals is equal to the sum of the output of each signal individually.

$$ L\{f(t) + g(t)\} = L\{f(t)\} + L\{g(t)\} $$

The two most common mathematical tools represent two differing perspectives on biophysics. In microbiology, differential equations are used when modelling when modeling bacteria as biochemical system. Each constituent part--ligand, internal messenger, mechanism--gets its own differential equation with the functional form dictated by theory and the constants fitted with experimental data. Signal processing is used when modelling bacteria as *information processors*. Here, we care not so much about the messy, internal details, but how in practice, this affects the behavior.

So the two mathematical tools give complentary perspectives on the same phenomena. So to be able to go between  and linear filters differential equations give us a low-level, mechanistic description and a high-level, agentic description.

When can you go between them? The answer is anticlimatic but useful: if you have a linear and time-invariant differential equation, then you can solve it as an integro-equation. This is the makes sense as the time-representation of a filter can be thought of as a Greens function, so anyone who has taken an electromagnetism class could have seen this punchline coming.

But most differential equations aren't linear? So what do you then? If you want to use some sort of filter theory.

One thing that you can do is to linearize your differential equation. You can do this if you expect that the values of your input signal (dependent variable) is going to be small perturbations around a fixed point. Is there an "interpretation" of small perturbations.