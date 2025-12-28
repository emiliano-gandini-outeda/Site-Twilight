import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  css: {
    transformer: "lightningcss",
    lightningcss: {
      drafts: {
        nesting: true,
      },
    },
  },
  build: {
    target: "es2020",
  },
})
