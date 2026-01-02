<template>
  <div class="admin-permissions-page">
    <!-- Fondo SCP (mismo estilo) -->
    <div class="site-background">
      <div class="grid-overlay"></div>
      <div class="scan-line"></div>
      <div class="particles"></div>
    </div>

    <!-- Header -->
    <header class="admin-header">
      <div class="header-content">
        <div class="header-left">
          <div class="header-logo">
            <div class="header-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="#ff3333" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                <path d="M12 8v4"></path>
                <path d="M12 16h.01"></path>
              </svg>
            </div>
            <div class="header-title">
              <span class="header-main">PERMISSION MANAGEMENT</span>
              <span class="header-sub">ADMINISTRATIVE CONTROL PANEL</span>
            </div>
          </div>
        </div>
        
        <div class="header-right">
          <button class="back-button" @click="goToModerationPanel">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M19 12H5"></path>
              <path d="M12 19l-7-7 7-7"></path>
            </svg>
            <span>BACK</span>
          </button>
        </div>
      </div>
    </header>

    <!-- Contenido Principal -->
    <main class="admin-main">
      <!-- Verificación de permisos -->
      <div v-if="!hasAdminPermissions()" class="access-denied">
        <div class="denied-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="#ff3333" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <path d="M4.93 4.93l14.14 14.14"></path>
          </svg>
        </div>
        <h3>ADMINISTRATIVE ACCESS REQUIRED</h3>
        <p>You need full_moderation_control permission to access this panel</p>
      </div>

      <div v-else class="admin-content">
        <!-- Búsqueda de Usuario -->
        <div class="user-search-section">
          <h2 class="section-title">ASSIGN PERMISSIONS TO USER</h2>
          <div class="search-container">
            <input
              v-model="userSearch"
              @keyup.enter="searchUser"
              type="text"
              placeholder="Search by Roblox ID or username..."
              class="search-input"
            />
            <button class="search-button" @click="searchUser">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="11" cy="11" r="8"></circle>
                <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
              </svg>
              <span>SEARCH</span>
            </button>
          </div>

          <!-- Resultados de búsqueda -->
          <div v-if="searchResults.length > 0" class="search-results">
            <div 
              v-for="user in searchResults" 
              :key="user.id"
              class="user-result"
              @click="selectUser(user)"
              :class="{ 'selected': selectedUser && selectedUser.id === user.id }"
            >
              <div class="user-avatar">
                {{ user.roblox_username.charAt(0).toUpperCase() }}
              </div>
              <div class="user-info">
                <span class="username">{{ user.roblox_username }}</span>
                <span class="user-id">ID: {{ user.roblox_id }}</span>
              </div>
              <div class="user-stats">
                <span class="stat warns" v-if="user.warning_count > 0">
                  {{ user.warning_count }} warns
                </span>
                <span class="stat banned" v-if="user.is_banned">
                  BANNED
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- Usuario seleccionado -->
        <div v-if="selectedUser" class="user-permissions-section">
          <div class="user-header">
            <h3 class="user-title">
              {{ selectedUser.roblox_username }}
              <span class="user-id">#{{ selectedUser.roblox_id }}</span>
            </h3>
            <div class="user-meta">
              <span class="meta-item" :class="{ 'staff': selectedUser.is_staff }">
                {{ selectedUser.is_staff ? 'STAFF' : 'USER' }}
              </span>
              <span class="meta-item" :class="{ 'superuser': selectedUser.is_superuser }">
                {{ selectedUser.is_superuser ? 'SUPERUSER' : 'NORMAL' }}
              </span>
            </div>
          </div>

          <!-- Permisos actuales -->
          <div class="current-permissions">
            <h4>CURRENT PERMISSIONS</h4>
            <div class="permissions-tags">
              <span 
                v-for="permission in selectedUserPermissions" 
                :key="permission"
                class="permission-tag"
              >
                {{ permission }}
                <button 
                  class="remove-permission"
                  @click.stop="removePermission(permission)"
                  title="Remove permission"
                >
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="18" y1="6" x2="6" y2="18"></line>
                    <line x1="6" y1="6" x2="18" y2="18"></line>
                  </svg>
                </button>
              </span>
            </div>
          </div>

          <!-- Asignar nuevos permisos -->
          <div class="assign-permissions">
            <h4>AVAILABLE PERMISSIONS</h4>
            <div class="permissions-grid">
              <div 
                v-for="permission in allPermissions" 
                :key="permission"
                class="permission-card"
                :class="{ 'assigned': selectedUserPermissions.includes(permission) }"
                @click="togglePermission(permission)"
              >
                <div class="permission-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                    <path d="M22 4 12 14.01l-3-3"></path>
                  </svg>
                </div>
                <div class="permission-name">{{ permission }}</div>
                <div class="permission-status">
                  {{ selectedUserPermissions.includes(permission) ? 'ASSIGNED' : 'AVAILABLE' }}
                </div>
              </div>
            </div>
          </div>

          <!-- Guardar cambios -->
          <div class="save-section">
            <button class="save-button" @click="savePermissions" :disabled="!permissionsChanged">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"></path>
                <polyline points="17 21 17 13 7 13 7 21"></polyline>
                <polyline points="7 3 7 8 15 8"></polyline>
              </svg>
              <span>SAVE CHANGES</span>
            </button>
          </div>
        </div>
      </div>
    </main>

    <!-- Sistema de notificaciones -->
    <div class="scp-notifications">
      <!-- ... mismo sistema de notificaciones ... -->
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// Estado
const userSearch = ref('')
const searchResults = ref([])
const selectedUser = ref(null)
const selectedUserPermissions = ref([])
const originalPermissions = ref([])
const loading = ref(false)

