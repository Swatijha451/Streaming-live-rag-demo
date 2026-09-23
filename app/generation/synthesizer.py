from .grounding import verify_claim
class MockLLM:
    """Extractive deterministic generator; never introduces facts outside evidence."""
    def synthesize(self, query, chunks):
        claims=[]
        for c in chunks[:3]:
            claim=verify_claim(c['text'],[c])
            if claim.verified: claims.append(claim)
        if not claims: return "I could not verify an answer from the supplied corpus.",[]
        answer="\n".join(f"- {x.text} [{x.citation_ids[0]}]" for x in claims)
        return answer,claims
