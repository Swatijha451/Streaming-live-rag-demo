from app.retrieval.hybrid import HybridRetriever
def test_hybrid_returns_real_ids_only():
 r=HybridRetriever('corpus/raw/sample_corpus.jsonl'); out=r.search('Pune venue capacity 30')
 assert out and all(x['chunk_id'].startswith('venue_a#') for x in out)
