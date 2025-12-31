<template>
  <div class="personajes-page">
    <!-- Fondo SCP -->
    <div class="site-background">
      <div class="grid-overlay"></div>
      <div class="scan-line"></div>
      <div class="particles"></div>
    </div>

    <!-- Header con padding-top de 2rem -->
    <header class="personajes-header">
      <div class="header-content">
        <div class="header-left">
          <div class="header-logo">
            <div class="person-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="#fc6f03" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
              </svg>
            </div>
            <div class="header-title">
              <span class="header-main">AGENT MANAGEMENT</span>
              <span class="header-sub">PERSONNEL CONTROL SYSTEM</span>
            </div>
          </div>
        </div>
        
        <div class="header-right">
          <div class="session-status">
            <div class="session-indicator active"></div>
            <span class="session-text">SESSION ACTIVE</span>
          </div>
          <div class="current-time">
            {{ currentTime }}
          </div>
        </div>
      </div>
    </header>

    <!-- Navegación Principal -->
    <nav class="personajes-nav">
      <div class="nav-controls">
        <button 
          class="nav-button" 
          :class="{ 'active': activeView === 'all' }"
          @click="setActiveView('all')"
        >
          <div class="nav-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
              <circle cx="9" cy="7" r="4"></circle>
              <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
            </svg>
          </div>
          <span class="nav-text">LISTA DE PERSONAL</span>
        </button>
        
        <button 
          class="nav-button" 
          :class="{ 'active': activeView === 'mine' }"
          @click="setActiveView('mine')"
        >
          <div class="nav-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
          </div>
          <span class="nav-text">MIS AGENTES</span>
        </button>
        
        <!-- Placeholders [REDACTED] -->
        <button class="nav-button redacted" v-for="n in 2" :key="n" disabled>
          <div class="nav-icon redacted">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
            </svg>
          </div>
          <span class="nav-text redacted-text">[REDACTED]</span>
        </button>
      </div>
      
      <div class="nav-info">
        <div class="info-item">
          <span class="info-label">USER:</span>
          <span class="info-value">{{ currentUser?.roblox_username || 'GUEST' }}</span>
        </div>
        <div class="info-item">
          <span class="info-label">CLEARANCE:</span>
          <span class="info-value">{{ currentUser?.is_authenticated ? 'LEVEL 2' : 'GUEST' }}</span>
        </div>
        <div class="info-item">
          <span class="info-label">SYSTEM:</span>
          <span class="info-value operational">OPERATIONAL</span>
        </div>
      </div>
    </nav>

    <!-- Contenido Principal -->
    <main class="personajes-main">
      <!-- Overlay de autenticación -->
      <div v-if="!currentUser?.is_authenticated" class="auth-modal-overlay">
        <Login_Required 
          :redirect-path="'/dashboard/personnel/'"
          :user="currentUser"
        />        
      </div>
      <!-- Contenido autenticado -->
      <div v-else class="authenticated-content">
        <!-- Header de la vista actual -->
        <div class="view-header">
          <h2 class="view-title">
            {{ activeView === 'all' ? 'LISTA DE PERSONAL' : 'MIS AGENTES' }}
          </h2>
          <div class="view-subtitle">
            {{ activeView === 'all' ? 'Todos los agentes registrados en Site-81' : 'Tus agentes registrados en Site-81' }}
            <span v-if="pagination.total > 0" class="pagination-info">
              | Página {{ pagination.currentPage }} de {{ pagination.totalPages }} ({{ pagination.total }} agentes)
            </span>
          </div>
        </div>

        <!-- Barra de búsqueda mejorada con fuzzy search -->
        <div class="search-bar">
          <div class="search-container">
            <div class="search-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="11" cy="11" r="8"></circle>
                <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
              </svg>
            </div>
            <input
              v-model="searchQuery"
              @input="handleSearch"
              @focus="showSearchSuggestions = searchQuery.length >= 2 && searchResults.length > 0"
              @blur="setTimeout(() => showSearchSuggestions = false, 200)"
              type="text"
              :placeholder="activeView === 'all' ? 'Buscar por nombre, codename, facción o owner...' : 'Buscar por nombre, codename...'"
              class="search-input"
            />
            
            <!-- Botón para limpiar búsqueda -->
            <button 
              v-if="searchQuery" 
              @click="clearSearch"
              class="search-clear"
              title="Limpiar búsqueda"
            >
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
              </svg>
            </button>
            
            <div class="search-info">
              <!-- Indicador de búsqueda fuzzy -->
              <span v-if="isFuzzySearch && searchQuery" class="fuzzy-indicator" title="Búsqueda inteligente activada">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M13.5 3H12H8"></path>
                  <path d="M17.5 10H19C20.1046 10 21 10.8954 21 12V14C21 15.1046 20.1046 16 19 16H17.5"></path>
                  <path d="M8.62128 3.48561L3.62128 8.48561C3.22399 8.8829 3 9.43038 3 10.0019V14.9978C3 16.1044 3.89543 16.9998 5 16.9998H10.7573C11.3279 16.9998 11.8754 16.7758 12.2727 16.3785L17.2727 11.3785C18.0601 10.5911 18.0601 9.3248 17.2727 8.53738L12.2627 3.52737C11.4753 2.73995 10.209 2.73995 9.42159 3.52737L8.62128 4.32769"></path>
                  <circle cx="18" cy="18" r="3"></circle>
                  <path d="M20 20L22 22"></path>
                </svg>
                INTELIGENTE
              </span>
              
              <div class="search-count" v-if="totalItems > 0">
                {{ totalItems }} {{ totalItems === 1 ? 'agente' : 'agentes' }} encontrados
              </div>
            </div>
          </div>
          
          <!-- Sugerencias de búsqueda -->
          <div v-if="showSearchSuggestions && searchResults.length > 0" class="search-suggestions">
            <div class="suggestion-item">
              <span class="suggestion-label">TIP:</span>
              <span class="suggestion-text">
                Buscando: "<strong>{{ searchQuery }}</strong>" 
                <span v-if="searchResults.length > 0">• Coincidencias: {{ searchResults.length }}</span>
              </span>
            </div>
            <div v-if="searchQuery.length < 3" class="suggestion-item">
              <span class="suggestion-label">TIP:</span>
              <span class="suggestion-text">
                Escribe más de 2 caracteres para mejores resultados
              </span>
            </div>
          </div>
        </div>

        <!-- Botón para añadir nuevo agente (solo en Mis Agentes) -->
        <div class="add-agent-section" v-if="activeView === 'mine' && !showCreateForm && !showEditForm && !selectedCharacter">
          <button class="add-agent-button" @click="showCreateForm = true">
            <div class="add-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="12" y1="5" x2="12" y2="19"></line>
                <line x1="5" y1="12" x2="19" y2="12"></line>
              </svg>
            </div>
            <span class="add-text">REGISTRAR NUEVO AGENTE</span>
          </button>
        </div>

        <!-- NUEVO GRID: Tarjetas mejoradas -->
        <div class="enhanced-cards-container" v-if="!showCreateForm && !showEditForm && !selectedCharacter">
          <div v-if="loading" class="loading-state">
            <div class="loading-spinner"></div>
            <p class="loading-text">Cargando agentes...</p>
          </div>
          
          <div v-else-if="displayedCharacters.length > 0" class="enhanced-cards-grid">
            <div 
              v-for="character in displayedCharacters" 
              :key="character.id"
              class="enhanced-character-card"
              @click="viewCharacter(character)"
            >
              <!-- Header de la tarjeta con gradiente -->
              <div class="card-header">
                <div class="header-gradient"></div>
                <div class="codename-container">
                  <h3 class="character-codename">{{ character.codename }}</h3>
                  <div class="id-badge">ID: #{{ character.id.toString().padStart(6, '0') }}</div>
                </div>
              </div>
              
              <!-- Contenido principal -->
              <div class="card-body">
                <div class="name-row">
                  <div class="name-faction">
                    <h4 class="character-name">{{ character.first_name }} {{ character.last_name }}</h4>
                    <span class="character-faction">{{ character.faction }}</span>
                  </div>
                  <div class="right-info">
                    <div class="info-item">
                      <span class="info-label">EDAD</span>
                      <span class="info-value">{{ character.age || 'N/A' }} años</span>
                    </div>
                    <div class="info-item">
                      <span class="info-label">REGISTRADO</span>
                      <span class="info-value">{{ formatDateShort(character.created_at) }}</span>
                    </div>
                  </div>
                </div>
                
                <div class="owner-id-section">
                  <div class="owner-label">OWNER</div>
                  <div class="owner-name">{{ character.owner_username }} | ID: #{{ character.id.toString().padStart(6, '0') }}</div>
                </div>
              </div>
              
              <!-- Footer de la tarjeta con acciones -->
              <div class="card-footer">
                <div class="status-indicator">
                  <div class="status-dot active"></div>
                  <span class="status-text">ACTIVO</span>
                </div>
                <div class="view-indicator">
                  <span>VER DETALLES</span>
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M5 12h14"></path>
                    <path d="m12 5 7 7-7 7"></path>
                  </svg>
                </div>
              </div>
              
              <!-- Elemento decorativo de esquina -->
              <div class="corner-decoration"></div>
            </div>
          </div>
          
          <div v-else class="empty-state">
            <div class="empty-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="#fc6f03" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
              </svg>
            </div>
            <h3 class="empty-title">
              {{ activeView === 'mine' ? 'No tienes agentes registrados' : 'No se encontraron agentes' }}
            </h3>
            <p class="empty-text" v-if="searchQuery">
              <span v-if="isFuzzySearch">No hay agentes que coincidan con "<strong>{{ searchQuery }}</strong>"</span>
              <span v-else>No hay agentes que coincidan con "{{ searchQuery }}"</span>
            </p>
            <p class="empty-text" v-else>
              {{ activeView === 'mine' ? 'Comienza registrando tu primer agente en el sistema.' : 'No hay agentes registrados en el sistema.' }}
            </p>
            <button v-if="activeView === 'mine'" class="action-button" @click="showCreateForm = true">
              <span class="button-text">REGISTRAR PRIMER AGENTE</span>
              <div class="button-indicator">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="9 18 15 12 9 6"></polyline>
                </svg>
              </div>
            </button>
          </div>

          <!-- Paginación -->
          <div v-if="pagination.totalPages > 1" class="pagination-controls">
            <button 
              class="pagination-button" 
              :disabled="pagination.currentPage === 1"
              @click="changePage(pagination.currentPage - 1)"
            >
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="15 18 9 12 15 6"></polyline>
              </svg>
              <span>ANTERIOR</span>
            </button>
            
            <div class="page-numbers">
              <span class="page-info">Página {{ pagination.currentPage }} de {{ pagination.totalPages }}</span>
            </div>
            
            <button 
              class="pagination-button" 
              :disabled="pagination.currentPage === pagination.totalPages"
              @click="changePage(pagination.currentPage + 1)"
            >
              <span>SIGUIENTE</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="9 18 15 12 9 6"></polyline>
              </svg>
            </button>
          </div>
        </div>

        <!-- Vista: Formulario de creación/edición -->
        <div v-if="showCreateForm || showEditForm" class="form-view">
          <div class="form-header">
            <button class="back-button" @click="closeFormView">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="19" y1="12" x2="5" y2="12"></line>
                <polyline points="12 19 5 12 12 5"></polyline>
              </svg>
              <span>VOLVER</span>
            </button>
            
            <h2 class="form-title">{{ showEditForm ? 'EDITAR AGENTE' : 'REGISTRAR NUEVO AGENTE' }}</h2>
          </div>
          
          <form @submit.prevent="submitCharacterForm" class="character-form">
            <div class="form-section">
              <h3 class="section-title">INFORMACIÓN DE IDENTIDAD</h3>
              <div class="form-grid">
                <div class="form-group">
                  <label class="form-label">Nombre *</label>
                  <input
                    v-model="characterForm.first_name"
                    type="text"
                    class="form-input"
                    required
                  />
                </div>
                
                <div class="form-group">
                  <label class="form-label">Apellido *</label>
                  <input
                    v-model="characterForm.last_name"
                    type="text"
                    class="form-input"
                    required
                  />
                </div>
                
                <div class="form-group">
                  <label class="form-label">País *</label>
                  <input
                    v-model="characterForm.country"
                    type="text"
                    class="form-input"
                    required
                  />
                </div>
                
                <div class="form-group">
                  <label class="form-label">Fecha de Nacimiento *</label>
                  <input
                    v-model="characterForm.birth_date"
                    type="text"
                    class="form-input"
                    placeholder="DD/MM/AAAA"
                    @input="formatBirthDate"
                    required
                  />
                </div>
                
                <div class="form-group">
                  <label class="form-label">Codename *</label>
                  <input
                    v-model="characterForm.codename"
                    type="text"
                    class="form-input"
                    required
                    :disabled="showEditForm"
                  />
                  <div class="form-hint" v-if="showEditForm">El codename no puede ser modificado</div>
                </div>
                
                <div class="form-group">
                  <label class="form-label">Facción *</label>
                  <input
                    v-model="characterForm.faction"
                    type="text"
                    class="form-input"
                    required
                  />
                </div>
              </div>
            </div>
            
            <div class="form-section">
              <h3 class="section-title">DATOS MORPH (al menos uno requerido)</h3>
              <div class="form-grid">
                <div class="form-group">
                  <label class="form-label">Morph</label>
                  <input
                    v-model="characterForm.morph"
                    type="text"
                    class="form-input"
                    placeholder="Ej: Scp173b"
                  />
                </div>
                
                <div class="form-group">
                  <label class="form-label">Hat</label>
                  <input
                    v-model="characterForm.hat"
                    type="text"
                    class="form-input"
                    placeholder="Ej: 1234567890"
                  />
                </div>
                
                <div class="form-group">
                  <label class="form-label">NVG Color (RGB)</label>
                  <div class="color-inputs">
                    <input
                      v-model.number="characterForm.nvg_r"
                      type="number"
                      min="0"
                      max="255"
                      class="color-input"
                      placeholder="R"
                    />
                    <input
                      v-model.number="characterForm.nvg_g"
                      type="number"
                      min="0"
                      max="255"
                      class="color-input"
                      placeholder="G"
                    />
                    <input
                      v-model.number="characterForm.nvg_b"
                      type="number"
                      min="0"
                      max="255"
                      class="color-input"
                      placeholder="B"
                    />
                  </div>
                </div>
                
                <div class="form-group">
                  <label class="form-label">Shirt</label>
                  <input
                    v-model="characterForm.shirt"
                    type="text"
                    class="form-input"
                    placeholder="Ej: 1234567890"
                  />
                </div>
                
                <div class="form-group">
                  <label class="form-label">Pants</label>
                  <input
                    v-model="characterForm.pants"
                    type="text"
                    class="form-input"
                    placeholder="Ej: 1234567890"
                  />
                </div>
                
                <div class="form-group">
                  <label class="form-label">Skin Color (RGB)</label>
                  <div class="color-inputs">
                    <input
                      v-model.number="characterForm.skin_r"
                      type="number"
                      min="0"
                      max="255"
                      class="color-input"
                      placeholder="R"
                    />
                    <input
                      v-model.number="characterForm.skin_g"
                      type="number"
                      min="0"
                      max="255"
                      class="color-input"
                      placeholder="G"
                    />
                    <input
                      v-model.number="characterForm.skin_b"
                      type="number"
                      min="0"
                      max="255"
                      class="color-input"
                      placeholder="B"
                    />
                  </div>
                </div>
                
                <div class="form-group">
                  <label class="form-label">NTag</label>
                  <input
                    v-model="characterForm.ntag"
                    type="text"
                    class="form-input"
                    placeholder="Texto para NTag"
                  />
                </div>
                
                <div class="form-group">
                  <label class="form-label">CNTag Color (RGB)</label>
                  <div class="color-inputs">
                    <input
                      v-model.number="characterForm.cntag_r"
                      type="number"
                      min="0"
                      max="255"
                      class="color-input"
                      placeholder="R"
                    />
                    <input
                      v-model.number="characterForm.cntag_g"
                      type="number"
                      min="0"
                      max="255"
                      class="color-input"
                      placeholder="G"
                    />
                    <input
                      v-model.number="characterForm.cntag_b"
                      type="number"
                      min="0"
                      max="255"
                      class="color-input"
                      placeholder="B"
                    />
                  </div>
                </div>
                
                <div class="form-group">
                  <label class="form-label">RTag</label>
                  <textarea
                    v-model="characterForm.rtag"
                    class="form-textarea"
                    placeholder="Texto para RTag (puede ser largo)"
                    rows="2"
                  ></textarea>
                </div>
                
                <div class="form-group">
                  <label class="form-label">CRTag Color (RGB)</label>
                  <div class="color-inputs">
                    <input
                      v-model.number="characterForm.crtag_r"
                      type="number"
                      min="0"
                      max="255"
                      class="color-input"
                      placeholder="R"
                    />
                    <input
                      v-model.number="characterForm.crtag_g"
                      type="number"
                      min="0"
                      max="255"
                      class="color-input"
                      placeholder="G"
                    />
                    <input
                      v-model.number="characterForm.crtag_b"
                      type="number"
                      min="0"
                      max="255"
                      class="color-input"
                      placeholder="B"
                    />
                  </div>
                </div>
                
                <div class="form-group checkbox-group">
                  <label class="checkbox-label">
                    <input
                      v-model="characterForm.rhat"
                      type="checkbox"
                      class="checkbox-input"
                    />
                    <span class="checkbox-text">RHat Activado</span>
                  </label>
                </div>
              </div>
            </div>
            
            <div class="form-section">
              <h3 class="section-title">LORE Y BIOGRAFÍA (Markdown)</h3>
              <div class="form-group full-width">
                <label class="form-label">Historia del Personaje</label>
                <textarea
                  v-model="characterForm.lore"
                  class="form-textarea lore-textarea"
                  placeholder="Escribe la historia de tu personaje aquí. Puedes usar formato Markdown..."
                  rows="8"
                ></textarea>
                <div class="form-hint">
                  Soporta formato Markdown: **negrita**, *cursiva*, # títulos, - listas, [enlaces](url), > citas
                </div>
              </div>
            </div>
            
            <div class="form-actions">
              <button type="button" class="cancel-button" @click="closeFormView">
                CANCELAR
              </button>
              <button type="submit" class="submit-button" :disabled="submitting || !isFormValid">
                <span v-if="submitting">PROCESANDO...</span>
                <span v-else>{{ showEditForm ? 'ACTUALIZAR AGENTE' : 'REGISTRAR AGENTE' }}</span>
              </button>
            </div>
          </form>
        </div>

        <!-- Vista: Detalle del personaje -->
        <div v-else-if="selectedCharacter" class="detail-view">
          <div class="detail-header">
            <button class="back-button" @click="selectedCharacter = null">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="19" y1="12" x2="5" y2="12"></line>
                <polyline points="12 19 5 12 12 5"></polyline>
              </svg>
              <span>VOLVER</span>
            </button>
            
            <div class="header-actions" v-if="selectedCharacter.is_owner">
              <button class="edit-button" @click="openEditForm">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                  <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                </svg>
                <span>EDITAR</span>
              </button>
              
              <button class="delete-button" @click="confirmDeleteCharacter">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="3 6 5 6 21 6"></polyline>
                  <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                  <line x1="10" y1="11" x2="10" y2="17"></line>
                  <line x1="14" y1="11" x2="14" y2="17"></line>
                </svg>
                <span>ELIMINAR</span>
              </button>
            </div>
          </div>
          
          <div class="detail-content">
            <div class="detail-section">
              <h3 class="section-title">INFORMACIÓN DE IDENTIDAD</h3>
              <div class="detail-grid">
                <div class="detail-item">
                  <span class="detail-label">Codename:</span>
                  <span class="detail-value highlight">{{ selectedCharacter.codename }}</span>
                </div>
                <div class="detail-item">
                  <span class="detail-label">Nombre:</span>
                  <span class="detail-value">{{ selectedCharacter.first_name }} {{ selectedCharacter.last_name }}</span>
                </div>
                <div class="detail-item">
                  <span class="detail-label">País:</span>
                  <span class="detail-value">{{ selectedCharacter.country }}</span>
                </div>
                <div class="detail-item">
                  <span class="detail-label">Edad:</span>
                  <span class="detail-value">{{ selectedCharacter.age || 'N/A' }} años</span>
                </div>
                <div class="detail-item">
                  <span class="detail-label">Facción:</span>
                  <span class="detail-value faction">{{ selectedCharacter.faction }}</span>
                </div>
                <div class="detail-item">
                  <span class="detail-label">Registrado:</span>
                  <span class="detail-value">{{ formatDateDDMMYYYY(selectedCharacter.created_at) }}</span>
                </div>
                <div class="detail-item full-width">
                  <span class="detail-label">Owner:</span>
                  <a 
                    :href="`/users/${selectedCharacter.owner_roblox_id}`" 
                    class="detail-value owner-link"
                  >
                    {{ selectedCharacter.owner_username }}
                  </a>
                  <span class="detail-value id-badge">ID: #{{ selectedCharacter.id.toString().padStart(6, '0') }}</span>
                </div>
              </div>
            </div>
            
            <div class="detail-section" v-if="selectedCharacter.lore">
              <h3 class="section-title">LORE Y BIOGRAFÍA</h3>
              <div class="lore-container">
                <div class="lore-content" v-html="renderMarkdown(selectedCharacter.lore)"></div>
              </div>
            </div>
            
            <div class="detail-section">
              <h3 class="section-title">DATOS MORPH</h3>
              <div class="morph-grid">
                <div class="morph-item" v-if="selectedCharacter.morph">
                  <span class="morph-label">Morph:</span>
                  <span class="morph-value">{{ selectedCharacter.morph }}</span>
                </div>
                <div class="morph-item" v-if="selectedCharacter.hat">
                  <span class="morph-label">Hat:</span>
                  <span class="morph-value">{{ selectedCharacter.hat }}</span>
                </div>
                <div class="morph-item" v-if="selectedCharacter.nvg_color">
                  <span class="morph-label">NVG Color:</span>
                  <div class="color-display">
                    <span class="morph-value">RGB({{ selectedCharacter.nvg_r }}, {{ selectedCharacter.nvg_g }}, {{ selectedCharacter.nvg_b }})</span>
                    <div 
                      class="color-preview" 
                      :style="{ backgroundColor: `rgb(${selectedCharacter.nvg_r}, ${selectedCharacter.nvg_g}, ${selectedCharacter.nvg_b})` }"
                      :title="`RGB(${selectedCharacter.nvg_r}, ${selectedCharacter.nvg_g}, ${selectedCharacter.nvg_b})`"
                    ></div>
                  </div>
                </div>
                <div class="morph-item" v-if="selectedCharacter.shirt">
                  <span class="morph-label">Shirt:</span>
                  <span class="morph-value">{{ selectedCharacter.shirt }}</span>
                </div>
                <div class="morph-item" v-if="selectedCharacter.pants">
                  <span class="morph-label">Pants:</span>
                  <span class="morph-value">{{ selectedCharacter.pants }}</span>
                </div>
                <div class="morph-item" v-if="selectedCharacter.skin_r !== null">
                  <span class="morph-label">Skin Color:</span>
                  <div class="color-display">
                    <span class="morph-value">RGB({{ selectedCharacter.skin_r }}, {{ selectedCharacter.skin_g }}, {{ selectedCharacter.skin_b }})</span>
                    <div 
                      class="color-preview" 
                      :style="{ backgroundColor: `rgb(${selectedCharacter.skin_r}, ${selectedCharacter.skin_g}, ${selectedCharacter.skin_b})` }"
                      :title="`RGB(${selectedCharacter.skin_r}, ${selectedCharacter.skin_g}, ${selectedCharacter.skin_b})`"
                    ></div>
                  </div>
                </div>
                <div class="morph-item" v-if="selectedCharacter.ntag">
                  <span class="morph-label">NTag:</span>
                  <span class="morph-value">{{ selectedCharacter.ntag }}</span>
                </div>
                <div class="morph-item" v-if="selectedCharacter.cntag_r !== null">
                  <span class="morph-label">CNTag Color:</span>
                  <div class="color-display">
                    <span class="morph-value">RGB({{ selectedCharacter.cntag_r }}, {{ selectedCharacter.cntag_g }}, {{ selectedCharacter.cntag_b }})</span>
                    <div 
                      class="color-preview" 
                      :style="{ backgroundColor: `rgb(${selectedCharacter.cntag_r}, ${selectedCharacter.cntag_g}, ${selectedCharacter.cntag_b})` }"
                      :title="`RGB(${selectedCharacter.cntag_r}, ${selectedCharacter.cntag_g}, ${selectedCharacter.cntag_b})`"
                    ></div>
                  </div>
                </div>
                <div class="morph-item" v-if="selectedCharacter.rtag">
                  <span class="morph-label">RTag:</span>
                  <span class="morph-value">{{ selectedCharacter.rtag }}</span>
                </div>
                <div class="morph-item" v-if="selectedCharacter.crtag_r !== null">
                  <span class="morph-label">CRTag Color:</span>
                  <div class="color-display">
                    <span class="morph-value">RGB({{ selectedCharacter.crtag_r }}, {{ selectedCharacter.crtag_g }}, {{ selectedCharacter.crtag_b }})</span>
                    <div 
                      class="color-preview" 
                      :style="{ backgroundColor: `rgb(${selectedCharacter.crtag_r}, ${selectedCharacter.crtag_g}, ${selectedCharacter.crtag_b})` }"
                      :title="`RGB(${selectedCharacter.crtag_r}, ${selectedCharacter.crtag_g}, ${selectedCharacter.crtag_b})`"
                    ></div>
                  </div>
                </div>
                <div class="morph-item" v-if="selectedCharacter.rhat">
                  <span class="morph-label">RHat:</span>
                  <span class="morph-value highlight">ACTIVADO</span>
                </div>
              </div>
            </div>
            
            <div class="detail-section">
              <h3 class="section-title">COMANDO MORPH</h3>
              <div class="morph-command-container">
                <div class="command-preview">
                  <code class="command-text">{{ selectedCharacter.morph_command }}</code>
                </div>
                <button class="copy-button small" @click="copyMorphCommand">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                  </svg>
                  <span>COPIAR</span>
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Modal de confirmación para eliminar -->
        <div v-if="showDeleteConfirm" class="modal-overlay" @click.self="showDeleteConfirm = false">
          <div class="modal-content confirm-modal" @click.stop>
            <div class="confirm-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="#aa2222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="12" y1="8" x2="12" y2="12"></line>
                <line x1="12" y1="16" x2="12.01" y2="16"></line>
              </svg>
            </div>
            <h3 class="confirm-title">CONFIRMAR ELIMINACIÓN</h3>
            <p class="confirm-text">
              ¿Estás seguro de que deseas eliminar al agente <strong>{{ selectedCharacter?.codename }}</strong>?
              Esta acción no se puede deshacer.
            </p>
            <div class="confirm-actions">
              <button class="confirm-cancel" @click="showDeleteConfirm = false">
                CANCELAR
              </button>
              <button class="confirm-delete" @click="deleteCharacter">
                ELIMINAR AGENTE
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- Footer -->
    <footer class="personajes-footer">
      <div class="footer-info">
        <span class="info-label">SYSTEM:</span>
        <span class="info-value">AGENT-MANAGEMENT v2.4</span>
      </div>
      <div class="footer-info">
        <span class="info-label">LAST UPDATE:</span>
        <span class="info-value">{{ currentTime }}</span>
      </div>
      <div class="footer-info">
        <span class="info-label">ACCESS LEVEL:</span>
        <span class="info-value">{{ currentUser?.is_authenticated ? 'AUTHORIZED' : 'GUEST' }}</span>
      </div>
    </footer>
      <!-- Sistema de notificaciones -->
      <div class="scp-notifications">
        <transition-group name="notification-slide">
          <div 
            v-for="notification in notifications" 
            :key="notification.id"
            class="scp-notification"
            :class="`type-${notification.type}`"
            @click="removeNotification(notification.id)"
          >
            <div class="notification-header">
              <div class="notification-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path v-if="notification.type === 'success'" d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                  <path v-if="notification.type === 'success'" d="M22 4 12 14.01l-3-3"></path>
                  <path v-if="notification.type === 'error'" d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
                  <line v-if="notification.type === 'error'" x1="12" y1="9" x2="12" y2="13"></line>
                  <line v-if="notification.type === 'error'" x1="12" y1="17" x2="12.01" y2="17"></line>
                  <circle v-if="notification.type === 'info'" cx="12" cy="12" r="10"></circle>
                  <line v-if="notification.type === 'info'" x1="12" y1="16" x2="12" y2="12"></line>
                  <line v-if="notification.type === 'info'" x1="12" y1="8" x2="12.01" y2="8"></line>
                </svg>
              </div>
              <div class="notification-title">
                {{ notification.title }}
              </div>
              <button class="notification-close">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="18" y1="6" x2="6" y2="18"></line>
                  <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
              </button>
            </div>
            <div class="notification-content">
              {{ notification.message }}
            </div>
            <div class="notification-progress" :style="{ 
              animationDuration: `${notification.duration}ms`,
              animationPlayState: notification.paused ? 'paused' : 'running' 
            }"></div>
          </div>
        </transition-group>
      </div>
  </div>
  <No_Mobile />
