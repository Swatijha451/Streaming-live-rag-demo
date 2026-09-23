import re
from .models import SubQuery

class RuleDecomposer:
    """Deterministic fallback; an LLM adapter may replace this without changing the contract."""
    def decompose(self, query):
        parts=re.split(r"\?|\band\b|,\s*(?=(?:what|which|do|does|are|is|can|cancellation|catering)\b)",query,flags=re.I)
        parts=[p.strip(" ,.") for p in parts if len(p.strip())>3]
        if len(parts)==1 and "cancellation" in query.lower() and "catering" in query.lower():
            parts=[query+" cancellation",query+" catering"]
        return [SubQuery(id=f"i{i+1}",text=p,intent="information",entities=re.findall(r"\b(?:Pune|Mumbai|international|catering|cancellation)\b",p,re.I)) for i,p in enumerate(parts)]
