# Audit

Dated log of editorial passes and verification runs. Newest first.

## 2026-09-23 — structured-evidence migration

Structured-evidence migration (references and claims).
- references.yaml: 21 CSL entries. 14 matched automatically in Crossref and resolved through doi.org; csikszentmihalyi1999, henrich2016 and kestin2025 matched by hand to their DOI records (Sternberg added as editor; henrich2016 given its full subtitle; article numbers added for bastani2025, doshi2024 and kestin2025). Entered by hand without DOIs after confirming the works in OpenAlex: bjork2011, boyd1985, collins1989, vygotsky1978. In-text author-year citations converted to Pandoc [@id] syntax; the legacy reference list replaced by the citeproc-rendered list (Chicago author-date).
- Citation rephrasings: "in Kauffman's (2000) sense" -> "in the sense of @kauffman2000"; "Henrich's (2016) collective brain" -> "The collective brain of @henrich2016"; "@sweller1988:" written as "@{sweller1988}:" so the checker does not read the colon as part of the key.
- Correction: Bastani et al. (2025) report that the GPT Tutor safeguards "largely mitigated" the harm; "a guardrailed version ... removed the harm" -> "... largely removed the harm". Bibliographic: csikszentmihalyi1999 pages 313-335 -> 313-336 per the Cambridge record.
- claims.yaml: 63 claims (34 computation, 11 source, 5 definition, 4 assumption, 7 interpretation, 2 normative). Every model number in the abstract, body and figure caption is bound to simulation/output/results.json; "production rose by 0.77" is bound as an interpretation (0.87 minus the initial 0.10). Source claims checked against Crossref or OpenAlex abstracts; the Kestin et al. 0.73-1.3 SD range was confirmed in the open-access article text.
- Not bound (support not retrievable or only partly confirmed): Csikszentmihalyi's three-part systems model (abstract confirms only the systems perspective); Clark and Chalmers's active externalism; Vygotsky's internalization; Boyd and Richerson's population dynamics; Bjork and Bjork on desirable difficulties; Collins et al. on cognitive apprenticeship; Wood et al. on scaffolding; Brynjolfsson et al.'s claim that novice output moved closest to that of the best (abstract confirms the average gain and its concentration among less experienced workers only); Kestin et al.'s own statement of the study's limits (retention and prompt engineering found in the text, but not the full list).
- Execution receipt: run id ratchet (uv run python run_all.py); results.json reproduced byte for byte.
- metadata claims_target: claim-ledger.

## 2026-09-23 — prose revision

Prose rewritten against the house standards. Headings made descriptive (Introduction, Exemplars and the expansion of possibility-space, Cultural ratchets and individual acquisition, Production, competence, and judgment frontiers, Generative regeneration of exemplars, A model of false ratcheting, Design conditions for genuine ratcheting, Measurement and falsification, Conclusion).

Tic counts before -> after: 'rather than' 22 -> 0; inline ', not X' 4 -> 0; negate-pivot 3 -> 0; 'not X but Y' 5 -> 0; 'this paper' 3 -> 0; 'exactly/precisely' 2 -> 0; 'merely/simply' 3 -> 0; 'worth' 1 -> 0.

Corrections found during the pass:
  - "production advanced almost a full unit" for the finished-output regime: the advance in results.json terms is P_frontier - C0 = 0.870 - 0.10 = 0.77; now stated as 0.77.
  - The no-tool learner's 23.9% drop on removal was described as "the honest cost of losing a tool they had learned to work with". That learner never used the tool; the drop is the lift the tool gives (at a = 0.9) over the learner's unaided competence 0.704. Text now says so.
  - Figure caption now gives the rounded collapse percentages shown on the panel (83, 10, 24) alongside the text's 83.1/10.3/23.9.

Grid audit: no thresholds, optima, or crossovers; the model is a deterministic 30-step recursion, the production frontier is the maximum over the course trajectory, and the robustness fractions (1.0 of 2,000 draws) are counts. Prose numbers match results.json (0.87/0.868, 0.147 -> 0.15, 0.843 -> 0.84, 0.704 -> 0.70, J 0.229/0.886, collapse 83.1/10.3/23.9, ratio 8.07, GRF 0.096/0.986). results.json unchanged by the re-run.

Title left unchanged ("and When It Only Appears To" is slightly rhetorical but not erroneous).

## 2026-07-11 — Initial draft, build, and gate pass

Scope: paper written end to end from the seed conversation (`chats/chat.md`), with an illustrative simulation. The drawing-roadmap origin of the seed was dropped; the paper stands alone.

