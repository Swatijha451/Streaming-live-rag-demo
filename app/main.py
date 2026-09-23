from fastapi import FastAPI
from app.config import settings
from app.retrieval.hybrid import HybridRetriever
app=FastAPI(title='Streaming Live RAG')
@app.get('/health')
def health(): return {'ok':True,'corpus_chunks':len(HybridRetriever(settings.corpus_path).chunks),'provider':settings.llm_provider}
