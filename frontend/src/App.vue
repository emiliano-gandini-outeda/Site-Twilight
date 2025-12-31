<script setup>
import Header from "./components/Header.vue"
import Footer from "./components/Footer.vue"
</script>

<template>
  <div id="app">
    <Header />

    <main class="main-content">
      <router-view />
    </main>

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
  width: 100%;
  padding-top: 64px;
  overflow-x: visible !important;
}

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

#app {
  width: 100%;
  min-height: 100vh;
}

</style>