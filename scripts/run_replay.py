import argparse,asyncio,json,sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from evaluation.replay import replay
p=argparse.ArgumentParser();p.add_argument('--dataset',default='evaluation/datasets/scenarios.json');p.add_argument('--corpus',default='corpus/raw/sample_corpus.jsonl');p.add_argument('--output',default='outputs/replay_report.json');a=p.parse_args()
r=asyncio.run(replay(a.dataset,a.corpus)); open(a.output,'w').write(json.dumps(r,indent=2)); print(json.dumps({'metrics':r['metrics'],'gates':r['gates']},indent=2))
