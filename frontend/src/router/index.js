import { createRouter, createWebHistory } from "vue-router"
import Landing from "@/views/Landing.vue"
import Privacy from "@/views/Privacy.vue"
import TermsOfService from "@/views/TermsOfService.vue"
import LoginSignup from "@/views/LoginSignup.vue"
import Information from "@/views/Information.vue"
import Error_404 from "@/views/Error_404.vue"
import Dashboard from "@/views/Dashboard.vue"
import Personajes from "@/views/Personajes.vue"
import Perfil from "@/views/Perfil.vue"

/* import CharacterCreate from "@/views/CharacterCreate.vue"
import CharacterList from "@/views/CharacterList.vue"
import CharacterDetail from "@/views/CharacterDetail.vue" */

const routes = [
  { path: "/", name: "Landing", component: Landing },
  { path: "/privacy", name: "Privacy", component: Privacy },
  { path: "/terms-of-service", name: "TermsOfService", component: TermsOfService },
  {
    path: '/login',
    name: 'LoginSignup',
    component: LoginSignup,
  },
  {
    path: "/information",
    name: "Information",
    component: Information,
  },
  {
    path: "/404",
    name: "Error404",
    component: Error_404,
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: Dashboard,
    meta: { requiresAuth: true }
  },
  {
    path: '/dashboard/personnel',
    name: 'personajes',
    component: Personajes,
    meta: {
      requiresAuth: true,
    }
  },
  {
    path: '/users/:id',  // :id capturará el roblox_id
    name: 'perfil',
    component: Perfil,
    meta: {
      requiresAuth: true,  // Solo usuarios autenticados pueden ver perfiles
    },
    props: true,  // Pasa los parámetros de ruta como props al componente
  },
/*   {
    path: "/characters",
    name: "CharacterList",
    component: CharacterList,
  },
  {
    path: "/characters/new",
    name: "CharacterCreate",
    component: CharacterCreate,
  },
  {
    path: "/characters/:id",
    name: "CharacterDetail",
    component: CharacterDetail,
    props: true,
  }, */
  // IMPORTANTE: El catch-all debe ser la ÚLTIMA ruta
  {
    path: '/:pathMatch(.*)*',
    name: "NotFound",
    component: Error_404,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
