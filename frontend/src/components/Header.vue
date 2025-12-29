<template>
  <header class="site-header">
    <div class="header-background"></div>
    
    <nav class="nav-container">
      <div class="logo-section">
        <img src="/logo.png" alt="Site Twilight Logo" class="logo-img" />
        <a href="/" class="site-name">
          <span class="site-title">SITE TWILIGHT</span>
          <span class="site-subtitle">SECURED FACILITY</span>
        </a>
        
        <!-- SSU Status Indicator -->
        <div class="ssu-indicator" :class="{'on': ssuStatus, 'off': !ssuStatus}">
          <span class="ssu-label">SSU</span>
          <span class="ssu-status">{{ ssuStatus ? 'ON' : 'OFF' }}</span>
          <div class="ssu-light" :class="{'active': ssuStatus}"></div>
        </div>
      </div>

      <div class="nav-links">
        <button class="nav-button" @click="openDiscord">
          <span class="button-icon">#</span>
          <span class="button-text">Discord</span>
        </button>
        
        <button class="nav-button secondary" @click="goToInfo">
          <span class="button-icon">ℹ</span>
          <span class="button-text">Info</span>
        </button>
        
        <button class="nav-button secondary" @click="goToDashboard">
          <span class="button-icon">📊</span>
          <span class="button-text">Dashboard</span>
        </button>

        <div class="user-menu" @click="toggleDropdown">
          <div class="account-display">
            <span class="account-icon">👤</span>
            <span class="account-text">
              <template v-if="user && user.is_authenticated">
                {{ user.roblox_username }}
              </template>
              <template v-else>
                ACCOUNT
              </template>
            </span>
            <span class="dropdown-arrow">▼</span>
          </div>
          
          <div v-show="dropdownOpen" class="dropdown">
            <div class="dropdown-header">
              <div class="status-indicator" :class="{'online': user && user.is_authenticated, 'offline': !user || !user.is_authenticated}"></div>
              <span class="status-text">
                {{ user && user.is_authenticated ? 'SESSION ACTIVE' : 'SESSION INACTIVE' }}
              </span>
            </div>
            
            <div class="dropdown-divider"></div>
            
            <!-- Show menu for authenticated users -->
            <template v-if="user && user.is_authenticated">
              <a href="#" class="dropdown-item">
                <span class="item-icon">⚙</span>
                <span class="item-text">Settings</span>
              </a>
              <a href="#" class="dropdown-item">
                <span class="item-icon">📁</span>
                <span class="item-text">Profile</span>
              </a>
              <a href="/accounts/logout" class="dropdown-item logout">
                <span class="item-icon">⎋</span>
                <span class="item-text">Logout</span>
              </a>
            </template>
            <!-- Show login/signup for non-authenticated users -->
            <template v-else>
              <a href="/accounts/login/roblox" class="dropdown-item login">
                <span class="item-icon">🔑</span>
                <span class="item-text">Login / Signup</span>
              </a>
            </template>
            
            <div class="dropdown-footer">
              <span class="footer-text">ACCESS LEVEL: {{ user && user.is_authenticated ? 'AUTHORIZED' : 'GUEST' }}</span>
            </div>
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
const ssuStatus = ref(false) // Add SSU status

// Check authentication status
const checkAuth = async () => {
  try {
    const response = await fetch('/api/auth/user/')
    if (response.ok) {
      const data = await response.json()
      user.value = data
    } else {
      user.value = { is_authenticated: false }
    }
  } catch (error) {
    console.error('Auth check failed:', error)
    user.value = { is_authenticated: false }
  }
}

// Check SSU status
const checkSSU = async () => {
  try {
    const response = await fetch('/api/ssu/')
    if (response.ok) {
      const data = await response.json()
      ssuStatus.value = data.ssu_status
    }
  } catch (error) {
    console.error('SSU check failed:', error)
  }
}

const openDiscord = () => {
  window.open('https://discord.com/invite/37BrVa6b8E', '_blank')
}

const goToInfo = () => {
  // Navigate to info page or implement info modal
  console.log('Navigate to info')
}

const goToDashboard = () => {
  router.push('/dashboard')
}

