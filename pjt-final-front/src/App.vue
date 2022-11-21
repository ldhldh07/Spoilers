<template>
  <div id="app">
    <b-navbar fixed="top" type="dark" id="bar">
      <b-navbar-brand id="title" to="/home">Spoilers</b-navbar-brand>
      <b-navbar-nav>
        <b-nav-item to="/home">인기</b-nav-item>
        <b-nav-item to="/new">최신</b-nav-item>
        <b-nav-item to="/genre">장르</b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav v-if="!isLogIn" class="ms-auto">
        <b-nav-item :to="{ name: 'LogInView', query: { next: fromName } }" >로그인</b-nav-item>
        <b-nav-item :to="{ name: 'SignUpView', query: { next: fromName } }" >회원가입</b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav v-else class="ms-auto">
        <a href="#" @click="logOut">로그아웃</a>
      </b-navbar-nav>
    </b-navbar>
    <b-modal ref="logout" hide-footer hide-header-close title="로그아웃">
      <p class="my-4">성공적으로 로그아웃 되었습니다.</p>
    </b-modal>
    <router-view id="content"/>
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
      this.$refs['logout'].show()
      this.$store.commit('LOG_OUT')
    }
  },
}
</script>

<style>
@font-face {
  font-family: 'SUIT-Medium';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_suit@1.0/SUIT-Medium.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: 'PyeongChangPeace-Bold';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2206-02@1.0/PyeongChangPeace-Bold.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
}

#title {
  font-family: 'PyeongChangPeace-Bold';
}

#app {
  font-family: 'SUIT-Medium';
  text-align: left;
  padding-left: 4rem;
  padding-right: 4rem;
  color: #333d51;
  background: #eef2f3;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to top, #8e9eab, #eef2f3);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to top, #8e9eab, #eef2f3); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  background-size: cover;
  background-attachment: fixed;
}

#bar {
  background-color: #333d51;
  padding-left: 4rem;
  padding-right: 4rem;
}

.navbar-dark .navbar-nav .nav-link{
  color:#d3ac2b !important
}

.navbar-dark .navbar-nav a{
  text-decoration: none;
  color:#d3ac2b !important
}

.navbar-dark .navbar-nav .nav-link.router-link-active{
  color: #f4f3ea !important;
}

.navbar-dark .navbar-brand {
  color:#d3ac2b !important ;
}

#content{
  padding-top: 100px;
}
</style>
