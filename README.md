# Distributed Genius and the Generative Ratchet

How Inherited Possibility Becomes Individual Capability, and When It Only Appears To.

Genius is usually attributed to individuals, but much of its cultural effect resides in what exceptional achievements leave behind: exemplars, tools, and enlarged possibility-spaces. We treat education as the conversion of this distributed inheritance into individual capability. Cumulative-culture theory explains how a population retains gains across generations; it does not explain how a retained gain becomes an individual's usable and extendable skill. We distinguish three frontiers: production (the best output a learner can produce with available tools), competence (what the learner can generate and revise unaided), and judgment (what the learner can reliably evaluate). Generative AI raises production almost immediately while competence and judgment change little, producing false ratcheting, sophisticated output without durable capability, which becomes measurable when the tool is removed. In an illustrative model with stipulated parameters, a finished-output tool and a fading structured tool reach the same production frontier (0.87), but competence ends at 0.15 and 0.84 respectively; on tool removal, output falls by 83.1% and 10.3%; the fraction of the production advance retained as capability is 0.10 and 0.99; and the ordering holds in all of 2,000 seeded parameter perturbations. We predict that AI builds capability when it decomposes achievements, elicits prediction and explanation before revealing answers, generates controlled contrasts, preserves productive difficulty, and withdraws its assistance, and that it produces only the appearance of capability when it supplies finished products. Existing evidence, a scaffolded physics tutor with gains of 0.73 to 1.3 standard deviations and an unrestricted chatbot that lowered later unaided scores, is consistent with this split.

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run `papers build distributed-genius-and-the-generative-ratchet`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace docs for the research and writing pipelines.