</template>

<script setup>
import { ref, reactive, onMounted, watch, computed, nextTick } from 'vue'
import { debounce } from 'lodash'
import { useRouter } from 'vue-router'
import Fuse from 'fuse.js' // Añadir esta línea
import No_Mobile from '@/components/No_Mobile.vue'
import Login_Required from '@/components/Login_Required.vue'

const router = useRouter()

// Estado principal
const activeView = ref('all')
const characters = ref([])
const myCharacters = ref([])
const selectedCharacter = ref(null)
const loading = ref(true)
const searchQuery = ref('')
const showCreateForm = ref(false)
const showEditForm = ref(false)
const showDeleteConfirm = ref(false)
const submitting = ref(false)
const currentUser = ref(null)
const currentTime = ref('')
const pagination = reactive({
  currentPage: 1,
  pageSize: 12,
  total: 0,
  totalPages: 0
})

// Nuevos estados para fuzzy search
const fuseAllCharacters = ref(null)
const fuseMyCharacters = ref(null)
const searchResults = ref([])
const isFuzzySearch = ref(false)
const showSearchSuggestions = ref(false)

// Configuración de Fuse.js
const fuseOptions = {
  keys: [
    { name: 'codename', weight: 0.4 },
    { name: 'first_name', weight: 0.3 },
    { name: 'last_name', weight: 0.2 },
    { name: 'faction', weight: 0.05 },
    { name: 'owner_username', weight: 0.05 }
  ],
  threshold: 0.3,
  distance: 100,
  minMatchCharLength: 2,
  includeScore: true,
  includeMatches: true,
  shouldSort: true,
  findAllMatches: true,
  ignoreLocation: true,
  useExtendedSearch: true,
  ignoreFieldNorm: true
}

