<template>
  <div class="personajes-container">
    <!-- Sidebar izquierdo -->
    <nav class="personajes-sidebar">
      <div class="sidebar-header">
        <h3 class="sidebar-title">AGENT MANAGEMENT</h3>
        <div class="sidebar-subtitle">Personnel Control Panel</div>
      </div>
      
      <div class="sidebar-tools">
        <button 
          class="tool-item" 
          :class="{ 'active': activeView === 'all' }"
          @click="setActiveView('all')"
        >
          <div class="tool-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
              <circle cx="9" cy="7" r="4"></circle>
              <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
            </svg>
          </div>
          <span class="tool-name">Lista de Personal</span>
          <div class="tool-indicator" v-if="activeView === 'all'">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </div>
        </button>
        
        <button 
          class="tool-item" 
          :class="{ 'active': activeView === 'mine' }"
          @click="setActiveView('mine')"
        >
          <div class="tool-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
          </div>
          <span class="tool-name">Mis Agentes</span>
          <div class="tool-indicator" v-if="activeView === 'mine'">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </div>
        </button>
        
        <!-- Placeholders [REDACTED] -->
        <div class="tool-item redacted">
          <div class="tool-icon redacted">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
            </svg>
          </div>
          <span class="tool-name redacted-text">[REDACTED]</span>
        </div>
        
        <div class="tool-item redacted">
          <div class="tool-icon redacted">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
            </svg>
          </div>
          <span class="tool-name redacted-text">[REDACTED]</span>
        </div>
      </div>
    </nav>

    <!-- Área de contenido principal -->
    <section class="personajes-main">
      <!-- Vista: Lista de todos los personajes -->
      <div v-if="activeView === 'all' && !selectedCharacter" class="all-characters-view">
        <div class="view-header">
          <h2 class="view-title">LISTA DE PERSONAL</h2>
          <div class="view-subtitle">Todos los agentes registrados en Site-81</div>
        </div>
        
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
              @input="debouncedSearch"
              type="text"
              placeholder="Buscar por nombre del personaje o usuario owner..."
              class="search-input"
            />
            <div class="search-count" v-if="characters.length > 0">
              {{ characters.length }} agentes encontrados
            </div>
          </div>
        </div>
        
        <div class="characters-grid" v-if="characters.length > 0">
          <div 
            v-for="character in characters" 
            :key="character.id"
            class="character-card"
            @click="viewCharacter(character)"
          >
            <div class="character-header">
              <h4 class="character-name">{{ character.codename }}</h4>
              <div class="character-faction">{{ character.faction }}</div>
            </div>
            
            <div class="character-info">
              <div class="info-row">
                <span class="info-label">Nombre:</span>
                <span class="info-value">{{ character.first_name }} {{ character.last_name }}</span>
              </div>
              <div class="info-row">
                <span class="info-label">Owner:</span>
                <span class="info-value owner-link" @click.stop="viewUser(character.owner_id)">
                  {{ character.owner_username }}
                </span>
              </div>
              <div class="info-row">
                <span class="info-label">País:</span>
                <span class="info-value">{{ character.country }}</span>
              </div>
              <div class="info-row" v-if="character.age">
                <span class="info-label">Edad:</span>
                <span class="info-value">{{ character.age }} años</span>
              </div>
            </div>
            
            <div class="character-footer">
              <div class="character-id">ID: {{ character.id }}</div>
              <div class="view-button">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="9 18 15 12 9 6"></polyline>
                </svg>
              </div>
            </div>
          </div>
        </div>
        
        <div v-else-if="loading" class="loading-state">
          <div class="loading-spinner"></div>
          <p class="loading-text">Cargando agentes...</p>
        </div>
        
        <div v-else class="empty-state">
          <div class="empty-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="#fc6f03" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
              <circle cx="9" cy="7" r="4"></circle>
              <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
            </svg>
          </div>
          <h3 class="empty-title">No se encontraron agentes</h3>
          <p class="empty-text" v-if="searchQuery">
            No hay agentes que coincidan con "{{ searchQuery }}"
          </p>
          <p class="empty-text" v-else>
            No hay agentes registrados en el sistema.
          </p>
        </div>
      </div>

      <!-- Vista: Mis agentes -->
      <div v-else-if="activeView === 'mine' && !selectedCharacter" class="my-characters-view">
        <div class="view-header">
          <h2 class="view-title">MIS AGENTES</h2>
          <div class="view-subtitle">Tus agentes registrados en Site-81</div>
        </div>
        
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
              @input="debouncedSearch"
              type="text"
              placeholder="Buscar por nombre o codename..."
              class="search-input"
            />
            <div class="search-count" v-if="myCharacters.length > 0">
              {{ myCharacters.length }} agentes encontrados
            </div>
          </div>
        </div>
        
        <div class="characters-grid" v-if="myCharacters.length > 0">
          <div 
            v-for="character in myCharacters" 
            :key="character.id"
            class="character-card"
            @click="viewCharacter(character)"
          >
            <div class="character-header">
              <h4 class="character-name">{{ character.codename }}</h4>
              <div class="character-faction">{{ character.faction }}</div>
            </div>
            
            <div class="character-info">
              <div class="info-row">
                <span class="info-label">Nombre:</span>
                <span class="info-value">{{ character.first_name }} {{ character.last_name }}</span>
              </div>
              <div class="info-row">
                <span class="info-label">País:</span>
                <span class="info-value">{{ character.country }}</span>
              </div>
              <div class="info-row" v-if="character.age">
                <span class="info-label">Edad:</span>
                <span class="info-value">{{ character.age }} años</span>
              </div>
              <div class="info-row">
                <span class="info-label">Creado:</span>
                <span class="info-value">{{ formatDate(character.created_at) }}</span>
              </div>
            </div>
            
            <div class="character-footer">
              <div class="character-id">ID: {{ character.id }}</div>
              <div class="view-button">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="9 18 15 12 9 6"></polyline>
                </svg>
              </div>
            </div>
          </div>
          
          <!-- Botón para añadir nuevo agente -->
          <div class="character-card add-new" @click="showCreateForm = true">
            <div class="add-new-content">
              <div class="add-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="#fc6f03" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="12" y1="5" x2="12" y2="19"></line>
                  <line x1="5" y1="12" x2="19" y2="12"></line>
                </svg>
              </div>
              <h4 class="add-title">REGISTRAR NUEVO AGENTE</h4>
              <p class="add-text">Crear un nuevo personaje en el sistema</p>
            </div>
          </div>
        </div>
        
        <div v-else-if="loading" class="loading-state">
          <div class="loading-spinner"></div>
          <p class="loading-text">Cargando tus agentes...</p>
        </div>
        
        <div v-else class="empty-state">
          <div class="empty-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="#fc6f03" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
          </div>
          <h3 class="empty-title">No tienes agentes registrados</h3>
          <p class="empty-text" v-if="searchQuery">
            No hay agentes que coincidan con "{{ searchQuery }}"
          </p>
          <p class="empty-text" v-else>
            Comienza registrando tu primer agente en el sistema.
          </p>
          <button class="action-button" @click="showCreateForm = true">
            <span class="button-text">REGISTRAR PRIMER AGENTE</span>
            <div class="button-indicator">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="9 18 15 12 9 6"></polyline>
              </svg>
            </div>
          </button>
        </div>
      </div>

      <!-- Vista: Detalle del personaje -->
      <div v-else-if="selectedCharacter" class="character-detail-view">
        <div class="detail-header">
          <button class="back-button" @click="selectedCharacter = null">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="19" y1="12" x2="5" y2="12"></line>
              <polyline points="12 19 5 12 12 5"></polyline>
            </svg>
            <span>Volver</span>
          </button>
          
          <div class="header-actions" v-if="selectedCharacter.is_owner">
            <button class="edit-button" @click="showEditForm = true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
              </svg>
              <span>Editar</span>
            </button>
            
            <button class="delete-button" @click="confirmDeleteCharacter">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="3 6 5 6 21 6"></polyline>
                <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                <line x1="10" y1="11" x2="10" y2="17"></line>
                <line x1="14" y1="11" x2="14" y2="17"></line>
              </svg>
              <span>Eliminar</span>
            </button>
          </div>
        </div>
        
        <div class="character-detail-content">
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
                <span class="detail-label">Fecha de Nacimiento:</span>
                <span class="detail-value">{{ selectedCharacter.birth_date }} ({{ selectedCharacter.age }} años)</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Facción:</span>
                <span class="detail-value faction">{{ selectedCharacter.faction }}</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Owner:</span>
                <span class="detail-value owner-link" @click="viewUser(selectedCharacter.owner_id)">
                  {{ selectedCharacter.owner_username }}
                </span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Registrado:</span>
                <span class="detail-value">{{ formatDate(selectedCharacter.created_at) }}</span>
              </div>
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
                <span class="morph-value">{{ selectedCharacter.nvg_color }}</span>
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
                <span class="morph-value">RGB({{ selectedCharacter.skin_r }}, {{ selectedCharacter.skin_g }}, {{ selectedCharacter.skin_b }})</span>
              </div>
              <div class="morph-item" v-if="selectedCharacter.ntag">
                <span class="morph-label">NTag:</span>
                <span class="morph-value">{{ selectedCharacter.ntag }}</span>
              </div>
              <div class="morph-item" v-if="selectedCharacter.cntag_r !== null">
                <span class="morph-label">CNTag Color:</span>
                <span class="morph-value">RGB({{ selectedCharacter.cntag_r }}, {{ selectedCharacter.cntag_g }}, {{ selectedCharacter.cntag_b }})</span>
              </div>
              <div class="morph-item" v-if="selectedCharacter.rtag">
                <span class="morph-label">RTag:</span>
                <span class="morph-value">{{ selectedCharacter.rtag }}</span>
              </div>
              <div class="morph-item" v-if="selectedCharacter.crtag_r !== null">
                <span class="morph-label">CRTag Color:</span>
                <span class="morph-value">RGB({{ selectedCharacter.crtag_r }}, {{ selectedCharacter.crtag_g }}, {{ selectedCharacter.crtag_b }})</span>
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
              <button class="copy-button" @click="copyMorphCommand">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                  <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                </svg>
                <span>Copiar Comando</span>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Modal: Crear/Editar Personaje -->
      <div v-if="showCreateForm || showEditForm" class="modal-overlay" @click.self="closeModal">
        <div class="modal-content character-form-modal" @click.stop>
          <div class="modal-header">
            <h3 class="modal-title">{{ showEditForm ? 'EDITAR AGENTE' : 'REGISTRAR NUEVO AGENTE' }}</h3>
            <button class="modal-close" @click="closeModal">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
              </svg>
            </button>
          </div>
          
          <form @submit.prevent="submitCharacterForm" class="character-form">
            <div class="form-section">
              <h4 class="form-section-title">Información Básica</h4>
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
                    type="date"
                    class="form-input"
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
              <h4 class="form-section-title">Datos Morph (al menos uno requerido)</h4>
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
                  <label class="form-label">NVG Color</label>
                  <input
                    v-model="characterForm.nvg_color"
                    type="text"
                    class="form-input"
                    placeholder="Ej: Bright orange"
                  />
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
                    v.model="characterForm.ntag"
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
                      v.model.number="characterForm.cntag_g"
                      type="number"
                      min="0"
                      max="255"
                      class="color-input"
                      placeholder="G"
                    />
                    <input
                      v.model.number="characterForm.cntag_b"
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
                    v.model="characterForm.rtag"
                    class="form-textarea"
                    placeholder="Texto para RTag (puede ser largo)"
                    rows="2"
                  ></textarea>
                </div>
                
                <div class="form-group">
                  <label class="form-label">CRTag Color (RGB)</label>
                  <div class="color-inputs">
                    <input
                      v.model.number="characterForm.crtag_r"
                      type="number"
                      min="0"
                      max="255"
                      class="color-input"
                      placeholder="R"
                    />
                    <input
                      v.model.number="characterForm.crtag_g"
                      type="number"
                      min="0"
                      max="255"
                      class="color-input"
                      placeholder="G"
                    />
                    <input
                      v.model.number="characterForm.crtag_b"
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
            
            <div class="form-actions">
              <button type="button" class="cancel-button" @click="closeModal">
                Cancelar
              </button>
              <button type="submit" class="submit-button" :disabled="submitting">
                <span v-if="submitting">Procesando...</span>
                <span v-else>{{ showEditForm ? 'ACTUALIZAR AGENTE' : 'REGISTRAR AGENTE' }}</span>
              </button>
            </div>
          </form>
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
              Cancelar
            </button>
            <button class="confirm-delete" @click="deleteCharacter">
              Eliminar Agente
            </button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, watch, computed } from 'vue'
