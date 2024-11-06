<template>
<v-card width="60%" class="ml-10">
  <v-img
    cover
    :src="hotel.imageUrl"
    class="align-end"
    height="300"
  >
  </v-img>
  <v-divider></v-divider>

  <v-card-text>
    <h2>Hotel</h2>
    <h3>{{ hotel.title }}</h3>
    <h3>{{ hotel.address }}</h3>

    
  </v-card-text>
  <v-card-text>
    <h2>Dates</h2>
    <h3>{{ formatDate(dates.min) + '-' + formatDate(dates.max) }}</h3>
  </v-card-text>

  <v-card-text>
    <h2>Approximate cost by person</h2>

    <h3>{{ price }}$</h3>
    <v-btn @click="getCities">Get cities</v-btn>
    <v-autocomplete
      variant="outlined"
      :items="cities"
    />
  </v-card-text>
</v-card>
</template>

<script>
  import axios from 'axios'
  import { format } from 'date-fns'

  export default {
    name: "SummaryTab",

    data: () => ({
      hotel: {
        id: 1,
        name: "ABCD",
        description: "test test test",
        address: "test test",
        imageUrl: "https://wallpapers.com/images/hd/pink-beach-aesthetic-yxkoq8kqlso6apb0.jpg"
      },
      dates: {
        min: "2024-11-05",
        max: "2024-11-15"
      },
      price: 1500
    }),

    methods: {
      formatDate(date) {
        return format(new Date(date), 'dd.MM.yyyy');
      },

      async getTopOptions() {
        
      }
    }
  }
</script>
  