"""
Chunking and vector store construction/search.
"""
from __future__ import annotations

from langchain_community.vectorstores import FAISS
from langchain_core.embeddings import Embeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(text: str, chunk_size: int, chunk_overlap: int) -> list[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return splitter.split_text(text)


def build_faiss_index(chunks: list[str], embedding_model: Embeddings) -> FAISS:
    if not chunks:
        raise ValueError("Cannot build a FAISS index from an empty chunk list.")
    return FAISS.from_texts(chunks, embedding_model)


def similarity_search(faiss_index: FAISS, query: str, k: int = 7):
    return faiss_index.similarity_search(query, k=k)
