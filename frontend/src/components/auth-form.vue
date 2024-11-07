<template>
  <v-container class="d-flex flex-column justify-center align-center " fluid
               style="min-height: 100vh;">

    <v-img
        src="assets/logo_white.png"
        width="auto"
        max-width="150px"
        max-height="100px"
        height="100px"
        alt="Logo"

    ></v-img>


    <h1 class="text-center white--text">
      <span v-if="isLoginForm">Log into your account</span>
      <span v-else>Register new account</span>
    </h1>

    <v-card variant="flat" width="350px" class="pa-6 mt-5 rounded-shaped">

      <v-card-text class="mt-2">
        <v-form>
          <v-text-field
              class="mx-auto"
              density="compact"
              label="Email address"
              :rules="rules.emailRules"
              max-width="300"
              persistent-placeholder
              placeholder="email@gmail.com"
              prepend-inner-icon="mdi-email"
              variant="outlined"
              v-model="email"

          ></v-text-field>

          <v-text-field
              v-if="!isLoginForm"
              class="mx-auto"
              density="compact"
              label="Name"
              max-width="300"
              persistent-placeholder
              placeholder="Ivanov I."
              prepend-inner-icon="mdi-account"
              variant="outlined"
              v-model="name"

          ></v-text-field>

          <v-text-field
              class="mx-auto"
              density="compact"
              :rules="rules.passwordRules"
              max-width="300"
              persistent-placeholder
              prepend-inner-icon="mdi-onepassword"
              label="Password"
              variant="outlined"
              dense
              color="grey"
              type="password"
              v-model="password"
          ></v-text-field>

          <v-text-field
              v-if="!isLoginForm"
              :rules="rules.confirmPasswordRules"
              class="mx-auto"
              density="compact"
              max-width="300"
              persistent-placeholder
              prepend-inner-icon="mdi-onepassword"
              label="Confirm Password"
              variant="outlined"
              dense
              color="grey"
              type="password"
              v-model="confirmPassword"

          ></v-text-field>

          <v-row class="d-flex align-center justify-space-between mt-4">
            <v-checkbox label="Remember me" color="blue" v-model="rememberMe" hide-details></v-checkbox>
            <v-btn variant="plain" text color="primary" class="blue--text text-subtitle-1" @click="forgotPassword">
              Forgot
              password?
            </v-btn>
          </v-row>

          <v-btn :loading="isSubmitting" class="mt-4 mb-4" block color="blue" dark @click="submit">
            <span v-if="isLoginForm"> Log In </span>
            <span v-else>Register</span>
          </v-btn>

          <v-divider class="my-4"></v-divider>

          <v-row justify="center" class="mt-4">
            <p v-if="isLoginForm" class="white--text">Don't have an account?
              <v-btn variant="plain" text="Sign Up" color="blue" @click="toggleForm">Sign up</v-btn>
            </p>
            <p v-else class="white--text">Do have an account yet?
              <v-btn variant="plain" text="Sign Up" color="blue" @click="toggleForm">Log in</v-btn>
            </p>
          </v-row>
        </v-form>
      </v-card-text>


    </v-card>
  </v-container>
</template>

<script>
import apiClient from "@/api/axios";

export default {
  data() {
    return {
      email: '',
      name: '',
      password: '',
      confirmPassword: '',
      rememberMe: false,
      isLoginForm: true,
      isSubmitting: false,
      rules: {
        emailRules: [
          v => !!v || "E-mail is required",
          v => /.+@.+\..+/.test(v) || "E-mail must be valid"
        ],
        passwordRules: [
          v => !!v || "Password is required",
        ],
        confirmPasswordRules: [
          v => !!v || "Confirm Password is required",
          v => v === this.password || "Passwords do not match"
        ]
      }
    };
  },
  methods: {
    validate() {
      this.$refs.form.validate();
    },
    async submit() {
      this.isSubmitting = true;

      const endpoint = this.isLoginForm ? "auth/login" : "auth/register"

      try {

        const response = await apiClient.post(endpoint, {
          email: this.email,
          name: this.name,
          password: this.password,
        })

        this.$store.commit('setToken', response.data['access_token'])

        this.$router.push("/")


        console.log(response.data)
      } catch (e) {
        console.log("error on submit: ", e)
      }

      this.isSubmitting = false;
    },
    toggleForm() {
      // Логика перехода на страницу регистрации
      this.isLoginForm = !this.isLoginForm
    },
  },
};
</script>

<style scoped>


</style>


