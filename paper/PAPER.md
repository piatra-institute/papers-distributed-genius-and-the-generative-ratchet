---
title: |
  Distributed Genius and the Generative Ratchet:\
  How Inherited Possibility Becomes Individual Capability,\
  and When It Only Appears To
author: PIATRA . INSTITUTE
date: July 2026
---

## Abstract

Genius is usually attributed to individuals, but much of its cultural effect resides in what exceptional achievements leave behind: exemplars, tools, and enlarged possibility-spaces. We treat education as the conversion of this distributed inheritance into individual capability. Cumulative-culture theory explains how a population retains gains across generations; it does not explain how a retained gain becomes an individual's usable and extendable skill. We distinguish three frontiers: production (the best output a learner can produce with available tools), competence (what the learner can generate and revise unaided), and judgment (what the learner can reliably evaluate). Generative AI raises production almost immediately while competence and judgment change little, producing false ratcheting, sophisticated output without durable capability, which becomes measurable when the tool is removed. In an illustrative model with stipulated parameters, a finished-output tool and a fading structured tool reach the same production frontier (0.87), but competence ends at 0.15 and 0.84 respectively; on tool removal, output falls by 83.1% and 10.3%; the fraction of the production advance retained as capability is 0.10 and 0.99; and the ordering holds in all of 2,000 seeded parameter perturbations. We predict that AI builds capability when it decomposes achievements, elicits prediction and explanation before revealing answers, generates controlled contrasts, preserves productive difficulty, and withdraws its assistance, and that it produces only the appearance of capability when it supplies finished products. Existing evidence, a scaffolded physics tutor with gains of 0.73 to 1.3 standard deviations and an unrestricted chatbot that lowered later unaided scores, is consistent with this split.

## Introduction

A contemporary student of composition can write counterpoint in a first term that would have taken Bach's contemporaries years to reach. The student's innate ability does not explain this. The explanation lies in what intervened: the tempered keyboard, figured-bass pedagogy, printed chorales, and two centuries of theory that named what Bach did so that it could be taught. A capability once confined to one exceptional person now resides partly in the apparatus surrounding an ordinary one. The student inherits the results of a search without paying its cost.

On this view the exceptional individual is one component of a larger productive system. Csikszentmihalyi (1999) argues that creativity is a property of a system with three interacting parts, the individual who produces variation, the domain that stores symbolic rules, and the field that selects what enters the domain, so that a contribution is creative only when the field admits it and the domain transmits it. Cognition has the same structure. Hutchins (1995) shows a navigational fix computed across instruments, charts, procedures, and a division of labour, a cognitive process whose parts are people and artifacts, with no single sailor holding the whole computation. Clark and Chalmers (1998) extend the point with active externalism: when an external resource is coupled tightly enough to the reasoning that uses it, it functions as part of the mind. On all three accounts, capability is distributed across a standing arrangement of people and things.

The individual-effort tradition appears to point the other way, but its evidence does not. Ericsson, Krampe and Tesch-Römer (1993) tie expert performance to deliberate practice, the effortful, feedback-rich, individually targeted training that separates experts from the experienced. Deliberate practice is real and indispensable, but it does not account for who reaches the frontier. Macnamara, Hambrick and Oswald (2014), in a meta-analysis of the practice literature, find that accumulated practice explains a modest and strongly domain-dependent share of performance variance, on the order of a fifth to a quarter in music and games and far less in education and the professions. Much of the residual variance is environmental: which exemplars a learner encounters, how early, decomposed by whom, and with what tools for varying them. Henrich (2016) makes the population-level version of the claim, that human success rests on a collective brain, the accumulated and transmitted know-how that no single lifetime could reconstruct, more than on individual intelligence.

We call the resulting object distributed genius: the spread of exceptional generative capability across artifacts, notations, practices, institutions, tools, and learners, such that achievements once dependent on rare individuals become navigable and extendable by many. The term is meant literally and narrowly. It does not claim that groups are more intelligent than individuals or that individuals cease to matter. It claims that the generative power a culture attributes to its geniuses is substantially carried by the infrastructure they left behind, and that education transmits this infrastructure to learners. A theory of education must therefore explain how that infrastructure becomes a particular person's capability.

## Exemplars and the expansion of possibility-space

A transformative work does more than add an item to an inheritance. It changes the shape of the domain, so that positions unreachable before it become reachable after it.

