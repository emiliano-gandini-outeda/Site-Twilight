<template>
  <div class="dashboard-page">
    <!-- Overlay para móviles -->
    <div v-if="isMobile" class="mobile-overlay">
      <div class="mobile-overlay-content">
        <div class="mobile-warning-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fc6f03" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="12" y1="8" x2="12" y2="12"></line>
            <line x1="12" y1="16" x2="12.01" y2="16"></line>
          </svg>
        </div>
        <h2 class="mobile-warning-title">ACCESO RESTRINGIDO</h2>
        <div class="mobile-warning-subtitle">SISTEMA DE CONTROL DE SITIO</div>
        <div class="mobile-warning-message">
          Este Dashboard no es accesible desde plataformas móviles.<br>
          Por favor, utilice un dispositivo de escritorio para acceder al sistema.
        </div>
        <div class="mobile-warning-info">
          <div class="warning-info-item">
            <span class="info-label">RAZÓN:</span>
            <span class="info-value">INTERFAZ CRÍTICA DE CONTROL</span>
          </div>
          <div class="warning-info-item">
            <span class="info-label">NIVEL DE SEGURIDAD:</span>
            <span class="info-value">CLASE 3</span>
          </div>
          <div class="warning-info-item">
            <span class="info-label">ACCESO PERMITIDO:</span>
            <span class="info-value">SOLO ESCRITORIO</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Contenido Desktop -->
    <template v-else>
      <!-- Fondo SCP -->
      <div class="site-background">
        <div class="grid-overlay"></div>
        <div class="scan-line"></div>
        <div class="particles"></div>
      </div>

      <!-- Contenido Principal -->
      <main class="dashboard-content">
        <!-- Sidebar de Navegación -->
        <nav class="dashboard-sidebar">
          <div class="sidebar-header">
            <h3 class="sidebar-title">CONTROL PANEL</h3>
            <div class="sidebar-subtitle">Authorized Tools</div>
          </div>
          
          <div class="sidebar-tools">
            <!-- Herramientas Disponibles -->
            <div class="tool-category">
              <div class="category-header">
                <span class="category-title">PERSONNEL MANAGEMENT</span>
                <div class="category-indicator"></div>
              </div>
              
              <div class="tool-list">
                <!-- Tool activo -->
                <button 
                  class="tool-item" 
                  :class="{ 'active': activeTool === 'characters' }"
                  @click="setActiveTool('characters')"
                >
                  <div class="tool-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                      <circle cx="12" cy="7" r="4"></circle>
                    </svg>
                  </div>
                  <span class="tool-name">Personajes</span>
                  <div class="tool-indicator" v-if="activeTool === 'characters'">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <polyline points="9 18 15 12 9 6"></polyline>
                    </svg>
                  </div>
                </button>
                
                <button 
                  class="tool-item" 
                  :class="{ 'active': activeTool === 'user' }"
                  @click="setActiveTool('user')"
                >
                  <div class="tool-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path>
                      <circle cx="12" cy="7" r="4"></circle>
                    </svg>
                  </div>
                  <span class="tool-name">Mi Usuario</span>
                  <div class="tool-indicator" v-if="activeTool === 'user'">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <polyline points="9 18 15 12 9 6"></polyline>
                    </svg>
                  </div>
                </button>
              </div>
            </div>
            
            <!-- Placeholders [REDACTED] -->
            <div class="tool-category">
              <div class="category-header">
                <span class="category-title">CLASSIFIED TOOLS</span>
                <div class="category-indicator classified"></div>
              </div>
              
              <div class="tool-list">
                <!-- 6 placeholders [REDACTED] -->
                <div class="tool-item redacted" v-for="n in 6" :key="n">
                  <div class="tool-icon redacted">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                      <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                    </svg>
                  </div>
                  <span class="tool-name redacted-text">[REDACTED]</span>
                  <div class="clearance-warning">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <circle cx="12" cy="12" r="10"></circle>
                      <line x1="12" y1="8" x2="12" y2="12"></line>
                      <line x1="12" y1="16" x2="12.01" y2="16"></line>
                    </svg>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <div class="sidebar-footer">
            <div class="system-status">
              <div class="status-item">
                <span class="status-label">USER:</span>
                <span class="status-value authorized">{{ currentUser?.roblox_username || 'GUEST' }}</span>
              </div>
              <div class="status-item">
                <span class="status-label">CLEARANCE:</span>
                <span class="status-value">LEVEL {{ clearanceLevel }}</span>
              </div>
              <div class="status-item">
                <span class="status-label">SYSTEM:</span>
                <span class="status-value">OPERATIONAL</span>
              </div>
            </div>
          </div>
        </nav>

        <!-- Área de Contenido Principal -->
        <section class="dashboard-main">
          <div class="main-header">
            <div class="header-left">
              <h2 class="main-title">{{ getActiveToolTitle() }}</h2>
              <div class="main-subtitle">
                <span v-if="activeTool === 'characters'">Manage and view your authorized personnel files</span>
                <span v-else-if="activeTool === 'user'">View and manage your user profile and settings</span>
                <span v-else>[CLASSIFIED CONTENT]</span>
              </div>
            </div>
            
            <div class="header-right">
              <div class="session-info">
                <div class="session-indicator active"></div>
                <span class="session-text">SESSION ACTIVE</span>
              </div>
              <div class="timestamp">
                {{ currentTime }}
              </div>
            </div>
          </div>
          
          <!-- Componente dinámico -->
          <div class="component-container">
            <div v-if="activeTool === 'characters'">
              <Personajes :current-user="currentUser" />
            </div>
            
            <div v-else-if="activeTool === 'user'" class="component-placeholder">
              <div class="placeholder-content">
                <div class="placeholder-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="#fc6f03" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path>
                    <circle cx="12" cy="7" r="4"></circle>
                  </svg>
                </div>
                <h3 class="placeholder-title">USER PROFILE</h3>
                <p class="placeholder-text">User management system is loading...</p>
                <div class="placeholder-action">
                  <button class="action-button" @click="loadUserProfile">
                    <span class="button-text">ACCESS PROFILE</span>
                    <div class="button-indicator">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <polyline points="9 18 15 12 9 6"></polyline>
                      </svg>
                    </div>
                  </button>
                </div>
              </div>
            </div>
            
            <div v-else class="component-placeholder classified">
              <div class="placeholder-content">
                <div class="placeholder-icon redacted">
                  <svg viewBox="0 0 24 24" fill="none" stroke="#aa2222" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                    <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                  </svg>
                </div>
                <h3 class="placeholder-title redacted-text">[ACCESS DENIED]</h3>
                <p class="placeholder-text">Insufficient clearance level for this tool. Required: Level 4 or higher.</p>
                <div class="clearance-required">
                  <span class="clearance-label">REQUIRED CLEARANCE:</span>
                  <span class="clearance-value">LEVEL 4+</span>
                </div>
              </div>
            </div>
          </div>
          
          <div class="main-footer">
            <div class="footer-info">
              <span class="info-label">SYSTEM:</span>
              <span class="info-value">TWILIGHT-DASHBOARD v1.0.3</span>
            </div>
            <div class="footer-info">
              <span class="info-label">LAST UPDATE:</span>
              <span class="info-value">{{ currentTime }}</span>
            </div>
            <div class="footer-info">
              <span class="info-label">ACCESS LEVEL:</span>
              <span class="info-value">{{ currentUser?.is_authenticated ? 'AUTHORIZED' : 'GUEST' }}</span>
            </div>
          </div>
        </section>
      </main>
    </template>
  </div>
