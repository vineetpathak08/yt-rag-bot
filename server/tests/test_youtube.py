from core.youtube import get_video_id, flatten_transcript, TranscriptSegment


def test_watch_url():
    assert get_video_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ") == "dQw4w9WgXcQ"


def test_watch_url_no_www():
    assert get_video_id("https://youtube.com/watch?v=dQw4w9WgXcQ") == "dQw4w9WgXcQ"


def test_short_url():
    assert get_video_id("https://youtu.be/dQw4w9WgXcQ") == "dQw4w9WgXcQ"


def test_shorts_url():
    assert get_video_id("https://www.youtube.com/shorts/dQw4w9WgXcQ") == "dQw4w9WgXcQ"


def test_watch_url_with_extra_params():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=42s"
    assert get_video_id(url) == "dQw4w9WgXcQ"


def test_invalid_url_returns_none():
    assert get_video_id("https://example.com/not-a-video") is None


def test_empty_url_returns_none():
    assert get_video_id("") is None


def test_flatten_transcript():
    segments = [TranscriptSegment("hello", 0.0), TranscriptSegment("world", 1.5)]
    flattened = flatten_transcript(segments)
    assert "hello" in flattened and "world" in flattened


def test_flatten_empty_transcript():
    assert flatten_transcript([]) == ""
