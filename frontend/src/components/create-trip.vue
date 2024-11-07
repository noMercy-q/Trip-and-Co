<template>
  <v-card class="mx-auto rounded-xl" width="30%">
    <v-card-title class="text-h5 text-center">Create a New Trip</v-card-title>
    <v-card-text>
      <v-form ref="tripForm">

        <!-- Название путешествия -->
        <v-text-field
            label="Trip Name"
            density="compact"
            persistent-placeholder
            v-model="tripName"
            :rules="rules.tripNameRules"
            placeholder="Summer Adventure"
            prepend-inner-icon="mdi-map"
            variant="outlined"
            class="mb-4"
        ></v-text-field>

        <!-- Города отправления и прибытия на одной строке -->
        <v-row>
          <v-col cols="6">
            <v-autocomplete
                :items="cityOptions"
                label="Departure City"
                density="compact"
                persistent-placeholder
                v-model="departureCity"
                :rules="rules.cityRules"
                placeholder="New York"
                prepend-inner-icon="mdi-city"
                variant="outlined"
            ></v-autocomplete>
          </v-col>
          <v-col cols="6">
            <v-autocomplete
                :items="cityOptions"
                label="Destination City"
                v-model="destinationCity"
                density="compact"
                persistent-placeholder
                :rules="rules.cityRules"
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
      <v-btn class="text-none ma-2" density="comfortable" variant="flat" color="white" @click="submitTrip"
             :loading="isSubmitting">Create
        Trip
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from "axios";

export default {
  data() {

    const today = new Date(); // Форматируем текущую дату в ISO для input типа date
    const nextWeek = new Date();
    nextWeek.setDate(today.getDate() + 7)

    return {
      tripName: '',
      cities: [],
      departureCity: '',
      destinationCity: '',
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
      const endpoint = "http://localhost:8000/cities"

      try {
        const response = await axios.get(endpoint)

        this.cities = response.data || [];

      } catch (e) {
        console.log("error to fetch cities: ", e)
      }


    },
    async submitTrip() {
      this.isSubmitting = true;

      try {
        // Отправка данных формы
        const endpoint = "http://localhost:8000/create_trip"
        const response = await axios.post(endpoint, {
          name: this.tripName,
          departureCity: this.departureCity,
          destinationCity: this.destinationCity,
          startDate: this.startDate,
          endDate: this.endDate,
        });

        console.log("Trip created:", response.data);

        // Закрыть диалоговое окно после успешного создания
        this.$emit('close');
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
