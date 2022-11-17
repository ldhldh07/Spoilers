<template>
  <div class="genre">
    <h1>장르별 보기</h1>
    <p>장르를 골라주세요</p>
    <div class="container">
      <router-link to="/genre/로맨스">
        <div class="genre-box">
          로맨스
        </div>
      </router-link>
      <router-link to="/genre/액션">
        <div class="genre-box">
          액션
        </div>
      </router-link>
      <router-link to="/genre/미스터리">
        <div class="genre-box">
          미스터리
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
  import MovieList from '@/components/MovieList'

  export default {
  name: 'GenreSelectView',
  components: {
      MovieList,
  },
  data : function() {
      return {
      genre: null
      }
  },
  }
</script>

<style>
.genre-box {
  border: 5px solid black;
}
</style>