</template>

<script setup>
import Personajes from "@/components/Personajes.vue"
import { ref, onMounted, onUnmounted } from 'vue'

const activeTool = ref('characters')
const currentUser = ref(null)
const clearanceLevel = ref(3)
const currentTime = ref('')
const isMobile = ref(false)

const setActiveTool = (tool) => {
  activeTool.value = tool
}

const getActiveToolTitle = () => {
  switch(activeTool.value) {
    case 'characters': return 'CHARACTERS MANAGEMENT'
    case 'user': return 'USER PROFILE'
    default: return '[CLASSIFIED TOOL]'
  }
}

const loadUserProfile = () => {
  console.log('Loading user profile component...')
}

const updateTime = () => {
  const now = new Date()
  currentTime.value = now.toLocaleString('en-US', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: false
  }).replace(/(\d+)\/(\d+)\/(\d+),/, '$3-$1-$2')
}

const checkMobile = () => {
  isMobile.value = window.innerWidth < 1024
}

const fetchCurrentUser = async () => {
  try {
    const response = await fetch('/api/auth/user/')
    if (response.ok) {
      const data = await response.json()
      currentUser.value = data
    }
  } catch (error) {
    console.error('Error fetching user:', error)
  }
}

onMounted(() => {
  checkMobile()
  updateTime()
  const timeInterval = setInterval(updateTime, 1000)
  fetchCurrentUser()
  
  window.addEventListener('resize', checkMobile)
  
  return () => {
    clearInterval(timeInterval)
    window.removeEventListener('resize', checkMobile)
  }
})
</script>

