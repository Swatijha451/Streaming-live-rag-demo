from app.generation.grounding import verify_claim
def test_unsupported_claim_is_uncertain_not_cited():
 c=verify_claim('Venue A has a swimming pool',[{'chunk_id':'venue_a#capacity','text':'Venue A accommodates 30 attendees.'}])
 assert not c.verified and c.citation_ids==[] and c.confidence<.5
def test_never_invents_citation():
 c=verify_claim('Mars colony policy',[]); assert c.citation_ids==[]
