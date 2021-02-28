import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import VueGoogleCharts from 'vue-google-charts'
import '@/plugins/filters'
import './assets/css/main.scss'

Vue.config.productionTip = false

Vue.use(VueGoogleCharts)

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
