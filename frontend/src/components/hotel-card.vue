<template>
<v-card width="400" height="400" class="rounded-xl" variant="outlined">
  <v-img
    cover
    :src="imageUrl"
    class="align-end"
    height="200"
  >
    <v-card-title>{{ title }}</v-card-title>
  </v-img>
  <v-card-subtitle class="pt-4">
    {{ title }}
  </v-card-subtitle>

  <v-card-text>
    <div>{{ title }}</div>
    <div>{{ description }}</div>
    <div>{{ address }}</div>
  </v-card-text>

  <v-card-actions>
    <v-btn color="orange" text="Upvote" />
  </v-card-actions>
</v-card>
</template>

<script>

export default {
  name: "HotelCard",
  
  props: {
    imageUrl: String,
    title: String,
    address: String,
    description: String,
    price: Number
  }
}
</script>
