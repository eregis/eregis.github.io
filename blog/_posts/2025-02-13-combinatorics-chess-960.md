---
layout: post
title: "Chess960 and Combinatorics"
date: 2025-02-13
mathjax: true
description: "An exploration of Chess960 as an alternative to traditional chess, addressing memorization issues in top-level play, with a combinatorial analysis of its 960 unique starting positions."
keywords: Chess960, Fischer Random Chess, combinatorics, chess variants, Bobby Fischer, chess memorization, opening theory, chess tournaments, mathematical counting, permutations
---

*Programming Note:*

*Sorry for the three week hiatus! I'm quite busy this semester. I'm taking two classes, with Statistical Physics II in particular
taking a significant portion of my time due to both my intrinsic interest in the material and its direct relevance
to future research directions I want to pursue. I still have teaching responsibilities (at my institution and program, you are supported
on a teaching assistanceship for your first four semesters). And on top of that, I have started doing research in earnest. 
I am working on a project studying guidance in diffusion models (guidance is the term for how you get an 
image generation model to generate an image of a specific category). 
I've been enjoying the work, but it's left me with less time for quirky blogging.*

*I am a big believer in consistent output and positive momentum. Ideally, I would like to post to this blog once or twice a week.
What I will probably do is relax some of my more perfectionist tendencies. That would specifically mean having shorter, more
"disposable" posts at times. It also means that I would have a lower bar for "creativity". Even when explaining a standard concept 
(e.g., detailed balance), I try to make the explanation fresh and different from the ones you would find in a textbook. 
But I might have more posts where I straightforwardly explain concepts that are relevant to my various interests 
without trying too hard to be original in my presentation.*

*Anyways, back to our regularly scheduled programming!*

While chess remains an immensely entertaining and popular game, it isn't perfect. One problem with chess---especially top-level chess---is
that there is a heavy incentive to memorize openings in order to get a competitive advantage. You can see glimpses of this even
at the club level where players are familiar with a dizzying array of different openings (the Caro-Kann,
the Czech-Benoni, the French Defense, etc.). But
it's at the supergrandmaster level where the memorization becomes truly staggering. Super grandmasters routinely know opening
theory for their favorite variations twenty, even thirty moves deep. And with the rise of superhuman chess engines, 
top grandmasters can cook up home-prepared computer variations. 
There have been top-level games where players simply blitzed out computer moves until agreeing to an unceremonious draw. 
And even when the impact isn't so drastic, engine preparation has completely changed the way chess is played. 

To combat the rise of memorization in top-level chess, American chess legend Bobby Fischer invented what was then called 
Fischer Random Chess (now officially known as Chess960 by FIDE).

The rules of Chess960 are almost identical to those of standard chess, and the pieces remain the same:
one king, one queen, two knights, two bishops, two rooks, and eight pawns. The key difference is that the
pieces on the back row are placed in random positions, with two constraints:

1. The two bishops must be on opposite-colored squares (ensuring both a light-square bishop and a dark-square bishop)
2. The king must be placed between the two rooks

![Chess960 opening example]({{site.baseurl}}/assets/chess-960/chess960openingexample.jpeg)

While the variant was invented by Fischer in the 1990s, it has recently been gaining in popularity. The first Chess960 World
Championship was played in 2019, memorable for Wesley So's unexpected shellacking of then-World Champion Magnus Carlsen in the finals.
And currently underway is the Freestyle Chess Grand Slam Tour, a Chess960 tournament series organized by Carlsen and
German investor Jan Henric Buettner.

I'll be honest: I was a skeptic of Chess960. The problems with classical chess have been discussed for quite a while, with 
two main solutions advocated: Chess960 and a shift to faster time controls. I was always on the side of shifting 
to faster time controls due to it being closer spiritually to classical chess and also being superior from a spectator perspective 
(if you've never watched a livestream of Titled Tuesday, you're missing out).

But I've been watching ChessNetwork's analysis videos of the recent games from the Freestyle Chess Grand Slam Tour
and I'm finding the games extremely compelling. I'm not that good at chess, but even I have a sense
of when a chess position looks "normal". Due to the diversity of starting positions, watching these Chess960 games is
breaking my brain in a wonderful way. What the hell is that knight doing on g3?
Why are we five moves in and neither the d-pawn nor the e-pawn has moved from either side?
With Chess960, the pawn structures are novel, the piece arrangements are alien, and due to the lack of preparation,
there are tactics *everywhere*.

