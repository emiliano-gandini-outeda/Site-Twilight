<script setup>
import { ref, onMounted } from "vue"
import Header from "./components/Header.vue"

// No necesitamos ssuStatus aquí ya que ahora está en Header
</script>

<template>
  <div id="app" class="flex flex-col min-h-screen">
    <!-- HEADER FIXED - El header ahora es fixed y cubre todo el ancho -->
    <Header />

    <!-- MAIN CONTENT - Se ajusta automáticamente debajo del header -->
    <main class="flex-1 overflow-auto pt-16"> <!-- pt-16 para dejar espacio para el header -->
      <router-view />
    </main>

    <!-- FOOTER FIXED -->
    <footer class="bg-gray-900 text-white p-4 text-center z-40 shadow-inner">
      <div class="max-w-7xl mx-auto">
        <span class="text-sm opacity-80">&copy; 2025 Site Twilight. All rights reserved.</span>
        <span class="text-xs opacity-60 ml-4">CLASSIFIED SYSTEM</span>
      </div>
    </footer>
  </div>
</template>

<style scoped>

main {
  /* El padding-top se maneja con la clase pt-16 de Tailwind */
  padding-bottom: 0;
}

#app {
  background: #0a0a0a;
  color: #d8d8d8;
}

footer {
  background: rgba(15, 15, 15, 0.95);
  border-top: 1px solid #333;
  backdrop-filter: blur(10px);
}
</style>