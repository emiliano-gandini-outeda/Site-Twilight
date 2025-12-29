<template>
  <div class="landing-page">
    <!-- Fondo SCP -->
    <div class="site-background">
      <div class="grid-overlay"></div>
      <div class="scan-line"></div>
      <div class="particles"></div>
    </div>

    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-container">
        <div class="logo-container">
          <div class="logo-shadow"></div>
          <img src="/logo.png" alt="SCP Foundation Logo" class="scp-logo" />
        </div>
        <div class="hero-motto">
          <span class="motto-word">SECURE.</span>
          <span class="motto-word">CONTAIN.</span>
          <span class="motto-word">PROTECT.</span>
        </div>
        <div class="site-designation">
          <div class="designation-line"></div>
          <h1 class="site-title">SITE 81: TWILIGHT</h1>
          <div class="designation-line"></div>
        </div>
        <div class="security-clearance">
          <span class="clearance-icon">🛡</span>
          <span class="clearance-text">NIVEL DE ACCESO: 3</span>
          <span class="clearance-icon">🛡</span>
        </div>
      </div>
    </section>

    <!-- Site 81 In-Role Section -->
    <section class="content-section">
      <div class="section-container">
        <div class="section-header">
          <div class="section-number">01</div>
          <h2 class="section-title">SITE 81 - PROTOCOLO DE OPERACIONES</h2>
          <div class="section-classification">CLASIFICADO - NIVEL 3</div>
        </div>
        <div class="section-content">
          <div class="text-card">
            <div class="card-header">
              <div class="card-icon">📋</div>
              <h3 class="card-title">DESCRIPCIÓN OPERATIVA</h3>
            </div>
            <div class="card-content">
              <p class="card-text">
                Site 81 opera como una instalación de contención secundaria bajo la jurisdicción del Sector-28. 
                Especializado en entidades de clase Euclid y Keter con propiedades temporales o dimensionales atenuadas. 
                La instalación mantiene protocolos de cuarentena extendida y sistemas de monitoreo de realidad en tiempo real.
              </p>
              <p class="card-text">
                La infraestructura principal incluye 12 cámaras de contención de nivel 4, 3 laboratorios de investigación temporal 
                y un sistema de redundancia dimensional que opera las 24 horas del día. Todo el personal debe someterse a evaluaciones 
                de realidad cada 72 horas y llevar dispositivos de anclaje dimensional en todo momento.
              </p>
            </div>
            <div class="card-footer">
              <div class="status-indicators">
                <div class="status-item">
                  <div class="status-light active"></div>
                  <span class="status-text">CONTENCIÓN: ESTABLE</span>
                </div>
                <div class="status-item">
                  <div class="status-light active"></div>
                  <span class="status-text">REALIDAD: ANCLADA</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Site Twilight Off-Role Section -->
    <section class="content-section secondary">
      <div class="section-container">
        <div class="section-header">
          <div class="section-number">02</div>
          <h2 class="section-title">SITE TWILIGHT - INFRAESTRUCTURA</h2>
          <div class="section-classification">RESTRINGIDO - NIVEL 2</div>
        </div>
        <div class="section-content">
          <div class="text-card">
            <div class="card-header">
              <div class="card-icon">🏢</div>
              <h3 class="card-title">PLATAFORMA DE ROLEPLAY</h3>
            </div>
            <div class="card-content">
              <p class="card-text">
                Site Twilight es una plataforma de roleplay dedicada a la recreación de experiencias dentro del universo SCP. 
                Ofrecemos un entorno inmersivo donde los usuarios pueden participar en narrativas colaborativas, desarrollar personajes 
                únicos y explorar escenarios inspirados en la Fundación SCP.
              </p>
              <p class="card-text">
                Nuestra plataforma utiliza tecnología moderna para proporcionar una experiencia fluida y accesible desde cualquier dispositivo. 
                Con integración de Discord para comunicación en tiempo real, sistema de personajes personalizables y eventos regulares 
                organizados por nuestro equipo de administración.
              </p>
            </div>
            <div class="card-footer">
              <div class="action-buttons">
                <a href="https://discord.com/invite/37BrVa6b8E" target="_blank" class="discord-button">
                  <span class="button-icon">🎮</span>
                  <span class="button-text">UNIRSE AL DISCORD</span>
                </a>
                <button class="info-button">
                  <span class="button-icon">ℹ</span>
                  <span class="button-text">MÁS INFORMACIÓN</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Site Functions Section -->
    <section class="functions-section">
      <div class="section-container">
        <div class="section-header">
          <div class="section-number">03</div>
          <h2 class="section-title">FUNCIONES DEL SITIO</h2>
          <div class="section-classification">ACCESO: TODO EL PERSONAL</div>
        </div>
        
        <div class="functions-grid">
          <!-- Card 1 -->
          <div class="function-card">
            <div class="card-icon">👤</div>
            <h3 class="card-title">SISTEMA DE PERSONAJES</h3>
            <p class="card-description">
              Crea y gestiona múltiples personajes con perfiles detallados, historias personalizadas y estadísticas únicas.
            </p>
            <div class="card-status">
              <div class="status-light active"></div>
              <span class="status-text">OPERATIVO</span>
            </div>
          </div>

          <!-- Card 2 -->
          <div class="function-card">
            <div class="card-icon">💬</div>
            <h3 class="card-title">ROLEPLAY EN TIEMPO REAL</h3>
            <p class="card-description">
              Participa en sesiones de roleplay sincronizadas con otros usuarios en canales temáticos organizados.
            </p>
            <div class="card-status">
              <div class="status-light active"></div>
              <span class="status-text">ACTIVO</span>
            </div>
          </div>

          <!-- Card 3 -->
          <div class="function-card">
            <div class="card-icon">📖</div>
            <h3 class="card-title">BIBLIOTECA SCP</h3>
            <p class="card-description">
              Accede a una base de datos extensa de artículos SCP, historias canónicas y documentación de la Fundación.
            </p>
            <div class="card-status">
              <div class="status-light"></div>
              <span class="status-text">EN DESARROLLO</span>
            </div>
          </div>

          <!-- Card 4 -->
          <div class="function-card">
            <div class="card-icon">🎭</div>
            <h3 class="card-title">EVENTOS PROGRAMADOS</h3>
            <p class="card-description">
              Participa en eventos especiales, misiones grupales y narrativas organizadas por el equipo de administración.
            </p>
            <div class="card-status">
              <div class="status-light active"></div>
              <span class="status-text">OPERATIVO</span>
            </div>
          </div>

          <!-- Card 5 -->
          <div class="function-card">
            <div class="card-icon">⚙️</div>
            <h3 class="card-title">SISTEMA DE RANGOS</h3>
            <p class="card-description">
              Progresión estructurada con rangos de la Fundación, permisos escalonados y responsabilidades asignadas.
            </p>
            <div class="card-status">
              <div class="status-light active"></div>
              <span class="status-text">ACTIVO</span>
            </div>
          </div>

          <!-- Card 6 -->
          <div class="function-card">
            <div class="card-icon">🔧</div>
            <h3 class="card-title">HERRAMIENTAS DE CREACIÓN</h3>
            <p class="card-description">
              Conjunto de herramientas para crear artículos SCP originales, historias colaborativas y contenido canónico.
            </p>
            <div class="card-status">
              <div class="status-light"></div>
              <span class="status-text">PRÓXIMAMENTE</span>
            </div>
          </div>

          <!-- Card 7 -->
          <div class="function-card">
            <div class="card-icon">📊</div>
            <h3 class="card-title">PANEL DE CONTROL</h3>
            <p class="card-description">
              Interfaz personalizable para gestionar personajes, seguir progreso y acceder a funciones avanzadas.
            </p>
            <div class="card-status">
              <div class="status-light active"></div>
              <span class="status-text">OPERATIVO</span>
            </div>
          </div>

          <!-- Card 8 -->
          <div class="function-card">
            <div class="card-icon">🛡️</div>
            <h3 class="card-title">SISTEMA DE SEGURIDAD</h3>
            <p class="card-description">
              Protocolos de moderación avanzados, verificación de contenido y protección contra conducta inapropiada.
            </p>
            <div class="card-status">
              <div class="status-light active"></div>
              <span class="status-text">ACTIVO</span>
            </div>
          </div>
        </div>

        <div class="section-footer">
          <div class="footer-note">
            <span class="note-icon">📌</span>
            <span class="note-text">TODAS LAS FUNCIONES SUJETAS A ACTUALIZACIONES PERIÓDICAS</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer Section -->
    <section class="document-footer">
      <div class="footer-line"></div>
      <div class="footer-text">
        <span>FIN DEL DOCUMENTO DE INTRODUCCIÓN</span>
        <span>CONFIDENCIAL - ACCESO NO AUTORIZADO PROHIBIDO</span>
      </div>
    </section>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue"

