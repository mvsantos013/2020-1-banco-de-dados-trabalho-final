<template>
  <nav>
    <v-app-bar class="primary" dark app fixed>
      <!-- <v-app-bar-nav-icon
        v-if="navigationDrawer.length"
        @click.stop="drawer = !drawer"
      ></v-app-bar-nav-icon>-->

      <v-toolbar-title>
        <router-link to="/" tag="span" style="display: flex;">
          <v-img v-if="logoImg" :src="logoImg" :width="logoWidth"></v-img>
          <span>{{ logo }}</span>
          <span class="ml-2 quartiary--text">{{ subLogo }}</span>
        </router-link>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <div class="navbar-avatar mr-3">
        <span class="pr-3">{{ username }}</span>
        <v-avatar v-if="avatar" size="36">
          <v-img :src="avatar"></v-img>
        </v-avatar>
      </div>
    </v-app-bar>

    <v-navigation-drawer
      v-if="navigationDrawer.length"
      v-model="drawer"
      app
      temporary
      class="primary"
      dark
      style="border: 0px"
    >
      <v-list-item>
        <v-list-item-avatar v-if="avatar">
          <v-img :src="avatar"></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title>{{ username }}</v-list-item-title>
          <v-list-item-title
            v-if="role"
            class="role grey--text text--lighten-2 caption font-weight-light pt-1"
            >{{ role }}</v-list-item-title
          >
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <template v-for="area in navigationDrawer">
        <div v-if="area.permission" :key="area.category">
          <v-subheader
            v-if="area.category"
            class="font-weight-regular subheader"
            >{{ area.category }}</v-subheader
          >

          <v-list dense>
            <template v-for="navLink in area.navLinks">
              <v-list-item
                v-if="navLink.permission"
                :key="navLink.text"
                :to="navLink.url"
                link
              >
                <v-list-item-icon>
                  <v-icon>{{ navLink.icon }}</v-icon>
                </v-list-item-icon>

                <v-list-item-content>
                  <v-list-item-title>{{ navLink.text }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </template>
          </v-list>
        </div>
      </template>

      <template v-if="footerText" v-slot:append>
        <v-divider></v-divider>
        <v-card-text class="white--text text-center">
          {{ new Date().getFullYear() }} —
          <strong>{{ footerText }}</strong>
        </v-card-text>
      </template>
    </v-navigation-drawer>
  </nav>
</template>

<script>
export default {
  props: {
    logoImg: {
      default: '',
      type: String
    },
    logoWidth: {
      default: '',
      type: String
    },
    logo: {
      default: '',
      type: String
    },
    subLogo: {
      default: '',
      type: String
    },
    avatar: {
      default: '',
      type: String
    },
    username: {
      default: '',
      type: String
    },
    role: {
      default: '',
      type: String
    },
    navigationDrawer: {
      default: () => [],
      type: Array
    },
    footerText: {
      default: null,
      type: String
    }
  },
  data() {
    return {
      drawer: false
    }
  }
}
</script>

<style lang="scss" scoped>
.subheader {
  margin-top: 1.1em;
  height: auto;
}
.navbar-avatar {
  display: flex;
  align-items: center;
}
</style>
