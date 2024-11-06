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
          <div v-if="tab==1">
            <v-sheet class="d-flex align-end flex-column" width="40%" min-height="800">      
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
              <v-btn @click="tab++" class="mb-10" color="white">Submit</v-btn>
            </v-sheet>
          </div>

          <div v-else-if="tab==3">
            <v-sheet
              class="d-flex flex-row ma-10"
            >
              <v-sheet
                class="d-flex align-content-start flex-wrap"
                width="60%"
                min-height="200"
              >
                <v-sheet
                  v-for="n in 8"
                  :key="n"
                  class="ma-3"
                >
                  <hotel-card 
                    :title="'Hotel #' + n"
                    :price="n * 1500"
                    address="Moscow, Bolshaya Baumanskaya, 18"
                    description="lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum"
                    imageUrl="https://www.ahstatic.com/photos/a596_ho_00_p_2048x1536.jpg"
                  />
                </v-sheet>
              </v-sheet>
              
              <comments-section :comments="comments"/>
            </v-sheet>
          </div>
        <v-card-text v-else v-text="text"></v-card-text>
      </v-tabs-window-item>
    </v-tabs-window>
  </v-card>
</div>
</template>

<script>
  import axios from 'axios'
  import { format } from 'date-fns'
  import HotelCard from './hotel-card'
  import CommentsSection from './comments-section'

  export default {
    components: {
      HotelCard,
      CommentsSection
    },

    data: () => ({
      text: 'Soon',
      selectedDates: [],
      tab: 3,
      minDate: new Date(2024, 10, 5).toISOString(),
      maxDate: new Date(2024, 10, 28).toISOString(),

      comments: [
        { id: 1, author: "Kate", text: "lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum" },
        { id: 2, author: "Max", text: "lorem ipsum lorem ipsum lorem ipsum lorem lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum" },
        { id: 3, author: "Denis", text: "lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum" }
      ]
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
        return format(new Date(date), 'dd.MM.yyyy');
      }
    }
  }
</script>
  