onMounted(() => {
  checkAuth()
  checkSSU()
  
  // Check every 15 seconds for SSU status updates
  setInterval(checkSSU, 15000)
  
  router.afterEach(() => {
    checkAuth()
  })
  
  document.addEventListener('click', handleClickOutside)
})

const toggleDropdown = (event) => {
  event.stopPropagation()
  dropdownOpen.value = !dropdownOpen.value
}

const handleClickOutside = (event) => {
  const userMenu = document.querySelector('.user-menu')
  if (userMenu && !userMenu.contains(event.target)) {
    dropdownOpen.value = false
  }
}
</script>

<style scoped>
.site-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background: rgba(10, 10, 10, 0.98);
  border-bottom: 1px solid #333;
  padding: 0.8rem 2rem;
  z-index: 1000;
  backdrop-filter: blur(10px);
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.5);
}

.header-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, 
    rgba(15, 15, 15, 0.95) 0%, 
    rgba(20, 20, 20, 0.95) 50%, 
    rgba(15, 15, 15, 0.95) 100%);
  z-index: -1;
}

.nav-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 100%;
  margin: 0 auto;
  position: relative;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  text-decoration: none;
}

.logo-img {
  height: 40px;
  width: 40px;
  object-fit: contain;
  filter: grayscale(0.3) brightness(1.2);
  transition: filter 0.3s ease;
}

.logo-section:hover .logo-img {
  filter: grayscale(0) brightness(1.5);
}

.site-name {
  display: flex;
  flex-direction: column;
  text-decoration: none;
}

.site-title {
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: 2px;
  color: #fff;
  text-transform: uppercase;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
}

.site-subtitle {
  font-size: 0.7rem;
  letter-spacing: 1px;
  color: #888;
  text-transform: uppercase;
  margin-top: 2px;
}

/* SSU Indicator Styles */
.ssu-indicator {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0.8rem;
  background: rgba(30, 30, 30, 0.8);
  border: 1px solid #444;
  border-radius: 2px;
  font-family: 'Consolas', monospace;
  margin-left: 1rem;
  position: relative;
  transition: all 0.3s ease;
}

.ssu-indicator.on {
  border-color: #00aa00;
  background: rgba(0, 40, 0, 0.3);
}

.ssu-indicator.off {
  border-color: #aa0000;
  background: rgba(40, 0, 0, 0.3);
}

.ssu-label {
  font-size: 0.8rem;
  font-weight: bold;
  color: #aaa;
  letter-spacing: 1px;
}

.ssu-status {
  font-size: 0.8rem;
  font-weight: bold;
  letter-spacing: 1px;
}

.ssu-indicator.on .ssu-status {
  color: #00ff00;
  text-shadow: 0 0 5px #00ff00;
}

.ssu-indicator.off .ssu-status {
  color: #ff0000;
  text-shadow: 0 0 5px #ff0000;
}

.ssu-light {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #333;
  transition: all 0.3s ease;
}

.ssu-light.active {
  background: #00ff00;
  box-shadow: 0 0 8px #00ff00;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { opacity: 0.6; }
  50% { opacity: 1; }
  100% { opacity: 0.6; }
}