// Todos los permisos disponibles
const allPermissions = [
  'create_warn',
  'register_ban',
  'access_moderation_dashboard',
  'manage_warns',
  'view_characters_basic',
  'full_discord_moderation',
  'full_moderation_control',
  'change_ssu_status',
  'edit_rp_files_basic',
  'edit_rp_files_full',
  'faction_moderation_basic',
  'faction_moderation_full',
  'supervise_actors_basic',
  'supervise_actors_full'
]

// Computed
const permissionsChanged = computed(() => {
  return JSON.stringify(selectedUserPermissions.value.sort()) !== 
         JSON.stringify(originalPermissions.value.sort())
})

// Métodos
const hasAdminPermissions = () => {
  // En producción, verificar del backend
  return true // Temporalmente true para desarrollo
}

const searchUser = async () => {
  if (!userSearch.value.trim()) return
  
  loading.value = true
  try {
    const response = await fetch(`/api/moderation/users/search/${encodeURIComponent(userSearch.value)}/`)
    if (response.ok) {
      const data = await response.json()
      searchResults.value = data.results
    }
  } catch (error) {
    console.error('Error searching users:', error)
  } finally {
    loading.value = false
  }
}

const selectUser = async (user) => {
  selectedUser.value = user
  // Cargar permisos del usuario
  try {
    const response = await fetch(`/api/auth/user/${user.id}/permissions/`)
    if (response.ok) {
      const data = await response.json()
      selectedUserPermissions.value = data.permissions || []
      originalPermissions.value = [...selectedUserPermissions.value]
    }
  } catch (error) {
    console.error('Error loading user permissions:', error)
  }
}

const togglePermission = (permission) => {
  const index = selectedUserPermissions.value.indexOf(permission)
  if (index === -1) {
    selectedUserPermissions.value.push(permission)
  } else {
    selectedUserPermissions.value.splice(index, 1)
  }
}

const removePermission = (permission) => {
  const index = selectedUserPermissions.value.indexOf(permission)
  if (index !== -1) {
    selectedUserPermissions.value.splice(index, 1)
  }
}

