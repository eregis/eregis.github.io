---
layout: post
title: "Physically-Interpreting Diffusion Model Noise Parameters"
date: 2024-12-19
mathjax: true
---

Diffusion models are ways of generating samples from complex probability distributions. You've probably heard of 
them from image generating AI like Dalle-2

The way diffusion models is that given a training set of images, they gradually blur them until each image because
random pixel noise. The model then attempts to each of the intermediary distributions over pixel spaces of the 
subsequently blurred images. Once the model has done that, you can then give it a random white noise image that 
*wasn't* the result of blurring an image, and the model will attempt to denoise the image anyway. The resultant 
image will be sampled from the distribution of natural images. This allows you to give the model random pixelated
images and generate natural images at your discretion.

When blurring the image, there is a decision to be made about how much to blur the image at each time step.
There is a way.