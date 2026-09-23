from enum import Enum
from pydantic import BaseModel

class RetrievalDecision(str, Enum): WAIT="wait"; RETRIEVE="retrieve"; SUPPRESS="suppress"
class ControllerResult(BaseModel):
    decision: RetrievalDecision
    reason: str
    query: str | None = None
    stability: float = 0.0
