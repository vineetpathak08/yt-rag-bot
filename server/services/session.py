"""
Session-level cache.

The original script kept `fetched_transcript` / `processed_transcript` as
module-level globals, which caused two problems:
  1. Asking a second question re-built the FAISS index from scratch every
     single time (slow + costs an embedding call per question).
  2. Switching to a new video URL without restarting the app could silently
     keep answering from the *previous* video's transcript.

This module fixes both by keying cached state off the video ID and
invalidating it whenever the URL changes.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from langchain_community.vectorstores import FAISS

from core.youtube import TranscriptSegment


@dataclass
class VideoState:
    video_id: str
    transcript_segments: list[TranscriptSegment] = field(default_factory=list)
    processed_transcript: str = ""
    faiss_index: FAISS | None = None


class SessionCache:
    """A tiny single-slot cache. Swap for a dict keyed by user/session id
    if you need multi-user concurrency (e.g. behind a real web server)."""

    def __init__(self) -> None:
        self._state: VideoState | None = None

    def get(self, video_id: str) -> VideoState | None:
        if self._state and self._state.video_id == video_id:
            return self._state
        return None

    def set(self, state: VideoState) -> None:
        self._state = state

    def clear(self) -> None:
        self._state = None


# Module-level singleton used by the Gradio app. This is still global state,
# but it is now explicit, typed, and invalidated correctly per video —
# rather than an implicit, leaky pair of loose variables.
session_cache = SessionCache()
