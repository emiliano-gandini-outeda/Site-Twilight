<template>
  <div class="dashboard-page">
    <!-- Fondo SCP -->
    <div class="site-background">
      <div class="grid-overlay"></div>
      <div class="scan-line"></div>
      <div class="particles"></div>
    </div>

    <!-- Header del Dashboard -->
    <header class="dashboard-header">
      <div class="header-content">
        <div class="site-info">
          <h1 class="site-title">SITE 81: TWILIGHT</h1>
          <h2 class="site-subtitle">Personal Management Dashboard</h2>
          <div class="user-status">
            <div class="status-indicator active"></div>
            <span class="status-text">CONNECTED</span>
          </div>
        </div>
        
        <div class="header-actions">
          <div class="clearance-badge">
            <span class="clearance-level">CLEARANCE LEVEL 3</span>
            <div class="clearance-indicator">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
              </svg>
            </div>
          </div>
        </div>
      </div>
      
      <div class="header-decoration">
        <div class="decoration-line"></div>
        <div class="decoration-dot"></div>
        <div class="decoration-line"></div>
      </div>
    </header>

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
              <span class="status-label">ACCESS:</span>
              <span class="status-value authorized">GRANTED</span>
            </div>
            <div class="status-item">
              <span class="status-label">SESSION:</span>
              <span class="status-value">00:24:18</span>
            </div>
          </div>
        </div>
      </nav>

      <!-- Área de Contenido Principal -->
      <section class="dashboard-main">
        <div class="main-header">
          <h2 class="main-title">{{ getActiveToolTitle() }}</h2>
          <div class="main-subtitle">
            <span v-if="activeTool === 'characters'">Manage and view your authorized personnel files</span>
            <span v-else-if="activeTool === 'user'">View and manage your user profile and settings</span>
            <span v-else>[CLASSIFIED CONTENT]</span>
          </div>
        </div>
        
        <!-- Componente dinámico -->
        <div class="component-container">
          <div v-if="activeTool === 'characters'" class="component-placeholder">
            <div class="placeholder-content">
              <div class="placeholder-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="#fc6f03" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
              </div>
              <h3 class="placeholder-title">CHARACTERS MANAGEMENT</h3>
              <p class="placeholder-text">Personnel management system is loading...</p>
              <div class="placeholder-action">
                <button class="action-button" @click="loadCharacters">
                  <span class="button-text">INITIALIZE SYSTEM</span>
                  <div class="button-indicator">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <polyline points="9 18 15 12 9 6"></polyline>
                    </svg>
                  </div>
                </button>
              </div>
            </div>
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
            <span class="info-value">2024-01-15 14:30:22 UTC</span>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const activeTool = ref('characters')

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

const loadCharacters = () => {
  console.log('Loading characters component...')
  // Aquí se cargará el componente de personajes
}

const loadUserProfile = () => {
  console.log('Loading user profile component...')
  // Aquí se cargará el componente de usuario
}
</script>

<style scoped>
/* Estilos principales - Solo Desktop */
.dashboard-page {
  position: relative;
  min-height: 100vh;
  color: #d8d8d8;
  background: #0a0a0a;
  overflow: hidden;
  font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
  line-height: 1.5;
  width: 100vw;
  height: 100vh;
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}

/* Fondo SCP (reutilizado de Information.vue) */
.site-background {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
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
  right: 0;
  bottom: 0;
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
  right: 0;
  bottom: 0;
  background: 
    radial-gradient(circle at 10% 20%, rgba(100, 100, 100, 0.05) 1px, transparent 1px),
    radial-gradient(circle at 90% 80%, rgba(100, 100, 100, 0.05) 1px, transparent 1px);
  background-size: 30px 30px;
}

.scan-line {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
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

/* Header del Dashboard */
.dashboard-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 80px;
  background: rgba(15, 15, 15, 0.95);
  border-bottom: 1px solid #333;
  backdrop-filter: blur(10px);
  z-index: 10;
  padding: 0 32px;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100%;
  width: 100%;
}