<style scoped>
/* Estilos principales - MODIFICADO: Ocupa toda la página */
.dashboard-page {
  position: relative;
  min-height: calc(100vh - 64px); /* Resta la altura del header */
  color: #d8d8d8;
  background: #0a0a0a;
  font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
  line-height: 1.5;
  width: 100%;
  max-width: 100%;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  box-sizing: border-box;
}

/* Overlay para móviles */
.mobile-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: 
    linear-gradient(135deg, #0a0a0a 0%, #121212 25%, #0a0a0a 50%, #121212 75%, #0a0a0a 100%),
    radial-gradient(circle at 20% 30%, rgba(30, 30, 30, 0.9) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(40, 40, 40, 0.7) 0%, transparent 50%);
  z-index: 10000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  backdrop-filter: blur(10px);
}

.mobile-overlay-content {
  max-width: 600px;
  width: 100%;
  background: rgba(15, 15, 15, 0.95);
  border: 1px solid #333;
  border-radius: 0px;
  padding: 40px;
  text-align: center;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
}

.mobile-warning-icon {
  width: 80px;
  height: 80px;
  color: #fc6f03;
  margin: 0 auto 20px;
}

.mobile-warning-title {
  font-size: 28px;
  font-weight: 900;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 0 0 8px 0;
  text-shadow: 0 0 10px rgba(252, 111, 3, 0.3);
}

.mobile-warning-subtitle {
  font-size: 14px;
  color: #aaa;
  letter-spacing: 0.5px;
  margin: 0 0 30px 0;
  text-transform: uppercase;
}

.mobile-warning-message {
  font-size: 16px;
  color: #d8d8d8;
  line-height: 1.6;
  margin: 0 0 30px 0;
  padding: 20px;
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  border-radius: 0px;
}

.mobile-warning-info {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 30px;
  padding: 20px;
  background: rgba(25, 25, 25, 0.8);
  border: 1px solid #333;
  border-radius: 0px;
}

.warning-info-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.warning-info-item:last-child {
  border-bottom: none;
}

.info-label {
  font-size: 12px;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.info-value {
  font-size: 14px;
  color: #fc6f03;
  font-weight: 600;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.5px;
}

/* Fondo SCP - MODIFICADO: Cubre toda la pantalla */
.site-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: 
    linear-gradient(135deg, #0a0a0a 0%, #121212 25%, #0a0a0a 50%, #121212 75%, #0a0a0a 100%),
    radial-gradient(circle at 20% 30%, rgba(30, 30, 30, 0.8) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(40, 40, 40, 0.6) 0%, transparent 50%);
  z-index: 0;
}

.grid-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: 
    linear-gradient(rgba(60, 60, 60, 0.1) 1px, transparent 1px),
    linear-gradient(90deg, rgba(60, 60, 60, 0.1) 1px, transparent 1px);
  background-size: 40px 40px;
  animation: gridMove 20s linear infinite;
}

.particles {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: 
    radial-gradient(circle at 10% 20%, rgba(100, 100, 100, 0.05) 1px, transparent 1px),
    radial-gradient(circle at 90% 80%, rgba(100, 100, 100, 0.05) 1px, transparent 1px);
  background-size: 30px 30px;
}

.scan-line {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, 
    transparent 0%, 
    rgba(80, 80, 80, 0.8) 10%, 
    rgba(120, 120, 120, 0.9) 50%, 
    rgba(80, 80, 80, 0.8) 90%, 
    transparent 100%);
  animation: scan 6s linear infinite;
  z-index: 1;
  opacity: 0.3;
}

@keyframes scan {
  0% { top: 0%; }
  100% { top: 100%; }
}

