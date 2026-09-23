"""Validates corpus schema; deterministic indexes are built at startup for reproducibility."""
import json,argparse,sys
from pathlib import Path
p=argparse.ArgumentParser(); p.add_argument('--corpus',default='corpus/raw/sample_corpus.jsonl'); a=p.parse_args()
rows=[json.loads(x) for x in Path(a.corpus).read_text().splitlines() if x]
assert all({'doc_id','section','text','chunk_id'}<=set(x) for x in rows); print(f'Validated {len(rows)} corpus chunks; startup builds BM25 and local dense proxy.')
