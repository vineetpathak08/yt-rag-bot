import { useEffect, useRef, useState, type FormEvent } from "react";
import type { QAPair } from "../types";

interface Props {
  thread: QAPair[];
  asking: boolean;
  videoUrl: string;
  onAsk: (question: string, videoUrl: string) => void;
}

export function QAPanel({ thread, asking, videoUrl, onAsk }: Props) {
  const [question, setQuestion] = useState("");
  const endRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [thread, asking]);

  function handleSubmit(e: FormEvent) {
    e.preventDefault();
    if (!question.trim()) return;
    onAsk(question.trim(),videoUrl);
     
    setQuestion("");
  }

  return (
    <section className="flex flex-col p-7">
      <h2 className="font-display text-xl font-bold text-slate-100">
        Ask about this video
      </h2>
      <div className="mb-4 mt-2 h-0.5 w-12 bg-amber-400" />

      <div className="mb-4 flex-1 space-y-4 overflow-y-auto">
        {thread.length === 0 && (
          <p className="text-sm text-slate-400">
            No questions yet — ask anything about the video.
          </p>
        )}
        {thread.map((qa, i) => (
          <div key={i}>
            <p className="font-medium text-slate-100">{qa.question}</p>
            <p className="mt-1 leading-relaxed text-slate-400">{qa.answer}</p>
          </div>
        ))}
        {asking && <p className="text-teal-300">Thinking…</p>}
        <div ref={endRef} />
      </div>

      <form onSubmit={handleSubmit} className="sticky bottom-0 flex gap-2">
        <input
          type="text"
          placeholder="Ask your question here.."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          disabled={asking}
          className="flex-1 rounded-lg border border-slate-700 bg-slate-800 px-4 py-3 text-slate-100 outline-none focus:ring-2 focus:ring-teal-300 disabled:opacity-60"
        />
        <button
          type="submit"
          disabled={asking}
          className="rounded-lg bg-teal-300 px-5 py-3 font-semibold text-slate-900 disabled:opacity-60"
        >
          Ask
        </button>
      </form>
    </section>
  );
}