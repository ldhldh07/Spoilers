<template>
  <div id="app">
    <b-navbar type="dark" variant="primary">
      <b-navbar-brand>Spoilers</b-navbar-brand>

    </b-navbar>
    <!--
    <h2 v-if="isLogIn"> {{ user?.username }}님 안녕하세용</h2>
    <nav>
      <router-link to="/">인기순 보기</router-link> |
      <span v-if="!isLogIn" >
        <router-link :to="{ name: 'SignUpView', query: { next: fromName }  }">회원가입</router-link> | 
        <router-link :to="{ name: 'LogInView', query: { next: fromName } }">로그인</router-link> | 
      </span>
      <span v-else>
        <a href="#" @click="logOut">로그아웃</a> | 
      </span>
      <router-link to="/genre">장르별 보기</router-link> |
      <router-link to="/new">최신순 보기</router-link> |
    </nav> -->
    <router-view/>
  </div>
</template>
<script>
export default {
  data() {
    return {
    }
  },
  computed: {
    user() {
      return this.$store.state.user
    },
    isLogIn() {
      return this.$store.getters.isLogIn
    },
    fromName() {
      return this.$route.name
    }
  },
  methods: {
    logOut() {
      this.$store.commit('LOG_OUT')
    }
  },
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
