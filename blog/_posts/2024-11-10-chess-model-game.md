---
layout: post
title: "Chess As The Model Game"
date: 2024-11-10
mathjax: true
---

Other than Pokemon, most of my YouTube consumption is comprised of chess analysis videos. This might surprise people because 
I don't play chess very often these days. And when I do play chess, I'm not that good. 

(My peak chess.com Elo rating was 1050 back in 2018---and surely, I've only gotten worse since then now that I am out of practice.)

I haven't been a chess enthusiast my whole life though. Besides a brief childhood dalliance, 
my love of chess was something that I discovered as a young adult.  Like a lot of tiger parents, 
my mom made sure that I was exposed to chess at an early age---just in case I was the South Florida Bobby Fischer or something. 
When I was around five or six, she bought me the computer game *Fritz and Chesster*.



![Fritz and Chesster Game](/assets/chess-model-game/fritz_and_chesster.jpg)

F&C is a cutesy computer game designed to teach you the rules of chess. The protagonists are a pair of royal siblings. 
At the beginning of the game, the king and queen of the kingdom (your parents) are kidnapped by the evil king of a rival kingdom. 
It's your job to save them. Your journey takes you through the most dangerous nooks and crannies of Chessland. Along the way,
you learn valuable lessons like proper rook-and-pawn ending technique and the importance of king safety. 
(Basically, it's Super Mario Bros with fewer Goombas and more queenside castling.) 

F&C did what it was supposed to do. By the end of the game, I was competent in moving all the different pieces and even had a solid
grasp on chess's more esoteric rules like *en passant*. But chess never really clicked for me---at least not deeply. 
F&C had several difficulty settings for the enemy computer, and I quickly plateaued at the easy-medium difficulty settings. 
So after a couple of months, I got bored and stopped playing chess, other than the occasional game here or there on random occasions
like at summer camp (where I would invariably be trounced).

Fast forward to the end of 2017. I'm in my sophmore year of undergrad. I do stereotypical college student things like hating on Tom Brady,
listening to Playboi Carti, and overusing the phrase "dings in the whip". It was also around the time that I started to casually get into machine learning. The YouTube algorithm must have picked up on this as it recommended me a video called "Google's self-learning AI AlphaZero masters chess in 4 hours".

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%;">
    <iframe 
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
        src="https://www.youtube.com/embed/0g9SlVdv1PY"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen>
    </iframe>
</div>

In the video, Jerry (the creator of the channel ChessNetwork) analyzes a game between AlphaZero and Stockfish. AlphaZero and Stockfish aren't colorful gamertags, however. AlphaZero and Stockfish were, at the time, the two most powerful chess engines in the world. And they represent two opposing paradigms in computer chess.



Stockfish represented the ancien regime of chess engines. Traditional chess engines evaluate positions using human-selected features. In machine learning, a feature is any property of the input that is passed to a network during learning. For chess, the raw data would be the state of the board (with some exceptions like castling rights and three-fold repetition, which require game history rather than just the current position). The engine's task is to evaluate which side is more likely to win, assuming perfect play from the current position.

Features are important because training a network on the raw board state would be too computationally expensive. While I'm not certain of the exact technical details, the general concept is that when training your network, you don't want it getting stuck trying to evaluate heuristics that we already know aren't useful. For example, we know that piece value is approximately additive: if a Bishop is worth three points and a Queen is worth nine points, then a Bishop + Queen is worth roughly 12 points. This pattern generalizes: if [Piece 1] is worth X points and [Piece 2] is worth Y points, then together they're worth X + Y points. In fact, even the basic concept that pieces have "value" would have to be learned from scratch by a chess engine evaluating raw board states. There are dozens of such common-sense chess intuitions that humans take for granted, which the network would need to discover on its own if given only the full state of the board.

Instead of evaluating the entire board state (the location of every piece), traditional engines use hand-selected features. These features include properties like material difference between the sides, whether one side has the bishop pair, or the presence of connected passed pawns. These features are selected based on advice from expert chess players, who choose them according to the heuristics they personally rely on when evaluating positions.

Once you have your bundle of heuristics, you face a dilemma: how do you weigh each one? This is where machine learning comes in. The network takes all these features and learns which combinations and weights lead to the most accurate position evaluation. This was how Stockfish originally worked (though it has since become more sophisticated).

AlphaZero represented a new school of thought. The 'zero' in its name refers to learning without human knowledge---starting from zero. Instead of using hand-selected features, its neural network learned its own features from scratch. It learned by playing against itself, favoring moves that led to winning positions. This approach allowed AlphaZero to discover heuristics that human experts either didn't know about or couldn't easily translate into computational rules. In just four hours of self-play, it mastered the game of chess.

So who won the match? As you might have been able to guess based on my framing, AlphaZero wiped the floor with Stockfish. They played a 100 games and Stockfish won precisely zero of them (final tally was 28 wins for AlphaZero and 72 draws). As there always is, there was [controversy on reddit surrounding the match](https://www.reddit.com/r/chess/comments/7hzda9/google_deepminds_alphazero_crushes_stockfish_280/), with Stockfish stans screeching that Stockfish's hardware limitations made the match unfair. But regardless, this match is now viewed as a pivotal moment in the history of computer chess.

This video singlehandly got me back into chess. I started watching not just ChessNetwork but other chess analysis YouTube channels like agadmator and Ben Finegold. It also gave me the new hobby of computer chess.

# The Model Game

In biology, there is a concept of "model organisms". These are the common organisms you hear about in biology experiments---mice, fruit flies, E. coli. Model organisms are creatures whose biology we understand extremely well, making them ideal for studying broader questions. For example, let's say you're interested in understanding a general question like "Do organisms tend to use most of their sensory information to achieve their goals?" While it would be difficult to answer this simultaneously for all organisms, you could start by examining a model organism like E. coli. Because E. coli is well-understood, you can operationalize slippery concepts like "How does E. coli represent information?" or "What goals is the E. coli trying to achieve?" Model organisms are also easier to experiment with. In the case of E. coli, we can genetically modify them and perform microscopy experiments on them.

In a similar way, chess is a *model game*. Chess is rich enough to shed light on a wide range of different fields like game theory, cognitive science, artificial intelligence, and thermodynamics. Yet it's also simple enough that we can make our questions operational and precise. Time and time again, I find myself leaning on chess as a source of intuition when grappling with a new discipline.

For example, chess is an excellent setting for understanding the nature of expertise. There is an entire "expertise" literature which studies questions like: How do experts acquire their expertise? How do the minds of experts differ from those of normal people?

Chess masters are known for their impressive feats of memory. You can pull up videos of super GMs like former World Chess Champion Magnus Carlsen [being able to instantaneously recognize random games](https://www.youtube.com/watch?v=eC1BAcOzHyY) from just a single board position. "Oh, yes, 1992 Linares between Gelfand and Short. Tricky endgame. Classic." And dating all the way back to the first super grandmaster Paul Morphy, the best chess players in the world are not only able to play while blindfolded, *but they are able to play blindfold simultaneous exhibitions*!

![Morphy Blindfold Simultaneous Exhibition](/assets/chess-model-game/morphy_blind_simul.jpg)

So you would think that elite chess players must have incredible memories. They must never have to use a list while grocery shopping, right? Well, not exactly. In [one of the most famous studies in all of psychology](https://psycnet.apa.org/record/1973-22240-001), they gave expert-level chess players two different chessboards to memorize. The first board came from an actual chess game, with the pieces arranged in a configuration that is typical for standard play. The second board had the chess pieces in completely random positions. What they found was that elite chess players were (as expected) way better than normal people at remembering the position of the chess pieces when the position came from an actual chess game. But to the researcher's surprise, the elite chess players were no better than the average person at memorizing the position of the pieces for a random board configuration!

What's going on? The explanation is that elite chess players don't store individual piece locations in memory. Instead, they use a hierarchical structure of high-level semantic concepts that can be unfolded to reconstruct the board position. This cognitive process is called *chunking*. When Magnus Carlsen recalls a chess game, his thought process is more like "Sicilian Dragon Variation, weak center for Black, king safety issues for White, far-advanced White h-pawn, unopposed light-squared bishop for Black" rather than "White king on c1, White knight on f3..."

Chunking is a universal phenomenem for understanding expertise, including expertise in physics. For example, consider the following expression:

$$i \hbar \frac{\partial \psi}{\partial t} = - \frac{\hbar^2}{2m} \nabla^2 \psi + \frac{1}{2} m \omega^2 x^2 \psi$$

Those with a physics background might recognize the equation: It's the Schrodinger equation! (Specifically, it's the special case when the potential is that of a harmonic oscillator.)

To those who haven't taken a quantum mechanics class, this equation might seem like an inscrutable jumble of symbols. But I was able to type it out from memory. How? Because of chunking. I won't write out my whole thought process (I don't *really* have conscious access to what chunks my brain is using anyway). But attempting to introspect, my thought process went something like this:

1. From classical mechanics, I know that the Hamiltonian is the generator of time-translation, so I associate time derivatives and the Hamiltonian in my head. So we should have a time-derivative on the left and a Hamiltonian on the right.

2. I know that the Hamiltonian is just a fancy name for energy. There are typically two components of energy: a kinetic term and a potential term. So $H = K + V$.

3. Also, from classical mechanics, I know that momentum is the generator of spatial translation. I also know that the kinetic energy is $\frac{p^2}{2m}$.

And so on and so forth. My brain is probably leaning on over a dozen of these heuristics in order to recall the Schrodinger equation from memory. (Pop quiz: Come up with a heuristic that let's you remember whether it's $+i \hbar$ or $- i \hbar$ in front of the time-derivative on the left side of the equation.)

Thinking in terms of chunking and higher-level semantic concepts was really helpful when I was self-studying physics after undergrad. It helped instill a certain attitude: *every* part of the equation is there for a reason. Every symbol, even something as small as a minus sign, has a reason for being the way that it is. You should search for the high-level concepts such that the equation *has* to have the form that it does.

We often use metaphors like 'he's quick on his feet' or 'she's a fast study.' But in practice, the difference between experts and non-experts isn't best understood as raw processing speed. Rather, experts have taken the time to develop the right mental models---the right level of abstraction to understand the problem.

And it's not just chunking. *Most* expertise is subconscious. There is no better demonstration than [watching GM Hikaru Nakamura play Puzzle Rush](https://www.youtube.com/watch?v=4EfSymvT59M) (a chess game where you have to answer as many chess puzzles as quickly as possible.) Without exaggeration, Nakamura often has determined the correct solution to the puzzle before my brain can resolve the visual information into a coherent board position. Admittedly, chess is an extreme example of a domain that rewards raw pattern-recognition. But in every field, refined intuition is at the heart of acquired expertise.

Chess also helps me understand aging curves: how people develop as they grow older. Everyone is familiar with aging curves in something like height. When I look at chess aging curves, two things stand out. One is that, especially at the very top level, there is incredible rank-order stability in chess-playing ability. The best players in the world as adults were already eminent talents as young adolescents. If you look at the list of youngest grandmasters in history, you'll see many recognizable names. I'm not sure if even something like height would exhibit the same rank-order stability. Prodigies are *real*.

![Young Magnus Carlsen](/assets/chess-model-game/carlsen_child.jpg)

Second, the best junior players are *good*. Like unfathomably good. In the chess world, 
up-and-coming Argentinian prodigy Faustino Oro has been making waves this year. 
He became the youngest International Master at 10 years, 8 months, and 16 days. 
According to ChatGPT, the academic equivalent of an IM would be an *associate professor*. 
Of course, we shouldn't take such comparisons too seriously. 
But it gives an intuition for the staggering level of ability on display.

I could go on. I could talk about the long intertwined history between chess and artificial intelligence, dating back to when Claude Shannon first proposed the chess-playing computer. I could talk about how chess was a microcosm of Soviet Union ethos. I could talk about how chess helps us reason about agency and the difference between instrumental and terminal goals. I could talk about how chess admits a thermodynamic perspective, where statements like "a knight is worth three pawns" are actually expectation values taken over the ensemble of plausible chess positions.

John von Neumann once said that "Chess is not a game. Chess is a well-defined form of computation." He was referring to how chess, being a game of perfect information, lacks the game-theoretic beauty of poker, which requires mixed strategies and deft handling of probabilities and risk. I couldn't disagree more. Chess *is* a game. It's in many ways the perfect game. Its beauty lies precisely in how its secrets are out there, yet somehow forever out of our reach.
