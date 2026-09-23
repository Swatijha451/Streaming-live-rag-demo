import json
class TelemetryLogger:
 def __init__(self): self.events=[]
 def emit(self,event,timestamp_s,session_id,**data): self.events.append({"event":event,"timestamp_s":timestamp_s,"session_id":session_id,"data":data})
 def jsonl(self): return "\n".join(json.dumps(x) for x in self.events)
