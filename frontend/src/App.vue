<script setup>
import Header from "./components/Header.vue"
import Footer from "./components/Footer.vue"
</script>

<template>
  <div id="app">
    <!-- HEADER FIXED -->
    <Header />

    <!-- MAIN CONTENT -->
    <main class="main-content">
      <!-- REMOVEMOS el content-wrapper y dejamos router-view directamente -->
      <router-view />
    </main>

    <!-- FOOTER -->
    <Footer />
  </div>
</template>

<style scoped>
#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: #0a0a0a;
  color: #d8d8d8;
  position: relative;
}

.main-content {
  flex: 1;
  padding-top: 64px; /* Espacio para header fixed */
  width: 100%;
  overflow-x: hidden; /* Previene scroll horizontal */
}
</style>

<style>
/* Estilos globales */
html, body {
  margin: 0;
  padding: 0;
  min-height: 100vh;
  background: #0a0a0a;
  overflow-x: hidden;
}

* {
  box-sizing: border-box;
}
</style>