Let $\Omega_t$ be the possibility-space of a domain at time $t$, the configurations its practitioners can currently conceive, attempt, and recognize as belonging to the domain. An excellent work occupies an open point in $\Omega_t$. A transformative exemplar $E$ enlarges the space:

$$
\Omega_{t+1} \;=\; \Omega_t \,\cup\, D(E) \,\cup\, V(E) \,\cup\, Q(E) \,\cup\, R(E, \Omega_t),
$$

where $D(E)$ is the set of operations the work demonstrates to be possible, $V(E)$ the variations it makes newly visible, $Q(E)$ the questions it raises that did not previously exist, and $R(E, \Omega_t)$ the recombinations it enables with the rest of the existing culture. The union formalizes the claim that a work opens a region of the space.

Each term corresponds to a distinct function of the exemplar. Demonstration converts an uncertainty into a settled possibility: after Michelangelo, the monumental torqued body is known to be drawable, and later artists begin from that certainty. Search compression stores the cost of the failures the exemplar already incurred, so successors inherit the outcome of an exploration without repeating it. Perceptual reorganization changes what practitioners can see; after certain drawings, a torso displays tensions and masses that were physically present all along but perceptually unavailable. New vocabulary supplies forms that can be named, varied, and recombined, such as the fugue as a manipulable type. Problem creation leaves open questions that become the next generation's frontier. Euler's manipulations of infinite series demonstrated operations, compressed a century of trial, and left the questions about convergence that the following century had to answer. The adjacent possible, in Kauffman's (2000) sense, is the expanding boundary of states reachable in one step from the culture's current position, and a transformative work is a large expansion of it.

The enlargement is not automatically available to any given learner. The space $\Omega_{t+1}$ is public. A person viewing a drawing sees a finished figure and not the sequence of decisions that produced it; the operations in $D(E)$ are demonstrated without being transferred. Vygotsky (1978) described the general form of this gap and how it closes: higher capabilities exist first between people, in externalized cultural tools and signs, and become individual only through internalization driven by social interaction. A masterpiece externalizes a structure, and whether that structure becomes anyone's capability is a separate, pedagogical question.

## Cultural ratchets and individual acquisition

Cumulative culture has a canonical mechanism for retaining enlargements once they occur. Tennie, Call and Tomasello (2009) call it the ratchet: human populations retain modifications and build on them across generations, whereas the traditions of other species remain within a zone of solutions each individual could reinvent. Retention depends on high-fidelity transmission. Tomasello, Kruger and Ratner (1993) attribute that fidelity to distinctively human forms of cultural learning, imitative, instructed, and collaborative, which copy the intent and procedure behind an outcome as well as the outcome itself. Boyd and Richerson (1985) supply the population dynamics under which transmitted variation accumulates into adaptations that no individual designed.

The ratchet is a theory of preservation, and preservation differs from acquisition. Retention of a technique in the collective record ensures that the next generation can find it, but says nothing about whether any particular member of that generation can use it. A library holds the calculus without any student thereby knowing it. The ratchet prevents $\Omega_{t+1}$ from decaying back toward $\Omega_t$ and leaves open how a point in the preserved space becomes an operation available to a specific learner.

The present framework addresses this conversion. The cumulative-culture literature sets it aside because its unit of analysis is the population and its measure is a trait's frequency. Education is the institution built for the conversion, and its success condition is that a learner can generate, vary, and extend an achievement without the scaffolding used to teach it; retention by the culture is insufficient. Henrich's (2016) collective brain explains why the species is capable far beyond any of its members, and does not attempt to explain how a given member becomes capable. The conversion has its own dynamics, failure modes, and measurements, and generative AI acts on it directly.

## Production, competence, and judgment frontiers

Assessment usually reports a single number, the quality of what a learner produced. When the learner worked with a capable tool, that number conflates capacities that must be distinguished.

\begin{definition}
For a learner $i$ on a domain of tasks, the \emph{production frontier} $P_i$ is the highest quality of output $i$ can produce using all tools currently available. The \emph{competence frontier} $C_i$ is what $i$ can independently generate, reconstruct, diagnose, and revise without those tools. The \emph{judgment frontier} $J_i$ is what $i$ can reliably evaluate: to tell a stronger output from a weaker one, detect an error, recognize cliché, and defend a selection.
\end{definition}