const message = ref("Cargando sistema...")

onMounted(() => {
  message.value = "Bienvenido a Site Twilight"
})
</script>

<style scoped>
/* Base mobile styles - mobile first */
.landing-page {
  position: relative;
  min-height: 100vh;
  padding: 1rem;
  color: #d8d8d8;
  background: #0a0a0a;
  overflow-x: hidden;
  font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
  line-height: 1.6;
}

/* Site Background (mismo que Privacy.vue) */
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
  background-size: 60px 60px;
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
  background-size: 50px 50px;
}

.scan-line {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, 
    transparent 0%, 
    rgba(80, 80, 80, 0.8) 10%, 
    rgba(120, 120, 120, 0.9) 50%, 
    rgba(80, 80, 80, 0.8) 90%, 
    transparent 100%);
  animation: scan 8s linear infinite;
  z-index: 1;
  opacity: 0.3;
}

@keyframes scan {
  0% { top: 0%; }
  100% { top: 100%; }
}

@keyframes gridMove {
  0% { transform: translateY(0); }
  100% { transform: translateY(60px); }
}

/* Hero Section */
.hero-section {
  position: relative;
  padding: 4rem 1rem 2rem;
  text-align: center;
  z-index: 1;
}

.hero-container {
  max-width: 800px;
  margin: 0 auto;
}