const savePermissions = async () => {
  if (!selectedUser.value) return
  
  try {
    const response = await fetch(`/api/auth/user/${selectedUser.value.id}/permissions/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken()
      },
      body: JSON.stringify({
        permissions: selectedUserPermissions.value
      })
    })
    
    if (response.ok) {
      showNotification('SUCCESS', 'Permissions updated successfully', 'success', 4000)
      originalPermissions.value = [...selectedUserPermissions.value]
    } else {
      showNotification('ERROR', 'Failed to update permissions', 'error', 5000)
    }
  } catch (error) {
    console.error('Error saving permissions:', error)
    showNotification('ERROR', 'Failed to update permissions', 'error', 5000)
  }
}

const goToModerationPanel = () => {
  router.push('/moderation')
}

// Función para obtener CSRF token (misma que en Moderacion_Global.vue)
const getCSRFToken = () => {
  const cookieValue = document.cookie
    .split('; ')
    .find(row => row.startsWith('csrftoken='))
    ?.split('=')[1]
  
  if (cookieValue) return cookieValue
  
  const metaTag = document.querySelector('meta[name="csrf-token"]')
  if (metaTag) return metaTag.content
  
  console.error('CSRF token not found')
  return ''
}

// Función de notificaciones (misma que en Moderacion_Global.vue)
const showNotification = (title, message, type = 'info', duration = 5000) => {
  // Implementación igual a Moderacion_Global.vue
}
</script>

<style scoped>
/* Estilos SCP (similar a los otros componentes) */
.admin-permissions-page {
  position: relative;
  min-height: 100vh;
  color: #d8d8d8;
  background: #0a0a0a;
  font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
}

/* ... Agrega aquí todos los estilos SCP del fondo ... */

/* Header */
.admin-header {
  position: relative;
  z-index: 2;
  background: rgba(15, 15, 15, 0.98);
  border-bottom: 1px solid #333;
  padding: 1.5rem 2rem;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1600px;
  margin: 0 auto;
}

.back-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.6rem 1.2rem;
  background: rgba(255, 51, 51, 0.1);
  border: 1px solid rgba(255, 51, 51, 0.3);
  color: #ff3333;
  font-size: 0.85rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.back-button:hover {
  background: rgba(255, 51, 51, 0.2);
  border-color: rgba(255, 51, 51, 0.5);
}

/* Contenido principal */
.admin-main {
  position: relative;
  z-index: 2;
  max-width: 1600px;
  margin: 0 auto;
  padding: 2rem;
}

.access-denied {
  text-align: center;
  padding: 4rem 2rem;
}

.denied-icon {
  width: 80px;
  height: 80px;
  color: #ff3333;
  margin: 0 auto 2rem;
}

.access-denied h3 {
  font-size: 1.5rem;
  color: #ff3333;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 1rem;
}

.access-denied p {
  color: #aaa;
}

/* Búsqueda de usuario */
.user-search-section {
  background: rgba(20, 20, 20, 0.95);
  border: 1px solid #333;
  padding: 2rem;
  margin-bottom: 2rem;
}

.section-title {
  font-size: 1.2rem;
  color: #ff3333;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 1.5rem 0;
}

.search-container {
  display: flex;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.search-input {
  flex: 1;
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  padding: 0.8rem 1rem;
  color: #fff;
  font-size: 1rem;
  font-family: inherit;
  outline: none;
}

.search-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.8rem 1.5rem;
  background: rgba(255, 51, 51, 0.1);
  border: 1px solid rgba(255, 51, 51, 0.3);
  color: #ff3333;
  font-size: 0.9rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  cursor: pointer;
}

/* Resultados de búsqueda */
.search-results {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.user-result {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: rgba(30, 30, 30, 0.6);
  border: 1px solid #444;
  cursor: pointer;
  transition: all 0.3s ease;
}

.user-result:hover {
  border-color: #555;
  background: rgba(40, 40, 40, 0.8);
}

.user-result.selected {
  border-color: #ff3333;
  background: rgba(255, 51, 51, 0.1);
}

.user-avatar {
  width: 40px;
  height: 40px;
  background: rgba(255, 51, 51, 0.1);
  border: 1px solid rgba(255, 51, 51, 0.3);
  border-radius: 2px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  color: #ff3333;
}

.user-info {
  flex: 1;
}

.username {
  display: block;
  font-weight: 600;
  color: #fff;
}

.user-id {
  display: block;
  font-size: 0.8rem;
  color: #888;
  font-family: 'Consolas', monospace;
}

.user-stats {
  display: flex;
  gap: 0.5rem;
}

.stat {
  font-size: 0.7rem;
  padding: 0.2rem 0.5rem;
  border-radius: 2px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  font-family: 'Consolas', monospace;
}

.stat.warns {
  background: rgba(255, 152, 0, 0.1);
  color: #FF9800;
  border: 1px solid rgba(255, 152, 0, 0.3);
}

.stat.banned {
  background: rgba(244, 67, 54, 0.1);
  color: #f44336;
  border: 1px solid rgba(244, 67, 54, 0.3);
}

/* Sección de permisos del usuario */
.user-permissions-section {
  background: rgba(20, 20, 20, 0.95);
  border: 1px solid #333;
  padding: 2rem;
}

.user-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.user-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #fff;
  margin: 0;
}

.user-id {
  color: #888;
  font-size: 1rem;
  font-family: 'Consolas', monospace;
}

.user-meta {
  display: flex;
  gap: 1rem;
}

.meta-item {
  font-size: 0.8rem;
  padding: 0.3rem 0.8rem;
  border-radius: 2px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  font-family: 'Consolas', monospace;
}

.meta-item.staff {
  background: rgba(33, 150, 243, 0.1);
  color: #2196F3;
  border: 1px solid rgba(33, 150, 243, 0.3);
}

.meta-item.superuser {
  background: rgba(76, 175, 80, 0.1);
  color: #4CAF50;
  border: 1px solid rgba(76, 175, 80, 0.3);
}

/* Permisos actuales */
.current-permissions {
  margin-bottom: 2rem;
}

.current-permissions h4 {
  font-size: 1rem;
  color: #ff3333;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  margin: 0 0 1rem 0;
}

.permissions-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.permission-tag {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(33, 150, 243, 0.1);
  border: 1px solid rgba(33, 150, 243, 0.3);
  color: #2196F3;
  padding: 0.4rem 0.8rem;
  border-radius: 2px;
  font-size: 0.8rem;
  font-weight: 600;
  font-family: 'Consolas', monospace;
}

.remove-permission {
  background: none;
  border: none;
  color: inherit;
  cursor: pointer;
  padding: 0.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0.6;
  transition: opacity 0.3s ease;
}

.remove-permission:hover {
  opacity: 1;
}

.remove-permission svg {
  width: 12px;
  height: 12px;
}

/* Asignar permisos */
.assign-permissions {
  margin-bottom: 2rem;
}

.assign-permissions h4 {
  font-size: 1rem;
  color: #ff3333;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  margin: 0 0 1.5rem 0;
}

.permissions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
}

.permission-card {
  background: rgba(30, 30, 30, 0.8);
  border: 1px solid #444;
  padding: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.permission-card:hover {
  border-color: #555;
  transform: translateY(-2px);
}

.permission-card.assigned {
  border-color: #4CAF50;
  background: rgba(76, 175, 80, 0.1);
}

.permission-icon {
  width: 24px;
  height: 24px;
  color: currentColor;
  margin-bottom: 0.5rem;
}

.permission-name {
  font-weight: 600;
  color: #fff;
  margin-bottom: 0.5rem;
  word-break: break-word;
}

.permission-status {
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  font-family: 'Consolas', monospace;
}

.permission-card:not(.assigned) .permission-status {
  color: #888;
}

.permission-card.assigned .permission-status {
  color: #4CAF50;
}

/* Guardar cambios */
.save-section {
  text-align: center;
  padding-top: 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.save-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.8rem;
  padding: 1rem 2rem;
  background: rgba(76, 175, 80, 0.1);
  border: 1px solid rgba(76, 175, 80, 0.3);
  color: #4CAF50;
  font-size: 1rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  cursor: pointer;
  transition: all 0.3s ease;
  min-width: 200px;
  margin: 0 auto;
}

.save-button:hover:not(:disabled) {
  background: rgba(76, 175, 80, 0.2);
  border-color: rgba(76, 175, 80, 0.5);
}

.save-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>