The three frontiers separate because they are supported differently. Production can be borrowed: a learner using a strong model produces at the model's level. Competence cannot be borrowed, by definition, because it is what remains when borrowing stops. Judgment is partly independent of both. A person can sometimes recognize that an output is wrong without being able to produce a correct one, and, more problematically, can produce fluent output without being able to assess its quality. Competence and judgment are coupled, since reliable evaluation of generative work generally requires enough internal structure to know how the work is made, but the coupling is loose enough that the two frontiers move at different rates and must be tracked separately.

The distinction is compatible with extended cognition and distinct from it. Clark and Chalmers (1998) argue that a coupled tool can be part of the cognitive system that produces an output, and the production frontier accommodates that view. The educational question is independent of the metaphysical one. Wherever the boundary of the mind is drawn, a learner who can perform only while coupled to a particular tool has acquired something different from a learner who can perform when the coupling is removed, and that difference is the object of schooling. Competence is the capacity that survives decoupling, and a pedagogy indifferent to it optimizes the wrong frontier.

Generative AI separates the frontiers because it raises production immediately and competence slowly, and it raises production most for those with least competence. Brynjolfsson, Li and Raymond (2025), studying customer-support agents given a generative assistant, found an average productivity gain concentrated among the least experienced workers, whose output moved closest to that of the best. As a fact about production, this is the intended effect of the technology. As a fact about the frontiers, it indicates that the tool most enlarges the distance between what a novice can produce and what a novice can do. The central prediction follows. Where the interaction supplies output without building capacity, the change in production over a course of study greatly exceeds the change in competence and judgment,

$$
\Delta P_i \;\gg\; \Delta C_i, \ \Delta J_i,
$$

and the gap is invisible to any assessment that measures production alone. It becomes visible under one manipulation, removal of the tool, which makes the framework testable.

## Generative regeneration of exemplars

The preceding analysis applies to any period: exemplars have always opened spaces, education has always faced the conversion problem, and the frontiers have always been distinct in principle. Generative models change one consequential feature: they make the exemplar interactive.

A printed chorale is fixed. A learner can copy, annotate, and study it, but it does not respond. A generative model used alongside the same chorale can re-voice it in another style, remove a suspension to show what the suspension contributed, transpose the problem to an instrument that did not exist when it was written, generate the piece the composer might have written next, and produce a plausibly defective version for the learner to diagnose. We call this generative regeneration: the reconstruction of a fixed cultural achievement as a variable, interactive, and counterfactual field. The exemplar becomes a neighbourhood to be explored, with its decisions individually adjustable and its invariants exposed by observing what fails when a decision is changed.

Regeneration is the active form of the possibility-space operator. For most of history the terms $D(E)$, $V(E)$, and $R(E,\Omega_t)$ were latent: the variations an exemplar made visible still had to be executed by hand, one at a time, at the cost of the skill required. Regeneration makes them available on demand at near-zero marginal cost. The neighbourhood of an achievement, the family of nearby works it implied but did not contain, becomes explorable by someone who cannot yet produce a single member of it unaided. The classical ratchet preserved one solution and passed it forward; a generative ratchet can pass forward the surrounding field of solutions, and can do so quickly.

Speed carries both the benefit and the risk. The mechanism that lets a learner traverse in an afternoon a space that once required an apprenticeship can also traverse it on the learner's behalf, delivering the destination without the journey. Regeneration can decompose an achievement into its decisions, or skip the decomposition and return the finished object. It can generate a controlled contrast that requires an explanation, and it can also generate the explanation, leaving nothing for the learner to do. Cognitive apprenticeship, in the sense of Collins, Brown and Newman (1989), makes an expert's normally hidden process visible so that a learner can take it over, through modelling, coaching, and gradual transfer of responsibility. Generative regeneration can support or preclude that transfer, and which it does depends on how the interaction is arranged; the model itself does not determine it. The next section quantifies the difference.

## A model of false ratcheting

To test whether the three-frontier distinction is coherent and separates the cases it names, we use a deliberately simple model of a course of practice. The model is illustrative: its parameters are stipulated to instantiate the definitions above and are not estimated from learners, so its numbers describe the model's logic and are not measurements of teaching. It establishes that the framework's predictions follow from its definitions under a transparent dynamics, and that the tool-removal test discriminates the regimes as the framework predicts.

