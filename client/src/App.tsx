
import { Routes, Route } from "react-router-dom";


import HomePage  from "./pages/HomePage";
import VideoPage  from "./pages/VideoPage";

// export default function App() {
//   const { stage, url, summary, error, summarize, reset } = useSummary();
//   const { thread, asking, ask, clear } = useQA();
  
//   function handleReset() {
//     reset();
//     clear();
//   }

//   if (stage !== "ready") {
//     return (
//       <main className="flex min-h-screen flex-col items-center justify-center gap-4 bg-slate-900 px-8 text-center">
//         <p className="font-mono text-xs uppercase tracking-widest text-teal-300">
//           transcript · summary · q&amp;a
//         </p>
//         <h1 className="font-display max-w-[20ch] text-3xl font-bold text-slate-100 sm:text-4xl">
//           Drop a YouTube link, get the signal.
//         </h1>
//         <UrlInputForm loading={stage === "loading"} onSubmit={summarize} />
//         {stage === "loading" && <Waveform />}
//         {error && <p className="text-sm text-red-400">{error}</p>}
//       </main>
//     );
//   }

//   return (
//     <main className="flex min-h-screen flex-col bg-slate-900">
//       <header className="flex items-center justify-between border-b border-slate-800 px-8 py-5">
//         <div>
//           <p className="font-mono text-xs uppercase tracking-widest text-teal-300">
//             now viewing
//           </p>
//           <p className="mt-1 font-mono text-sm text-slate-400">{url}</p>
//         </div>
//         <button
//           onClick={handleReset}
//           className="rounded-lg border border-slate-700 px-4 py-2 text-sm text-slate-400 hover:text-slate-100"
//         >
//           New video
//         </button>
//       </header>

//       <div className="grid flex-1 grid-cols-1 divide-y divide-slate-800 md:grid-cols-2 md:divide-x md:divide-y-0">
//         <SummaryPanel summary={summary} />
//         <QAPanel thread={thread} videoUrl={url} asking={asking} onAsk={ask} />
//       </div>
//     </main>

    
//   );
// }


export default function App() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/video" element={<VideoPage />} />
    </Routes>
  );
}
   
 