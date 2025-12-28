<script setup>
import { onMounted, ref } from "vue"

const message = ref("Loading...")

onMounted(() => {
  message.value = "Welcome to Site Twilight!"
})
</script>

<template>
  <div class="landing text-center mt-10">
    <h2 class="text-3xl font-bold mb-4">Landing Page</h2>
    <p class="text-lg">{{ message }}</p>
  </div>
</template>

<style scoped>
/* opcional */
</style>
