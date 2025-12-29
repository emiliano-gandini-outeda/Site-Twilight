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
            <span class="section-emoji">🔒</span>
            <div class="section-icon-svg">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
              </svg>
            </div>
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
            <span class="section-emoji">📄</span>
            <div class="section-icon-svg">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14 2 14 8 20 8"></polyline>
                <line x1="16" y1="13" x2="8" y2="13"></line>
                <line x1="16" y1="17" x2="8" y2="17"></line>
                <polyline points="10 9 9 9 8 9"></polyline>
              </svg>
            </div>
            <h3 class="section-title">DOCUMENTACIÓN</h3>
          </div>
          <div class="section-content">
            <div class="document-links">
              <a href="/privacy" class="document-link">
                <span class="link-emoji">📋</span>
                <div class="link-icon-svg">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                    <polyline points="14 2 14 8 20 8"></polyline>
                    <line x1="16" y1="13" x2="8" y2="13"></line>
                    <line x1="16" y1="17" x2="8" y2="17"></line>
                  </svg>
                </div>
                <span class="link-text">Protocolo de Privacidad</span>
              </a>
              <a href="/terms-of-service" class="document-link">
                <span class="link-emoji">⚖</span>
                <div class="link-icon-svg">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 15v2"></path>
                    <path d="M12 8v5"></path>
                    <path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"></path>
                  </svg>
                </div>
                <span class="link-text">Términos de Servicio</span>
              </a>
            </div>
          </div>
        </div>

        <!-- Enlaces del Sistema -->
        <div class="footer-section">
          <div class="section-header">
            <span class="section-emoji">🔗</span>
            <div class="section-icon-svg">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
              </svg>
            </div>
            <h3 class="section-title">ENLACES DEL SISTEMA</h3>
          </div>
          <div class="section-content">
            <div class="system-links">
              <a href="#" class="system-link">
                <span class="link-emoji">📊</span>
                <div class="link-icon-svg">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                    <line x1="3" y1="9" x2="21" y2="9"></line>
                    <line x1="9" y1="21" x2="9" y2="9"></line>
                  </svg>
                </div>
                <span class="link-text">Marcador 1</span>
              </a>
              <a href="#" class="system-link">
                <span class="link-emoji">🔧</span>
                <div class="link-icon-svg">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>
                  </svg>
                </div>
                <span class="link-text">Marcador 2</span>
              </a>
              <a href="#" class="system-link">
                <span class="link-emoji">📈</span>
                <div class="link-icon-svg">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="18" y1="20" x2="18" y2="10"></line>
                    <line x1="12" y1="20" x2="12" y2="4"></line>
                    <line x1="6" y1="20" x2="6" y2="14"></line>
                  </svg>
                </div>
                <span class="link-text">Marcador 3</span>
              </a>
              <a href="#" class="system-link">
                <span class="link-emoji">📁</span>
                <div class="link-icon-svg">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
                  </svg>
                </div>
                <span class="link-text">Marcador 4</span>
              </a>
            </div>
          </div>
        </div>

        <!-- Contacto -->
        <div class="footer-section">
          <div class="section-header">
            <span class="section-emoji">📞</span>
            <div class="section-icon-svg">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
              </svg>
            </div>
            <h3 class="section-title">COMUNICACIONES</h3>
          </div>
          <div class="section-content">
            <div class="contact-info">
              <a href="https://discord.com/invite/37BrVa6b8E" target="_blank" class="contact-link">
                <span class="contact-emoji">🎮</span>
                <div class="contact-icon-svg">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path>
                  </svg>
                </div>
                <span class="contact-text">Canal de Discord</span>
              </a>
              <div class="security-notice">
                <span class="notice-emoji">⚠</span>
                <div class="notice-icon-svg">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
                    <line x1="12" y1="9" x2="12" y2="13"></line>
                    <line x1="12" y1="17" x2="12.01" y2="17"></line>
                  </svg>
                </div>
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
            <span class="level-emoji">🛡</span>
            <div class="level-icon-svg">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
              </svg>
            </div>
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

/* Iconos SVG - ocultos por defecto en mobile, visibles en desktop */
.section-icon-svg,
.link-icon-svg,
.contact-icon-svg,
.notice-icon-svg,
.level-icon-svg {
  display: none;
  width: 16px;
  height: 16px;
  color: currentColor;
  flex-shrink: 0;
}

.section-emoji,
.link-emoji,
.contact-emoji,
.notice-emoji,
.level-emoji {
  display: block;
  font-size: 1rem;
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

/* Estado del Protocolo - NORMALIZADO */
.protocol-status {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  width: 100%;
}

.protocol-item {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  width: 100%;
  min-height: 40px;
  padding: 0.6rem 0.8rem;
  background: rgba(30, 30, 30, 0.5);
  border: 1px solid #444;
  border-radius: 2px;
  box-sizing: border-box;
}

.protocol-indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #333;
  flex-shrink: 0;
}

