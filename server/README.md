# YouTube RAG Summarizer & Q&A Bot

A Gradio app that fetches a YouTube video's transcript, summarizes it, and
answers questions about it using retrieval-augmented generation over a
FAISS index.

## Project layout

```
yt_rag_bot/
├── main.py                # entrypoint: python main.py
├── config/
│   └── settings.py        # all env-driven config in one place
├── core/                  # pure, stateless building blocks
│   ├── youtube.py         # video ID parsing + transcript fetching
│   ├── llm.py             # LLM / embedding model construction
│   ├── vectorstore.py     # chunking + FAISS index build/search
│   └── prompts.py         # prompt templates
├── services/               # use-case orchestration (what main.py calls)
│   ├── session.py          # per-video cache (transcript + FAISS index)
│   ├── summarizer.py       # summarize_video()
│   └── qa.py                # answer_question()
├── ui/
│   └── app.py              # Gradio Blocks UI — only talks to services/
├── tests/
│   ├── test_youtube.py
│   └── test_vectorstore.py
├── requirements.txt
└── .env.example
```