My biggest concern with Chess960 was that, as a spectator, I would be confused about what was going on because
I couldn't properly interpret the various board positions. But in the hands of a skilled commentator, this concern is ameliorated.
A good commentator will point out how the given starting position differs from other positions,
and how that leads to different opening plans than the ones you would expect to see in standard chess.
For example, in standard chess, all pawns in the second rank start the game protected by at least one piece.
But in Chess960, there are sometimes pawns that start out unprotected. These pawns often serve as focal points for opening strategy:
launch a quick strike against the opponent's weakness and you can dictate the pace of play.

But beyond the watchability of Chess960, it's also a fun setting for simple combinatorics problems. For example, the "960" in
the name Chess960 comes from the number of unique starting positions. Walking through why there are exactly 960 starting positions
serves as a nice combinatorics exercise.

# Why are there 960 unique starting positions?

When trying to count something, a framework that is helpful for me is to think in terms of *choices* and *options*. For example,
let's say you're at Subway and you need to choose a meat and a cheese for your sandwich. 
Let's say you have four options for meat and three options for cheese, 
and you must choose exactly one meat and one cheese, and you can mix and match any combo of meat and cheese. Then you
would have $4 \times 3 = 12$ different unique sandwiches to choose from.

This problem was straightforward because (a) we had a small number of choices to make and (b) the number of options for 
each choice is independent of the other choices. It's also pretty straightforward which "choices" we have to make
(this isn't always the case). In more complicated problems, things are not so simple. 

When counting the number of different starting positions, we are constructing a tree where each branching point represents a choice 
(e.g., where to put the queen). After all choices have been made, the leaf nodes represent the possible starting positions.
We must design our tree such that every valid starting position appears as a leaf node *exactly* once. 
Ideally, the combinatorial factor of each choice should be independent of all previous choices made. This would allow us to find
the total number of unique starting positions by multiplying the branching factor for each choice. 
Since there are eight pieces that must be placed on the board, there are naively 8! different orderings in
which we can make these choices. However, some decision orders are more advantageous than others.

For example, imagine we try to place the queen first and then the dark-square bishop.
With an empty back row, there are 8 possible choices for the queen. But the options for where to put the dark-square bishop
will depend on where we placed the queen. If we put the queen on a light square, then there would be four options for the dark-square
bishop. If we put the queen on a dark square, then there would be three options for the dark-square bishop. This type of case analysis
is exactly what we are trying to avoid.

We also want to account for the fact that we have identical pieces. 
For example, imagine that the back rank is empty and you want to place the two knights down. 
The naive approach would be to say there are eight options for the 
first knight and seven options for the second knight. But because the knights are identical, 
we would be overcounting in this case (to correct the overcounting, we should divide by two). 
A better approach, rather than breaking up the decision of where to place the two knights as two separate choices, 
is to consider placing both knights as *one simultaneous choice*. If there are $n$ remaining open slots on the back rank, 
there would be $\binom{n}{2}$ possible ways to place the two knights.

Now that I've established the problem, I will now present the correct approach. 
The key to determining how many unique starting positions there are relies on two observations:

1. We want to place the light-square and dark-square bishops first. This is because the other pieces are agnostic of square color, 
so placing the other pieces first would cause the number of squares in each color complex to vary in a way we don't want. 
It's also convenient that there is no conflict between placement options for the two bishops, 
as they must go on different colored squares.

2. It's most convenient to place the rooks and king at the end. Because the king must be between the two rooks, 
after placing the other five pieces, there is only one possible arrangement of the king and rooks that satisfies 
this constraint---so you essentially have no choice at all.

The general principle seems to be that "complicated" choices should be made either at the very beginning 
(where you don't have to worry about compatibility with previous choices) 
or at the very end (where your constraints limit your options, simplifying the problem). 
The pieces with the most flexibility---the queen and the two knights---are placed in the middle because they are unconstrained.

Here's the algorithm:

1. You place the light-squared bishop. There are 4 options for where to place it.
2. You place the dark-squared bishop. There are 4 options for where to place it.
3. You place the queen. There are 6 options for where to place it.
4. You place the two knights. There are 10 options for where to place them.
5. You place the king and the two rooks. There is 1 option for where to place them.

Which gets us $4 \times 4 \times 6 \times \times 10 \times 1 = 960$ different starting positions.


