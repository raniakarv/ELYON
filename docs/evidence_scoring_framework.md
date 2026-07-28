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

## Objective

Evaluate the strength and reliability of the molecular relationship between a compound and its biological target(s).

Molecular Evidence focuses on target-level evidence, biological plausibility, mechanistic specificity and confidence across curated biological databases, independently of clinical or experimental outcome studies.

### Evidence Dimensions

Molecular Evidence is evaluated across four complementary dimensions:

#### 1. Target Evidence

Evaluates the strength of evidence supporting the molecular interaction between the compound and its biological target(s).

#### 2. Biological Plausibility

Evaluates the biological importance of the proposed target in skin physiology, homeostasis and disease-related molecular pathways.

#### 3. Molecular Specificity

Evaluates how specifically and consistently the proposed molecular mechanism has been characterized.

#### 4. Database Confidence

Evaluates the consistency and independent corroboration across curated biological knowledge resources.

### Important Considerations

Target evidence should be distinguished from downstream biological effects. Direct molecular interactions provide stronger evidence than indirect associations.

Compounds with multiple molecular targets should not automatically receive higher scores. The quality and characterization of the primary molecular mechanism are prioritized over the number of reported targets.

Curated biological databases provide complementary evidence and should be interpreted collectively rather than individually.

### Score Architecture
The Molecular Evidence Score is calculated across four complementary dimensions:

- Target Evidence: 0–7 points
- Biological Plausibility: 0–5 points
- Molecular Specificity: 0–5 points
- Database Confidence: 0–3 points

Maximum Molecular Evidence Score: 20 points.

Evidence from curated biological databases should complement, but not replace, experimental molecular evidence.

#### Target Evidence — 0–7 points

Target Evidence reflects the strength of evidence supporting the molecular interaction between the evaluated compound and its proposed biological target(s).

- 0 points: No molecular evidence supporting the interaction
- 1 point: Computational prediction only
- 2 points: Single experimental observation supporting the interaction
- 3 points: Multiple experimental observations
- 4 points: Direct molecular evidence demonstrating modulation of the proposed target (e.g., target expression, protein abundance, activity assays or pathway-specific molecular readouts)
- 5 points: Multiple direct molecular studies supporting the interaction
- 6 points: Strong evidence from independent studies using complementary molecular techniques
- 7 points: Extensive, reproducible molecular evidence supported by multiple independent studies and curated biological databases

Target Evidence reflects the quality and reproducibility of the molecular interaction rather than the number of reported biological effects.
Review articles may support mechanistic interpretation but should not independently increase the Target Evidence score.

#### Biological Plausibility — 0–5 points

Biological Plausibility reflects how strongly the proposed biological target is associated with skin physiology and pathology.

- 0 points: No established biological relevance to skin
- 1 point: Weak or indirect association with skin biology
- 2 points: Moderate association supported by limited evidence
- 3 points: Established role in one major skin-related biological process
- 4 points: Established role in multiple skin-related biological processes
- 5 points: Central regulator of multiple skin-relevant biological pathways

Biological Plausibility evaluates the biological importance of the target itself rather than the strength of evidence supporting the compound.

#### Molecular Specificity — 0–5 points

Molecular Specificity reflects how clearly the molecular mechanism of the compound has been characterized.

- 0 points: Molecular mechanism is unknown
- 1 point: Very broad or nonspecific biological activity
- 2 points: Multiple possible mechanisms with limited characterization
- 3 points: One well-supported primary molecular mechanism
- 4 points: Primary mechanism clearly established with secondary supporting mechanisms
- 5 points: Highly characterized molecular mechanism with strong target specificity or exceptionally well-defined pathway modulation

Compounds with multiple biological targets are not penalized, provided that a well-supported primary molecular mechanism has been established.

#### Database Confidence — 0–3 points

Database Confidence reflects the degree to which independent curated biological resources converge on the same molecular relationship.

- 0 points: No curated database support
- 1 point: Supported by one curated biological database
- 2 points: Supported by multiple curated biological databases
- 3 points: Consistent support across several high-quality curated biological resources

Examples of curated resources include UniProt, CTD, Reactome, Gene Ontology, KEGG, ChEMBL and DrugBank.
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
