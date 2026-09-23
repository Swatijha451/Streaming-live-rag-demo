import re

PRESENTATION = re.compile(r"\b(shorter|bullet|bullets|translate|format|rephrase|summari[sz]e|make it)\b", re.I)
REQUEST = re.compile(r"\b(what|which|where|when|how|can you|need|tell me|provide|is|are|does|do)\b|\?", re.I)
STOP = {"i","me","a","an","the","for","to","in","and","of","it","this","that","can","you","need"}
def content_terms(text): return {x.lower() for x in re.findall(r"[a-zA-Z0-9]+", text) if x.lower() not in STOP and len(x)>2}
def features(text, previous):
    terms, old = content_terms(text), content_terms(previous)
    delta = len(terms-old)/max(1,len(terms))
    has_subject = len(terms)>=2
    complete = bool(REQUEST.search(text)) and has_subject and len(text.split())>=5
    stability = min(1.0, .35*bool(REQUEST.search(text))+.35*has_subject+.30*delta)
    return {"presentation":bool(PRESENTATION.search(text)),"complete":complete,"delta":delta,"stability":stability}
