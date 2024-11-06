<template>
  <v-app>
    <v-app-bar
      :elevation="0"
      rounded
      color="black"
    >
      <template v-slot:prepend>
        <v-app-bar-nav-icon @click="toggleNavigationDrawer"></v-app-bar-nav-icon>
      </template>

      <v-app-bar-title>Trip&Co</v-app-bar-title>
      <!-- <v-app-bar-icon src="@assets/logo_white.png"></v-app-bar-icon> -->

      <template v-slot:append>
        <v-btn icon="mdi-heart"></v-btn>
        <v-btn icon="mdi-dots-vertical" @click="toggleTheme"></v-btn>
      </template>
    </v-app-bar>

    <v-navigation-drawer
      v-model="showNavigationDrawer"
    >
      <v-list-item title="Your trips"></v-list-item>
      <v-divider></v-divider>
      <v-list-item link title="Trip 1"></v-list-item>
      <v-list-item link title="Trip 2"></v-list-item>
      <v-list-item link title="Trip 3"></v-list-item>
      <v-btn>New trip</v-btn>
    </v-navigation-drawer>

    <v-main>
      <router-view></router-view>
    </v-main>
    
  </v-app>
</template>

<script>
import { useTheme } from 'vuetify'

export default {
  setup() {
    const theme = useTheme()
    theme.global.name.value = 'dark'

    function toggleTheme() {
      theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
    }

    return {
      toggleTheme
    }
  },

  data() {
    return {
      showNavigationDrawer: false
    }
  },

  methods: {
    toggleNavigationDrawer() {
      this.showNavigationDrawer = !this.showNavigationDrawer
    }
  }
}
</script>
