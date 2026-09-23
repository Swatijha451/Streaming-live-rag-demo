from app.generation.grounding import verify_claim
def refine(state, delta, retriever, synthesizer):
    """Delta-only retrieval: retain old claims unless their terms overlap late constraints."""
    evidence=retriever.search(delta); state.retrieval_calls+=1
    answer,new_claims=synthesizer.synthesize(delta,evidence)
    affected={t.lower() for t in delta.split() if len(t)>3}
    kept=[c for c in state.claims if not affected.intersection(c.text.lower().split())]
    state.claims=kept+new_claims; state.citations={x for c in state.claims for x in c.citation_ids}; state.answer_version+=1
    state.current_answer="\n".join(f"- {c.text} [{c.citation_ids[0]}]" for c in state.claims if c.verified) or answer
    return state
