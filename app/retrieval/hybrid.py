import json,re,math
from pathlib import Path
try:
 from rank_bm25 import BM25Okapi
except ImportError: BM25Okapi=None

def tok(s): return re.findall(r"[a-z0-9]+",s.lower())
class HybridRetriever:
    def __init__(self, corpus_path):
        self.chunks=[json.loads(x) for x in Path(corpus_path).read_text(encoding="utf8").splitlines() if x.strip()]
        self.tokens=[tok(c["text"]) for c in self.chunks]; self.bm25=BM25Okapi(self.tokens) if BM25Okapi else None
        self.calls=0
    def search(self, query, k=5):
        self.calls+=1; q=tok(query); lexical=self.bm25.get_scores(q) if self.bm25 else [sum(t in x for t in q) for x in self.tokens]
        # deterministic local dense proxy: cosine term-frequency vectors, independently ranked.
        dense=[sum(min(q.count(t),d.count(t)) for t in set(q))/math.sqrt(max(1,len(q)*len(d))) for d in self.tokens]
        ranks=[]
        for scores in (lexical,dense): ranks.append(sorted(range(len(scores)),key=lambda i:scores[i],reverse=True))
        rrf={}
        for rank in ranks:
          for pos,i in enumerate(rank,1): rrf[i]=rrf.get(i,0)+1/(60+pos)
        ids=sorted(rrf,key=rrf.get,reverse=True)
        seen=set(); out=[]
        for i in ids:
          c=dict(self.chunks[i]); key=re.sub(r"\W+","",c["text"].lower())
          if key not in seen and (lexical[i]>0 or dense[i]>0): seen.add(key); c["score"]=rrf[i]; out.append(c)
          if len(out)>=k: break
        return out