.nav-links {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.nav-button {
  padding: 0.6rem 1.2rem;
  background: rgba(30, 30, 30, 0.9);
  border: 1px solid #444;
  color: #d8d8d8;
  font-family: inherit;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  border-radius: 2px;
  letter-spacing: 0.5px;
}

.nav-button:hover {
  background: rgba(40, 40, 40, 0.95);
  border-color: #666;
  transform: translateY(-1px);
}

.nav-button.secondary {
  background: rgba(35, 35, 35, 0.8);
  border-color: #555;
}

.button-icon {
  font-size: 1rem;
  opacity: 0.9;
}

.button-text {
  font-weight: 500;
}

.user-menu {
  position: relative;
  cursor: pointer;
  margin-left: 0.5rem;
}

.account-display {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 0.7rem 1rem;
  background: rgba(25, 25, 25, 0.9);
  border: 1px solid #444;
  border-radius: 2px;
  transition: all 0.3s ease;
  min-width: 180px;
}

.account-display:hover {
  background: rgba(35, 35, 35, 0.95);
  border-color: #666;
}

.account-icon {
  font-size: 1.1rem;
  color: #aaa;
}

.account-text {
  color: #d8d8d8;
  font-size: 0.9rem;
  font-weight: 500;
  letter-spacing: 0.5px;
  flex: 1;
  text-transform: uppercase;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  max-width: 100px;
}

.dropdown-arrow {
  color: #666;
  font-size: 0.7rem;
  transition: transform 0.3s ease;
}

.user-menu:hover .dropdown-arrow {
  transform: rotate(180deg);
}

.dropdown {
  position: absolute;
  right: 0;
  top: calc(100% + 5px);
  background: rgba(20, 20, 20, 0.98);
  border: 1px solid #444;
  border-radius: 2px;
  min-width: 220px;
  z-index: 1001;
  backdrop-filter: blur(20px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  border-top: 1px solid #555;
}

.dropdown-header {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 1rem;
  background: rgba(30, 30, 30, 0.6);
  border-bottom: 1px solid #333;
}

.status-indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.status-indicator.online {
  background: #00cc00;
  box-shadow: 0 0 8px #00cc00;
}

.status-indicator.offline {
  background: #cc0000;
  box-shadow: 0 0 8px #cc0000;
}

.status-text {
  font-size: 0.75rem;
  color: #aaa;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

.dropdown-divider {
  height: 1px;
  background: linear-gradient(90deg, transparent, #444, transparent);
  margin: 0.5rem 0;
}

.dropdown-item {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 0.8rem 1rem;
  color: #d8d8d8;
  text-decoration: none;
  transition: all 0.3s ease;
  border-left: 2px solid transparent;
}

.dropdown-item:hover {
  background: rgba(40, 40, 40, 0.7);
  border-left-color: #666;
}

.dropdown-item.logout:hover {
  border-left-color: #cc0000;
  color: #ff6666;
}

.dropdown-item.login:hover {
  border-left-color: #00cc00;
  color: #66ff66;
}

.item-icon {
  font-size: 0.9rem;
  opacity: 0.8;
  width: 20px;
  text-align: center;
}

.item-text {
  font-size: 0.9rem;
  flex: 1;
}

.dropdown-footer {
  padding: 0.8rem 1rem;
  background: rgba(15, 15, 15, 0.8);
  border-top: 1px solid #333;
  margin-top: 0.5rem;
}

.footer-text {
  font-size: 0.7rem;
  color: #777;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  text-align: center;
  display: block;
}

@media (max-width: 1024px) {
  .nav-container {
    flex-wrap: wrap;
    gap: 1rem;
  }
  
  .logo-section {
    order: 1;
    flex: 1;
  }
  
  .nav-links {
    order: 2;
    width: 100%;
    justify-content: center;
  }
  
  .ssu-indicator {
    margin-left: auto;
  }
}

@media (max-width: 768px) {
  .site-header {
    padding: 0.8rem 1rem;
  }
  
  .logo-section {
    gap: 1rem;
  }
  
  .ssu-indicator {
    padding: 0.4rem 0.6rem;
    margin-left: 0.5rem;
  }
  
  .nav-links {
    gap: 0.5rem;
    flex-wrap: wrap;
  }
  
  .nav-button {
    padding: 0.5rem 0.8rem;
    font-size: 0.85rem;
  }
  
  .account-display {
    min-width: auto;
    padding: 0.6rem 0.8rem;
  }
  
  .account-text {
    max-width: 80px;
  }
  
  .dropdown {
    position: fixed;
    top: 100px;
    left: 50%;
    transform: translateX(-50%);
    width: 90%;
    max-width: 300px;
  }
}

@media (max-width: 480px) {
  .logo-section {
    flex-wrap: wrap;
    gap: 0.5rem;
  }
  
  .ssu-indicator {
    margin-left: 0;
    margin-top: 0.5rem;
    order: 3;
    width: 100%;
    justify-content: center;
  }
  
  .nav-links {
    order: 2;
  }
}
</style>