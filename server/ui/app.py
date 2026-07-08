"""
Gradio interface. This module only knows about `services` — it never
touches core/ or config/ directly, so the UI can be swapped (e.g. for
FastAPI/Streamlit) without touching business logic.
"""
import gradio as gr

from config.settings import settings
from services.qa import answer_question
from services.summarizer import summarize_video


def build_interface() -> gr.Blocks:
    with gr.Blocks(title="YouTube Video Summarizer and Q&A") as interface:
        gr.Markdown("<h2 style='text-align: center;'>YouTube Video Summarizer and Q&A</h2>")

        video_url = gr.Textbox(label="YouTube Video URL", placeholder="Enter the YouTube Video URL")

        summary_output = gr.Textbox(label="Video Summary", lines=5)
        question_input = gr.Textbox(label="Ask a Question About the Video", placeholder="Ask your question")
        answer_output = gr.Textbox(label="Answer to Your Question", lines=5)

        summarize_btn = gr.Button("Summarize Video")
        question_btn = gr.Button("Ask a Question")

        summarize_btn.click(summarize_video, inputs=video_url, outputs=summary_output)
        question_btn.click(answer_question, inputs=[video_url, question_input], outputs=answer_output)

    return interface


def launch() -> None:
    settings.validate()
    interface = build_interface()
    interface.launch(server_name=settings.server_name, server_port=settings.server_port)