// Formulario (mantener igual)
const characterForm = reactive({
  first_name: '',
  last_name: '',
  country: '',
  birth_date: '',
  codename: '',
  faction: '',
  morph: '',
  hat: '',
  nvg_r: 255,
  nvg_g: 165,
  nvg_b: 0,
  shirt: '',
  pants: '',
  skin_r: null,
  skin_g: null,
  skin_b: null,
  ntag: '',
  cntag_r: null,
  cntag_g: null,
  cntag_b: null,
  rtag: '',
  crtag_r: null,
  crtag_g: null,
  crtag_b: null,
  rhat: false,
  lore: ''
})

const formatBirthDate = (event) => {
  let value = event.target.value.replace(/\D/g, '')
  
  if (value.length > 8) {
    value = value.substring(0, 8)
  }
  
  if (value.length > 4) {
    value = value.substring(0, 2) + '/' + value.substring(2, 4) + '/' + value.substring(4)
  } else if (value.length > 2) {
    value = value.substring(0, 2) + '/' + value.substring(2)
  }
  
  characterForm.birth_date = value
}

// Computed properties
const loginUrl = computed(() => {
  const nextUrl = encodeURIComponent('/dashboard/personnel')
  return `/accounts/login/roblox/?next=${nextUrl}`
})

const isFormValid = computed(() => {
  return characterForm.first_name && 
         characterForm.last_name && 
         characterForm.codename && 
         characterForm.faction &&
         hasAtLeastOneMorphField.value
})

const hasAtLeastOneMorphField = computed(() => {
  const morphFields = [
    characterForm.morph,
    characterForm.hat,
    characterForm.shirt,
    characterForm.pants,
    characterForm.ntag,
    characterForm.rtag,
  ]
  return morphFields.some(field => field && field.trim() !== '')
})

// Modificar displayedCharacters para usar fuzzy search
const displayedCharacters = computed(() => {
  if (isFuzzySearch.value && searchQuery.value.trim()) {
    const startIndex = (pagination.currentPage - 1) * pagination.pageSize
    const endIndex = startIndex + pagination.pageSize
    return searchResults.value.slice(startIndex, endIndex)
  }
  
  const source = activeView.value === 'all' ? characters.value : myCharacters.value
  const startIndex = (pagination.currentPage - 1) * pagination.pageSize
  const endIndex = startIndex + pagination.pageSize
  return source.slice(startIndex, endIndex)
})

