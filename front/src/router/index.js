import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  { path: '/', name: 'Home', component: () => import('../pages/Home.vue') },
  { path: '/db/analitos', name: 'Analitos', component: () => import('../pages/database/Analitos.vue') },
  { path: '/db/atendimentos', name: 'Atendimentos', component: () => import('../pages/database/Atendimentos.vue') },
  { path: '/db/clinicas', name: 'Clinicas', component: () => import('../pages/database/Clinicas.vue') },
  { path: '/db/desfechos', name: 'Desfechos', component: () => import('../pages/database/Desfechos.vue') },
  { path: '/db/enderecos', name: 'Enderecos', component: () => import('../pages/database/Enderecos.vue') },
  { path: '/db/estados', name: 'Estados', component: () => import('../pages/database/Estados.vue') },
  { path: '/db/exames', name: 'Exames', component: () => import('../pages/database/Exames.vue') },
  { path: '/db/locais-de-exame', name: 'LocaisDeExame', component: () => import('../pages/database/LocaisDeExame.vue') },
  { path: '/db/municipios', name: 'Municipios', component: () => import('../pages/database/Municipios.vue') },
  { path: '/db/pacientes', name: 'Pacientes', component: () => import('../pages/database/Pacientes.vue') },
  { path: '/db/Paises', name: 'Paises', component: () => import('../pages/database/Paises.vue') },
  { path: '/db/sexos', name: 'Sexos', component: () => import('../pages/database/Sexos.vue') },
  { path: '/db/tipos-de-atendimento', name: 'TiposDeAtendimento', component: () => import('../pages/database/TiposDeAtendimento.vue') },
  { path: '/db/tipos-de-desfecho', name: 'TiposDeDesfecho', component: () => import('../pages/database/TiposDeDesfecho.vue') },
  { path: '/db/tipos-de-exame', name: 'TiposDeExame', component: () => import('../pages/database/TiposDeExame.vue') }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
