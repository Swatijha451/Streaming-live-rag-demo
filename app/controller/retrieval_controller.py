from .decision import RetrievalDecision, ControllerResult
from .intent_stability import features

class RetrievalController:
    def __init__(self): self.last_query=""
    def decide(self, transcript: str, is_final=False):
        f=features(transcript,self.last_query)
        if f["presentation"]: return ControllerResult(decision=RetrievalDecision.SUPPRESS,reason="presentation_only",stability=f["stability"])
        if not f["complete"] and not is_final: return ControllerResult(decision=RetrievalDecision.WAIT,reason="insufficient_semantic_completeness",stability=f["stability"])
        if f["delta"] < .12 and not is_final: return ControllerResult(decision=RetrievalDecision.WAIT,reason="no_material_delta",stability=f["stability"])
        self.last_query=transcript
        return ControllerResult(decision=RetrievalDecision.RETRIEVE,reason="stable_request_or_final",query=transcript,stability=f["stability"])
