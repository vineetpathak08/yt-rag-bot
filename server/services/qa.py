"""
Q&A use case: fetch transcript (if needed) -> chunk -> embed -> retrieve -> answer.

The FAISS index and embeddings are cached per video_id via `session_cache`,
so asking multiple questions about the same video only pays the embedding
cost once, not once per question (the original script's behavior).
"""
from __future__ import annotations

import logging

from langchain_core.output_parsers import StrOutputParser

from config.settings import settings
from core import prompts
from core.llm import get_embedding_model, get_llm
from core.vectorstore import build_faiss_index, chunk_text, similarity_search
from core.youtube import TranscriptError, fetch_transcript, flatten_transcript, get_video_id
from services.session import VideoState, session_cache

logger = logging.getLogger(__name__)


def _get_or_build_index(video_url: str) -> VideoState | str:
    """Returns a populated VideoState, or an error string on failure."""
    video_id = get_video_id(video_url)
    if not video_id:
        return "Please provide a valid YouTube URL."

    state = session_cache.get(video_id)

    if state is None or not state.processed_transcript:
        try:
            segments = fetch_transcript(video_url, language=settings.preferred_language)
        except TranscriptError as exc:
            logger.warning("Transcript fetch failed: %s", exc)
            return str(exc)

        processed = flatten_transcript(segments)
        if not processed:
            return "No transcript available for this video."

        state = VideoState(video_id=video_id, transcript_segments=segments, processed_transcript=processed)
        session_cache.set(state)

    if state.faiss_index is None:
        chunks = chunk_text(state.processed_transcript, settings.chunk_size, settings.chunk_overlap)
        embedding_model = get_embedding_model()
        state.faiss_index = build_faiss_index(chunks, embedding_model)
        session_cache.set(state)

    return state


def answer_question(video_url: str, question: str) -> str:
    if not question or not question.strip():
        return "Please enter a question."

    result = _get_or_build_index(video_url)
    if isinstance(result, str):
        return result
    state = result

    relevant_docs = similarity_search(state.faiss_index, question, k=settings.retrieval_k)
    context = "\n".join(doc.page_content for doc in relevant_docs)

    llm = get_llm()
    chain = prompts.qa_prompt() | llm | StrOutputParser()
    return chain.invoke({"context": context, "question": question})
