import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    app_name: str = os.getenv("APP_NAME", "Shreyas Agent API")
    app_env: str = os.getenv("APP_ENV", "dev")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")

    llm_base_url: str = os.getenv("LLM_BASE_URL", "http://localhost:11434")
    llm_model: str = os.getenv("LLM_MODEL", "llama3.1")

    qdrant_url: str = os.getenv("QDRANT_URL", "http://localhost:6333")
    qdrant_collection_evidence: str = os.getenv("QDRANT_COLLECTION_EVIDENCE", "career_evidence")
    qdrant_collection_platform: str = os.getenv("QDRANT_COLLECTION_PLATFORM", "platform_docs")

    evidence_repo_path: str = os.getenv("EVIDENCE_REPO_PATH", "")
    platform_docs_repo_path: str = os.getenv("PLATFORM_DOCS_REPO_PATH", "")


settings = Settings()