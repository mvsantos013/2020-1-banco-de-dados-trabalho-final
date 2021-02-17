import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../pages/Home.vue'
import Pacientes from '../pages/Pacientes.vue'
import Sexos from '../pages/Sexos.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/pacientes',
    name: 'Pacientes',
    component: Pacientes
  },
  {
    path: '/sexos',
    name: 'Sexos',
    component: Sexos
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
