---
layout: post
title: "Thoughts on Scott Alexander on the Dwarkesh Podcast"
date: 2025-04-05
mathjax: true
---

While I've only recently started researching the mathematics underlying our machine learning models, I've long been
interested in cutting-edge advances in artificial intelligence as well as futurism-style debates on how artificial intelligence will affect society going forward.

One of the best resources for learning more about AI is The Dwarkesh Podcast. Dwarkesh Patel, who majored in Computer Science at UT Austin, started the eponymous podcast while still in undergrad (because what else are you going to do during Covid except start a podcast). For the first couple years, the audience of the podcast was small. Though even at the beginning, Dwarkesh had an impressive slate of guests due to being surprisingly well-connected (most notably, enjoying a patronage relationship with influential GMU economist Tyler Cowen). 

But around early 2023, the podcast started to pick up steam, with new episodes being frequently discussed in online tech discourse.
As is often the case, success begets success: due to Dwarkesh's reputation for high-quality research, he started landing
more notable guests, which led to even more prominent figures wanting to be featured on the podcast. In the past year alone, he's interviewed Mark Zuckerberg, Satya Nadella, and Tony Blair.

On the most recent episode, Dwarkesh somehow managed to land *Scott Alexander* as a guest. Imagine you are going for your routine morning jog, and on the trail, you see the Yeti and Bigfoot riding a tandem bicycle. They wave at you. That's what it felt like when I saw the notification for the episode pop up on my phone.

![Bigfoot and Yeti](/assets/scott-alexander-dwarkesh/big-foot-yeti.png)

Scott Alexander is a blogger who used to write Slate Star Codex and now writes Astral Codex Ten on Substack. He is one of the most prominent writers affiliated with the "rationalism" movement, which started as an online community focused on learning how to combat cognitive biases. Despite rationalism being fairly obscure except to the Terminally Online, Scott's readership is surprisingly influential, including some of the biggest names in tech and even popular academics (For example, computer scientist Scott Aaronson often engages with Scott and rationalism on [his blog Shtetl-Optimized](https://scottaaronson.blog/)).