.logo-container {
  position: relative;
  margin: 0 auto 2rem;
  width: 200px;
  height: 200px;
}

.scp-logo {
  width: 100%;
  height: 100%;
  object-fit: contain;
  filter: grayscale(0.3) brightness(1.2);
  position: relative;
  z-index: 2;
}

.logo-shadow {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 50%;
  background: linear-gradient(to top, 
    rgba(0, 0, 0, 0.8) 0%, 
    rgba(0, 0, 0, 0.4) 50%, 
    transparent 100%);
  z-index: 3;
  border-radius: 50%;
}

.hero-motto {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 2rem;
}

.motto-word {
  font-size: 1.8rem;
  font-weight: 700;
  letter-spacing: 3px;
  color: #ffffff;
  text-transform: uppercase;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
  font-family: 'Courier New', monospace;
}

.site-designation {
  margin-bottom: 1.5rem;
}

.designation-line {
  height: 1px;
  background: linear-gradient(90deg, transparent, #555, transparent);
  margin: 1rem auto;
  width: 80%;
}

.site-title {
  font-size: 2rem;
  font-weight: 300;
  letter-spacing: 2px;
  color: #ffffff;
  text-transform: uppercase;
  margin: 1rem 0;
}

.security-clearance {
  display: inline-flex;
  align-items: center;
  gap: 1rem;
  padding: 0.8rem 1.5rem;
  background: rgba(30, 30, 30, 0.7);
  border: 1px solid #444;
  border-radius: 2px;
}

.clearance-icon {
  font-size: 1rem;
  color: #aaa;
}

.clearance-text {
  font-size: 0.9rem;
  color: #ddd;
  letter-spacing: 1px;
  text-transform: uppercase;
}

/* Content Sections */
.content-section {
  position: relative;
  padding: 2rem 1rem;
  z-index: 1;
}

.content-section.secondary {
  background: rgba(15, 15, 15, 0.5);
  border-top: 1px solid #333;
  border-bottom: 1px solid #333;
}

.section-container {
  max-width: 900px;
  margin: 0 auto;
}

.section-header {
  text-align: center;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #333;
}

.section-number {
  font-size: 3rem;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.1);
  margin-bottom: 0.5rem;
  font-family: 'Courier New', monospace;
}

.section-title {
  font-size: 1.4rem;
  font-weight: 600;
  color: #e0e0e0;
  letter-spacing: 1px;
  text-transform: uppercase;
  margin: 0.5rem 0;
}

.section-classification {
  font-size: 0.8rem;
  color: #888;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-top: 0.5rem;
}

.section-content {
  width: 100%;
}

/* Text Cards */
.text-card {
  background: rgba(25, 25, 25, 0.7);
  border: 1px solid #444;
  border-radius: 2px;
  padding: 1.5rem;
  width: 100%;
  box-sizing: border-box;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
  padding-bottom: 0.8rem;
  border-bottom: 1px solid #333;
}

.card-icon {
  font-size: 1.5rem;
  color: #aaa;
}

.card-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: #ddd;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0;
}

.card-content {
  margin-bottom: 1.5rem;
}

.card-text {
  color: #ccc;
  line-height: 1.6;
  margin-bottom: 1rem;
  text-align: justify;
}

.card-text:last-child {
  margin-bottom: 0;
}

