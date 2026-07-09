
import { UrlInputForm } from "../components/UrlInputForm";
import { Waveform } from "../components/Waveform";
import { useSummary } from "../context/SummaryContext";


const HomePage = () => {

     const { stage, error, summarize } = useSummary();
  return (
      <main className="flex min-h-screen flex-col items-center justify-center gap-4 bg-slate-900 px-8 text-center">
        <p className="font-mono text-xs uppercase tracking-widest text-teal-300">
          transcript · summary · q&amp;a
        </p>
        <h1 className="font-display max-w-[20ch] text-3xl font-bold text-slate-100 sm:text-4xl">
          Drop a YouTube link, get the signal.
        </h1>
        <UrlInputForm loading={stage === "loading"} onSubmit={summarize} />
        {stage === "loading" && <Waveform />}
        {error && <p className="text-sm text-red-400">{error}</p>}
      </main>
    );
};

export default HomePage;
