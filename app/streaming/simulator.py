from app.controller.decision import RetrievalDecision
from app.intents.decomposer import RuleDecomposer
from app.session.state import SessionState
from app.session.refinement import refine

class StreamingRAG:
 def __init__(self,retriever,synthesizer,controller,logger): self.retriever=retriever; self.synthesizer=synthesizer; self.controller=controller; self.logger=logger; self.decomposer=RuleDecomposer()
 async def process(self,state,event):
  state.transcript.append(event); transcript=" ".join(x.text for x in state.transcript)
  result=self.controller.decide(transcript,event.is_final)
  self.logger.emit("retrieval_decision",event.timestamp_s,state.session_id,decision=result.decision.value,reason=result.reason,stability=result.stability)
  if result.decision!=RetrievalDecision.RETRIEVE: return result
  intents=self.decomposer.decompose(result.query); state.active_intents=intents
  # Parallel interface is retained; local index is CPU deterministic.
  chunks=[]
  for intent in intents: chunks.extend(self.retriever.search(intent.text))
  unique={c['chunk_id']:c for c in chunks}; evidence=list(unique.values()); state.retrieval_calls+=len(intents)
  answer,claims=self.synthesizer.synthesize(transcript,evidence); state.claims=claims; state.citations={x for c in claims for x in c.citation_ids}; state.current_answer=answer; state.answer_version+=1
  self.logger.emit("answer_update",event.timestamp_s,state.session_id,answer_version=state.answer_version,citation_ids=sorted(state.citations),token_cost=len(transcript.split()),documents=[c['chunk_id'] for c in evidence])
  return result
