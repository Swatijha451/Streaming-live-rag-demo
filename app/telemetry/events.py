from pydantic import BaseModel,Field
class TelemetryEvent(BaseModel): event:str; timestamp_s:float; session_id:str; data:dict=Field(default_factory=dict)
