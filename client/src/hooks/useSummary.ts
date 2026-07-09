import { useState } from "react";
import { api } from "../lib/api";
import type { Stage } from "../types";
import { useNavigate } from "react-router-dom";

export function useSummary() {
  const [stage, setStage] = useState<Stage>("idle");
  const [url, setUrl] = useState("");
  const [summary, setSummary] = useState("");
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();
  async function summarize(videoUrl: string) {
    setError(null);
    setStage("loading");
    setUrl(videoUrl);
    try {
      const res = await api.summarize(videoUrl);
      console.log("Summary response:", res.summary);
      setSummary(res.summary);
      setStage("ready");
      navigate("/video", {
        state: {
          summary: res.summary,
          url: videoUrl,
        },
      });
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong.");
      setStage("idle");
    }
  }

  function reset() {
    const navigate = useNavigate();
    setStage("idle");
    setUrl("");
    setSummary("");
    setError(null);
    navigate("/");
  }

  return { stage, url, summary, error, summarize, reset };
}
