import { createRouter, createWebHistory } from "vue-router"

const routes = [
  {
    path: "/privacy",
    component: () => import("../views/Privacy.vue"),
  },
  {
    path: "/terms-of-service",
    component: () => import("../views/TermsOfService.vue"),
  },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
