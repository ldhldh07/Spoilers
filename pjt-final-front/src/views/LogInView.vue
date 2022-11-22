<template>
  <div class="d-flex flex-column align-items-center">
    <h1>로그인</h1>
    <form @submit.prevent="logIn">
      <!-- <label for="email">email : </label>
      <input type="email" id="email" v-model="email"><br> -->
      <label class="form-label" for="username">name : </label>
      <input class="form-control" type="text" id="username" v-model="username"><br>

      <label class="form-label" for="password"> password : </label>
      <input class="form-control" type="password" id="password" v-model="password"><br>

      <input class="btn btn-warning" type="submit" value="logIn">
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