A learner has a competence frontier $C$ and a judgment frontier $J$, each starting at $0.10$ and bounded above by $1$. Production is an algebraic function of competence and the current assistance $a$, $P = C + a\,(\kappa - C)$, with tool ceiling $\kappa = 0.95$, so that at full assistance the learner produces near the tool's level regardless of their own, and at zero assistance production equals competence. Over thirty practice sessions a single update law moves $C$ and $J$. Competence grows in proportion to the generative work the learner performs, the quality of the feedback that corrects it, and the degree to which the task sits at a productive level of difficulty, a managed gap above current competence. A desirable-difficulty term, peaked at that gap and vanishing when the task is trivial, encodes the finding documented from three directions by Bjork and Bjork (2011), Kapur (2008), and Sweller (1988): learning is greatest at an intermediate, effortful level of challenge and least when the work is done for the learner or left entirely unsupported. Judgment grows with the evaluative work the interaction demands, weighted by the competence needed to make evaluation reliable.

Three regimes apply the same dynamics with different interaction signals. The no-tool baseline assigns all the work to the learner but leaves them facing the raw, unscaffolded gap. The finished-output regime holds assistance high and constant, has the tool perform most of the work and supply answers in place of operations, and demands little evaluation, corresponding to an unrestricted chatbot used to complete a task. The structured-fading regime begins with high assistance and withdraws it to zero over the course, has the tool structure the work without performing it, demands prediction and evaluation at each step, and holds the learner at the productive gap, corresponding to a scaffolded tutor that returns responsibility to the learner.

![Production and competence frontiers over 30 practice sessions in the illustrative model. Left: under a finished-output tool with constant assistance, production stays near 0.87 while competence rises only to 0.15, and the gap (shaded) persists. Centre: under a structured tool whose assistance fades to zero, competence rises to 0.84 and the gap closes. Right: output at course end with the tool at a common assistance level $a = 0.9$ and with the tool removed; the fall is 83% for the finished-output learner, 10% for the structured-fading learner, and 24% for the no-tool learner. Values are properties of the model.](../simulation/output/figures/frontiers.png){width=100%}

The regimes diverge as predicted. Both tools reach essentially the same production frontier, $0.87$, so any assessment of output alone would rate them as equivalent. Their competence frontiers end far apart: $0.15$ under the finished-output tool, $0.84$ under the fading structured tool, and $0.70$ for the learner who used no tool. Judgment separates in the same way, ending at $0.23$ and $0.89$ for the two tools. The comparison with the no-tool learner is the most informative: the finished-output learner ends less competent than a learner who never had a tool, while appearing more accomplished than either throughout the course, so a tool that maximizes visible output can leave a learner below the level reached by unaided practice.

The gap remains hidden until the tool is removed. When each learner is given the tool at a common strength and it is then withdrawn, production falls to the level competence supports. Displayed output falls by 83.1% for the finished-output learner and by 10.3% for the structured-fading learner. For the no-tool learner it falls by 23.9%, which here measures the lift the tool provides to a learner who never practised with it. The finished-output regime loses about 8 times as much as the structured one. The incorporation ratio, the share of the production advance that became durable capability, with judgment weighted at $\lambda = 0.5$, is $0.10$ for the finished-output tool and $0.99$ for the structured one. In the first case production rose by 0.77 above the novice level and almost none of that advance was retained by the learner; in the second, the production the learner displays at the end is production they can generate unaided.

The ordering does not depend on a single parameter set. When the model's constants are perturbed by up to 15% in either direction across 2,000 draws with a fixed seed, the finished-output regime ends below the structured regime in competence in every draw and loses more output on tool removal in every draw. The separation is a property of the interaction architecture and not of a finely tuned choice of numbers. The model cannot determine the size of the real gap in a real classroom, because its parameters were chosen to express the definitions; only measurement can supply them. It shows that the distinction is coherent, that it has a determinate empirical signature, and that the signature is performance after tool removal.

## Design conditions for genuine ratcheting

The model places the difference between regimes in their interaction signals, which are the variables open to design. Translating the contrast into guidance yields five conditions, each stated as a claim that a study could refute.

A tool builds capability when it decomposes an achievement into the decisions that produced it, in place of returning the achievement whole. The predicted effect is an interaction: decomposition should raise unaided transfer more than assisted output, so a design that improves the finished product least may improve durable competence most. Cognitive apprenticeship rests on this externalization of hidden process (Collins, Brown, and Newman, 1989), and the framework places its benefit on the competence frontier.

