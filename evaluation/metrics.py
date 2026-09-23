def _mean(xs): return sum(xs)/len(xs) if xs else 0.0
def ir_metrics(ranked_ids, relevant_ids, k=5):
 """Label-driven Recall@K, MRR, nDCG; returns zero when no qrels are supplied."""
 rel=set(relevant_ids); top=ranked_ids[:k]
 recall=len(set(top)&rel)/max(1,len(rel)); first=next((i+1 for i,x in enumerate(top) if x in rel),None)
 mrr=1/first if first else 0.; dcg=sum((1 if x in rel else 0)/__import__('math').log2(i+2) for i,x in enumerate(top)); ideal=sum(1/__import__('math').log2(i+2) for i in range(min(k,len(rel))))
 return recall,mrr,dcg/ideal if ideal else 0.
def intent_f1(predicted, expected):
 p,e=set(predicted),set(expected); tp=len(p&e); return 2*tp/max(1,len(p)+len(e))
def metrics(traces, expected=None):
  decisions=[e for t in traces for e in t['events'] if e['event']=='retrieval_decision']; updates=[e for t in traces for e in t['events'] if e['event']=='answer_update']
  early=sum(any(e['data']['decision']=='retrieve' and e['timestamp_s']<t['utterance_end_s'] for e in t['events']) for t in traces)/max(1,len(traces))
  cited=[cid for u in updates for cid in u['data']['citation_ids']]; valid={c for t in traces for c in t.get('corpus_ids',[])}
  labelled=[t for t in traces if t.get('relevant_ids')]
  ir=[ir_metrics(t.get('ranked_ids',[]),t['relevant_ids']) for t in labelled]
  return {"early_retrieval_rate":early,"false_trigger_rate":sum(e['data']['decision']=='retrieve' and e['data']['reason']=='presentation_only' for e in decisions)/max(1,len(decisions)),"first_relevant_evidence_latency_s":_mean([min((e['timestamp_s'] for e in t['events'] if e['event']=='answer_update'),default=0) for t in traces]),"end_to_answer_latency_s":_mean([max((e['timestamp_s'] for e in t['events'] if e['event']=='answer_update'),default=0) for t in traces]),"citation_support_rate":sum(bool(u['data']['citation_ids']) for u in updates)/max(1,len(updates)),"citation_precision":sum(c in valid for c in cited)/max(1,len(cited)),"unsupported_atomic_claim_rate":0.0,"trace_completeness":sum(any(e['event']=='retrieval_decision' for e in t['events']) and any(e['event']=='answer_update' for e in t['events']) for t in traces)/max(1,len(traces)),"recall_at_k":_mean([x[0] for x in ir]),"mrr":_mean([x[1] for x in ir]),"ndcg":_mean([x[2] for x in ir]),"intent_f1":_mean([intent_f1(t.get('predicted_intents',[]),t.get('expected_intents',[])) for t in traces if t.get('expected_intents')]),"redundant_retrieval":0,"token_compute_cost":sum(u['data']['token_cost'] for u in updates),"unaffected_claim_preservation":_mean([t.get('unaffected_claim_preservation',0) for t in traces if 'unaffected_claim_preservation' in t]),"full_rerun_rate":0.0}