.site-info {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.site-title {
  font-size: 22px;
  font-weight: 900;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 0;
  text-shadow: 0 0 10px rgba(252, 111, 3, 0.3);
}

.site-subtitle {
  font-size: 14px;
  font-weight: 500;
  color: #aaa;
  letter-spacing: 0.5px;
  margin: 0;
}

.user-status {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 4px;
}

.status-indicator.active {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #4CAF50;
  box-shadow: 0 0 8px #4CAF50;
  animation: pulse 2s infinite;
}

.status-text {
  font-size: 12px;
  color: #4CAF50;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.3px;
  text-transform: uppercase;
  font-weight: 600;
}

@keyframes pulse {
  0% { opacity: 1; }
  50% { opacity: 0.5; }
  100% { opacity: 1; }
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 20px;
}

.clearance-badge {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: rgba(252, 111, 3, 0.1);
  border: 1px solid rgba(252, 111, 3, 0.3);
  border-radius: 6px;
}

.clearance-level {
  font-size: 12px;
  font-weight: 600;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  font-family: 'Consolas', monospace;
}

.clearance-indicator {
  width: 16px;
  height: 16px;
  color: #fc6f03;
}

.header-decoration {
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 0 32px;
}

.decoration-line {
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, transparent, #fc6f03, transparent);
}

.decoration-dot {
  width: 6px;
  height: 6px;
  background: #fc6f03;
  border-radius: 50%;
  box-shadow: 0 0 8px #fc6f03;
}

/* Contenido Principal */
.dashboard-content {
  position: fixed;
  top: 80px;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  z-index: 5;
  padding: 24px 32px;
  box-sizing: border-box;
  overflow: hidden;
}

/* Sidebar de Navegación */
.dashboard-sidebar {
  width: 280px;
  background: rgba(20, 20, 20, 0.9);
  border: 1px solid #333;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  margin-right: 24px;
  flex-shrink: 0;
  backdrop-filter: blur(5px);
  overflow: hidden;
}

.sidebar-header {
  padding: 20px 24px;
  border-bottom: 1px solid #333;
  background: rgba(30, 30, 30, 0.6);
}

.sidebar-title {
  font-size: 18px;
  font-weight: 700;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 4px 0;
}

.sidebar-subtitle {
  font-size: 12px;
  color: #888;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.3px;
}

.sidebar-tools {
  flex: 1;
  padding: 20px 0;
  overflow-y: auto;
}

.tool-category {
  margin-bottom: 24px;
}

.category-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px 12px 24px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.category-title {
  font-size: 11px;
  font-weight: 600;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.category-indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #fc6f03;
  box-shadow: 0 0 6px rgba(252, 111, 3, 0.5);
}

.category-indicator.classified {
  background: #aa2222;
  box-shadow: 0 0 6px rgba(170, 34, 34, 0.5);
}

.tool-list {
  padding: 8px 0;
}

.tool-item {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 24px;
  background: transparent;
  border: none;
  color: #aaa;
  text-align: left;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.tool-item:not(.redacted):hover {
  background: rgba(40, 40, 40, 0.6);
  color: #ddd;
}

.tool-item.active {
  background: rgba(252, 111, 3, 0.1);
  color: #fc6f03;
  border-right: 3px solid #fc6f03;
}

.tool-item.redacted {
  cursor: not-allowed;
  opacity: 0.6;
}

.tool-icon {
  width: 20px;
  height: 20px;
  color: currentColor;
  flex-shrink: 0;
}

.tool-icon.redacted {
  color: #aa2222;
}

.tool-name {
  font-size: 14px;
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
  width: 16px;
  height: 16px;
  color: #fc6f03;
  opacity: 0.8;
}

.clearance-warning {
  width: 16px;
  height: 16px;
  color: #aa2222;
  flex-shrink: 0;
}

.sidebar-footer {
  padding: 20px 24px;
  border-top: 1px solid #333;
  background: rgba(30, 30, 30, 0.6);
}

.system-status {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.status-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.status-label {
  font-size: 11px;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.status-value {
  font-size: 12px;
  font-weight: 600;
  color: #ddd;
  font-family: 'Consolas', monospace;
}

.status-value.authorized {
  color: #4CAF50;
}

/* Área de Contenido Principal */
.dashboard-main {
  flex: 1;
  background: rgba(20, 20, 20, 0.9);
  border: 1px solid #333;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  backdrop-filter: blur(5px);
  overflow: hidden;
}

.main-header {
  padding: 24px 32px;
  border-bottom: 1px solid #333;
  background: rgba(30, 30, 30, 0.6);
}

.main-title {
  font-size: 24px;
  font-weight: 700;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 8px 0;
}

.main-subtitle {
  font-size: 14px;
  color: #aaa;
}

.component-container {
  flex: 1;
  padding: 32px;
  overflow-y: auto;
}

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
  border-radius: 8px;
}

.placeholder-content {
  text-align: center;
  max-width: 400px;
  padding: 40px;
  background: rgba(25, 25, 25, 0.6);
  border: 1px solid #444;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.placeholder-icon {
  width: 60px;
  height: 60px;
  color: #fc6f03;
  opacity: 0.8;
}

.placeholder-icon.redacted {
  color: #aa2222;
}

.placeholder-title {
  font-size: 20px;
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
  font-size: 15px;
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
  padding: 12px 24px;
  background: rgba(252, 111, 3, 0.1);
  border: 1px solid rgba(252, 111, 3, 0.3);
  border-radius: 6px;
  color: #fc6f03;
  font-size: 14px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.action-button:hover {
  background: rgba(252, 111, 3, 0.2);
  border-color: rgba(252, 111, 3, 0.5);
  transform: translateY(-2px);
}

.button-text {
  font-family: 'Consolas', monospace;
}

.button-indicator {
  width: 16px;
  height: 16px;
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
  border-radius: 6px;
  width: 100%;
}

.clearance-label {
  font-size: 11px;
  color: #aa2222;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.clearance-value {
  font-size: 14px;
  font-weight: 700;
  color: #aa2222;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.5px;
}

.main-footer {
  padding: 16px 32px;
  border-top: 1px solid #333;
  background: rgba(30, 30, 30, 0.6);
  display: flex;
  justify-content: space-between;
}

.footer-info {
  display: flex;
  align-items: center;
  gap: 8px;
}

.info-label {
  font-size: 11px;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.info-value {
  font-size: 12px;
  color: #ddd;
  font-family: 'Consolas', monospace;
}

/* Asegurar que sea solo para desktop */
@media (max-width: 1024px) {
  .dashboard-page::before {
    content: 'DESKTOP ONLY - Please access from a desktop device';
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(10, 10, 10, 0.95);
    color: #fc6f03;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    text-align: center;
    padding: 40px;
    z-index: 1000;
    backdrop-filter: blur(10px);
  }
}
</style>