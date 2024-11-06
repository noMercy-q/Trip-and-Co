<template>
<div>
  <v-sheet
    class="d-flex flex-row ma-10"
  >
    <v-sheet class="d-flex flex-column ml-10" width="60%">
      <v-sheet
        class="d-flex align-content-start flex-wrap"
        min-height="200"
      >
        <v-sheet
          v-for="view in views"
          :key="view.id"
          class="ma-3"
        >
          <v-card width="450" height="250" class="rounded-xl" variant="outlined">
            <v-card-title>{{ view.title }}</v-card-title>
            <v-card-text>
              <div>{{ view.description }}</div>
            </v-card-text>

            <v-card-actions class="d-flex align-end ma-2">
              <v-btn color="white" text="Upvote" />
            </v-card-actions>
          </v-card>
        </v-sheet>
      </v-sheet>
      <v-sheet>
        <v-card-actions class="my-2 d-flex align-end">
          <v-btn
            variant="outlined"
            color="white"
            text="Suggest a place"
            @click="showDialog = true"
          />
          <v-btn
            variant="flat"
            color="white"
            text="Submit"
            @click="tab++"
          />
        </v-card-actions>
      </v-sheet>  
    </v-sheet>
    
    <comments-section :comments="comments"/>
  </v-sheet>
</div>
</template>

<script>
  import axios from 'axios'
  import CommentsSection from '../comments-section'

  export default {
    name: "ViewsTab",
    components: { CommentsSection },

    data: () => ({
      showDialog: false,
      views: [
        {
          id: 1,
          title: "Go to the theatre",
          description: "orem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lore"
        },
        {
          id: 1,
          title: "Go to the theatre",
          description: "orem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lore"
        },
        {
          id: 2,
          title: "Go to the theatre",
          description: "orem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lore"
        },
        {
          id: 3,
          title: "Go to the theatre",
          description: "orem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lore"
        },
        {
          id: 4,
          title: "Go to the theatre",
          description: "orem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lore"
        },
        {
          id: 5,
          title: "Go to the theatre",
          description: "orem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lore"
        },
        {
          id: 6,
          title: "Go to the theatre",
          description: "orem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lore"
        },
        {
          id: 7,
          title: "Go to the theatre",
          description: "orem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lore"
        },
        
      ],

      comments: [
        { id: 1, author: "Kate", text: "lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum" },
        { id: 2, author: "Max", text: "lorem ipsum lorem ipsum lorem ipsum lorem lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum" },
        { id: 3, author: "Denis", text: "lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum" }
      ],
    }),

    methods: {
      async getViews() {

      }
    }
  }
</script>
