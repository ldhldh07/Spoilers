<template>
  <div class="genre">
    <h1>장르별 보기</h1>
    <p>장르를 골라주세요</p>
    <div class="container d-flex justify-content flex-wrap">
      <div class="genre-box"
      v-for="genre in genres"
      :key="genre.id">
        <router-link :to="{name:'GenreView', params:{genre:genre.name,code:String(genre.id)}}">        
          {{genre.name}}
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'GenreSelectView',
  created() {
    this.getGenres()
  },
  methods: {
    getGenres() {
      this.$store.dispatch('getGenres')
    }
  },
  computed: {
    genres() {
      const array = this.$store.state.genres
      return array
    }
  }
}
</script>

<style>
.genre-box {
  border: 1px solid black;
  width: 150px;
  margin-top: 10px;
  margin-left: 60px;
  margin-bottom: 20px;
}
</style>