@keyframes gridMove {
  0% { transform: translateY(0); }
  100% { transform: translateY(40px); }
}

/* Contenido Principal - MODIFICADO: Ocupa todo el ancho */
.dashboard-content {
  position: relative;
  z-index: 1;
  display: flex;
  min-height: calc(100vh - 64px);
  padding: 20px 0 20px 0;
  box-sizing: border-box;
  width: 1500%;
  max-width: 100%;
  margin: 0;
  gap: 20px;
}

/* Sidebar de Navegación - MODIFICADO: Altura completa */
.dashboard-sidebar {
  width: 260px;
  background: rgba(15, 15, 15, 0.95);
  border: 1px solid #333;
  border-radius: 0px;
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  backdrop-filter: blur(5px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  height: calc(100vh - 104px); /* Altura fija para ocupar toda la pantalla */
  position: sticky;
  top: 84px; /* 64px del header + 20px de padding */
}

.sidebar-header {
  padding: 16px 20px;
  border-bottom: 1px solid #333;
  background: rgba(25, 25, 25, 0.8);
  overflow-x: hidden;
}

.sidebar-title {
  font-size: 16px;
  font-weight: 700;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 4px 0;
  overflow-x: hidden;
}

.sidebar-subtitle {
  font-size: 11px;
  color: #888;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.3px;
  overflow-x: hidden;
}

.sidebar-tools {
  flex: 1;
  padding: 16px 0;
  overflow-y: auto;
  overflow-x: hidden;
}

.tool-category {
  margin-bottom: 20px;
}

.category-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px 10px 20px;
  border-bottom: 1px solid #333;
}

