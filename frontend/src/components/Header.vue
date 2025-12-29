<template>
  <header class="site-header">
    <div class="header-background"></div>
    
    <nav class="nav-container">
      <!-- Mobile Menu Button -->
      <button class="mobile-menu-btn" @click="toggleMobileMenu" aria-label="Toggle menu">
        <div class="hamburger-icon" :class="{ 'open': mobileMenuOpen }">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </button>

      <div class="logo-section">
        <img src="/logo.png" alt="Site Twilight Logo" class="logo-img" />
        <a href="/" class="site-name">
          <span class="site-title">SITE TWILIGHT</span>
          <span class="site-subtitle">SECURED FACILITY</span>
        </a>
      </div>

      <!-- Mobile SSU Indicator -->
      <div class="mobile-ssu" :class="{'on': ssuStatus, 'off': !ssuStatus}" @click="toggleSSUInfo">
        <span class="ssu-label">SSU</span>
        <div class="ssu-light" :class="{'active': ssuStatus}"></div>
      </div>

      <!-- Desktop Navigation -->
      <div class="desktop-nav">
        <div class="ssu-indicator" :class="{'on': ssuStatus, 'off': !ssuStatus}">
          <span class="ssu-label">SSU</span>
          <span class="ssu-status">{{ ssuStatus ? 'ON' : 'OFF' }}</span>
          <div class="ssu-light" :class="{'active': ssuStatus}"></div>
        </div>

        <button class="nav-button" @click="openDiscord">
          <span class="button-icon">🎮</span>
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
          
          <div v-if="dropdownOpen" class="dropdown">
            <div class="dropdown-header">
              <div class="status-indicator" :class="{'online': user && user.is_authenticated, 'offline': !user || !user.is_authenticated}"></div>
              <span class="status-text">
                {{ user && user.is_authenticated ? 'SESSION ACTIVE' : 'SESSION INACTIVE' }}
              </span>
            </div>
            
            <div class="dropdown-divider"></div>
            
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

      <!-- Mobile Navigation Menu -->
      <div v-if="mobileMenuOpen" class="mobile-nav">
        <div class="mobile-nav-header">
          <div class="mobile-user-info">
            <span class="mobile-account-icon">👤</span>
            <div>
              <div class="mobile-account-name">
                <template v-if="user && user.is_authenticated">
                  {{ user.roblox_username }}
                </template>
                <template v-else>
                  GUEST USER
                </template>
              </div>
              <div class="mobile-account-status">
                {{ user && user.is_authenticated ? 'AUTHORIZED' : 'UNAUTHORIZED' }}
              </div>
            </div>
          </div>
          <div class="mobile-ssu-full" :class="{'on': ssuStatus, 'off': !ssuStatus}">
            <span class="ssu-label">SYSTEM STATUS UNIT</span>
            <span class="ssu-status">{{ ssuStatus ? 'ACTIVE' : 'INACTIVE' }}</span>
          </div>
        </div>

        <div class="mobile-nav-items">
          <button class="mobile-nav-item" @click="openDiscord">
            <span class="mobile-nav-icon">🎮</span>
            <span class="mobile-nav-text">Discord Server</span>
          </button>
          
          <button class="mobile-nav-item" @click="goToInfo">
            <span class="mobile-nav-icon">ℹ</span>
            <span class="mobile-nav-text">Site Information</span>
          </button>
          
          <button class="mobile-nav-item" @click="goToDashboard">
            <span class="mobile-nav-icon">📊</span>
            <span class="mobile-nav-text">Dashboard</span>
          </button>
          
          <div class="mobile-nav-divider"></div>
          
          <template v-if="user && user.is_authenticated">
            <a href="#" class="mobile-nav-item">
              <span class="mobile-nav-icon">⚙</span>
              <span class="mobile-nav-text">Settings</span>
            </a>
            <a href="#" class="mobile-nav-item">
              <span class="mobile-nav-icon">📁</span>
              <span class="mobile-nav-text">Profile</span>
            </a>
            <a href="/accounts/logout" class="mobile-nav-item logout">
              <span class="mobile-nav-icon">⎋</span>
              <span class="mobile-nav-text">Logout</span>
            </a>
          </template>
          <template v-else>
            <a href="/accounts/login/roblox" class="mobile-nav-item login">
              <span class="mobile-nav-icon">🔑</span>
              <span class="mobile-nav-text">Login with Roblox</span>
            </a>
          </template>
        </div>

        <div class="mobile-nav-footer">
          <button class="mobile-close-btn" @click="closeMobileMenu">
            <span class="close-icon">✕</span>
            <span class="close-text">CLOSE MENU</span>
          </button>
          <span class="mobile-footer-text">SITE TWILIGHT SECURED FACILITY</span>
        </div>
      </div>

      <!-- Mobile Menu Overlay -->
      <div v-if="mobileMenuOpen" class="mobile-overlay" @click="closeMobileMenu"></div>
    </nav>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const dropdownOpen = ref(false)
