from dataclasses import dataclass,field
from app.streaming.transcript import TranscriptChunk
@dataclass
class SessionState:
 session_id:str; transcript:list[TranscriptChunk]=field(default_factory=list); claims:list=field(default_factory=list); citations:set=field(default_factory=set); active_intents:list=field(default_factory=list); answer_version:int=0; current_answer:str=""; retrieval_calls:int=0
