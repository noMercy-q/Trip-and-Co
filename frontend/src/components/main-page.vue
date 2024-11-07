<template>
<div class="mt-10 ml-10">
  <div class="mb-10">
    <h3>ITMO super mega trip to Moscow 2024</h3>
  </div>
  <v-card rounded="lg" width="80%" class="align-center">
    <v-tabs
      v-model="tab" 
      align-tabs="start"
    >
      <v-tab :value="1">Dates</v-tab>
      <v-tab :value="2">Accomodation</v-tab>
      <v-tab :value="3">Places to visit</v-tab>
      <v-tab :value="4">Summary</v-tab>
    </v-tabs>

    <v-tabs-window v-model="tab">
      <v-card-title class="ml-10 mt-5"><h2>{{ tabTitle }}</h2></v-card-title>
      <v-tabs-window-item
        v-for="n in 4"
        :key="n"
        :value="n"
      >
        <div v-if="tab==1">
          <date-tab @next_tab="tab++" />
        </div>

        <div v-else-if="tab==2">
          <accomodation-tab @next_tab="tab++" />
        </div>

        <div v-else-if="tab==3">
          <views-tab @next_tab="tab++" />
        </div>

        <div v-else-if="tab==4">
          <summary-tab />
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
  import DateTab from './tabs/date-tab'
  import AccomodationTab from './tabs/accomodation-tab'
  import ViewsTab from './tabs/views-tab'
  import SummaryTab from './tabs/summary-tab'

  export default {
    components: {
      DateTab,
      AccomodationTab,
      ViewsTab,
      SummaryTab
    },

    data: () => ({
      text: 'Soon',
      selectedDates: [],
      tab: 4,
      minDate: new Date(2024, 10, 5).toISOString(),
      maxDate: new Date(2024, 10, 28).toISOString(),
      cities: []
    }),

    computed: {
      tabTitle() {
        if (this.tab == 1) return "Select dates of your journey"
        if (this.tab == 2) return "Vote suggested accomodation options"
        if (this.tab == 3) return "Vote suggested places to visit"
        if (this.tab == 4) return "Here is the most popular combination. Have a nice trip!"

        return "Ghost tab"
      }
    },

    methods: {
      async getCities() {
        try {
          const { data } = await axios.get('http://0.0.0.0:8000/cities', { trip_id: 1 })
          console.log(data)
          this.cities = data.flat()
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
