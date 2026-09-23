import re
from pydantic import BaseModel
class Claim(BaseModel): text:str; citation_ids:list[str]=[]; confidence:float=0.; verified:bool=False; affected:bool=False
def verify_claim(text, chunks):
    q={x for x in re.findall(r"[a-z0-9]+",text.lower()) if len(x)>3}
    supported=[c["chunk_id"] for c in chunks if len(q & set(re.findall(r"[a-z0-9]+",c["text"].lower())))>=max(1,min(3,len(q)//2))]
    return Claim(text=text,citation_ids=supported[:1],confidence=.9 if supported else .15,verified=bool(supported))
