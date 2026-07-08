"""
Summarization use case: fetch transcript (if needed) -> summarize.
"""
from __future__ import annotations

import logging

from langchain_core.output_parsers import StrOutputParser

from config.settings import settings
from core import prompts
from core.llm import get_llm
from core.youtube import TranscriptError, fetch_transcript, flatten_transcript, get_video_id
from services.session import VideoState, session_cache

logger = logging.getLogger(__name__)


def summarize_video(video_url: str) -> str:
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
        state = VideoState(video_id=video_id, transcript_segments=segments, processed_transcript=processed)
        session_cache.set(state)

    if not state.processed_transcript:
        return "No transcript available for this video."

    llm = get_llm()
    chain = prompts.summary_prompt() | llm | StrOutputParser()
    return chain.invoke({"transcript": state.processed_transcript})