A tool also builds capability when it elicits a prediction and an explanation from the learner before revealing an answer. Requiring a commitment to what will happen, and why, before the model shows the result converts a passive display into a test the learner takes. AI helps when it redirects effort toward comparison, diagnosis, and explanation, and harms when it removes the operation the learner was meant to acquire.

Controlled contrast is a third condition. A single finished example demonstrates a possibility; a family of variations differing in one decision at a time teaches what each decision does, provided the learner predicts and explains the differences. The tool generates the contrasts and leaves their interpretation to the learner.

Difficulty is the fourth. The desirable-difficulties (Bjork and Bjork, 2011) and productive-failure (Kapur, 2008) literatures agree, from different starting points, that struggle at an appropriate level builds durable understanding, and cognitive-load theory (Sweller, 1988) marks the opposite boundary, where difficulty without support becomes overload. A tool that removes all difficulty removes the conditions for learning.

The fifth condition is withdrawal. Scaffolding, in the original sense of Wood, Bruner and Ross (1976), is defined by its removal: support is provided for what the learner cannot yet do and withdrawn as they become able, and a scaffold that is never removed becomes a permanent prosthesis. The design goal is a learner who can function when the tool is absent, whether or not the tool was used during learning.

The field evidence is limited but already has the predicted form. Bastani et al. (2025), in a field experiment with about 1,000 secondary-school mathematics students, found that access to an unrestricted model raised performance by about half during assisted practice and then left students scoring below their tool-free peers once the model was withdrawn, while a guardrailed version that guided without answering removed the harm. The two arms correspond to the model's two tool regimes, and they diverged on removal as the framework predicts. Kestin et al. (2025) report a randomized trial in which an engineered physics tutor, built with scaffolding, step-by-step guidance, and targeted feedback, produced a learning gain estimated at 0.73 to 1.3 standard deviations over in-class active learning, in less time. The authors note the limits of this single result: it measures immediate post-lesson outcomes and not durable retention, uses a heavily prompt-engineered tutor and not a generic chatbot, and covers two physics topics in one course. Without validating the framework, it is consistent with its more specific claim that interaction architecture determines whether AI tutoring works, so that a scaffolded tutor and an answer-dispensing chatbot are two treatments with opposite effects and not two doses of one treatment.

Two collective effects extend the same logic beyond the individual learner. Doshi and Hauser (2024) found that AI-generated ideas raise the assessed creativity of individual stories, most for the least creative writers, while making stories more similar to one another, so optimizing each learner's output can reduce the diversity of a cohort while raising its average. Recursive dependence on generated material carries a distribution-level risk: Shumailov et al. (2024) show that models trained on their own output collapse toward the head of the distribution and lose its tails. That result concerns models, and no equivalent process in human culture has been demonstrated, but it supplies a precise analogy and a testable concern. A pedagogy in which generated approximations replace the primary human archive, instead of anchoring exploration to it, risks teaching the mean of the model in place of the range of the tradition.

## Measurement and falsification

The framework has consequences only if it changes what is measured, and its principal prescription is to stop treating assisted output as the criterion of learning. The decisive quantities are what the learner can do with the tool switched off, and they are directly observable.

| construct | operational measure |
|---|---|
| assisted production | quality produced with the tool available |
| autonomous competence | quality produced after the tool is removed |
| assistance gap | assisted minus unassisted, on matched tasks |
| durable competence | unassisted performance after a delay of weeks |
| transfer | unassisted performance on a structurally new task |
| judgment calibration | agreement of the learner's selections and confidence with expert assessment |
| error detection | rate of catching planted or model-generated defects |
| collective diversity | dispersion of outputs across a cohort |

The assistance gap is the practical form of the tool-removal test, and it converts the central claim into a study that is straightforward to run. Learners are assigned to a finished-output tool, a fading structured tool, or no tool; tasks are equated; and the outcome is what each group can produce and evaluate without assistance, immediately and after a delay, in addition to what it produces with help. The framework predicts that assisted output will not order the groups and that unassisted competence and judgment will, with the fading tool ahead, the finished-output tool behind, and the gap widening with delay. A learner's trajectory from exemplar to artifact to transferable capability contains evidence that any finished artifact conceals, so assessment must follow the trajectory as well as the endpoint.