import { debounce } from 'lodash'

const props = defineProps({
  currentUser: {
    type: Object,
    required: true
  }
})

// Estado principal
const activeView = ref('all')
const characters = ref([])
const myCharacters = ref([])
const selectedCharacter = ref(null)
const loading = ref(false)
const searchQuery = ref('')
const showCreateForm = ref(false)
const showEditForm = ref(false)
const showDeleteConfirm = ref(false)
const submitting = ref(false)

// Formulario
const characterForm = reactive({
  first_name: '',
  last_name: '',
  country: '',
  birth_date: '',
  codename: '',
  faction: '',
  morph: '',
  hat: '',
  nvg_color: '',
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
  rhat: false
})

// Métodos
const setActiveView = (view) => {
  activeView.value = view
  selectedCharacter.value = null
  searchQuery.value = ''
  loadCharacters()
}

const loadCharacters = async () => {
  loading.value = true
  try {
    let endpoint = '/api/characters/all/'
    if (activeView.value === 'mine') {
      endpoint = '/api/characters/mine/'
    }
    
    const response = await fetch(`${endpoint}?search=${searchQuery.value}`)
    const data = await response.json()
    
    if (activeView.value === 'all') {
      characters.value = data.results || []
    } else {
      myCharacters.value = data.results || []
    }
  } catch (error) {
    console.error('Error loading characters:', error)
  } finally {
    loading.value = false
  }
}