.category-title {
  font-size: 10px;
  font-weight: 600;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.category-indicator {
  width: 6px;
  height: 6px;
  border-radius: 0px;
  background: #fc6f03;
}

.category-indicator.classified {
  background: #aa2222;
}

.tool-list {
  padding: 8px 0;
}

.tool-item {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 20px;
  background: transparent;
  border: none;
  color: #aaa;
  text-align: left;
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
  border-radius: 0px;
}

.tool-item:not(.redacted):hover {
  background: rgba(40, 40, 40, 0.6);
  color: #ddd;
}

.tool-item.active {
  background: rgba(252, 111, 3, 0.1);
  color: #fc6f03;
  border-left: 2px solid #fc6f03;
}

.tool-item.redacted {
  cursor: not-allowed;
  opacity: 0.6;
}

.tool-icon {
  width: 18px;
  height: 18px;
  color: currentColor;
  flex-shrink: 0;
}

.tool-icon.redacted {
  color: #aa2222;
}

.tool-name {
  font-size: 13px;
  font-weight: 500;
  flex: 1;
}

.tool-name.redacted-text {
  font-family: 'Consolas', monospace;
  color: #aa2222;
  font-weight: 700;
  letter-spacing: 0.5px;
}

.tool-indicator {
  width: 14px;
  height: 14px;
  color: #fc6f03;
  opacity: 0.8;
}

.clearance-warning {
  width: 14px;
  height: 14px;
  color: #aa2222;
  flex-shrink: 0;
}

.sidebar-footer {
  padding: 16px 20px;
  border-top: 1px solid #333;
  background: rgba(25, 25, 25, 0.8);
}

.system-status {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.status-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.status-label {
  font-size: 10px;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.status-value {
  font-size: 11px;
  font-weight: 600;
  color: #ddd;
  font-family: 'Consolas', monospace;
}

.status-value.authorized {
  color: #4CAF50;
}

/* Área de Contenido Principal - MODIFICADO: Ocupa todo el espacio restante */
.dashboard-main {
  flex: 1;
  background: rgba(15, 15, 15, 0.95);
  border: 1px solid #333;
  border-radius: 0px;
  display: flex;
  flex-direction: column;
  backdrop-filter: blur(5px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  height: calc(100vh - 104px); /* Altura fija para ocupar toda la pantalla */
  min-width: 0; /* Importante para flexbox */
}

.main-header {
  padding: 20px 24px;
  border-bottom: 1px solid #333;
  background: rgba(25, 25, 25, 0.8);
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  flex-shrink: 0;
}

.header-left {
  flex: 1;
}

.main-title {
  font-size: 20px;
  font-weight: 700;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 6px 0;
}

.main-subtitle {
  font-size: 13px;
  color: #aaa;
}

.header-right {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 8px;
}

.session-info {
  display: flex;
  align-items: center;
  gap: 6px;
}

.session-indicator {
  width: 6px;
  height: 6px;
  border-radius: 0px;
  background: #4CAF50;
  box-shadow: 0 0 6px #4CAF50;
  animation: pulse 2s infinite;
}

.session-indicator.active {
  background: #4CAF50;
}

.session-text {
  font-size: 11px;
  color: #4CAF50;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.3px;
  text-transform: uppercase;
  font-weight: 600;
}

.timestamp {
  font-size: 11px;
  color: #888;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.3px;
}

@keyframes pulse {
  0% { opacity: 0.6; }
  50% { opacity: 1; }
  100% { opacity: 0.6; }
}

/* Component Container - MODIFICADO: Scroll si es necesario */
.component-container {
  flex: 1;
  overflow: auto;
  position: relative;
  width: 100%;
  height: 100%;
}

/* Placeholders */
.component-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 400px;
}

.component-placeholder.classified {
  background: rgba(30, 20, 20, 0.3);
  border: 1px solid rgba(170, 34, 34, 0.3);
  border-radius: 0px;
}

.placeholder-content {
  text-align: center;
  max-width: 400px;
  padding: 40px;
  background: rgba(25, 25, 25, 0.6);
  border: 1px solid #444;
  border-radius: 0px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.placeholder-icon {
  width: 50px;
  height: 50px;
  color: #fc6f03;
  opacity: 0.8;
}

.placeholder-icon.redacted {
  color: #aa2222;
}

.placeholder-title {
  font-size: 18px;
  font-weight: 700;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0;
}

.placeholder-title.redacted-text {
  color: #aa2222;
  font-family: 'Consolas', monospace;
}

.placeholder-text {
  font-size: 14px;
  color: #aaa;
  line-height: 1.6;
  margin: 0;
}

.placeholder-action {
  margin-top: 16px;
}

.action-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 20px;
  background: rgba(252, 111, 3, 0.1);
  border: 1px solid rgba(252, 111, 3, 0.3);
  border-radius: 0px;
  color: #fc6f03;
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.action-button:hover {
  background: rgba(252, 111, 3, 0.2);
  border-color: rgba(252, 111, 3, 0.5);
  transform: translateY(-1px);
}

.button-text {
  font-family: 'Consolas', monospace;
}

.button-indicator {
  width: 14px;
  height: 14px;
  color: currentColor;
}

.clearance-required {
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin-top: 16px;
  padding: 12px 16px;
  background: rgba(170, 34, 34, 0.1);
  border: 1px solid rgba(170, 34, 34, 0.3);
  border-radius: 0px;
  width: 100%;
}

.clearance-label {
  font-size: 10px;
  color: #aa2222;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.clearance-value {
  font-size: 13px;
  font-weight: 700;
  color: #aa2222;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.5px;
}

.main-footer {
  padding: 12px 24px;
  border-top: 1px solid #333;
  background: rgba(25, 25, 25, 0.8);
  display: flex;
  justify-content: space-between;
  flex-shrink: 0;
}

.footer-info {
  display: flex;
  align-items: center;
  gap: 6px;
}

.info-label {
  font-size: 10px;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.info-value {
  font-size: 11px;
  color: #ddd;
  font-family: 'Consolas', monospace;
}

/* Responsive */
@media (max-width: 1023px) {
  .dashboard-content {
    display: none;
  }
}

/* Ajustes para pantallas grandes */
@media (min-width: 1024px) {
  .mobile-overlay {
    display: none !important;
  }
  
  .dashboard-content {
    display: flex !important;
  }
}

@media (min-width: 1400px) {
  .dashboard-sidebar {
    width: 280px;
  }
  
  .dashboard-main {
    flex: 1;
  }
  
  .main-title {
    font-size: 22px;
  }
  
  .main-subtitle {
    font-size: 14px;
  }
}

/* Reglas adicionales para asegurar ancho completo */
:deep(.dashboard-page) {
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
}

:deep(.dashboard-content) {
  width: 1500px !important;
  max-width: 100% !important;
  margin: 0 !important;
}
</style>