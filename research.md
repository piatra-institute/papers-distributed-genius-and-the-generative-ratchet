# Research

Findings, tiered by source proximity (T1 primary · T2 authoritative secondary ·
T3 reference · T4 general web, leads only). Every finding that reaches the paper
rests on a T1 or T2 source. All references verified 2026-07-11; full entries and
provenance in `sources.md`.

## Cumulative culture and the ratchet

- [T1] Tennie, Call & Tomasello (2009), *Phil. Trans. R. Soc. B* 364(1528), 2405–2415 — the ratchet effect: human culture uniquely accumulates modifications across generations, where chimpanzee traditions stay within a "zone of latent solutions." Supports §3 (the ratchet preserves).
- [T1] Tomasello, Kruger & Ratner (1993), *BBS* 16(3), 495–511 — high-fidelity transmission via imitative, instructed, and collaborative learning. Supports §3.
- [T1] Boyd & Richerson (1985), *Culture and the Evolutionary Process* — the population-dynamic mechanism by which socially transmitted variation accumulates into complex adaptation. Supports §3.
- [T2] Henrich (2016), *The Secret of Our Success* — the collective brain; capability rests on accumulated transmitted know-how rather than raw individual intelligence. Supports §1 and §3. KEY: the ratchet literature explains preservation of collective gains, NOT the conversion into individual capability. That gap is the paper's opening.

## Genius as environment (distributed / extended cognition, systems view)

- [T1] Hutchins (1995), *Cognition in the Wild* — cognition distributed across people, artifacts, social organization. Supports §1.
- [T1] Clark & Chalmers (1998), *Analysis* 58(1), 7–19 — active externalism; coupled external resources can be constitutive of cognition. Supports §1.
- [T2] Csikszentmihalyi (1999), in *Handbook of Creativity*, 313–335 — creativity as a property of a system (individual, domain, field), not a lone trait. Supports §1.
- [T1] Ericsson, Krampe & Tesch-Römer (1993), *Psych. Review* 100(3), 363–406 — deliberate practice as effortful, feedback-rich training. Supports §1 (the individual-effort account the paper qualifies).
- [T1] Macnamara, Hambrick & Oswald (2014), *Psych. Science* 25(8), 1608–1618 — meta-analysis: practice explains a modest, domain-dependent share of variance (26% games, 21% music, 18% sports, 4% education, <1% professions). Supports §1: the residual is largely environmental (which exemplars and tools the learner inherits).

## The exemplar / possibility space

- [T1] Kauffman (2000), *Investigations* — the adjacent possible. Supports §2 (the possibility-space operator; an exemplar expands the set of reachable next states).
- [T1] Vygotsky (1978), *Mind in Society* — internalization (external cultural tools become internal capability) and the zone of proximal development. Supports §2 and §4.

## The design conditions (what makes learning durable)

- [T1] Collins, Brown & Newman (1989), in Resnick (Ed.), 453–494 — cognitive apprenticeship: modelling, coaching, scaffolding, articulation, reflection, exploration. Supports §5 (decompression) and §7.
- [T1] Wood, Bruner & Ross (1976), *J. Child Psychol. Psychiatry* 17(2), 89–100 — scaffolding, and its withdrawal. Supports §7 (the fading condition).
- [T1] Sweller (1988), *Cognitive Science* 12(2), 257–285 — cognitive load; unguided problem solving can consume working memory without building schemas. Supports the overload arm of the kernel and §7.
- [T1] Kapur (2008), *Cognition and Instruction* 26(3), 379–424 — productive failure; pre-instruction struggle deepens understanding and transfer. Supports the difficulty condition, §7.
- [T2] Bjork & Bjork (2011), in Gernsbacher et al. (Eds.), 56–64 — desirable difficulties. Supports §7.

## The AI-empirical anchors

- [T1] Kestin, Miller, Klales, Milbourne & Ponti (2025), *Scientific Reports* 15, Article 17458 — RCT, N=194 Harvard physics; scaffolded AI tutor beat in-class active learning, effect 0.73–1.3 SD, in less time. CAUTIONS (authors' own): immediate/short-term post-lesson, heavily prompt-engineered tutor with guardrails, two topics (surface tension, fluid flow), single course. Cite as a single suggestive result of a STRUCTURED tutor; NOT as validating the framework. Supports §7.
- [T1] Bastani, Bastani, Sungu, Ge, Kabakcı & Mariman (2025), *PNAS* 122(26), e2422633122 — ~1,000 Turkish high-schoolers; unrestricted GPT +48% during practice but −17% vs controls when removed; guardrailed tutor removed the harm. Supports §6 (false ratcheting) and §7. The finished-output vs structured contrast, in the field.
- [T1] Brynjolfsson, Li & Raymond (2025), *QJE* 140(2), 889–942 — customer support; ~15% average productivity gain, concentrated among less-experienced agents. Supports §4/§6: the production frontier lifts most for the least skilled.
- [T1] Doshi & Hauser (2024), *Science Advances* 10(28), eadn5290 — AI ideas raise individual creativity (most for less-creative writers) while making outputs more similar. Supports §7 (diversity paradox).
- [T1] Shumailov, Shumaylov, Zhao, Papernot, Anderson & Gal (2024), *Nature* 631, 755–759 — model collapse; recursive training on generated output loses tails and variance. Supports §7 (archive-anchor warning) as a precise analogy, NOT a claim about human culture.

## The simulation

- Illustrative model, `simulation/`. Three regimes (no_tool, finished_output, structured_fading) under one update law; parameters stipulated to instantiate the definitions. Headline (results.json): production frontier ~0.87 for both tools; competence ends 0.15 (finished) vs 0.84 (structured); tool-removal collapse 83.1% vs 10.3% vs 23.9% (no tool); genuine-ratchet fraction 0.10 vs 0.99; ordering stable across 2000 seeded +/-15% perturbations. Labelled illustrative in-text.
