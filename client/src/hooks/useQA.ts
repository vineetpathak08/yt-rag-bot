import { useState } from "react";
import { api } from "../lib/api";
import type { QAPair } from "../types";

export function useQA() {
  const [thread, setThread] = useState<QAPair[]>([]);
  const [asking, setAsking] = useState(false);


  async function ask(question: string, videoUrl: string, ) {
    if (!question.trim() || asking) return;
    setAsking(true);
    try {
      const res = await api.ask(question.trim(), videoUrl);
      setThread((t) => [...t, { question, answer: res.answer }]);
    } catch (err) {
      const message = err instanceof Error ? err.message : "unknown error";
      setThread((t) => [
        ...t,
        { question, answer: `Couldn't get an answer: ${message}` },
      ]);
    } finally {
      setAsking(false);
    }
  }

  function clear() {
    setThread([]);
  }

  return { thread, asking, ask, clear };
}