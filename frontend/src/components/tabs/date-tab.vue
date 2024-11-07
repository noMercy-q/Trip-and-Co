<template>
<v-card class="ml-10 mb-10" width="400">
  <v-date-picker
    v-model="selectedDates"
    :min="minDate"
    :max="maxDate"
    multiple="range"
    width="400"
  >
    <template #title />
    <template #header>
        <div v-if="selectedDates[0]" class="ml-5">Starts on: {{ formatDate(selectedDates[0]) }}</div>
        <div v-if="selectedDates[1]" class="ml-5">Ends on: {{ formatDate(selectedDates[selectedDates.length-1]) }}</div>
    </template>
  </v-date-picker>
  <v-card-actions class="my-2 d-flex justify-end">
    <v-btn
      class="text-none"
      color="white"
      text="Submit"
      variant="flat"
      @click="$emit('next_tab')"
    ></v-btn>
  </v-card-actions>
</v-card> 
</template>

<script>
  // import axios from 'axios'
  import { format } from 'date-fns'

  export default {
    name: "DateTab",

    data: () => ({
      selectedDates: [],
      minDate: new Date(2024, 10, 5).toISOString(),
      maxDate: new Date(2024, 10, 28).toISOString(),
    }),

    methods: {
      formatDate(date) {
        return format(new Date(date), 'dd.MM.yyyy');
      },

      async saveDates() {

      }
    }
  }
</script>
