<template>
  <v-card class="mx-auto rounded-xl" width="30%">
    <v-card-title class="text-h5 text-center">Create a New Trip</v-card-title>
    <v-card-text>
      <v-form ref="tripForm">

        <!-- Название путешествия -->
        <v-text-field
          :rules="rules.tripNameRules"
          label="Trip Name"
          density="compact"
          persistent-placeholder
          v-model="tripName"
          placeholder="Summer Adventure"
          prepend-inner-icon="mdi-map"
          variant="outlined"
          class="mb-4"
        ></v-text-field>

        <!-- Города отправления и прибытия на одной строке -->
        <v-row>
          <v-col cols="6">
            <v-autocomplete
              :items="cities"
              :rules="rules.cityRules"
              item-title="name"
              item-value="code"
              label="Departure City"
              density="compact"
              persistent-placeholder
              v-model="departureCityCode"
              placeholder="New York"
              prepend-inner-icon="mdi-city"
              variant="outlined"
            ></v-autocomplete>
          </v-col>
          <v-col cols="6">
            <v-autocomplete
              :items="cities"
              :rules="rules.cityRules"
              item-title="name"
              item-value="code"
              label="Destination City"
              v-model="destinationCityCode"
              density="compact"
              persistent-placeholder
              placeholder="Los Angeles"
              prepend-inner-icon="mdi-city-variant"
              variant="outlined"
            ></v-autocomplete>
          </v-col>
        </v-row>

        <!-- Даты вылета и прилета на одной строке -->
        <v-row>
          <v-col cols="6">
            <v-text-field
              label="Departure Date"
              v-model="startDate"
              density="compact"
              persistent-placeholder
              :rules="rules.dateRules"
              type="date"
              prepend-inner-icon="mdi-calendar"
              variant="outlined"
            ></v-text-field>
          </v-col>
          <v-col cols="6">
            <v-text-field
              label="Return Date"
              density="compact"
              persistent-placeholder
              v-model="endDate"
              :rules="rules.dateRules"
              type="date"
              prepend-inner-icon="mdi-calendar-end"
              variant="outlined"
            ></v-text-field>
          </v-col>
        </v-row>

      </v-form>
    </v-card-text>

    <v-card-actions>
      <v-btn class="text-none" density="comfortable" variant="outlined" color="white" @click="$emit('close')">Cancel</v-btn>
      <v-btn
        :loading="isSubmitting"
        class="text-none ma-2"
        density="comfortable"
        variant="flat"
        color="white"
        @click="submitTrip"
      >
        Create Trip
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import apiClient from '../api/axios';

export default {
  data() {

    const today = new Date(); // Форматируем текущую дату в ISO для input типа date
    const nextWeek = new Date();
    nextWeek.setDate(today.getDate() + 7)

    return {
      tripName: '',
      cities: [],
      departureCityCode: '',
      destinationCityCode: '',
      startDate: today.toISOString().slice(0, 10),
      endDate: nextWeek.toISOString().slice(0, 10),
      isSubmitting: false,
      rules: {
        tripNameRules: [v => !!v || "Trip name is required"],
        cityRules: [v => !!v || "City is required"],
        dateRules: [v => !!v || "Date is required"]
      }
    };
  },
  computed: {
    cityOptions() {
      return this.cities.map(city => city.name).sort();
    },
  },
  mounted() {
    this.fetchCities();
  },
  methods: {
    async fetchCities() {
      try {
        const response = await apiClient.get('cities')

        this.cities = response.data || [];
        console.log(this.cities)

      } catch (e) {
        console.log("error to fetch cities: ", e)
      }


    },
    async submitTrip() {
      this.isSubmitting = true;

      try {
        const { data } = await apiClient.post('create_trip', {
          name: this.tripName,
          origin_city_id: this.departureCityCode,
          dest_city_id: this.destinationCityCode,
          start_date: this.startDate,
          end_date: this.endDate,
        });


        this.$emit('close');
        this.$router.push({ name: 'TripDetail', params: { id: data.id } });

      } catch (error) {
        console.error("Error creating trip:", error);
      } finally {
        this.isSubmitting = false;
      }
    }
  }
};
</script>

<style scoped>
</style>
