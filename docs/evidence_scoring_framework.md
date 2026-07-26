# ELYON Evidence Scoring Framework

## Objective

The objective of ELYON is to support the prioritization of natural bioactive compounds for skin health by integrating biological, chemical and scientific evidence into a transparent scoring framework.

ELYON organizes available evidence and produces explainable recommendations.

---

# Overall Score

Each compound receives an Overall Evidence Score.

Overall Score = Weighted combination of five evidence pillars.

---

## Pillar 1
### Molecular Evidence

Questions

- Which proteins does the compound target?
- Are these proteins associated with skin biology?
- Is the mechanism of action understood?

Example output

Score:
0–20

---

## Pillar 2
### Biological Pathways

Questions

- Which pathways are affected?
- Are these pathways relevant to skin ageing?
- Oxidative stress?
- Inflammation?
- ECM remodeling?
- Pigmentation?
- Wound healing?

Score:
0–20

---

## Pillar 3 — Scientific Evidence

### Objective

Evaluate the strength, quality, relevance and reproducibility of the scientific evidence supporting a compound–target–skin relationship.

### Evidence dimensions

Scientific evidence is evaluated across four dimensions:

#### 1. Study Level

Evidence is weighted according to the experimental model:

- In vitro experimental study
- Animal in vivo study
- Human observational study
- Human intervention study
- Randomized controlled human trial
- Systematic review / meta-analysis

Higher-level evidence receives greater weight, while mechanistic studies remain valuable for understanding biological activity.

#### 2. Mechanistic Directness

Evidence is classified according to how directly the study demonstrates the proposed molecular mechanism:

- Direct target/pathway measurement
- Downstream pathway evidence
- Indirect biological association

Direct measurement of the proposed target or pathway provides stronger mechanistic evidence.

#### 3. Context Relevance

Evidence is evaluated according to its relevance to the intended biological context:

- Direct human skin evidence
- Skin tissue or skin cell evidence
- Non-skin evidence

Skin-specific evidence receives greater weight for ELYON skin-health assessments.

#### 4. Independent Replication

Evidence strength increases when findings are reproduced across:

- independent research groups
- different experimental models
- different study populations
- multiple publications

### Important considerations

Formulation-specific effects should be distinguished from effects attributable to the compound itself.

Positive, negative and non-significant findings should all be retained to reduce selective reporting bias.

Review articles may provide supporting context but should not be counted as independent primary experimental evidence.

### Score

Scientific Evidence Score: 0–20
 ### Score Architecture

The Scientific Evidence Score is calculated across four complementary dimensions:

- Study Level: 0–7 points
- Mechanistic Directness: 0–5 points
- Context Relevance: 0–5 points
- Independent Replication: 0–3 points

Maximum Scientific Evidence Score: 20 points.

Dose, route of administration and formulation are recorded as evidence qualifiers and do not independently increase the score.

#### Study Level — 0–7 points

Study Level reflects the highest level of primary experimental evidence available for the evaluated compound–target–context relationship.

- 0 points: No primary experimental evidence
- 2 points: In vitro experimental evidence
- 3 points: Animal in vivo experimental evidence
- 4 points: Human observational evidence
- 5 points: Non-randomized human intervention evidence
- 6 points: Randomized or controlled human intervention evidence
- 7 points: Multiple high-quality controlled human studies providing consistent evidence

Systematic reviews and meta-analyses are used for evidence synthesis and validation but do not automatically increase the Study Level score, in order to avoid double-counting primary studies.

#### Mechanistic Directness — 0–5 points

Mechanistic Directness reflects how directly the available experimental evidence supports the proposed compound–target or compound–pathway relationship.

- 0 points: No mechanistic evidence
- 1 point: Indirect biological association without measurement of the proposed target or pathway
- 2 points: Downstream biomarker evidence consistent with activation or inhibition of the proposed pathway
- 3 points: Direct measurement of the target or pathway showing a compound-associated change
- 4 points: Direct mechanistic evidence supported by multiple molecular readouts
- 5 points: Causal mechanistic evidence, such as target inhibition, knockdown, knockout or rescue experiments demonstrating that the biological effect depends on the proposed target or pathway

Mechanistic claims should not exceed the level directly supported by the experimental design.

#### Context Relevance — 0–5 points

Context Relevance reflects how closely the available evidence matches the biological context evaluated by ELYON: human skin health.

- 0 points: Evidence is not relevant to skin biology
- 1 point: Evidence originates from non-skin biological systems but may involve mechanisms relevant to skin
- 2 points: Evidence from animal-derived skin cells or indirect skin-related experimental models
- 3 points: Evidence from animal skin in vivo
- 4 points: Evidence from human skin cells, reconstructed human skin or ex vivo human skin
- 5 points: Direct evidence from human skin in vivo

The score reflects biological context rather than study quality. Study quality and experimental design are evaluated separately under Study Level.

#### Independent Replication — 0–3 points

Independent Replication reflects whether the proposed compound–target–context relationship is supported by independent studies and across different experimental models.

- 0 points: Evidence is derived from a single study
- 1 point: Multiple studies provide supporting evidence, but replication is limited to similar experimental models or conditions
- 2 points: Independent research groups provide consistent supporting evidence across different experimental models
- 3 points: Consistent evidence is demonstrated by multiple independent research groups across substantially different models, including human evidence

Studies from the same research group should not be considered fully independent replication.

Replication is evaluated based on consistency of the core biological relationship rather than identical experimental outcomes.

## Pillar 4
### Safety Profile

Questions

- Toxicity
- Irritation
- Contraindications
- Regulatory status

Score:
0–20

---

## Pillar 5
### Skin Relevance

Questions

Does the available evidence directly concern skin?

Examples

- collagen synthesis
- elastin
- wound healing
- UV protection
- hydration
- acne
- pigmentation

Score:
0–20

---

# Final Report

Each compound receives

- Overall Score

- Individual pillar scores

- Confidence Level

- Biological targets

- Relevant pathways

- Scientific summary

- Advantages

- Limitations

- Suggested applications
