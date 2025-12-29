<template>
  <div class="error-page">
    <!-- Fondo SCP -->
    <div class="site-background">
      <div class="grid-overlay"></div>
      <div class="scan-line"></div>
      <div class="particles"></div>
    </div>

    <!-- Error Content Section -->
    <section class="content-section">
      <div class="section-content">
        <div class="section-header">
          <div class="section-number">ERROR</div>
          <h2 class="section-title">CÓDIGO 404 - RECURSO NO ENCONTRADO</h2>
          <div class="section-classification">RESTRINGIDO - NIVEL 2</div>
        </div>
        
        <div class="error-card">
          <div class="card-header">
            <div class="error-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="15" y1="9" x2="9" y2="15"></line>
                <line x1="9" y1="9" x2="15" y2="15"></line>
              </svg>
            </div>
            <h3 class="card-title">LOCALIZACIÓN DE DOCUMENTO FALLIDA</h3>
          </div>
          
          <div class="card-body">
            <p class="card-text">
              El recurso solicitado no ha sido localizado dentro de los registros de la Fundación SCP. 
              La ruta especificada puede haber sido reasignada, clasificada o eliminada por protocolos de seguridad.
            </p>
            
            <div class="error-details">
              <div class="detail-item">
                <div class="detail-label">CÓDIGO DE ERROR:</div>
                <div class="detail-value">404-NF</div>
              </div>
              <div class="detail-item">
                <div class="detail-label">TIPO DE FALLO:</div>
                <div class="detail-value">LOCALIZACIÓN</div>
              </div>
              <div class="detail-item">
                <div class="detail-label">TIEMPO:</div>
                <div class="detail-value">{{ currentTime }}</div>
              </div>
            </div>

            <p class="card-text warning">
              ADVERTENCIA: Los intentos repetidos de acceder a recursos no autorizados pueden resultar 
              en la revocación de privilegios de acceso y acciones disciplinarias.
            </p>
          </div>
          
          <div class="card-footer">
            <div class="status-indicators">
              <!-- CORRECCIÓN: Ambos botones del mismo tamaño -->
              <div class="status-item">
                <div class="status-light"></div>
                <span class="status-text">CONEXIÓN: INTERRUMPIDA</span>
              </div>
              <div class="status-item">
                <div class="status-light active"></div>
                <span class="status-text">SEGURIDAD: ACTIVA</span>
              </div>
            </div>
            
            <div class="action-buttons">
              <button class="primary-button" @click="goHome">
                <div class="button-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                    <polyline points="9 22 9 12 15 12 15 22"></polyline>
                  </svg>
                </div>
                <span class="button-text">VOLVER AL INICIO</span>
              </button>
              
              <button class="secondary-button" @click="goBack">
                <div class="button-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M19 12H5"></path>
                    <path d="M12 19l-7-7 7-7"></path>
                  </svg>
                </div>
                <span class="button-text">PÁGINA ANTERIOR</span>
              </button>
            </div>
            
            <div class="protocol-section">
              <div class="protocol-header">
                <div class="protocol-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                    <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
                  </svg>
                </div>
                <h4 class="protocol-title">PROTOCOLO DE ACCIÓN RECOMENDADO</h4>
              </div>
              <ol class="protocol-steps">
                <li>Verificar la dirección del recurso solicitado</li>
                <li>Contactar con administración si el error persiste</li>
                <li>Reportar anomalías de navegación al departamento técnico</li>
                <li>Mantener registro del incidente para auditoría</li>
              </ol>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer Section -->
    <section class="document-footer">
      <div class="footer-line"></div>
      <div class="footer-text">
        <span>DOCUMENTO DE ERROR 404 GENERADO AUTOMÁTICAMENTE</span>
        <span>CONFIDENCIAL - ACCESO NO AUTORIZADO PROHIBIDO</span>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const currentTime = ref('')

const updateTime = () => {
  const now = new Date()
  const options = { 
    year: 'numeric', 
    month: '2-digit', 
    day: '2-digit',
    hour: '2-digit', 
    minute: '2-digit', 
    second: '2-digit',
    hour12: false
  }
  currentTime.value = now.toLocaleString('es-ES', options).replace(',', '')
}

const goHome = () => {
  router.push('/')
}

const goBack = () => {
  if (window.history.length > 1) {
    router.go(-1)
  } else {
    goHome()
  }
}

onMounted(() => {
  updateTime()
  const timer = setInterval(updateTime, 1000)
  
  onUnmounted(() => {
    clearInterval(timer)
  })
})
</script>

