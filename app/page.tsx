import Image from "next/image"

export default function Page() {
  return (
    <main className="min-h-screen bg-background flex flex-col items-center justify-center p-4">
      <div className="flex flex-col items-center gap-10">
        {/* SCP Logo */}
        <div className="relative w-48 h-48 md:w-64 md:h-64">
          <Image
            src="/scp-logo.png"
            alt="SCP Foundation Logo"
            fill
            className="object-contain invert brightness-90"
            priority
          />
        </div>

        <h1
          className="font-sans text-3xl md:text-4xl lg:text-5xl font-semibold animate-glow text-balance text-center tracking-wide"
          style={{ color: "#ff8800" }}
        >
          SITE TWILIGHT
        </h1>

        <div className="flex items-center gap-4 text-muted-foreground font-sans text-xs md:text-sm tracking-[0.3em] uppercase">
          <div className="px-3 py-1 border border-border bg-card/50 rounded">CLEARANCE LEVEL 5 REQUIRED</div>
          <div className="w-1 h-1 rounded-full bg-muted-foreground" />
          <div className="px-3 py-1 border border-border bg-card/50 rounded">ACCESS DENIED</div>
        </div>

        <div className="flex items-center gap-4 text-muted-foreground font-sans text-xs md:text-sm tracking-[0.3em] mt-8">
          <span className="animate-bracket-left">{">--"}</span>
          <span className="font-bold">LOADING</span>
          <span className="animate-bracket-right">{"--<"}</span>
        </div>

        <div className="text-center mt-4 space-y-2">
          <p className="text-muted-foreground/80 font-sans text-xs md:text-sm tracking-[0.25em] uppercase">
            Secure · Contain · Protect
          </p>
          <p className="text-muted-foreground/50 font-sans text-[10px] md:text-xs tracking-wider">
            FOUNDATION DATABASE INITIALIZATION IN PROCESS
          </p>
        </div>
      </div>
    </main>
  )
}
