def deduplicate(chunks):
    seen=set(); return [c for c in chunks if not (c['chunk_id'] in seen or seen.add(c['chunk_id']))]
