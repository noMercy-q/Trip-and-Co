<template>
<v-card width="300" min-height="300" class="rounded-xl" variant="outlined">
  <v-img
    cover
    :src="hotel.imageUrl"
    class="align-end"
    height="150"
  >
    <v-card-title>{{ hotel.title }}</v-card-title>
  </v-img>
  <v-card-subtitle class="pt-4">
    {{ hotel.title }}
  </v-card-subtitle>

  <v-card-text>
    <div>{{ hotel.title }}</div>
    <div>{{ hotel.description }}</div>
    <div>{{ hotel.address }}</div>
  </v-card-text>

  <v-card-actions class="d-flex justify-end ma-2">
    <v-btn color="white" text="Upvote" @click="upvote(hotel.id)"/>
  </v-card-actions>
</v-card>
</template>

<script>
import apiClient from '../api/axios';

export default {
  name: "HotelCard",
  
  props: {
    hotel: Object
  },

  methods: {
    async upvote(hotelId) {
      try {
        await apiClient.post('votes', {
          trip_item_id: hotelId
        });

      } catch (error) {
        console.error("Error upvoting:", error);
      } finally {
        this.isSubmitting = false;
      }
    }
  }
}
</script>
