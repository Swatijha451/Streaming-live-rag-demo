from pydantic import BaseModel, Field

class TranscriptChunk(BaseModel):
    timestamp_s: float
    text: str
    utterance_id: str
    is_final: bool = False
    metadata: dict = Field(default_factory=dict)