const debouncedSearch = debounce(loadCharacters, 500)

const viewCharacter = async (character) => {
  try {
    const response = await fetch(`/api/characters/${character.id}/`)
    const data = await response.json()
    selectedCharacter.value = data
  } catch (error) {
    console.error('Error loading character details:', error)
  }
}

const viewUser = (userId) => {
  // Esto redirigirá al perfil del usuario cuando se implemente
  console.log('Viewing user:', userId)
  alert(`Redirigiendo al perfil del usuario ID: ${userId}`)
}

const copyMorphCommand = async () => {
  if (selectedCharacter.value?.morph_command) {
    try {
      await navigator.clipboard.writeText(selectedCharacter.value.morph_command)
      alert('Comando copiado al portapapeles')
    } catch (error) {
      console.error('Error copying to clipboard:', error)
    }
  }
}

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('es-ES', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const resetCharacterForm = () => {
  Object.keys(characterForm).forEach(key => {
    if (key === 'rhat') {
      characterForm[key] = false
    } else {
      characterForm[key] = ''
    }
  })
}

const openEditForm = () => {
  if (selectedCharacter.value) {
    Object.keys(characterForm).forEach(key => {
      characterForm[key] = selectedCharacter.value[key] || ''
    })
    showEditForm.value = true
  }
}

const closeModal = () => {
  showCreateForm.value = false
  showEditForm.value = false
  resetCharacterForm()
}

const submitCharacterForm = async () => {
  submitting.value = true
  
  try {
    const formData = { ...characterForm }
    
    // Convertir valores vacíos a null para campos numéricos
    const numericFields = ['skin_r', 'skin_g', 'skin_b', 'cntag_r', 'cntag_g', 'cntag_b', 'crtag_r', 'crtag_g', 'crtag_b']
    numericFields.forEach(field => {
      formData[field] = formData[field] === '' ? null : Number(formData[field])
    })
    
    // Verificar que haya al menos un campo de morph
    const morphFields = [
      formData.morph,
      formData.hat,
      formData.nvg_color,
      formData.shirt,
      formData.pants,
      formData.ntag,
      formData.rtag,
    ]
    
    if (!morphFields.some(field => field && field.trim() !== '')) {
      alert('Error: Al menos un campo de morph debe estar definido.')
      submitting.value = false
      return
    }
    
    let endpoint = '/api/characters/create/'
    let method = 'POST'
    
    if (showEditForm.value && selectedCharacter.value) {
      endpoint = `/api/characters/${selectedCharacter.value.id}/update/`
      method = 'PUT'
    }
    
    const response = await fetch(endpoint, {
      method: method,
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken()
      },
      body: JSON.stringify(formData)
    })
    
    const data = await response.json()
    
    if (response.ok) {
      alert(showEditForm.value ? 'Agente actualizado correctamente' : 'Agente registrado correctamente')
      closeModal()
      loadCharacters()
      
      if (showEditForm.value && selectedCharacter.value) {
        // Recargar los detalles del personaje
        viewCharacter(selectedCharacter.value)
      }
    } else {
      alert(`Error: ${data.error || 'Error desconocido'}`)
    }
  } catch (error) {
    console.error('Error submitting form:', error)
    alert('Error al procesar la solicitud')
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
    const response = await fetch(`/api/characters/${selectedCharacter.value.id}/delete/`, {
      method: 'DELETE',
      headers: {
        'X-CSRFToken': getCSRFToken()
      }
    })
    
    if (response.ok) {
      alert('Agente eliminado correctamente')
      selectedCharacter.value = null
      showDeleteConfirm.value = false
      loadCharacters()
    } else {
      const data = await response.json()
      alert(`Error: ${data.error || 'Error al eliminar'}`)
    }
  } catch (error) {
    console.error('Error deleting character:', error)
    alert('Error al eliminar el agente')
  }
}

