<template>
  <div class="popular">
    <h1>인기순 보기</h1>
    <MovieList
      :genre="popular"
    />
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'

export default {
  name: 'PopularView',
  components: {
    MovieList,
  },
  created() {
    this.getMovies()
  },
  data: function() {
    return {
      popular: 10
      // 타 장르값과 겹치지 않도록 한다.
    }
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  }

}
</script>
