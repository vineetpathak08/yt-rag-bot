"""
Centralized application settings.

All tunables live here and are overridable via environment variables (.env),
so nothing is hardcoded deep inside business logic.
"""
from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    # --- Google Generative AI ---
    google_api_key: str = os.getenv("GOOGLE_API_KEY", "")
    llm_model: str = os.getenv("LLM_MODEL", "gemini-2.5-flash")
    llm_temperature: float = float(os.getenv("LLM_TEMPERATURE", "0"))
    embedding_model: str = os.getenv("EMBEDDING_MODEL", "models/gemini-embedding-2")

    # --- Chunking ---
    chunk_size: int = int(os.getenv("CHUNK_SIZE", "800"))
    chunk_overlap: int = int(os.getenv("CHUNK_OVERLAP", "100"))

    # --- Retrieval ---
    retrieval_k: int = int(os.getenv("RETRIEVAL_K", "7"))

    # --- Transcript ---
    preferred_language: str = os.getenv("TRANSCRIPT_LANGUAGE", "en")

    # --- Gradio server ---
    server_name: str = os.getenv("SERVER_NAME", "0.0.0.0")
    server_port: int = int(os.getenv("SERVER_PORT", "7860"))

    def validate(self) -> None:
        if not self.google_api_key:
            raise EnvironmentError(
                "GOOGLE_API_KEY is not set. Add it to your .env file "
                "(see .env.example)."
            )


settings = Settings()
