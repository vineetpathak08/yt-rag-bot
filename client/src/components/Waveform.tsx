export function Waveform() {
  return (
    <div
      aria-hidden
      className="h-7 w-32 animate-pulse bg-[repeating-linear-gradient(90deg,theme(colors.teal.300)_0_3px,transparent_3px_8px)] bg-bottom bg-no-repeat"
      style={{ backgroundSize: "100% 60%" }}
    />
  );
}