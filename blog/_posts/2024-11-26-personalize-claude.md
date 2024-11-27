---
layout: post
title: "Personalize Claude"
date: 2024-11-26
mathjax: true
---

I'm a big fan of large language models (LLMs): both for their utility in automating some of the more tedious parts of my work, 
but also I'm just fascinated with them as a novel technology. If you haven't had a chance to use them, I highly recommend you 
experiment with them. At the moment, the consensus killerapp of LLMs is programming. Assuming that you are coding in a decently-popular 
programming language, the LLMs are *incredible* at creating the skeleton of a working
program. And if the program you are asking for is simple enough, they often nail it on the first try. They do have limitations, however.
LLMs are limited in their "context window" (how much the LLM can keep in its head at once), so it won't be able to handle
really long scripts all at once. For similar reasons, working with multiple script simultaneously is also a challenge. But they are still
indispensable.

At this point, there are many different LLMs available for use. The most popular one (and the one that you've probably have heard of) is
ChatGPT. But the *best* one---honestly, by far---is Claude. Claude is the signature LLM of Anthropic, an AI company that started due to an
internal schism at OpenAI. I can't quite articulate what makes Claude feel like a notch above the other LLMs.
But if you know, you know.

Earlier today, Anthropic announced a new feature: [Personalize Claude](https://www.anthropic.com/news/styles).

> **Personalize Claude chats**

>With styles, you can customize Claude's responses to match your communication preferences, tone, and structure. Whether you're a developer writing technical documentation, a marketer crafting specific brand guidelines, 
or a product team planning extensive project requirements, Claude can adapt to your preferred way of writing.

This sounds really promising! If Personalize Claude works, then I could feed it the contents of this blog and use Claude!Eric to flood 
the internet with obscure probability theory content. Then Human!Eric would have more time to watch Nuzlocke videos.

This is what the prompt screen for Claude looks like:

![Claude prompt screen](/assets/personalize-claude/claude-prompt-screen.png)

If we click on the text that says "Choose style" next to the quill pen, then we get this menu.

![Different styles menu](/assets/personalize-claude/different-styles.png)

It lists different possible styles for Claude. I haven't personally experimented with any of the different styles, so I can't comment on
their various strengths and weaknesses. I have never felt any need to because the "Normal" version of Claude is quite powerful
and quite flexible---given a little poking and prodding and prompt-engineering. I am also acquainted 
with the "Concise" version of Claude, but not by choice. Whenever site traffic is particularly heavy 
(like mid-mornings and early evenings), Claude will be overloaded by all the people trying to use it. As a way to manage bandwidth, 
Claude gets switched to "Concise" mode---which, as you would expect based on its name, is the strong and silent type. 
It honestly works fine; I don't know why I am complaining about it.

But what we're interested in aren't the default styles, but creating our own personal style. If we click through, we are
given the option to upload writing samples.

![Add writing example](/assets/personalize-claude/add-a-writing-example.png)

I uploaded the last couple blog posts from *Critical Points*.

![Uploading blog posts](/assets/personalize-claude/Uploading-blog-posts.png)

Claude will take about half a minute to analyze your style. It will then describe the provided writing style, and also
give you the option of generating various examples written in that style.

![Style summary](/assets/personalize-claude/style-summary.png)

That's a flattering description of this blog. Thanks Claude! 

I decided to have Claude generate an example of "Educational Content" since that's the closest match to content of this blog.
Claude then attempted to write an explainer of Rayleigh scattering in my writing style. How did it do?

![Educational content example](/assets/personalize-claude/educational-content.png)

My personal verdict: Claude did terribly. This example failed both (a) as an emulation of my writing style and (b) as an engaging piece of
writing in its own right. I only made it two sentences in before my eyes glazed over. I *still* haven't read the entire writing sample (and I never will).

I didn't think super hard beforehand about what my expectations were for Personalize Claude, but I can't help but notice 
that I am disappointed. I definitely expected better than *this*. I'm not sure how Anthropic technically implemented the Personalize Claude,
but based on the results, I suspect that the verbal description of the writing style that they provide is all that Claude has to work with
as well.

In Claude's defense: the idiosyncracies of personal writing styles are *really* hard to put into words. Humans would struggle with
this task too. This actually seems like it would a fun game of telephone to be played in a Creative Writing class. You choose an obscure author
that only you are a fan of. You then have to describe their writing style in words such that a classmate can write a story in emulation
of their style. (Okay, maybe that was more interesting in my head.)

One fascinating aspect of LLMs is that, because they are trained on human-generated text, they exhibit a "folk psychology" 
similar to that of humans. In psychology, there is a concept called prototypes. Humans tend to think in categories, 
with certain members serving as more central examples than others. 
For example, an eagle would be a prototype for the bird category, while an ostrich would not. 
While LLMs may struggle with unique, idiosyncratic elements, they excel at capturing the stereotypical features of any genre. 
But who really asked for *more* cliche writing?