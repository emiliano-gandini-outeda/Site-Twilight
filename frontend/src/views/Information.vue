<template>
  <div class="information-page">
    <!-- Fondo SCP -->
    <div class="site-background">
      <div class="grid-overlay"></div>
      <div class="scan-line"></div>
      <div class="particles"></div>
    </div>

    <!-- Header de la Página -->
    <div class="page-header">
      <div class="role-switch">
        <div class="switch-container">
          <button 
            class="switch-option" 
            :class="{ 'active': activeRole === 'on' }"
            @click="setActiveRole('on')"
          >
            <span class="switch-text">ON ROL</span>
            <div class="switch-indicator" v-if="activeRole === 'on'">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
            </div>
          </button>
          <button 
            class="switch-option" 
            :class="{ 'active': activeRole === 'off' }"
            @click="setActiveRole('off')"
          >
            <span class="switch-text">OFF ROL</span>
            <div class="switch-indicator" v-if="activeRole === 'off'">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
            </div>
          </button>
        </div>
        <div class="switch-label">
          <div class="status-indicator" :class="activeRole"></div>
          <span class="status-text">{{ activeRole === 'on' ? 'ROL ACTIVO' : 'ROL DESACTIVADO' }}</span>
        </div>
      </div>
    </div>

    <!-- Contenido Principal -->
    <main class="page-content">
      <!-- Contenido ON ROL -->
      <div v-if="activeRole === 'on'" class="on-role-content">
        <!-- Título Principal -->
        <div class="main-title-section">
          <h1 class="main-title">SITE 81: TWILIGHT</h1>
          <h2 class="main-subtitle">SCP Foundation Secure Facility Dossier</h2>
          <div class="title-decoration">
            <div class="decoration-line"></div>
            <div class="decoration-dot"></div>
            <div class="decoration-line"></div>
          </div>
        </div>

        <!-- Información General -->
        <div class="section-block">
          <h3 class="section-title">INFORMACIÓN GENERAL</h3>
          <div class="general-info">
            <div class="info-text">
              <p>Site 81, designado como "Twilight", opera como una instalación de contención secundaria bajo la jurisdicción del Sector-28. Especializado en entidades de clase Euclid y Keter con propiedades temporales o dimensionales atenuadas.</p>
              <p>La instalación mantiene protocolos de cuarentena extendida y sistemas de monitoreo de realidad en tiempo real, sirviendo como punto crítico para investigaciones interdimensionales.</p>
            </div>
            <div class="info-image">
              <div class="image-container">
                <div class="placeholder-image">
                  <div class="image-content">
                    <div class="image-grid">
                      <div v-for="n in 16" :key="n" class="grid-cell"></div>
                    </div>
                    <div class="image-overlay">
                      <div class="overlay-text">VISUALIZACIÓN DE CONTENCIÓN</div>
                      <div class="overlay-subtext">SECTOR-28 - SITE 81</div>
                    </div>
                  </div>
                </div>
                <div class="image-caption">
                  <span class="caption-icon">📡</span>
                  <span class="caption-text">Monitoreo dimensional activo - Protocolo Twilight</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Secciones Decorativas -->
        <div class="decorative-sections">
          <div class="decorative-item">
            <div class="decorative-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="#fc6f03" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="2" y1="12" x2="22" y2="12"></line>
                <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
              </svg>
            </div>
            <h4 class="decorative-title">ESTABILIDAD DIMENSIONAL</h4>
            <p class="decorative-text">Site 81 mantiene anclajes de realidad constantes para prevenir brechas dimensionales. El sistema de redundancia opera las 24 horas con un margen de error del 0.0001%.</p>
          </div>

          <div class="decorative-item">
            <div class="decorative-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="#fc6f03" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="6" width="20" height="12" rx="2" ry="2"></rect>
                <path d="M12 12h.01"></path>
                <path d="M16 6V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"></path>
              </svg>
            </div>
            <h4 class="decorative-title">CONTENCIÓN AVANZADA</h4>
            <p class="decorative-text">12 cámaras de contención de nivel 4 equipadas con sistemas de supresión temporal. Capacidad para albergar hasta 24 entidades Euclid simultáneamente.</p>
          </div>

          <div class="decorative-item">
            <div class="decorative-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="#fc6f03" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                <circle cx="9" cy="7" r="4"></circle>
                <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
              </svg>
            </div>
            <h4 class="decorative-title">PERSONAL ESPECIALIZADO</h4>
            <p class="decorative-text">Equipo multidisciplinario de 247 investigadores y agentes de contención. Evaluaciones de realidad obligatorias cada 72 horas para todo el personal.</p>
          </div>
        </div>

        <!-- Instalaciones -->
        <div class="section-block">
          <h3 class="section-title">INSTALACIONES</h3>
          <div class="facilities-grid">
            <div class="facility-card">
              <div class="facility-header">
                <h4 class="facility-title">CORTES ISLAND POWER STATION</h4>
                <div class="facility-wing">Ala A</div>
              </div>
              <p class="facility-text">Central eléctrica principal. Provee energía redundante para sistemas de contención críticos. Capacidad de 500MW con respaldo nuclear.</p>
            </div>

            <div class="facility-card">
              <div class="facility-header">
                <h4 class="facility-title">CORTES WATER TREATMENT STATION</h4>
                <div class="facility-wing">Ala B</div>
              </div>
              <p class="facility-text">Planta de tratamiento de agua especializada. Sistema de filtración para anomalías acuáticas. Laboratorios de investigación hídrica.</p>
            </div>

            <div class="facility-card">
              <div class="facility-header">
                <h4 class="facility-title">CORTES ISLAND MILITARY BASE</h4>
                <div class="facility-wing">Ala C</div>
              </div>
              <p class="facility-text">Base militar de respuesta rápida. Aloja unidades MTF especializadas. Centro de comando para operaciones de contención.</p>
            </div>
          </div>
        </div>

        <!-- Instalación Principal -->
        <div class="section-block">
          <h3 class="section-title">INSTALACIÓN PRINCIPAL</h3>
          <div class="main-facility">
            <div class="office-section">
              <div class="office-card">
                <h4 class="office-title">OFICINAS PRINCIPALES</h4>
                <ul class="office-list">
                  <li class="office-item">
                    <div class="office-icon">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                        <circle cx="12" cy="7" r="4"></circle>
                      </svg>
                    </div>
                    <span class="office-name">Administración</span>
                  </li>
                  <li class="office-item">
                    <div class="office-icon">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"></circle>
                        <line x1="12" y1="8" x2="12" y2="12"></line>
                        <line x1="12" y1="16" x2="12.01" y2="16"></line>
                      </svg>
                    </div>
                    <span class="office-name">Comité de Clasificación</span>
                  </li>
                  <li class="office-item">
                    <div class="office-icon">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                        <polyline points="14 2 14 8 20 8"></polyline>
                        <line x1="16" y1="13" x2="8" y2="13"></line>
                        <line x1="16" y1="17" x2="8" y2="17"></line>
                        <polyline points="10 9 9 9 8 9"></polyline>
                      </svg>
                    </div>
                    <span class="office-name">Comité de Ética</span>
                  </li>
                </ul>
              </div>
            </div>

            <div class="wings-section">
              <div class="wings-container">
                <div 
                  v-for="wing in wings" 
                  :key="wing.id"
                  class="wing-card"
                  :class="{ 'expanded': expandedWing === wing.id }"
                  @click="toggleWing(wing.id)"
                >
                  <div class="wing-header">
                    <div class="wing-name">{{ wing.name }}</div>
                    <div class="wing-icon">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <polyline points="6 9 12 15 18 9"></polyline>
                      </svg>
                    </div>
                  </div>
                  <div v-if="expandedWing === wing.id" class="wing-content">
                    <div class="wing-detail">
                      <span class="detail-label">Nombre:</span>
                      <span class="detail-value">{{ wing.fullName }}</span>
                    </div>
                    <div v-if="wing.subterranean" class="wing-detail">
                      <span class="detail-label subterranean">Subterráneo</span>
                    </div>
                    <div class="wing-detail">
                      <span class="detail-label">Función:</span>
                      <span class="detail-value">{{ wing.function }}</span>
                    </div>
                    <div class="wing-detail">
                      <span class="detail-label">Capacidad:</span>
                      <span class="detail-value">{{ wing.capacity }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Información Adicional -->
        <div class="section-block">
          <h3 class="section-title">INFORMACIÓN ADICIONAL</h3>
          <div class="additional-info">
            <p class="info-paragraph">Site 81 fue establecido en 1987 como respuesta al Incidente de Realidad Delta-7. Su ubicación en Cortes Island fue seleccionada por sus propiedades geológicas únicas, que proporcionan blindaje natural contra anomalías dimensionales.</p>
            
            <p class="info-paragraph">La instalación opera bajo el Protocolo Twilight, un conjunto de medidas de seguridad diseñadas específicamente para contener entidades con propiedades espacio-temporales inestables. Este protocolo incluye monitoreo constante de fluctuaciones de realidad y sistemas de redundancia cuántica.</p>
            
            <p class="info-paragraph">El personal de Site 81 está compuesto por especialistas en física anómala, investigadores de realidad y agentes de contención entrenados en protocolos de emergencia interdimensional. Todos los miembros del personal deben completar el Curso de Adaptación a la Realidad antes de ser asignados.</p>
          </div>

          <div class="mixed-section">
            <div class="mixed-content">
              <div class="mixed-text">
                <h4 class="mixed-title">INVESTIGACIÓN TEMPORAL</h4>
                <p>Site 81 alberga 3 laboratorios de investigación temporal equipados con tecnología de vanguardia para estudiar anomalías cronológicas. Estos laboratorios operan bajo estrictos protocolos de seguridad temporal para prevenir paradojas.</p>
              </div>
              <div class="mixed-image">
                <div class="image-placeholder">
                  <div class="placeholder-content">
                    <div class="placeholder-grid">
                      <div v-for="n in 9" :key="n" class="grid-square"></div>
                    </div>
                    <div class="placeholder-label">LABORATORIO TEMPORAL A-7</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="info-paragraph solo">
            <p>La cooperación con otros sitios de la Fundación es constante, particularmente con Site 17 para intercambio de datos de investigación y con Area 12 para protocolos de contención especializados. Site 81 también sirve como centro de entrenamiento para personal que trabajará con anomalías dimensionales.</p>
          </div>

          <div class="mixed-section reversed">
            <div class="mixed-content">
              <div class="mixed-image">
                <div class="image-placeholder">
                  <div class="placeholder-content">
                    <div class="placeholder-grid alt">
                      <div v-for="n in 12" :key="n" class="grid-square"></div>
                    </div>
                    <div class="placeholder-label">SISTEMA DE MONITOREO DIMENSIONAL</div>
                  </div>
                </div>
              </div>
              <div class="mixed-text">
                <h4 class="mixed-title">SISTEMAS DE SEGURIDAD</h4>
                <p>La instalación cuenta con múltiples capas de seguridad física y dimensional. Sistemas de contención de clase IV, barreras de realidad y protocolos de cuarentena automatizados aseguran la integridad de la instalación incluso bajo estrés anómalo extremo.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Contenido OFF ROL -->
      <div v-else class="off-role-content">
        <div class="off-role-container">
          <div class="off-role-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="#fc6f03" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="4.93" y1="4.93" x2="19.07" y2="19.07"></line>
            </svg>
          </div>
          <h2 class="off-role-title">MODO OFF ROL ACTIVADO</h2>
          <p class="off-role-text">
            Esta sección contiene información fuera del rol (meta-información) sobre la plataforma Site Twilight. 
            Aquí encontrarás detalles técnicos, guías de uso, y documentación relacionada con la plataforma de roleplay.
          </p>
          <p class="off-role-text">
            Site Twilight es una plataforma dedicada al roleplay dentro del universo SCP, ofreciendo herramientas 
            para creación de personajes, narrativas colaborativas y participación en eventos organizados.
          </p>
          <p class="off-role-text">
            El contenido de rol (ON ROL) representa la ficción dentro del universo SCP Foundation, mientras que 
            esta sección (OFF ROL) proporciona información sobre cómo utilizar la plataforma efectivamente.
          </p>
          <div class="off-role-note">
            <div class="note-icon">ℹ</div>
            <div class="note-text">Esta sección está en desarrollo. Próximamente se añadirá más contenido OFF ROL.</div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const activeRole = ref('on')
const expandedWing = ref(null)

const wings = ref([
  { id: 1, name: 'Ala A', fullName: 'Contención Primaria', subterranean: false, function: 'Contención Euclid', capacity: '12 cámaras' },
  { id: 2, name: 'Ala B', fullName: 'Investigación Temporal', subterranean: true, function: 'Laboratorios', capacity: '3 laboratorios' },
  { id: 3, name: 'Ala C', fullName: 'Administración Central', subterranean: false, function: 'Oficinas', capacity: '80 oficinas' },
  { id: 4, name: 'Ala D', fullName: 'Sistemas de Soporte', subterranean: true, function: 'Mantenimiento', capacity: 'Sistemas críticos' },
  { id: 5, name: 'Ala E', fullName: 'Cuarteles MTF', subterranean: false, function: 'Alojamiento', capacity: '150 agentes' },
  { id: 6, name: 'Ala F', fullName: 'Archivos Seguros', subterranean: true, function: 'Almacenamiento', capacity: 'Nivel 4' },
  { id: 7, name: 'Ala G', fullName: 'Medicina Anómala', subterranean: false, function: 'Hospital', capacity: '50 camas' },
  { id: 8, name: 'Ala H', fullName: 'Comunicaciones', subterranean: true, function: 'Transmisiones', capacity: 'Red global' },
  { id: 9, name: 'Ala I', fullName: 'Energía', subterranean: true, function: 'Generación', capacity: '500MW' },
  { id: 10, name: 'Ala J', fullName: 'Investigación Keter', subterranean: true, function: 'Contención especial', capacity: '4 cámaras' },
  { id: 11, name: 'Ala K', fullName: 'Cuarentena', subterranean: true, function: 'Aislamiento', capacity: '20 unidades' }
])

const setActiveRole = (role) => {
  activeRole.value = role
  expandedWing.value = null
}

const toggleWing = (wingId) => {
  expandedWing.value = expandedWing.value === wingId ? null : wingId
}
</script>

<style scoped>
/* Reset y base - Mobile First */
.information-page {
  position: relative;
  min-height: 100vh;
  color: #d8d8d8;
  background: #0a0a0a;
  overflow-x: hidden;
  font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
  line-height: 1.5;
  width: 100%;
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}

/* Fondo SCP */
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

/* Header de la Página */
.page-header {
  position: relative;
  z-index: 2;
  width: 100%;
  padding: 20px 16px;
  background: rgba(15, 15, 15, 0.9);
  border-bottom: 1px solid #333;
  backdrop-filter: blur(10px);
}

.role-switch {
  width: 100%;
  max-width: 100%;
}

.switch-container {
  display: flex;
  background: rgba(30, 30, 30, 0.8);
  border: 1px solid #444;
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 12px;
  width: 100%;
}

.switch-option {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 16px;
  background: transparent;
  border: none;
  color: #888;
  font-family: inherit;
  font-size: 16px;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.switch-option.active {
  background: rgba(252, 111, 3, 0.1);
  color: #fc6f03;
  border-bottom: 2px solid #fc6f03;
}

.switch-option:not(.active):hover {
  background: rgba(40, 40, 40, 0.6);
  color: #aaa;
}

.switch-indicator {
  width: 18px;
  height: 18px;
  color: #fc6f03;
}

.switch-text {
  font-weight: 700;
}

.switch-label {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 16px;
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  border-radius: 6px;
  width: 100%;
  box-sizing: border-box;
}

.status-indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.status-indicator.on {
  background: #fc6f03;
  box-shadow: 0 0 8px #fc6f03;
  animation: pulse 2s infinite;
}

.status-indicator.off {
  background: #888;
  box-shadow: 0 0 8px #888;
}

.status-text {
  font-size: 14px;
  color: #aaa;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  font-weight: 600;
}

@keyframes pulse {
  0% { opacity: 1; }
  50% { opacity: 0.5; }
  100% { opacity: 1; }
}

/* Contenido Principal */
.page-content {
  position: relative;
  z-index: 1;
  width: 100%;
  padding: 24px 16px;
  box-sizing: border-box;
  max-width: 100%;
  overflow-x: hidden;
}

/* Título Principal */
.main-title-section {
  width: 100%;
  text-align: center;
  margin-bottom: 32px;
  padding: 20px 0;
  position: relative;
}

.main-title {
  font-size: 32px;
  font-weight: 900;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 0 0 8px 0;
  text-shadow: 0 0 10px rgba(252, 111, 3, 0.3);
  line-height: 1.2;
}

.main-subtitle {
  font-size: 16px;
  font-weight: 500;
  color: #fff;
  letter-spacing: 0.5px;
  margin: 0;
  text-shadow: 0 0 5px rgba(255, 255, 255, 0.2);
  opacity: 0.9;
}

.title-decoration {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-top: 16px;
}

.decoration-line {
  width: 40px;
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

/* Secciones Generales */
.section-block {
  width: 100%;
  margin-bottom: 40px;
  position: relative;
}

.section-title {
  font-size: 20px;
  font-weight: 700;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 20px 0;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(252, 111, 3, 0.3);
  position: relative;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  width: 60px;
  height: 2px;
  background: #fc6f03;
  box-shadow: 0 0 5px #fc6f03;
}

/* Información General */
.general-info {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.info-text {
  width: 100%;
}

.info-text p {
  font-size: 15px;
  color: #ccc;
  line-height: 1.6;
  margin: 0 0 16px 0;
}

.info-text p:last-child {
  margin-bottom: 0;
}

.info-image {
  width: 100%;
}

.image-container {
  background: rgba(25, 25, 25, 0.8);
  border: 1px solid #444;
  border-radius: 8px;
  overflow: hidden;
}

.placeholder-image {
  width: 100%;
  height: 200px;
  background: rgba(20, 20, 20, 0.9);
  position: relative;
  overflow: hidden;
}

.image-content {
  width: 100%;
  height: 100%;
  position: relative;
}

.image-grid {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(4, 1fr);
  gap: 1px;
  padding: 16px;
}

.grid-cell {
  background: rgba(40, 40, 40, 0.6);
  border: 1px solid rgba(252, 111, 3, 0.2);
}

.image-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: rgba(10, 10, 10, 0.7);
  padding: 20px;
  text-align: center;
}

.overlay-text {
  font-size: 14px;
  font-weight: 600;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 4px;
}

.overlay-subtext {
  font-size: 12px;
  color: #888;
  letter-spacing: 0.3px;
}

.image-caption {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 16px;
  background: rgba(30, 30, 30, 0.6);
  border-top: 1px solid #444;
}

.caption-icon {
  font-size: 14px;
  color: #fc6f03;
}

.caption-text {
  font-size: 13px;
  color: #aaa;
  letter-spacing: 0.3px;
}

/* Secciones Decorativas */
.decorative-sections {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 40px;
}

.decorative-item {
  background: rgba(25, 25, 25, 0.7);
  border: 1px solid #444;
  border-radius: 8px;
  padding: 20px 16px;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.decorative-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, #fc6f03, transparent);
  opacity: 0.5;
}

.decorative-icon {
  width: 48px;
  height: 48px;
  margin: 0 auto 16px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.decorative-title {
  font-size: 16px;
  font-weight: 700;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 12px 0;
}

.decorative-text {
  font-size: 14px;
  color: #ccc;
  line-height: 1.5;
  margin: 0;
}

/* Instalaciones Grid */
.facilities-grid {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.facility-card {
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  border-radius: 8px;
  padding: 20px 16px;
  position: relative;
  overflow: hidden;
}

.facility-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: #fc6f03;
  opacity: 0.8;
}

.facility-header {
  margin-bottom: 12px;
}

.facility-title {
  font-size: 17px;
  font-weight: 600;
  color: #fc6f03;
  margin: 0 0 4px 0;
  line-height: 1.3;
}

.facility-wing {
  font-size: 13px;
  color: #888;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.3px;
}

.facility-text {
  font-size: 14px;
  color: #ccc;
  line-height: 1.5;
  margin: 0;
}

/* Instalación Principal */
.main-facility {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.office-section {
  width: 100%;
}

.office-card {
  background: rgba(25, 25, 25, 0.8);
  border: 1px solid #444;
  border-radius: 8px;
  padding: 20px 16px;
  width: 100%;
  box-sizing: border-box;
}

.office-title {
  font-size: 18px;
  font-weight: 700;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 20px 0;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(252, 111, 3, 0.3);
}

.office-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.office-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  background: rgba(40, 40, 40, 0.6);
  border: 1px solid #444;
  border-radius: 6px;
  transition: all 0.3s ease;
}

.office-item:hover {
  background: rgba(50, 50, 50, 0.7);
  border-color: #555;
}

.office-icon {
  width: 20px;
  height: 20px;
  color: #fc6f03;
  flex-shrink: 0;
}

.office-name {
  font-size: 15px;
  color: #ddd;
  font-weight: 500;
}

.wings-section {
  width: 100%;
}

.wings-container {
  width: 100%;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.wing-card {
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  border-radius: 6px;
  padding: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.wing-card:hover {
  background: rgba(40, 40, 40, 0.7);
  border-color: #555;
  transform: translateY(-2px);
}

.wing-card.expanded {
  background: rgba(35, 35, 35, 0.8);
  border-color: #fc6f03;
  grid-column: 1 / -1;
}

.wing-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}

.wing-name {
  font-size: 16px;
  font-weight: 600;
  color: #ddd;
  font-family: 'Consolas', monospace;
}

.wing-icon {
  width: 20px;
  height: 20px;
  color: #fc6f03;
  transition: transform 0.3s ease;
}

.wing-card.expanded .wing-icon {
  transform: rotate(180deg);
}

.wing-content {
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid #444;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.wing-detail {
  display: flex;
  gap: 8px;
  font-size: 14px;
}

.detail-label {
  color: #888;
  font-weight: 500;
  min-width: 70px;
}

.detail-label.subterranean {
  color: #666;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  background: rgba(50, 50, 50, 0.6);
  padding: 2px 6px;
  border-radius: 3px;
  border: 1px solid #555;
}

.detail-value {
  color: #ccc;
  flex: 1;
}

/* Información Adicional */
.additional-info {
  width: 100%;
  margin-bottom: 32px;
}

.info-paragraph {
  font-size: 15px;
  color: #ccc;
  line-height: 1.6;
  margin: 0 0 20px 0;
}

.info-paragraph.solo {
  margin: 32px 0;
  padding: 20px;
  background: rgba(25, 25, 25, 0.6);
  border: 1px solid #444;
  border-radius: 8px;
  border-left: 4px solid #fc6f03;
}

.mixed-section {
  width: 100%;
  margin: 32px 0;
}

.mixed-content {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.mixed-section.reversed .mixed-content {
  flex-direction: column-reverse;
}

.mixed-text {
  width: 100%;
}

.mixed-title {
  font-size: 18px;
  font-weight: 700;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 12px 0;
}

.mixed-text p {
  font-size: 15px;
  color: #ccc;
  line-height: 1.6;
  margin: 0;
}

.mixed-image {
  width: 100%;
}

.image-placeholder {
  width: 100%;
  height: 200px;
  background: rgba(20, 20, 20, 0.9);
  border: 1px solid #444;
  border-radius: 8px;
  overflow: hidden;
  position: relative;
}

.placeholder-content {
  width: 100%;
  height: 100%;
  position: relative;
}

.placeholder-grid {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
  gap: 1px;
  padding: 20px;
}

.placeholder-grid.alt {
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(3, 1fr);
}

.grid-square {
  background: rgba(40, 40, 40, 0.6);
  border: 1px solid rgba(252, 111, 3, 0.2);
}

.placeholder-label {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 12px;
  background: rgba(10, 10, 10, 0.8);
  text-align: center;
  font-size: 12px;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  border-top: 1px solid #444;
}

/* Contenido OFF ROL */
.off-role-content {
  width: 100%;
  padding: 40px 0;
}

.off-role-container {
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
  padding: 40px 20px;
  background: rgba(25, 25, 25, 0.7);
  border: 1px solid #444;
  border-radius: 12px;
  position: relative;
  overflow: hidden;
}

.off-role-container::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, transparent, #fc6f03, transparent);
}

.off-role-icon {
  width: 80px;
  height: 80px;
  margin: 0 auto 24px;
  color: #fc6f03;
  opacity: 0.8;
}

.off-role-title {
  font-size: 24px;
  font-weight: 700;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 24px 0;
  text-shadow: 0 0 10px rgba(252, 111, 3, 0.2);
}

.off-role-text {
  font-size: 16px;
  color: #ccc;
  line-height: 1.6;
  margin: 0 0 20px 0;
  text-align: left;
}

.off-role-text:last-child {
  margin-bottom: 0;
}

.off-role-note {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  margin-top: 32px;
  padding: 20px;
  background: rgba(40, 30, 0, 0.2);
  border: 1px solid #aa8800;
  border-radius: 8px;
  text-align: left;
}

.note-icon {
  font-size: 20px;
  color: #ffcc00;
  flex-shrink: 0;
  margin-top: 2px;
}

.note-text {
  font-size: 15px;
  color: #ffdd88;
  line-height: 1.5;
  flex: 1;
}

/* Tablet */
@media (min-width: 768px) {
  .page-header {
    padding: 24px 32px;
  }
  
  .page-content {
    padding: 32px;
  }
  
  .main-title {
    font-size: 40px;
  }
  
  .main-subtitle {
    font-size: 18px;
  }
  
  .section-title {
    font-size: 22px;
  }
  
  .general-info {
    flex-direction: row;
    gap: 32px;
  }
  
  .info-text {
    flex: 1;
  }
  
  .info-image {
    flex: 1;
  }
  
  .placeholder-image {
    height: 240px;
  }
  
  .decorative-sections {
    flex-direction: row;
    flex-wrap: wrap;
  }
  
  .decorative-item {
    flex: 1;
    min-width: 200px;
  }
  
  .facilities-grid {
    flex-direction: row;
    flex-wrap: wrap;
  }
  
  .facility-card {
    flex: 1;
    min-width: 200px;
  }
  
  .main-facility {
    flex-direction: row;
    gap: 32px;
  }
  
  .office-section {
    flex: 1;
  }
  
  .wings-section {
    flex: 2;
  }
  
  .wings-container {
    grid-template-columns: repeat(3, 1fr);
  }
  
  .mixed-content {
    flex-direction: row;
    align-items: center;
    gap: 32px;
  }
  
  .mixed-section.reversed .mixed-content {
    flex-direction: row-reverse;
  }
  
  .mixed-text {
    flex: 1;
  }
  
  .mixed-image {
    flex: 1;
  }
  
  .image-placeholder {
    height: 220px;
  }
  
  .off-role-container {
    padding: 60px 40px;
  }
  
  .off-role-title {
    font-size: 28px;
  }
}

/* Desktop */
@media (min-width: 1024px) {
  .page-header {
    padding: 28px 40px;
  }
  
  .page-content {
    padding: 40px;
    max-width: 1400px;
    margin: 0 auto;
  }
  
  .main-title {
    font-size: 48px;
  }
  
  .main-subtitle {
    font-size: 20px;
  }
  
  .section-title {
    font-size: 24px;
  }
  
  .placeholder-image {
    height: 280px;
  }
  
  .decorative-sections {
    gap: 24px;
  }
  
  .decorative-item {
    padding: 24px 20px;
  }
  
  .decorative-title {
    font-size: 17px;
  }
  
  .decorative-text {
    font-size: 15px;
  }
  
  .facilities-grid {
    gap: 24px;
  }
  
  .facility-card {
    padding: 24px 20px;
  }
  
  .facility-title {
    font-size: 18px;
  }
  
  .office-card {
    padding: 24px 20px;
  }
  
  .office-title {
    font-size: 20px;
  }
  
  .office-item {
    padding: 14px 16px;
  }
  
  .wings-container {
    gap: 16px;
  }
  
  .wing-card {
    padding: 18px 16px;
  }
  
  .wing-content {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
  }
  
  .info-paragraph {
    font-size: 16px;
  }
  
  .mixed-title {
    font-size: 20px;
  }
  
  .mixed-text p {
    font-size: 16px;
  }
  
  .image-placeholder {
    height: 240px;
  }
}

/* Pantallas grandes */
@media (min-width: 1400px) {
  .page-content {
    padding: 48px 60px;
  }
  
  .main-title {
    font-size: 56px;
  }
  
  .main-subtitle {
    font-size: 22px;
  }
  
  .section-block {
    margin-bottom: 60px;
  }
  
  .general-info {
    gap: 48px;
  }
  
  .decorative-sections {
    gap: 32px;
  }
  
  .facilities-grid {
    gap: 32px;
  }
  
  .main-facility {
    gap: 48px;
  }
  
  .wings-container {
    grid-template-columns: repeat(4, 1fr);
  }
}
</style>