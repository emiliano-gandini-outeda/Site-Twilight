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
      <div class="content-wrapper">
        <router-view />
      </div>
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
  padding-bottom: 0;
  width: 100%;
  overflow-x: hidden; /* Previene scroll horizontal */
}

.content-wrapper {
  max-width: 100%;
  width: 100%;
  margin: 0 auto;
  padding: 1rem;
  box-sizing: border-box;
}
</style>

<style>
/* Estilos globales */
html, body {
  margin: 0;
  padding: 0;
  min-height: 100vh;
  background: #0a0a0a;
  overflow-x: hidden; /* Previene scroll horizontal global */
}

* {
  box-sizing: border-box;
}
</style>