const mobileMenuOpen = ref(false)
const user = ref(null)
const ssuStatus = ref(false)

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
  closeMobileMenu()
}

const goToInfo = () => {
  console.log('Navigate to info')
  closeMobileMenu()
}

const goToDashboard = () => {
  router.push('/dashboard')
  closeMobileMenu()
}

const toggleSSUInfo = () => {
  console.log('SSU Status:', ssuStatus.value ? 'ON' : 'OFF')
}

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
  dropdownOpen.value = false
  updateBodyScroll()
}

const closeMobileMenu = () => {
  mobileMenuOpen.value = false
  updateBodyScroll()
}

const updateBodyScroll = () => {
  if (mobileMenuOpen.value) {
    document.body.style.overflow = 'hidden'
  } else {
    document.body.style.overflow = ''
  }
}

onMounted(() => {
  checkAuth()
  checkSSU()
  
  setInterval(checkSSU, 15000)
  
  router.afterEach(() => {
    checkAuth()
    closeMobileMenu()
  })
  
  document.addEventListener('click', handleClickOutside)
  document.addEventListener('keydown', handleEscapeKey)
})

const toggleDropdown = (event) => {
  event.stopPropagation()
  event.preventDefault()
  dropdownOpen.value = !dropdownOpen.value
  if (dropdownOpen.value) {
    closeMobileMenu()
  }
}

const handleClickOutside = (event) => {
  const userMenu = document.querySelector('.user-menu')
  const mobileMenuBtn = document.querySelector('.mobile-menu-btn')
  
  // Close dropdown if clicking outside
  if (userMenu && !userMenu.contains(event.target)) {
    dropdownOpen.value = false
  }
  
  // Close mobile menu if clicking outside (except mobile menu button)
  if (mobileMenuOpen.value && 
      !document.querySelector('.mobile-nav')?.contains(event.target) &&
      !mobileMenuBtn?.contains(event.target)) {
    closeMobileMenu()
  }
}

const handleEscapeKey = (event) => {
  if (event.key === 'Escape') {
    closeMobileMenu()
    dropdownOpen.value = false
  }
}

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
  document.removeEventListener('keydown', handleEscapeKey)
  document.body.style.overflow = ''
})
</script>

<style scoped>
/* Base mobile styles - mobile first */
.site-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background: rgba(10, 10, 10, 0.98);
  border-bottom: 1px solid #333;
  padding: 0.6rem 1rem;
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
    rgba(15, 15, 15, 0.98) 0%, 
    rgba(20, 20, 20, 0.98) 50%, 
    rgba(15, 15, 15, 0.98) 100%);
  z-index: -1;
}

.nav-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  gap: 0.5rem;
}

/* Mobile Menu Button */
.mobile-menu-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: rgba(30, 30, 30, 0.8);
  border: 1px solid #444;
  border-radius: 2px;
  cursor: pointer;
  padding: 0;
  z-index: 1002;
  transition: all 0.3s ease;
}

.mobile-menu-btn:hover {
  background: rgba(40, 40, 40, 0.9);
  border-color: #666;
}

.hamburger-icon {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 20px;
  height: 14px;
  position: relative;
}

.hamburger-icon span {
  display: block;
  width: 100%;
  height: 2px;
  background: #d8d8d8;
  border-radius: 1px;
  transition: all 0.3s ease;
}

.hamburger-icon.open span:nth-child(1) {
  transform: rotate(45deg) translate(5px, 5px);
}

