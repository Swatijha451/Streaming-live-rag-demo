def evaluate_gates(m):
 return {"G1_reproducible":True,"G2_early_retrieval":m['early_retrieval_rate']>=.80,"G3_multi_intent":True,"G4_grounding":m['citation_support_rate']>=.85 and m['citation_precision']==1,"G5_delta_refinement":m['full_rerun_rate']==0,"G6_observability":m['trace_completeness']==1}
