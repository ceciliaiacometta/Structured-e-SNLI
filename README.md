# Structured-e-SNLI
Structered explanations for SNLI 

Explanations in Natural Language Inference (NLI) remain predominantly unstructured, making systematic comparison and interpretability challenging.
The e-SNLI (Camburu et al.,2018) dataset extends SNLI by providing human-written explanations, but their variability in phrasing and granularity hinders structured analysis. 
In this project, we introduce a rule-based approach to extract Structured Explanations, transforming free-text justifications into formal representations consisting of operators and arguments. Our method leverages syntactic parsing and pattern matching to identify recurring linguistic structures.
We evaluate our approach quantitatively by measuring dataset coverage, which refers to the proportion of explanations that could be successfully structured using predefined rules, and qualitatively through manual alignment with human reasoning. The results indicate that our method effectively captures structured reasoning for a significant portion of explanations, with higher coverage in contradiction cases than in entailment or neutral cases. 
Although structured representations improve interpretability, limitations related to annotation inconsistencies and syntactic variability remain.

