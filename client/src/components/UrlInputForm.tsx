import { useState, type FormEvent } from "react";

interface Props {
  loading: boolean;
  onSubmit: (url: string) => void;
}

export function UrlInputForm({ loading, onSubmit }: Props) {
  const [url, setUrl] = useState("");

  function handleSubmit(e: FormEvent) {
    e.preventDefault();
    if (url.trim()) onSubmit(url.trim());
  }

  return (
    <form onSubmit={handleSubmit} className="flex w-full max-w-xl gap-2">
      <input
        type="url"
        required
        placeholder="https://youtube.com/watch?v=..."
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        disabled={loading}
        className="flex-1 rounded-lg border border-slate-700 bg-slate-800 px-4 py-3 text-slate-100 outline-none focus:ring-2 focus:ring-teal-300 disabled:opacity-60"
      />
      <button
        type="submit"
        disabled={loading}
        className="rounded-lg bg-teal-300 px-5 py-3 font-semibold text-slate-900 disabled:opacity-60"
      >
        {loading ? "Listening…" : "Summarize"}
      </button>
    </form>
  );
}