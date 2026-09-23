from app.session.state import SessionState
from app.session.refinement import refine
from app.retrieval.hybrid import HybridRetriever
from app.generation.synthesizer import MockLLM
from app.generation.grounding import Claim
def test_delta_refinement_preserves_unaffected_claims():
 s=SessionState('x',claims=[Claim(text='Standard business travel reimbursement requires original receipts.',citation_ids=['travel#standard'],verified=True)])
 refine(s,'international travel booked after travel',HybridRetriever('corpus/raw/sample_corpus.jsonl'),MockLLM())
 assert any('Standard business' in x.text for x in s.claims)
 assert s.retrieval_calls==1
