<template>
  <div v-if="isTripRoute">
    <v-btn
        @click="fetchAndCopy"
        class="text-none"
        density="comfortable"
        variant="flat"
        color="white"
    >Invite users to Trip
    </v-btn>

    <div class="text-center ma-2">
      <v-snackbar location="top"
                  v-model="snackbar"
                  timeout="4000"
                  variant="tonal"
      >
        The link to the invitation was copied to the clipboard!

        <template v-slot:actions>
          <v-btn
              variant="text"
              @click="snackbar = false"
          >
            X
          </v-btn>
        </template>
      </v-snackbar>
    </div>
  </div>
</template>

<script>
import apiClient from "@/api/axios";

export default {
  data() {
    return {
      snackbar: false,
      showInput: false, // флаг для управления видимостью input
      inputValue: '',   // значение input
      text: "Copy to invite",
      copyText: '',
    };
  },
  methods: {
    async fetchAndCopy() {
      if (!this.isTripRoute || !this.tripID) {
        return;
      }

      try {
        const response = await apiClient.get(`/trips`, {
          params: {
            trip_id: this.tripID,
          }
        })

        if (Array.from(response.data).length < 1) {
          console.log('not data')
          return;
        }

        this.snackbar = true;

        const token = response.data[0]['invite_token']

        const path = `${window.location.origin}/join/${token}`

        await navigator.clipboard.writeText(path)

      } catch (e) {

        console.log("failed to get trips_info", e)
      }
    },
  },
  computed: {
    tripID() {
      return this.$route.params.id
    },
    isTripRoute() {
      return this.$route.path.startsWith('/trips/')
    }
  }
};
</script>

<style scoped>
.input-container {
  margin-top: 8px;
}
</style>