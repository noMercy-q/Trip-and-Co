<template>
<div class="mt-10 ml-10">
  <div class="mb-10">
    <h3>ITMO super mega trip to Moscow 2024</h3>
  </div>
  <v-card round>
    <v-tabs
      v-model="tab" 
      align-tabs="start"
    >
      <v-tab :value="1">Dates</v-tab>
      <v-tab :value="2">Transportation</v-tab>
      <v-tab :value="3">Accomodation</v-tab>
      <v-tab :value="4">Summary</v-tab>
    </v-tabs>

    <v-tabs-window v-model="tab">
      <v-tabs-window-item
        v-for="n in 4"
        :key="n"
        :value="n"
      >
        <!-- <v-container v-if="tab==1"> -->
          <div v-if="tab==1">
            <v-sheet class="d-flex align-end flex-column" width="40%">      
              <v-date-picker
                v-model="selectedDates"
                :min="minDate"
                :max="maxDate"
                multiple="range"
                width="400"
                class="ml-10"
              >
                <template #title />
                <template #header>
                    <div v-if="selectedDates[0]" class="ml-5">Starts on: {{ formatDate(selectedDates[0]) }}</div>
                    <div v-if="selectedDates[1]" class="ml-5">Ends on: {{ formatDate(selectedDates[selectedDates.length-1]) }}</div>
                </template>
              </v-date-picker>
              <v-btn @click="tab++" class="mb-10" color="white">Submit</v-btn>
            </v-sheet>
          </div>


          <div v-else-if="tab==3">
            <v-sheet
              class="d-flex flex-row"
            >
              <v-sheet
                class="d-flex align-content-start flex-wrap bg-surface-variant"
                width="50%"
                min-height="200"
              >
                <v-sheet
                  v-for="n in 8"
                  :key="n"
                  class="ma-3 pa-2"
                >
                  <v-card text="Item" width="150" height="150"></v-card>
                </v-sheet>
              </v-sheet>

              <v-sheet class="d-flex flex-column" width="50%">
                <v-sheet class="d-flex">
                  <v-textarea label="Comment" variant="outlined" class="ml-10 mr-10" width="400"></v-textarea>
                </v-sheet>
              </v-sheet>
            </v-sheet>
          </div>
        <!-- </v-container> -->
        <v-card-text v-else v-text="text"></v-card-text>
      </v-tabs-window-item>
    </v-tabs-window>
  </v-card>
</div>
</template>

<script>
  import axios from 'axios'
  import { format } from 'date-fns'

  export default {
    data: () => ({
      text: 'Здесь уже становится красиво!',
      selectedDates: [],
      tab: 3,
      minDate: new Date(2024, 10, 5).toISOString(),
      maxDate: new Date(2024, 10, 28).toISOString()
    }),

    methods: {
      async handleNewMessage() {
        try {
          const response =
            await axios.post('our url', { })
          console.log(response)
        } catch (error) {
          this.error = error
        }
      }, 
      formatDate(date) {
        console.log(date)
        return format(new Date(date), 'dd.MM.yyyy');
      }
    }
  }
</script>
  