// Modificar totalItems
const totalItems = computed(() => {
  if (isFuzzySearch.value && searchQuery.value.trim()) {
    return searchResults.value.length
  }
  return activeView.value === 'all' ? characters.value.length : myCharacters.value.length
})

// Métodos
const setActiveView = (view) => {
  if (!currentUser.value?.is_authenticated) return
  
  activeView.value = view
  selectedCharacter.value = null
  showCreateForm.value = false
  showEditForm.value = false
  searchQuery.value = ''
  isFuzzySearch.value = false
  searchResults.value = []
  pagination.currentPage = 1
  
  loadCharacters()
}

// Modificar loadCharacters para inicializar Fuse.js
const loadCharacters = async () => {
  if (!currentUser.value?.is_authenticated) {
    loading.value = false
    return
  }
  
  loading.value = true
  try {
    let endpoint = '/api/characters/all/'
    if (activeView.value === 'mine') {
      endpoint = '/api/characters/mine/'
    }
    
    const response = await fetch(endpoint)
    const data = await response.json()
    
    let characterList = data.results || []
    
    // Inicializar Fuse.js con los datos
    if (activeView.value === 'all') {
      characters.value = characterList
      fuseAllCharacters.value = new Fuse(characterList, fuseOptions)
    } else {
      myCharacters.value = characterList
      fuseMyCharacters.value = new Fuse(characterList, fuseOptions)
    }
    
    // Aplicar búsqueda si hay query
    if (searchQuery.value) {
      handleSearch()
    } else {
      updatePagination(characterList.length)
    }
    
  } catch (error) {
    console.error('Error loading characters:', error)
    characters.value = []
    myCharacters.value = []
  } finally {
    loading.value = false
  }
}

// Función auxiliar para actualizar paginación
const updatePagination = (total) => {
  pagination.total = total
  pagination.totalPages = Math.ceil(total / pagination.pageSize)
}

// Modificar handleSearch para usar fuzzy search
const handleSearch = debounce(() => {
  pagination.currentPage = 1
  showSearchSuggestions.value = false
  
  if (!searchQuery.value.trim()) {
    isFuzzySearch.value = false
    searchResults.value = []
    const source = activeView.value === 'all' ? characters.value : myCharacters.value
    updatePagination(source.length)
    return
  }
  
  isFuzzySearch.value = true
  
  let results = []
  let fuseInstance = activeView.value === 'all' ? fuseAllCharacters.value : fuseMyCharacters.value
  
  if (fuseInstance) {
    // Búsqueda fuzzy con Fuse.js
    const searchResultsFuse = fuseInstance.search(searchQuery.value)
    results = searchResultsFuse.map(result => result.item)
    
    // Mostrar sugerencias si hay resultados
    if (results.length > 0 && searchQuery.value.length >= 2) {
      showSearchSuggestions.value = true
    }
    
    // Si no hay resultados fuzzy, intentar búsqueda exacta
    if (results.length === 0) {
      const source = activeView.value === 'all' ? characters.value : myCharacters.value
      results = source.filter(character => {
        const searchLower = searchQuery.value.toLowerCase()
        return (
          character.codename?.toLowerCase().includes(searchLower) ||
          character.first_name?.toLowerCase().includes(searchLower) ||
          character.last_name?.toLowerCase().includes(searchLower) ||
          character.faction?.toLowerCase().includes(searchLower) ||
          character.owner_username?.toLowerCase().includes(searchLower)
        )
      })
    }
  } else {
    // Fallback a búsqueda normal si Fuse no está inicializado
    const source = activeView.value === 'all' ? characters.value : myCharacters.value
    results = source.filter(character => {
      const searchLower = searchQuery.value.toLowerCase()
      return (
        character.codename?.toLowerCase().includes(searchLower) ||
        character.first_name?.toLowerCase().includes(searchLower) ||
        character.last_name?.toLowerCase().includes(searchLower) ||
        character.faction?.toLowerCase().includes(searchLower) ||
        character.owner_username?.toLowerCase().includes(searchLower)
      )
    })
  }
  
  searchResults.value = results
  updatePagination(results.length)
}, 300)

// Añadir método para limpiar búsqueda
const clearSearch = () => {
  searchQuery.value = ''
  isFuzzySearch.value = false
  searchResults.value = []
  showSearchSuggestions.value = false
  pagination.currentPage = 1
  loadCharacters()
}

// Añadir método para buscar sugerencia
const searchSuggestion = (suggestion) => {
  searchQuery.value = suggestion
  handleSearch()
}

