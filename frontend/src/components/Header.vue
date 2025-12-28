<template>
  <header class="site-header">
    <nav class="nav-container">
      <div class="logo">
        <a href="/">Site Twilight</a>
      </div>

      <div class="nav-links">
        <a href="/">Home</a>
        <a href="/terms-of-service">Terms</a>

        <div class="user-menu" @click="toggleDropdown">
          <!-- Always show "Account" when not logged in -->
          <span v-if="user && user.is_authenticated">
            {{ user.roblox_username }}
          </span>
          <span v-else>Account</span>
          
          <div v-show="dropdownOpen" class="dropdown">
            <!-- Show menu for authenticated users -->
            <template v-if="user && user.is_authenticated">
              <a href="#">Placeholder</a>
              <a href="#">Placeholder</a>
              <a href="/accounts/logout">Logout</a>
            </template>
            <!-- Show login/signup for non-authenticated users -->
            <template v-else>
              <a href="/accounts/login/roblox">Login / Signup</a>
            </template>
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const dropdownOpen = ref(false)
const user = ref(null)

// Check authentication status
const checkAuth = async () => {
  try {
    const response = await fetch('/api/auth/user/')
    if (response.ok) {
      const data = await response.json()
      user.value = data
    } else {
      // If response is not OK, set user to null/not authenticated
      user.value = { is_authenticated: false }
    }
  } catch (error) {
    console.error('Auth check failed:', error)
    // On error, assume not authenticated
    user.value = { is_authenticated: false }
  }
}

onMounted(() => {
  checkAuth()
  
  // Check auth on route changes
  router.afterEach(() => {
    checkAuth()
  })
  
  document.addEventListener('click', handleClickOutside)
})

// Toggle menu
const toggleDropdown = () => {
  dropdownOpen.value = !dropdownOpen.value
}

// Close dropdown when clicking outside
const handleClickOutside = (event) => {
  const userMenu = document.querySelector('.user-menu')
  if (userMenu && !userMenu.contains(event.target)) {
    dropdownOpen.value = false
  }
}
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
  z-index: 1000; /* Ensure dropdown is above other elements */
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