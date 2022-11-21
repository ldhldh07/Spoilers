<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="logIn">
      <!-- <label for="email">email : </label>
      <input type="email" id="email" v-model="email"><br> -->
      <label for="username">name : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="logIn">
    </form>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      // email: null,
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      // const email = this.email
      const username = this.username
      const password = this.password
      const next = this.$route.query.next

      const payload = {
        // email,
        username,
        password,
        next,
      }
      this.$store.dispatch('logIn', payload)
    }
  }
}
</script>
