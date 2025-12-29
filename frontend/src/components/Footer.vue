<template>
  <footer class="site-footer">
    <div class="footer-background"></div>
    
    <div class="footer-container">
      <!-- Banner de Clasificación -->
      <div class="classification-banner">
        <div class="classification-text">DOCUMENTACIÓN CLASIFICADA</div>
        <div class="classification-subtext">USO INTERNO EXCLUSIVO - SITE TWILIGHT</div>
      </div>

      <!-- Contenido del Footer -->
      <div class="footer-content">
        <!-- Información del Sitio -->
        <div class="footer-section">
          <div class="section-header">
            <div class="section-icon">🔒</div>
            <h3 class="section-title">INSTALACIÓN SEGURA</h3>
          </div>
          <div class="section-content">
            <p class="facility-description">
              Site Twilight opera bajo protocolos de seguridad estrictos. 
              Todo acceso es monitoreado y registrado.
            </p>
            <div class="protocol-status">
              <div class="protocol-item">
                <div class="protocol-indicator active"></div>
                <span class="protocol-text">SEGURIDAD: ACTIVA</span>
              </div>
              <div class="protocol-item">
                <div class="protocol-indicator active"></div>
                <span class="protocol-text">MONITOREO: HABILITADO</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Enlaces Rápidos -->
        <div class="footer-section">
          <div class="section-header">
            <div class="section-icon">📄</div>
            <h3 class="section-title">DOCUMENTACIÓN</h3>
          </div>
          <div class="section-content">
            <div class="document-links">
              <a href="/privacy" class="document-link">
                <span class="link-icon">📋</span>
                <span class="link-text">Protocolo de Privacidad</span>
              </a>
              <a href="/terms-of-service" class="document-link">
                <span class="link-icon">⚖</span>
                <span class="link-text">Términos de Servicio</span>
              </a>
            </div>
          </div>
        </div>

        <!-- Enlaces del Sistema -->
        <div class="footer-section">
          <div class="section-header">
            <div class="section-icon">🔗</div>
            <h3 class="section-title">ENLACES DEL SISTEMA</h3>
          </div>
          <div class="section-content">
            <div class="system-links">
              <a href="#" class="system-link">
                <span class="link-icon">📊</span>
                <span class="link-text">Marcador 1</span>
              </a>
              <a href="#" class="system-link">
                <span class="link-icon">🔧</span>
                <span class="link-text">Marcador 2</span>
              </a>
              <a href="#" class="system-link">
                <span class="link-icon">📈</span>
                <span class="link-text">Marcador 3</span>
              </a>
              <a href="#" class="system-link">
                <span class="link-icon">📁</span>
                <span class="link-text">Marcador 4</span>
              </a>
            </div>
          </div>
        </div>

        <!-- Contacto -->
        <div class="footer-section">
          <div class="section-header">
            <div class="section-icon">📞</div>
            <h3 class="section-title">COMUNICACIONES</h3>
          </div>
          <div class="section-content">
            <div class="contact-info">
              <a href="https://discord.com/invite/37BrVa6b8E" target="_blank" class="contact-link">
                <span class="contact-icon">🎮</span>
                <span class="contact-text">Canal de Discord</span>
              </a>
              <div class="security-notice">
                <span class="notice-icon">⚠</span>
                <span class="notice-text">Reportar problemas de seguridad inmediatamente</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Parte Inferior del Footer -->
      <div class="footer-bottom">
        <div class="footer-divider"></div>
        <div class="bottom-content">
          <div class="copyright">
            <span class="copyright-symbol">©</span>
            <span class="copyright-text">2025 SITE TWILIGHT. TODOS LOS DERECHOS RESERVADOS.</span>
          </div>
          <div class="security-level">
            <span class="level-icon">🛡</span>
            <span class="level-text">NIVEL DE SEGURIDAD: CLASIFICADO</span>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
// No se necesita lógica específica para este footer básico
</script>

<style scoped>
/* Base mobile styles - mobile first */
.site-footer {
  background: rgba(10, 10, 10, 0.95);
  border-top: 1px solid #333;
  position: relative;
  backdrop-filter: blur(10px);
  width: 100%;
  left: 0;
  right: 0;
  margin-top: auto;
  flex-shrink: 0;
}

.footer-background {
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

.footer-container {
  width: 100%;
  position: relative;
  padding: 1.5rem 1rem;
  box-sizing: border-box;
  max-width: 100%;
  overflow: hidden;
}

/* Banner de Clasificación */
.classification-banner {
  background: linear-gradient(90deg, #222, #333, #222);
  padding: 0.8rem;
  text-align: center;
  border: 1px solid #444;
  border-radius: 2px;
  margin-bottom: 1.5rem;
  width: 100%;
  box-sizing: border-box;
}

.classification-text {
  font-size: 0.8rem;
  font-weight: bold;
  letter-spacing: 1px;
  color: #aaa;
  text-transform: uppercase;
  margin-bottom: 0.3rem;
  word-break: break-word;
}

.classification-subtext {
  font-size: 0.7rem;
  color: #888;
  letter-spacing: 0.5px;
  word-break: break-word;
}

/* Grid del Contenido del Footer */
.footer-content {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
  width: 100%;
  box-sizing: border-box;
}

/* Secciones del Footer */
.footer-section {
  background: rgba(25, 25, 25, 0.6);
  border: 1px solid #444;
  border-radius: 2px;
  padding: 1rem;
  width: 100%;
  box-sizing: border-box;
  overflow: hidden;
}

.section-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.8rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid #333;
  width: 100%;
  box-sizing: border-box;
}

.section-icon {
  font-size: 1rem;
  color: #aaa;
  flex-shrink: 0;
}

.section-title {
  font-size: 0.9rem;
  font-weight: 600;
  color: #e0e0e0;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin: 0;
  word-break: break-word;
  overflow-wrap: break-word;
}

.section-content {
  padding-left: 0.5rem;
  width: 100%;
  box-sizing: border-box;
}

/* Descripción de la Instalación */
.facility-description {
  font-size: 0.8rem;
  color: #ccc;
  line-height: 1.5;
  margin-bottom: 1rem;
  word-break: break-word;
  overflow-wrap: break-word;
}

/* Estado del Protocolo */
.protocol-status {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  width: 100%;
}

.protocol-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  width: 100%;
}