<style scoped>
/* Reset y base */
.error-page {
  position: relative;
  min-height: 100vh;
  color: #d8d8d8;
  background: #0a0a0a;
  overflow-x: hidden;
  font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
  line-height: 1.6;
  width: 100%;
  box-sizing: border-box;
  padding-top: 80px; /* Espacio para el header */
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

/* Secciones comunes */
.content-section {
  position: relative;
  z-index: 1;
  width: 100%;
  display: flex;
  justify-content: center;
  padding: 2rem 0;
  min-height: calc(100vh - 80px); /* Altura menos el header */
  align-items: center;
}

/* Contenedor común */
.section-content {
  width: 100%;
  max-width: calc(100vw - 1rem);
  margin: 0 auto;
  padding: 0 0.5rem;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Section Header */
.section-header {
  text-align: center;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #333;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.section-number {
  font-size: 3rem;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.1);
  margin-bottom: 0.5rem;
  font-family: 'Courier New', monospace;
  line-height: 1;
}

.section-title {
  font-size: 1.3rem;
  font-weight: 600;
  color: #e0e0e0;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  margin: 0.5rem 0;
  text-align: center;
  width: 100%;
  box-sizing: border-box;
  line-height: 1.3;
}

.section-classification {
  font-size: 0.75rem;
  color: #888;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-top: 0.5rem;
  text-align: center;
  width: 100%;
}

/* Error Card */
.error-card {
  background: rgba(25, 25, 25, 0.7);
  border: 1px solid #444;
  border-radius: 6px;
  padding: 2rem;
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0 auto;
}

.card-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid #333;
  text-align: center;
  width: 100%;
}

.error-icon {
  width: 80px;
  height: 80px;
  color: #ff4444;
  margin-bottom: 1rem;
  animation: pulseError 2s infinite;
}

@keyframes pulseError {
  0% { opacity: 0.6; }
  50% { opacity: 1; }
  100% { opacity: 0.6; }
}

.card-title {
  font-size: 1.4rem;
  font-weight: 600;
  color: #ff4444;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  margin: 0;
  text-align: center;
  width: 100%;
  line-height: 1.3;
}

.card-body {
  margin-bottom: 2.5rem;
  width: 100%;
}

.card-text {
  color: #ccc;
  line-height: 1.7;
  margin-bottom: 1.5rem;
  text-align: center;
  width: 100%;
  box-sizing: border-box;
  font-size: 1rem;
}

.card-text.warning {
  color: #ffaa44;
  background: rgba(255, 170, 68, 0.1);
  padding: 1rem;
  border-radius: 4px;
  border-left: 3px solid #ffaa44;
  text-align: left;
}

/* Error Details */
.error-details {
  background: rgba(30, 30, 30, 0.5);
  border: 1px solid #444;
  border-radius: 4px;
  padding: 1.5rem;
  margin: 2rem 0;
  width: 100%;
  box-sizing: border-box;
}

.detail-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.8rem 0;
  border-bottom: 1px solid #333;
}

.detail-item:last-child {
  border-bottom: none;
}

.detail-label {
  font-size: 0.9rem;
  color: #aaa;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

.detail-value {
  font-size: 1rem;
  color: #fff;
  font-family: 'Consolas', monospace;
  font-weight: 600;
  letter-spacing: 0.5px;
}

/* Status Indicators - CORREGIDO: Mismo tamaño */
.status-indicators {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width: 100%;
  align-items: center;
  margin: 2rem 0;
}

.status-item {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  width: 100%;
  max-width: 300px;
  padding: 0.8rem 1.2rem;
  background: rgba(30, 30, 30, 0.5);
  border-radius: 4px;
  height: 50px; /* Tamaño fijo para ambos */
  box-sizing: border-box;
  min-width: 280px; /* Ancho mínimo igual */
}

.status-light {
  width: 10px;
  height: 10px;
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
  font-size: 0.95rem;
  color: #aaa;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.8px;
  text-align: center;
  font-weight: 500;
  flex: 1;
  white-space: nowrap;
}

/* Action Buttons */
.action-buttons {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  width: 100%;
  align-items: center;
  margin: 2.5rem 0;
}

.primary-button,
.secondary-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  padding: 1.2rem 1.8rem;
  color: #d8d8d8;
  text-decoration: none;
  border-radius: 4px;
  transition: all 0.3s ease;
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: 0.8px;
  width: 100%;
  max-width: 320px;
  box-sizing: border-box;
  border: none;
  cursor: pointer;
  font-family: inherit;
  height: 54px; /* Tamaño consistente para botones */
  min-width: 280px; /* Ancho mínimo igual que status items */
}

.primary-button {
  background: rgba(114, 137, 218, 0.25);
  border: 1px solid rgba(114, 137, 218, 0.5);
}

.primary-button:hover {
  background: rgba(114, 137, 218, 0.35);
  border-color: rgba(114, 137, 218, 0.7);
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(114, 137, 218, 0.2);
}

.secondary-button {
  background: rgba(60, 60, 60, 0.4);
  border: 1px solid #666;
}

.secondary-button:hover {
  background: rgba(80, 80, 80, 0.5);
  border-color: #777;
  transform: translateY(-3px);
}

.button-icon {
  width: 20px;
  height: 20px;
  color: #d8d8d8;
  opacity: 0.9;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.button-text {
  text-transform: uppercase;
  text-align: center;
  font-weight: 600;
}

/* Protocol Section */
.protocol-section {
  background: rgba(20, 20, 20, 0.8);
  border: 1px solid #444;
  border-radius: 4px;
  padding: 1.5rem;
  margin-top: 2rem;
  width: 100%;
  box-sizing: border-box;
}

.protocol-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #333;
}

