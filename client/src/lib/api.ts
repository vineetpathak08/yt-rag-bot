import type { SummarizeResponse, AskResponse } from "../types";

export const API_BASE = import.meta.env.VITE_API_BASE ?? "http://localhost:7860";

async function post<T>(path: string, body: unknown): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });

  if (!res.ok) {
    const text = await res.text().catch(() => "");
    throw new Error(text || `Request failed (${res.status})`);
  }

  return res.json() as Promise<T>;
}

export const api = {
  summarize: (url: string) => post<SummarizeResponse>("/summarize", { video_url: url }),
  ask: (question: string, videoUrl: string) => post<AskResponse>("/ask", { question, video_url: videoUrl }),
};