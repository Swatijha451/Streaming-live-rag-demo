# Streaming Live RAG

An offline-first, reproducible reference implementation of event-driven RAG: streamed transcript events enter a WAIT / RETRIEVE / SUPPRESS controller; stable requests are decomposed into intents, retrieved in parallel through hybrid BM25 plus a deterministic local dense proxy, fused by RRF, deduplicated, grounded at claim level, and preserved through delta-only session refinement.

## One-command replay

```bash
cp .env.example .env
docker compose up --build
```

This validates the sample corpus, replays all three streaming edge cases, writes `outputs/replay_report.json`, then serves `/health` on port 8000. For local execution: `pip install -r requirements.txt && python scripts/run_replay.py`.

## Guarantees and boundaries

- Mock mode is deterministic, offline, and extractive: factual answer sentences originate from corpus chunks; citations are only real `doc_id#section` chunk IDs.
- Unsupported claims have no citation and are expressed as uncertainty. The verifier rejects invented IDs.
- A late constraint calls `session.refinement.refine`, retrieving only the delta and retaining unaffected claims. Session state is in-memory per replay session; plug in SQLite for multi-process persistence.
- The local dense proxy is intentional for zero-download reproducibility. `OpenAICompatibleLLM` is provided for configured provider use, but an external model is a genuine deployment dependency and remains TODO for semantic reranking/generation.

## Layout

`app/controller` holds policy/stability; `app/intents` decomposition; `app/retrieval` BM25+dense/RRF/dedup; `app/session` state/refinement; `app/generation` grounded synthesis; `app/telemetry` lineage; `evaluation` replay, metrics, gates, baselines; `corpus` isolated evidence.

## Evaluation

`evaluation/metrics.py` reports early retrieval, false triggers, evidence and answer latency, citation support/precision, unsupported atomic claim rate, trace completeness, token/compute cost, redundant retrieval, full-rerun rate, and placeholders for externally labelled Recall@K/MRR/nDCG/intent F1. Those IR measures require relevance labels, deliberately not fabricated by this sample corpus. `evaluation/baselines.py` defines B1–B5 and two ablations (no WAIT and no delta refinement). Extend the JSONL corpus plus replay dataset—do not hardcode queries into source.

Run tests with `pytest -q`.
