import asyncio,json
from pathlib import Path
from app.retrieval.hybrid import HybridRetriever
from app.generation.synthesizer import MockLLM
from app.controller.retrieval_controller import RetrievalController
from app.telemetry.logger import TelemetryLogger
from app.session.state import SessionState
from app.streaming.transcript import TranscriptChunk
from app.streaming.simulator import StreamingRAG
from .metrics import metrics
from .gates import evaluate_gates
async def replay(dataset, corpus):
 traces=[]
 for scenario in json.loads(Path(dataset).read_text()):
  logger=TelemetryLogger(); engine=StreamingRAG(HybridRetriever(corpus),MockLLM(),RetrievalController(),logger); state=SessionState(scenario['id'])
  for x in scenario['events']: await engine.process(state,TranscriptChunk(**x))
  traces.append({'id':scenario['id'],'events':logger.events,'utterance_end_s':scenario['events'][-1]['timestamp_s'],'corpus_ids':[f"{x['doc_id']}#{x['section']}" for x in json.loads(Path(corpus).read_text())]})
 m=metrics(traces); return {'metrics':m,'gates':evaluate_gates(m),'traces':traces}
