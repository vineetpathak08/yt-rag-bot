interface Props {
  summary: string;
}

export function SummaryPanel({ summary }: Props) {
  return (
    <section className="overflow-y-auto p-7">
      <h2 className="font-display text-xl font-bold text-slate-100">Summary</h2>
      <div className="mb-4 mt-2 h-0.5 w-12 bg-amber-400" />
      <p className="whitespace-pre-wrap leading-relaxed text-slate-200">
        {summary}
      </p>
    </section>
  );
}