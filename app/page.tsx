"use client"

import Image from "next/image"
import { useEffect, useState } from "react"

function generateAlias(ip: string): string {
  let hash = 0
  for (let i = 0; i < ip.length; i++) {
    const char = ip.charCodeAt(i)
    hash = (hash << 5) - hash + char
    hash = hash & hash
  }
  const hashStr = Math.abs(hash).toString(16).toUpperCase().slice(0, 6)
  return `SUBJECT-${hashStr}`
}

function redactText(text: string, percentage = 0.6): string {
  const chars = text.split("")
  return chars
    .map((char, i) => (Math.random() < percentage && char !== "." && char !== "-" && char !== " " ? "█" : char))
    .join("")
}

export default function Page() {
  const [loadingStage, setLoadingStage] = useState<"stage1" | "stage2" | "complete">("stage1")
  const [ipData, setIpData] = useState({ ip: "███.███.███.██", country: "███████", alias: "SUBJECT-███" })
  const [stage1Line, setStage1Line] = useState(0)
  const [typedText, setTypedText] = useState("")
  const [stage2Progress, setStage2Progress] = useState(0)
  const [spinnerIndex, setSpinnerIndex] = useState(0)
  const [dots, setDots] = useState("")

  useEffect(() => {
    const fetchIpData = async () => {
      try {
        const response = await fetch("https://ipapi.co/json/")
        const data = await response.json()
        const alias = generateAlias(data.ip)
        setIpData({
          ip: data.ip || "███.███.███.██",
          country: data.country_name || "███████",
          alias,
        })
      } catch (error) {
        console.log("[v0] Failed to fetch IP data:", error)
      }
    }
    fetchIpData()
  }, [])

  useEffect(() => {
    if (loadingStage !== "stage1") return

    const lines = [
      `ALIAS: ${redactText(ipData.alias, 0.3)}`,
      `COUNTRY: ${redactText(ipData.country, 0.4)}`,
      `IP: ${redactText(ipData.ip, 0.5)}`,
    ]

    let charIndex = 0
    const currentLine = lines[stage1Line]

    const typeInterval = setInterval(() => {
      if (charIndex < currentLine.length) {
        setTypedText(currentLine.slice(0, charIndex + 1))
        charIndex++
      } else {
        clearInterval(typeInterval)
        setTimeout(() => {
          if (stage1Line < lines.length - 1) {
            setStage1Line(stage1Line + 1)
            setTypedText("")
          } else {
            setTimeout(() => {
              setLoadingStage("stage2")
            }, 800)
          }
        }, 1200)
      }
    }, 50)

    return () => clearInterval(typeInterval)
  }, [loadingStage, stage1Line, ipData])

  useEffect(() => {
    if (loadingStage !== "stage2") return

    const progressInterval = setInterval(() => {
      setStage2Progress((prev) => {
        if (prev >= 100) {
          clearInterval(progressInterval)
          setTimeout(() => {
            setLoadingStage("complete")
          }, 500)
          return 100
        }
        return prev + 2
      })
    }, 50)

    return () => clearInterval(progressInterval)
  }, [loadingStage])

  useEffect(() => {
    if (loadingStage !== "stage2") return

    const spinnerChars = ["|", "/", "-", "\\"]
    const spinnerInterval = setInterval(() => {
      setSpinnerIndex((prev) => (prev + 1) % spinnerChars.length)
    }, 150)

    return () => clearInterval(spinnerInterval)
  }, [loadingStage])

  useEffect(() => {
    if (loadingStage !== "stage2") return

    const dotsInterval = setInterval(() => {
      setDots((prev) => {
        if (prev === "...") return ""
        return prev + "."
      })
    }, 500)

    return () => clearInterval(dotsInterval)
  }, [loadingStage])

  if (loadingStage === "stage1") {
    return (
      <main className="min-h-screen flex items-center justify-center" style={{ backgroundColor: "#050505" }}>
        <div className="font-mono text-lg md:text-xl tracking-wider" style={{ color: "#e0e0e0" }}>
          <div className="border border-gray-700 p-8 md:p-12 bg-black/40">
            <div className="h-8" style={{ fontFamily: "monospace" }}>
              {typedText}
              <span className="animate-pulse">_</span>
            </div>
          </div>
        </div>
      </main>
    )
  }

  if (loadingStage === "stage2") {
    const spinnerChars = ["|", "/", "-", "\\"]
    const filledBlocks = Math.floor((stage2Progress / 100) * 20)
    const emptyBlocks = 20 - filledBlocks
    const loadingBar = `[${"■".repeat(filledBlocks)}${"□".repeat(emptyBlocks)}]`

    return (
      <main className="min-h-screen flex items-center justify-center" style={{ backgroundColor: "#050505" }}>
        <div
          className="font-mono text-base md:text-lg tracking-wider flex flex-col items-center gap-8"
          style={{ color: "#e0e0e0" }}
        >
          {/* ASCII Spinner */}
          <div className="text-4xl md:text-5xl font-bold">{spinnerChars[spinnerIndex]}</div>

          {/* Loading Bar */}
          <div className="text-xl md:text-2xl tracking-widest">{loadingBar}</div>

          {/* Initializing Database text */}
          <div className="text-sm md:text-base">Initializing Database{dots}</div>
        </div>
      </main>
    )
  }

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