const getCSRFToken = () => {
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')
  return csrfToken ? csrfToken.value : ''
}

// Watchers
watch(searchQuery, () => {
  debouncedSearch()
})

watch(showEditForm, (newValue) => {
  if (newValue && selectedCharacter.value) {
    openEditForm()
  }
})

// Lifecycle
onMounted(() => {
  loadCharacters()
})
</script>

<style scoped>
.personajes-container {
  display: flex;
  width: 100%;
  height: 100%;
  background: rgba(20, 20, 20, 0.8);
}

/* Sidebar */
.personajes-sidebar {
  width: 280px;
  background: rgba(25, 25, 25, 0.9);
  border-right: 1px solid #333;
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
}

.sidebar-header {
  padding: 24px 20px;
  border-bottom: 1px solid #333;
  background: rgba(30, 30, 30, 0.6);
}

.sidebar-title {
  font-size: 16px;
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
}

.tool-item {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px 20px;
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

/* Área principal */
.personajes-main {
  flex: 1;
  padding: 24px;
  overflow-y: auto;
}

.view-header {
  margin-bottom: 32px;
  padding-bottom: 20px;
  border-bottom: 1px solid rgba(252, 111, 3, 0.3);
}

.view-title {
  font-size: 28px;
  font-weight: 700;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 8px 0;
}

.view-subtitle {
  font-size: 15px;
  color: #aaa;
}

/* Barra de búsqueda */
.search-bar {
  margin-bottom: 32px;
}

.search-container {
  position: relative;
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  border-radius: 8px;
  padding: 12px 16px;
  display: flex;
  align-items: center;
  gap: 12px;
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
  font-size: 14px;
  font-family: inherit;
  outline: none;
}

.search-input::placeholder {
  color: #666;
}

.search-count {
  font-size: 12px;
  color: #888;
  font-family: 'Consolas', monospace;
  white-space: nowrap;
}

/* Grid de personajes */
.characters-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.character-card {
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  border-radius: 8px;
  padding: 20px;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.character-card:hover {
  transform: translateY(-2px);
  border-color: #fc6f03;
  box-shadow: 0 4px 12px rgba(252, 111, 3, 0.1);
}

.character-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: #fc6f03;
  opacity: 0.8;
}

.character-card.add-new {
  border-style: dashed;
  border-color: #666;
  background: rgba(30, 30, 30, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 200px;
}

.character-card.add-new:hover {
  border-color: #fc6f03;
  background: rgba(252, 111, 3, 0.05);
}

.add-new-content {
  text-align: center;
  padding: 20px;
}

.add-icon {
  width: 48px;
  height: 48px;
  color: #fc6f03;
  margin: 0 auto 16px;
  opacity: 0.8;
}

.add-title {
  font-size: 18px;
  font-weight: 700;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 8px 0;
}

.add-text {
  font-size: 14px;
  color: #aaa;
  margin: 0;
}

.character-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 16px;
}

.character-name {
  font-size: 18px;
  font-weight: 700;
  color: #fff;
  margin: 0;
}

.character-faction {
  font-size: 12px;
  color: #fc6f03;
  background: rgba(252, 111, 3, 0.1);
  padding: 4px 8px;
  border-radius: 4px;
  border: 1px solid rgba(252, 111, 3, 0.3);
  font-family: 'Consolas', monospace;
  letter-spacing: 0.3px;
  white-space: nowrap;
}

.character-info {
  margin-bottom: 16px;
}

.info-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.info-row:last-child {
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
  color: #ddd;
  font-weight: 500;
}

.owner-link {
  color: #4CAF50;
  cursor: pointer;
  text-decoration: underline;
  transition: color 0.3s ease;
}

.owner-link:hover {
  color: #66BB6A;
}

.character-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
}

