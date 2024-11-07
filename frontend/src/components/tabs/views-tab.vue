<template>
<div>
  <v-sheet
    class="d-flex flex-row ma-10"
  >
    <v-sheet class="d-flex flex-column mr-10" width="60%">
      <v-sheet
        class="d-flex justify-space-between flex-wrap"
        min-height="200"
      >
        <v-sheet
          v-for="view in views"
          :key="view.id"
          class="ma-3"
        >
          <v-card width="470" min-height="100" class="rounded-xl" variant="outlined">
            <v-card-title>{{ view.name }}</v-card-title>
            <v-card-text>
              <div>{{ view.description }}</div>
            </v-card-text>

            <v-card-actions class="d-flex justify-end ma-2">
              <v-btn color="white" text="Upvote" />
            </v-card-actions>
          </v-card>
        </v-sheet>
      </v-sheet>
      <v-sheet>
        <v-card-actions class="my-2 d-flex justify-end">
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
            @click="$emit('next_tab')"
          />
        </v-card-actions>
      </v-sheet>  
    </v-sheet>
    
    <comments-section :comments="comments"/>
  </v-sheet>

  <v-dialog
    v-model="showDialog"
    width="500"
  >
    <v-card rounded="lg">
      <v-card-title class="d-flex justify-space-between align-center">
        <div class="text-h5 text-medium-emphasis ps-2">
          Suggest a place to visit
        </div>

        <v-btn
          icon="mdi-close"
          variant="text"
          @click="showDialog = false"
        ></v-btn>
      </v-card-title>

      <v-divider class="mt-2" />

      <v-card-text>
        <v-text-field
          v-model="newView.name"
          class="mb-2"
          variant="outlined"
          label="Title"
        />
        <v-textarea
          v-model="newView.description"
          :counter="300"
          class="mb-2"
          rows="2"
          variant="outlined"
          label="Description"
          persistent-counter
        />
      </v-card-text>

      <v-card-actions class="my-2 d-flex justify-end">
        <v-btn
          class="text-none"
          variant="outlined"
          text="Cancel"
          @click="showDialog = false"
        ></v-btn>

        <v-btn
          class="text-none"
          color="white"
          text="Suggest"
          variant="flat"
          @click="createView"
        ></v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</div>
</template>

<script>
  import apiClient from '../../api/axios'
  import CommentsSection from '../comments-section'

  export default {
    name: "ViewsTab",
    components: { CommentsSection },

    data: () => ({
      showDialog: false,
      newView: {
        name: '',
        description: ''
      },
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
          description: "orem ipsum lorem ipsum lorem ipsum lorem ipsum loremorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem orem ipsum lorem ipsum lorem ipsum lorem ipsorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem orem ipsum lorem ipsum lorem ipsum lorem ipsum lorem orem ipsum lorem ipsum lorem ipsum lorem ipsum lorem orem ipsum lorem ipsum lorem ipsum lorem ipsum lorem orem ipsum lorem ipsum lorem ipsum lorem ipsum lorem um lorem orem ipsum lorem ipsum lorem ipsum lorem ipsum lorem  ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lore"
        },
        {
          id: 4,
          title: "Go to the theatre",
          description: "orem ipsuorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem orem ipsum lorem ipsum lorem ipsum lorem ipsum lorem orem ipsum lorem ipsum lorem ipsum lorem ipsum lorem orem ipsum lorem ipsum lorem ipsum lorem ipsum lorem orem ipsum lorem ipsum lorem ipsum lorem ipsum lorem m lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lore"
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

    computed: {
      tripId() {
        return this.$route.params.id
      }
    },

    created() {
      this.getViews()
    },

    methods: {
      async getViews() {
        try {
          const { data } = await apiClient.get("/views", { params: { trip_id: this.$route.params.id } });

          console.log(data)
          this.views = data
          this.$emit('close');
        } catch (error) {
          console.error("Error getting views:", error);
        } finally {
          this.isSubmitting = false;
        }
      },

      async createView() {
        try {
          await apiClient.post("create_view", {
            trip_id: this.$route.params.id,
            type: 'view',
            name: this.newView.name,
            description: this.newView.description
          });

          this.views.push(this.newView)
          this.newView = {}

        } catch (error) {
          console.error("Error creating view:", error);
        } finally {
          this.showDialog = false;
        }
      }
    }
  }
</script>