.protocol-indicator.active {
  background: #00ff00;
  box-shadow: 0 0 6px #00ff00;
  animation: pulse 2s infinite;
}

.protocol-text {
  font-size: 0.85rem;
  color: #aaa;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.5px;
  word-break: break-word;
  flex: 1;
}

/* Enlaces de Documentación - NORMALIZADOS */
.document-links {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  width: 100%;
}

.document-link {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 0.8rem 1rem;
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  border-radius: 2px;
  color: #d8d8d8;
  text-decoration: none;
  transition: all 0.3s ease;
  width: 100%;
  box-sizing: border-box;
  overflow: hidden;
  min-height: 48px;
}

.document-link:hover {
  background: rgba(40, 40, 40, 0.8);
  border-color: #666;
  transform: translateY(-2px);
}

.link-text {
  font-size: 0.85rem;
  font-weight: 500;
  word-break: break-word;
  overflow-wrap: break-word;
  flex: 1;
}

/* Enlaces del Sistema - NORMALIZADOS */
.system-links {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0.8rem;
  width: 100%;
}

.system-link {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 0.8rem 1rem;
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  border-radius: 2px;
  color: #d8d8d8;
  text-decoration: none;
  transition: all 0.3s ease;
  width: 100%;
  box-sizing: border-box;
  overflow: hidden;
  min-height: 48px;
}

.system-link:hover {
  background: rgba(40, 40, 40, 0.8);
  border-color: #666;
  transform: translateY(-2px);
}

/* Información de Contacto - NORMALIZADA */
.contact-info {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width: 100%;
}

.contact-link {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 0.8rem 1rem;
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  border-radius: 2px;
  color: #d8d8d8;
  text-decoration: none;
  transition: all 0.3s ease;
  width: 100%;
  box-sizing: border-box;
  overflow: hidden;
  min-height: 48px;
}

.contact-link:hover {
  background: rgba(40, 40, 40, 0.8);
  border-color: #666;
  transform: translateY(-2px);
}

.contact-text {
  font-size: 0.85rem;
  font-weight: 500;
  word-break: break-word;
  overflow-wrap: break-word;
  flex: 1;
}

.security-notice {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 0.8rem 1rem;
  background: rgba(40, 30, 0, 0.3);
  border: 1px solid #aa8800;
  border-radius: 2px;
  width: 100%;
  box-sizing: border-box;
  overflow: hidden;
  min-height: 48px;
}

.notice-text {
  font-size: 0.75rem;
  color: #ddd;
  letter-spacing: 0.5px;
  word-break: break-word;
  overflow-wrap: break-word;
  flex: 1;
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
  gap: 1rem;
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
  gap: 0.8rem;
  padding: 0.8rem 1rem;
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  border-radius: 2px;
  margin: 0 auto;
  max-width: 300px;
  width: 100%;
  box-sizing: border-box;
  min-height: 48px;
}

.level-text {
  font-size: 0.75rem;
  color: #aaa;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  word-break: break-word;
  overflow-wrap: break-word;
  flex: 1;
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
  
  /* Ajustes de tamaño en tablet */
  .protocol-item,
  .document-link,
  .system-link,
  .contact-link,
  .security-notice,
  .security-level {
    min-height: 44px;
    padding: 0.7rem 0.9rem;
  }
  
  .protocol-text,
  .link-text,
  .contact-text {
    font-size: 0.9rem;
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
  
  /* Mostrar SVG y ocultar emojis en desktop */
  .section-emoji,
  .link-emoji,
  .contact-emoji,
  .notice-emoji,
  .level-emoji {
    display: none;
  }
  
  .section-icon-svg,
  .link-icon-svg,
  .contact-icon-svg,
  .notice-icon-svg,
  .level-icon-svg {
    display: block;
  }
  
  /* Ajustes de tamaño en desktop */
  .protocol-item,
  .document-link,
  .system-link,
  .contact-link,
  .security-notice,
  .security-level {
    min-height: 48px;
    padding: 0.8rem 1rem;
  }
  
  .section-icon-svg {
    width: 18px;
    height: 18px;
  }
  
  .link-icon-svg,
  .contact-icon-svg,
  .notice-icon-svg,
  .level-icon-svg {
    width: 16px;
    height: 16px;
  }
}

/* Para pantallas muy grandes */
@media (min-width: 1400px) {
  .footer-container {
    max-width: 1400px;
  }
  
  .protocol-item,
  .document-link,
  .system-link,
  .contact-link,
  .security-notice,
  .security-level {
    min-height: 52px;
    padding: 0.9rem 1.1rem;
  }
  
  .section-icon-svg {
    width: 20px;
    height: 20px;
  }
}

/* Mobile optimizations */
@media (max-width: 639px) {
  .protocol-item,
  .document-link,
  .system-link,
  .contact-link,
  .security-notice,
  .security-level {
    min-height: 42px;
    padding: 0.6rem 0.8rem;
  }
  
  .section-header {
    gap: 0.4rem;
  }
  
  .section-emoji {
    font-size: 0.9rem;
  }
}
</style>