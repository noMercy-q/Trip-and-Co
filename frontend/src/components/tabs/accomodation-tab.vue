<template>
<div>
  <v-card>
    <v-sheet
      class="d-flex flex-row ma-10"
    >
      <v-sheet class="d-flex flex-column mr-10" width="60%">
        <v-sheet
          class="d-flex justify-space-between flex-wrap"
          min-height="200"
        >
          <v-sheet
            v-for="hotel in hotels"
            :key="hotel.id"
            class="ma-3"
          >
            <hotel-card :hotel="hotel"/>
          </v-sheet>
        </v-sheet>
        <v-sheet>
          <v-card-actions class="my-2 d-flex justify-end">
            <v-btn
              variant="outlined"
              color="white"
              text="Suggest an accomodation"
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
  </v-card> 

  <v-dialog
    v-model="showDialog"
    width="500"
  >
    <v-card rounded="lg">
      <v-card-title class="d-flex justify-space-between align-center">
        <div class="text-h5 text-medium-emphasis ps-2">
          Suggest an accomodation option
        </div>

        <v-btn
          icon="mdi-close"
          variant="text"
          @click="showDialog = false"
        ></v-btn>
      </v-card-title>

      <v-divider class="mt-2"></v-divider>

      <v-card-text>
        <v-text-field
          v-model="newHotel.name"
          class="mb-2"
          variant="outlined"
          label="Title"
        />
        <v-textarea
          v-model="newHotel.description"
          :counter="300"
          class="mb-2"
          rows="2"
          variant="outlined"
          label="Description"
          persistent-counter
        />
        <v-text-field
          v-model="newHotel.imageUrl"
          class="mb-2"
          variant="outlined"
          label="Title"
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
          @click="createHotel"
        ></v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</div>
</template>

<script>
  import apiClient from '../../api/axios'
  import HotelCard from '../hotel-card'
  import CommentsSection from '../comments-section'

  export default {
    name: "AccomodationTab",
    components: {
      HotelCard,
      CommentsSection
    },

    data: () => ({
      showDialog: false,
      newHotel: {},
      hotels: [
        {
          id: 1,
          title: "Test hotel",
          description: "test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test",
          address: "Test address address address address",
          imageUrl: "https://i.ytimg.com/vi/KlVTk6-jbq8/maxresdefault.jpg"
        },
        {
          id: 2,
          title: "Test hotel",
          description: "test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test",
          address: "Test address address address address",
          imageUrl: "https://i.ytimg.com/vi/KlVTk6-jbq8/maxresdefault.jpg"
        },
        {
          id: 3,
          title: "Test hotel",
          description: "test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test",
          address: "Test address address address address",
          imageUrl: "https://i.ytimg.com/vi/KlVTk6-jbq8/maxresdefault.jpg"
        },
        {
          id: 4,
          title: "Test hotel",
          description: "test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test",
          address: "Test address address address address",
          imageUrl: "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/14/45/e2/8e/piscina-de-dia.jpg?w=1200&h=-1&s=1"
        },
        {
          id: 5,
          title: "Test hotel",
          description: "test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test",
          address: "Test address address address address",
          imageUrl: "https://static.independent.co.uk/s3fs-public/thumbnails/image/2019/04/10/15/luxwawlcex-126117-hotel-bristol-warsaw-high1.jpg"
        },
        {
          id: 6,
          title: "Test hotel",
          description: "test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test",
          address: "Test address address address address",
          imageUrl: "https://www.ahstatic.com/photos/a596_ho_00_p_2048x1536.jpg"
        },
        {
          id: 7,
          title: "Test hotel",
          description: "test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test",
          address: "Test address address address address",
          imageUrl: "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Hotel_Bristol_w_Warszawie.JPG/1200px-Hotel_Bristol_w_Warszawie.JPG"
        },
        {
          id: 8,
          title: "Test hotel",
          description: "test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test",
          address: "Test address address address address",
          imageUrl: "https://cdnn21.img.ria.ru/images/151472/35/1514723511_0:546:5244:3495_1920x0_80_0_0_b2e21246367c8a57294b5974a7809512.jpg"
        },
        {
          id: 9,
          title: "Test hotel",
          description: "test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test",
          address: "Test address address address address",
          imageUrl: "https://tophotels.ru/icache/hotel_photos/74/10360/31895/1125022_740x550.jpg"
        }
      ],

      comments: [
        { id: 1, author: "Kate", text: "lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum" },
        { id: 2, author: "Max", text: "lorem ipsum lorem ipsum lorem ipsum lorem lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum" },
        { id: 3, author: "Denis", text: "lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum" }
      ],
    }),

    created() {
      this.getHotels()
    },

    methods: {
      async getHotels() {
        try {
          const { data } = await apiClient.get("/hotels", { params: { trip_id: this.$route.params.id } });

          console.log(data)
          this.hotels = data
          this.$emit('close');
        } catch (error) {
          console.error("Error getting hotels:", error);
        } finally {
          this.isSubmitting = false;
        }
      },

      async createHotel() {
        try {
          await apiClient.post("create_view", {
            trip_id: this.$route.params.id,
            type: 'hotel',
            name: this.newHotel.name,
            description: this.newHotel.description,
            image_url: this.newHotel.imageUrl
          });

          this.hotels.push(this.newHotel)
          this.newHotel = {}

        } catch (error) {
          console.error("Error creating hotel:", error);
        } finally {
          this.showDialog = false;
        }
      }
    }
  }
</script>
