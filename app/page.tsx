"use client"

import { useEffect, useState } from "react"

interface GeoData {
  ip: string
  country: string
  alias: string
}

export default function Page() {
  const [stage, setStage] = useState<1 | 2>(1)
  const [geoData, setGeoData] = useState<GeoData | null>(null)
  const [currentLine, setCurrentLine] = useState(0)
  const [typewriterText, setTypewriterText] = useState("")
  const [progress, setProgress] = useState(0)
  const [dots, setDots] = useState(".")
  const [spinner, setSpinner] = useState(0)

  const spinnerChars = ["|", "/", "-", "\\"]

  // Fetch IP and geo data
  useEffect(() => {
    async function fetchGeoData() {
      try {
        const response = await fetch("https://ipapi.co/json/")
        const data = await response.json()

        // Generate deterministic alias from IP
        const hash = Array.from(data.ip)
          .reduce((acc, char) => acc + char.charCodeAt(0), 0)
          .toString(36)
          .toUpperCase()
          .slice(0, 6)

        setGeoData({
          ip: data.ip || "███.███.███.██",
          country: data.country_name || "███████",
          alias: `SUBJECT-${hash}`,
        })
      } catch (error) {
        console.log("[v0] Failed to fetch geo data:", error)
        setGeoData({
          ip: "███.███.███.██",
          country: "███████",
          alias: "SUBJECT-UNKNOWN",
        })
      }
    }
    fetchGeoData()
  }, [])

  // Stage 1: Identity cycling with typewriter
  useEffect(() => {
    if (!geoData || stage !== 1) return

    const lines = [`ALIAS: ${geoData.alias}`, `COUNTRY: ${geoData.country}`, `IP: ${geoData.ip}`]

    if (currentLine >= lines.length) {
      // Transition to stage 2
      setTimeout(() => setStage(2), 500)
      return
    }

    const currentText = lines[currentLine]
    let charIndex = 0

    const typeInterval = setInterval(() => {
      if (charIndex <= currentText.length) {
        setTypewriterText(currentText.slice(0, charIndex))
        charIndex++
      } else {
        clearInterval(typeInterval)
        setTimeout(() => {
          setCurrentLine((prev) => prev + 1)
          setTypewriterText("")
        }, 1200)
      }
    }, 50)

    return () => clearInterval(typeInterval)
  }, [geoData, currentLine, stage])

  // Stage 2: Loading bar progression
  useEffect(() => {
    if (stage !== 2) return

    const progressInterval = setInterval(() => {
      setProgress((prev) => {
        if (prev >= 100) {
          clearInterval(progressInterval)
          return 100
        }
        return prev + 2
      })
    }, 50)

    return () => clearInterval(progressInterval)
  }, [stage])

  // Stage 2: Dots animation
  useEffect(() => {
    if (stage !== 2) return

    const dotsInterval = setInterval(() => {
      setDots((prev) => {
        if (prev === "...") return "."
        return prev + "."
      })
    }, 500)

    return () => clearInterval(dotsInterval)
  }, [stage])

  // Stage 2: Spinner animation
  useEffect(() => {
    if (stage !== 2) return

    const spinnerInterval = setInterval(() => {
      setSpinner((prev) => (prev + 1) % 4)
    }, 150)

    return () => clearInterval(spinnerInterval)
  }, [stage])

  if (!geoData) {
    return (
      <main className="min-h-screen bg-[#050505] flex items-center justify-center">
        <div className="text-[#00ff00] font-mono text-sm">
          <span className="animate-pulse">█</span>
        </div>
      </main>
    )
  }

  return (
    <main className="min-h-screen bg-[#050505] flex items-center justify-center p-4 relative overflow-hidden">
      {/* Scanline effect */}
      <div className="absolute inset-0 pointer-events-none opacity-10">
        <div className="h-full w-full bg-gradient-to-b from-transparent via-[#00ff00] to-transparent animate-scanline" />
      </div>

      {stage === 1 && (
        <div className="font-mono text-[#00ff00] text-lg md:text-xl tracking-wider">
          <div className="flex items-center gap-2">
            <span className="text-[#00ff00]/50">{">"}</span>
            <span>{typewriterText}</span>
            <span className="animate-pulse">█</span>
          </div>
        </div>
      )}

      {stage === 2 && (
        <div className="font-mono text-[#00ff00] space-y-8 text-center">
          {/* ASCII Spinner */}
          <div className="text-3xl md:text-4xl tracking-widest">{spinnerChars[spinner]}</div>

          {/* Loading Bar */}
          <div className="space-y-2">
            <div className="flex gap-0.5 justify-center">
              {Array.from({ length: 20 }).map((_, i) => (
                <span key={i} className="text-lg">
                  {i < Math.floor(progress / 5) ? "■" : "□"}
                </span>
              ))}
            </div>
            <div className="text-sm tracking-wider">{progress}%</div>
          </div>

          {/* Initializing text */}
          <div className="text-base md:text-lg tracking-wide">Initializing Database{dots}</div>
        </div>
      )}
    </main>
  )
}
