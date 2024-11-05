<template>
  <div class="mt-10 ml-10">
    <v-sheet class="mx-left" width="50%">
      <v-card>
        <template #text>{{ text }}</template>
      </v-card>
    </v-sheet>
  </div>
  </template>
  
  <script>
    import axios from 'axios'
  
    export default {
      data: () => ({
        text: 'Скоро здесь будет красиво!'
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
        }
      }
    }
  </script>
  