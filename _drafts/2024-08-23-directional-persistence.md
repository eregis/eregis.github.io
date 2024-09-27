---
layout: post
title: "Directional Persistence"
date: 2024-08-23
mathjax: true
---
https://journals.aps.org/pre/pdf/10.1103/PhysRevE.57.4604

In Adaption and Optimal chemotactic strategy for E Coli (by a group in collaboration with Bialek),
they talk about the differing optimal chemotactic strategies in two regimes: the high signal regime (where you have perfect, instantaneous knowledge of the direction that you are traveling with respect to the gradient) as well as the low signal regime (where you only have limited information).

They find that the optimal strategy is highly dependent on being adaptive: (which  makes sense in the context that what the E coli in this model actually experiences is the change in the concentration of the ligand, so translating that into the actual direction that it's facing requires additional assumptions about the distributions of gradients that it's likely to be encountering.)

One of the ultimate conclusions was that it was inconclusive. Reading between the lines, one of the motivating results for the theory was there was an observed long, super-exponential tail (if I recall correctly, it went as e^{t^0.5})) that they wanted to explain; their result fell out of the theory in the low signal to noise regime where it actually becomes favorable to retain information for *long* time scales (rather than the first-order approximation where you would expect that the kernel would be an exponential function with characteristic time of the rough order of magnitude of the duration of a run (since tumbles tend to randomize direction of the E coli, making previous information less relevant; Though not completely irrelevant--which is one of the main ideas of this paper!)

So the paper is in search of the *theoretically* optimal strategy that E Coli take in order to climb gradients. 

>Clearly, for an optimal strategy to exist at all, a problem
must be very highly constrained. The principle constraints
which make this problem solvable are taken largely from the
experimental literature on chemotaxis and motility of E. coli.
First, as pointed out by Berg and Purcell @15# in this context,
and as we will briefly discuss, due to rotational Brownian
motion, E. coli cannot maintain an orientation for an ex-
tended period of time. Second, E. coli make no controlled
changes of direction. It is obvious, given that they cannot
maintain orientation that, for sensory processing reasons
alone, they are incapable of turning in a specific direction
@6,15#; however, a change of direction of a controlled mag-
nitude is in principle possible. In practice, there is some evi-
dence that the length of tumbles is affected by sensory input
under some circumstances @16#; however, this is not believed
to be important for chemotaxis under realistic conditions @6#.
We therefore make the assumption that E. coli change direc-
tion by entering into ‘‘tumbles’’ which have have no char-
acteristics which depend on sensory input. It seems likely
that, in view of the limited use E. coli could make of steering
capability given its orientation problems, this simple method
of direction change was evolutionarily preferred because the
cost associated with this capability are lower than those that
a more developed steering capability would impose. In any
case, we assume here that the tumbles are all identical, and
effectively randomize the orientation of the bacteria over the
course of a time
ttumble;0.15 sec @17#. Finally, we assume
that during runs the bacterium swims with a fixed speed v,
independent of sensory inputs. This is known to be approxi-
mately true experimentally @6#.

So the three constraints are:
1. Rotational diffusion during runs
2. Identically distributed tumbles (tumble statistics are independent of the history of the system)
3. The bacteria swims as the same fixed speed.

These are pretty typical assumptions in the E Coli literature. The most interesting constraint is number 2, as that is (a) surprising if it were true (that tumbles were that "stereotyped" in that manner); and theoretically, you would assume that the "real" optimal strategy would take that into account, with tumbles being longer depending on the degree of belief that one is going down the gradient. This is actually investigated in another paper that I am reading this week as well, and they found that the directional persistence (expected value of the direction cosine before and after tumbling) has roughly a 3% difference between tumbles executed while climbing the gradient versus tumbles that are executed when going down the gradient. This doesn't sound like a big difference, but apparently, they attribute this difference with an over 50% increase in drift speed (in their units, that would be 0.9 $\mu $m/s to 1.4 $\mu$ m/s).

But anyway: the most interesting part of the constraints is not what's on the list, but what *isn't* on the list. One of their key assumptions when deriving the optimal strategy for the two regimes is that they assume that the bacteria tumbles deterministically. Rather than the signal history influencing some poisson process with time-varying tumble rate, the bacteria can choose, definitively, to tumble at a given instantaneous moment in time. Depending on what your molecular model of the motor is, it can be viewed as a limit when the Hill Coefficient goes to infinity: there is perfect discrimination between internal states that are in the run motion and internal states that are in the tumble motion. So it would seem that the extent that this approximation is meaningful/applicable to *real* bacterial chemotaxis, depends on what the Hill Coefficient of the motor is under usual conditions. The number I've seen is on the order of 15 which is indeed quite large, though a far cry from truly infinite.

Our optimization function is $\langle \vec{v} \cdot \nabla c \rangle$ where we will be working in environements with static gradients. There are other possible optimization functions; you could maximize $\langle c \rangle$, the expectation value of the concentration (as opposed to the time derivative of the concentration). Or you could maximize the expected direction during runs *only*. In our optimziation critiria, there is an implicit penalty for long tumble times as the cell doesn't climb the gradient during tumbles (which will lower the overall time average assuming that during runs, cells climb the gradient more often than they go down the gradient)

The motivation for choosing the maximize the time-averaged gradient versus the concentration is motivated by the fact that bacterial chemotaxis is often done in populations of isogenic bacteria all executing a similar strategy.