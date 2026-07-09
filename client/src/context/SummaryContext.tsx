import { createContext, useContext, useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../lib/api";
import type { Stage } from "../types";

type SummaryContextType = {
  stage: Stage;
  url: string;
  summary: string;
  error: string | null;
  summarize: (videoUrl: string) => Promise<void>;
  reset: () => void;
};

const SummaryContext = createContext<SummaryContextType | undefined>(undefined);

export function SummaryProvider({
  children,
}: {
  children: React.ReactNode;
}) {
  const [stage, setStage] = useState<Stage>("idle");
  const [url, setUrl] = useState("");
  const [summary, setSummary] = useState("");
  const [error, setError] = useState<string | null>(null);

  const navigate = useNavigate();

  async function summarize(videoUrl: string) {
    setStage("loading");
    setError(null);
    setUrl(videoUrl);

    try {
      const res = await api.summarize(videoUrl);

      setSummary(res.summary);
      setStage("ready");

      navigate("/video");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong.");
      setStage("idle");
    }
  }

  function reset() {
    setStage("idle");
    setUrl("");
    setSummary("");
    setError(null);

    navigate("/");
  }

  return (
    <SummaryContext.Provider
      value={{
        stage,
        url,
        summary,
        error,
        summarize,
        reset,
      }}
    >
      {children}
    </SummaryContext.Provider>
  );
}

export function useSummary() {
  const context = useContext(SummaryContext);

  if (!context) {
    throw new Error("useSummary must be used inside SummaryProvider");
  }

  return context;
}