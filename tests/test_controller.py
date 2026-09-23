from app.controller.retrieval_controller import RetrievalController
from app.controller.decision import RetrievalDecision
def test_wait_then_retrieve_and_suppress():
 c=RetrievalController()
 assert c.decide('Can you tell me').decision==RetrievalDecision.WAIT
 assert c.decide('Can you tell me cancellation policy for Venue A').decision==RetrievalDecision.RETRIEVE
 assert c.decide('Make that shorter in bullets',True).decision==RetrievalDecision.SUPPRESS
def test_no_false_trigger_on_presentation_request(): assert RetrievalController().decide('Translate that answer',True).decision==RetrievalDecision.SUPPRESS
