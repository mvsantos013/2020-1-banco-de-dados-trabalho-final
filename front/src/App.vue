<template>
  <transition name="fade-transition" mode="out-in">
    <v-app v-if="isAppLoading">
      <v-layout
        align-center
        justify-center
        row
        fill-height
        ma-0
        class="primary"
        style="height: -webkit-fill-available"
      >
        <v-progress-circular
          indeterminate
          :size="50"
          color="white"
          align-center
        ></v-progress-circular>
      </v-layout>
    </v-app>
    <v-app v-else>
      <Navbar
        logo="BD 2020.1"
        subLogo="Trabalho Final"
        :avatar="null"
        :username="'username'"
        :role="null"
        :navigationDrawer="navigationDrawer"
        footerText="BD 2020.1 Trabalho Final"
      />

      <v-main>
        <v-container>
          <router-view></router-view>
        </v-container>
      </v-main>
    </v-app>
  </transition>
</template>

<script>
import Navbar from '@/components/shared/layout/navbar'

export default {
  components: {
    Navbar
  },
  async mounted() {
    try {
      this.isAppLoading = true
      await new Promise(resolve => setTimeout(resolve, 2000)) // sleep 2 seconds
      this.logged = true
      this.isAppLoading = false
    } catch (e) {
      console.log(e)
    }
  },
  data() {
    return {
      isAppLoading: false,
      logged: false,
      navigationDrawer: [
        {
					category: null,
					permission: true,
					navLinks: [
						{ text: 'Página inicial', icon: 'mdi-view-dashboard', url: '/', permission: true },
						{ text: 'Relatório', icon: 'mdi-note-text-outline', url: '/relatorio', permission: true }
          ]
        },
        {
					category: 'Queries',
					permission: true,
					navLinks: [
						{ text: 'Resumo dos desfechos', icon: 'mdi-file-document-outline', url: '/desfechos-resumo', permission: true },
						{ text: 'Altas Administrativas', icon: 'mdi-medical-bag', url: '/altas-administrativas', permission: true },
						{ text: 'Óbitos', icon: 'mdi-skull-outline', url: '/obitos', permission: true },
						{ text: 'Casos por estado', icon: 'mdi-numeric-9-plus-box-multiple-outline', url: '/casos', permission: true }
          ]
        },
        {
					category: 'Banco de dados (raw)',
					permission: true,
					navLinks: [
            { text: 'Analitos', icon: 'mdi-atom', url: '/db/analitos', permission: true },
            { text: 'Atendimentos', icon: 'mdi-hospital-box', url: '/db/atendimentos', permission: true },
						{ text: 'Clinicas', icon: 'mdi-account-group', url: '/db/clinicas', permission: true },
						{ text: 'Desfechos', icon: 'mdi-forum', url: '/db/desfechos', permission: true },
						{ text: 'Enderecos', icon: 'mdi-map-marker', url: '/db/enderecos', permission: true },
						{ text: 'Estados', icon: 'mdi-sign-real-estate', url: '/db/estados', permission: true },
						{ text: 'Exames', icon: 'mdi-newspaper-variant', url: '/db/exames', permission: true },
						{ text: 'Locais De Exame', icon: 'mdi-map-marker-path', url: '/db/locais-de-exame', permission: true },
						{ text: 'Municipios', icon: 'mdi-home-city-outline', url: '/db/municipios', permission: true },
						{ text: 'Pacientes', icon: 'mdi-account-group', url: '/db/pacientes', permission: true },
						{ text: 'Paises', icon: 'mdi-earth', url: '/db/paises', permission: true },
						{ text: 'Sexos', icon: 'mdi-human-handsdown', url: '/db/sexos', permission: true },
						{ text: 'Tipos de Atendimento', icon: 'mdi-format-list-bulleted-square', url: '/db/tipos-de-atendimento', permission: true },
						{ text: 'Tipos de Desfecho', icon: 'mdi-format-list-bulleted-triangle', url: '/db/tipos-de-desfecho', permission: true },
						{ text: 'Tipos de Exame', icon: 'mdi-format-list-bulleted-type', url: '/db/tipos-de-exame', permission: true },
						{ text: 'Unidade', icon: 'mdi-home-variant-outline', url: '/db/unidade', permission: true },
					]
				},
      ],
    }
  }
}
</script>