The same design specifies how the framework would fail. If adequately powered trials find that unassisted competence and judgment track assisted production regardless of how the interaction is arranged, so that finished-output and fading structured tools leave learners equally capable once the tool is removed, the three-frontier distinction collapses and the framework is wrong. If fading and scaffolding show no advantage in delayed unaided transfer over tools that supply answers, the design conditions of the previous section are empty. These are the observations that would refute the account, and stating them distinguishes it from a redescription of existing good teaching practice.

## Conclusion

Much of the framework's machinery is established. Cumulative culture supplies the ratchet, extended cognition the distributed ontology, and cognitive apprenticeship, desirable difficulties, and productive failure the design conditions. The new elements are the separation of production from competence and judgment into frontiers that move at different rates when a tool is present, and the observation that their divergence is measurable on tool removal. The neighbouring theories were developed under conditions in which producing an output at a given level was evidence of the capability to produce it, because production was costly and could not be borrowed. Generative AI removes that link. When output is nearly free and fully borrowable, the quantity that formerly certified learning no longer does so. Teaching has historically worked by supplying what the learner lacked; when supply is what the tool provides best and most cheaply, the scarce pedagogical actions become the withdrawal of assistance, the deliberate reintroduction of difficulty, and restraint at the points where acting for the learner would seem most helpful. Distributed genius becomes individual capability only in an environment that at times declines to perform the work on the learner's behalf, and the appropriate measure of a pedagogy is the capability that remains when the tool is switched off.

## References

Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *Proceedings of the National Academy of Sciences*, 122(26), Article e2422633122.

Bjork, E. L., & Bjork, R. A. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning. In M. A. Gernsbacher, R. W. Pew, L. M. Hough, & J. R. Pomerantz (Eds.), *Psychology and the real world: Essays illustrating fundamental contributions to society* (pp. 56–64). Worth Publishers.

Boyd, R., & Richerson, P. J. (1985). *Culture and the evolutionary process*. University of Chicago Press.

Brynjolfsson, E., Li, D., & Raymond, L. R. (2025). Generative AI at work. *The Quarterly Journal of Economics*, 140(2), 889–942.

Clark, A., & Chalmers, D. (1998). The extended mind. *Analysis*, 58(1), 7–19.

Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship: Teaching the crafts of reading, writing, and mathematics. In L. B. Resnick (Ed.), *Knowing, learning, and instruction: Essays in honor of Robert Glaser* (pp. 453–494). Lawrence Erlbaum Associates.

Csikszentmihalyi, M. (1999). Implications of a systems perspective for the study of creativity. In R. J. Sternberg (Ed.), *Handbook of creativity* (pp. 313–335). Cambridge University Press.

Doshi, A. R., & Hauser, O. P. (2024). Generative AI enhances individual creativity but reduces the collective diversity of novel content. *Science Advances*, 10(28), Article eadn5290.

Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). The role of deliberate practice in the acquisition of expert performance. *Psychological Review*, 100(3), 363–406.

Henrich, J. (2016). *The secret of our success: How culture is driving human evolution, domesticating our species, and making us smarter*. Princeton University Press.

Hutchins, E. (1995). *Cognition in the wild*. MIT Press.

Kapur, M. (2008). Productive failure. *Cognition and Instruction*, 26(3), 379–424.

Kauffman, S. A. (2000). *Investigations*. Oxford University Press.

Kestin, G., Miller, K., Klales, A., Milbourne, T., & Ponti, G. (2025). AI tutoring outperforms in-class active learning: An RCT introducing a novel research-based design in an authentic educational setting. *Scientific Reports*, 15, Article 17458.

Macnamara, B. N., Hambrick, D. Z., & Oswald, F. L. (2014). Deliberate practice and performance in music, games, sports, education, and professions: A meta-analysis. *Psychological Science*, 25(8), 1608–1618.

Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., & Gal, Y. (2024). AI models collapse when trained on recursively generated data. *Nature*, 631, 755–759.

Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science*, 12(2), 257–285.

Tennie, C., Call, J., & Tomasello, M. (2009). Ratcheting up the ratchet: On the evolution of cumulative culture. *Philosophical Transactions of the Royal Society B*, 364(1528), 2405–2415.

Tomasello, M., Kruger, A. C., & Ratner, H. H. (1993). Cultural learning. *Behavioral and Brain Sciences*, 16(3), 495–511.

Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes* (M. Cole, V. John-Steiner, S. Scribner, & E. Souberman, Eds.). Harvard University Press. (Original works written 1930–1934.)

Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry*, 17(2), 89–100.
