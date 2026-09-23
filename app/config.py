from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Settings:
    corpus_path: str = os.getenv("CORPUS_PATH", "corpus/raw/sample_corpus.jsonl")
    llm_provider: str = os.getenv("LLM_PROVIDER", "mock")
    top_k: int = int(os.getenv("TOP_K", "5"))

settings = Settings()