.character-id {
  font-size: 11px;
  color: #666;
  font-family: 'Consolas', monospace;
}

.view-button {
  width: 24px;
  height: 24px;
  color: #fc6f03;
  opacity: 0.8;
}

/* Estados de carga y vacío */
.loading-state,
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  text-align: center;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid rgba(252, 111, 3, 0.3);
  border-top: 3px solid #fc6f03;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 16px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-text {
  font-size: 15px;
  color: #aaa;
  margin: 0;
}

.empty-icon {
  width: 60px;
  height: 60px;
  color: #fc6f03;
  opacity: 0.8;
  margin-bottom: 20px;
}

.empty-title {
  font-size: 20px;
  font-weight: 700;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 12px 0;
}

.empty-text {
  font-size: 15px;
  color: #aaa;
  margin: 0 0 24px 0;
  max-width: 400px;
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

/* Vista de detalle del personaje */
.character-detail-view {
  width: 100%;
}

.detail-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 32px;
  padding-bottom: 20px;
  border-bottom: 1px solid rgba(252, 111, 3, 0.3);
}

.back-button {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: rgba(40, 40, 40, 0.6);
  border: 1px solid #444;
  border-radius: 6px;
  color: #aaa;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
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

.header-actions {
  display: flex;
  gap: 12px;
}

.edit-button,
.delete-button {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
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

.edit-button svg,
.delete-button svg {
  width: 16px;
  height: 16px;
}

.character-detail-content {
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.detail-section {
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  border-radius: 8px;
  padding: 24px;
}

.section-title {
  font-size: 18px;
  font-weight: 700;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 20px 0;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(252, 111, 3, 0.3);
}

.detail-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 16px;
}

.detail-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.detail-label {
  font-size: 12px;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.detail-value {
  font-size: 15px;
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
  padding: 4px 8px;
  border-radius: 4px;
  border: 1px solid rgba(252, 111, 3, 0.3);
  display: inline-block;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.3px;
}

.morph-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 12px;
}

.morph-item {
  padding: 12px;
  background: rgba(40, 40, 40, 0.6);
  border: 1px solid #444;
  border-radius: 6px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.morph-label {
  font-size: 11px;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.morph-value {
  font-size: 14px;
  color: #ddd;
  font-weight: 500;
  word-break: break-all;
}

.morph-command-container {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.command-preview {
  background: rgba(20, 20, 20, 0.8);
  border: 1px solid #444;
  border-radius: 6px;
  padding: 16px;
  overflow-x: auto;
}

.command-text {
  font-family: 'Consolas', monospace;
  font-size: 14px;
  color: #4CAF50;
  white-space: nowrap;
}

.copy-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 24px;
  background: rgba(76, 175, 80, 0.1);
  border: 1px solid rgba(76, 175, 80, 0.3);
  border-radius: 6px;
  color: #4CAF50;
  font-size: 14px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  cursor: pointer;
  transition: all 0.3s ease;
  align-self: flex-start;
}

.copy-button:hover {
  background: rgba(76, 175, 80, 0.2);
  border-color: rgba(76, 175, 80, 0.5);
}

.copy-button svg {
  width: 16px;
  height: 16px;
}

/* Modal y formulario */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(5px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.character-form-modal {
  background: rgba(25, 25, 25, 0.95);
  border: 1px solid #fc6f03;
  border-radius: 8px;
  padding: 30px;
  max-width: 900px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  animation: slideUp 0.3s ease;
}

@keyframes slideUp {
  from { 
    opacity: 0;
    transform: translateY(20px);
  }
  to { 
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  padding-bottom: 16px;
  border-bottom: 1px solid rgba(252, 111, 3, 0.3);
}

.modal-title {
  font-size: 22px;
  font-weight: 700;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0;
}

.modal-close {
  background: transparent;
  border: none;
  color: #aaa;
  cursor: pointer;
  padding: 4px;
  transition: color 0.3s ease;
}

.modal-close:hover {
  color: #fc6f03;
}

.modal-close svg {
  width: 20px;
  height: 20px;
}

.form-section {
  margin-bottom: 32px;
}

.form-section-title {
  font-size: 16px;
  font-weight: 600;
  color: #fc6f03;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 16px 0;
  padding-bottom: 8px;
  border-bottom: 1px solid rgba(252, 111, 3, 0.2);
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 16px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.form-label {
  font-size: 13px;
  color: #ccc;
  font-weight: 500;
}

.form-input,
.form-textarea {
  background: rgba(40, 40, 40, 0.6);
  border: 1px solid #444;
  border-radius: 6px;
  padding: 10px 12px;
  color: #fff;
  font-size: 14px;
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
  min-height: 80px;
}

.form-hint {
  font-size: 11px;
  color: #888;
  font-style: italic;
}

.color-inputs {
  display: flex;
  gap: 8px;
}

.color-input {
  flex: 1;
  background: rgba(40, 40, 40, 0.6);
  border: 1px solid #444;
  border-radius: 6px;
  padding: 10px;
  color: #fff;
  font-size: 14px;
  text-align: center;
  font-family: inherit;
}

.color-input::placeholder {
  color: #666;
}

.color-input:focus {
  outline: none;
  border-color: #fc6f03;
}

.checkbox-group {
  flex-direction: row;
  align-items: center;
  margin-top: 8px;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
}

.checkbox-input {
  width: 18px;
  height: 18px;
  accent-color: #fc6f03;
}

.checkbox-text {
  font-size: 14px;
  color: #ccc;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 32px;
  padding-top: 24px;
  border-top: 1px solid #444;
}

.cancel-button,
.submit-button {
  padding: 12px 24px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
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

/* Modal de confirmación */
.confirm-modal {
  background: rgba(25, 25, 25, 0.95);
  border: 1px solid #aa2222;
  border-radius: 8px;
  padding: 40px;
  max-width: 500px;
  width: 100%;
  text-align: center;
  animation: slideUp 0.3s ease;
}

.confirm-icon {
  width: 60px;
  height: 60px;
  color: #aa2222;
  margin: 0 auto 20px;
}

.confirm-title {
  font-size: 20px;
  font-weight: 700;
  color: #aa2222;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 16px 0;
}

.confirm-text {
  font-size: 15px;
  color: #ccc;
  line-height: 1.5;
  margin: 0 0 24px 0;
}

.confirm-text strong {
  color: #fff;
}

.confirm-actions {
  display: flex;
  justify-content: center;
  gap: 16px;
}

.confirm-cancel,
.confirm-delete {
  padding: 12px 24px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
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

/* Responsive */
@media (max-width: 1024px) {
  .personajes-sidebar {
    width: 240px;
  }
  
  .characters-grid {
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  }
  
  .form-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  }
}

@media (max-width: 768px) {
  .personajes-container {
    flex-direction: column;
  }
  
  .personajes-sidebar {
    width: 100%;
    border-right: none;
    border-bottom: 1px solid #333;
  }
  
  .sidebar-tools {
    display: flex;
    overflow-x: auto;
    padding: 16px 0;
  }
  
  .tool-item {
    flex: 0 0 auto;
    width: auto;
    padding: 12px 16px;
    white-space: nowrap;
  }
  
  .characters-grid {
    grid-template-columns: 1fr;
  }
  
  .character-form-modal {
    padding: 20px;
    max-height: 80vh;
  }
  
  .form-grid {
    grid-template-columns: 1fr;
  }
  
  .form-actions {
    flex-direction: column;
  }
  
  .confirm-actions {
    flex-direction: column;
  }
}
</style>