Changes:
  - `simulation/`: three-frontier model (`analyses.py`, `figures.py`, `run_all.py`, `pyproject.toml`). Production `P = C + a(kappa - C)`; competence and judgment move by one update law with a desirable-difficulty kernel; three regimes (no_tool, finished_output, structured_fading). Tool-removal test at a common assistance level; seeded (20260711) robustness sweep of 2000 +/-15% perturbations. Writes `output/results.json` and `output/figures/frontiers.png`.
  - `paper/PAPER.md`: abstract plus eight argument-driven sections and References. Possibility-space operator as a display equation; one `\begin{definition}` for the three frontiers; the central prediction as a labelled falsifiable claim; no templated closer. Ends on the withdrawal-of-assistance point.
  - `metadata.yaml`: real title/header/abstract; `has_simulation: true`; `claims_target: results.json`; `date` left null; `status: draft` (flip to built after a clean build).
  - `sources.md`, `research.md`, `brief.md`, `README.md` filled.

Verification:
  - references: all 21 verified via WebSearch/WebFetch against publisher/primary records. The AI-tutor RCT is Kestin, Miller, Klales, Milbourne & Ponti (2025), *Scientific Reports* 15, Article 17458, effect 0.73–1.3 SD, N=194; cited as a single suggestive result of a heavily scaffolded tutor with the authors' own cautions (short-term, two topics, one course), NOT as validation. Bastani et al. cited as the 2025 PNAS version; Brynjolfsson, Li & Raymond as the 2025 QJE version (novice effect described qualitatively; the 34% figure is the 2023 working paper's). Vygotsky dated 1978 with "original works written 1930–1934."
  - simulation numbers (results.json): production frontier 0.87 (both tools); competence 0.147 (finished) vs 0.843 (structured) vs 0.704 (no tool); judgment 0.229 vs 0.886; collapse-on-removal 83.1% vs 10.3% vs 23.9%; genuine-ratchet fraction 0.096 vs 0.986 vs 0.969; ordering holds in all 2000 seeded draws. Model labelled illustrative in-text.
  - voice / refs / claims / build / check: see the run recorded below on this date.

---

## 2026-07-11 — build + publish

Drafted from the seed chat (a conversation that began on learning to draw like the old masters and pivoted to cumulative culture and a "Generative Ratchet Pedagogy" draft). Distilled into a PIATRA-voice paper led by the falsifiable core: three frontiers (production, competence, judgment) and false ratcheting, the gap generative AI opens by lifting production while leaving competence and judgment behind, revealed on tool removal.

- Constructs given precise, operational definitions (the possibility-space operator Omega_{t+1} = Omega_t u D(E) u V(E) u Q(E) u R(E,Omega_t); a formal definition of the three frontiers; generative regeneration). Grounded in cumulative culture (Tennie/Tomasello, Boyd-Richerson, Henrich), distributed/extended cognition (Hutchins, Clark-Chalmers, Csikszentmihalyi), expertise limits (Ericsson, Macnamara), and design conditions (Collins cognitive apprenticeship, Vygotsky, Bjork, Kapur, Sweller, Wood-Bruner-Ross).
- Honest framing: proposed framework, not validated; the model is explicitly illustrative ("numbers are facts about the model's logic rather than measurements of teaching"); a "how the framework fails" section states the observations that would retire it; the redescription charge is met directly. The AI-tutor RCT (Kestin et al. 2025, 0.73-1.3 SD, N=194) is cited with its own cautions and "It does not validate the framework"; the contrasting field harm result (Bastani et al. 2025) and homogenization/collapse risks (Doshi-Hauser 2024; Shumailov et al. 2024) are cited carefully. Kestin's two decimals are recorded in results.json under an "external_anchors" block, clearly labelled as the cited study's figures, not model outputs.
- Simulation: deterministic three-frontier model (numpy; uv run run_all.py), one figure; headline production 0.87 both tools, competence 0.15 (finished) vs 0.84 (structured) vs 0.70 (no tool), collapse-on-removal 83.1% vs 10.3% vs 23.9%, genuine-ratchet fraction 0.10 vs 0.99, ordering robust across 2,000 seeded perturbations. Every prose decimal maps to a results.json key.
- Gates: voice 0 errors; refs 21/21, 0 missing/0 unused; claims 15/15 matched; build clean (13 pages); check => PASS. status -> published (date July 2026); synced PDF; added ownPapers entry to piatra-institute-web/app/papers/page.tsx (topics psychology/computer-science/philosophy; kinds formal/simulation), left uncommitted.
