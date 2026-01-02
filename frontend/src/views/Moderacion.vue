<template>
  <div class="moderacion-page">
    <!-- Fondo SCP -->
    <div class="site-background">
      <div class="grid-overlay"></div>
      <div class="scan-line"></div>
      <div class="particles"></div>
    </div>

    <!-- Header -->
    <div class="moderacion-header">
      <div class="header-left">
        <div class="header-logo">
          <div class="header-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="#ff3333" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"></circle>
              <path d="M12 8v4"></path>
              <path d="M12 16h.01"></path>
            </svg>
          </div>
          <div class="header-title">
            <span class="header-main">MODERATION CONTROL</span>
            <span class="header-sub">SECURITY & COMPLIANCE DIVISION</span>
          </div>
        </div>
      </div>
      
      <div class="header-right">
        <div class="session-status">
          <div class="session-indicator active"></div>
          <span class="session-text">{{ userRole?.toUpperCase() || 'UNAUTHORIZED' }}</span>
        </div>
        <div class="current-time">
          {{ currentTime }}
        </div>
      </div>
    </div>

    <!-- Contenido Principal - Tarjetas de Mods -->
    <main class="moderacion-main">
      <div class="moderacion-header-section">
        <h1 class="moderacion-title">MODERATION PANEL</h1>
        <div class="moderacion-subtitle">AUTHORIZED MODERATION FUNCTIONS</div>
        
        <!-- Estadísticas Rápidas -->
        <div class="quick-stats">
          <div class="stat-item">
            <div class="stat-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14 2 14 8 20 8"></polyline>
                <line x1="16" y1="13" x2="8" y2="13"></line>
                <line x1="16" y1="17" x2="8" y2="17"></line>
                <polyline points="10 9 9 9 8 9"></polyline>
              </svg>
            </div>
            <div class="stat-info">
              <span class="stat-label">ACTIVE WARNS</span>
              <span class="stat-value">{{ stats.activeWarns || 0 }}</span>
            </div>
          </div>
          
          <div class="stat-item">
            <div class="stat-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
              </svg>
            </div>
            <div class="stat-info">
              <span class="stat-label">ACTIVE BANS</span>
              <span class="stat-value">{{ stats.activeBans || 0 }}</span>
            </div>
          </div>
          
          <div class="stat-item">
            <div class="stat-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
              </svg>
            </div>
            <div class="stat-info">
              <span class="stat-label">PENDING APPEALS</span>
              <span class="stat-value">{{ stats.pendingAppeals || 0 }}</span>
            </div>
          </div>
          
          <div class="stat-item">
            <div class="stat-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                <circle cx="9" cy="7" r="4"></circle>
                <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
              </svg>
            </div>
            <div class="stat-info">
              <span class="stat-label">TOP WARNED</span>
              <span class="stat-value">{{ stats.topWarnedUsers || 0 }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Grid de Funciones de Moderación -->
      <div class="moderation-grid">
        <!-- Tarjeta 1: Admin -->
        <div class="moderation-card" :class="{ 'active': activeCard === 9 }" @click="activateCard(9)">
        <div class="card-header">
            <div class="card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                <path d="M12 8v4"></path>
                <path d="M12 16h.01"></path>
            </svg>
            </div>
            <div class="card-title">PERMISSION MANAGEMENT</div>
            <div class="card-status" v-if="hasPermission('full_moderation_control')">
            <span class="status-active">ACCESS GRANTED</span>
            </div>
        </div>
        <div class="card-content">
            <p class="card-description">Manage user permissions, assign moderation roles, and control access levels.</p>
            <div class="card-meta">
            <span class="meta-label">REQUIRED PERMISSION:</span>
            <span class="meta-value" :class="hasPermission('full_moderation_control') ? 'authorized' : 'denied'">
                {{ hasPermission('full_moderation_control') ? 'full_moderation_control' : 'INSUFFICIENT' }}
            </span>
            </div>
        </div>
        <div class="card-footer">
            <div class="card-action">
            <button 
                class="action-button" 
                @click.stop="goToPermissionManagement"
                :disabled="!hasPermission('full_moderation_control')"
                :class="{ 'disabled': !hasPermission('full_moderation_control') }"
            >
                <span class="button-text">ACCESS SYSTEM</span>
                <div class="button-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="9 18 15 12 9 6"></polyline>
                </svg>
                </div>
            </button>
            </div>
        </div>
        </div>

        <!-- Tarjeta 2: Gestión de Bans -->
        <div class="moderation-card" :class="{ 'active': activeCard === 2 }" @click="activateCard(2)">
          <div class="card-header">
            <div class="card-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
              </svg>
            </div>
            <div class="card-title">BAN MANAGEMENT</div>
            <div class="card-status" v-if="hasPermission('register_ban')">
              <span class="status-active">ACCESS GRANTED</span>
            </div>
          </div>
          <div class="card-content">
            <p class="card-description">Issue temporary or permanent bans, manage ban durations and appeal systems.</p>
            <div class="card-meta">
              <span class="meta-label">REQUIRED PERMISSION:</span>
              <span class="meta-value" :class="hasPermission('register_ban') ? 'authorized' : 'denied'">
                {{ hasPermission('register_ban') ? 'register_ban' : 'INSUFFICIENT' }}
              </span>
            </div>
          </div>
          <div class="card-footer">
            <div class="card-action">
              <button 
                class="action-button" 
                @click.stop="goToBanManagement"
                :disabled="!hasPermission('register_ban')"
                :class="{ 'disabled': !hasPermission('register_ban') }"
              >
                <span class="button-text">ACCESS SYSTEM</span>
                <div class="button-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="9 18 15 12 9 6"></polyline>
                  </svg>
                </div>
              </button>
            </div>
          </div>
        </div>

        <!-- Tarjeta 3: Dashboard de Moderación -->
        <div class="moderation-card" :class="{ 'active': activeCard === 3 }" @click="activateCard(3)">
          <div class="card-header">
            <div class="card-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="3" y1="9" x2="21" y2="9"></line>
                <line x1="9" y1="21" x2="9" y2="9"></line>
              </svg>
            </div>
            <div class="card-title">MODERATION DASHBOARD</div>
            <div class="card-status" v-if="hasPermission('access_moderation_dashboard')">
              <span class="status-active">ACCESS GRANTED</span>
            </div>
          </div>
          <div class="card-content">
            <p class="card-description">Global moderation overview with statistics, user tracking, and system monitoring.</p>
            <div class="card-meta">
              <span class="meta-label">REQUIRED PERMISSION:</span>
              <span class="meta-value" :class="hasPermission('access_moderation_dashboard') ? 'authorized' : 'denied'">
                {{ hasPermission('access_moderation_dashboard') ? 'access_moderation_dashboard' : 'INSUFFICIENT' }}
              </span>
            </div>
          </div>
          <div class="card-footer">
            <div class="card-action">
              <button 
                class="action-button" 
                @click.stop="goToGlobalModeration"
                :disabled="!hasPermission('access_moderation_dashboard')"
                :class="{ 'disabled': !hasPermission('access_moderation_dashboard') }"
              >
                <span class="button-text">ACCESS SYSTEM</span>
                <div class="button-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="9 18 15 12 9 6"></polyline>
                  </svg>
                </div>
              </button>
            </div>
          </div>
        </div>

        <!-- Tarjeta 4: Gestión de Apelaciones -->
        <div class="moderation-card" :class="{ 'active': activeCard === 4 }" @click="activateCard(4)">
          <div class="card-header">
            <div class="card-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                <path d="M13 8H7"></path>
                <path d="M17 12H7"></path>
              </svg>
            </div>
            <div class="card-title">APPEAL MANAGEMENT</div>
            <div class="card-status" v-if="hasPermission('manage_warns')">
              <span class="status-active">ACCESS GRANTED</span>
            </div>
          </div>
          <div class="card-content">
            <p class="card-description">Review and respond to user appeals for warnings and ban modifications.</p>
            <div class="card-meta">
              <span class="meta-label">REQUIRED PERMISSION:</span>
              <span class="meta-value" :class="hasPermission('manage_warns') ? 'authorized' : 'denied'">
                {{ hasPermission('manage_warns') ? 'manage_warns' : 'INSUFFICIENT' }}
              </span>
            </div>
          </div>
          <div class="card-footer">
            <div class="card-action">
              <button 
                class="action-button" 
                @click.stop="goToAppealManagement"
                :disabled="!hasPermission('manage_warns')"
                :class="{ 'disabled': !hasPermission('manage_warns') }"
              >
                <span class="button-text">ACCESS SYSTEM</span>
                <div class="button-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="9 18 15 12 9 6"></polyline>
                  </svg>
                </div>
              </button>
            </div>
          </div>
        </div>

        <!-- Tarjeta 5: Moderación en Juego -->
        <div class="moderation-card" :class="{ 'active': activeCard === 5 }" @click="activateCard(5)">
          <div class="card-header">
            <div class="card-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
                <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
              </svg>
            </div>
            <div class="card-title">IN-GAME MODERATION</div>
            <div class="card-status" v-if="hasPermission('view_characters_basic')">
              <span class="status-active">ACCESS GRANTED</span>
            </div>
          </div>
          <div class="card-content">
            <p class="card-description">Monitor in-game characters, verify identities, and manage roleplay compliance.</p>
            <div class="card-meta">
              <span class="meta-label">REQUIRED PERMISSION:</span>
              <span class="meta-value" :class="hasPermission('view_characters_basic') ? 'authorized' : 'denied'">
                {{ hasPermission('view_characters_basic') ? 'view_characters_basic' : 'INSUFFICIENT' }}
              </span>
            </div>
          </div>
          <div class="card-footer">
            <div class="card-action">
              <button 
                class="action-button" 
                @click.stop="goToInGameModeration"
                :disabled="!hasPermission('view_characters_basic')"
                :class="{ 'disabled': !hasPermission('view_characters_basic') }"
              >
                <span class="button-text">ACCESS SYSTEM</span>
                <div class="button-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="9 18 15 12 9 6"></polyline>
                  </svg>
                </div>
              </button>
            </div>
          </div>
        </div>

        <!-- Tarjeta 6: Moderación de Discord -->
        <div class="moderation-card" :class="{ 'active': activeCard === 6 }" @click="activateCard(6)">
          <div class="card-header">
            <div class="card-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                <line x1="10" y1="9" x2="14" y2="9"></line>
                <line x1="12" y1="7" x2="12" y2="11"></line>
              </svg>
            </div>
            <div class="card-title">DISCORD MODERATION</div>
            <div class="card-status" v-if="hasPermission('full_discord_moderation')">
              <span class="status-active">ACCESS GRANTED</span>
            </div>
          </div>
          <div class="card-content">
            <p class="card-description">Manage Discord-specific warnings, bans, and community compliance enforcement.</p>
            <div class="card-meta">
              <span class="meta-label">REQUIRED PERMISSION:</span>
              <span class="meta-value" :class="hasPermission('full_discord_moderation') ? 'authorized' : 'denied'">
                {{ hasPermission('full_discord_moderation') ? 'full_discord_moderation' : 'INSUFFICIENT' }}
              </span>
            </div>
          </div>
          <div class="card-footer">
            <div class="card-action">
              <button 
                class="action-button" 
                @click.stop="goToDiscordModeration"
                :disabled="!hasPermission('full_discord_moderation')"
                :class="{ 'disabled': !hasPermission('full_discord_moderation') }"
              >
                <span class="button-text">ACCESS SYSTEM</span>
                <div class="button-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="9 18 15 12 9 6"></polyline>
                  </svg>
                </div>
              </button>
            </div>
          </div>
        </div>

        <!-- Tarjeta 7: Logs de Auditoría -->
        <div class="moderation-card" :class="{ 'active': activeCard === 7 }" @click="activateCard(7)">
          <div class="card-header">
            <div class="card-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
              </svg>
            </div>
            <div class="card-title">AUDIT LOGS</div>
            <div class="card-status" v-if="hasPermission('full_moderation_control')">
              <span class="status-active">ACCESS GRANTED</span>
            </div>
          </div>
          <div class="card-content">
            <p class="card-description">Complete audit trail of all moderation actions, modifications, and system changes.</p>
            <div class="card-meta">
              <span class="meta-label">REQUIRED PERMISSION:</span>
              <span class="meta-value" :class="hasPermission('full_moderation_control') ? 'authorized' : 'denied'">
                {{ hasPermission('full_moderation_control') ? 'full_moderation_control' : 'INSUFFICIENT' }}
              </span>
            </div>
          </div>
          <div class="card-footer">
            <div class="card-action">
              <button 
                class="action-button" 
                @click.stop="goToAuditLogs"
                :disabled="!hasPermission('full_moderation_control')"
                :class="{ 'disabled': !hasPermission('full_moderation_control') }"
              >
                <span class="button-text">ACCESS SYSTEM</span>
                <div class="button-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="9 18 15 12 9 6"></polyline>
                  </svg>
                </div>
              </button>
            </div>
          </div>
        </div>

        <!-- Tarjeta 8: [REDACTED] -->
        <div class="moderation-card redacted" :class="{ 'active': activeCard === 8 }" @click="showAccessDenied(8)">
          <div class="card-header redacted">
            <div class="card-icon redacted">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <path d="M4.93 4.93l14.14 14.14"></path>
              </svg>
            </div>
            <div class="card-title redacted-text">[REDACTED]</div>
            <div class="card-status">
              <span class="status-redacted">CLASSIFIED</span>
            </div>
          </div>
          <div class="card-content redacted">
            <p class="card-description redacted-text">This function requires Level 5 clearance and administrative authorization.</p>
            <div class="card-meta">
              <span class="meta-label">CLEARANCE:</span>
              <span class="meta-value redacted">LEVEL 5+</span>
            </div>
          </div>
          <div class="card-footer redacted">
            <div class="clearance-warning">
              <div class="warning-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="#aa2222" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"></circle>
                  <line x1="12" y1="8" x2="12" y2="12"></line>
                  <line x1="12" y1="16" x2="12.01" y2="16"></line>
                </svg>
              </div>
              <span class="warning-text">ADMINISTRATIVE CLEARANCE REQUIRED</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Información del Usuario -->
      <div class="user-info-panel">
        <div class="info-header">
          <h3 class="info-title">MODERATOR PROFILE</h3>
          <div class="info-subtitle">CURRENT SESSION INFORMATION</div>
        </div>
        <div class="info-grid">
          <div class="info-item">
            <span class="info-label">MODERATOR ID:</span>
            <span class="info-value">{{ currentUser?.roblox_username || 'GUEST' }}</span>
          </div>
          <div class="info-item">
            <span class="info-label">CLEARANCE LEVEL:</span>
            <span class="info-value">{{ getClearanceLevel() }}</span>
          </div>
          <div class="info-item">
            <span class="info-label">PERMISSIONS:</span>
            <span class="info-value permissions">{{ getUserPermissions().length }}</span>
          </div>
          <div class="info-item">
            <span class="info-label">SCOPES:</span>
            <span class="info-value scopes">{{ getUserScopes().length }}</span>
          </div>
          <div class="info-item">
            <span class="info-label">SESSION START:</span>
            <span class="info-value">{{ sessionStartTime }}</span>
          </div>
          <div class="info-item">
            <span class="info-label">SESSION DURATION:</span>
            <span class="info-value">{{ sessionDuration }}</span>
          </div>
        </div>
        
        <!-- Permisos Detallados -->
        <div class="permissions-panel" v-if="getUserPermissions().length > 0">
          <h4 class="permissions-title">ACTIVE PERMISSIONS</h4>
          <div class="permissions-grid">
            <span 
              v-for="(permission, index) in getUserPermissions()" 
              :key="index"
              class="permission-tag"
              :class="getPermissionType(permission)"
            >
              {{ permission }}
            </span>
          </div>
        </div>
      </div>
    </main>

    <!-- Modal de Acceso Denegado -->
    <div v-if="showDeniedModal" class="access-denied-modal">
      <div class="modal-overlay" @click="closeModal"></div>
      <div class="modal-content">
        <div class="modal-header">
          <div class="modal-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="#aa2222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="15" y1="9" x2="9" y2="15"></line>
              <line x1="9" y1="9" x2="15" y2="15"></line>
            </svg>
          </div>
          <h3 class="modal-title">ACCESS RESTRICTED</h3>
        </div>
        <div class="modal-body">
          <p class="modal-text">You do not have the required permissions to access this function.</p>
          <div class="clearance-info">
            <div class="clearance-item">
              <span class="clearance-label">CURRENT CLEARANCE:</span>
              <span class="clearance-value">{{ getClearanceLevel() }}</span>
            </div>
            <div class="clearance-item">
              <span class="clearance-label">REQUIRED PERMISSION:</span>
              <span class="clearance-value denied">INSUFFICIENT</span>
            </div>
            <div class="clearance-item">
              <span class="clearance-label">STATUS:</span>
              <span class="clearance-value denied">ACCESS DENIED</span>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button class="modal-button" @click="closeModal">
            <span class="button-text">ACKNOWLEDGE</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, onUnmounted, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// Estado principal
const activeCard = ref(1)
const currentUser = ref(null)
const currentTime = ref('')
const sessionStartTime = ref('')
const sessionDuration = ref('00:00:00')
const showDeniedModal = ref(false)
const stats = reactive({
  activeWarns: 0,
  activeBans: 0,
  pendingAppeals: 0,
  topWarnedUsers: 0
})

// Permisos del usuario (simulados - en producción vendrían del backend)
const userPermissions = ref([
  'create_warn',
  'access_moderation_dashboard',
  'view_characters_basic'
])

// Scopes del usuario (simulados)
const userScopes = ref([
  { scope: 'ingame', level: 2 },
  { scope: 'moderation', level: 1 }
])

// Computed
const userRole = computed(() => {
  if (!currentUser.value) return null
  if (currentUser.value.is_superuser) return 'ADMINISTRATOR'
  if (currentUser.value.is_staff) return 'MODERATOR'
  if (userPermissions.value.length > 0) return 'JUNIOR_MODERATOR'
  return 'GUEST'
})

// Métodos
const activateCard = (cardNumber) => {
  activeCard.value = cardNumber
  
  // Verificar permisos antes de permitir acceso
  const requiredPermissions = {
    1: 'create_warn',
    2: 'register_ban',
    3: 'access_moderation_dashboard',
    4: 'manage_warns',
    5: 'view_characters_basic',
    6: 'full_discord_moderation',
    7: 'full_moderation_control',
    8: 'admin_only' // Clasificado
  }
  
  const required = requiredPermissions[cardNumber]
  if (required && !hasPermission(required) && cardNumber !== 8) {
    showAccessDenied(cardNumber)
  }
}

const showAccessDenied = (cardNumber) => {
  activeCard.value = cardNumber
  showDeniedModal.value = true
}

const closeModal = () => {
  showDeniedModal.value = false
  activeCard.value = 1
}

const hasPermission = (permission) => {
  if (!currentUser.value) return false
  if (currentUser.value.is_superuser) return true
  
  return userPermissions.value.includes(permission)
}

const getClearanceLevel = () => {
  if (!currentUser.value) return 'GUEST'
  if (currentUser.value.is_superuser) return 'LEVEL 5'
  if (userScopes.value.some(s => s.scope === 'global')) return 'LEVEL 4'
  if (userPermissions.value.includes('full_moderation_control')) return 'LEVEL 3'
  if (userPermissions.value.includes('register_ban')) return 'LEVEL 2'
  if (userPermissions.value.length > 0) return 'LEVEL 1'
  return 'LEVEL 0'
}

const goToPermissionManagement = () => {
  if (hasPermission('full_moderation_control')) {
    router.push('/moderation/admin/permissions')
  } else {
    showAccessDenied(9)
  }
}

const getUserPermissions = () => {
  return userPermissions.value
}

const getUserScopes = () => {
  return userScopes.value
}

const getPermissionType = (permission) => {
  if (permission.includes('full_')) return 'permission-full'
  if (permission.includes('manage_')) return 'permission-manage'
  if (permission.includes('create_') || permission.includes('register_')) return 'permission-create'
  if (permission.includes('view_') || permission.includes('access_')) return 'permission-view'
  return 'permission-basic'
}

// Navegación
const goToWarnManagement = () => {
  if (hasPermission('create_warn')) {
    router.push('/moderation/warns')
  } else {
    showAccessDenied(1)
  }
}

const goToBanManagement = () => {
  if (hasPermission('register_ban')) {
    router.push('/moderation/bans')
  } else {
    showAccessDenied(2)
  }
}

const goToGlobalModeration = () => {
  if (hasPermission('access_moderation_dashboard')) {
    router.push('/moderation/global')
  } else {
    showAccessDenied(3)
  }
}

const goToAppealManagement = () => {
  if (hasPermission('manage_warns')) {
    router.push('/moderation/appeals')
  } else {
    showAccessDenied(4)
  }
}

const goToInGameModeration = () => {
  if (hasPermission('view_characters_basic')) {
    router.push('/moderation/ingame')
  } else {
    showAccessDenied(5)
  }
}

const goToDiscordModeration = () => {
  if (hasPermission('full_discord_moderation')) {
    router.push('/moderation/discord')
  } else {
    showAccessDenied(6)
  }
}

const goToAuditLogs = () => {
  if (hasPermission('full_moderation_control')) {
    router.push('/moderation/audit')
  } else {
    showAccessDenied(7)
  }
}

// Tiempo y sesión
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
  
  // Actualizar duración de sesión
  if (sessionStartTime.value) {
    const start = new Date(sessionStartTime.value)
    const diff = now - start
    const hours = Math.floor(diff / 3600000)
    const minutes = Math.floor((diff % 3600000) / 60000)
    const seconds = Math.floor((diff % 60000) / 1000)
    sessionDuration.value = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`
  }
}

// Fetch datos
const fetchCurrentUser = async () => {
  try {
    const response = await fetch('/api/auth/user/')
    if (response.ok) {
      const data = await response.json()
      currentUser.value = data
      
      // Si el usuario está autenticado, inicializar sesión
      if (data.is_authenticated) {
        sessionStartTime.value = new Date().toISOString()
        fetchModerationStats()
        fetchUserPermissions()
      }
    }
  } catch (error) {
    console.error('Error fetching user:', error)
  }
}

const fetchModerationStats = async () => {
  try {
    const response = await fetch('/api/moderation/dashboard/')
    if (response.ok) {
      const data = await response.json()
      stats.activeWarns = data.stats?.active_warns || 0
      stats.activeBans = data.stats?.active_bans || 0
      stats.pendingAppeals = data.stats?.pending_appeals || 0
      stats.topWarnedUsers = data.top_warned_users?.length || 0
    }
  } catch (error) {
    console.error('Error fetching moderation stats:', error)
  }
}

const fetchUserPermissions = async () => {
  try {

    const response = await fetch('/api/auth/permissions/')
    if (response.ok) {
      const data = await response.json()
      userPermissions.value = data.permissions || []
      userScopes.value = data.scopes || []
    }
  } catch (error) {
    console.error('Error fetching permissions:', error)
  }
}

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
/* Estilos base */
.moderacion-page {
  position: relative;
  min-height: 100vh;
  color: #d8d8d8;
  background: #0a0a0a;
  font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
  line-height: 1.5;
  overflow-x: hidden;
  padding: 20px;
  box-sizing: border-box;
}

/* Fondo SCP (mismo que otros componentes) */
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

/* Header */
.moderacion-header {
  position: relative;
  z-index: 2;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  background: rgba(15, 15, 15, 0.95);
  border: 1px solid #333;
  border-radius: 0px;
  margin-bottom: 30px;
  backdrop-filter: blur(10px);
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.3);
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.header-logo {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.header-icon {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 51, 51, 0.1);
  border: 1px solid rgba(255, 51, 51, 0.3);
  border-radius: 2px;
}

.header-icon svg {
  width: 24px;
  height: 24px;
  color: #ff3333;
}

.header-title {
  display: flex;
  flex-direction: column;
}

.header-main {
  font-size: 1.1rem;
  font-weight: 700;
  letter-spacing: 1px;
  color: #ff3333;
  text-transform: uppercase;
  line-height: 1.2;
}

.header-sub {
  font-size: 0.7rem;
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

/* Sección Principal */
.moderacion-main {
  position: relative;
  z-index: 2;
}

.moderacion-header-section {
  text-align: center;
  margin-bottom: 40px;
}

.moderacion-title {
  font-size: 2rem;
  font-weight: 900;
  color: #ff3333;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 0 0 8px 0;
  text-shadow: 0 0 10px rgba(255, 51, 51, 0.3);
}

.moderacion-subtitle {
  font-size: 0.9rem;
  color: #aaa;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-bottom: 30px;
}

/* Estadísticas Rápidas */
.quick-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 15px;
  margin-top: 30px;
}

.stat-item {
  background: rgba(30, 30, 30, 0.8);
  border: 1px solid #333;
  padding: 15px;
  display: flex;
  align-items: center;
  gap: 12px;
  transition: all 0.3s ease;
}

.stat-item:hover {
  border-color: #444;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.stat-icon {
  width: 40px;
  height: 40px;
  background: rgba(255, 51, 51, 0.1);
  border: 1px solid rgba(255, 51, 51, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.stat-icon svg {
  width: 20px;
  height: 20px;
  color: #ff3333;
}

.stat-info {
  flex: 1;
}

.stat-label {
  display: block;
  font-size: 0.7rem;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  font-family: 'Consolas', monospace;
  margin-bottom: 4px;
}

.stat-value {
  display: block;
  font-size: 1.5rem;
  font-weight: 700;
  color: #fff;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.5px;
}

/* Grid de Moderación */
.moderation-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-bottom: 40px;
}

.moderation-card {
  background: rgba(20, 20, 20, 0.95);
  border: 1px solid #333;
  border-radius: 0px;
  overflow: hidden;
  transition: all 0.3s ease;
  cursor: pointer;
  backdrop-filter: blur(5px);
}

.moderation-card:hover {
  transform: translateY(-2px);
  border-color: #444;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.moderation-card.active {
  border-color: #ff3333;
  background: rgba(40, 20, 20, 0.95);
  box-shadow: 0 0 20px rgba(255, 51, 51, 0.2);
}

.moderation-card.redacted {
  cursor: not-allowed;
  opacity: 0.8;
}

.moderation-card.redacted:hover {
  transform: none;
  border-color: #aa2222;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 20px;
  background: rgba(30, 30, 30, 0.8);
  border-bottom: 1px solid #333;
}

.card-header.redacted {
  background: rgba(40, 20, 20, 0.8);
  border-bottom-color: #aa2222;
}

.card-icon {
  width: 24px;
  height: 24px;
  color: #ff3333;
  flex-shrink: 0;
}

.card-icon.redacted {
  color: #aa2222;
}

.card-title {
  font-size: 1rem;
  font-weight: 700;
  color: #fff;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  flex: 1;
}

.card-title.redacted-text {
  color: #aa2222;
  font-family: 'Consolas', monospace;
}

.card-status {
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.3px;
}

.status-active {
  color: #4CAF50;
  text-transform: uppercase;
}

.status-redacted {
  color: #aa2222;
  text-transform: uppercase;
}

.card-content {
  padding: 20px;
}

.card-description {
  font-size: 0.9rem;
  color: #aaa;
  line-height: 1.6;
  margin: 0 0 16px 0;
}

.card-description.redacted-text {
  color: #884444;
  font-style: italic;
}

.card-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.meta-label {
  font-size: 0.7rem;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.meta-value {
  font-size: 0.8rem;
  font-weight: 600;
  font-family: 'Consolas', monospace;
}

.meta-value.authorized {
  color: #4CAF50;
}

.meta-value.denied {
  color: #ff3333;
}

.meta-value.redacted {
  color: #aa2222;
}

.card-footer {
  padding: 0 20px 20px 20px;
}

.card-action {
  display: flex;
  justify-content: flex-end;
}

.action-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 20px;
  background: rgba(255, 51, 51, 0.1);
  border: 1px solid rgba(255, 51, 51, 0.3);
  border-radius: 0px;
  color: #ff3333;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.action-button:hover:not(.disabled) {
  background: rgba(255, 51, 51, 0.2);
  border-color: rgba(255, 51, 51, 0.5);
  transform: translateY(-1px);
}

.action-button.disabled {
  opacity: 0.5;
  cursor: not-allowed;
  background: rgba(40, 40, 40, 0.6);
  border-color: #444;
  color: #888;
}

.button-icon {
  width: 14px;
  height: 14px;
  color: currentColor;
}

.clearance-warning {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px;
  background: rgba(170, 34, 34, 0.1);
  border: 1px solid rgba(170, 34, 34, 0.3);
  border-radius: 0px;
}

.warning-icon {
  width: 16px;
  height: 16px;
  color: #aa2222;
}

.warning-text {
  font-size: 0.7rem;
  color: #aa2222;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

/* Panel de Información del Usuario */
.user-info-panel {
  background: rgba(15, 15, 15, 0.95);
  border: 1px solid #333;
  border-radius: 0px;
  padding: 25px;
  backdrop-filter: blur(5px);
  margin-bottom: 30px;
}

.info-header {
  text-align: center;
  margin-bottom: 25px;
}

.info-title {
  font-size: 1.2rem;
  font-weight: 700;
  color: #ff3333;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 8px 0;
}

.info-subtitle {
  font-size: 0.8rem;
  color: #888;
  letter-spacing: 0.3px;
  text-transform: uppercase;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 25px;
}

.info-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.info-item:last-child {
  border-bottom: none;
}

.info-label {
  font-size: 0.75rem;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.info-value {
  font-size: 0.85rem;
  font-weight: 600;
  color: #ddd;
  font-family: 'Consolas', monospace;
}

.info-value.permissions {
  color: #4CAF50;
}

.info-value.scopes {
  color: #2196F3;
}

/* Panel de Permisos */
.permissions-panel {
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  padding: 20px;
  margin-top: 20px;
}

.permissions-title {
  font-size: 0.9rem;
  color: #ff3333;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 15px 0;
  padding-bottom: 10px;
  border-bottom: 1px solid rgba(255, 51, 51, 0.3);
}

.permissions-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.permission-tag {
  font-size: 0.7rem;
  padding: 4px 8px;
  border-radius: 2px;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.3px;
  text-transform: uppercase;
  font-weight: 600;
}

.permission-tag.permission-full {
  background: rgba(255, 51, 51, 0.1);
  border: 1px solid rgba(255, 51, 51, 0.3);
  color: #ff3333;
}

.permission-tag.permission-manage {
  background: rgba(33, 150, 243, 0.1);
  border: 1px solid rgba(33, 150, 243, 0.3);
  color: #2196F3;
}

.permission-tag.permission-create {
  background: rgba(76, 175, 80, 0.1);
  border: 1px solid rgba(76, 175, 80, 0.3);
  color: #4CAF50;
}

.permission-tag.permission-view {
  background: rgba(255, 152, 0, 0.1);
  border: 1px solid rgba(255, 152, 0, 0.3);
  color: #FF9800;
}

.permission-tag.permission-basic {
  background: rgba(158, 158, 158, 0.1);
  border: 1px solid rgba(158, 158, 158, 0.3);
  color: #9E9E9E;
}

/* Modal de Acceso Denegado */
.access-denied-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.modal-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(10px);
}

.modal-content {
  position: relative;
  background: rgba(15, 15, 15, 0.98);
  border: 1px solid #aa2222;
  border-radius: 0px;
  max-width: 500px;
  width: 100%;
  box-shadow: 0 10px 40px rgba(170, 34, 34, 0.3);
  animation: modalAppear 0.3s ease forwards;
}

@keyframes modalAppear {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-header {
  padding: 30px 30px 20px 30px;
  text-align: center;
  border-bottom: 1px solid #333;
}

.modal-icon {
  width: 50px;
  height: 50px;
  color: #aa2222;
  margin: 0 auto 15px;
}

.modal-title {
  font-size: 1.5rem;
  font-weight: 900;
  color: #aa2222;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 0;
}

.modal-body {
  padding: 30px;
}

.modal-text {
  font-size: 1rem;
  color: #d8d8d8;
  text-align: center;
  line-height: 1.6;
  margin: 0 0 30px 0;
}

.clearance-info {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 20px;
  background: rgba(40, 20, 20, 0.6);
  border: 1px solid rgba(170, 34, 34, 0.3);
  border-radius: 0px;
}

.clearance-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.clearance-item:last-child {
  border-bottom: none;
}

.clearance-label {
  font-size: 0.8rem;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.clearance-value {
  font-size: 0.9rem;
  font-weight: 700;
  font-family: 'Consolas', monospace;
  letter-spacing: 0.5px;
}

.clearance-value.denied {
  color: #ff4444;
}

.modal-footer {
  padding: 20px 30px 30px 30px;
  text-align: center;
  border-top: 1px solid #333;
}

.modal-button {
  padding: 12px 30px;
  background: rgba(170, 34, 34, 0.1);
  border: 1px solid rgba(170, 34, 34, 0.3);
  border-radius: 0px;
  color: #aa2222;
  font-size: 0.9rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  cursor: pointer;
  transition: all 0.2s ease;
  min-width: 200px;
}

.modal-button:hover {
  background: rgba(170, 34, 34, 0.2);
  border-color: rgba(170, 34, 34, 0.5);
  transform: translateY(-1px);
}

.button-text {
  font-family: 'Consolas', monospace;
}

/* Responsive */
@media (max-width: 768px) {
  .moderation-grid {
    grid-template-columns: 1fr;
  }
  
  .moderacion-header {
    flex-direction: column;
    gap: 15px;
    text-align: center;
  }
  
  .header-left {
    flex-direction: column;
    text-align: center;
  }
  
  .header-right {
    align-items: center;
  }
  
  .quick-stats {
    grid-template-columns: 1fr;
  }
  
  .info-grid {
    grid-template-columns: 1fr;
  }
  
  .permissions-grid {
    justify-content: center;
  }
}

@media (min-width: 769px) and (max-width: 1024px) {
  .moderation-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1025px) {
  .moderation-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}
</style>