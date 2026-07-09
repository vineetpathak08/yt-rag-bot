from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


from config.settings import settings
from services.qa import answer_question
from services.summarizer import summarize_video

app = FastAPI(title="YouTube Video Summarizer and Q&A", description="A FastAPI application that summarizes YouTube videos and answers questions based on the video content.", version="1.0.0")


origins = [
    "http://localhost:5173", 
    
    "http://127.0.0.1:5173",    # Vite local development port
    "https://yourfrontend.com/*",  # my Production domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Allow specific origins
    allow_credentials=True,          # Support cookies and auth headers
    allow_methods=["*"],             # Allow all standard HTTP methods (GET, POST, etc.)
    allow_headers=["*"],             # Allow all HTTP request headers
)

class SummarizeRequest(BaseModel):
    video_url: str

class QuestionRequest(BaseModel):
    video_url: str
    question: str

@app.post("/summarize")
async def summarize(request: SummarizeRequest):
    """
    Summarizes the content of a YouTube video.

    Args:
        request (SummarizeRequest): The request body containing the video URL.

    Returns:
        dict: A dictionary containing the summary of the video.
    """
    summary = summarize_video(request.video_url)
    return {"summary": summary}

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    """
    Answers a question based on the content of a YouTube video.

    Args:
        request (QuestionRequest): The request body containing the video URL and the question.

    Returns:
        dict: A dictionary containing the answer to the question.
    """
    answer = answer_question(request.video_url, request.question)
    return {"answer": answer}

@app.get("/health")
def health():
    return {"status": "ok"}