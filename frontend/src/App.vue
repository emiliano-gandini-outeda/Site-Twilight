<script setup>
import { ref, onMounted } from "vue"
import Header from "./components/Header.vue"
const ssuStatus = ref(false)

async function fetchSSU() {
  const res = await fetch("/api/ssu/", { credentials: "include" })
  const data = await res.json()
  ssuStatus.value = data.ssu_status
}

onMounted(() => {
  fetchSSU()
})
</script>

<template>
  <div id="app" class="flex flex-col h-screen">
    <!-- HEADER FIXED -->
      <Header />

    <!-- MAIN CONTENT -->
    <main class="flex-1 pt-4 pb-4 overflow-auto">
      <router-view /> 
    </main>

    <!-- FOOTER FIXED -->
    <footer class="bg-gray-900 text-white p-4 text-center fixed bottom-0 left-0 right-0 z-50 shadow-inner">
      &copy; 2025 Site Twilight. All rights reserved.
    </footer>
  </div>
</template>

<style scoped>
/* Opcional: aseguramos que el contenido no quede oculto detrás de header/footer */
main {
  padding-top: 64px; /* igual a la altura del header */
  padding-bottom: 64px; /* igual a la altura del footer */
}
</style>
