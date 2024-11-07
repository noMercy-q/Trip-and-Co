<template>
  <v-container class="d-flex flex-column justify-center align-center" fluid
               style="min-height: 100vh;">
    <v-img
        src="/assets/logo_white.png"
        width="auto"
        max-width="150px"
        max-height="100px"
        height="100px"
        alt="Logo"
    ></v-img>

    <h1 class="text-center white--text">
      You've been invited!
    </h1>

    <v-card v-if="trip" variant="flat" width="350px" class="pa-6 mt-5 rounded-shaped">
      <v-card-text class="mt-2">
        <p>Trip title: <strong>{{ trip.name }}</strong></p>
        <p> {{ trip.description }}</p>

        <v-btn :loading="isSubmitting" class="mt-4 mb-4" block color="blue" dark @click="acceptInvite">
          Accept Invitation
        </v-btn>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import apiClient from "@/api/axios";

export default {
  data() {
    return {
      trip: null,
      inviteToken: '',
      isSubmitting: false,
    };
  },
  created() {
    // Получение inviteToken из параметра маршрута
    this.inviteToken = this.$route.params.invite_token;

    this.loadTrip();
  },
  methods: {
    async acceptInvite() {
      this.isSubmitting = true;

      try {
        const response = await apiClient.post('join_trip',{}, {
          params: {
            invite_token: this.inviteToken
          }
        });

        // После успешного запроса можно сделать редирект на главную страницу
        this.$router.push(`/trips/${this.trip.id}`);
        console.log(response.data);
      } catch (e) {
        console.log("Error accepting invite: ", e);
      } finally {
        this.isSubmitting = false;
      }
    },
    async loadTrip() {
      try {
        const response = await apiClient.get('/trips', {
          params: {
            invite_token: this.inviteToken
          }
        })

        if (Array.from(response.data).length < 1) {
          return;
        }

        this.trip = response.data[0]

      } catch (e) {
        console.log('failed to fetch trip', e)
      }
    },
  },
};
</script>

<style scoped>
</style>
