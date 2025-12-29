import { createRouter, createWebHistory } from "vue-router"
import Landing from "@/views/Landing.vue"
import Privacy from "@/views/Privacy.vue"
import TermsOfService from "@/views/TermsOfService.vue"
import LoginSignup from "@/views/LoginSignup.vue"
import Information from "@/views/Information.vue"
import Error_404 from "@/views/Error_404.vue"

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