While he writes about many topics---spanning from psychiatry to philosophy to fiction---a recurring theme in Scott Alexander's writing is artificial intelligence, making him a natural guest for the Dwarkesh Podcast. However, despite his incredibly large Internet word count, Scott has infamously stated that he would *never* do podcasts. But it seems, due to a combination of Dwarkesh's reputation as well as the need to promote [his new project AI 2027](https://www.astralcodexten.com/p/introducing-ai-2027), Scott has now made his very first podcast appearance.

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%;">
    <iframe
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
        src="https://www.youtube.com/embed/htOvH12T7mU?start=15"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen>
    </iframe>
</div>

In this three-hour long interview, Dwarkesh interviews Scott and former Open AI engineer Daniel Kotojoko about their new project AI 2027. AI 2027 is meant to be a highly-detailed attempt to forecast the near future in artificial intelligence. The most notable prediction of the project is that sometime around the year 2027---which, by my math, is *two years from now*---the AIs will get so good at coding
that they will start leading the research to improve their own capabilities, jumpstarting a positive feedback loop that ends in artificial superintelligence.

I'm going to give my reaction to the first hour or so of the podcast. I'll quote from [the transcript of the episode](https://www.dwarkesh.com/p/scott-daniel) to provide context.

# The Interview

> **Scott**: Yeah, AI 2027 is our scenario trying to forecast the next few years of AI progress. We’re trying to do two things here. First of all we just want to have a concrete scenario at all. So you have all these people, Sam Altman, Dario Amodei, Elon Musk saying, “going to have AGI in three years, superintelligence in five years”. And people just think that’s crazy because right now we have chatbots that are able to do a Google search, not much more than that in a lot of ways. And so people ask, “how is it going to be AGI in three years?” What we wanted to do is provide a story, provide the transitional fossils. So start right now, go up to 2027 when there’s AGI, 2028, when there’s potentially super intelligence, show on a month-by-month level what happened. Kind of in fiction writing terms, make it feel earned.

Rationalists are a bit odd in that, while they are not *uninterested* in recent developments in machine learning, their main concern is the arrival of artificial general intelligence or "AGI" for short. This concern with AGI started with the founder of the rationalist movement, Eliezer Yudkowsky, and various memes about AGI have since percolated to the rest of Silicon Valley. Notable ones include asking someone what their "timeline" is (when they predict AGI to arrive) as well as their "pDoom" (the probability that, if AGI is invented, the world ends).

Rationalists tend to both have shorter timelines and higher pDooms---and Scott is no exception (though he is less pessimistic than other rationalists like Yudkowsky, who once gave a pDoom of over 99%). But often, when pressed to give specifics, rationalists have struggled to articulate plausible scenarios. This has hurt their credibility and gotten them labeled as "doomers". The AI 2027 project seems to be an attempt to fix that.

> **Scott**: The thing that gives me optimism is Daniel back in 2021, wrote the prequel to this scenario called What 2026 Looks Like. It’s his forecast for the next five years of AI progress. And he got it almost exactly right. You should stop this podcast right now. You should go and read this document. It’s amazing. Kind of looks like you asked ChatGPT to summarize the past five years of AI progress, and you got something with a couple of hallucinations, but basically well intentioned and correct. So when Daniel said he was doing this sequel, I was very excited, really wanted to see where it was going. It goes to some pretty crazy places and I’m excited to talk about it more today.

Daniel was recently in the news for quitting OpenAI, when he revealed that OpenAI required employees to sign a non-disparagement agreement in order to receive their vested equity. (Basically, if former employees spoke negatively about OpenAI, then OpenAI could sue and take their stock away.)

> **Scott**: Everyone else on the team, also extremely impressive. Eli Liflund, who’s a member of Samotsvety, the world’s top forecasting team. He has won, like, the top forecasting competition, plausibly described as just the best forecaster in the world, at least by these really technical measures that people use in the superforecasting community. Thomas Larsen, Jonas Vollmer, both really amazing people who have done great work in AI before.

There are deep ties between the rationalist community and "superforecasters." Superforecasters grew out of the work of Phil Tetlock, who studied forecasting. Two of the main takeaways from Tetlock's work were:

1. The existence of wisdom of the crowds. If you have a group of people try to forecast some event, and then aggregate everyone's prediction, the aggregate prediction would do better than the median person. You can see this in many places, like how in carnival games, if you ask a bunch of people to guess the number of marbles in a jar, the average guess is usually surprisingly close to the actual number.

2. He identified the existence of superforecasters. These are people who are able to consistently perform at a level matching or even exceeding the aggregate prediction. This was a non-trivial finding. Of course, for any given event, there will be people who do a better job than average at prediction. But it's not obvious that someone could consistently outperform the average. The events that the participants of the study were asked to forecast ranged quite widely, such that you couldn't attribute the performance of the superforecasters to superior domain knowledge.

Superforecasters are relevant because they are arguably the closest thing to experts for a project like this. One could argue that machine learning researchers have the most relevant expertise, but arguably these sorts of messy predictions---that don't just involve the evolution of technology but also how that will interact with the messy arena of geopolitics---require a more generalized skillset for reasoning under uncertainty.

> **Daniel**: My guess is that they won’t be making basic mouse click errors by the end of 2025, like they sometimes currently do. If you watch Claude Plays Pokemon- which you totally should- it seems like sometimes it’s just failing to parse what’s on the screen and it thinks that its own player character is an NPC and gets confused. My guess is that that sort of thing will mostly be gone by the end of this year, but that they still won’t be able to autonomously operate for long periods on their own.

This is the crux of the debate. Something that should be emphasized about current AI is that they are *already* narrowly superintelligent. ChatGPT is a polyglot who can recite from memory arcane details of obscure medical textbooks. And yet: most companies aren't lining up to replace their employees with LLMs. Why?

I would say it comes down to "executive function"---the ability to formulate coherent plans and enact them over long periods of time. We take for granted what a complex skill this is, as it's something humans can do naturally. But it seems quite difficult to get models to behave in coherent, agent-like ways. 

The relevent question is: How quickly will they improve? Here, there is a bit of a measurement problem. With more narrow forms of intelligence like coding, measuring progress is as simple as giving the models a battery of coding problems and scoring how well they do over time. While solving coding problems isn't the same as managing a complex software project, the narrow skill of coding is easy enough to define and measure.

Executive functioning is different. And this is important because it would seem (to me) that this would also make finding the correct training paradigm difficult as well. There are attempts to quantify the executive functioning ability of LLMs with the notion of their "time horizon", but based on my admittedly superficial engagement with these metrics, I find them unsatisfying and not really capturing what we actually care about in terms of the LLM's practical capabilities. And I don't think that moar scale will fix this problem any time soon. This is probably the main point of disagreement between me and people with shorter timelines.

> **Dwarkesh**: Yeah. I had this interesting experience yesterday. We were having lunch with this senior AI researcher, probably makes on the order of millions a month or something, and we were asking him, “how much are the AIs helping you?” And he said, “in domains which I understand well, and it’s closer to autocomplete but more intense, there it’s maybe saving me four to eight hours a week.”

>But then he says, “in domains which I’m less familiar with, if I need to go wrangle up some hardware library or make some modification to the kernel or whatever, where I know less, that saves me on the order of 24 hours a week.” Now, with current models. What I found really surprising is that the help is bigger where it’s less like autocomplete and more like a novel contribution. It’s like a more significant productivity improvement there.

This tracks with my experience using LLMs (though I'm not nearly getting a 2x productivity boost).

The way I would describe LLMs is that they are superhuman *associative* reasoners (as compared-and-contrasted with logical, deductive reasoning). If you ask an LLM to prove some difficult, famous theorem in math, it will often get it wrong. But usually the vibes of the proof will actually be pretty close (e.g., if a crucial step of the proof involves the triangle inequality, then the LLM's proof will also have the triangle inequality, but perhaps at the wrong step). 

This can be useful as it gives me a hint about what the right framework for thinking about the problem might be. For example, I've been reading a lot of machine learning papers lately and LLMs have been invaluable at quickly providing context---clarifying confusing jargon, providing the historical motivation behind otherwise mysterious choices---that would have otherwise taken me hours to provide for myself.

> **Dwarkesh**: Well, I asked this question where, as you say, they know all this stuff. I don’t know if you saw this. I asked this question where I said, look, these models know all this stuff. And if a human knew every single thing a human has ever written down on the Internet, they’d be able to make all these interesting connections between different ideas and maybe even find medical cures or scientific discoveries as a result.

I agree that this is a really interesting question. I don't have a good answer to it.

Though as Scott noted, humans aren't logically omniscient either ("logical omniscience" is when an entity can deduce all the implications from all the facts that it has instantaneously). He gave the nice example of etymology: even very proficient, native speakers of English might not stop to think about the fact that "hapless" and "happen" share a common root. So perhaps there is no mystery to explain.

If I were to try to explain why humans aren't logically omniscient, I would say that it has something to do with the fact that we don't store facts in our head like clothes in a closet, but rather what we do have is something like a hierarchical structure of programs that we can execute at runtime to get the information. Since information isn't just lying around, but needs to be extracted from the programs, information that resides in differing programs that are rarely called concurrently won't ever have a chance to interact.

> **Scott:** And I think right now if we tried it, we would run into the combinatorial explosion. We would need better heuristics. Humans have such good heuristics that probably most of the things that show up even in our conscious mind, rather than happening on the level of some kind of unconscious processing, are at least the kind of things that could be true. I think you could think of this as like a chess engine. You have some unbelievable number of possible next moves, you have some heuristics for picking out which of those are going to be the right ones. And then gradually you kind of have the chess engine think about it, go through it, come up with a better or worse move, then at some point you potentially become better than humans. I think if you were to force the AI to do this in a reasonable way, or you were to train the AI such that it itself could come up with the plan of going through this in some kind of heuristic-laden way, you could potentially equal humans.

One of my strongest opinions about creativity is that it's not about "randomness". In any high-skill domain---whether it's composing music or writing novels---the number of different possible choices is simply too large for dumb experimentation to be feasible.

As Scott mentioned, chess engines are a good intuition pump here. Perhaps a not super-well-known fact about chess engines is that most of the value of the evaluation function comes from the ability to prune bad moves and not consider them, not from the final evaluation at the leaf nodes. Or in other words, most of the value is that it allows a more efficient guided search.

Based on my amateur study of the minds of highly-creative people, their creativity stemmed not from "randomness" but rather from their "evaluation function"---their sense of taste, essentially---being unusually refined in their domain of expertise. This allowed them to identify superficially wrong or unappealing ideas that other people overlooked and develop them to their full potential.

> **Dwarkesh:** Maybe the reason that this sounds less plausible to me than the 25x number implies is that when I think about concretely what that would look like, where you have these AIs and we know that there’s a gap in data efficiency between human brains and these AIs. And so somehow there’s a lot of them thinking and they think really hard and they figure out how to define a new architecture that is like the human brain or has the advantages of the human brain. And I guess they can still do experiments, but not that many.

> Part of me just wonders, what if you just need an entirely different kind of data source that’s not like pre-training for that, but they have to go out in the real world to get that. Or maybe it needs to be an online learning policy where they need to be actively deployed in the world for them to learn in this way. And so you’re bottlenecked on how fast they can be getting real world data. I just think it’s hard…

So during this portion of their interview, they start getting into some of the nitty-gritty details of their model and Dwarkesh voices his objections/qualms. I'm pretty much entirely on Dwarkesh's side here. The flow is basically Dwarkesh raising a potential bottleneck, and then Scott and Daniel reply with some iteration of "the AI is smart, it will figure it out." 

I don't deny that smart entities can perform feats that my puny human brain can't comprehend. At the same time, I am just not convinced that they've adequately accounted for all the unknown unknowns the AIs will face once they start transitioning into interacting with the real world. I admittedly haven't read the full AI 2027 report yet, so maybe after reading it I will be more convinced than I am after casually listening to their off-the-cuff remarks.

> **Scott:** We do think that the AI will be closer to the eusocial insects in the sense that they all have the same goals, especially if these aren’t indexical goals, they’re goals like “have the research program succeed”. So that’s going to be changing the weights of each individual AI, I mean, before they’re individuated, but it’s going to be changing the weights of the AI class overall to be more amenable to cooperation.

> And then, yes, you do have cultural evolution. Like you said, this takes hundreds of thousands of individuals. We do expect there will be these hundreds of thousands of individuals. It takes decades and decades. Again, we expect this research multiplier such that decades of progress happen within this one year, 2027 or 2028. So I think between the two of these, it is possible.

One of the interesting parts about thinking about superintelligence is considering the capabilities of AI that *don't* neatly map to intelligence. One of those capabilities is the possibility for levels of cooperation that isn't possible among humans. Humans have only low-bandwidth ways of transferring information to each other (e.g. vibrating vocal cords while contorting the mouth to transmit information via pressure waves in the ambient air) and we also don't fully trust each other.

Another interesting thing to consider is raw processing speed. Even if AIs are in some sense only as smart as humans, if they can reason 50x as fast, that has to count for something, right?

~ ~ ~

I'm going to call it there. This should give you a taste of what the interview was like. They covered a bunch of other topics like misalignment, the Race with China, and even Scott's take on the blogosphere.

Overall, I walked away from the interview slightly less favorable towards shorter timelines, but I mostly still remain highly uncertain/agnostic.