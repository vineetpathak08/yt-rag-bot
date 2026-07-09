export interface SummarizeResponse {
  summary: string;
}

export interface AskResponse {
  answer: string;
}

export interface QAPair {
  question: string;
  answer: string;
}

export type Stage = "idle" | "loading" | "ready";