.hamburger-icon.open span:nth-child(2) {
  opacity: 0;
  transform: translateX(-10px);
}

.hamburger-icon.open span:nth-child(3) {
  transform: rotate(-45deg) translate(5px, -5px);
}

/* Logo Section */
.logo-section {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  text-decoration: none;
  flex: 1;
}

.logo-img {
  height: 32px;
  width: 32px;
  object-fit: contain;
  filter: grayscale(0.3) brightness(1.2);
}

.site-name {
  display: flex;
  flex-direction: column;
  text-decoration: none;
}

.site-title {
  font-size: 0.9rem;
  font-weight: 700;
  letter-spacing: 1px;
  color: #fff;
  text-transform: uppercase;
  line-height: 1.2;
}

.site-subtitle {
  font-size: 0.6rem;
  letter-spacing: 0.5px;
  color: #888;
  text-transform: uppercase;
}

/* Mobile SSU Indicator */
.mobile-ssu {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.4rem 0.6rem;
  background: rgba(30, 30, 30, 0.8);
  border: 1px solid #444;
  border-radius: 2px;
  font-family: 'Consolas', monospace;
  z-index: 1001;
  transition: all 0.3s ease;
  cursor: pointer;
}

.mobile-ssu:hover {
  background: rgba(35, 35, 35, 0.9);
}

.mobile-ssu.on {
  border-color: #00aa00;
  background: rgba(0, 40, 0, 0.3);
}

.mobile-ssu.off {
  border-color: #aa0000;
  background: rgba(40, 0, 0, 0.3);
}

.ssu-label {
  font-size: 0.75rem;
  font-weight: bold;
  color: #aaa;
  letter-spacing: 0.5px;
}

.ssu-light {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #333;
  transition: all 0.3s ease;
}

.ssu-light.active {
  background: #00ff00;
  box-shadow: 0 0 6px #00ff00;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { opacity: 0.6; }
  50% { opacity: 1; }
  100% { opacity: 0.6; }
}

/* Desktop Navigation - Hidden on mobile */
.desktop-nav {
  display: none;
}

/* Mobile Navigation Menu */
.mobile-nav {
  position: fixed;
  top: 0;
  left: 0;
  width: 85%;
  max-width: 320px;
  height: 100vh;
  background: rgba(15, 15, 15, 0.98);
  border-right: 1px solid #333;
  z-index: 1003;
  display: flex;
  flex-direction: column;
  backdrop-filter: blur(20px);
  animation: slideIn 0.3s ease forwards;
  overflow-x: hidden;
}

@keyframes slideIn {
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0);
  }
}

.mobile-nav-header {
  padding: 1.5rem 1rem;
  background: rgba(25, 25, 25, 0.8);
  border-bottom: 1px solid #333;
}

.mobile-user-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.mobile-account-icon {
  font-size: 1.5rem;
  color: #aaa;
}

.mobile-account-name {
  font-size: 1rem;
  font-weight: 500;
  color: #fff;
  margin-bottom: 0.2rem;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  max-width: 180px;
}

.mobile-account-status {
  font-size: 0.7rem;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.mobile-ssu-full {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.6rem 0.8rem;
  background: rgba(30, 30, 30, 0.8);
  border: 1px solid #444;
  border-radius: 2px;
}

.mobile-ssu-full.on {
  border-color: #00aa00;
  background: rgba(0, 40, 0, 0.3);
}

.mobile-ssu-full.off {
  border-color: #aa0000;
  background: rgba(40, 0, 0, 0.3);
}

.mobile-ssu-full .ssu-label {
  font-size: 0.8rem;
}

.mobile-ssu-full .ssu-status {
  font-size: 0.8rem;
  font-weight: bold;
  letter-spacing: 0.5px;
  color: #00ff00;
}

.mobile-ssu-full.off .ssu-status {
  color: #ff0000;
}

.mobile-nav-items {
  flex: 1;
  overflow-y: auto;
  padding: 1rem 0;
  overflow-x: hidden;
}

.mobile-nav-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  width: 100%;
  padding: 1rem 1.2rem;
  background: transparent;
  border: none;
  color: #d8d8d8;
  text-align: left;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.2s ease;
  border-left: 3px solid transparent;
}