.protocol-icon {
  width: 24px;
  height: 24px;
  color: #aaa;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.protocol-title {
  font-size: 1rem;
  color: #ddd;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0;
}

.protocol-steps {
  margin: 0;
  padding-left: 1.5rem;
  color: #ccc;
  line-height: 1.8;
}

.protocol-steps li {
  margin-bottom: 0.8rem;
}

.protocol-steps li:last-child {
  margin-bottom: 0;
}

/* Document Footer */
.document-footer {
  position: relative;
  margin-top: 4rem;
  padding: 2.5rem 0 1.5rem;
  text-align: center;
  z-index: 1;
  border-top: 1px solid #333;
  width: 100%;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: rgba(15, 15, 15, 0.8);
}

.footer-line {
  height: 1px;
  background: linear-gradient(90deg, transparent, #666, transparent);
  margin-bottom: 1.5rem;
  width: 100%;
  max-width: 600px;
}

.footer-text {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  font-size: 0.85rem;
  color: #888;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  width: 100%;
  max-width: 600px;
  align-items: center;
}

.footer-text span {
  text-align: center;
  width: 100%;
  font-weight: 500;
  line-height: 1.5;
}

/* Animations */
@keyframes pulse {
  0% { opacity: 1; }
  50% { opacity: 0.5; }
  100% { opacity: 1; }
}

/* Tablet styles */
@media (min-width: 640px) {
  .section-content {
    max-width: calc(100vw - 4rem);
    padding: 0 2rem;
  }
  
  .section-title {
    font-size: 1.6rem;
  }
  
  .error-card {
    padding: 2.5rem;
    border-radius: 8px;
  }
  
  .card-title {
    font-size: 1.6rem;
  }
  
  .card-text {
    font-size: 1.05rem;
  }
  
  .action-buttons {
    flex-direction: row;
    justify-content: center;
    flex-wrap: wrap;
  }
  
  .primary-button,
  .secondary-button {
    min-width: 240px;
    max-width: 280px;
    padding: 1.3rem 2rem;
    height: 56px; /* Tamaño consistente en tablet */
  }
  
  .status-indicators {
    flex-direction: row;
    justify-content: center;
    gap: 2rem;
  }
  
  .status-item {
    height: 52px; /* Tamaño consistente en tablet */
    min-width: 240px;
  }
  
  .error-details {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
  }
  
  .detail-item {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
    padding: 1rem;
    border-bottom: none;
    border-right: 1px solid #333;
  }
  
  .detail-item:last-child {
    border-right: none;
  }
  
  .footer-text {
    flex-direction: row;
    justify-content: space-between;
    max-width: 800px;
    gap: 1.5rem;
  }
  
  .footer-text span {
    text-align: center;
    flex: 1;
  }
}

/* Desktop styles */
@media (min-width: 1024px) {
  .section-content {
    max-width: 1200px;
    padding: 0 2rem;
  }
  
  .content-section {
    padding: 4rem 0;
  }
  
  .section-title {
    font-size: 1.9rem;
  }
  
  .error-card {
    padding: 3rem;
    border-radius: 10px;
    max-width: 900px;
  }
  
  .card-title {
    font-size: 1.8rem;
  }
  
  .card-text {
    font-size: 1.1rem;
  }
  
  .action-buttons {
    max-width: 900px;
  }
  
  .primary-button,
  .secondary-button {
    max-width: 300px;
    padding: 1.5rem 2.2rem;
    font-size: 1.1rem;
    height: 60px; /* Tamaño consistente en desktop */
  }
  
  .status-item {
    height: 56px; /* Tamaño consistente en desktop */
    max-width: 280px;
  }
}

/* Large Desktop styles */
@media (min-width: 1400px) {
  .section-content {
    max-width: 1400px;
  }
  
  .error-card {
    max-width: 1000px;
  }
  
  .primary-button,
  .secondary-button {
    height: 62px; /* Tamaño consistente en pantallas grandes */
  }
  
  .status-item {
    height: 58px; /* Tamaño consistente en pantallas grandes */
  }
}

/* Mobile optimizations */
@media (max-width: 639px) {
  .error-page {
    padding-top: 70px; /* Menos espacio para header en mobile */
  }
  
  .content-section {
    min-height: calc(100vh - 70px);
    padding: 1.5rem 0;
  }
  
  .error-card {
    padding: 1.5rem 1rem;
  }
  
  .card-header {
    padding-bottom: 1rem;
    margin-bottom: 1.5rem;
  }
  
  .error-icon {
    width: 60px;
    height: 60px;
  }
  
  .card-title {
    font-size: 1.2rem;
  }
  
  .detail-label {
    font-size: 0.8rem;
  }
  
  .detail-value {
    font-size: 0.9rem;
  }
  
  .primary-button,
  .secondary-button {
    padding: 1rem 1.5rem;
    height: 50px; /* Tamaño consistente en mobile */
    min-width: 250px;
  }
  
  .status-item {
    height: 48px; /* Tamaño consistente en mobile */
    min-width: 250px;
    padding: 0.6rem 1rem;
  }
  
  .status-text {
    font-size: 0.85rem;
  }
}
</style>