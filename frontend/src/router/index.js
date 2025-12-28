import { createRouter, createWebHistory } from "vue-router"
import Landing from "@/views/Landing.vue"
import Privacy from "@/views/Privacy.vue"
import TermsOfService from "@/views/TermsOfService.vue"

const routes = [
  { path: "/", name: "Landing", component: Landing },
  { path: "/privacy", name: "Privacy", component: Privacy },
  { path: "/terms-of-service", name: "TermsOfService", component: TermsOfService },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
