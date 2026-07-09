import { SummaryPanel } from "../components/SummaryPanel";
import { QAPanel } from "../components/QAPanel";
import { useQA } from "../hooks/useQA";
import { useSummary } from "../context/SummaryContext";

const VideoPage = () => {
    const { summary, url,reset } = useSummary();
    const { thread, asking, ask, clear } = useQA();
     console.log("VideoPage summary:", summary);
    function handleReset() {
    reset();
    clear();
  }


    return (
         <main className="flex min-h-screen flex-col bg-slate-900">
       <header className="flex items-center justify-between border-b border-slate-800 px-8 py-5">
        <div>
          <p className="font-mono text-xs uppercase tracking-widest text-teal-300">
            now viewing
         </p>
          <p className="mt-1 font-mono text-sm text-slate-400">{url}</p>
        </div>        
         <button
          onClick={handleReset}
          className="rounded-lg border border-slate-700 px-4 py-2 text-sm text-slate-400 hover:text-slate-100"
        >
          New video
        </button>
      </header>

      <div className="grid flex-1 grid-cols-1 divide-y divide-slate-800 md:grid-cols-2 md:divide-x md:divide-y-0">
        <SummaryPanel summary={summary} />
        <QAPanel thread={thread} videoUrl={url} asking={asking} onAsk={ask} />
      </div>
    </main>
    );
};

export default VideoPage;
