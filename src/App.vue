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
        :username="'username@test.com'"
        :role="null"
        :navigationDrawer="navigationDrawer"
        footerText="BD 2020.1 Trabalho Final"
      />

      <v-main>
        <router-view></router-view>
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
            {
              text: 'Home',
              icon: 'mdi-view-dashboard',
              url: '/',
              permission: true
            }
          ]
        }
      ]
    }
  }
}
</script>
