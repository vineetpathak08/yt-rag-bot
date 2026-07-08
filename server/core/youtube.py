"""
Everything related to talking to YouTube: parsing video URLs and
fetching/normalizing transcripts.
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)

logger = logging.getLogger(__name__)

# Covers: watch?v=, youtu.be/, /shorts/, /embed/ — with or without www.
_VIDEO_ID_PATTERN = re.compile(
    r"(?:youtube\.com/(?:watch\?v=|shorts/|embed/)|youtu\.be/)([a-zA-Z0-9_-]{11})"
)


class TranscriptError(Exception):
    """Raised whenever a transcript cannot be retrieved for a video."""


@dataclass
class TranscriptSegment:
    text: str
    start: float


def get_video_id(url: str) -> str | None:
    """Extract an 11-character YouTube video ID from a variety of URL shapes."""
    if not url:
        return None
    match = _VIDEO_ID_PATTERN.search(url)
    return match.group(1) if match else None


def fetch_transcript(url: str, language: str = "en") -> list[TranscriptSegment]:
    """
    Fetch the transcript for a YouTube URL, preferring a manually created
    transcript over an auto-generated one.

    Raises:
        TranscriptError: if the URL is invalid or no transcript is available.
    """
    video_id = get_video_id(url)
    if not video_id:
        raise TranscriptError(f"Could not extract a video ID from URL: {url!r}")

    ytt_api = YouTubeTranscriptApi()

    try:
        transcript_list = ytt_api.list(video_id)
    except (TranscriptsDisabled, VideoUnavailable) as exc:
        raise TranscriptError(f"Transcript unavailable for video {video_id}: {exc}") from exc

    auto_generated = None
    for t in transcript_list:
        if t.language_code != language:
            continue
        if t.is_generated:
            auto_generated = auto_generated or t
        else:
            # Manually created transcript wins outright.
            logger.info("Using manually created transcript for %s", video_id)
            return [TranscriptSegment(seg.text, seg.start) for seg in t.fetch()]

    if auto_generated:
        logger.info("Using auto-generated transcript for %s", video_id)
        return [TranscriptSegment(seg.text, seg.start) for seg in auto_generated.fetch()]

    raise TranscriptError(
        f"No '{language}' transcript (manual or auto-generated) found for video {video_id}"
    )


def flatten_transcript(segments: list[TranscriptSegment]) -> str:
    """Turn transcript segments into a single string suitable for chunking/summarizing."""
    if not segments:
        return ""
    return "\n".join(f"Text: {s.text} Start: {s.start}" for s in segments)