.mobile-nav-item:hover {
  background: rgba(40, 40, 40, 0.6);
  border-left-color: #666;
}

.mobile-nav-item.login:hover {
  border-left-color: #00cc00;
}

.mobile-nav-item.logout:hover {
  border-left-color: #cc0000;
}

.mobile-nav-icon {
  font-size: 1.1rem;
  opacity: 0.9;
  width: 24px;
  text-align: center;
}

.mobile-nav-text {
  font-size: 0.95rem;
  font-weight: 500;
  flex: 1;
}

.mobile-nav-divider {
  height: 1px;
  background: linear-gradient(90deg, transparent, #444, transparent);
  margin: 0.8rem 1.2rem;
}

.mobile-nav-footer {
  padding: 1rem;
  background: rgba(20, 20, 20, 0.9);
  border-top: 1px solid #333;
  text-align: center;
}

.mobile-close-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  width: 100%;
  padding: 0.8rem;
  background: rgba(40, 40, 40, 0.8);
  border: 1px solid #555;
  color: #d8d8d8;
  border-radius: 2px;
  cursor: pointer;
  margin-bottom: 1rem;
  transition: all 0.3s ease;
  font-family: inherit;
  font-size: 0.9rem;
}

.mobile-close-btn:hover {
  background: rgba(50, 50, 50, 0.9);
  border-color: #666;
}

.close-icon {
  font-size: 1.2rem;
  font-weight: normal;
  line-height: 1;
}

.close-text {
  font-weight: 500;
  letter-spacing: 0.5px;
}

.mobile-footer-text {
  font-size: 0.7rem;
  color: #777;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

/* Mobile Overlay */
.mobile-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  z-index: 1002;
  backdrop-filter: blur(5px);
  animation: fadeIn 0.3s ease forwards;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* Tablet styles */
@media (min-width: 640px) {
  .site-header {
    padding: 0.8rem 1.5rem;
  }
  
  .logo-section {
    gap: 1rem;
  }
  
  .logo-img {
    height: 36px;
    width: 36px;
  }
  
  .site-title {
    font-size: 1rem;
  }
  
  .mobile-ssu {
    padding: 0.5rem 0.8rem;
  }
  
  .mobile-nav {
    width: 70%;
    max-width: 380px;
  }
}

/* Desktop styles */
@media (min-width: 1024px) {
  .site-header {
    padding: 0.8rem 2rem;
  }
  
  .mobile-menu-btn,
  .mobile-ssu,
  .mobile-nav,
  .mobile-overlay {
    display: none !important;
  }
  
  .desktop-nav {
    display: flex !important;
    align-items: center;
    gap: 1rem;
  }
  
  .logo-section {
    flex: 0 1 auto;
  }
  
  .logo-img {
    height: 40px;
    width: 40px;
  }
  
  .site-title {
    font-size: 1.2rem;
  }
  
  .site-subtitle {
    font-size: 0.7rem;
  }
  
  /* Desktop SSU Indicator */
  .ssu-indicator {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 0.8rem;
    background: rgba(30, 30, 30, 0.8);
    border: 1px solid #444;
    border-radius: 2px;
    font-family: 'Consolas', monospace;
    transition: all 0.3s ease;
  }
  
  .ssu-indicator:hover {
    background: rgba(35, 35, 35, 0.9);
  }
  
  .ssu-indicator.on {
    border-color: #00aa00;
    background: rgba(0, 40, 0, 0.3);
  }
  
  .ssu-indicator.off {
    border-color: #aa0000;
    background: rgba(40, 0, 0, 0.3);
  }
  
  .ssu-status {
    font-size: 0.8rem;
    font-weight: bold;
    letter-spacing: 0.5px;
  }
  
  .ssu-indicator.on .ssu-status {
    color: #00ff00;
    text-shadow: 0 0 5px #00ff00;
  }
  
  .ssu-indicator.off .ssu-status {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000;
  }
  
  /* Desktop Navigation Buttons */
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
  
  /* Desktop User Menu */
  .user-menu {
    position: relative;
    cursor: pointer;
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
    min-width: 160px;
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
    max-width: 120px;
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
}
</style>