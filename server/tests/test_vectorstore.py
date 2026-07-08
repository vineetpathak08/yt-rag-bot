from core.vectorstore import chunk_text


def test_chunk_text_respects_size_roughly():
    text = "word " * 500
    chunks = chunk_text(text, chunk_size=200, chunk_overlap=20)
    assert len(chunks) > 1
    for c in chunks:
        assert len(c) <= 220  # small slack for splitter boundary behavior


def test_chunk_text_empty_input():
    assert chunk_text("", chunk_size=200, chunk_overlap=20) == []