.protocol-indicator {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #333;
  flex-shrink: 0;
}

.protocol-indicator.active {
  background: #00ff00;
  box-shadow: 0 0 5px #00ff00;
  animation: pulse 2s infinite;
}

.protocol-text {
  font-size: 0.75rem;
  color: #aaa;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.5px;
  word-break: break-word;
}

/* Enlaces de Documentación */
.document-links {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  width: 100%;
}

.document-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.6rem 0.8rem;
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  border-radius: 2px;
  color: #d8d8d8;
  text-decoration: none;
  transition: all 0.3s ease;
  width: 100%;
  box-sizing: border-box;
  overflow: hidden;
}

.document-link:hover {
  background: rgba(40, 40, 40, 0.8);
  border-color: #666;
  transform: translateY(-1px);
}

.link-icon {
  font-size: 0.9rem;
  opacity: 0.9;
  flex-shrink: 0;
}

.link-text {
  font-size: 0.85rem;
  font-weight: 500;
  word-break: break-word;
  overflow-wrap: break-word;
}

/* Enlaces del Sistema */
.system-links {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0.6rem;
  width: 100%;
}

.system-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0.8rem;
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  border-radius: 2px;
  color: #d8d8d8;
  text-decoration: none;
  transition: all 0.3s ease;
  width: 100%;
  box-sizing: border-box;
  overflow: hidden;
}

.system-link:hover {
  background: rgba(40, 40, 40, 0.8);
  border-color: #666;
}

/* Información de Contacto */
.contact-info {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  width: 100%;
}

.contact-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.6rem 0.8rem;
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  border-radius: 2px;
  color: #d8d8d8;
  text-decoration: none;
  transition: all 0.3s ease;
  width: 100%;
  box-sizing: border-box;
  overflow: hidden;
}

.contact-link:hover {
  background: rgba(40, 40, 40, 0.8);
  border-color: #666;
  transform: translateY(-1px);
}

.contact-icon {
  font-size: 0.9rem;
  flex-shrink: 0;
}

.contact-text {
  font-size: 0.85rem;
  font-weight: 500;
  word-break: break-word;
  overflow-wrap: break-word;
}

.security-notice {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.6rem;
  background: rgba(40, 30, 0, 0.3);
  border: 1px solid #aa8800;
  border-radius: 2px;
  width: 100%;
  box-sizing: border-box;
  overflow: hidden;
}

.notice-icon {
  color: #ffcc00;
  font-size: 0.9rem;
  flex-shrink: 0;
}

.notice-text {
  font-size: 0.75rem;
  color: #ddd;
  letter-spacing: 0.5px;
  word-break: break-word;
  overflow-wrap: break-word;
}

/* Parte Inferior del Footer */
.footer-bottom {
  margin-top: 1.5rem;
  width: 100%;
}

.footer-divider {
  height: 1px;
  background: linear-gradient(90deg, transparent, #555, transparent);
  margin-bottom: 1rem;
  width: 100%;
}

.bottom-content {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  text-align: center;
  width: 100%;
}

.copyright {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  width: 100%;
  flex-wrap: wrap;
}

.copyright-symbol {
  font-size: 0.9rem;
  color: #888;
  flex-shrink: 0;
}

.copyright-text {
  font-size: 0.8rem;
  color: #777;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  word-break: break-word;
  overflow-wrap: break-word;
}

.security-level {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  border-radius: 2px;
  margin: 0 auto;
  max-width: 300px;
  width: 100%;
  box-sizing: border-box;
}

.level-icon {
  font-size: 0.8rem;
  color: #aaa;
  flex-shrink: 0;
}

.level-text {
  font-size: 0.75rem;
  color: #aaa;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  word-break: break-word;
  overflow-wrap: break-word;
}

/* Animación */
@keyframes pulse {
  0% { opacity: 0.6; }
  50% { opacity: 1; }
  100% { opacity: 0.6; }
}

/* Estilos para Tablet */
@media (min-width: 640px) {
  .footer-container {
    padding: 2rem 1.5rem;
  }
  
  .footer-content {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
  }
  
  .classification-text {
    font-size: 0.85rem;
  }
  
  .section-title {
    font-size: 0.95rem;
  }
  
  .bottom-content {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    text-align: left;
  }
  
  .security-level {
    margin: 0;
    max-width: none;
    width: auto;
  }
}

/* Estilos para Desktop */
@media (min-width: 1024px) {
  .site-footer {
    width: 100vw;
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
  }
  
  .footer-container {
    padding: 2.5rem 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .footer-content {
    grid-template-columns: repeat(4, 1fr);
    gap: 2rem;
  }
  
  .footer-section {
    padding: 1.2rem;
  }
  
  .system-links {
    grid-template-columns: 1fr;
  }
  
  .classification-banner {
    padding: 1rem;
    margin-bottom: 2rem;
  }
  
  .classification-text {
    font-size: 0.9rem;
  }
  
  .classification-subtext {
    font-size: 0.75rem;
  }
  
  .copyright {
    flex-wrap: nowrap;
  }
}

/* Para pantallas muy grandes */
@media (min-width: 1400px) {
  .footer-container {
    max-width: 1400px;
  }
}
</style>