<template>
<v-sheet class="d-flex flex-column ml-10 mr-10" width="40%">
  <h2 class="mb-10">Discussion</h2>
  <v-sheet v-for="comment in comments" :key="comment.id">
    <v-card
      variant="outlined"
      class="mb-5 pa-5"
    >
      <h3>{{ comment.author }}</h3>
      <div>{{ comment.text }}</div>
    </v-card>
  </v-sheet>
  <v-textarea
    label="Comment"
    variant="outlined"
    density="compact"
  />
</v-sheet>
</template>

<script>

export default {
  name: "HotelCard",
  
  props: {
    comments: Array
  }
}
</script>
