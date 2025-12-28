<template>
  <header class="site-header">
    <nav class="nav-container">
      <div class="logo">
        <a href="/">Site Twilight</a>
      </div>

      <div class="nav-links">
        <a href="/">Home</a>
        <a href="/terms">Terms</a>

        <div class="user-menu" @click="toggleDropdown">
          <span v-if="user">{{ user.roblox_username }}</span>
          <span v-else>Account</span>
          <div v-show="dropdownOpen" class="dropdown">
            <template v-if="user">
              <a href="#">Placeholder</a>
              <a href="#">Placeholder</a>
              <a href="/accounts/logout">Logout</a>
            </template>
            <template v-else>
              <a href="/accounts/login">Login</a>
              <a href="/accounts/signup">Signup</a>
            </template>
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { ref } from 'vue'

const dropdownOpen = ref(false)
const user = ref(null)

// Toggle menu
const toggleDropdown = () => {
  dropdownOpen.value = !dropdownOpen.value
}

// In production, fetch user info from Django API
// Example: user.value = { roblox_username: 'Emiliano' }
</script>

<style scoped>
.site-header {
  background-color: #111;
  color: #fff;
  padding: 1rem 2rem;
}

.nav-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-links {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.user-menu {
  position: relative;
  cursor: pointer;
}

.dropdown {
  position: absolute;
  right: 0;
  top: 120%;
  background: #222;
  border: 1px solid #444;
  border-radius: 4px;
  display: flex;
  flex-direction: column;
  min-width: 150px;
  padding: 0.5rem 0;
}

.dropdown a {
  color: #fff;
  text-decoration: none;
  padding: 0.5rem 1rem;
}

.dropdown a:hover {
  background: #333;
}
</style>