/* Status Indicators */
.status-indicators {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.status-item {
  display: flex;
  align-items: center;
  gap: 0.8rem;
}

.status-light {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #333;
  flex-shrink: 0;
}

.status-light.active {
  background: #00ff00;
  box-shadow: 0 0 8px #00ff00;
  animation: pulse 2s infinite;
}

.status-text {
  font-size: 0.9rem;
  color: #aaa;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.5px;
}

/* Action Buttons */
.action-buttons {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.discord-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.8rem;
  padding: 1rem 1.5rem;
  background: rgba(114, 137, 218, 0.2);
  border: 1px solid rgba(114, 137, 218, 0.4);
  color: #d8d8d8;
  text-decoration: none;
  border-radius: 2px;
  transition: all 0.3s ease;
  font-size: 0.95rem;
  font-weight: 500;
  letter-spacing: 0.5px;
}

.discord-button:hover {
  background: rgba(114, 137, 218, 0.3);
  border-color: rgba(114, 137, 218, 0.6);
  transform: translateY(-2px);
}

.info-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.8rem;
  padding: 1rem 1.5rem;
  background: rgba(60, 60, 60, 0.3);
  border: 1px solid #555;
  color: #d8d8d8;
  border-radius: 2px;
  transition: all 0.3s ease;
  font-size: 0.95rem;
  font-weight: 500;
  letter-spacing: 0.5px;
  cursor: pointer;
  width: 100%;
}

.info-button:hover {
  background: rgba(70, 70, 70, 0.4);
  border-color: #666;
  transform: translateY(-2px);
}

.button-icon {
  font-size: 1.1rem;
}

.button-text {
  text-transform: uppercase;
}

/* Functions Section */
.functions-section {
  position: relative;
  padding: 2rem 1rem;
  z-index: 1;
}

.functions-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
  margin: 2rem 0;
}

.function-card {
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  border-radius: 2px;
  padding: 1.5rem;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.function-card:hover {
  background: rgba(40, 40, 40, 0.7);
  border-color: #666;
  transform: translateY(-3px);
}

.function-card .card-icon {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.function-card .card-title {
  font-size: 1rem;
  margin-bottom: 1rem;
  color: #ddd;
}

.card-description {
  color: #bbb;
  font-size: 0.9rem;
  line-height: 1.5;
  margin-bottom: 1.5rem;
  flex: 1;
}

.card-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: rgba(20, 20, 20, 0.7);
  border-radius: 2px;
  width: 100%;
  justify-content: center;
}

/* Section Footer */
.section-footer {
  margin-top: 2rem;
  text-align: center;
}

.footer-note {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.8rem 1.5rem;
  background: rgba(40, 30, 0, 0.3);
  border: 1px solid #aa8800;
  border-radius: 2px;
}

.note-icon {
  color: #ffcc00;
  font-size: 1rem;
}

.note-text {
  font-size: 0.8rem;
  color: #ddd;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

/* Document Footer */
.document-footer {
  position: relative;
  margin-top: 3rem;
  padding-top: 2rem;
  text-align: center;
  z-index: 1;
  border-top: 1px solid #333;
}

.footer-line {
  height: 1px;
  background: linear-gradient(90deg, transparent, #555, transparent);
  margin-bottom: 1.2rem;
}

.footer-text {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  font-size: 0.8rem;
  color: #777;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

/* Tablet styles */
@media (min-width: 640px) {
  .landing-page {
    padding: 1.5rem;
  }
  
  .hero-section {
    padding: 5rem 2rem 3rem;
  }
  
  .logo-container {
    width: 250px;
    height: 250px;
  }
  
  .motto-word {
    font-size: 2.2rem;
  }
  
  .site-title {
    font-size: 2.5rem;
  }
  
  .section-title {
    font-size: 1.6rem;
  }
  
  .action-buttons {
    flex-direction: row;
    justify-content: center;
  }
  
  .discord-button,
  .info-button {
    min-width: 200px;
  }
  
  .functions-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .footer-text {
    flex-direction: row;
    justify-content: space-between;
  }
}

/* Desktop styles */
@media (min-width: 1024px) {
  .landing-page {
    padding: 2rem;
  }
  
  .hero-section {
    padding: 6rem 2rem 4rem;
  }
  
  .logo-container {
    width: 300px;
    height: 300px;
  }
  
  .motto-word {
    font-size: 2.8rem;
  }
  
  .hero-motto {
    flex-direction: row;
    justify-content: center;
    gap: 2rem;
  }
  
  .site-title {
    font-size: 3rem;
  }
  
  .content-section,
  .functions-section {
    padding: 3rem 2rem;
  }
  
  .section-title {
    font-size: 1.8rem;
  }
  
  .text-card {
    padding: 2rem;
  }
  
  .functions-grid {
    grid-template-columns: repeat(4, 1fr);
  }
  
  .function-card {
    padding: 2rem;
  }
}

/* Large Desktop styles */
@media (min-width: 1400px) {
  .hero-container,
  .section-container {
    max-width: 1200px;
  }
  
  .motto-word {
    font-size: 3.2rem;
  }
  
  .site-title {
    font-size: 3.5rem;
  }
}
</style>