const changePage = (page) => {
  if (page < 1 || page > pagination.totalPages) return
  pagination.currentPage = page
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const viewCharacter = async (character) => {
  if (!currentUser.value?.is_authenticated) return
  
  try {
    loading.value = true
    const response = await fetch(`/api/characters/${character.id}/`)
    const data = await response.json()
    selectedCharacter.value = data
  } catch (error) {
    console.error('Error loading character details:', error)
  } finally {
    loading.value = false
  }
}

const getFactionColor = (faction) => {
  const factions = {
    'CHAOS': { bg: 'rgba(220, 53, 69, 0.15)', text: '#dc3545', border: 'rgba(220, 53, 69, 0.3)' },
    'NATO': { bg: 'rgba(13, 110, 253, 0.15)', text: '#0d6efd', border: 'rgba(13, 110, 253, 0.3)' },
    'SCP': { bg: 'rgba(25, 135, 84, 0.15)', text: '#198754', border: 'rgba(25, 135, 84, 0.3)' },
    'FOUNDATION': { bg: 'rgba(25, 135, 84, 0.15)', text: '#198754', border: 'rgba(25, 135, 84, 0.3)' },
    'MTF': { bg: 'rgba(108, 117, 125, 0.15)', text: '#6c757d', border: 'rgba(108, 117, 125, 0.3)' },
    'CI': { bg: 'rgba(111, 66, 193, 0.15)', text: '#6f42c1', border: 'rgba(111, 66, 193, 0.3)' },
    'GOC': { bg: 'rgba(253, 126, 20, 0.15)', text: '#fd7e14', border: 'rgba(253, 126, 20, 0.3)' },
    'SERAPHS': { bg: 'rgba(32, 201, 151, 0.15)', text: '#20c997', border: 'rgba(32, 201, 151, 0.3)' },
  }
  
  return factions[faction?.toUpperCase()] || { 
    bg: 'rgba(252, 111, 3, 0.15)', 
    text: '#fc6f03', 
    border: 'rgba(252, 111, 3, 0.3)' 
  }
}

const openEditForm = () => {
  if (selectedCharacter.value) {
    Object.keys(characterForm).forEach(key => {
      characterForm[key] = selectedCharacter.value[key] || ''
    })
    showEditForm.value = true
  }
}

const closeFormView = () => {
  showCreateForm.value = false
  showEditForm.value = false
  selectedCharacter.value = null
  resetCharacterForm()
}

const resetCharacterForm = () => {
  Object.keys(characterForm).forEach(key => {
    if (key === 'rhat') {
      characterForm[key] = false
    } else if (key.startsWith('nvg_') || key.startsWith('skin_') || key.startsWith('cntag_') || key.startsWith('crtag_')) {
      if (key === 'nvg_r') characterForm[key] = 255
      else if (key === 'nvg_g') characterForm[key] = 165
      else if (key === 'nvg_b') characterForm[key] = 0
      else characterForm[key] = null
    } else {
      characterForm[key] = ''
    }
  })
}

const renderMarkdown = (text) => {
  if (!text) return ''
  
  let html = text
    .replace(/^##### (.*$)/gm, '<h5>$1</h5>')
    .replace(/^#### (.*$)/gm, '<h4>$1</h4>')
    .replace(/^### (.*$)/gm, '<h3>$1</h3>')
    .replace(/^## (.*$)/gm, '<h2>$1</h2>')
    .replace(/^# (.*$)/gm, '<h1>$1</h1>')
  
  html = html
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.*?)\*/g, '<em>$1</em>')
  
  html = html.replace(/^- (.*$)/gm, '<li>$1</li>')
  html = html.replace(/(<li>.*<\/li>)/gs, '<ul>$1</ul>')
  
  html = html.replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>')
  
  html = html.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
  
  html = html.replace(/`(.*?)`/g, '<code>$1</code>')
  
  html = html.replace(/^> (.*$)/gm, '<blockquote>$1</blockquote>')
  
  const parts = html.split(/(<pre>[\s\S]*?<\/pre>)/)
  html = parts.map(part => {
    if (part.startsWith('<pre>') && part.endsWith('</pre>')) {
      return part
    }
    return part.replace(/\n/g, '<br>')
  }).join('')
  
  return html
}

const getCSRFToken = () => {
  const cookieValue = document.cookie
    .split('; ')
    .find(row => row.startsWith('csrftoken='))
    ?.split('=')[1]
  
  if (cookieValue) return cookieValue
  
  const metaTag = document.querySelector('meta[name="csrf-token"]')
  if (metaTag) return metaTag.content
  
  const inputTag = document.querySelector('input[name="csrfmiddlewaretoken"]')
  if (inputTag) return inputTag.value
  
  console.error('CSRF token no encontrado')
  return ''
}

const submitCharacterForm = async () => {
  if (!currentUser.value?.is_authenticated) {
    showNotification(
      'OPERACIÓN FALLIDA',
      showEditForm.value ? 'No Autenticado' : 'Debes estar autenticado',
      'error',
      6000
    )
  }
  
  submitting.value = true
  
  try {
    const formData = { ...characterForm }

    if (formData.birth_date) {
      const parts = formData.birth_date.split('/')
      if (parts.length === 3) {
        const [day, month, year] = parts
        const date = new Date(`${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`)
        if (!isNaN(date.getTime())) {
          formData.birth_date = `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
        } else {
          throw new Error('Fecha de nacimiento inválida')
        }
      }
    }
    
    const numericFields = ['nvg_r', 'nvg_g', 'nvg_b', 'skin_r', 'skin_g', 'skin_b', 'cntag_r', 'cntag_g', 'cntag_b', 'crtag_r', 'crtag_g', 'crtag_b']
    numericFields.forEach(field => {
      formData[field] = formData[field] === '' ? null : Number(formData[field])
    })
    
    const morphFields = [
      formData.morph,
      formData.hat,
      formData.shirt,
      formData.pants,
      formData.ntag,
      formData.rtag,
    ]
    
    if (!morphFields.some(field => field && field.trim() !== '')) {
      showNotification(
        'ERROR',
        'Al menos un campo de morph debe estar definido',
        'error',
        6000
      )
    }
    
    let endpoint = '/api/characters/create/'
    let method = 'POST'
    
    if (showEditForm.value && selectedCharacter.value) {
      endpoint = `/api/characters/${selectedCharacter.value.id}/update/`
      method = 'PUT'
    }
    
    const csrfToken = getCSRFToken()
    if (!csrfToken) {
      showNotification(
        'ERROR DE SEGURIDAD',
        'Error: No se pudo obtener el token de seguridad. Por favor, recarga la página.',
        'error',
        6000
      )
    }
    
    const response = await fetch(endpoint, {
      method: method,
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      credentials: 'include',
      body: JSON.stringify(formData)
    })
    
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}))
      throw new Error(errorData.error || `Error ${response.status}: ${response.statusText}`)
    }
    
    const data = await response.json()
    showNotification(
    'OPERACIÓN EXITOSA',
    showEditForm.value ? 'Agente actualizado correctamente' : 'Agente registrado correctamente',
    'success',
    4000
    )
    closeFormView()
    loadCharacters()
    
    if (showEditForm.value && selectedCharacter.value) {
      viewCharacter(selectedCharacter.value)
    }
  } catch (error) {
    console.error('Error submitting form:', error)
    showNotification(
      'ERROR',
      'Error al procesar la solicitud. Contacte un administrador.',
      'error',
      6000
    )
  } finally {
    submitting.value = false
  }
}

const confirmDeleteCharacter = () => {
  showDeleteConfirm.value = true
}

const deleteCharacter = async () => {
  if (!selectedCharacter.value) return
  
  try {
    const csrfToken = getCSRFToken()
    if (!csrfToken) {
      showNotification(
        'ERROR DE SEGURIDAD',
        'Error: No se pudo obtener el token de seguridad.',
        'error',
        6000
      )
    }
    
    const response = await fetch(`/api/characters/${selectedCharacter.value.id}/delete/`, {
      method: 'DELETE',
      headers: {
        'X-CSRFToken': csrfToken
      },
      credentials: 'include'
    })
    
    if (response.ok) {
      showNotification(
        'AGENTE ELIMINADO',
        'Agente eliminado correctamente del sistema',
        'success',
        4000
      )
      selectedCharacter.value = null
      showDeleteConfirm.value = false
      loadCharacters()
    } else {
      const data = await response.json()
      showNotification(
        'ERROR DE ELIMINACIÓN',
        data.error || 'Error al eliminar el agente',
        'error',
        6000
      )
    }
  } catch (error) {
    console.error('Error deleting character:', error)
    showNotification(
      'ERROR DE ELIMINACIÓN',
      data.error || 'Error al eliminar el agente',
      'error',
      6000
    )
  }
}

const copyMorphCommand = async () => {
  if (selectedCharacter.value?.morph_command) {
    try {
      await navigator.clipboard.writeText(selectedCharacter.value.morph_command)
      showNotification(
        'COMANDO COPIADO',
        'El comando morph ha sido copiado al portapapeles',
        'success',
        3000
      )
    } catch (error) {
      console.error('Error copying to clipboard:', error)
    }
  }
}

const formatDateDDMMYYYY = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  const day = date.getDate().toString().padStart(2, '0')
  const month = (date.getMonth() + 1).toString().padStart(2, '0')
  const year = date.getFullYear()
  return `${day}/${month}/${year}`
}

const formatDateShort = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  const day = date.getDate().toString().padStart(2, '0')
  const month = (date.getMonth() + 1).toString().padStart(2, '0')
  const year = date.getFullYear().toString().slice(-2)
  return `${day}/${month}/${year}`
}

const updateTime = () => {
  const now = new Date()
  const day = now.getDate().toString().padStart(2, '0')
  const month = (now.getMonth() + 1).toString().padStart(2, '0')
  const year = now.getFullYear()
  const hours = now.getHours().toString().padStart(2, '0')
  const minutes = now.getMinutes().toString().padStart(2, '0')
  const seconds = now.getSeconds().toString().padStart(2, '0')
  currentTime.value = `${day}/${month}/${year} ${hours}:${minutes}:${seconds}`
}

const fetchCurrentUser = async () => {
  try {
    const response = await fetch('/api/auth/user/')
    if (response.ok) {
      const data = await response.json()
      currentUser.value = data
      if (data.is_authenticated) {
        loadCharacters()
      }
    }
  } catch (error) {
    console.error('Error fetching user:', error)
    loading.value = false
  }
}

const notifications = ref([])
let notificationId = 0

const showNotification = (title, message, type = 'info', duration = 5000) => {
  const id = ++notificationId
  notifications.value.push({
    id,
    title,
    message,
    type,
    duration,
    paused: false
  })
  
  setTimeout(() => {
    removeNotification(id)
  }, duration)
}

const removeNotification = (id) => {
  const index = notifications.value.findIndex(n => n.id === id)
  if (index !== -1) {
    notifications.value.splice(index, 1)
  }
}

const pauseNotification = (id) => {
  const notification = notifications.value.find(n => n.id === id)
  if (notification) {
    notification.paused = true
  }
}

const resumeNotification = (id) => {
  const notification = notifications.value.find(n => n.id === id)
  if (notification) {
    notification.paused = false
  }
}

// Watchers
watch(searchQuery, () => {
  if (currentUser.value?.is_authenticated) {
    handleSearch()
  }
})

watch(showEditForm, (newValue) => {
  if (newValue && selectedCharacter.value) {
    openEditForm()
  }
})

// Lifecycle
onMounted(() => {
  updateTime()
  const timeInterval = setInterval(updateTime, 1000)
  
  fetchCurrentUser()
  
  return () => {
    clearInterval(timeInterval)
  }
})
</script>

<style scoped>
/* Estilos principales - Página completa */
.personajes-page {
  position: relative;
  min-height: 100vh;
  color: #d8d8d8;
  background: #0a0a0a;
  font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
  line-height: 1.5;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
}

/* Fondo SCP */
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

/* Header con 2rem de padding top */
.personajes-header {
  position: relative;
  z-index: 2;
  background: rgba(15, 15, 15, 0.98);
  border-bottom: 1px solid #333;
  padding: 2rem 2rem 1rem 2rem; /* 2rem top padding */
  backdrop-filter: blur(10px);
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.5);
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1600px;
  margin: 0 auto;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.header-logo {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.person-icon {
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(252, 111, 3, 0.1);
  border: 1px solid rgba(252, 111, 3, 0.3);
  border-radius: 2px;
}

.person-icon svg {
  width: 28px;
  height: 28px;
}

.header-title {
  display: flex;
  flex-direction: column;
}

.header-main {
  font-size: 1.3rem;
  font-weight: 700;
  letter-spacing: 1px;
  color: #fff;
  text-transform: uppercase;
  line-height: 1.2;
}

.header-sub {
  font-size: 0.75rem;
  letter-spacing: 0.5px;
  color: #888;
  text-transform: uppercase;
}

.header-right {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 8px;
}

.session-status {
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

.session-text {
  font-size: 11px;
  color: #4CAF50;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.3px;
  text-transform: uppercase;
  font-weight: 600;
}

.current-time {
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

/* Navegación */
.personajes-nav {
  position: relative;
  z-index: 2;
  background: rgba(20, 20, 20, 0.95);
  border-bottom: 1px solid #333;
  padding: 1rem 2rem;
  backdrop-filter: blur(10px);
}

.nav-controls {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.nav-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.8rem;
  padding: 0.8rem 1.5rem;
  background: rgba(30, 30, 30, 0.9);
  border: 1px solid #444;
  color: #aaa;
  font-family: inherit;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.3s ease;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  flex-shrink: 0;
}

.nav-button:hover:not(:disabled) {
  background: rgba(40, 40, 40, 0.95);
  border-color: #666;
  color: #ddd;
}

.nav-button.active {
  background: rgba(252, 111, 3, 0.1);
  border-color: #fc6f03;
  color: #fc6f03;
}

.nav-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.nav-button.redacted {
  border-color: #aa2222;
  background: rgba(170, 34, 34, 0.1);
}

.nav-icon {
  width: 18px;
  height: 18px;
  color: currentColor;
}

.nav-icon.redacted {
  color: #aa2222;
}

.nav-text {
  font-weight: 600;
  font-family: 'Consolas', monospace;
}

.nav-text.redacted-text {
  color: #aa2222;
}

.nav-info {
  display: flex;
  gap: 2rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  flex-wrap: wrap;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.info-label {
  font-size: 11px;
  color: #666;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  font-family: 'Consolas', monospace;
}

.info-value {
  font-size: 12px;
  color: #ddd;
  font-weight: 600;
  letter-spacing: 0.3px;
  font-family: 'Consolas', monospace;
}

.info-value.operational {
  color: #4CAF50;
}

/* Contenido Principal */
.personajes-main {
  position: relative;
  z-index: 2;
  flex: 1;
  padding: 2rem;
  max-width: 1600px;
  margin: 0 auto;
  width: 100%;
}

/* Overlay de autenticación */
.auth-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.95);
  backdrop-filter: blur(10px);
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
}

.auth-panel {
  background: linear-gradient(135deg, 
    rgba(15, 15, 15, 0.98) 0%, 
    rgba(20, 20, 20, 0.98) 50%, 
    rgba(15, 15, 15, 0.98) 100%);
  border: 1px solid #333;
  width: 100%;
  max-width: 800px;
  max-height: 90vh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.7);
}

.panel-header {
  padding: 30px;
  background: rgba(25, 25, 25, 0.9);
  border-bottom: 1px solid #333;
  text-align: center;
  position: relative;
}

.warning-icon {
  width: 50px;
  height: 50px;
  color: #aa2222;
  margin: 0 auto 20px;
}

.panel-title {
  font-size: 28px;
  font-weight: 700;
  color: #ff3333;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 0 0 8px 0;
  font-family: 'Consolas', 'Courier New', monospace;
}

.panel-subtitle {
  font-size: 14px;
  color: #ff6666;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  font-weight: 600;
}

.panel-content {
  flex: 1;
  padding: 40px;
  display: flex;
  flex-direction: column;
  gap: 30px;
  overflow-y: auto;
}

.warning-section {
  border: 1px solid #444;
  padding: 25px;
  background: rgba(30, 30, 30, 0.6);
}

.section-title {
  font-size: 16px;
  font-weight: 700;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 20px 0;
  padding-bottom: 10px;
  border-bottom: 1px solid rgba(252, 111, 3, 0.3);
  font-family: 'Consolas', 'Courier New', monospace;
}

.warning-message {
  color: #ddd;
  line-height: 1.6;
  font-size: 15px;
}

.warning-message p {
  margin: 0 0 15px 0;
}

.action-section {
  text-align: center;
  padding: 20px 0;
}

.login-action-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 15px;
  padding: 16px 32px;
  background: rgba(30, 30, 30, 0.9);
  border: 1px solid #4CAF50;
  color: #4CAF50;
  font-size: 16px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-bottom: 20px;
  font-family: 'Consolas', 'Courier New', monospace;
}

.login-action-button:hover {
  background: rgba(76, 175, 80, 0.1);
  border-color: #66BB6A;
  color: #66BB6A;
}

.button-icon {
  width: 20px;
  height: 20px;
  color: currentColor;
}

.action-info {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  color: #888;
  font-size: 13px;
  max-width: 400px;
  margin: 0 auto;
}

.action-info svg {
  width: 16px;
  height: 16px;
  color: #888;
  flex-shrink: 0;
}

.security-notice {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  padding: 20px;
  background: rgba(20, 20, 20, 0.9);
  border-top: 1px solid #333;
  margin-top: auto;
}

.notice-item {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.notice-label {
  font-size: 11px;
  color: #666;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-family: 'Consolas', monospace;
}

.notice-value {
  font-size: 13px;
  color: #ddd;
  font-weight: 500;
  letter-spacing: 0.3px;
}

.notice-value.error {
  color: #ff3333;
  font-weight: 700;
}

/* Contenido autenticado */
.authenticated-content {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.view-header {
  padding: 2rem 0;
  border-bottom: 1px solid #333;
  margin-bottom: 2rem;
}

.view-title {
  font-size: 2rem;
  font-weight: 700;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 0.5rem 0;
  font-family: 'Consolas', 'Courier New', monospace;
}

.view-subtitle {
  font-size: 1rem;
  color: #aaa;
  letter-spacing: 0.3px;
}

.pagination-info {
  color: #888;
  font-size: 0.9rem;
  margin-left: 1rem;
}

.search-bar {
  margin-bottom: 2rem;
}

.search-container {
  position: relative;
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  padding: 1rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  transition: all 0.3s ease;
}

.search-container:focus-within {
  border-color: #fc6f03;
  box-shadow: 0 0 0 2px rgba(252, 111, 3, 0.1);
}

.search-icon {
  width: 20px;
  height: 20px;
  color: #888;
  flex-shrink: 0;
}

.search-input {
  flex: 1;
  background: transparent;
  border: none;
  color: #fff;
  font-size: 1rem;
  font-family: inherit;
  outline: none;
}

.search-input::placeholder {
  color: #666;
}

.search-count {
  font-size: 0.9rem;
  color: #888;
  font-family: 'Consolas', monospace;
  white-space: nowrap;
}

.add-agent-section {
  margin-bottom: 2rem;
}

.add-agent-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  padding: 1rem 2rem;
  background: rgba(252, 111, 3, 0.1);
  border: 1px solid rgba(252, 111, 3, 0.3);
  color: #fc6f03;
  font-size: 1rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  cursor: pointer;
  transition: all 0.3s ease;
  width: 100%;
}

.add-agent-button:hover {
  background: rgba(252, 111, 3, 0.2);
  border-color: rgba(252, 111, 3, 0.5);
}

.add-icon {
  width: 24px;
  height: 24px;
  color: currentColor;
}

.add-text {
  font-family: 'Consolas', monospace;
}

/* NUEVO: Contenedor de tarjetas mejoradas */
.enhanced-cards-container {
  flex: 1;
}

.loading-state,
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  text-align: center;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid rgba(252, 111, 3, 0.3);
  border-top: 3px solid #fc6f03;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-text {
  font-size: 1rem;
  color: #aaa;
  margin: 0;
}

.empty-icon {
  width: 60px;
  height: 60px;
  color: #fc6f03;
  opacity: 0.8;
  margin-bottom: 1.5rem;
}

.empty-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 1rem 0;
}

.empty-text {
  font-size: 1rem;
  color: #aaa;
  margin: 0 0 2rem 0;
  max-width: 400px;
}

.action-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.8rem;
  padding: 1rem 2rem;
  background: rgba(252, 111, 3, 0.1);
  border: 1px solid rgba(252, 111, 3, 0.3);
  color: #fc6f03;
  font-size: 1rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.action-button:hover {
  background: rgba(252, 111, 3, 0.2);
  border-color: rgba(252, 111, 3, 0.5);
}

.button-text {
  font-family: 'Consolas', monospace;
}

.button-indicator {
  width: 16px;
  height: 16px;
  color: currentColor;
}

/* NUEVO: Grid de tarjetas mejoradas - 3 por línea */
.enhanced-cards-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.enhanced-character-card {
  background: linear-gradient(145deg, rgba(20, 20, 20, 0.95) 0%, rgba(30, 30, 30, 0.95) 100%);
  border: 1px solid #333;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.4s ease;
  position: relative;
  overflow: hidden;
  height: 300px;
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
}

.enhanced-character-card:hover {
  transform: translateY(-6px);
  border-color: #fc6f03;
  box-shadow: 0 12px 30px rgba(252, 111, 3, 0.25);
}

.enhanced-character-card:hover .card-header .header-gradient {
  opacity: 1;
  transform: scale(1.05);
}

.enhanced-character-card:hover .view-indicator {
  color: #fc6f03;
}

.enhanced-character-card:hover .view-indicator svg {
  transform: translateX(4px);
}

/* Header con gradiente */
.card-header {
  position: relative;
  padding: 1.2rem 1.2rem 0.8rem 1.2rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  min-height: 70px;
  flex-shrink: 0;
}

.header-gradient {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 100%;
  background: linear-gradient(90deg, rgba(252, 111, 3, 0.1) 0%, rgba(252, 111, 3, 0.05) 50%, transparent 100%);
  opacity: 0.7;
  transition: all 0.4s ease;
  z-index: 1;
}

.codename-container {
  position: relative;
  z-index: 2;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.character-codename {
  font-size: min(1.4rem, max(0.9rem, 3.5vw)); /* Se ajusta entre 0.9rem y 1.4rem */
  font-weight: 800;
  color: #fff;
  margin: 0;
  font-family: 'Consolas', 'Courier New', monospace;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
  line-height: 1.2;
  word-wrap: break-word; /* Permite que las palabras largas se dividan */
  overflow-wrap: break-word;
  hyphens: auto; /* Agrega guiones automáticamente si es necesario */
  max-height: 2.8em; /* Aproximadamente 2 líneas */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2; /* Máximo 2 líneas */
  overflow: hidden;
  text-overflow: ellipsis;
}

.id-badge {
  font-size: 0.7rem;
  color: #888;
  background: rgba(255, 255, 255, 0.05);
  padding: 0.2rem 0.5rem;
  border-radius: 2px;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.3px;
}

.faction-badge {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  padding: 0.3rem 0.8rem;
  border-radius: 12px;
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-family: 'Consolas', monospace;
  z-index: 3;
  border: 1px solid;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

/* Cuerpo de la tarjeta */
.card-body {
  flex: 1;
  padding: 0.8rem 1.2rem;
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  position: relative;
  z-index: 2;
  min-height: 0; /* Importante para que flex funcione correctamente */
  overflow: hidden;
}

.name-section {
  margin-bottom: 0.5rem;
}

.character-name {
  font-size: min(1.1rem, max(0.8rem, 2.5vw)); /* Se ajusta entre 0.8rem y 1.1rem */
  font-weight: 600;
  color: #ddd;
  margin: 0 0 0.3rem 0;
  line-height: 1.2;
  word-wrap: break-word;
  overflow-wrap: break-word;
  hyphens: auto;
  max-height: 2.4em; /* Aproximadamente 2 líneas */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2; /* Máximo 2 líneas */
  overflow: hidden;
  text-overflow: ellipsis;
}

.character-country {
  font-size: 0.85rem;
  color: #aaa;
  margin: 0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.name-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 0.8rem;
  gap: 0.5rem;
  min-height: 70px; /* Espacio suficiente para 2 líneas de nombre + facción */
}

.name-faction {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.character-faction {
  font-size: min(0.8rem, max(0.65rem, 1.8vw)); /* Se ajusta entre 0.65rem y 0.8rem */
  color: #fc6f03;
  background: rgba(252, 111, 3, 0.1);
  padding: 0.2rem 0.5rem;
  border: 1px solid rgba(252, 111, 3, 0.3);
  display: inline-block;
  margin-top: 0.3rem;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.3px;
  max-width: 100%;
  word-wrap: break-word;
  overflow-wrap: break-word;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.right-info {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.5rem;
  margin-left: 0.5rem;
  flex-shrink: 0;
  min-width: 110px; /* Ancho mínimo para edad y registro */
}

.owner-id-section {
  margin-top: auto;
  padding-top: 0.8rem;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
}

.owner-label {
  font-size: 0.65rem;
  color: #666;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-family: 'Consolas', monospace;
  margin-bottom: 0.2rem;
}

.owner-name {
  font-size: 0.85rem;
  color: #aaa;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.country-icon {
  width: 14px;
  height: 14px;
  color: #888;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.8rem;
  margin-top: 0.5rem;
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}

.info-label {
  font-size: 0.65rem;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-family: 'Consolas', monospace;
  font-weight: 600;
}

.info-value {
  font-size: min(0.9rem, max(0.75rem, 2vw)); /* Se ajusta entre 0.75rem y 0.9rem */
  color: #ddd;
  font-weight: 500;
  text-align: right;
  line-height: 1.2;
  word-wrap: break-word;
  overflow-wrap: break-word;
}

.owner-section {
  margin-top: auto;
  padding-top: 0.8rem;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
}

.owner-label {
  font-size: 0.65rem;
  color: #666;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-family: 'Consolas', monospace;
  margin-bottom: 0.2rem;
}

.owner-name {
  font-size: min(0.85rem, max(0.75rem, 1.8vw)); /* Se ajusta entre 0.75rem y 0.85rem */
  color: #aaa;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  word-wrap: break-word;
  overflow-wrap: break-word;
  max-height: 1.8em;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* Footer de la tarjeta */
.card-footer {
  padding: 1rem 1.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(0, 0, 0, 0.2);
}

.status-indicator {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #4CAF50;
  box-shadow: 0 0 8px #4CAF50;
  animation: pulse 2s infinite;
}

.status-text {
  font-size: 0.75rem;
  color: #4CAF50;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-family: 'Consolas', monospace;
  font-weight: 700;
}

.view-indicator {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.8rem;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-family: 'Consolas', monospace;
  font-weight: 600;
  transition: all 0.3s ease;
}

.view-indicator svg {
  width: 16px;
  height: 16px;
  transition: transform 0.3s ease;
}

/* Decoración de esquina */
.corner-decoration {
  position: absolute;
  top: 0;
  right: 0;
  width: 20px;
  height: 20px;
  border-top: 2px solid #fc6f03;
  border-right: 2px solid #fc6f03;
  border-top-right-radius: 4px;
  opacity: 0.5;
}

/* Paginación */
.pagination-controls {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.pagination-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.8rem 1.5rem;
  background: rgba(30, 30, 30, 0.9);
  border: 1px solid #444;
  color: #aaa;
  font-family: 'Consolas', monospace;
  font-size: 0.9rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  cursor: pointer;
  transition: all 0.3s ease;
  min-width: 140px;
}

.pagination-button:hover:not(:disabled) {
  background: rgba(40, 40, 40, 0.95);
  border-color: #666;
  color: #ddd;
}

.pagination-button:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.pagination-button svg {
  width: 16px;
  height: 16px;
}

.page-numbers {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.page-info {
  font-family: 'Consolas', monospace;
  font-size: 0.9rem;
  color: #888;
  letter-spacing: 0.3px;
}

/* Vista de formulario */
.form-view {
  background: rgba(20, 20, 20, 0.95);
  border: 1px solid #333;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.form-header {
  padding: 1.5rem 2rem;
  border-bottom: 1px solid #333;
  background: rgba(25, 25, 25, 0.9);
  display: flex;
  align-items: center;
  gap: 2rem;
}

.back-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: rgba(40, 40, 40, 0.6);
  border: 1px solid #444;
  color: #aaa;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.back-button:hover {
  background: rgba(50, 50, 50, 0.7);
  border-color: #555;
  color: #fff;
}

.back-button svg {
  width: 16px;
  height: 16px;
}

.form-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0;
  font-family: 'Consolas', 'Courier New', monospace;
}

.character-form {
  flex: 1;
  overflow-y: auto;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.form-section {
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  padding: 1.5rem;
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-group.full-width {
  grid-column: 1 / -1;
}

.form-label {
  font-size: 0.9rem;
  color: #ccc;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  font-family: 'Consolas', monospace;
}

.form-input,
.form-textarea {
  background: rgba(40, 40, 40, 0.6);
  border: 1px solid #444;
  padding: 0.75rem;
  color: #fff;
  font-size: 1rem;
  font-family: inherit;
  transition: all 0.3s ease;
}

.form-input:focus,
.form-textarea:focus {
  outline: none;
  border-color: #fc6f03;
  box-shadow: 0 0 0 2px rgba(252, 111, 3, 0.1);
}

.form-input:disabled {
  background: rgba(50, 50, 50, 0.4);
  color: #888;
  cursor: not-allowed;
}

.form-textarea {
  resize: vertical;
  min-height: 100px;
}

.lore-textarea {
  min-height: 200px;
}

.form-hint {
  font-size: 0.8rem;
  color: #888;
  font-style: italic;
}

.color-inputs {
  display: flex;
  gap: 0.5rem;
}

.color-input {
  flex: 1;
  background: rgba(40, 40, 40, 0.6);
  border: 1px solid #444;
  padding: 0.75rem;
  color: #fff;
  font-size: 0.9rem;
  text-align: center;
  font-family: inherit;
}

.checkbox-group {
  flex-direction: row;
  align-items: center;
  margin-top: 1rem;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
}

.checkbox-input {
  width: 18px;
  height: 18px;
  accent-color: #fc6f03;
}

.checkbox-text {
  font-size: 0.9rem;
  color: #ccc;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 1px solid #444;
}

.cancel-button,
.submit-button {
  padding: 1rem 2rem;
  font-size: 0.9rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  font-family: 'Consolas', monospace;
}

.cancel-button {
  background: rgba(40, 40, 40, 0.6);
  border: 1px solid #444;
  color: #aaa;
}

.cancel-button:hover {
  background: rgba(50, 50, 50, 0.7);
  border-color: #555;
  color: #fff;
}

.submit-button {
  background: rgba(252, 111, 3, 0.1);
  border: 1px solid rgba(252, 111, 3, 0.3);
  color: #fc6f03;
}

.submit-button:hover:not(:disabled) {
  background: rgba(252, 111, 3, 0.2);
  border-color: rgba(252, 111, 3, 0.5);
}

.submit-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Vista de detalle */
.detail-view {
  background: rgba(20, 20, 20, 0.95);
  border: 1px solid #333;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.detail-header {
  padding: 1.5rem 2rem;
  border-bottom: 1px solid #333;
  background: rgba(25, 25, 25, 0.9);
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 2rem;
}

.header-actions {
  display: flex;
  gap: 1rem;
}

.edit-button,
.delete-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.edit-button {
  background: rgba(252, 111, 3, 0.1);
  border: 1px solid rgba(252, 111, 3, 0.3);
  color: #fc6f03;
}

.edit-button:hover {
  background: rgba(252, 111, 3, 0.2);
  border-color: rgba(252, 111, 3, 0.5);
}

.delete-button {
  background: rgba(220, 53, 69, 0.1);
  border: 1px solid rgba(220, 53, 69, 0.3);
  color: #dc3545;
}

.delete-button:hover {
  background: rgba(220, 53, 69, 0.2);
  border-color: rgba(220, 53, 69, 0.5);
}

.detail-content {
  flex: 1;
  overflow-y: auto;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.detail-section {
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  padding: 1.5rem;
}

.detail-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
}

.detail-item {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.detail-label {
  font-size: 0.8rem;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  font-family: 'Consolas', monospace;
}

.detail-value {
  font-size: 1rem;
  color: #ddd;
  font-weight: 500;
}

.detail-value.highlight {
  color: #fc6f03;
  font-weight: 700;
}

.detail-value.faction {
  color: #fc6f03;
  background: rgba(252, 111, 3, 0.1);
  padding: 0.25rem 0.5rem;
  border: 1px solid rgba(252, 111, 3, 0.3);
  display: inline-block;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.3px;
}

.lore-container {
  background: rgba(40, 40, 40, 0.6);
  border: 1px solid #444;
  padding: 1.5rem;
  margin-top: 1rem;
}

.lore-content {
  color: #ddd;
  line-height: 1.6;
}

.lore-content h1,
.lore-content h2,
.lore-content h3,
.lore-content h4,
.lore-content h5,
.lore-content h6 {
  color: #fc6f03;
  margin-top: 1.5em;
  margin-bottom: 0.5em;
}

.lore-content p {
  margin: 1em 0;
}

.lore-content ul,
.lore-content ol {
  margin: 1em 0;
  padding-left: 2em;
}

.lore-content li {
  margin: 0.5em 0;
}

.morph-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}

.morph-item {
  padding: 1rem;
  background: rgba(40, 40, 40, 0.6);
  border: 1px solid #444;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.morph-label {
  font-size: 0.8rem;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  font-family: 'Consolas', monospace;
}

.morph-value {
  font-size: 0.9rem;
  color: #ddd;
  font-weight: 500;
  word-break: break-all;
}

.color-display {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.color-preview {
  width: 30px;
  height: 30px;
  border: 2px solid #ddd;
  flex-shrink: 0;
}

.morph-command-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.command-preview {
  background: rgba(20, 20, 20, 0.8);
  border: 1px solid #444;
  padding: 1rem;
  overflow-x: auto;
}

.command-text {
  font-family: 'Consolas', monospace;
  font-size: 0.9rem;
  color: #4CAF50;
  white-space: nowrap;
}

/* Botón de copiar más pequeño */
.copy-button.small {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: rgba(76, 175, 80, 0.1);
  border: 1px solid rgba(76, 175, 80, 0.3);
  color: #4CAF50;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  cursor: pointer;
  transition: all 0.3s ease;
  align-self: flex-start;
  min-width: auto;
}

.copy-button.small:hover {
  background: rgba(76, 175, 80, 0.2);
  border-color: rgba(76, 175, 80, 0.5);
}

/* Modal de confirmación */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(5px);
  z-index: 2000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.confirm-modal {
  background: rgba(25, 25, 25, 0.95);
  border: 1px solid #aa2222;
  padding: 2.5rem;
  max-width: 500px;
  width: 100%;
  text-align: center;
}

.confirm-icon {
  width: 60px;
  height: 60px;
  color: #aa2222;
  margin: 0 auto 1.5rem;
}

.confirm-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #aa2222;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 1rem 0;
  font-family: 'Consolas', 'Courier New', monospace;
}

.confirm-text {
  font-size: 1rem;
  color: #ccc;
  line-height: 1.5;
  margin: 0 0 2rem 0;
}

.confirm-text strong {
  color: #fff;
}

.confirm-actions {
  display: flex;
  justify-content: center;
  gap: 1rem;
}

.confirm-cancel,
.confirm-delete {
  padding: 0.75rem 1.5rem;
  font-size: 0.9rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  font-family: 'Consolas', monospace;
}

.confirm-cancel {
  background: rgba(40, 40, 40, 0.6);
  border: 1px solid #444;
  color: #aaa;
}

.confirm-cancel:hover {
  background: rgba(50, 50, 50, 0.7);
  border-color: #555;
  color: #fff;
}

.confirm-delete {
  background: rgba(220, 53, 69, 0.1);
  border: 1px solid rgba(220, 53, 69, 0.3);
  color: #dc3545;
}

.confirm-delete:hover {
  background: rgba(220, 53, 69, 0.2);
  border-color: rgba(220, 53, 69, 0.5);
}

/* Footer */
.personajes-footer {
  position: relative;
  z-index: 2;
  background: rgba(15, 15, 15, 0.98);
  border-top: 1px solid #333;
  padding: 1rem 2rem;
  backdrop-filter: blur(10px);
  margin-top: auto;
}

.footer-info {
  display: flex;
  justify-content: center;
  gap: 2rem;
  flex-wrap: wrap;
}

/* Modal de autenticación SCP */
.auth-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.95);
  backdrop-filter: blur(10px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  animation: fadeIn 0.3s ease;
}

.scp-auth-modal {
  background: linear-gradient(135deg, 
    rgba(15, 15, 15, 0.98) 0%, 
    rgba(20, 20, 20, 0.98) 50%, 
    rgba(15, 15, 15, 0.98) 100%);
  border: 2px solid #333;
  width: 100%;
  max-width: 800px;
  max-height: 90vh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8);
  position: relative;
}

.scp-auth-modal::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, 
    #fc6f03 0%, 
    #ff3333 50%, 
    #fc6f03 100%);
  z-index: 2;
}

.modal-header {
  padding: 2rem;
  background: rgba(25, 25, 25, 0.95);
  border-bottom: 1px solid #333;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  position: relative;
}

.modal-icon {
  width: 50px;
  height: 50px;
  background: rgba(252, 111, 3, 0.1);
  border: 1px solid rgba(252, 111, 3, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.modal-icon svg {
  width: 28px;
  height: 28px;
  color: #fc6f03;
}

.modal-title-section {
  flex: 1;
}

.modal-title {
  font-size: 1.8rem;
  font-weight: 800;
  color: #ff3333;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 0 0 0.3rem 0;
  font-family: 'Consolas', 'Courier New', monospace;
  text-shadow: 0 2px 4px rgba(255, 51, 51, 0.3);
}

.modal-subtitle {
  font-size: 0.85rem;
  color: #888;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  font-weight: 600;
}

.modal-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 51, 51, 0.1);
  border: 1px solid rgba(255, 51, 51, 0.3);
  padding: 0.5rem 1rem;
}

.status-indicator.denied {
  width: 8px;
  height: 8px;
  background: #ff3333;
  box-shadow: 0 0 8px #ff3333;
  animation: pulse 1.5s infinite;
}

.status-text {
  font-size: 0.8rem;
  color: #ff3333;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  font-family: 'Consolas', monospace;
}

.modal-content {
  flex: 1;
  padding: 2rem;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.security-warning {
  background: rgba(40, 40, 40, 0.6);
  border: 1px solid #444;
  padding: 1.5rem;
}

.warning-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid rgba(255, 51, 51, 0.3);
}

.warning-header svg {
  width: 24px;
  height: 24px;
}

.warning-header h3 {
  font-size: 1.1rem;
  color: #ff3333;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0;
  font-family: 'Consolas', monospace;
}

.warning-content {
  color: #ddd;
  line-height: 1.6;
}

.warning-content p {
  margin: 0 0 1rem 0;
}

.warning-content ul {
  margin: 1rem 0;
  padding-left: 1.5rem;
}

.warning-content li {
  margin: 0.5rem 0;
  color: #ccc;
}

.warning-content strong {
  color: #fc6f03;
}

.warning-note {
  font-style: italic;
  color: #ff6666;
  border-left: 3px solid #ff3333;
  padding-left: 1rem;
  margin-top: 1rem !important;
}

.system-info {
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  padding: 1.5rem;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

.info-label {
  font-size: 0.7rem;
  color: #666;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-family: 'Consolas', monospace;
}

.info-value {
  font-size: 0.9rem;
  color: #ddd;
  font-weight: 600;
  letter-spacing: 0.3px;
}

.info-value.status-operational {
  color: #4CAF50;
}

.info-value.status-classified {
  color: #ff3333;
  background: rgba(255, 51, 51, 0.1);
  padding: 0.2rem 0.5rem;
  display: inline-block;
}

.action-section {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.action-required {
  display: flex;
  align-items: center;
  gap: 1rem;
  background: rgba(76, 175, 80, 0.1);
  border: 1px solid rgba(76, 175, 80, 0.3);
  padding: 1rem;
}

.required-icon {
  width: 40px;
  height: 40px;
  background: rgba(76, 175, 80, 0.2);
  border: 1px solid rgba(76, 175, 80, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.required-icon svg {
  width: 20px;
  height: 20px;
  color: #4CAF50;
}

.required-text {
  flex: 1;
}

.required-text h4 {
  font-size: 1rem;
  color: #4CAF50;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 0.3rem 0;
  font-family: 'Consolas', monospace;
}

.required-text p {
  font-size: 0.9rem;
  color: #aaa;
  margin: 0;
}

.scp-login-button {
  display: block;
  background: rgba(30, 30, 30, 0.9);
  border: 2px solid #4CAF50;
  color: #4CAF50;
  text-decoration: none;
  position: relative;
  overflow: hidden;
  transition: all 0.3s ease;
  cursor: pointer;
}

.scp-login-button:hover {
  border-color: #66BB6A;
  background: rgba(76, 175, 80, 0.05);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(76, 175, 80, 0.3);
}

.button-glow {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, 
    transparent 0%, 
    rgba(76, 175, 80, 0.2) 50%, 
    transparent 100%);
  transition: left 0.5s ease;
}

.scp-login-button:hover .button-glow {
  left: 100%;
}

.button-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem 2rem;
  position: relative;
  z-index: 1;
}

.button-icon {
  width: 28px;
  height: 28px;
  color: currentColor;
}

.button-text {
  flex: 1;
  margin: 0 2rem;
  text-align: center;
}

.main-text {
  display: block;
  font-size: 1.2rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 0.3rem;
  font-family: 'Consolas', monospace;
}

.sub-text {
  display: block;
  font-size: 0.85rem;
  color: #88cc88;
  letter-spacing: 0.3px;
}

.button-indicator {
  width: 24px;
  height: 24px;
  color: currentColor;
}

.login-info {
  display: flex;
  align-items: flex-start;
  gap: 0.8rem;
  color: #888;
  font-size: 0.85rem;
  line-height: 1.4;
}

.login-info svg {
  width: 16px;
  height: 16px;
  color: #888;
  margin-top: 0.2rem;
  flex-shrink: 0;
}

.modal-footer {
  padding: 1.5rem 2rem;
  background: rgba(25, 25, 25, 0.95);
  border-top: 1px solid #333;
}

.footer-grid {
  display: flex;
  justify-content: space-between;
  gap: 2rem;
  flex-wrap: wrap;
}

.footer-item {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}

.footer-label {
  font-size: 0.65rem;
  color: #666;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-family: 'Consolas', monospace;
}

.footer-value {
  font-size: 0.8rem;
  color: #aaa;
  font-weight: 600;
  letter-spacing: 0.3px;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Sistema de notificaciones SCP */
.scp-notifications {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  z-index: 10000;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-width: 400px;
  pointer-events: none;
}

.scp-notification {
  background: linear-gradient(135deg, 
    rgba(20, 20, 20, 0.95) 0%, 
    rgba(30, 30, 30, 0.95) 100%);
  border: 1px solid #333;
  border-left: 4px solid #fc6f03;
  padding: 1rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  position: relative;
  overflow: hidden;
  pointer-events: auto;
  cursor: pointer;
  transition: all 0.3s ease;
  animation: slideInRight 0.3s ease;
}

.scp-notification:hover {
  transform: translateX(-5px);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6);
}

.scp-notification.type-success {
  border-left-color: #4CAF50;
}

.scp-notification.type-error {
  border-left-color: #ff3333;
}

.scp-notification.type-info {
  border-left-color: #2196F3;
}

.notification-header {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  margin-bottom: 0.8rem;
}

.notification-icon {
  width: 24px;
  height: 24px;
  flex-shrink: 0;
}

.scp-notification.type-success .notification-icon {
  color: #4CAF50;
}

.scp-notification.type-error .notification-icon {
  color: #ff3333;
}

.scp-notification.type-info .notification-icon {
  color: #2196F3;
}

.notification-title {
  flex: 1;
  font-size: 0.9rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: #fff;
  font-family: 'Consolas', monospace;
}

.notification-close {
  background: none;
  border: none;
  color: #888;
  cursor: pointer;
  padding: 0.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.3s ease;
}

.notification-close:hover {
  color: #fff;
}

.notification-close svg {
  width: 16px;
  height: 16px;
}

.notification-content {
  font-size: 0.9rem;
  color: #ccc;
  line-height: 1.4;
  margin-bottom: 0.5rem;
}

.notification-progress {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, 
    transparent 0%, 
    #fc6f03 50%, 
    transparent 100%);
  animation: progressBar linear forwards;
}

.scp-notification.type-success .notification-progress {
  background: linear-gradient(90deg, 
    transparent 0%, 
    #4CAF50 50%, 
    transparent 100%);
}

.scp-notification.type-error .notification-progress {
  background: linear-gradient(90deg, 
    transparent 0%, 
    #ff3333 50%, 
    transparent 100%);
}

.scp-notification.type-info .notification-progress {
  background: linear-gradient(90deg, 
    transparent 0%, 
    #2196F3 50%, 
    transparent 100%);
}

/* Animaciones */
@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(100%);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes progressBar {
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(100%);
  }
}

.notification-slide-enter-active,
.notification-slide-leave-active {
  transition: all 0.3s ease;
}

.notification-slide-enter-from,
.notification-slide-leave-to {
  opacity: 0;
  transform: translateX(100%);
}

/* Clases para control de texto responsive */
.text-responsive {
  font-size: min(var(--max-size), max(var(--min-size), var(--dynamic-size)));
  line-height: 1.2;
  word-wrap: break-word;
  overflow-wrap: break-word;
}

/* Para nombres muy largos con guiones */
.hyphenate {
  hyphens: auto;
  -webkit-hyphens: auto;
  -ms-hyphens: auto;
}

/* Contenedor flexible para texto */
.text-container {
  min-width: 0; /* Permite que el texto se ajuste en flex containers */
  flex: 1;
}

/* Responsive */
@media (max-width: 1200px) {
  .enhanced-cards-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .personajes-header,
  .personajes-nav,
  .personajes-footer {
    padding: 1rem;
  }
  
  .header-content {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }
  
  .header-right {
    align-items: center;
  }
  
  .nav-controls {
    justify-content: center;
  }
  
  .nav-info {
    justify-content: center;
  }
  
  .enhanced-cards-grid {
    grid-template-columns: 1fr;
  }
  
  .enhanced-character-card {
    height: 260px;
  }
  
  .card-header {
    padding: 1rem 1rem 0.8rem 1rem;
  }
  
  .card-body {
    padding: 0.8rem 1rem;
  }
  
  .card-footer {
    padding: 0.8rem 1rem;
  }
  
  .form-grid,
  .detail-grid,
  .morph-grid {
    grid-template-columns: 1fr;
  }
  
  .security-notice {
    grid-template-columns: 1fr;
  }
  
  .form-header,
  .detail-header {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }
  
  .header-actions {
    justify-content: center;
  }
  
  .form-actions,
  .confirm-actions,
  .pagination-controls {
    flex-direction: column;
    gap: 1rem;
  }
  
  .pagination-button {
    min-width: 100%;
  }
}

@media (min-width: 769px) and (max-width: 1024px) {
  .enhanced-cards-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1025px) {
  .enhanced-cards-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

.detail-item.full-width {
  grid-column: 1 / -1;
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.owner-link {
  color: #4CAF50;
  text-decoration: none;
  transition: color 0.3s ease;
}

.owner-link:hover {
  color: #66BB6A;
  text-decoration: underline;
}

.id-badge {
  font-size: 0.8rem;
  color: #888;
  background: rgba(255, 255, 255, 0.05);
  padding: 0.2rem 0.5rem;
  border-radius: 2px;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.3px;
  margin-left: 0.5rem;
}

/* Estilos para la búsqueda mejorada con fuzzy search */
.search-clear {
  background: none;
  border: none;
  color: #888;
  cursor: pointer;
  padding: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  flex-shrink: 0;
}

.search-clear:hover {
  color: #fc6f03;
}

.search-clear svg {
  width: 16px;
  height: 16px;
}

.search-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-left: auto;
}

.fuzzy-indicator {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.75rem;
  color: #4CAF50;
  background: rgba(76, 175, 80, 0.1);
  padding: 0.3rem 0.6rem;
  border-radius: 2px;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.3px;
  animation: pulse 2s infinite;
  white-space: nowrap;
}

.fuzzy-indicator svg {
  width: 14px;
  height: 14px;
}

.search-suggestions {
  margin-top: 0.5rem;
  padding: 0.5rem 1rem;
  background: rgba(30, 30, 30, 0.8);
  border: 1px solid rgba(252, 111, 3, 0.3);
  font-size: 0.85rem;
  border-radius: 2px;
  animation: fadeIn 0.3s ease;
}

.suggestion-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.3rem;
}

.suggestion-item:last-child {
  margin-bottom: 0;
}

.suggestion-label {
  color: #fc6f03;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.75rem;
  font-family: 'Consolas', monospace;
  white-space: nowrap;
}

.suggestion-text {
  color: #aaa;
  flex: 1;
}

.suggestion-text strong {
  color: #fff;
  font-weight: 600;
}

/* Mejorar el contador de búsqueda */
.search-count {
  font-size: 0.9rem;
  color: #888;
  font-family: 'Consolas', monospace;
  white-space: nowrap;
  background: rgba(255, 255, 255, 0.05);
  padding: 0.2rem 0.5rem;
  border-radius: 2px;
}

/* Animación para fadeIn */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-5px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Mejorar el foco del input de búsqueda */
.search-container:focus-within {
  border-color: #fc6f03;
  box-shadow: 0 0 0 2px rgba(252, 111, 3, 0.1), 0 4px 12px rgba(252, 111, 3, 0.1);
}

/* Responsive para la barra de búsqueda */
@media (max-width: 768px) {
  .search-info {
    flex-direction: column;
    align-items: flex-end;
    gap: 0.5rem;
  }
  
  .fuzzy-indicator {
    font-size: 0.7rem;
    padding: 0.2rem 0.4rem;
  }
  
  .search-count {
    font-size: 0.8rem;
  }
}
</style>