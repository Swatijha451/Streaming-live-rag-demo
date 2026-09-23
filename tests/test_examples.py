import asyncio
from evaluation.replay import replay
def test_three_edge_cases_replay_with_complete_trace(tmp_path):
 r=asyncio.run(replay('evaluation/datasets/scenarios.json','corpus/raw/sample_corpus.jsonl'))
 assert len(r['traces'])==3 and r['metrics']['trace_completeness']>=2/3
 assert r['metrics']['citation_precision']==1
