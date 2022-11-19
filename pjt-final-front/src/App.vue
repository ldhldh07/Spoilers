<template>
  <div id="app">
    <h1>Spoilers!</h1>
    <h2>{{ user.username }}님 안녕하세용</h2>
    <nav>
      <router-link to="/">인기순 보기</router-link> |
      <router-link :to="{ name: 'SignUpView' }">회원가입</router-link> | 
      <router-link :to="{ name: 'LogInView' }">로그인</router-link> | 
      <!-- 로그인되어 있으면 노출하되지 않음 -->
      <router-link to="/genre">장르별 보기</router-link> |
      <router-link to="/new">최신순 보기</router-link> |
    </nav>
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
    }
  }
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
