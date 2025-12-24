import type React from "react"
import type { Metadata } from "next"
import { Inter } from "next/font/google"
import localFont from "next/font/local"
import "./globals.css"

const inter = Inter({ subsets: ["latin"] })
const azonix = localFont({
  src: [
    {
      path: "/fonts/Azonix.woff2",
      weight: "400",
      style: "normal",
    },
  ],
  variable: "--font-azonix",
})

export const metadata: Metadata = {
  title: "Site Twilight - SCP Foundation",
  description: "Secure, Contain, Protect",
  generator: "Site Twilight",
  icons: {
    icon: [
      {
        url: "/scp-logo.png",
        media: "(prefers-color-scheme: light)",
      },
      {
        url: "/scp-logo.png",
        media: "(prefers-color-scheme: dark)",
      },
      {
        url: "/scp-logo.png",
        type: "image/svg+xml",
      },
    ],
    apple: "/scp-logo.png",
  },
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en" className="dark">
      <body className={`${inter.className} ${azonix.variable} antialiased`}>{children}</body>
    </html>
  )
}
