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
        <!-- <div>{{ username }}</div> -->
        <InviteButton></InviteButton>

        <v-btn icon="mdi-dots-vertical" @click="toggleTheme"></v-btn>
      </template>

    </v-app-bar>


    <v-navigation-drawer
        v-model="showNavigationDrawer"
    >
<!--      // <v-sheet v-for="comment in comments" :key="comment.id">-->
      <v-list-item title="Your trips"></v-list-item>
      <v-divider></v-divider>

      <span v-for="trip in userTrips" :key="trip.id">
         <v-list-item link :title="trip.name" @click="this.$router.push(`/trips/${trip.id}`)"></v-list-item>
      </span>

<!--      <v-list-item link title="Trip 1"></v-list-item>-->
<!--      <v-list-item link title="Trip 2"></v-list-item>-->
<!--      <v-list-item link title="Trip 3"></v-list-item>-->
      <v-btn
          @click="toggleCreateTripDialog"
          class="ma-5"
          color="white"
          variant="flat"
      >
        New trip
      </v-btn>
    </v-navigation-drawer>

    <v-main>
      <v-dialog v-model="showCreateTripDialog">
        <CreateTrip @close="toggleCreateTripDialog"></CreateTrip>
      </v-dialog>
      <router-view></router-view>
    </v-main>

  </v-app>
</template>

<script>
import {useTheme} from 'vuetify'
import CreateTrip from "@/components/create-trip.vue";
import InviteButton from "@/components/invite-button.vue";
import apiClient from "@/api/axios";

export default {
  components: {
    CreateTrip,
    InviteButton,
  },
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
      showNavigationDrawer: false,
      showCreateTripDialog: false,
      userTrips: [],
    }
  },
  created() {
    this.loadUserTrips();
  },

  methods: {
    toggleNavigationDrawer() {
      this.showNavigationDrawer = !this.showNavigationDrawer
    },
    toggleCreateTripDialog() {
      this.showCreateTripDialog = !this.showCreateTripDialog
    },
    async loadUserTrips() {

      try {
        const response = await apiClient.get('/trips', {
          params: {
            participant: true,
          }
        })

        this.userTrips = response.data

      } catch (e) {
        console.log("failed to get user trips", e)
      }
    }
  }
}
</script>
