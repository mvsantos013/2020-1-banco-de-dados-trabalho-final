import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import '@mdi/font/css/materialdesignicons.css'

Vue.use(Vuetify)

const opts = {
  icons: {
    iconfont: 'mdi'
  },
  theme: {
    themes: {
      light: {
        primary: '#6A96C7',
        secondary: '#76a6db',
        tertiary: '#82b5ed',
        quartiary: '#b4d5fa',
        'primary-darker': '#608cbd',
        'primary-darker-2': '#527ba8',
        accent: '#82B1FF',
        error: '#FF5252',
        info: '#2196F3',
        success: '#4CAF50',
        warning: '#FFC107'
      }
    }
  }
}

export default new Vuetify(opts)
